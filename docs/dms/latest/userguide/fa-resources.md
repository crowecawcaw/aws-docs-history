

# Creating required AWS resources for AWS DMS Fleet Advisor
<a name="fa-resources"></a>

**Important**  
End of support notice: On May 20, 2026, AWS will end support for AWS Database Migration Service Fleet Advisor. After May 20, 2026, you will no longer be able to access the AWS DMS Fleet Advisor console or AWS DMS Fleet Advisor resources. For more information, see [AWS DMS Fleet Advisor end of support](https://docs.aws.amazon.com/dms/latest/userguide/dms_fleet.advisor-end-of-support.html).

DMS Fleet Advisor needs a set of AWS resources in your account to forward and import inventory information, and to update the status of the DMS data collector.

Before you collect data and create inventories of databases and schemas for the first time, complete the following prerequisites.

To configure your Amazon S3 bucket and IAM resources, do one of the following: 
+ [Configure Amazon S3 and IAM resources using CloudFormation](#fa-resources-cf) (recommended).
+ [Configure Amazon S3 and IAM resources in the AWS Management Console](#fa-resources-manual)

## Configure Amazon S3 and IAM resources using CloudFormation
<a name="fa-resources-cf"></a>

A CloudFormation stack is a collection of AWS resources that you can manage as a single unit. To simplify creating required resources for DMS Fleet Advisor, you can use the CloudFormation template files to create CloudFormation stacks. For more information, see [Creating a stack on the CloudFormation console](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-console-create-stack.html) in *CloudFormation User Guide*.

**Note**  
This section only applies to using the standalone DMS Fleet Advisor collector. For information about using a single on-premises collector for gathering information about both databases and servers, see [ Application Discovery Service Agentless Collector ](https://docs.aws.amazon.com/application-discovery/latest/userguide/agentless-collector.html) in the [*AWS Application Discovery Service User Guide*](https://docs.aws.amazon.com/). 

### Amazon S3 and IAM resources created by CloudFormation
<a name="fa-resources-cf.resources"></a>

When you use the CloudFormation templates, they create stacks that include the following resources in your AWS account:
+ An Amazon S3 bucket named `dms-fleetadvisor-data-{{accountId}}-{{region}}`
+ An IAM user named `FleetAdvisorCollectorUser-{{region}}`
+ An IAM service role named `FleetAdvisorS3Role-{{region}}`
+ An access policy named `FleetAdvisorS3Role-{{region}}-Policy`
+ An access policy named `FleetAdvisorCollectorUser-{{region}}-Policy`
+ An IAM Service Linked Role (SLR) named `AWSServiceRoleForDMSFleetAdvisor`

Follow the steps listed below to configure your resources with CloudFormation.
+ [Step 1: Download the CloudFormation template files](#fa-resources-cf.dl-templates)
+ [Step 2: Configure Amazon S3 and IAM using CloudFormation](#fa-resources-cf.config)

### Step 1: Download the CloudFormation template files
<a name="fa-resources-cf.dl-templates"></a>

A CloudFormation template is a declaration of the AWS resources that make up a stack. The template is stored as a JSON file.

**To download the CloudFormation template files**

1. Open the context (right-click) menu for one of the following links and choose **Save Link As**:
   + If you plan to use DMS Fleet Advisor, choose [dms-fleetadvisor-iam-slr-s3.zip](samples/dms-fleetadvisor-iam-slr-s3.zip). If you have already created the SLR for DMS Fleet Advisor, choose [dms-fleetadvisor-iam-s3.zip](samples/dms-fleetadvisor-iam-s3.zip)
   + If you plan to use the AWS Application Discovery Service (ADS) Agentless Collector and have not created the SLR for it, then choose [ dms-fleetadvisor-ads-iam-slr-s3.zip](samples/dms-fleetadvisor-ads-iam-slr-s3.zip). If you have created the SLR for DMS Fleet Advisor with ADS before, choose [ dms-fleetadvisor-ads-iam-s3.zip](samples/dms-fleetadvisor-ads-iam-s3.zip).

1. Save the file to your computer.

### Step 2: Configure Amazon S3 and IAM using CloudFormation
<a name="fa-resources-cf.config"></a>

When you use the CloudFormation template for IAM, it creates the Amazon S3 and IAM resources listed previously.

**To configure Amazon S3 and IAM using CloudFormation**

1. Open the CloudFormation console at [https://console.aws.amazon.com/cloudformation](https://console.aws.amazon.com/cloudformation/).

1. Start the Create Stack wizard by choosing **Create Stack** and **With new resources** in the dropdown list.

1. On the **Create stack** page, do the following:

   1. For **Prepare template**, choose **Template is ready**.

   1. For **Template source**, choose **Upload a template file**.

   1. For **Choose file**, navigate to, then choose **dms-fleetadvisor-iam-slr-S3.json**, **dms-fleetadvisor-iam-S3.json.**, **dms-fleetadvisor-ads-iam-slr-s3.zip**, or **dms-fleetadvisor-ads-iam-s3.zip**.

   1. Choose **Next**.

1. On the **Specify stack details** page, do the following:

   1. For **Stack name**, enter **dms-fleetadvisor-iam-slr-s3**,**dms-fleetadvisor-iam-s3**, **dms-fleetadvisor-ads-iam-slr-s3**, or **dms-fleetadvisor-ads-iam-s3**.

   1. Choose **Next**.

1. On the **Configure stack options page**, choose **Next**.

1. On the **Review dms-fleetadvisor-iam-slr-s3**,**Review dms-fleetadvisor-iam-s3**, **Review dms-fleetadvisor-ads-iam-slr-s3**, or **Review dms-fleetadvisor-ads-iam-s3** page, do the following:

   1. Select the ****I acknowledge that CloudFormation might create IAM resources with custom names**** check box.

   1. Choose **Submit**.

   CloudFormation creates the S3 bucket and IAM roles and user that DMS Fleet Advisor requires. In the left panel, when **dms-fleetadvisor-iam-slr-s3**, **dms-fleetadvisor-iam-s3**, **dms-fleetadvisor-ads-iam-slr-s3**, or **dms-fleetadvisor-ads-iam-s3** shows **CREATE\_COMPLETE**, proceed to the next step.

1. In the left panel, choose **dms-fleetadvisor-iam-slr-s3**, **dms-fleetadvisor-iam-s3**, **dms-fleetadvisor-ads-iam-slr-s3**, or **dms-fleetadvisor-ads-iam-s3**. In the right panel, do the following:

   1. Choose **Stack info**. Your stack has an ID in the format **arn:aws:cloudformation:{{region}}:{{account-no}}:stack/dms-fleetadvisor-iam-slr-s3/{{identifier}}**, **arn:aws:cloudformation:{{region}}:{{account-no}}:stack/dms-fleetadvisor-iam-s3/{{identifier}}**, **arn:aws:cloudformation:{{region}}:{{account-no}}:stack/dms-fleetadvisor-ads-iam-slr-s3/{{identifier}}**, or **arn:aws:cloudformation:{{region}}:{{account-no}}:stack/dms-fleetadvisor-ads-iam-s3/{{identifier}}**.

   1. Choose **Resources**. You should see the following:
      + An Amazon S3 bucket named `dms-fleetadvisor-data-{{accountId}}-{{region}}`
      + A service role named `FleetAdvisorS3Role-{{region}}`
      + An IAM user named `FleetAdvisorCollectorUser-{{region}}`
      + An IAM SLR named `AWSServiceRoleForDMSFleetAdvisor` (if you downloaded `dms-fleet-advisor-iam-slr-s3.zip` or `dms-fleet-advisor-ads-iam-slr-s3.zip`).
      + An access policy named `FleetAdvisorS3Role-{{region}}-Policy`
      + An access policy named `FleetAdvisorCollectorUser-{{region}}-Policy`

## Configure Amazon S3 and IAM resources in the AWS Management Console
<a name="fa-resources-manual"></a>

### Create an Amazon S3 bucket
<a name="fa-resources-s3"></a>

Create an Amazon S3 bucket where inventory metadata can be stored. We recommend that you preconfigure this S3 bucket before using DMS Fleet Advisor. AWS DMS stores your DMS Fleet Advisor inventory metadata in this S3 bucket.

For more information about creating an S3 bucket, see [Create your first S3 bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/creating-bucket.html) in the *Amazon S3 User Guide*.

**Note**  
DMS Fleet Advisor only supports SSE-S3 encrypted buckets.

**To create an Amazon S3 bucket to store local data environment information**

1. Sign in to the AWS Management Console and open the Amazon S3 console at [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/).

1. Choose **Create bucket**. 

1. On the **Create bucket** page, enter a globally unique name that includes your sign-in name for the bucket, such as **fa-bucket-{{yoursignin}}**. 

1. Choose the AWS Region where you use the DMS Fleet Advisor.

1. Keep the remaining settings and choose **Create bucket**.

### Create IAM resources
<a name="fa-resources-iam"></a>

In this section, you create IAM resources for your data collector, IAM user, and DMS Fleet Advisor.

**Topics**
+ [Create IAM resources for your data collector](#fa-resources-iam-collector)
+ [Create the DMS Fleet Advisor service-linked role](#fa-resources-iam-slr)

#### Create IAM resources for your data collector
<a name="fa-resources-iam-collector"></a>

To make sure that your data collector works correctly and uploads the collected metadata to your Amazon S3 bucket, create the following policies. Then, create an IAM user with the following minimum permissions. For more information about DMS data collector, see [Discovering databases for migration using data collectors in AWS DMS](fa-data-collectors.md).

**To create an IAM policy for DMS Fleet Advisor and your data collector to access Amazon S3**

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/).

1. In the navigation pane, choose **Policies**.

1. Choose **Create policy**.

1. In the **Create policy** page, choose the **JSON** tab.

1. Paste the following JSON into the editor, replacing the example code. Replace `{{fa_bucket}}` with the name of the Amazon S3 bucket that you created in the previous section.

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
               "s3:GetObject*",
               "s3:GetBucket*",
               "s3:List*",
               "s3:DeleteObject*",
               "s3:PutObject*"
           ],
           "Resource": [
               "arn:aws:s3:::{{fa_bucket}}",
               "arn:aws:s3:::{{fa_bucket}}/*"
           ]
       }
       ]
       }
   ```

------

1. Choose **Next: Tags** and **Next: Review.**

1. Enter **FleetAdvisorS3Policy** for **Name\***, and then choose **Create policy**.

**To create an IAM policy for DMS data collector to access DMS Fleet Advisor**

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/).

1. In the navigation pane, choose **Policies**.

1. Choose **Create policy**.

1. In the **Create policy** page, choose the **JSON** tab.

1. Paste the following JSON code into the editor, replacing the example code. 

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
               "dms:DescribeFleetAdvisorCollectors",
               "dms:ModifyFleetAdvisorCollectorStatuses",
               "dms:UploadFileMetadataList"
           ],
           "Resource": "*"
       }
       ]
       }
   ```

------

1. Choose **Next: Tags** and **Next: Review.**

1. Enter **DMSCollectorPolicy** for **Name\***, then choose **Create policy**.

**To create an IAM user with minimum permissions to use DMS data collector**

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/).

1. In the navigation pane, choose **Users**.

1. Choose **Add users**.

1. On the **Add user** page, enter **FleetAdvisorCollectorUser** for **User name\***. Choose **Access key- Programmatic Access** for **Select AWS Access Type**. Choose **Next: Permissions**.

1. In the **Set permissions** section, choose **Attach existing policies directly**.

1. Use the search control to find and choose the **DMSCollectorPolicy** and **FleetAdvisorS3Policy** policies that you created before. Choose **Next: Tags**.

1. On the **Tags** page, choose **Next: Review**.

1. On the **Review** page, choose **Create user**. On the next page, choose **Download .csv** to save the new user credentials. Use these credentials with DMS Fleet Advisor for minimum required access permissions.

**To create an IAM role for DMS Fleet Advisor and your data collector to access Amazon S3**

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/).

1. In the navigation pane, choose **Roles**.

1. Choose **Create role**.

1. On the **Select trusted entity** page, for **Trusted entity type**, choose **AWS Service**. For **Use cases for other AWS services**, choose **DMS**. 

1. Select the **DMS** check box and choose **Next**. 

1. On the **Add permissions** page, choose **FleetAdvisorS3Policy**. Choose **Next**.

1. On the **Name, review, and create** page, enter **FleetAdvisorS3Role** for **Role name**, then choose **Create role**.

1. On the **Roles** page, enter **FleetAdvisorS3Role** for **Role name**. Choose **FleetAdvisorS3Role**.

1. On the **FleetAdvisorS3Role** page, choose the **Trust relationships** tab. Choose **Edit trust policy**.

1. On the **Edit trust policy** page, paste the following JSON into the editor, replacing the existing text.

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
       "Service": [
        "dms.amazonaws.com",
        "dms-fleet-advisor.amazonaws.com"
       ]
       },
       "Action": "sts:AssumeRole"
       }
       ]
       }
   ```

------

   The preceding policy grants the `sts:AssumeRole` permission to the services that AWS DMS uses to import collected data from the Amazon S3 bucket.

1. Choose **Update policy**.

#### Create the DMS Fleet Advisor service-linked role
<a name="fa-resources-iam-slr"></a>

DMS Fleet Advisor uses a service-linked role to manage Amazon CloudWatch metrics in your AWS account. DMS Fleet Advisor uses this service-linked role to publish the collected database performance metrics to CloudWatch on your behalf.

**To create the service-linked role for DMS Fleet Advisor**

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/).

1. In the navigation pane, choose **Roles**. Then, choose **Create role**.

1. For **Trusted entity type**, choose **AWS service**.

1. For **Use cases for other AWS services**, choose **DMS – Fleet Advisor**.

1. Select the **DMS – Fleet Advisor** check box and choose **Next**.

1. On the **Add permissions** page, choose **Next**.

1. On the **Name, review, and create** page, choose **Create role**.

Alternatively, you can create this service-linked role from the AWS API or AWS CLI. For more information, see [Creating a service-linked role for AWS DMS Fleet Advisor](slr-services-fa.md#create-slr-fa).

After you create the service-linked role for DMS Fleet Advisor, you can see performance metrics for your source databases in target recommendations. Also, you can see these metrics and in your CloudWatch account. For more information, see [Target recommendations](fa-recommendations.md).

**To create an IAM policy that is required for the DMS Fleet Advisor service-linked role**

The minimum required permissions to create the service-linked role are specified in the `DMSFleetAdvisorCreateServiceLinkedRolePolicy` policy. Create this IAM policy for your account if you are unable to create the service-linked role.

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/).

1. In the navigation pane, choose **Policies**.

1. Choose **Create policy**.

1. In the **Create policy** page, choose the **JSON** tab.

1. Paste the following JSON code into the editor, replacing the example code. 

------
#### [ JSON ]

****  

   ```
   {
       "Version":"2012-10-17",		 	 	 
       "Statement": [
       {
           "Effect": "Allow",
           "Action": "iam:CreateServiceLinkedRole",
           "Resource": "arn:aws:iam::*:role/aws-service-role/dms-fleet-advisor.amazonaws.com/AWSServiceRoleForDMSFleetAdvisor*",
           "Condition": {"StringLike": {"iam:AWSServiceName": "dms-fleet-advisor.amazonaws.com"}}
       },
       {
           "Effect": "Allow",
           "Action": [
               "iam:AttachRolePolicy",
               "iam:PutRolePolicy"
           ],
           "Resource": "arn:aws:iam::*:role/aws-service-role/dms-fleet-advisor.amazonaws.com/AWSServiceRoleForDMSFleetAdvisor*"
       }
       ]
       }
   ```

------

1. Choose **Next: Tags** and **Next: Review.**

1. Enter **DMSFleetAdvisorCreateServiceLinkedRolePolicy** for **Name\***, then choose **Create policy**.

Now, you can use this policy to create the service-linked role for DMS Fleet Advisor.