# Setting up cross-account

access

To set up cross-account access for EMR Serverless, complete the following steps.
In the example, `AccountA` is the account where you created your
Amazon EMR Serverless application, and `AccountB` is the account where your
Amazon DynamoDB is located.

1. Create a DynamoDB table in `AccountB`. For more information, refer to
   [Step 1: Create a table](../../../amazondynamodb/latest/developerguide/getting-started-step-1.md "../../../amazondynamodb/latest/developerguide/getting-started-step-1.md").
2. Create a `Cross-Account-Role-B` IAM role in
   `AccountB` that can access the DynamoDB table.
   1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
   2. Choose **Roles**, and create a new role called
      `Cross-Account-Role-B`. For more information on how
      to create IAM roles, refer to [Creating IAM
      roles](../../../IAM/latest/UserGuide/id_roles_create.md "../../../IAM/latest/UserGuide/id_roles_create.md") in the _a user Guide_.
   3. Create an IAM policy that grants permissions to access the
      cross-account DynamoDB table. Then attach the IAM policy to
      `Cross-Account-Role-B`.

   The following is a policy that grants access to a DynamoDB table
   `CrossAccountTable`. 4. Edit the trust relationship for the
   `Cross-Account-Role-B` role.

   To configure the trust relationship for the role, choose the
   **Trust Relationships** tab in the IAM
   console for the role that you created in _Step 2:
   Cross-Account-Role-B_.

   Select **Edit Trust Relationship** and then add
   the following policy document. This document allows
   `Job-Execution-Role-A` in `AccountA` to
   assume this `Cross-Account-Role-B` role.

   JSON

   ```
   `{
    "Version":"2012-10-17",
    "Statement": [
    {
    "Effect": "Allow",
    "Action": [
    "sts:AssumeRole"
    ],
    "Resource": "arn:aws:iam::123456789012:role/Job-Execution-Role-A",
    "Sid": "AllowSTSAssumerole"
    }
    ]
   }`

   ```

   5. Grant `Job-Execution-Role-A` in `AccountA`
      with `- STS Assume role` permissions to assume
      `Cross-Account-Role-B`.

   In the IAM console for AWS account `AccountA`,
   select `Job-Execution-Role-A`. Add the following policy
   statement to the `Job-Execution-Role-A` to allow the
   `AssumeRole` action on the
   `Cross-Account-Role-B` role.

   JSON

   ```
   `{
    "Version":"2012-10-17",
    "Statement": [
    {
    "Effect": "Allow",
    "Action": [
    "sts:AssumeRole"
    ],
    "Resource": [
    "arn:aws:iam::123456789012:role/Cross-Account-Role-B"
    ],
    "Sid": "AllowSTSAssumerole"
    }
    ]
   }`

   ```

   6. Set the `dynamodb.customAWSCredentialsProvider`
      property with value as
      `com.amazonaws.emr.AssumeRoleAWSCredentialsProvider`
      in core-site classification. Set the environment variable
      `ASSUME_ROLE_CREDENTIALS_ROLE_ARN` with the ARN value
      of `Cross-Account-Role-B`.

3. Run Spark or Hive job using `Job-Execution-Role-A`.
