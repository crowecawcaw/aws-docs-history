# Entering custom settings

After you enter the system configuration settings, you enter settings for the Amazon S3 bucket used to upload and store custom EULAs.

1. In Salesforce, on the [Guided setup tab](use-guided-setup.md "use-guided-setup.md"), return to the **Custom Settings** page, locate **S3 Bucket
   Settings**, and choose **Manage**.
2. Choose **New**.
3. Enter values for the following settings.

| **Setting name**            | **Default value** | **Description**                                                                                                                                  |
| --------------------------- | ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------- |
| **Name**                    | N/A               | **Provide unique account prefix** The name of the Amazon S3 setting. This name should be same as the AWS account name in the AWS accounts table. |
| **Amazon S3 Bucket Name**   | N/A               | The name of the Amazon S3 bucket that stores the custom EULA.                                                                                    |
| **Amazon S3 Bucket Prefix** | N/A               | Prefix of the Amazon S3 bucket that stores the custom EULA.                                                                                      | 4. Choose **Save**. 5. For each configured AWS Seller account, repeat steps 2-4 to add the Amazon S3 settings. |
