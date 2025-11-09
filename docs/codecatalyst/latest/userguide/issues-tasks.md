Amazon CodeCatalyst is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Managing tasks on issues

_Tasks_ can be added to issues to further break down, organize,
and track the work of that issue. You can create tasks yourself, or you can use
Amazon Q to recommend tasks based on its analysis of the issue and its complexity.

Amazon Q Developer is a generative AI-powered conversational assistant that can help you
to understand, build, extend, and operate AWS applications. To accelerate your
building on AWS, the model that powers Amazon Q is augmented with high-quality AWS
content to produce more complete, actionable, and referenced answers. For more
information, see [What is Amazon Q Developer?](../../../amazonq/latest/aws-builder-use-ug/what-is.md "../../../amazonq/latest/aws-builder-use-ug/what-is.md")
in the _Amazon Q Developer User Guide_.

###### To manage tasks on an issue

1. Choose the issue for which you want to manage tasks. For help on finding
   your issue, see [Finding and viewing issues](issues-view.md "issues-view.md").
2. In **Tasks**, you can view and manage tasks for the
   issue.
   1. To add a task, input the task name in the text field and press
      enter.
   2. If there are no tasks for the issue, you can choose to have Amazon Q
      analyze the issue and create tasks based on the issue title,
      description, and its analysis of the complexity of the issue and the
      repository code, choose **Recommend tasks**. You
      will need to specify the source repository that contains the code
      for the issue. Choose **Start recomending tasks**
      to begin the task recommendation analysis. That dialog will close.
      Once the recommendation is complete, choose **View
      recommended tasks** to review the tasks and take any
      needed action, such as deleting or adding tasks to the list or
      reordering the recommended tasks, before choosing **Create
      tasks**.

   After tasks are created for you, you can assign them to users and
   work with them the same way you work with manually created
   tasks. 3. To mark a task as completed, choose the checkbox of the
   task. 4. To view or update the details of a task, choose it from the
   list. 5. To reorder the tasks, choose and drag the task from the left side
   of the checkbox. 6. To remove a task, choose the ellipses menu of the task and choose
   **Remove**.
