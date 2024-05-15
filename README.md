# SonarSource GitHub Action for Build failure notifications

![GitHub Release](https://img.shields.io/github/v/release/SonarSource/gh-action_gh-action_build-notify)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=SonarSource_gh-action_build-notify&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=SonarSource_gh-action_build-notify)

Get notified for CircleCI/SonarCloud/SonarQube build failures on Slack.

### Supported platforms
Notifications will be triggered upon build failures in any of the following platforms

* SonarCloud
* SonarQube-Next
* CirrusCI

### Enabled branches
Slack notifications will be enabled only for builds in the following branches

* master
* main
* dogfood-*
* branch-*

## Usage

Create a new GitHub workflow:

```yaml
# .github/workflows/slack_notify.yml
---
name: Slack Notifications
on:
 check_run:
  types: [rerequested, completed]

jobs:
 slack-notifications:
  permissions:
   id-token: write  # to authenticate via OIDC
  uses: SonarSource/gh-action_build-notify/.github/workflows/main.yaml@v1
  with:
    slackChannel: <your_slack_channel>

```

## Options

| Option name     | Description                                                        | Default                   |
|-----------------|--------------------------------------------------------------------|---------------------------|
| `slackChannel`   | Name of the slack channel where the notifications are to be sent | `build` |

## Versioning

This project is using [Semantic Versioning](https://semver.org/).

Branches prefixed with a `v` are pointers to the last major versions, ie: [`v1`](https://github.com/SonarSource/gh-action_build-notify/tree/v1).

> Note: the `master` branch is used for development and can not be referenced directly. Use a `v` branch or a tag instead.
