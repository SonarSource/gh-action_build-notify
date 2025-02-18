# SonarSource GitHub Action for Build failure notifications

![GitHub Release](https://img.shields.io/github/v/release/SonarSource/gh-action_build-notify)

It sends Slack notifications for failed GitHub Checks reported by the Cirrus CI, SonarCloud, SonarQube, and AzureDevops apps.

## Supported platforms

Notifications will be triggered upon build failures in any of the following platforms

- SonarCloud
- SonarQube-Next
- CirrusCI
- Azure Pipelines

## Enabled branches

Slack notifications will be enabled only for builds in the following branches

- master
- main
- dogfood-\*
- branch-\*

## Requirements

The repository needs to be onboarded to [Vault](https://xtranet-sonarsource.atlassian.net/wiki/spaces/RE/pages/2466316312/HashiCorp+Vault#Onboarding-a-Repository-on-Vault).

### Required permissions

```yaml
development/kv/data/slack
```

## Usage

Create a new GitHub workflow:

```yaml
# .github/workflows/slack_notify.yml
---
name: Slack Notifications
on:
  check_suite:
    types: [completed]

jobs:
  slack-notifications:
    permissions:
      contents: read
      checks: read
      id-token: write # to authenticate via OIDC
    uses: SonarSource/gh-action_build-notify/.github/workflows/main.yaml@v2
    with:
      slackChannel: <your_slack_channel>
```

> WARNING
> This workflow has to be merged into the default branch before being able to be used.
> There is a limitation (or a security feature) from GitHub. Workflows which are triggered
> based on check_run have to be merged to the default branch.

## Options

| Option name    | Description                                                                                                                                              | Default                 |
| -------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------- |
| `slackChannel` | Name of the slack channel where the notifications are to be sent.                                                                                         | `build`                 |
| `environment`  | Name of the GitHub Environment to use. Required if your repository uses GitHub Environments with a modified OIDC sub claim. Set to `slack` in this case. | Do not use environments |

## Versioning

This project is using [Semantic Versioning](https://semver.org/).

Branches prefixed with a `v` are pointers to the last major versions, ie: [`v1`](https://github.com/SonarSource/gh-action_build-notify/tree/v1).

> Note: the `master` branch is used for development and can not be referenced directly. Use a `v` branch or a tag instead.

## Releases

To create a new release,

1. Draft a new release from Github releases page with the next semantic version.
2. Run `scripts/updatevbranch.sh <tag>` with the release version tag to update the v\* branch with the new tag.
