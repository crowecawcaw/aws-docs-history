

# Step 6: Add a launch constraint to assign an IAM role
<a name="getstarted-launchconstraint"></a>

 A launch constraint designates an IAM role that AWS Service Catalog assumes when an end user launches a product. 

 For this step, you add a launch constraint to the Linux Desktop product, so AWS Service Catalog can use the IAM resources that make up the product's AWS CloudFormation template. 

 The IAM role that you assign to a product as a launch constraint must have the following permissions 

1. AWS CloudFormation

1. Services in the AWS CloudFormation template for the product

1. Read access to the AWS CloudFormation template in a service-owned Amazon S3 bucket. 

This launch constraint enables the end user to launch the product and, after launch, manage it as a provisioned product. For more information, see [AWS Service Catalog Launch Constraints](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/constraints-launch.html).

Without a launch constraint, you need to grant additional IAM permissions to your end users before they can use the Linux Desktop product. For example, the `ServiceCatalogEndUserAccess` policy grants the minimum IAM permissions required to access the AWS Service Catalog end user console view. 

Using a launch constraint allows you follow the IAM best practice of keeping end user IAM permissions to a minimum. For more information, see [Grant least privilege](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#grant-least-privilege) in the *IAM User Guide*.

**To add a launch constraint**

1. Follow the instructions to [ Create new policies on the JSON tab](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create-console.html) in the *IAM User guide*. 

1. Paste the following JSON policy document:
   +  `cloudformation`– Allows AWS Service Catalog full permissions to create, read, update, delete, list, and tag CloudFormation stacks. 
   +  `ec2`— Allows AWS Service Catalog full permissions to list, read, write, provision, and tag Amazon Elastic Compute Cloud (Amazon EC2) resources that are part of the AWS Service Catalog product. Depending on the AWS resource that you want to deploy, this permission might change. 
   +  `ec2`– Creates a new managed policy for you AWS account and attaches the specified managed policy to the specified IAM role. 
   +  `s3`— Allows access to Amazon S3 buckets owned by AWS Service Catalog. To deploy the product, AWS Service Catalog requires access to provisioning artifacts. 
   +  `servicecatalog`— Allows AWS Service Catalog permissions to list, read, write, tag, and launch resources on behalf of the end-user. 
   +  `sns`— Allows AWS Service Catalog permissions to list, read, write, and tag Amazon SNS topics for the launch constraint. 
**Note**  
 Depending on the underlying resources that you want to deploy, you might need to modify the example JSON policy. 

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
                   "cloudformation:CreateStack",
                   "cloudformation:DeleteStack",
                   "cloudformation:DescribeStackEvents",
                   "cloudformation:DescribeStacks",
                   "cloudformation:GetTemplateSummary",
                   "cloudformation:SetStackPolicy",
                   "cloudformation:ValidateTemplate",
                   "cloudformation:UpdateStack",
                   "ec2:*",
                   "servicecatalog:*",
                   "sns:*"
               ],
               "Resource": "*"
           },
           {
            "Effect":"Allow",
            "Action":[
               "s3:GetObject"
            ],
            "Resource":"*",
            "Condition":{
               "StringEquals":{
                  "s3:ExistingObjectTag/servicecatalog:provisioning":"true"
               }
            }
         }
       ]
   }
   ```

------

1. Choose **Next**, **Tags**.

1. Choose **Next,** **Review**.

1. In the **Review policy** page, for the **Name**, enter **linuxDesktopPolicy**.

1. Choose **Create policy**.

1. In the navigation pane, choose **Roles**. Then choose **Create role** and do the following:

   1. For **Select trusted entity**, choose **AWS service** and then under **Use case for other AWS services **choose **Service Catalog**. Select the Service Catalog use case and then choose **Next**.

   1. Search for the **linuxDesktopPolicy** policy and then select the checkbox.

   1. Choose **Next**. 

   1. For **Role name**, type **linuxDesktopLaunchRole**.

   1. Choose **Create role**.

1. Open the AWS Service Catalog console at [https://console.aws.amazon.com/servicecatalog](https://console.aws.amazon.com/servicecatalog.).

1. Choose the **Engineering Tools** portfolio.

1. On the **Portfolio details** page, choose the **Constraints** tab, and then choose **Create constraint**.

1. For **Product**, choose **Linux Desktop**, and for **Constraint type**, choose **Launch**.

1. Choose **Select IAM role**. Next choose **linuxDesktopLaunchRole**, and then choose **Create**. 