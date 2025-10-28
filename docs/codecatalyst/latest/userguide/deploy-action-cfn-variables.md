Amazon CodeCatalyst will no longer be open to new customers starting on November
7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For
more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# 'Deploy AWS CloudFormation stack' variables

The **Deploy AWS CloudFormation stack** action produces and sets the following
variables at run time. These are known as _predefined variables_.

For information about referencing these variables in a workflow, see [Using predefined variables](workflows-using-predefined-variables.md "workflows-using-predefined-variables.md").

| Key                 | Value                                                                                                                                                                            |
| ------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| deployment-platform | The name of the deployment platform. Hardcoded to `AWS:CloudFormation`.                                                                                                          |
| region              | The region code of the AWS Region that was deployed to during the workflow run. Example: `us-west-2`                                                                             |
| stack-id            | The Amazon Resource Name (ARN) of the deployed stack. Example: `arn:aws:cloudformation:us-west-2:111122223333:stack/codecatalyst-cfn-stack/6aad4380-100a-11ec-a10a-03b8a84d40df` |
