# Step 7: Create an IAM role for SageMaker AI

notebooks

If you plan to use SageMaker AI notebooks with development endpoints, you need to grant the IAM
role permissions. You provide those permissions by using AWS Identity and Access Management (IAM), through an
IAM role.

###### To create an IAM role for SageMaker AI notebooks

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the left navigation pane, choose **Roles**.
3. Choose **Create role**.
4. For role type, choose **AWS Service**, find and choose
   **SageMaker**, and then choose the **SageMaker -
   Execution** use case. Then choose **Next:
   Permissions**.
5. On the **Attach permissions policy** page, choose the
   policies that contain the required permissions; for example,
   **AmazonSageMakerFullAccess**.

Choose **Next: Review**.

If you plan to access Amazon S3 sources and targets that are encrypted with SSE-KMS, attach a
policy that allows notebooks to decrypt the data, as shown in the following
example. For more information, see [Protecting Data Using Server-Side
Encryption with AWS KMS-Managed Keys (SSE-KMS)](../../../AmazonS3/latest/userguide/UsingKMSEncryption.md "../../../AmazonS3/latest/userguide/UsingKMSEncryption.md").

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "kms:Decrypt"
 ],
 "Resource": [
 "arn:aws:kms:*:`111122223333`:key/`key-id`"
 ]
 }
 ]
}`

```

6. For **Role name**, enter a name for your role. To allow the
   role to be passed from console users to SageMaker AI, use a name that is prefixed with
   the string `AWSGlueServiceSageMakerNotebookRole`. AWS Glue
   provided policies expect IAM roles to begin with
   `AWSGlueServiceSageMakerNotebookRole`. Otherwise you must
   add a policy to your users to allow the `iam:PassRole` permission for
   IAM roles to match your naming convention.

For example, enter
`AWSGlueServiceSageMakerNotebookRole-Default`, and then
choose **Create role**. 7. After you create the role, attach the policy that allows additional
permissions required to create SageMaker AI notebooks from AWS Glue.

Open the role that you just created,
`AWSGlueServiceSageMakerNotebookRole-Default`, and choose
**Attach policies**. Attach the policy that you created
named `AWSGlueSageMakerNotebook` to the role.
