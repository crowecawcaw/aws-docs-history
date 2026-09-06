

End of support notice: On March 31, 2027, AWS will end support for AWS Service Management Connector. After March 31, 2027, you will no longer be able to access the AWS Service Management Connector console or AWS Service Management Connector resources. For more information, see [AWS Service Management Connector end of support](https://docs.aws.amazon.com/smc/latest/ag/smc-end-of-support.html). 

# Creating SCConnectLaunch Role
<a name="jsd-creating-scconnectlaunch-role"></a>

The following section describes how to create the **SCConnectLaunch** role. This role places baseline AWS service permissions into the Service Catalog launch constraints. For more information, see CORRECT LINK.

**To create SCConnectLaunch role**

1. Create the **AWSCloudFormationFullAccess** policy. Choose **create policy** and then paste the following in the JSON editor.

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
               "cloudformation:DescribeStackResource",
               "cloudformation:DescribeStackResources",
               "cloudformation:GetTemplate",
               "cloudformation:List*",
               "cloudformation:DescribeStackEvents",
               "cloudformation:DescribeStacks",
               "cloudformation:CreateStack",
               "cloudformation:DeleteStack",
               "cloudformation:DescribeStackEvents",
               "cloudformation:DescribeStacks",
               "cloudformation:GetTemplateSummary",
               "cloudformation:SetStackPolicy",
               "cloudformation:ValidateTemplate",
               "cloudformation:UpdateStack",
               "cloudformation:CreateChangeSet",
               "cloudformation:DescribeChangeSet",
               "cloudformation:ExecuteChangeSet",
               "cloudformation:DeleteChangeSet",
               "s3:GetObject"
               ],
               "Resource": "*"
           }
       ]
   }
   ```

------

1. Create a policy called **ServiceCatalogSSMActionsBaseline**. Follow the instructions in [Creating IAM Policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create.html), and paste the following into the JSON editor.

------
#### [ JSON ]

****  

   ```
    {
       "Version":"2012-10-17",		 	 	 
       "Statement": [
           {
               "Sid": "Stmt1536341175150",
               "Action": [
                   "servicecatalog:ListServiceActionsForProvisioningArtifact",
                   "servicecatalog:ExecuteprovisionedProductServiceAction",
                   "ssm:DescribeDocument",
                   "ssm:GetAutomationExecution",
                   "ssm:StartAutomationExecution",
                   "ssm:StopAutomationExecution",
                   "cloudformation:ListStackResources",
                   "ec2:DescribeInstanceStatus",
                   "ec2:StartInstances",
                   "ec2:StopInstances"
               ],
               "Effect": "Allow",
               "Resource": "*"
           }
       ]
   }
   ```

------

1. Create the **SCConnectLaunch** role. Assign the trust relationship to Service Catalog.

------
#### [ JSON ]

****  

   ```
   {
     "Version":"2012-10-17",		 	 	 
     "Statement": [
       {
         "Sid": "",
         "Effect": "Allow",
         "Principal": {
           "Service": "servicecatalog.amazonaws.com"
         },
         "Action": "sts:AssumeRole"
       }
     ]
   }
   ```

------

1. Attach the relevant policies to the **SCConnectLaunch** role. Attach the following baseline IAM policies:
   + **AmazonEC2FullAccess** (AWS managed policy)
   + **AmazonS3FullAccess ** (AWS managed policy)
   + **AWSCloudFormationFullAccess** (custom managed policy)
   + **ServiceCatalogSSMActionsBaseline** (custom managed policy)

**Note**  
You can use the available AWS CloudFormation templates for the JSM connector to configure your AWS account to enable AWS Service Catalog integration. This stack includes the *Sync user* and *End user* roles, which attach the required permissions for all available integrations. For more information, see [Baseline Permissions](https://docs.aws.amazon.com/smc/latest/ag/jsd-baseline-permissions.html).