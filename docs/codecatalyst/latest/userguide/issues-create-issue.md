Amazon CodeCatalyst will no longer be open to new customers starting on November
7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For
more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Creating an issue in CodeCatalyst

Development teams create issues to help track and manage their work. You can create
issues within a project based on your needs. For example, you could create an issue to
track updating a variable in your code. You can assign issues to other users in the
project, use labels to help you track your work, and more.

Follow these instructions to create an issue in CodeCatalyst.

###### To create an issue

1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/ "https://codecatalyst.aws/").
2. Navigate to the project where you want to create an issue.
3. On the project home page, choose **Create issue**.
   Alternatively, in the navigation pane, choose
   **Issues**.
4. Choose **Create issue**.

###### Note

You can also add issues inline when using a grid view. 5. Enter a title for the issue. 6. (Optional) Enter a **Description**. You can use Markdown to
add formatting. 7. (Optional) Choose a **Status**,
**Priority**, and **Estimation** for the
issue.

###### Note

If the project's estimation setting is set to **Hide
estimates**, there will not be an
**Estimation** field. 8. (Optional) Add tasks to the issue. Tasks can be used to break down the work of
an issue into smaller objectives. To add a task, choose **+ Add
tasks**. Then, input the task name in the text field and press
enter. After adding tasks, you can mark them as complete by choosing the
checkbox, or reorder them by choosing and dragging the task from the left side
of the checkbox. 9. (Optional) Add an existing label or create a new label and add it by choosing
**+ Add label**.

    1. To add an existing label, choose the label from the list. You can
     enter a search term in the field to search all labels containing that
     term in the project.
    2. To create a new label and add it, enter the name of the label you want
     to create in the search field and press enter.

10. (Optional) Add an assignee by choosing **+ Add an assignee**.
    You can quickly add yourself as the assignee by choosing **+ Add
    me**.

###### Tip

You can choose to assign an issue to **Amazon Q** to
have Amazon Q try to solve the issue. For more information, see [Tutorial: Using CodeCatalyst generative AI
features to speed up your development work](getting-started-project-assistance.md "getting-started-project-assistance.md"). This feature is
only available in the US West (Oregon) Region.

This functionality requires that generative AI features are enabled for
the space. For more information, see [Managing generative AI features](../adminguide/managing-generative-ai-features.md "../adminguide/managing-generative-ai-features.md"). 11. (Optional) Add an existing **custom field** or create a new
custom field. Issues can have multiple custom fields.

    1. To add an existing custom field, choose the custom field from the
     list. You can enter a search term in the field to search all custom
     fields containing that term in the project.
    2. To create a new custom field and add it, enter the name of the custom
     field you want to create in the search field and press enter. Then
     choose the type of custom field you want to create and set a
     value.

12. Choose **Create issue**. A notification appears in the lower
    right corner: If the issue was created successfully, a confirmation message
    appears saying the issue was successfully created. If the issue was not created
    successfully, an error message with the reason for the failure appears. You can
    then choose **Retry** to edit and retry creating the issue, or
    choose **Discard** to discard the issue. Both options will
    dismiss the notification.

###### Note

You cannot link a pull request to an issue when you create it. However,
you can [edit it](issues-edit-issue.md "issues-edit-issue.md") after you create it
to add links to pull requests.

## Best practices

when creating and working with issues assigned to Amazon Q

When you create issues, sometimes some of them linger. The causes for this can be
complex and variable. Sometimes it's because it's not clear who should work on it.
Other times the issue requires research into or expertise with a particular part of
the code base and the best candidates for the work are busy with other issues. Often
there is other urgent work must be attended to first. Any or all of these causes can
result in issues that aren't worked on. CodeCatalyst includes integration with a
generative AI assistant called Amazon Q that can analyze an issue based on its
title and its description. If you assign the issue to Amazon Q, it will attempt to
create a draft solution for you to evaluate. This can help you and your team to
focus and optimize work on issues that require your attention, while Amazon Q
works on a solution for problems you don't have resources to address immediately.

###### Note

###### Note

**Powered by Amazon Bedrock**: AWS implements [automated abuse detection](../../../bedrock/latest/userguide/abuse-detection.md "../../../bedrock/latest/userguide/abuse-detection.md").
Because the **Write description for me**, **Create content summary**, **Recommend tasks**, **Use Amazon Q to create or add features to a project**, and **Assign issues to Amazon Q** feature with Amazon Q Developer Agent for software development features are built on Amazon Bedrock, users can take full advantage of the controls implemented in Amazon Bedrock to enforce safety, security, and the responsible use of artificial intelligence (AI).

Amazon Q performs best on simple issues and straightforward problems. For best
results, use plain language to clearly explain what you want done. The following are
some best practices to help you create issues optimized for Amazon Q to work
on.

###### Important

Generative AI features are only available in the US West (Oregon)
Region.

- **Keep it simple**. Amazon Q does best with
  simple code changes and fixes that can be explained in the title and
  description of the issue. Don't assign issues with vague titles or overly
  flowery or contradictory descriptions.
- **Be specific**. The more information you can
  provide about the exact changes needed to resolve the issue, the more likely
  Amazon Q will be able to create a solution that solves the issue. If
  possible, include specific details such as the name of APIs you want
  changed, methods you want updated, tests that need changes, and any other
  details you can think of.
- **Make sure you have all the details included in the
  title and description of the issue before assigning it to
  Amazon Q**. You can't change the title or description of an
  issue after you assign it to Amazon Q, so make sure you have all the
  information required in an issue before you assign it to Amazon Q.
- **Only assign issues that require code changes in a
  single source repository**. Amazon Q can only work on code in
  a single source repository in CodeCatalyst. Linked repositories are not supported.
  Make sure that the issue only requires changes in a single source repository
  before you assign that issue to Amazon Q.
- **Use the default suggested by Amazon Q for
  approving each step**. By default, Amazon Q will require your
  approval for each step it takes. This allows you to interact with Amazon Q
  in comments not only on the issue, but also on any pull request it creates.
  This provides a more interactive experience with Amazon Q that helps you
  adjust its approach and refine the code it creates to solve the
  issue.

###### Note

Amazon Q does not respond to individual comments in issues or pull
requests, but it will review them when asked to reconsider its approach
or create a revision.

- **Always carefully review the approach suggested by
  Amazon Q**. Once you approve its approach, Amazon Q will
  start work on generating code based on that approach. Make sure that the
  approach seems correct and includes all the details you expect before you
  tell Amazon Q to proceed.
- **Make sure to only allow Amazon Q to work on
  workflows if you don't have existing workflows that might deploy them
  before they're reviewed**. Your project might have workflows
  configured to start runs on pull request events. If so, any pull request
  that Amazon Q creates that includes creating or updating workflow YAML
  might start a run of those workflows included in the pull request. As a best
  practice, don't choose to allow Amazon Q to work on workflow files unless
  you are sure there are no workflows in your project that will automatically
  run these workflows before you review and approve the pull request it
  creates.

For more information, see [Tutorial: Using CodeCatalyst generative AI
features to speed up your development work](getting-started-project-assistance.md "getting-started-project-assistance.md") and [Managing generative AI features](../adminguide/managing-generative-ai-features.md "../adminguide/managing-generative-ai-features.md").
