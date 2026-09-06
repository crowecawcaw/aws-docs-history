

# Onboarding an AWS Seller account
<a name="onboard-seller-account"></a>

The following steps explain how to onboard AWS Seller accounts to the CRM connector.

1. In Salesforce, on the [Guided setup tab](use-guided-setup.md), expand **Step 1: Set up access to AWS Marketplace Management Portal (AMMP)** and choose **Start.** 

1. On the **Named credentials** page, choose **New earlier**. 

1. In the **New named credential** form, enter the values from the following table. 
**Note**  
For {{unique\_account\_prefix}}, use a descriptor for the AWS account, such as SellerA; SellerB. For example, **AWS\_SELLER\_CATALOG\_sellerA**. Always use the same prefix for the named credentials related to the AWS seller account.    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/partner-central/latest/crm/onboard-seller-account.html)

1. Choose **Save**.

1. Return to the **AWSGuided setup** page. In the **Authentication details** section, choose **Review** and confirm the credentials.

Repeat the above steps for each type of the listed **Named Credentials** in the following table. Use the values in the table below to replace the corresponding values in **Step 3** above 


|  **Named Credential Label**  |  **Named Credential Name**  |  **API endpoint**  |  **AWS Region**  |  **AWS service**  | 
| --- | --- | --- | --- | --- | 
| AWS SELLER Amazon S3 | AWS\_SELLER\_S3\_{{unique\_account\_prefix }} |  [https://s3.amazonaws.com/](https://s3.amazonaws.com/)  | us-east-1  | s3  | 
| AWS SELLER AWS STS | AWS\_SELLER\_STS\_{{unique\_account\_prefix}} |  [https://sts.us-east-1.amazonaws.com/](https://sts.us-east-1.amazonaws.com/)  | us-east-1  | sts  | 
| AWS SELLER Amazon SQS  | AWS\_SELLER\_SQS\_{{unique\_account\_prefix}} |  [https://sqs.us-east-1.amazonaws.com/](https://sqs.us-east-1.amazonaws.com/)  | us-east-1  | sqs  | 
| AWS SELLER AGREEMENT  | AWS\_SELLER\_AGREEMENT\_{{unique\_account\_prefix}} |  [https://agreement-marketplace.us-east-1.amazonaws.com/](https://agreement-marketplace.us-east-1.amazonaws.com/)  | us-east-1  | aws-marketplace  | 

Repeat the above steps for each AWS Seller account you want added to the AWS Marketplace integration.

After onboarding the named credentials, go to the **AWS Accounts** tab in the **AWS Partner CRM connector app** and complete the steps in the next sections.