Amazon CodeCatalyst will no longer be open to new customers starting on November
7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For
more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Examples: Triggers in workflows

The following examples show how to add different types of triggers in an Amazon CodeCatalyst
workflow definition file.

For more information about triggers, see [Starting a workflow run automatically using
triggers](workflows-add-trigger.md "workflows-add-trigger.md").

###### Topics

- [Example: A simple code
  push trigger](#workflows-add-trigger-examples-push-simple "#workflows-add-trigger-examples-push-simple")
- [Example: A simple 'push
  to main' trigger](#workflows-add-trigger-examples-push-main "#workflows-add-trigger-examples-push-main")
- [Example: A simple pull
  request trigger](#workflows-add-trigger-examples-pull-simple "#workflows-add-trigger-examples-pull-simple")
- [Example: A simple
  schedule trigger](#workflows-add-trigger-examples-schedule-simple "#workflows-add-trigger-examples-schedule-simple")
- [Example: A
  trigger with a schedule and branches](#workflows-add-trigger-examples-schedule-branches "#workflows-add-trigger-examples-schedule-branches")
- [Example: A
  trigger with a schedule, a push, and branches](#workflows-add-trigger-examples-schedule-push-branches "#workflows-add-trigger-examples-schedule-push-branches")
- [Example: A trigger
  with a pull and branches](#workflows-add-trigger-examples-pull-branches "#workflows-add-trigger-examples-pull-branches")
- [Example: A trigger
  with a pull, branches, and a 'CLOSED' event](#workflows-add-trigger-examples-push-pull-close "#workflows-add-trigger-examples-push-pull-close")
- [Example: A trigger with
  a push, branches, and files](#workflows-add-trigger-examples-push-multi "#workflows-add-trigger-examples-push-multi")
- [Example: A manual
  trigger](#workflows-add-trigger-examples-manual "#workflows-add-trigger-examples-manual")
- [Example: Triggers in a CI/CD
  multi-workflow setup](#workflows-add-trigger-usecases "#workflows-add-trigger-usecases")

## Example: A simple code

push trigger

The following example shows a trigger that starts a workflow run whenever code is
pushed to _any_ branch in your source repository.

When this trigger is activated, CodeCatalyst starts a workflow run using the files in
the branch that you're pushing _to_ (that is, the destination
branch).

For example, if you push a commit to `main`, CodeCatalyst starts a workflow
run using the workfow definition file and other source files on
`main`.

As another example, if you push a commit to `feature-branch-123`,
CodeCatalyst starts a workflow run using the workfow definition file and other source
files on `feature-branch-123`.

```
Triggers:
  - Type: PUSH
```

###### Note

If you want a workflow run to start only when you push to `main`,
see [Example: A simple 'push
to main' trigger](#workflows-add-trigger-examples-push-main "#workflows-add-trigger-examples-push-main").

## Example: A simple 'push

to main' trigger

The following example shows a trigger that starts a workflow run whenever code is
pushed to the `main` branch—and _only_ the
`main` branch—in your source repository.

```
Triggers:
  - Type: PUSH
    Branches:
      - main
```

## Example: A simple pull

request trigger

The following example shows a trigger that starts a workflow run whenever a pull
request is created or revised in your source repository.

When this trigger is activated, CodeCatalyst starts a workflow run using the workflow
definition file and other source files in the branch that you're pulling
_from_ (that is, the source branch).

For example, if you create a pull request with a source branch called
`feature-123` and a destination branch called `main`,
CodeCatalyst starts a workflow run using the workfow definition file and other source
files on `feature-123`.

```
Triggers:
  - Type: PULLREQUEST
    Events:
      - OPEN
      - REVISION
```

## Example: A simple

schedule trigger

The following example shows a trigger that starts a workflow run at midnight
(UTC+0) every Monday through Friday.

When this trigger is activated, CodeCatalyst starts a single workflow run for each
branch in your source repository that contains a workflow definition file with this
trigger.

For example, if you have three branches in your source repository,
`main`, `release-v1`, `feature-123`, and each
of these branches contains a workflow definition file with the trigger that follows,
CodeCatalyst starts three workflow runs: one using the files in `main`, another
using the files in `release-v1`, and another using the files in
`feature-123`.

```
Triggers:
  - Type: SCHEDULE
    Expression: "0 0 ? * MON-FRI *"
```

For more examples of cron expressions you can use in the `Expression`
property, see [Expression](workflow-reference.md#workflow.triggers.expression "workflow-reference.md#workflow.triggers.expression").

## Example: A

trigger with a schedule and branches

The following example shows a trigger that starts a workflow run at 6:15 pm
(UTC+0) every day.

When this trigger is activated, CodeCatalyst starts a workflow run using the files in
the `main` branch, and starts additional runs for each branch that begins
with `release-`.

For example, if you have branches named `main`,
`release-v1`, `bugfix-1`, and `bugfix-2` in your
source repository, CodeCatalyst starts two workflow runs: one using the the files in
`main`, and another using the files in `release-v1`. It
does _not_ start workflow runs for the `bugfix-1` and
`bugfix-1` branches.

```
Triggers:
  - Type: SCHEDULE
    Expression: "15 18 * * ? *"
    Branches:
      - main
      - release\-.*
```

For more examples of cron expressions you can use in the `Expression`
property, see [Expression](workflow-reference.md#workflow.triggers.expression "workflow-reference.md#workflow.triggers.expression").

## Example: A

trigger with a schedule, a push, and branches

The following example shows a trigger that starts a workflow run at midnight
(UTC+0) every day, and whenever code is pushed to the `main`
branch.

In this example:

- A workflow run starts at midnight every day. The workflow run uses the
  workflow definition file and other source files in the `main`
  branch.
- A workflow run also starts whenever you push a commit to the
  `main` branch. The workflow run uses the workflow definition
  file and other source files in the destination branch
  (`main`).

```
Triggers:
  - Type: SCHEDULE
    Expression: "0 0 * * ? *"
    Branches:
      - main
  - Type: PUSH
    Branches:
      - main
```

For more examples of cron expressions you can use in the `Expression`
property, see [Expression](workflow-reference.md#workflow.triggers.expression "workflow-reference.md#workflow.triggers.expression").

## Example: A trigger

with a pull and branches

The following example shows a trigger that starts a workflow run whenever someone
opens or modifies a pull request with a destination branch called `main`.
Although the branch specified in the `Triggers` configuration is
`main`, the workflow run will use the workflow definition file and
other source files in the _source_ branch (which is the branch
you're pulling _from_).

```
Triggers:
  - Type: PULLREQUEST
    Branches:
      - main
    Events:
      - OPEN
      - REVISION
```

## Example: A trigger

with a pull, branches, and a 'CLOSED' event

The following example shows a trigger that starts a workflow run whenever a pull
request is closed on a branch that starts with `main`.

In this example:

- When you close a pull request with a destination branch that starts with
  `main`, a workflow run starts automatically using the
  workflow definition file and other source files in the (now closed) source
  branch.
- If you've configured your source repository to delete branches
  automatically after a pull request is merged, these branches will never have
  the chance to enter the `CLOSED` state. This means that merged
  branches will not activate the pull request `CLOSED` trigger. The
  only way to activate the `CLOSED` trigger in this scenario is to
  close the pull request without merging it.

```
Triggers:
  - Type: PULLREQUEST
    Branches:
      - main.*
    Events:
      - CLOSED
```

## Example: A trigger with

a push, branches, and files

The following example shows a trigger that starts a workflow run whenever a change
is made to the `filename.txt` file, or any file in the `src`
directory, on the `main` branch.

When this trigger is activated, CodeCatalyst starts a workflow run using the workflow
definition file and other source files in the `main` branch.

```
Triggers:
  - Type: PUSH
    Branches:
      - main
    FilesChanged:
      - filename.txt
      - src\/.*
```

## Example: A manual

trigger

To configure a manual trigger, omit the `Triggers` section from the
workflow definition file. Without this section, users are forced to start the
workflow manually by choosing the **Run** button in the CodeCatalyst
console. For more information, see [Starting a workflow run manually](workflows-manually-start.md "workflows-manually-start.md").

## Example: Triggers in a CI/CD

multi-workflow setup

This example describes how to set up triggers when you want to use separate
Amazon CodeCatalyst workflows for continuous integration (CI) and continuous deployment
(CD).

In this scenario, you set up two workflows:

- a **CI workflow** – this workflow
  builds and tests your application when a pull request is created or
  revised.
- a **CD workflow** – this workflow
  builds and deploys your application when a pull request is merged.

The **CI workflow**'s definition file would look
similar to this:

```
Triggers:
  - Type: PULLREQUEST
    Branches:
      - main
    Events:
      - OPEN
      - REVISION
Actions:
  BuildAction:
    `instructions-for-building-the-app`
  TestAction:
    `instructions-for-test-the-app`
```

The `Triggers` code indicates to start a workflow run automatically
whenever a software developer creates a pull request (or [modifies one](pull-requests-update.md "pull-requests-update.md")) asking to merge their
feature branch to the `main` branch. CodeCatalyst starts the workflow run using
the source code in the source branch (which is the feature branch).

The **CD workflow**'s definition file would look
similar to this:

```
Triggers:
  - Type: PUSH
    Branches:
      - main
Actions:
  BuildAction:
    `instructions-for-building-the-app`
  DeployAction:
    `instructions-for-deploying-the-app`
```

The `Triggers` code indicates to start the workflow automatically when
a merge to `main` occurs. CodeCatalyst starts the workflow run using the source
code in the `main` branch.
