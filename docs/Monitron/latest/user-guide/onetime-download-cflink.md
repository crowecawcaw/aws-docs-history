

Amazon Monitron is no longer open to new customers. Existing customers can continue to use the service as normal. For capabilities similar to Amazon Monitron, see our [blog post](https://aws.amazon.com/blogs/machine-learning/maintain-access-and-consider-alternatives-for-amazon-monitron).

# Exporting your data with CloudFormation (recommended option)
<a name="onetime-download-cflink"></a>

**Topics**
+ [Step 1: Create your Amazon S3 bucket, IAM role, and IAM policies.](#gdpr-cloudfront-makestack)
+ [Step 2: Note your resources](#gdpr-cloudfront-resources)
+ [Step 3: Create the support case](#gdpr-cloudfront-case)

## Step 1: Create your Amazon S3 bucket, IAM role, and IAM policies.
<a name="gdpr-cloudfront-makestack"></a>

1. Sign in to your AWS account.

1. Open a new browser tab with the following URL.

   ```
   https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/review?templateURL=https://s3.us-east-1.amazonaws.com/monitron-cloudformation-templates-us-east-1/monitron_manual_download.yaml&stackName=monitronexport
   ```

1. On the CloudFormation page that opens, in the upper right corner, select the region in which you are using Amazon Monitron.

1. Choose **Create stack**.  
![Capabilities section with acknowledgment checkbox for IAM resource creation.](http://docs.aws.amazon.com/Monitron/latest/user-guide/images/s3-export-1.png)

1. On the next page, choose the refresh icon as often as you like until the status of the stack (monitronexport) is CREATE\_COMPLETE.  
![Events tab showing monitronexport stack with CREATE_IN_PROGRESS status and refresh icon highlighted.](http://docs.aws.amazon.com/Monitron/latest/user-guide/images/s3-export-2.png)

## Step 2: Note your resources
<a name="gdpr-cloudfront-resources"></a>

1. Choose the **Outputs** tab.

1. Note the value of the key `MonRoleArn`.

1. Note the value of the key `S3BucketArn`.

1. Note your account ID from the upper right corner of the page).

1. Note the region you chose in Step 1. It also now appears at the top of the page, to the left of your account ID.  
![Outputs tab showing MonRoleArn and S3BucketArn values with their descriptions.](http://docs.aws.amazon.com/Monitron/latest/user-guide/images/s3-export-3.png)

## Step 3: Create the support case
<a name="gdpr-cloudfront-case"></a>

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