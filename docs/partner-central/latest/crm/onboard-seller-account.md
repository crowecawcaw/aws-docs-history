# Onboarding an AWS Seller account

The following steps explain how to onboard AWS Seller accounts to the CRM
connector.

1. In Salesforce, on the [Guided setup tab](use-guided-setup.md "use-guided-setup.md"), expand **Step 1: Set up access to AWS Marketplace Management Portal (AMMP)**
   and choose **Start.**
2. On the **Named credentials** page, choose **New
   earlier**.
3. In the **New named credential** form, enter the values from the
   following table.

###### Note

For `unique_account_prefix`, use a descriptor for the AWS
account, such as SellerA; SellerB. For example, `AWS_SELLER_CATALOG_sellerA`. Always use
the same prefix for the named credentials related to the AWS seller account.

| **Field**                             | **Value**                                           |
| ------------------------------------- | --------------------------------------------------- |
| **Label**                             | AWS SELLER CATALOG                                  |
| **Name**                              | AWS_SELLER_CATALOG\_`unique_account_prefix`         |
| **URL**                               | https://catalog.marketplace.us-east-1.amazonaws.com |
| **Identity type**                     | Named Principal                                     |
| **Authentication protocol**           | AWS signature version 4                             |
| **AWS access key ID**                 | The ID of the IAM user's access key                 |
| **AWS secret access key**             | The IAM user's secret access key                    |
| **AWS Region**                        | us-east-1                                           |
| **AWS service**                       | aws-marketplace                                     |
| **Generate authorization header**     | checked                                             |
| **Allow merge fields in HTTP header** | checked                                             |
| **Allow merge fields in HTTP body**   | unchecked                                           |

4. Choose **Save**.
5. Return to the **AWSGuided setup** page. In the
   **Authentication details** section, choose **Review**
   and confirm the credentials.
   Repeat the above steps for each type of the listed **Named Credentials**
   in the following table. Use the values in the table below to replace the corresponding values
   in **Step 3** above

| **Named Credential Label** | **Named Credential Name**                     | **API endpoint**                                                                                                                                                          | **AWS Region** | **AWS service** |
| -------------------------- | --------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------- | --------------- |
| AWS SELLER Amazon S3       | AWS_SELLER_S3\_`unique_account_prefix`        | [https://s3.amazonaws.com/](https://s3.amazonaws.com/ "https://s3.amazonaws.com/")                                                                                        | us-east-1      | s3              |
| AWS SELLER AWS STS         | AWS_SELLER_STS\_`unique_account_prefix`       | [https://sts.us-east-1.amazonaws.com/](https://sts.us-east-1.amazonaws.com/ "https://sts.us-east-1.amazonaws.com/")                                                       | us-east-1      | sts             |
| AWS SELLER Amazon SQS      | AWS_SELLER_SQS\_`unique_account_prefix`       | [https://sqs.us-east-1.amazonaws.com/](https://sqs.us-east-1.amazonaws.com/ "https://sqs.us-east-1.amazonaws.com/")                                                       | us-east-1      | sqs             |
| AWS SELLER AGREEMENT       | AWS_SELLER_AGREEMENT\_`unique_account_prefix` | [https://agreement-marketplace.us-east-1.amazonaws.com/](https://agreement-marketplace.us-east-1.amazonaws.com/ "https://agreement-marketplace.us-east-1.amazonaws.com/") | us-east-1      | aws-marketplace |

Repeat the above steps for each AWS Seller account you want added to the AWS Marketplace
integration.

After onboarding the named credentials, go to the **AWS Accounts** tab
in the **AWS Partner CRM connector app** and complete the steps in the next sections.
