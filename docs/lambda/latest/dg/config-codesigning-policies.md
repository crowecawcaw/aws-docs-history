# Configuring IAM policies for Lambda code signing configurations

To grant permission for a user to access Lambda code signing API operations, attach one or more policy statements to the user policy. For more information about user
policies, see [Identity-based IAM policies for Lambda](access-control-identity-based.md "access-control-identity-based.md").

The following example policy statement grants permission to create, update, and retrieve code signing
configurations.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "lambda:CreateCodeSigningConfig",
 "lambda:UpdateCodeSigningConfig",
 "lambda:GetCodeSigningConfig"
 ],
 "Resource": "*"
 }
 ]
}`

```

Administrators can use the `CodeSigningConfigArn` condition key to specify the code signing
configurations that developers must use to create or update your functions.

The following example policy statement grants permission to create a function. The policy statement includes a
`lambda:CodeSigningConfigArn` condition to specify the allowed code signing configuration. Lambda
blocks `CreateFunction` API requests if the [CodeSigningConfigArn](../api/API_CreateFunction.md#lambda-CreateFunction-request-CodeSigningConfigArn "../api/API_CreateFunction.md#lambda-CreateFunction-request-CodeSigningConfigArn") parameter is missing
or does not match the value in the condition.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AllowReferencingCodeSigningConfig",
 "Effect": "Allow",
 "Action": [
 "lambda:CreateFunction"
 ],
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "lambda:CodeSigningConfigArn": "arn:aws:lambda:us-east-1:`111122223333`:code-signing-config:csc-0d4518bd353a0a7c6"
 }
 }
 }
 ]
}`

```
