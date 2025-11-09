Amazon CodeCatalyst is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Example: Defining two action

groups

The following example shows how to define two Amazon CodeCatalyst action groups:
`BuildAndTest` and `Deploy`. The `BuildAndTest`
group includes two actions (`Build` and `Test`), and the
`Deploy` group also includes two actions
(`DeployCloudFormationStack` and `DeployToECS`).

```
Actions:
  BuildAndTest: # Action group 1
    Actions:
      Build:
        Identifier: aws/build@v1
        Configuration:
          ...
      Test:
        Identifier: aws/managed-test@v1
        Configuration:
  Deploy: #Action group 2
    Actions:
      DeployCloudFormationStack:
        Identifier: aws/cfn-deploy@v1
        Configuration:
          ...
      DeployToECS:
        Identifier: aws/ecs-deploy@v1
        Configuration:
          ...
```
