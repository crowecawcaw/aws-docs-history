

**AWS Mainframe Modernization self-managed experience** is no longer open to new customers. For capabilities similar to AWS Mainframe Modernization self-managed experience, explore capabilities from vendor-direct offerings and from AWS Transform. Existing customers can continue to use the service as normal. For more information, see [AWS Mainframe Modernization availability change](https://docs.aws.amazon.com/m2/latest/userguide/mainframe-modernization-availability-change.html). 

**AWS Mainframe Modernization Service (Managed Runtime Environment experience)** is no longer open to new customers. For capabilities similar to AWS Mainframe Modernization Service (Managed Runtime Environment experience) explore AWS Mainframe Modernization Service (Self-Managed Experience). Existing customers can continue to use the service as normal. For more information, see [AWS Mainframe Modernization availability change](https://docs.aws.amazon.com/m2/latest/userguide/mainframe-modernization-availability-change.html). 

# Create the AWS Identity and Access Management role
<a name="mf-runtime-setup-iam-role"></a>

Create an AWS Identity and Access Management policy and role to be used by the AWS Mainframe Modernization Amazon EC2 instances. Creating the role through the IAM console will create an associated instance profile of the same name. Assigning this instance profile to the Amazon EC2 instances allows Rocket Software Licenses to be assigned. For more information on instance profiles, see [Using an IAM role to grant permissions to applications running on Amazon EC2 instances](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_switch-role-ec2.html).

## Create an IAM policy
<a name="mf-runtime-setup-iam-role-policy"></a>

An IAM policy is created first and then attached to the role.

1. Navigate to AWS Identity and Access Management in the AWS Management Console.

1. Choose **Policies** and then **Create Policy**.  
![Policy page with no filters applied.](http://docs.aws.amazon.com/m2/latest/userguide/images/mf-create-iam-policy_1.png)

1. Choose the **JSON** tab.  
![JSON tab with no content](http://docs.aws.amazon.com/m2/latest/userguide/images/mf-create-iam-policy_2.png)

1. Replace `us-west-1` in the following JSON with the AWS Region where the Amazon S3 endpoint was defined, then copy and paste the JSON into the policy editor.

------
#### [ JSON ]

****  

   ```
   {
       "Version":"2012-10-17",		 	 	 
       "Statement": [
           {
               "Sid": "S3WriteObject",
               "Effect": "Allow",
               "Action": [
                   "s3:PutObject"
               ],
               "Resource": [
                   "arn:aws:s3:::aws-supernova-marketplace-us-west-1-prod/*"
               ]
           },
           {
               "Sid": "OtherRequiredActions",
               "Effect": "Allow",
               "Action": [
                   "sts:GetCallerIdentity",
                   "ec2:DescribeInstances",
                   "license-manager:ListReceivedLicenses"
               ],
               "Resource": [
                   "*"
               ]
           }
       ]
   }
   ```

------
**Note**  
The Actions under the Sid `OtherRequiredActions` do not support resource-level permissions and must specify `*` in the resource element.  
![JSON tab with policy entered and us-west-1 highlighted.](http://docs.aws.amazon.com/m2/latest/userguide/images/mf-create-iam-policy_3.png)

1. Choose **Next: Tags**.  
![Tags with no data entered.](http://docs.aws.amazon.com/m2/latest/userguide/images/mf-create-iam-policy_4.png)

1. Optionally enter any tags, then choose **Next: Review**.

1. Enter a name for the policy, for example “Micro-Focus-Licensing-policy”. Optionally enter a description, for example “A role that includes this policy must be attached to each AWS Mainframe Modernization Amazon EC2 instance.”  
![Review policy with name and description entered.](http://docs.aws.amazon.com/m2/latest/userguide/images/mf-create-iam-policy_5.png)

1. Choose **Create Policy**.

## Create the IAM role
<a name="mf-runtime-setup-iam-role-create"></a>

After creating an IAM policy, you create an IAM role and attach it to the policy. 

1. Navigate to IAM in the AWS Management Console.

1. Choose **Roles** and then **Create Role**.  
![Roles with no filter applied.](http://docs.aws.amazon.com/m2/latest/userguide/images/mf-create-iam-role_1.png)

1. Leave **Trusted entity type** as **AWS service** and choose the **EC2** common use case.  
![Select trusted entity with AWS service and EC2 selected](http://docs.aws.amazon.com/m2/latest/userguide/images/mf-create-iam-role_2.png)

1. Choose **Next**.

1. Enter “Micro” into the filter and press enter to apply the filter.

1. Choose the policy that was just created, for example the “Micro-Focus-Licensing-policy”. 

1. Choose **Next**.  
![Add permissions with Micro Focus policy selected.](http://docs.aws.amazon.com/m2/latest/userguide/images/mf-create-iam-role_3.png)

1. Enter the Role name, for example “Micro-Focus-Licensing-role”. 

1. Replace the description with one of your own, for example “Allows Amazon EC2 instances with this role to obtain Micro Focus Licenses”.   
![Role details with name and description entered.](http://docs.aws.amazon.com/m2/latest/userguide/images/mf-create-iam-role_4.png)

1. Under **Step 1: Select trusted entities** review the JSON and confirm it has the following values:

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
                   "sts:AssumeRole"
               ],
               "Principal": {
                   "Service": [
                       "ec2.amazonaws.com"
                   ]
               }
           }
       ]
   }
   ```

------
**Note**  
The order of the Effect, Action, and Principal are not significant.

1. Confirm that **Step 2: Add permissions** shows your Licensing policy.  
![Step 2: Add permissions with licensing policy selected.](http://docs.aws.amazon.com/m2/latest/userguide/images/mf-create-iam-role_6.png)

1. Choose **Create role**.

After the allowlist request is complete, continue with the following steps.