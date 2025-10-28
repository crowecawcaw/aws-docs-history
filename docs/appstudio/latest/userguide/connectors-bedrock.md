# Connect to Amazon Bedrock

To connect App Studio with Amazon Bedrock so builders can access and use Amazon Bedrock in applications, you must perform
the following steps:

1. [Step 1: Enable Amazon Bedrock models](#connectors-bedrock-model-access "#connectors-bedrock-model-access")
2. [Step 2: Create an IAM policy and role with appropriate Amazon Bedrock permissions](#connectors-bedrock-iam "#connectors-bedrock-iam")
3. [Step 3: Create Amazon Bedrock connector](#connectors-bedrock-create-connector "#connectors-bedrock-create-connector")

## Step 1: Enable Amazon Bedrock models

Use the following procedure to enable Amazon Bedrock models.

###### To enable Amazon Bedrock models

1. Sign in to the AWS Management Console and open the Amazon Bedrock console at
   [https://console.aws.amazon.com/bedrock/](https://console.aws.amazon.com/bedrock/ "https://console.aws.amazon.com/bedrock/").
2. In the left navigation pane, choose **Model access**.
3. Enable the models that you want to use. For more information, see
   [Manage access to Amazon Bedrock foundation models](../../../bedrock/latest/userguide/model-access.md "../../../bedrock/latest/userguide/model-access.md").

## Step 2: Create an IAM policy and role with appropriate Amazon Bedrock permissions

To use Amazon Bedrock resources with App Studio, administrators must create an IAM policy and role to give App Studio
permissions to access the resources. The IAM policy controls what resources and what operations can
be called against those resources, such as `InvokeModel`. The IAM policy is then attached to an IAM role that is used by App Studio.

### Step 2a: Create an IAM policy with appropriate Amazon Bedrock permissions

The IAM policy that you create and use with App Studio should contain only the minimally necessary permissions on the appropriate resources
for the application to follow best security practices.

###### To create an IAM policy with appropriate Amazon Bedrock permissions

1. Sign in to the [IAM console](https://console.aws.amazon.com/iam "https://console.aws.amazon.com/iam") with a user that has permissions to create IAM policies. We recommend
   using the administrative user created in
   [Create an administrative user for managing AWS resources](setting-up-first-time-admin.md#setting-up-create-admin-user "setting-up-first-time-admin.md#setting-up-create-admin-user").
2. In the left-side navigation pane, choose **Policies**.
3. Choose **Create policy**.
4. In the **Policy editor** section, choose the **JSON** option.
5. Type or paste in a JSON policy document. The following example policy provides `InvokeModel` on all Amazon Bedrock resources,
   using the wildcard (`*`).

For best security practices, you should replace the wildcard with the Amazon Resource Name (ARN) of the resources you want to use with App Studio.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "BedrockAccessForAppStudio",
 "Effect": "Allow",
 "Action": [
 "bedrock:InvokeModel"
 ],
 "Resource": "*"
 }
 ]
}`

```

6. Choose **Next**.
7. On the **Review and create** page, provide a **Policy name**, such as `BedrockAccessForAppStudio`,
   and **Description** (optional).
8. Choose **Create policy** to create the policy.

### Step 2b: Create an IAM role to give App Studio access to Amazon Bedrock

To use Amazon Bedrock with App Studio, administrators must create an IAM role to give App Studio
permissions to access the resources. The IAM role controls the scope of permissions for App Studio apps to use, and is
used when creating the connector. We recommend creating at least one IAM role per service and policy.

###### To create an IAM role to give App Studio access to Amazon Bedrock

1. Sign in to the [IAM console](https://console.aws.amazon.com/iam "https://console.aws.amazon.com/iam") with a user that has permissions to create IAM roles. We recommend
   using the administrative user created in
   [Create an administrative user for managing AWS resources](setting-up-first-time-admin.md#setting-up-create-admin-user "setting-up-first-time-admin.md#setting-up-create-admin-user").
2. In the navigation pane of the console, choose **Roles** and then choose **Create role**.
3. In **Trusted entity type**, choose **Custom trust policy**.
4. Replace the default policy with the following policy to allow App Studio applications to assume this role in your account.

You must replace the following placeholders in the policy. The values to be used can be found in App Studio, in the **Account settings** page.

    * Replace `111122223333` with the AWS account number of the account used to set up the App Studio instance, listed as
     **AWS account ID** in the account settings in your App Studio instance.
    * Replace `11111111-2222-3333-4444-555555555555` with your App Studio instance ID, listed as **Instance ID**
     in the account settings in your App Studio instance.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "AWS": "arn:aws:iam::`111122223333`:root"
 },
 "Action": "sts:AssumeRole",
 "Condition": {
 "StringEquals": {
 "aws:PrincipalTag/IsAppStudioAccessRole": "true",
 "sts:ExternalId": "`11111111-2222-3333-4444-555555555555`"
 }
 }
 }
 ]
}`

```

Choose **Next**. 5. In **Add permissions**, search for and select the policy that you created in the previous step (`BedrockAccessForAppStudio`).
Choosing the **+** next to a policy will expand the policy to show the
permissions granted by it and choosing the checkbox selects the policy.

Choose **Next**. 6. On the **Name, review, and create** page, provide a **Role name** and **Description**. 7. In **Step 3: Add tags**,
choose **Add new tag** to add the following tag to provide App Studio access:

    * **Key:** `IsAppStudioDataAccessRole`
    * **Value:** `true`

8. Choose **Create role** and make note of the generated Amazon Resource Name (ARN), you
   will need it when creating the Amazon Bedrock connector in App Studio in the next step.

## Step 3: Create Amazon Bedrock connector

Now that you have your Amazon Bedrock resources and IAM policy and role configured, use that information to create the connector in App Studio that builders
can use to connect their apps to Amazon Bedrock.

###### Note

You must have the Admin role in App Studio to create connectors.

###### To create a connector for Amazon Bedrock

1. Navigate to App Studio.
2. In the left-side navigation pane, choose **Connectors** in the **Manage** section.
   You will be taken to a page displaying a list of existing connectors with some details about each.
3. Choose **+ Create connector**.
4. Choose **Other AWS services** from the list of connector types.
5. Configure your connector by filling out the following fields:
   - **Name:** Enter a name for your Amazon Bedrock connector.
   - **Description:** Enter a description for your Amazon Bedrock connector.
   - **IAM role:** Enter the Amazon Resource Name (ARN) from
     the IAM role created in [Step 2b: Create an IAM role to give App Studio access to Amazon Bedrock](#connectors-bedrock-iam-role "#connectors-bedrock-iam-role").
     For more information about IAM, see the [IAM User Guide](../../../IAM/latest/UserGuide/introduction.md "../../../IAM/latest/UserGuide/introduction.md").
   - **Service:** Choose **Bedrock Runtime**.

   ###### Note

   **Bedrock Runtime** is used to make inference requests for models hosted in Amazon Bedrock, whereas **Bedrock** is used
   to manage, train, and deploy models.
   - **Region:** Choose the AWS Region where your Amazon Bedrock resources are located.

6. Choose **Create**.
7. The newly created connector will appear in the **Connectors** list.
