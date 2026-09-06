

# DynamoDB resource-based policy examples
<a name="rbac-examples"></a>

When you specify an ARN in the `Resource` field of a resource-based policy, the policy takes effect only if the specified ARN matches the ARN of the DynamoDB resource to which it is attached.

**Note**  
Remember to replace the {{italicized}} text with your resource-specific information.

## Resource-based policy for a table
<a name="rbac-examples-get"></a>

The following resource-based policy attached to a DynamoDB table named {{MusicCollection}}, gives the IAM users {{John}} and {{Jane}} permission to perform [GetItem](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_GetItem.html) and [BatchGetItem](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_BatchGetItem.html) actions on the {{MusicCollection}} resource.

------
#### [ JSON ]

****  

```
{
  "Version":"2012-10-17",		 	 	 
  "Statement": [
    {
      "Sid": "1111",
        "Effect": "Allow",
        "Principal": {
          "AWS": [
            "arn:aws:iam::{{111122223333}}:user/{{username}}",
            "arn:aws:iam::{{111122223333}}:user/{{Jane}}"
          ]
        },
        "Action": [
          "dynamodb:GetItem",
          "dynamodb:BatchGetItem"
        ],
        "Resource": [
          "arn:aws:dynamodb:{{us-east-1}}:{{123456789012}}:table/{{MusicCollection}}"
        ]
    }
  ]
}
```

------

## Resource-based policy for a stream
<a name="rbac-examples-streams"></a>

The following resource-based policy attached to a DynamoDB stream named `2024-02-12T18:57:26.492` gives the IAM users {{John}} and {{Jane}} permission to perform [GetRecords](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_streams_GetRecords.html), [GetShardIterator](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_streams_GetShardIterator.html), and [DescribeStream](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_streams_DescribeStream.html) API actions on the `2024-02-12T18:57:26.492` resource.

------
#### [ JSON ]

****  

```
{
  "Version":"2012-10-17",		 	 	 
  "Statement": [
    {
      "Sid": "1111",
      "Effect": "Allow",
      "Principal": {
        "AWS": [
          "arn:aws:iam::{{111122223333}}:user/{{username}}",
          "arn:aws:iam::{{111122223333}}:user/{{Jane}}"
        ]
      },
      "Action": [
        "dynamodb:DescribeStream",
        "dynamodb:GetRecords",
        "dynamodb:GetShardIterator"
      ],
      "Resource": [
        "arn:aws:dynamodb:{{us-east-1}}:{{123456789012}}:table/{{MusicCollection}}/stream/{{2024-02-12T18:57:26.492}}"
      ]
    }
  ]
}
```

------

## Resource-based policy for access to perform all actions on specified resources
<a name="rbac-examples-wildcard"></a>

To allow a user to perform all actions on a table and all associated indexes with a table, you can use a wildcard (\*) to represent the actions and the resources associated with the table. Using a wild card character for the resources, will allow the user access to the DynamoDB table and all its associated indexes, including the ones that haven’t yet been created. For example, the following policy will give the user {{John}} permission to perform any actions on the {{MusicCollection}} table and all of its indexes, including any indexes that will be created in the future.

------
#### [ JSON ]

****  

```
{
  "Version":"2012-10-17",		 	 	 
  "Statement": [
    {
      "Sid": "1111",
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::{{111122223333}}:user/{{username}}"
      },
      "Action": "dynamodb:*",
      "Resource": [
        "arn:aws:dynamodb:{{us-east-1}}:{{123456789012}}:table/{{MusicCollection}}",
        "arn:aws:dynamodb:{{us-east-1}}:{{123456789012}}:table/{{MusicCollection}}/index/{{index-name}}"
      ]
    }
  ]
}
```

------

## Resource-based policy for cross-account access
<a name="rbac-examples-cross-account"></a>

You can specify permissions for a cross-account IAM identity to access DynamoDB resources. For example, you might need a user from a trusted account to get access to read the contents of your table, with the condition that they access only specific items and specific attributes in those items. The following policy allows access to user {{John}} from a trusted AWS account ID {{111111111111}} to access data from a table in account {{123456789012}} by using the [GetItem](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_GetItem.html) API. The policy ensures that the user can access only items with a primary key {{Jane}} and that the user can only retrieve the attributes `Artist` and `SongTitle`, but no other attributes.

**Important**  
If you do not specify the `SPECIFIC_ATTRIBUTES` condition, you'll see all attributes for the items returned.

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Sid": "CrossAccountTablePolicy",
            "Effect": "Allow",
            "Principal": {
                "AWS": "arn:aws:iam::111111111111:user/John"
            },
            "Action": "dynamodb:GetItem",
            "Resource": [
                "arn:aws:dynamodb:us-west-2:123456789012:table/MusicCollection"
            ],
            "Condition": {
                "ForAllValues:StringEquals": {
                    "dynamodb:LeadingKeys": "Jane",
                    "dynamodb:Attributes": [
                        "Artist",
                        "SongTitle"
                    ]
                },
                "StringEquals": {
                    "dynamodb:Select": "SPECIFIC_ATTRIBUTES"
                }
            }
        }
    ]
}
```

------

In addition to the preceding resource-based policy, the identity-based policy attached to the user {{John}} also needs to allow the `GetItem` API action for the cross-account access to work. The following is an example of an identity-based policy that you must attach to the user {{John}}.

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Sid": "CrossAccountIdentityBasedPolicy",
            "Effect": "Allow",
            "Action": [
                "dynamodb:GetItem"
            ],
            "Resource": [
                "arn:aws:dynamodb:{{us-east-1}}:{{123456789012}}:table/{{MusicCollection}}"
            ],
            "Condition": {
                "ForAllValues:StringEquals": {
                    "dynamodb:LeadingKeys": "{{Jane}}",
                    "dynamodb:Attributes": [
                        "Artist",
                        "SongTitle"
                    ]
                },
                "StringEquals": {
                    "dynamodb:Select": "SPECIFIC_ATTRIBUTES"
                }
            }
        }
    ]
}
```

------

The user John can make a `GetItem` request by specifying the table ARN in the `table-name` parameter for accessing the table {{MusicCollection}} in the account {{123456789012}}.

```
aws dynamodb get-item \
    --table-name arn:aws:dynamodb:us-west-2:{{123456789012}}:table/{{MusicCollection}} \
    --key '{"Artist": {"S": "{{Jane}}"}' \
    --projection-expression 'Artist, SongTitle' \
    --return-consumed-capacity TOTAL
```

## Resource-based policy with IP address conditions
<a name="rbac-examples-conditions"></a>

You can apply a condition to restrict source IP addresses, virtual private clouds (VPCs), and VPC endpoint (VPCE). You can specify permissions based on the source addresses of the originating request. For example, you might want to allow a user to access DynamoDB resources only if they are being accessed from a specific IP source, such as a corporate VPN endpoint. Specify these IP addresses in the `Condition` statement.

The following example allows the user {{John}} access to any DynamoDB resource when the source IPs are `54.240.143.0/24` and `2001:DB8:1234:5678::/64`.

------
#### [ JSON ]

****  

```
{
  "Id":"PolicyId2",
  "Version":"2012-10-17",		 	 	 
  "Statement":[
    {
      "Sid":"AllowIPmix",
      "Effect":"Allow",
      "Principal": {
        "AWS": "arn:aws:iam::{{111111111111}}:user/{{username}}"
      },
      "Action":"dynamodb:*",
      "Resource":"*",
      "Condition": {
        "IpAddress": {
          "aws:SourceIp": [
            "54.240.143.0/24",
            "2001:DB8:1234:5678::/64"
          ]
        }
      }
    }
  ]
}
```

------

You can also deny all access to DynamoDB resources except when the source is a specific VPC endpoint, for example {{vpce-1a2b3c4d}}.

**Important**  
A resource-based policy that contains only a `Deny` statement with `"Principal": "*"` denies access to every principal, including your own ability to update or delete the policy later. If you attach a policy that would lock you out in this way, DynamoDB rejects it with the following error: *The new resource policy will not allow you to update the resource policy in the future.* Adding a separate `Allow` statement does not resolve this, because an explicit `Deny` always overrides an `Allow`. To deny access to everyone except a specific VPC endpoint while retaining the ability to manage the policy, exempt the administering principal from the `Deny` statement by adding an `ArnNotEquals` condition on `aws:PrincipalArn`, as shown in the following example.

**Important**  
When you use DAX with DynamoDB tables that have IP-based resource policies in IPv6-only environments, you must configure additional access rules. If your resource policy restricts access to the IPv4 address space `0.0.0.0/0` on tables, you must allow access for the IAM role associated with your DAX cluster. Add an `ArnNotEquals` condition to your policy to ensure DAX maintains access to your DynamoDB tables. For more information see, [DAX and IPv6](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DAX.create-cluster.DAX_and_IPV6.html).

------
#### [ JSON ]

****  

```
{
  "Id":"PolicyId",
  "Version":"2012-10-17",		 	 	 
  "Statement": [
    {
      "Sid": "AccessToSpecificVPCEOnly",
      "Principal": "*",
      "Action": "dynamodb:*",
      "Effect": "Deny",
      "Resource": "*",
      "Condition": {
        "StringNotEquals":{
          "aws:sourceVpce":"{{vpce-1a2b3c4d}}"
        },
        "ArnNotEquals":{
          "aws:PrincipalArn":"{{arn:aws:iam::123456789012:role/AdminRole}}"
        }
      }
    }
  ]
}
```

------

## Resource-based policy using an IAM role
<a name="rbac-examples-iam"></a>

You can also specify an IAM service role in the resource-based policy. IAM entities that assume this role are bounded by the permissible actions specified for the role and to the specific set of resources within the resource-based policy.

The following example allows an IAM entity to perform all DynamoDB actions on the {{MusicCollection}} and {{MusicCollection}} DynamoDB resources.

------
#### [ JSON ]

****  

```
{
  "Version":"2012-10-17",		 	 	 
  "Statement": [
    {
      "Sid": "1111",
      "Effect": "Allow",
      "Principal": { "AWS": "arn:aws:iam::{{111122223333}}:role/{{role-name}}" },
      "Action": "dynamodb:*",
      "Resource": [
        "arn:aws:dynamodb:{{us-east-1}}:{{123456789012}}:table/{{MusicCollection}}",
        "arn:aws:dynamodb:{{us-east-1}}:{{123456789012}}:table/{{MusicCollection}}/*"
      ]
    }
  ]
}
```

------