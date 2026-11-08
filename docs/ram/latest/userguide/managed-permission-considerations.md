

# Considerations for using customer managed permissions in AWS RAM
<a name="managed-permission-considerations"></a>

Customer managed permissions are only available in the AWS Region that you create them in. Not all resource types support customer managed permissions. For a list of supported resource types in AWS Resource Access Manager, see [Shareable AWS resources](shareable.md).

The policy template of a customer managed permission follows these rules:
+ It can contain one statement or several.
+ Each statement must have the `Allow` effect.
+ Each statement can contain only the `Effect`, `Action`, and `Condition` elements.
+ You can use any IAM condition operator, including negating operators such as `StringNotEquals` and `NotIpAddress`, `...IfExists` operators, and the `ForAnyValue` and `ForAllValues` set operators.

To use more than one statement, specify the policy template as a JSON array of statement objects. The template must start with the `[` character. The following example policy template has two statements. The first grants read access to principals with a `team` tag of `payments`. The second grants describe access to everyone in the share.

```
[
    {
        "Effect": "Allow",
        "Action": [
            "ssm:GetParameter",
            "ssm:GetParameters"
        ],
        "Condition": {
            "StringEquals": {
                "aws:PrincipalTag/team": "payments"
            }
        }
    },
    {
        "Effect": "Allow",
        "Action": [
            "ssm:DescribeParameters"
        ]
    }
]
```

The following conditions aren't supported in customer managed permissions:
+ Condition keys used to match properties of the principal:
  + `aws:PrincipalOrgId`
  + `aws:PrincipalOrgPaths`
  + `aws:PrincipalAccount`
+ Condition keys used to restrict access for service principals:
  + `aws:SourceArn`
  + `aws:SourceAccount`
  + `aws:SourceOrgPaths`
  + `aws:SourceOrgID`
+ System tags:
  + `aws:PrincipalTag/aws:`
  + `aws:ResourceTag/aws:`
  + `aws:RequestTag/aws:`

**Note**  
The `aws:SourceAccount` value is automatically populated when sharing to service principals.