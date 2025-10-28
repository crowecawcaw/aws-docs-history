# Invoke an AWS Lambda function from an Amazon Bedrock

flow in a different AWS account

An Amazon Bedrock flow can invoke a AWS Lambda function that is in a different AWS account from
the flow. Use the following procedure to configure the Lambda function (_Account
A_) and the flow (_Account B_).

###### To configure a flow flow to call a Lambda

function in a different AWS account

1. In Account A (Lambda function), add a resource-based policy to the Lambda
   function, using the Flow Execution Role from Account B as the principal. For more
   information, see [Granting Lambda
   function access to other accounts](../../../lambda/latest/dg/permissions-function-cross-account.md "../../../lambda/latest/dg/permissions-function-cross-account.md") in the _AWS Lambda_
   documentation.
2. In Account B (Amazon Bedrock flow), add permission for the [invoke](../../../lambda/latest/api/API_Invoke.md "../../../lambda/latest/api/API_Invoke.md") operation to the flow
   execution role for the Lambda function ARN that you are using. For more information,
   see [Update
   permissions for a role](../../../IAM/latest/UserGuide/id_roles_update-role-permissions.md "../../../IAM/latest/UserGuide/id_roles_update-role-permissions.md") in the _AWS Identity and Access Management_
   documentation.
