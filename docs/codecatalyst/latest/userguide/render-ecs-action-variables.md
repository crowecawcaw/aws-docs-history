Amazon CodeCatalyst will no longer be open to new customers starting on November
7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For
more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# 'Render Amazon ECS task definition' variables

The **Render Amazon ECS task definition** action produces and sets the
following variables at run time. These are known as _predefined
variables_.

For information about referencing these variables in a workflow, see [Using predefined variables](workflows-using-predefined-variables.md "workflows-using-predefined-variables.md").

| Key             | Value                                                                                                                                                                                                                                   |
| --------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| task-definition | The name given to the task definition file that was updated by the **Render Amazon ECS task definition** action. The name follows the format `task-definition-*random-string*.json`. Example: `task-definition--259-0a2r7gxlTF5Xr.json` |
