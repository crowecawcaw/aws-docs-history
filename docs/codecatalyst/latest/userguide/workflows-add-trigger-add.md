Amazon CodeCatalyst will no longer be open to new customers starting on November
7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For
more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Adding triggers to workflows

Use the following instructions to add a push, pull, or schedule trigger to your
Amazon CodeCatalyst workflow.

For more information about triggers, see [Starting a workflow run automatically using
triggers](workflows-add-trigger.md "workflows-add-trigger.md").

Visual

###### To add a trigger (visual

editor)

1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/ "https://codecatalyst.aws/").
2. Choose your project.
3. In the navigation pane, choose **CI/CD**, and then choose **Workflows**.
4. Choose the name of your workflow. You can filter by the source
   repository or branch name where the workflow is defined, or filter
   by workflow name or status.
5. Choose **Edit**.
6. Choose **Visual**.
7. In the workflow diagram, choose the **Source**
   and **Triggers** box.
8. In the configuration pane, Choose **Add
   trigger**.
9. In the **Add trigger** dialog box, supply
   information in the fields, as follows.

**Trigger type**

Specify the type of trigger. You can use one of the following values:

    * **Push** (visual editor) or `PUSH` (YAML editor)


    A push trigger starts a workflow run when a change is pushed to your source repository.
     The workflow run will use the files in the branch that you're pushing
     *to* (that is, the destination branch).
    * **Pull request** (visual editor) or `PULLREQUEST` (YAML
     editor)


    A pull request trigger starts a workflow run when a pull request is opened, updated, or
     closed in your source repository. The workflow run will use the files in the branch that
     you're pulling *from* (that is, the source branch).
    * **Schedule** (visual editor) or `SCHEDULE` (YAML
     editor)


    A schedule trigger starts workflow runs on a schedule defined by a cron expression that
     you specify. A separate workflow run will start for each branch in your source repository
     using the branch's files. (To limit the branches that the trigger activates on, use the
     **Branches** field (visual editor) or `Branches` property
     (YAML editor).)


    When configuring a schedule trigger, follow these guidelines:




    	+ Only use one schedule trigger per workflow.
    	+ If you've defined multiple workflows in your CodeCatalyst space, we
    	 recommend that you schedule no more than 10 of them to start
    	 concurrently.
    	+ Make sure you configure the trigger's cron expression with adequate time between
    	 runs. For more information, see [Expression](workflow-reference.md#workflow.triggers.expression "workflow-reference.md#workflow.triggers.expression").

For examples, see [Examples: Triggers in workflows](workflows-add-trigger-examples.md "workflows-add-trigger-examples.md").

**Events for pull request**

This field only appears if you selected the **Pull
request** trigger type.

Specify the type of pull request events that will start a workflow run. The following are
the valid values:

    * **Pull request is created** (visual editor) or `OPEN` (YAML
     editor)


    The workflow run is started when a pull request is created.
    * **Pull request is closed** (visual editor) or `CLOSED` (YAML
     editor)


    The workflow run is started when a pull request is closed. The `CLOSED`
     event's behavior is tricky, and is best understood through an example. See [Example: A trigger
     with a pull, branches, and a 'CLOSED' event](workflows-add-trigger-examples.md#workflows-add-trigger-examples-push-pull-close "workflows-add-trigger-examples.md#workflows-add-trigger-examples-push-pull-close") for more
     information.
    * **New revision is made to pull request** (visual editor) or
     `REVISION` (YAML editor)


    The workflow run is started when a revision to a pull request is created. The first
     revision is created when the pull request is created. After that, a new revision is created
     every time someone pushes a new commit to the source branch specified in the pull
     request. If you include the `REVISION` event in your pull request trigger, you
     can omit the `OPEN` event, since `REVISION` is a superset of
     `OPEN`.

You can specify multiple events in the same pull request trigger.

For examples, see [Examples: Triggers in workflows](workflows-add-trigger-examples.md "workflows-add-trigger-examples.md").

**Schedule**

This field only appears if you selected the
**Schedule** trigger type.

Specify the cron expression that describes when you want your scheduled workflow runs to
occur.

Cron expressions in CodeCatalyst use the following six-field syntax, where each field is separated
by a space:

`minutes`
`hours`
`days-of-month`
`month`
`days-of-week`
`year`

**Examples of cron expressions**

| Minutes | Hours | Days of month | Month | Days of week | Year      | Meaning                                                                                                                                 |
| ------- | ----- | ------------- | ----- | ------------ | --------- | --------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0       | 0     | ?             | \*    | MON-FRI      | \*        | Runs a workflow at midnight (UTC+0) every Monday through Friday.                                                                        |
| 0       | 2     | \*            | \*    | ?            | \*        | Runs a workflow at 2:00 am (UTC+0) every day.                                                                                           |
| 15      | 22    | \*            | \*    | ?            | \*        | Runs a workflow at 10:15 pm (UTC+0) every day.                                                                                          |
| 0/30    | 22-2  | ?             | \*    | SAT-SUN      | \*        | Runs a workflow every 30 minutes Saturday through Sunday between 10:00 pm on the starting day and 2:00 am on the following day (UTC+0). |
| 45      | 13    | L             | \*    | ?            | 2023-2027 | Runs a workflow at 1:45 pm (UTC+0) on the last day of the month between the years 2023 and 2027 inclusive.                              | When specifying cron expressions in CodeCatalyst, make sure you follow these guidelines: <br>• Specify a single cron expression per `SCHEDULE` trigger. <br>• Enclose the cron expression in double-quotes (`"`) in the YAML editor. <br>• Specify the time in Coordinated Universal Time (UTC). Other time zones are not supported. <br>• Configure at least 30 minutes between runs. A faster cadence is not supported. <br>• Specify the `days-of-month` or `days-of-week` field, but not both. If you specify a value or an asterisk (`*`) in one of the fields, you must use a question mark (`?`) in the other. The asterisk means 'all' and the question mark means 'any'. For more examples of cron expressions and information about wildcards like `?`, `*`, and `L`, see the [Cron expressions reference](../../../eventbridge/latest/userguide/eb-cron-expressions.md "../../../eventbridge/latest/userguide/eb-cron-expressions.md") in the _Amazon EventBridge User Guide_. Cron expressions in EventBridge and CodeCatalyst work exactly the same way. For examples of schedule triggers, see [Examples: Triggers in workflows](workflows-add-trigger-examples.md "workflows-add-trigger-examples.md"). **Branches** and **Branch pattern** (Optional) Specify the branches in your source repository that the trigger monitors in order to know when to start a workflow run. You can use regex patterns to define your branch names. For example, use `main.*` to match all branches beginning with `main`. The branches to specify are different depending on the trigger type: <br>• For a push trigger, specify the branches you're pushing _to_, that is, the _destination_ branches. One workflow run will start per matched branch, using the files in the matched branch. Examples: `main.*`, `mainline` <br>• For a pull request trigger, specify the branches you're pushing _to_, that is, the _destination_ branches. One workflow run will start per matched branch, using the workflow definition file and source files in the **source** branch (_not_ the matched branch). Examples: `main.*`, `mainline`, `v1\-.*` (matches branches that start with `v1-`) <br>• For a schedule trigger, specify the branches that contain the files that you want your scheduled run to use. One workflow run will start per matched branch, using the the workflow definition file and source files in the matched branch. Examples: `main.*`, `version\-1\.0` ###### Note If you _don't_ specify branches, the trigger monitors all branches in your source repository, and will start a workflow run using the workflow definition file and source files in: <br>• The branch you're pushing _to_ (for push triggers). For more information, see [Example: A simple code push trigger](workflows-add-trigger-examples.md#workflows-add-trigger-examples-push-simple "workflows-add-trigger-examples.md#workflows-add-trigger-examples-push-simple"). <br>• The branch you're pulling _from_ (for pull request triggers). For more information, see [Example: A simple pull request trigger](workflows-add-trigger-examples.md#workflows-add-trigger-examples-pull-simple "workflows-add-trigger-examples.md#workflows-add-trigger-examples-pull-simple"). <br>• All branches (for schedule triggers). One workflow run will start per branch in your source repository. For more information, see [Example: A simple schedule trigger](workflows-add-trigger-examples.md#workflows-add-trigger-examples-schedule-simple "workflows-add-trigger-examples.md#workflows-add-trigger-examples-schedule-simple"). For more information about branches and triggers, see [Usage guidelines for triggers and branches](workflows-add-trigger-considerations.md "workflows-add-trigger-considerations.md"). For more examples, see [Examples: Triggers in workflows](workflows-add-trigger-examples.md "workflows-add-trigger-examples.md"). **Files changed** This field only appears if you selected the **Push** or **Pull request** trigger type. Specify the files or folders in your source repository that the trigger monitors in order to know when to start a workflow run. You can use regular expressions to match file names or paths. For examples, see [Examples: Triggers in workflows](workflows-add-trigger-examples.md "workflows-add-trigger-examples.md"). 10. (Optional) Choose **Validate** to validate the workflow's YAML code before committing. 11. Choose **Commit**, enter a commit message, and choose **Commit** again. YAML ###### To add a trigger (YAML editor) 1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/ "https://codecatalyst.aws/"). 2. Choose your project. 3. In the navigation pane, choose **CI/CD**, and then choose **Workflows**. 4. Choose the name of your workflow. You can filter by the source repository or branch name where the workflow is defined, or filter by workflow name or status. 5. Choose **Edit**. 6. Choose **YAML**. 7. Add a `Triggers` section and underlying properties using the following example as a guide. For more information, see the [Triggers](workflow-reference.md#triggers-reference "workflow-reference.md#triggers-reference") in the [Workflow YAML definition](workflow-reference.md "workflow-reference.md"). A code push trigger might look like this: `Triggers: <br>• Type: PUSH Branches: <br>• main` A pull request trigger might look like this: `Triggers: <br>• Type: PULLREQUEST Branches: <br>• main.* Events: <br>• OPEN <br>• REVISION <br>• CLOSED` A schedule trigger might look like this: `Triggers: <br>• Type: SCHEDULE Branches: <br>• main.* # Run the workflow at 1:15 am (UTC+0) every Friday until the end of 2023 Expression: "15 1 ? * FRI 2022-2023"` For more examples of cron expressions you can use in the `Expression` property, see [Expression](workflow-reference.md#workflow.triggers.expression "workflow-reference.md#workflow.triggers.expression"). For more examples of push, pull request, and schedule triggers, see [Examples: Triggers in workflows](workflows-add-trigger-examples.md "workflows-add-trigger-examples.md"). 8. (Optional) Choose **Validate** to validate the workflow's YAML code before committing. 9. Choose **Commit**, enter a commit message, and choose **Commit** again. |
