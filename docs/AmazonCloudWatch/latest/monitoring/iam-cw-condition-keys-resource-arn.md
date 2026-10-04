

# Condition keys for resource metrics configuration access
<a name="iam-cw-condition-keys-resource-arn"></a>

This topic explains how the `cloudwatch:ResourceArn` condition key works and how to use it to limit the resources that a principal can enable or disable detailed monitoring for.

The resource metrics configuration operations are not authorized against a CloudWatch resource type. These operations are `CreateResourceMetricsConfiguration`, `UpdateResourceMetricsConfiguration`, `GetResourceMetricsConfiguration`, and `DeleteResourceMetricsConfiguration`. Instead, they are authorized at the action level, and the AWS resource that the request targets is supplied to IAM in the `cloudwatch:ResourceArn` condition key. For links to the API reference for these operations, see [Amazon CloudWatch permissions reference](permissions-reference-cw.md).

**Important**  
Because these operations are authorized at the action level, specifying the target resource ARN in the `Resource` element of a policy statement does not restrict them. Use `"Resource": "*"` together with a `Condition` block on `cloudwatch:ResourceArn` to control which resources a principal can configure. A statement that omits the condition allows the principal to configure detailed monitoring for any resource in the account.

The value of `cloudwatch:ResourceArn` is the Amazon Resource Name (ARN) that the caller passes in the `ResourceArn` request parameter. Each of these operations targets exactly one resource per request.

For example, to allow a principal to manage detailed monitoring for only one resource, grant the resource metrics configuration actions on `"Resource": "*"` and add a `StringEquals` condition on `cloudwatch:ResourceArn` with the full ARN of that resource. A request that targets any other resource is denied.

------
#### [ JSON ]

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
        "cloudwatch:CreateResourceMetricsConfiguration",
        "cloudwatch:UpdateResourceMetricsConfiguration",
        "cloudwatch:GetResourceMetricsConfiguration",
        "cloudwatch:DeleteResourceMetricsConfiguration"
            ],
            "Resource": "*",
            "Condition": {
                "StringEquals": {
                    "cloudwatch:ResourceArn": "arn:aws:service:us-east-1:123456789012:resource-type/resource-id"
                }
            }
        }
    ]
}
```

------

`cloudwatch:ResourceArn` is evaluated as a string. Use `StringEquals` for an exact match, or `StringLike` with wildcards to match a set of resources. For example, you can use `arn:aws:service:*:123456789012:resource-type/*`. The ARN condition operators, such as `ArnEquals` and `ArnLike`, do not apply to this key.

The following policy uses `StringLike` with wildcards to allow the principal to manage detailed monitoring for any resource of one type in the account:

------
#### [ JSON ]

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
        "cloudwatch:CreateResourceMetricsConfiguration",
        "cloudwatch:UpdateResourceMetricsConfiguration",
        "cloudwatch:GetResourceMetricsConfiguration",
        "cloudwatch:DeleteResourceMetricsConfiguration"
            ],
            "Resource": "*",
            "Condition": {
                "StringLike": {
                    "cloudwatch:ResourceArn": "arn:aws:service:*:123456789012:resource-type/*"
                }
            }
        }
    ]
}
```

------

For more information about the `Condition` element in IAM policies, see [IAM JSON policy elements: Condition](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition.html).