# Blocking public access with resource-based policies in Aurora DSQL

Block Public Access (BPA) is a feature that identifies and prevents the attaching of resource-based policies that grant public access to your Aurora DSQL clusters across your AWS accounts. With BPA, you can prevent public access to your Aurora DSQL resources. BPA performs checks during the creation or modification of a resource-based policy and helps improve your security posture with Aurora DSQL.

BPA uses [automated reasoning](https://aws.amazon.com/what-is/automated-reasoning/ "https://aws.amazon.com/what-is/automated-reasoning/") to analyze the access granted by your resource-based policy and alerts you if such permissions are found at the time of administering a resource-based policy. The analysis verifies access across all resource-based policy statements, actions, and the set of condition keys used in your policies.

###### Important

BPA helps protect your resources by preventing public access from being granted through the resource-based policies that are directly attached to your Aurora DSQL resources, such as clusters. In addition to using BPA, carefully inspect the following policies to confirm that they do not grant public access:

- Identity-based policies attached to associated AWS principals (for example, IAM roles)
- Resource-based policies attached to associated AWS resources (for example, AWS Key Management Service (KMS) keys)
  You must ensure that the [principal](../../../IAM/latest/UserGuide/reference_policies_elements_principal.md "../../../IAM/latest/UserGuide/reference_policies_elements_principal.md") doesn't include a `*` entry or that one of the specified condition keys restrict access from principals to the resource. If the resource-based policy grants public access to your cluster across AWS accounts, Aurora DSQL will block you from creating or modifying the policy until the specification within the policy is corrected and deemed non-public.

You can make a policy non-public by specifying one or more principals inside the `Principal` block. The following resource-based policy example blocks public access by specifying two principals.

```
{
  "Effect": "Allow",
  "Principal": {
    "AWS": [
      "`123456789012`",
      "`111122223333`"
    ]
  },
  "Action": "dsql:*",
  "Resource": "arn:aws:dsql:`us-east-1:123456789012`:cluster/`cluster-id`"
}
```

Policies that restrict access by specifying certain condition keys are also not considered public. Along with evaluation of the principal specified in the resource-based policy, the following [trusted condition keys](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md") are used to complete the evaluation of a resource-based policy for non-public access:

- `aws:PrincipalAccount`
- `aws:PrincipalArn`
- `aws:PrincipalOrgID`
- `aws:PrincipalOrgPaths`
- `aws:SourceAccount`
- `aws:SourceArn`
- `aws:SourceVpc`
- `aws:SourceVpce`
- `aws:UserId`
- `aws:PrincipalServiceName`
- `aws:PrincipalServiceNamesList`
- `aws:PrincipalIsAWSService`
- `aws:Ec2InstanceSourceVpc`
- `aws:SourceOrgID`
- `aws:SourceOrgPaths`
  Additionally, for a resource-based policy to be non-public, the values for Amazon Resource Name (ARN) and string keys must not contain wildcards or variables. If your resource-based policy uses the `aws:PrincipalIsAWSService` key, you must make sure that you've set the key value to true.

The following policy limits access to the user `Ben` in the specified account.
The condition makes the `Principal` constrained and not be considered as
public.

```
{
  "Effect": "Allow",
  "Principal": {
    "AWS": "*"
  },
  "Action": "dsql:*",
  "Resource": "arn:aws:dsql:`us-east-1:123456789012`:cluster/`cluster-id`",
  "Condition": {
    "StringEquals": {
      "aws:PrincipalArn": "arn:aws:iam::123456789012:user/Ben"
    }
  }
}
```

The following example of a non-public resource-based policy constrains `sourceVPC` using the `StringEquals` operator.

```
{
  "Version":"2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "AWS": "*"
      },
      "Action": "dsql:*",
      "Resource": "arn:aws:dsql:`us-east-1:123456789012`:cluster/`cluster-id`",
      "Condition": {
        "StringEquals": {
          "aws:SourceVpc": [
            "vpc-91237329"
          ]
        }
      }
    }
  ]
}
```
