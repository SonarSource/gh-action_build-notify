import os
import json
from github import Github

def set_github_env(key, value):
    """Sets a GitHub Actions environment variable."""
    with open(os.environ['GITHUB_ENV'], 'a') as f:
        f.write(f"{key}={value}\n")

def get_github_event():
    """Retrieves the GitHub Actions event data."""
    with open(os.environ['GITHUB_EVENT_PATH'], 'r') as f:
        return json.load(f)

def main():
    event = get_github_event()
    event_name = os.environ['GITHUB_EVENT_NAME']
    repository = os.environ['GITHUB_REPOSITORY']
    github_token = os.environ['GITHUB_TOKEN'] # Ensure GITHUB_TOKEN is available

    g = Github(github_token)
    repo = g.get_repo(repository)

    if event_name == "check_run":
        check_run = event['check_run']
        set_github_env("event_type", "check_run")
        set_github_env("app_name", check_run['app']['name'])
        set_github_env("details_url", check_run['details_url'])
        set_github_env("run_name", check_run['name'])
        set_github_env("conclusion", check_run['conclusion'])
        set_github_env("head_branch", check_run['check_suite']['head_branch'])
        set_github_env("head_sha", check_run['head_sha'])
        set_github_env("avatar_url", check_run['app']['owner']['avatar_url'])
        set_github_env("check_suite_id", check_run['check_suite']['id'])
    else:
        check_suite_id = event['check_suite']['id']
        print(f"Retrieving failed check runs for check suite ID: {check_suite_id}")

        try:
            check_runs = repo.get_check_suite(check_suite_id).get_check_runs()
            failed_check_runs = [run for run in check_runs if run.conclusion == "failure"]

            if failed_check_runs:
                failed_check_run = failed_check_runs[0]
                print(f"Extract fields for check-run: {failed_check_run.name}")

                set_github_env("app_name", failed_check_run.app.name)
                set_github_env("details_url", failed_check_run.details_url)
                set_github_env("run_name", failed_check_run.name)
                set_github_env("conclusion", failed_check_run.conclusion)
                set_github_env("head_branch", event['check_suite']['head_branch'])
                set_github_env("head_sha", failed_check_run.head_sha)
                set_github_env("avatar_url", failed_check_run.app.owner.avatar_url)
                set_github_env("check_suite_id", failed_check_run.check_suite.id)
            else:
                print("No failed check runs found.")

        except Exception as e:
            print(f"Error processing check runs: {e}")

if __name__ == "__main__":
    main()
