

# Using IAM condition keys with Amazon Aurora DSQL
<a name="using-iam-condition-keys"></a>

The `Condition` element (or `Condition` block) specifies the conditions under which a policy statement is in effect. You build conditional expressions using [condition operators](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition_operators.html) such as `StringEquals` or `StringLike` to match keys in the policy against values in the request. Condition keys are different from resource ARN scoping, which restricts actions to specific resources using the `Resource` element.

Amazon Aurora DSQL supports both service-specific condition keys and AWS global condition keys. You can use these keys to refine the conditions under which your IAM policy statements apply. For more information about AWS global condition keys, see [AWS global condition context keys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html) in the *IAM User Guide*.

## Available condition keys for Amazon Aurora DSQL
<a name="using-iam-condition-keys-available"></a>

Amazon Aurora DSQL supports the service-specific condition keys `dsql:WitnessRegion`, `dsql:FisActionId`, and `dsql:FisTargetArns`. You can also use AWS global condition keys such as `aws:RequestTag`, `aws:ResourceTag`, and `aws:TagKeys`. For a complete list of Amazon Aurora DSQL actions, condition keys, and resources that you can specify in policies, see [Actions, resources, and condition keys for Amazon Aurora DSQL](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonauroradsql.html#amazonauroradsql-policy-keys) in the *Service Authorization Reference*.

## Example: Restrict the witness Region for multi-Region clusters
<a name="using-iam-condition-keys-create-cluster"></a>

The following policy uses the `dsql:WitnessRegion` condition key to restrict multi-Region cluster creation to cases where the witness Region is US West (Oregon). Without this condition, you can specify any Region as the witness Region.

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Sid": "AllowCreateWithSpecificWitness",
            "Effect": "Allow",
            "Action": [
                "dsql:CreateCluster",
                "dsql:PutWitnessRegion"
            ],
            "Resource": "arn:aws:dsql:*:123456789012:cluster/*",
            "Condition": {
                "StringEquals": {
                    "dsql:WitnessRegion": "us-west-2"
                }
            }
        },
        {
            "Sid": "AllowMultiRegionSetup",
            "Effect": "Allow",
            "Action": [
                "dsql:PutMultiRegionProperties",
                "dsql:AddPeerCluster"
            ],
            "Resource": "arn:aws:dsql:*:123456789012:cluster/*"
        }
    ]
}
```

------

The first statement applies the `dsql:WitnessRegion` condition to the actions that support it (`dsql:CreateCluster` and `dsql:PutWitnessRegion`). The second statement grants `dsql:PutMultiRegionProperties` and `dsql:AddPeerCluster` without the condition, because the `dsql:WitnessRegion` condition key applies only to `dsql:CreateCluster` and `dsql:PutWitnessRegion`.

## Example: Require tags when creating clusters
<a name="using-iam-condition-keys-tag-on-create"></a>

The following policy uses the `aws:RequestTag` and `aws:TagKeys` condition keys to require an `Environment` tag when you create clusters.

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Sid": "AllowCreateWithRequiredTag",
            "Effect": "Allow",
            "Action": "dsql:CreateCluster",
            "Resource": "arn:aws:dsql:*:123456789012:cluster/*",
            "Condition": {
                "StringEquals": {
                    "aws:RequestTag/Environment": [
                        "production",
                        "staging",
                        "development"
                    ]
                },
                "ForAllValues:StringEquals": {
                    "aws:TagKeys": [
                        "Environment",
                        "Owner"
                    ]
                }
            }
        }
    ]
}
```

------

This policy uses two condition keys together. The `aws:RequestTag/Environment` condition requires that the `Environment` tag has one of the allowed values. The `aws:TagKeys` condition with the `ForAllValues` set operator ensures that the request includes only the `Environment` and `Owner` tag keys.

## Example: Restrict fault injection to specific clusters
<a name="using-iam-condition-keys-fis"></a>

The following policy uses the `dsql:FisActionId` and `dsql:FisTargetArns` condition keys to restrict AWS FIS fault injection to a specific action and target cluster.

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Sid": "AllowSpecificFaultInjection",
            "Effect": "Allow",
            "Action": "dsql:InjectError",
            "Resource": "*",
            "Condition": {
                "StringEquals": {
                    "dsql:FisActionId": "aws:dsql:cluster-connection-failure"
                },
                "ForAllValues:ArnLike": {
                    "dsql:FisTargetArns": "arn:aws:dsql:us-east-1:123456789012:cluster/*"
                }
            }
        }
    ]
}
```

------

The `dsql:FisActionId` condition restricts the fault injection actions that you can perform. The `dsql:FisTargetArns` condition uses the `ForAllValues` set operator and the `ArnLike` operator. Together, they ensure that every cluster ARN in the request matches the allowed pattern. This blocks any request that includes cluster ARNs outside the intended scope.