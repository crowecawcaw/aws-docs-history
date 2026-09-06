

End of support notice: On March 31, 2027, AWS will end support for AWS Service Management Connector. After March 31, 2027, you will no longer be able to access the AWS Service Management Connector console or AWS Service Management Connector resources. For more information, see [AWS Service Management Connector end of support](https://docs.aws.amazon.com/smc/latest/ag/smc-end-of-support.html). 

# Creating the AWS Service Management Connector Sync user
<a name="scsyncuser"></a>

This section describes how to create the AWS Sync user and associate the appropriate IAM permission. To perform this task, you need IAM permissions to create new users. The following steps to create a Sync user and End user are not required if you use the CloudFormation template to deploy the permissions. Review [Setting baseline permissions for AWS Service Management Connector for ServiceNow](sn-base-perms.md) for more information. 

**Note**  
The CloudFormation template to set up the AWS configurations of the Connector for ServiceNow creates the Sync user and End user with the required permissions for all the supported integrations. 

**To create AWS Service Management Connector sync user**

1. Follow the instructions in [Creating an IAM user in your AWS account](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_create.html) to create a sync user (SMSyncUser). The user needs programmatic and AWS Management Console access to follow the Connector for ServiceNow installation instructions. 

1. Set permissions for your sync user (SMSyncUser). Choose **Attach existing policies directly** and select:
   + **`AWSServiceCatalogAdminReadOnlyAccess`** (AWS managed policy)
   + **`AmazonSSMReadOnlyAccess`** (AWS managed policy)
   + **`AWSConfigUserAccess`** (AWS managed policy)
   + **`AWSSupportAccess`** (AWS managed policy)

1. Create this policy: `ConfigBidirectionalPolicy`. Then follow the instructions in [Creating IAM Policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create.html), and add this code in the JSON editor: 

------
#### [ JSON ]

****  

   ```
   {
      "Version":"2012-10-17",		 	 	 
      "Statement": [
        {
            "Action": [
            "cloudformation:RegisterType",
            "cloudformation:DescribeTypeRegistration",
            "cloudformation:DeregisterType",
            "config:PutResourceConfig"
        ],
        "Resource": "*",
        "Effect": "Allow"
        }
      ]
   }
   ```

------

   The provided AWS Configuration template consists of two policies: `ConfigBiDirectionalPolicy` and `SecurityHubPolicy`.

1. Create this policy: `SecurityHubPolicy`. Then follow the instructions in [Creating IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create.html), and add this code in the JSON editor:

------
#### [ JSON ]

****  

   ```
   {
       "Version":"2012-10-17",		 	 	 
       "Statement": [
           {
               "Action": [
                   "sqs:ReceiveMessage",
                   "sqs:DeleteMessage"
               ],
               "Resource": "arn:aws:sqs:{{us-east-1}}:{{111122223333}}:{{QueueName}}",
               "Effect": "Allow"
           },
           {
               "Action": [
                   "securityhub:BatchUpdateFindings"
               ],
               "Resource": "*",
               "Effect": "Allow"
           }
       ]
   }
   ```

------

1. Create this policy: `OpsCenterExecutionPolicy.` Then follow the instructions in [Creating IAM Policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create.html) and add this code in the JSON editor:

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
                   "ssm:CreateOpsItem",
                   "ssm:GetOpsItem",
                   "ssm:UpdateOpsItem",
                   "ssm:DescribeOpsItems"
                ],
               "Resource": "*"
           }
       ]
   }
   ```

------

1. Create this policy: `AWSIncidentBaselinePolicy`. Then follow the instructions in [Creating IAM Policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create.html) and add this code in the JSON editor:

------
#### [ JSON ]

****  

   ```
   {
       "Version":"2012-10-17",		 	 	 
       "Statement": [
           {
               "Action": [
                   "ssm-incidents:ListIncidentRecords",
                   "ssm-incidents:GetIncidentRecord",
                   "ssm-incidents:UpdateRelatedItems",
                   "ssm-incidents:ListTimelineEvents",
                   "ssm-incidents:GetTimelineEvent",
                   "ssm-incidents:UpdateIncidentRecord",
                   "ssm-incidents:ListRelatedItems",
                   "ssm:ListOpsItemRelatedItems"
               ],
               "Resource": "*",
               "Effect": "Allow"
           }
       ]
   }
   ```

------

1. [Optional] Create this policy: `AWSChangeManagerCloudtrailPolicy`. Then follow the instructions in [Creating IAM Policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create.html) and add this code in the JSON editor:

------
#### [ JSON ]

****  

   ```
   {
       "Version":"2012-10-17",		 	 	 
       "Statement": [
           {
               "Action": [
                   "cloudtrail:DescribeQuery",
                   "cloudtrail:ListEventDataStores",
                   "cloudtrail:StartQuery",
                   "cloudtrail:GetQueryResults"
               ],
               "Resource": "*",
               "Effect": "Allow"
           }
       ]
   }
   ```

------

1. Create this policy: `DescribeWorkSpacesPolicy`. Then follow the instructions in [Creating IAM Policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create.html) and add this code in the JSON editor:

------
#### [ JSON ]

****  

   ```
   {
     "Version":"2012-10-17",		 	 	 
     "Statement": [
       {
         "Action": ["workspaces:DescribeWorkspaces"],
         "Effect": "Allow",
         "Resource": "*"
       }
     ]
   }
   ```

------

1. Add a policy that allows `budgets:ViewBudget` on all resources (\*). 

1. Review and choose **Create User**. 

1. Note the access and secret access information. Download the .csv file that contains the user credential information.

**Note**  
To align with best practices, AWS recommends periodically rotating IAM user access keys. For more information, refer to [Manage access keys for IAM users](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html#securing_access-keys).