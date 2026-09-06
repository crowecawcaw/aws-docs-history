

# Identity-based policy examples for AWS PrivateLink
<a name="security_iam_id-based-policy-examples"></a>

By default, users and roles don't have permission to create or modify AWS PrivateLink resources. To grant users permission to perform actions on the resources that they need, an IAM administrator can create IAM policies.

To learn how to create an IAM identity-based policy by using these example JSON policy documents, see [Create IAM policies (console)](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create-console.html) in the *IAM User Guide*.

For details about actions and resource types defined by AWS PrivateLink, including the format of the ARNs for each of the resource types, see [Actions, resources, and condition keys for Amazon EC2](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonec2.html) in the *Service Authorization Reference*.

**Topics**
+ [Control the use of VPC endpoints](#endpoints-example)
+ [Control VPC endpoints creation based on the service owner](#create-endpoints-example)
+ [Control the private DNS names that can be specified for VPC endpoint services](#private-dns-name-example)
+ [Control the service names that can be specified for VPC endpoint services](#service-names-example)

## Control the use of VPC endpoints
<a name="endpoints-example"></a>

By default, users do not have permission to work with endpoints. You can create an identity-based policy that grants users permission to create, modify, describe, and delete endpoints. The following is an example.

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement":[
        {
            "Effect": "Allow",
            "Action":"ec2:*VpcEndpoint*",
            "Resource":"*"
        }
    ]
}
```

------

For information about controlling access to services using VPC endpoints, see [Control access to VPC endpoints using endpoint policies](vpc-endpoints-access.md).

## Control VPC endpoints creation based on the service owner
<a name="create-endpoints-example"></a>

You can use the `ec2:VpceServiceOwner` condition key to control what VPC endpoint can be created based on who owns the service (`amazon`, `aws-marketplace`, or the account ID). The following example grants permission to create VPC endpoints with the specified service owner. To use this example, substitute the Region, the account ID, and the service owner.

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "ec2:CreateVpcEndpoint",
            "Resource": [
                "arn:aws:ec2:{{us-east-1}}:{{111111111111}}:vpc/*",
                "arn:aws:ec2:{{us-east-1}}:{{111111111111}}:security-group/*",
                "arn:aws:ec2:{{us-east-1}}:{{111111111111}}:subnet/*",
                "arn:aws:ec2:{{us-east-1}}:{{111111111111}}:route-table/*"
            ]
        },
        {
            "Effect": "Allow",
            "Action": "ec2:CreateVpcEndpoint",
            "Resource": [
                "arn:aws:ec2:{{us-east-1}}:{{111111111111}}:vpc-endpoint/*"
            ],
            "Condition": {
                "StringEquals": {
                    "ec2:VpceServiceOwner": [
                        "{{amazon}}"
                    ]
                }
            }
        }
    ]
}
```

------

## Control the private DNS names that can be specified for VPC endpoint services
<a name="private-dns-name-example"></a>

You can use the `ec2:VpceServicePrivateDnsName` condition key to control what VPC endpoint service can be modified or created based on the private DNS name associated with the VPC endpoint service. The following example grants permission to create a VPC endpoint service with the specified private DNS name. To use this example, substitute the Region, the account ID, and the private DNS name.

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "ec2:ModifyVpcEndpointServiceConfiguration",
                "ec2:CreateVpcEndpointServiceConfiguration"
            ],
            "Resource": [
                "arn:aws:ec2:{{us-east-1}}:{{111111111111}}:vpc-endpoint-service/*"
            ],
            "Condition": {
                "StringEquals": {
                    "ec2:VpceServicePrivateDnsName": [
                        "{{example.com}}"
                    ]
                }
            }
        }
    ]
}
```

------

## Control the service names that can be specified for VPC endpoint services
<a name="service-names-example"></a>

You can use the `ec2:VpceServiceName` condition key to control what VPC endpoint can be created based on the VPC endpoint service name. The following example grants permission to create a VPC endpoint with the specified service name. To use this example, substitute the Region, the account ID, and the service name.

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "ec2:CreateVpcEndpoint",
            "Resource": [
                "arn:aws:ec2:{{us-east-1}}:{{111111111111}}:vpc/*",
                "arn:aws:ec2:{{us-east-1}}:{{111111111111}}:security-group/*",
                "arn:aws:ec2:{{us-east-1}}:{{111111111111}}:subnet/*",
                "arn:aws:ec2:{{us-east-1}}:{{111111111111}}:route-table/*"
            ]
        },
        {
            "Effect": "Allow",
            "Action": "ec2:CreateVpcEndpoint",
            "Resource": [
                "arn:aws:ec2:{{us-east-1}}:{{111111111111}}:vpc-endpoint/*"
            ],
            "Condition": {
                "StringEquals": {
                    "ec2:VpceServiceName": [
                        "com.amazonaws.{{111111111111}}.{{s3}}"
                    ]
                }
            }
        }
    ]
}
```

------