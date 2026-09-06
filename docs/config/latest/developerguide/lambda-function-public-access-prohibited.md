

# lambda-function-public-access-prohibited
<a name="lambda-function-public-access-prohibited"></a>

Checks if the AWS Lambda function policy attached to the Lambda resource prohibits public access. If the Lambda function policy allows public access it is NON\_COMPLIANT.

**Context**: A lambda function policy is considered to allow public access if the principal element is empty or contains a wildcard. For example, if the principal element is `“”` or `{“AWS”: “”}`. Granting public access is not recommended for security reasons. Restricting public access can help you prevent unauthorized invocations of your Lambda functions, which could compromise your data or incur unwanted costs.

To restrict access to your Lambda functions, specify the AWS account IDs or the Amazon Resource Names (ARNs) of the IAM users, roles, or services that can invoke the functions. For more information, see [Granting function access to other accounts](https://docs.aws.amazon.com/lambda/latest/dg/access-control-resource-based.html#permissions-resource-xaccountinvoke) in the *AWS Lambda Developer Guide*.

The rule is also `NON_COMPLIANT` if a Lambda function is invoked from Amazon S3, and the policy doesn't include a condition to limit public access, such as `AWS:SourceAccount`. We recommend using other S3 conditions along with `AWS:SourceAccount` in your bucket policy for more refined access.

**Note**  
To be considered non-public, a Lambda resource-based policy must grant access only to fixed values. This means values that don't contain a wildcard or the following IAM policy element: [Variables](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_variables.html#policy-vars-using-variables).

**Identifier:** LAMBDA\_FUNCTION\_PUBLIC\_ACCESS\_PROHIBITED

**Resource Types:** AWS::Lambda::Function

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except China (Ningxia) Region

**Parameters:**

None  

## AWS CloudFormation template
<a name="w2aac20c16c17b7e1067c25"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).