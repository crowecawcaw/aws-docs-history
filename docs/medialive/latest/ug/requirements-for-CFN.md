# Requirements for AWS CloudFormation

MediaLive includes a workflow wizard. Creation of a workflow always includes automatic creation
of an AWS CloudFormation stack. Therefore, to use the workflow wizard, users need permissions in AWS CloudFormation.

| Permissions                   | Service name in IAM | Actions                                                                                        |
| ----------------------------- | ------------------- | ---------------------------------------------------------------------------------------------- |
| Work with the workflow wizard | AWS CloudFormation  | `ListStacks`<br>`DescribeStacks`<br>`DescribeStackResources`<br>`CreateStack`<br>`DeleteStack` |
