

Amazon CodeCatalyst is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [How to migrate from CodeCatalyst](migration.md).

# 'Render Amazon ECS task definition' variables
<a name="render-ecs-action-variables"></a>

The **Render Amazon ECS task definition** action produces and sets the following variables at run time. These are known as *predefined variables*.

For information about referencing these variables in a workflow, see [Using predefined variables](workflows-using-predefined-variables.md).


| Key | Value | 
| --- | --- | 
| task-definition | The name given to the task definition file that was updated by the **Render Amazon ECS task definition** action. The name follows the format `task-definition-random-string.json`.<br />Example: `task-definition--259-0a2r7gxlTF5Xr.json` | 