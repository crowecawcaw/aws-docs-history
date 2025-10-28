# [CT.LAMBDA.PV.2] Require an AWS Lambda function or AWS Lambda function URL to be configured for access only to principals within your AWS account

This control requires an AWS Lambda function resource-based policy to grant access only to IAM principals that reside in your AWS account.

This is a preventive control with elective guidance based on service control policies (SCPs). By default, this control is not enabled. You can enable this control through the AWS Control Tower console, or though the AWS Control Tower APIs.

**AWS service:** AWS Lambda

###### Control metadata

- **Control objective:** Enforce least privilege
- **Implementation:** Service control policy (SCP)
- **Control behavior:** Preventive
- **Control owner:** AWS Control Tower
- **Control groups:** digital-sovereignty
- **Resource types:** `AWS::Lambda::Url`, `AWS::Lambda::Function`

###### Usage considerations

- This control limits cross-account access to AWS Lambda functions by restricting the allowed IAM principals in a Lambda function resource policy to those in the same account as the Lambda function. Allow listing AWS service principals is not supported by this control.
- Permissions to AWS Lambda functions and related URL(s) are governed by this control.
- This control supports configuration. It contains elements that are included by AWS Control Tower conditionally, based on the configuration you select. This control supports the following configuration parameters: **ExemptedPrincipalArns**. For more information, see [Configure controls with parameters](control-parameter-concepts.md "control-parameter-concepts.md").
  The artifact for this control is the following service control policy (SCP).

```

{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "CTLAMBDAPV2",
            "Effect": "Deny",
            "Action": "lambda:AddPermission",
            "Resource": "arn:*:lambda:*:*:function:*",
            "Condition": {
                "StringNotLike": {
                    "lambda:Principal": [
                        "arn:*:iam::${aws:PrincipalAccount}:*",
                        "${aws:PrincipalAccount}"
                    ]
                },
                "ArnNotLike": {
                    "aws:PrincipalArn": [
                        {{ExemptedPrincipalArns}}
                        "arn:*:iam::*:role/AWSControlTowerExecution"
                    ]
                }
            }
        }
    ]
}


```
