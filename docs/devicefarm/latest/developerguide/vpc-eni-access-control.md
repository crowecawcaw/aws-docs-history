

# AWS access control and IAM
<a name="vpc-eni-access-control"></a>

AWS Device Farm allows you to use [AWS Identity and Access Management](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html) (IAM) to create policies granting or restricting access to Device Farm's features. To use the VPC Connectivity feature with AWS Device Farm, the following IAM Policy is required for the user account or role that you are using to access AWS Device Farm:

------
#### [ JSON ]

****  

```
{
  "Version":"2012-10-17",		 	 	 
  "Statement": [{
      "Effect": "Allow",
      "Action": [
        "devicefarm:*",
        "ec2:DescribeVpcs",
        "ec2:DescribeSubnets",
        "ec2:DescribeSecurityGroups",
        "ec2:CreateNetworkInterface"
      ],
      "Resource": [
        "*"
      ]
    },
    {
      "Effect": "Allow",
      "Action": "iam:CreateServiceLinkedRole",
      "Resource": "arn:aws:iam::*:role/aws-service-role/devicefarm.amazonaws.com/AWSServiceRoleForDeviceFarm",
      "Condition": {
        "StringLike": {
          "iam:AWSServiceName": "devicefarm.amazonaws.com"
        }
      }
    }
  ]
}
```

------

To create or update a Device Farm project with a VPC configuration, your IAM policy must allow you to call the following actions against the resources listed in the VPC configuration:

```
"ec2:DescribeVpcs"
"ec2:DescribeSubnets"
"ec2:DescribeSecurityGroups"
"ec2:CreateNetworkInterface"
```

Additionally, your IAM policy must also allow for the creation of the service-linked role:

```
"iam:CreateServiceLinkedRole"
```

**Note**  
None of these permissions are required for users who don't use VPC configurations in their projects.