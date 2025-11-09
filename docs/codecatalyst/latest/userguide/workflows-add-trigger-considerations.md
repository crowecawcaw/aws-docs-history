Amazon CodeCatalyst is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Usage guidelines for triggers and

branches

This section describes some of the main guidelines when setting up Amazon CodeCatalyst triggers
that include branches.

For more information about triggers, see [Starting a workflow run automatically using
triggers](workflows-add-trigger.md "workflows-add-trigger.md").

- **Guideline 1:** For both push and pull request
  triggers, if you are going to specify a branch, you must specify the destination
  (or 'to') branch in the trigger configuration. Never specify the source (or
  'from') branch.

In the following example, a push from any branch to `main`
activates the workflow.

```
Triggers:
  - Type: PUSH
    Branches:
      - main
```

In the following example, a pull request from any branch into
`main` activates the workflow.

```
Triggers:
  - Type: PULLREQUEST
    Branches:
      - main
    Events:
      - OPEN
      - REVISION
```

- **Guideline 2:** For push triggers, after the
  workflow is activated, the workflow will run using the workflow definition file
  and source files in the _destination_ branch.
- **Guideline 3:** For pull request triggers, after
  the workflow is activated, the workflow will run using the workflow definition
  file and source files in the _source_ branch (even though you
  specified the destination branch in the trigger configuration).
- **Guideline 4:** The exact same trigger in one
  branch might not run in another branch.

Consider the following push trigger:

```
Triggers:
  - Type: PUSH
    Branches:
      - main
```

If the workflow definition file containing this trigger exists in
`main` and gets cloned to `test`, the workflow will
never start automatically using the files in `test` (although you
could start the workflow _manually_ to have it use the files
in `test`). Review **Guideline 2** to
understand why the workflow will never run automatically using the files in
`test`.

Consider also the following pull request trigger:

```
Triggers:
  - Type: PULLREQUEST
    Branches:
      - main
    Events:
      - OPEN
      - REVISION
```

If the workflow definition file containing this trigger exists in
`main`, the workflow will never run using the files in
`main`. (However, if you create a `test` branch off of
`main`, the workflow will run using the files in
`test`.) Review **Guideline 3** to
understand why.
