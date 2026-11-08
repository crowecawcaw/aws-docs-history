

# Common resource-based policy examples
<a name="rbp-examples"></a>

These examples show common patterns for controlling access to your Aurora DSQL clusters. You can combine and modify these patterns to meet your specific access requirements.

**Note**  
Use `"Resource": "*"` in cluster policies. In a cluster policy, `*` means the cluster that has the policy. If a statement names a different cluster's ARN, such as one copied from a peered cluster in another AWS Region, the statement doesn't apply. When you create a cluster with a policy, you also can't name the cluster's ARN, because the cluster doesn't have one yet.

## Block public internet access
<a name="rbp-example-block-public"></a>

This policy blocks connections to your Aurora DSQL clusters from the public internet (non-VPC). The policy doesn't restrict which VPC your connections come from, only that they come from a VPC. To limit access to a specific VPC, use a `StringNotEquals` condition on `aws:SourceVpc` instead, as in [Multi-Region cluster policies](#rbp-example-multi-region). This condition also blocks connections from the public internet, because they don't include `aws:SourceVpc`.

```
{
  "Version": "2012-10-17",		 	 	 
  "Statement": [
    {
      "Effect": "Deny",
      "Principal": {
        "AWS": "*"
      },
      "Resource": "*",
      "Action": [
        "dsql:DbConnect",
        "dsql:DbConnectAdmin"
      ],
      "Condition": {
        "Null": {
          "aws:SourceVpc": "true"
        }
      }
    }
  ]
}
```

**Note**  
This example uses only `aws:SourceVpc` to check for VPC connections. The `aws:VpcSourceIp` and `aws:SourceVpce` condition keys provide additional granularity but are not required for basic VPC-only access control.

To provide an exception for specific roles, use this policy instead:

```
{
  "Version": "2012-10-17",		 	 	 
  "Statement": [
    {
      "Sid": "DenyAccessFromOutsideVPC",
      "Effect": "Deny",
      "Principal": {
        "AWS": "*"
      },
      "Resource": "*",
      "Action": [
        "dsql:DbConnect",
        "dsql:DbConnectAdmin"
      ],
      "Condition": {
        "Null": {
          "aws:SourceVpc": "true"
        },
        "StringNotEquals": {
          "aws:PrincipalArn": [
            "arn:aws:iam::123456789012:role/ExceptionRole",
            "arn:aws:iam::123456789012:role/AnotherExceptionRole"
          ]
        }
      }
    }
  ]
}
```

## Restrict access to AWS Organization
<a name="rbp-example-org-access"></a>

This policy restricts access to principals within an AWS Organization:

```
{
  "Version": "2012-10-17",		 	 	 
  "Statement": [
    {
      "Effect": "Deny",
      "Principal": {
        "AWS": "*"
      },
      "Action": [
        "dsql:DbConnect",
        "dsql:DbConnectAdmin"
      ],
      "Resource": "*",
      "Condition": {
        "StringNotEquals": {
          "aws:PrincipalOrgID": "o-exampleorgid"
        }
      }
    }
  ]
}
```

## Restrict access to specific Organizational Unit
<a name="rbp-example-ou-access"></a>

This policy restricts access to principals within a specific Organizational Unit (OU) in an AWS Organization, providing more granular control than organization-wide access:

```
{
  "Version": "2012-10-17",		 	 	 
  "Statement": [
    {
      "Effect": "Deny",
      "Principal": {
        "AWS": "*"
      },
      "Action": [
        "dsql:DbConnect",
        "dsql:DbConnectAdmin"
      ],
      "Resource": "*",
      "Condition": {
        "ForAnyValue:StringNotLike": {
          "aws:PrincipalOrgPaths": "o-exampleorgid/r-examplerootid/ou-exampleouid/*"
        }
      }
    }
  ]
}
```

## Multi-Region cluster policies
<a name="rbp-example-multi-region"></a>

For multi-Region clusters, each regional cluster maintains its own resource policy, allowing for Region-specific controls. In the following example, each policy denies connections that don't come from a specific VPC in its Region:

*us-east-1 policy:*

```
{
  "Version": "2012-10-17",		 	 	 
  "Statement": [
    {
      "Effect": "Deny",
      "Principal": {
        "AWS": "*"
      },
      "Resource": "*",
      "Action": [
        "dsql:DbConnect",
        "dsql:DbConnectAdmin"
      ],
      "Condition": {
        "StringNotEquals": {
          "aws:SourceVpc": "vpc-0a1b2c3d4e5f67890"
        }
      }
    }
  ]
}
```

*us-east-2 policy:*

```
{
  "Version": "2012-10-17",		 	 	 
  "Statement": [
    {
      "Effect": "Deny",
      "Principal": {
        "AWS": "*"
      },
      "Resource": "*",
      "Action": [
        "dsql:DbConnect",
        "dsql:DbConnectAdmin"
      ],
      "Condition": {
        "StringNotEquals": {
          "aws:SourceVpc": "vpc-0f9e8d7c6b5a43210"
        }
      }
    }
  ]
}
```

**Note**  
Condition context keys may vary between AWS Regions (such as VPC IDs).