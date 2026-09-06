

Amazon Monitron is no longer open to new customers. Existing customers can continue to use the service as normal. For capabilities similar to Amazon Monitron, see our [blog post](https://aws.amazon.com/blogs/machine-learning/maintain-access-and-consider-alternatives-for-amazon-monitron).

# Exporting your data with the console
<a name="onetime-download-console"></a>

**Topics**
+ [Step 1: Setting up your Amazon S3 bucket](#gdpr-console-s3)
+ [Step 2: Give Amazon Monitron permission to access Amazon S3](#gdpr-console-set-policy)
+ [Step 3: Create the role](#gdpr-console-create-role)
+ [Step 4: Create the trust policy](#gdpr-console-trust-policy)
+ [Step 5: Create the support case](#gdpr-console-case)

## Step 1: Setting up your Amazon S3 bucket
<a name="gdpr-console-s3"></a>

1. Open the [Amazon S3 console](https://console.aws.amazon.com/s3/).

1. Choose **Create bucket**.  
![](http://docs.aws.amazon.com/Monitron/latest/user-guide/images/gdpr-create-bucket.png)

1. Name your bucket and select an appropriate region. Then, at the bottom of the page, choose **Create bucket**.
**Important**  
At this time, Amazon Monitron is only supported in three regions:  
US East (N. Virginia) us-east-1
EU (Ireland) eu-west-1
 Asia Pacific (Sydney) ap-south-east-2
Therefore, your Amazon S3 bucket must be in one of those regions.

   It must also be the same region in which you are using the Amazon Monitron service.  
![](http://docs.aws.amazon.com/Monitron/latest/user-guide/images/gdpr-create-bucket-2.png)

1. Review the rest of the options on the page, and make the appropriate choices, depending on your security needs and policies.
**Important**  
You are responsible for taking the appropriate steps to secure your data. We strongly recommend using server-side encryption and blocking public access to your bucket.

1. Using the search box, find the bucket you just created, and then choose it.  
![](http://docs.aws.amazon.com/Monitron/latest/user-guide/images/gdpr-choose-s3-bucket.png)

1. From the **Properties** tab, make a note of the name, ARN, and region of the bucket.  
![](http://docs.aws.amazon.com/Monitron/latest/user-guide/images/gdpr-s3-properties-tab.png)

## Step 2: Give Amazon Monitron permission to access Amazon S3
<a name="gdpr-console-set-policy"></a>

1. Open the [ IAM console](https://console.aws.amazon.com/iam/) and choose **Policies**.  
![IAM Dashboard showing resource counts, recent updates, and tools for policy management.](http://docs.aws.amazon.com/Monitron/latest/user-guide/images/s3-export-9.png)

1. Choose **Create policy**.  
![IAM Policies page with options to search, filter, and create a new policy.](http://docs.aws.amazon.com/Monitron/latest/user-guide/images/s3-export-10.png)

1. Select the **JSON** tab.  
![Policy editor interface showing JSON structure for specifying permissions in IAM.](http://docs.aws.amazon.com/Monitron/latest/user-guide/images/s3-export-11.png)

1. Delete the default JSON text so that the form is empty.

1. Paste in the bucket access policy.

------
#### [ JSON ]

****  

   ```
   {
       "Version":"2012-10-17",		 	 	 
   
       "Statement": [
           {
               "Action": [
                   "s3:GetBucketAcl",
                   "s3:GetBucketLocation",
                   "s3:ListBucket"
               ],
               "Effect": "Allow",
               "Resource": [
                   "arn:aws:s3:::bucketname"
               ]
           },
           {
               "Action": [
                   "s3:PutObject",
                   "s3:GetBucketAcl"
               ],
               "Effect": "Allow",
               "Resource": [
                   "arn:aws:s3:::bucketname/*"
               ]
           }
       ]
   }
   ```

------  
![IAM policy editor interface showing JSON code for S3 bucket permissions.](http://docs.aws.amazon.com/Monitron/latest/user-guide/images/s3-export-12.png)

1. Select **Next**.

1. On the **Review and create** page, do the following:

   1. In **Policy details**, enter a **Policy name** and optional **Description**.

   1. Leave the **Permissions defined in this policy** section as is.

   1. In **Add tags — *optional*, you can choose to add tags to keep track of your resources.**.

   1. Choose **Create policy**.  
![Policy creation interface showing policy details, permissions, and tags sections.](http://docs.aws.amazon.com/Monitron/latest/user-guide/images/s3-export-13.png)

## Step 3: Create the role
<a name="gdpr-console-create-role"></a>

1. Open the [ IAM console](https://console.aws.amazon.com/iam/) and choose **Roles**.  
![IAM Dashboard showing resource counts, recent updates, and available tools.](http://docs.aws.amazon.com/Monitron/latest/user-guide/images/s3-export-14.png)

1. Choose **Create role**.  
![IAM roles interface showing 116 roles and a prominent "Create role" button.](http://docs.aws.amazon.com/Monitron/latest/user-guide/images/s3-export-15.png)

1. On the **Select trusted entity**, in **Trusted entity type**, choose **AWS account**.

1. In **An AWS account**, choose **This account**. You can customize additional setting using **Options**.

1. Choose **Next**.  
![AWS account selection interface with trusted entity types and account options.](http://docs.aws.amazon.com/Monitron/latest/user-guide/images/s3-export-16.png)

1. In **Add permissions**, for **Permissions policies**, search for the policy you just created in the search box, and select your policy.  
![Add permissions interface showing search for "monitron-policy" with one matching result selected.](http://docs.aws.amazon.com/Monitron/latest/user-guide/images/s3-export-17.png)

1. On the **Name, review, and create** page do the following:

   1. In **Role details** enter a **Role name** and optional **Description**.

   1. You can choose to ignore **Step 1: Select trusted entities** and **Step 2: Add permisions**.

   1. For **Step 3: Add tags**, for **Add tags — *optional***, add optional tags to keep track of your resources.

1. Choose **Create role**.  
![Form for creating a new role with fields for role name, description, trust policy, and permissions.](http://docs.aws.amazon.com/Monitron/latest/user-guide/images/s3-export-18.png)

## Step 4: Create the trust policy
<a name="gdpr-console-trust-policy"></a>

1. Search for the role you just created and choose the role.  
![IAM Roles page showing search results for "monitron-role" with one matching role listed.](http://docs.aws.amazon.com/Monitron/latest/user-guide/images/s3-export-19.png)

1. Select the **Trust relationships** tab.  
![IAM role details page showing Trust relationships tab and Edit trust policy button.](http://docs.aws.amazon.com/Monitron/latest/user-guide/images/s3-export-20.png)

1. Choose **Edit trust relationship**.  
![](http://docs.aws.amazon.com/Monitron/latest/user-guide/images/gdpr-edit-trust-relationship.png)

1. Erase the default JSON text so that the form is empty.

1. Paste in the policy that allows Amazon Monitron to assume the role.

------
#### [ JSON ]

****  

   ```
   {
   	"Version":"2012-10-17",		 	 	 
   	"Statement": [{
   		"Effect": "Allow",
   		"Principal": {
   			"Service": ["monitron.amazonaws.com"]
   		},
   		"Action": "sts:AssumeRole"
   	}]
   }
   ```

------  
![Form for creating a new role with fields for role name, description, trust policy, and permissions.](http://docs.aws.amazon.com/Monitron/latest/user-guide/images/s3-export-18.png)

1. Choose **Update Trust Policy**.

## Step 5: Create the support case
<a name="gdpr-console-case"></a>

1.  From your AWS console, choose the question mark icon near the upper right corner of any page, then choose **Support Center**.   
![](http://docs.aws.amazon.com/Monitron/latest/user-guide/images/gdpr-support-question-mark.png)

1.  On the next page, choose **Create case**.   
![Support Center interface with Quick solutions, Active cases, and Create case button.](http://docs.aws.amazon.com/Monitron/latest/user-guide/images/s3-export-4.png)

1. On the **How can we help?** page, do the following:

   1.  Choose **Account and billing support**. 

   1. Under **Service**, choose **Account**. 

   1. Under **Category**, choose **Compliance & Accreditations**. 

   1. Choose **Severity**, if that option is available to you based on your support subscription. 

   1. Choose **Next step: Additional information**.   
![Support case form with Account and billing selected, Service set to Account, Category set to Compliance and Accreditations, and Severity set to General question.](http://docs.aws.amazon.com/Monitron/latest/user-guide/images/s3-export-5.png)

1. In **Additional information** do the following:

   1. Under **Subject**, enter **Amazon Monitron data export request**. 

   1. In the **Description** field, enter:

      1. your account ID

      1. the region of the bucket you created

      1. the ARN of the bucket you created (for example: "arn:aws:s3:::bucketname")

      1. the ARN of the role you created (for example: "arn:aws:iam::273771705212:role/role-for-monitron")  
![Form for Amazon Monitron data export request with fields for account and bucket details.](http://docs.aws.amazon.com/Monitron/latest/user-guide/images/s3-export-6.png)

   1. Choose **Next step: Solve now or contact us**.

1. In **Solve now or contact us** do the following:

   1. In **Solve now**, select **Next**.   
![Support options interface with "Solve now" and "Contact us" buttons, and recommendations.](http://docs.aws.amazon.com/Monitron/latest/user-guide/images/s3-export-7.png)

   1. In **Contact us**, choose your **Preferred contact language** and preferred method of contact.

   1. Choose **Submit**. A confirmation screen with your case ID and details will be displayed.  
![Contact options with language selection and choices for Web, Phone, or Chat communication.](http://docs.aws.amazon.com/Monitron/latest/user-guide/images/s3-export-8.png)

 An AWS customer support specialist will get back to you as soon as possible. If there are any issues with the steps listed, the specialist may ask you for more information. If all the necessary information has been provided, the specialist will let you know as soon as your data has been copied to the Amazon S3 bucket that you created above. 