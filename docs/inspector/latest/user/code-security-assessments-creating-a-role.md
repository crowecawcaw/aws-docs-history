

# Creating roles for Amazon Inspector Code Security

 To use Amazon Inspector Code Security with GitHub Enterprise Server or GitLab Self-Managed instances in private networks, you must create an IAM role with specific permissions. 

## IAM role for private network connectivity
<a name="w2aac17b9b5b5"></a>

 If you plan to connect Amazon Inspector Code Security to GitHub Enterprise Server or GitLab Self-Managed instances in private networks, you must create an IAM role with permissions to manage network resources and AWS CodeConnections. You can create this role using a CloudFormation template or manually in IAM. 

**Important**  
 This role is only required for private network connectivity configurations. If you are connecting to publicly accessible repositories, you do not need to create this role. 

### Creating the role with a CloudFormation template
<a name="w2aac17b9b5b5b7"></a>

 Use the following CloudFormation template to automate the creation of the IAM role for private network connectivity. You can customize the role name in the template. 

```json
{
    "AWSTemplateFormatVersion": "2010-09-09",
    "Resources": {
        "InspectorCodeSecurityPrivateNetworkRole": {
            "Type": "AWS::IAM::Role",
            "Properties": {
                "RoleName": "InspectorCodeSecurityPrivateNetworkRole",
                "AssumeRolePolicyDocument": {
                    "Version": "2012-10-17",		 	 	 
                    "Statement": [
                        {
                            "Effect": "Allow",
                            "Principal": {
                                "Service": "inspector2.amazonaws.com"
                            },
                            "Action": "sts:AssumeRole"
                        }
                    ]
                },
                "Policies": [
                    {
                        "PolicyName": "VPCNetworkAccess",
                        "PolicyDocument": {
                            "Version": "2012-10-17",		 	 	 
                            "Statement": [
                                {
                                    "Sid": "VPCAndNetworkManagement",
                                    "Effect": "Allow",
                                    "Action": [
                                        "ec2:DescribeVpcs",
                                        "ec2:DescribeVpcEndpoints",
                                        "ec2:DescribeSecurityGroups",
                                        "ec2:DescribeSubnets",
                                        "ec2:DeleteNetworkInterface",
                                        "ec2:CreateNetworkInterface",
                                        "ec2:DescribeNetworkInterfaces",
                                        "ec2:CreateTags",
                                        "ec2:DescribeDhcpOptions"
                                    ],
                                    "Resource": "*"
                                }
                            ]
                        }
                    },
                    {
                        "PolicyName": "CodeConnectionsAccess",
                        "PolicyDocument": {
                            "Version": "2012-10-17",		 	 	 
                            "Statement": [
                                {
                                    "Sid": "CodeConnectionsHostManagement",
                                    "Effect": "Allow",
                                    "Action": [
                                        "codeconnections:ListHostInternal",
                                        "codeconnections:GetHost",
                                        "codeconnections:DeleteHostInternal"
                                    ],
                                    "Resource": "*"
                                }
                            ]
                        }
                    }
                ]
            }
        }
    }
}
```

### Creating the role manually in IAM
<a name="w2aac17b9b5b5b9"></a>

 To create the role manually, follow these steps: 

1.  Open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/). 

1.  In the navigation pane, choose **Roles**, and then choose **Create role**. 

1.  For **Trusted entity type**, choose **AWS service**. 

1.  For **Service or use case**, choose **EC2**, then choose **Next**. 

1.  Choose **Create policy** to create a new policy with the required permissions. 

1.  In the policy editor, choose the **JSON** tab and paste the following policy document: 

   ```json
   {
       "Version": "2012-10-17",		 	 	 
       "Statement": [
           {
               "Sid": "VPCAndNetworkManagement",
               "Effect": "Allow",
               "Action": [
                   "ec2:DescribeVpcs",
                   "ec2:DescribeVpcEndpoints",
                   "ec2:DescribeSecurityGroups",
                   "ec2:DescribeSubnets",
                   "ec2:DeleteNetworkInterface",
                   "ec2:CreateNetworkInterface",
                   "ec2:DescribeNetworkInterfaces",
                   "ec2:CreateTags",
                   "ec2:DescribeDhcpOptions"
               ],
               "Resource": "*"
           },
           {
               "Sid": "CodeConnectionsHostManagement",
               "Effect": "Allow",
               "Action": [
                   "codeconnections:ListHostInternal",
                   "codeconnections:GetHost",
                   "codeconnections:DeleteHostInternal"
               ],
               "Resource": "*"
           }
       ]
   }
   ```

1.  Choose **Next**, provide a policy name such as `InspectorCodeSecurityPrivateNetworkPolicy`, and choose **Create policy**. 

1.  Return to the role creation workflow, attach the policy you just created, and choose **Next**. 

1.  For **Role name**, enter a name for your role (for example, `InspectorCodeSecurityPrivateNetworkRole`). 

1.  Update the trust policy to allow Amazon Inspector to assume the role. Choose **Edit** in the **Trust relationships** section and replace the trust policy with: 

   ```json
   {
       "Version": "2012-10-17",		 	 	 
       "Statement": [
           {
               "Effect": "Allow",
               "Principal": {
                   "Service": "inspector2.amazonaws.com"
               },
               "Action": "sts:AssumeRole"
           }
       ]
   }
   ```

1.  Choose **Create role**. 

 After creating the role, you can use it when configuring private network connectivity for GitHub Enterprise Server or GitLab Self-Managed integrations. 