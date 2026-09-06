

End of support notice: On March 31, 2027, AWS will end support for AWS Service Management Connector. After March 31, 2027, you will no longer be able to access the AWS Service Management Connector console or AWS Service Management Connector resources. For more information, see [AWS Service Management Connector end of support](https://docs.aws.amazon.com/smc/latest/ag/smc-end-of-support.html). 

# Creating the SCConnectLaunch role
<a name="scconnectlaunchrole"></a>

The `SCConnectLaunch` role is an IAM role that places baseline AWS service permissions into the AWS Service Catalog launch constraints. Configuring this role enables segregation of duty through provisioning product resources for ServiceNow end users. 

The `SCConnectLaunch` role baseline contains permissions to Amazon EC2 and Amazon S3 services. If your products contain more AWS services, you must either include those services in the `SCConnectLaunch` role or create new launch roles.

This section describes how to create the `SCConnectLaunch` role. This role places baseline AWS service permissions in the Service Catalog launch constraints. For more information, see [Service Catalog Launch Constraints](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/constraints-launch.html).

****To create SCConnectLaunch role****

1. Create this policy: `AWSCloudFormationFullAccess` policy. Choose **create policy** and add this code in the JSON editor:

------
#### [ JSON ]

****  

   ```
   {
      "Version":"2012-10-17",		 	 	 
      "Statement":[
         {
            "Effect":"Allow",
            "Action":[
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
            "Resource":"*"
         }
      ]
   }
   ```

------
**Note**  
`AWSCloudFormationFullAccess` includes additional permissions for ChangeSets.

1. Create this policy: `ServicecodeCatalogSSMActionsBaseline`. Follow the instructions in [Creating IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create.html), and add this code in the JSON editor: 

------
#### [ JSON ]

****  

   ```
   {
      "Version":"2012-10-17",		 	 	 
      "Statement":[
         {
            "Sid":"Stmt1536341175150",
            "Action":[
               "servicecatalog:AssociateResource",
               "servicecatalog:DisassociateResource",
               "servicecatalog:ListServiceActionsForProvisioningArtifact",
               "servicecatalog:ExecuteprovisionedProductServiceAction",
               "ssm:DescribeDocument",
               "ssm:GetAutomationExecution",
               "ssm:StartAutomationExecution",
               "ssm:StopAutomationExecution",
               "ssm:StartChangeRequestExecution",
               "cloudformation:ListStackResources",
               "ec2:DescribeInstanceStatus",
               "ec2:StartInstances",
               "ec2:StopInstances"
            ],
            "Effect":"Allow",
            "Resource":"*"
         },
         {
            "Effect":"Allow",
            "Action":"iam:PassRole",
            "Resource":"*",
            "Condition":{
               "StringEquals":{
                  "iam:PassedToService":"ssm.amazonaws.com"
               }
            }
         }
      ]
   }
   ```

------

1. Create the `SCConnectLaunch` role. Then assign the trust relationship to Service Catalog.

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

1. Attach the relevant policies to the `SCConnectLaunch` role. 

   We recommend you customize and scope your launch policies to the specific AWS Services, which are in the associated CloudFormation template for the given Service Catalog product. 

   For example, to provision EC2 and S3 products, your role policies are as follows:
   + `AmazonEC2FullAccess` AWS managed policy)
   + `AmazonS3FullAccess` AWS managed policy)
   + `AWSCloudFormationFullAccess` (custom managed policy)
   + `ServiceCatalogSSMActionsBaseline` (custom managed policy)