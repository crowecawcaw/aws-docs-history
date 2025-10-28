# UpdateConstraint

Updates the specified constraint.

## Request Syntax

```
{
   "AcceptLanguage": "`string`",
   "Description": "`string`",
   "Id": "`string`",
   "Parameters": "`string`"
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[AcceptLanguage](#API_UpdateConstraint_RequestSyntax "#API_UpdateConstraint_RequestSyntax")**

The language code.

- `jp` - Japanese
- `zh` - Chinese

Type: String

Length Constraints: Maximum length of 100.

Required: No

**[Description](#API_UpdateConstraint_RequestSyntax "#API_UpdateConstraint_RequestSyntax")**

The updated description of the constraint.

Type: String

Length Constraints: Maximum length of 2000.

Required: No

**[Id](#API_UpdateConstraint_RequestSyntax "#API_UpdateConstraint_RequestSyntax")**

The identifier of the constraint.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 100.

Pattern: `^[a-zA-Z0-9_\-]*`

Required: Yes

**[Parameters](#API_UpdateConstraint_RequestSyntax "#API_UpdateConstraint_RequestSyntax")**

The constraint parameters, in JSON format. The syntax depends on the constraint type as follows:

LAUNCH

You are required to specify either the `RoleArn` or the `LocalRoleName` but can't use both.

Specify the `RoleArn` property as follows:

`{"RoleArn" : "arn:aws:iam::123456789012:role/LaunchRole"}`

Specify the `LocalRoleName` property as follows:

`{"LocalRoleName": "SCBasicLaunchRole"}`

If you specify the `LocalRoleName` property, when an account uses the launch constraint, the IAM role with that name in the account will be used. This allows launch-role constraints to be
account-agnostic so the administrator can create fewer resources per shared account.

###### Note

The given role name must exist in the account used to create the launch constraint and the account of the user who launches a product with this launch constraint.

You cannot have both a `LAUNCH` and a `STACKSET` constraint.

You also cannot have more than one `LAUNCH` constraint on a product and portfolio.

NOTIFICATION

Specify the `NotificationArns` property as follows:

`{"NotificationArns" : ["arn:aws:sns:us-east-1:123456789012:Topic"]}`

RESOURCE_UPDATE

Specify the `TagUpdatesOnProvisionedProduct` property as follows:

`{"Version":"2.0","Properties":{"TagUpdateOnProvisionedProduct":"String"}}`

The `TagUpdatesOnProvisionedProduct` property accepts a string value of `ALLOWED` or `NOT_ALLOWED`.

STACKSET

Specify the `Parameters` property as follows:

`{"Version": "String", "Properties": {"AccountList": [ "String" ], "RegionList": [ "String" ], "AdminRole": "String", "ExecutionRole": "String"}}`

You cannot have both a `LAUNCH` and a `STACKSET` constraint.

You also cannot have more than one `STACKSET` constraint on a product and portfolio.

Products with a `STACKSET` constraint will launch an AWS CloudFormation stack set.

TEMPLATE

Specify the `Rules` property. For more information, see
[Template Constraint Rules](../adminguide/reference-template_constraint_rules.md "../adminguide/reference-template_constraint_rules.md").

Type: String

Required: No

## Response Syntax

```
{
   "ConstraintDetail": {
      "ConstraintId": "***string***",
      "Description": "***string***",
      "Owner": "***string***",
      "PortfolioId": "***string***",
      "ProductId": "***string***",
      "Type": "***string***"
   },
   "ConstraintParameters": "***string***",
   "Status": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[ConstraintDetail](#API_UpdateConstraint_ResponseSyntax "#API_UpdateConstraint_ResponseSyntax")**

Information about the constraint.

Type: [ConstraintDetail](API_ConstraintDetail.md "API_ConstraintDetail.md") object

**[ConstraintParameters](#API_UpdateConstraint_ResponseSyntax "#API_UpdateConstraint_ResponseSyntax")**

The constraint parameters.

Type: String

**[Status](#API_UpdateConstraint_ResponseSyntax "#API_UpdateConstraint_ResponseSyntax")**

The status of the current request.

Type: String

Valid Values: `AVAILABLE | CREATING | FAILED`

## Errors

**InvalidParametersException**

One or more parameters provided to the operation are not valid.

HTTP Status Code: 400

**ResourceNotFoundException**

The specified resource was not found.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/servicecatalog-2015-12-10/UpdateConstraint.md "../../../goto/cli2/servicecatalog-2015-12-10/UpdateConstraint.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/servicecatalog-2015-12-10/UpdateConstraint.md "../../../goto/DotNetSDKV3/servicecatalog-2015-12-10/UpdateConstraint.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/servicecatalog-2015-12-10/UpdateConstraint.md "../../../goto/SdkForCpp/servicecatalog-2015-12-10/UpdateConstraint.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/servicecatalog-2015-12-10/UpdateConstraint.md "../../../goto/SdkForGoV2/servicecatalog-2015-12-10/UpdateConstraint.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/servicecatalog-2015-12-10/UpdateConstraint.md "../../../goto/SdkForJavaV2/servicecatalog-2015-12-10/UpdateConstraint.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/servicecatalog-2015-12-10/UpdateConstraint.md "../../../goto/SdkForJavaScriptV3/servicecatalog-2015-12-10/UpdateConstraint.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/servicecatalog-2015-12-10/UpdateConstraint.md "../../../goto/SdkForKotlin/servicecatalog-2015-12-10/UpdateConstraint.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/servicecatalog-2015-12-10/UpdateConstraint.md "../../../goto/SdkForPHPV3/servicecatalog-2015-12-10/UpdateConstraint.md")
- [AWS SDK for Python](../../../goto/boto3/servicecatalog-2015-12-10/UpdateConstraint.md "../../../goto/boto3/servicecatalog-2015-12-10/UpdateConstraint.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/servicecatalog-2015-12-10/UpdateConstraint.md "../../../goto/SdkForRubyV3/servicecatalog-2015-12-10/UpdateConstraint.md")
