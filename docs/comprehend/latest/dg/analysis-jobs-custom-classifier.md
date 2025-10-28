# Analysis jobs for custom classification (console)

After you create and train a custom document classifier,
you can use the console to run custom classification jobs with the model.

###### To create a custom classification job (console)

1. Sign in to the AWS Management Console and open the Amazon Comprehend console at [https://console.aws.amazon.com/comprehend/](https://console.aws.amazon.com/comprehend/ "https://console.aws.amazon.com/comprehend/")
2. From the left menu, choose **Analysis jobs** and then choose **Create
   job**.
3. Give the classification job a name. The name must be unique to your account and current Region.
4. Under **Analysis type**, choose **Custom
   classification**.
5. From **Select classifier**, choose the custom classifier to use.
6. (Optional) If you choose to encrypt the data that Amazon Comprehend uses while processing your job, choose
   **Job encryption**. Then choose whether to use a KMS key associated with the current
   account, or one from another account.
   - If you are using a key associated with the current account, choose the key ID for
     **KMS key ID**.
   - If you are using a key associated with a different account, enter the ARN for the key ID under
     **KMS key ARN**.

###### Note

For more information on creating and using KMS keys and the associated encryption, see [Key management service (KMS)](../../../kms/latest/developerguide/overview.md "../../../kms/latest/developerguide/overview.md"). 7. Under **Input data**, enter the location of the Amazon S3 bucket that contains your input
documents or navigate to it by choosing **Browse S3**. This bucket must be in the same Region
as the API that you are calling. The IAM role that you're using for access permissions for the classification
job must have reading permissions for the S3 bucket.

To achieve the highest level of accuracy in training a model, match the type of input to the classifier model type.
The classifier job returns a warning
if you submit native documents to a plain-text model, or plain text documents to a native document model.
For more information, see [Training classification models](training-classifier-model.md "training-classifier-model.md"). 8. (Optional) For **Input format**, you can choose the format of the input documents.
The format can be one document per file, or one document per line in a single file. One document per line
applies only to text documents. 9. (Optional) For **Document read mode**, you can override the default text extraction actions.
For more information, see [Setting text extraction options](idp-set-textract-options.md "idp-set-textract-options.md"). 10. Under **Output data**, enter the location of the Amazon S3 bucket where Amazon Comprehend should write the
job's output data or navigate to it by choosing **Browse S3**. This bucket must be in the same
Region as the API that you are calling. The IAM role that you're using for access permissions for the
classification job must have write permissions for the S3 bucket. 11. (Optional) If you choose to encrypt the output result from your job, choose
**Encryption**. Then choose whether to use a KMS key associated with the current account,
or one from another account.

    * If you are using a key associated with the current account, choose the key alias or ID for
     **KMS key ID**.
    * If you are using a key associated with a different account, enter the ARN for the key alias or
     ID under **KMS key ID**.

12. (Optional) To launch your resources into Amazon Comprehend from a VPC, enter the VPC ID under **VPC** or
    choose the ID from the drop-down list.
    1.  Choose the subnet under **Subnet(s)**. After you select the first subnet, you
        can choose additional ones.
    2.  Under **Security Group(s)**, choose the security group to use if you
        specified one. After you select the first security group, you can choose additional
        ones.

###### Note

When you use a VPC with your classification job, the `DataAccessRole` used for the Create and Start
operations must grant permissions to the VPC that accesses the output bucket. 13. Choose **Create job** to create the document classification job.
