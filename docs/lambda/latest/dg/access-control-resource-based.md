# Viewing resource-based IAM policies in Lambda

Lambda supports resource-based permissions policies for Lambda functions and layers. You can use resource-based policies to grant access to other [AWS accounts](permissions-function-cross-account.md "permissions-function-cross-account.md"), [organizations](permissions-function-organization.md "permissions-function-organization.md"), or [services](permissions-function-services.md "permissions-function-services.md"). Resource-based policies apply to a single function, version, alias, or layer version.

Console

###### To view a function's resource-based policy

1. Open the [Functions page](https://console.aws.amazon.com/lambda/home#/functions "https://console.aws.amazon.com/lambda/home#/functions") of the Lambda console.
2. Choose a function.
3. Choose **Configuration** and then choose **Permissions**.
4. Scroll down to **Resource-based policy** and then choose **View policy document**. The resource-based policy shows the permissions that are applied when another account or AWS service
   attempts to access the function. The following example shows a statement that allows Amazon S3 to invoke a function
   named `my-function` for a bucket named `amzn-s3-demo-bucket` in account
   `123456789012`.

###### Example resource-based policy

```
`{
 "Version":"2012-10-17",
 "Id": "default",
 "Statement": [
 {
 "Sid": "lambda-allow-s3-my-function",
 "Effect": "Allow",
 "Principal": {
 "Service": "s3.amazonaws.com"
 },
 "Action": "lambda:InvokeFunction",
 "Resource": "arn:aws:lambda:us-east-2:123456789012:function:my-function",
 "Condition": {
 "StringEquals": {
 "AWS:SourceAccount": "123456789012"
 },
 "ArnLike": {
 "AWS:SourceArn": "arn:aws:s3:::amzn-s3-demo-bucket"
 }
 }
 }
 ]
}`

```

AWS CLI
To view a function's resource-based policy, use the `get-policy` command.

```
`aws lambda get-policy \
 --function-name my-function \
 --output text`
```

You should see the following output:

```
`{"Version":"2012-10-17", "Id":"default","Statement":[{"Sid":"sns","Effect":"Allow","Principal":{"Service":"s3.amazonaws.com"},"Action":"lambda:InvokeFunction","Resource":"arn:aws:lambda:us-east-2:123456789012:function:my-function","Condition":{"ArnLike":{"AWS:SourceArn":"arn:aws:sns:us-east-2:123456789012:lambda*"}}}]}`

```

For versions and aliases, append the version number or alias to the function name.

```
`aws lambda get-policy --function-name my-function:PROD`
```

To remove permissions from your function, use `remove-permission`.

```
`aws lambda remove-permission \
 --function-name example \
 --statement-id sns`
```

Use the `get-layer-version-policy` command to view the permissions on a layer.

```
`aws lambda get-layer-version-policy \
 --layer-name my-layer \
 --version-number 3 \
 --output text`
```

You should see the following output:

```
b0cd9796-d4eb-4564-939f-de7fe0b42236    {"Sid":"engineering-org","Effect":"Allow","Principal":"*","Action":"lambda:GetLayerVersion","Resource":"arn:aws:lambda:us-west-2:123456789012:layer:my-layer:3","Condition":{"StringEquals":{"aws:PrincipalOrgID":"o-t194hfs8cz"}}}"
```

Use `remove-layer-version-permission` to remove statements from the policy.

```
`aws lambda remove-layer-version-permission --layer-name my-layer --version-number 3 --statement-id engineering-org`
```

## Supported API actions

The following Lambda API actions support resource-based policies:

- [CreateAlias](../api/API_CreateAlias.md "../api/API_CreateAlias.md")
- [DeleteAlias](../api/API_DeleteAlias.md "../api/API_DeleteAlias.md")
- [DeleteFunction](../api/API_DeleteFunction.md "../api/API_DeleteFunction.md")
- [DeleteFunctionConcurrency](../api/API_DeleteFunctionConcurrency.md "../api/API_DeleteFunctionConcurrency.md")
- [DeleteFunctionEventInvokeConfig](../api/API_DeleteFunctionEventInvokeConfig.md "../api/API_DeleteFunctionEventInvokeConfig.md")
- [DeleteProvisionedConcurrencyConfig](../api/API_DeleteProvisionedConcurrencyConfig.md "../api/API_DeleteProvisionedConcurrencyConfig.md")
- [GetAlias](../api/API_GetAlias.md "../api/API_GetAlias.md")
- [GetFunction](../api/API_GetFunction.md "../api/API_GetFunction.md")
- [GetFunctionConcurrency](../api/API_GetFunctionConcurrency.md "../api/API_GetFunctionConcurrency.md")
- [GetFunctionConfiguration](../api/API_GetFunctionConfiguration.md "../api/API_GetFunctionConfiguration.md")
- [GetFunctionEventInvokeConfig](../api/API_GetFunctionEventInvokeConfig.md "../api/API_GetFunctionEventInvokeConfig.md")
- [GetPolicy](../api/API_GetPolicy.md "../api/API_GetPolicy.md")
- [GetProvisionedConcurrencyConfig](../api/API_GetProvisionedConcurrencyConfig.md "../api/API_GetProvisionedConcurrencyConfig.md")
- [Invoke](../api/API_Invoke.md "../api/API_Invoke.md")
- [InvokeFunctionUrl](urls-auth.md "urls-auth.md") (permission only)
- [ListAliases](../api/API_ListAliases.md "../api/API_ListAliases.md")
- [ListFunctionEventInvokeConfigs](../api/API_ListFunctionEventInvokeConfigs.md "../api/API_ListFunctionEventInvokeConfigs.md")
- [ListProvisionedConcurrencyConfigs](../api/API_ListProvisionedConcurrencyConfigs.md "../api/API_ListProvisionedConcurrencyConfigs.md")
- [ListTags](../api/API_ListTags.md "../api/API_ListTags.md")
- [ListVersionsByFunction](../api/API_ListVersionsByFunction.md "../api/API_ListVersionsByFunction.md")
- [PublishVersion](../api/API_PublishVersion.md "../api/API_PublishVersion.md")
- [PutFunctionConcurrency](../api/API_PutFunctionConcurrency.md "../api/API_PutFunctionConcurrency.md")
- [PutFunctionEventInvokeConfig](../api/API_PutFunctionEventInvokeConfig.md "../api/API_PutFunctionEventInvokeConfig.md")
- [PutProvisionedConcurrencyConfig](../api/API_PutProvisionedConcurrencyConfig.md "../api/API_PutProvisionedConcurrencyConfig.md")
- [TagResource](../api/API_TagResource.md "../api/API_TagResource.md")
- [UntagResource](../api/API_UntagResource.md "../api/API_UntagResource.md")
- [UpdateAlias](../api/API_UpdateAlias.md "../api/API_UpdateAlias.md")
- [UpdateFunctionCode](../api/API_UpdateFunctionCode.md "../api/API_UpdateFunctionCode.md")
- [UpdateFunctionEventInvokeConfig](../api/API_UpdateFunctionEventInvokeConfig.md "../api/API_UpdateFunctionEventInvokeConfig.md")
