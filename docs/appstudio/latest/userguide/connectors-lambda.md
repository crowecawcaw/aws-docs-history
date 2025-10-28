# Connect to AWS Lambda

To connect App Studio with Lambda to enable builders to access and use Lambda resources in applications, you must perform
the following steps:

1. [Step 1: Create and configure Lambda functions](#connectors-lambda-create-resources "#connectors-lambda-create-resources")
2. [Step 2: Create an IAM role to give App Studio access to Lambda resources](#connectors-lambda-iam-role "#connectors-lambda-iam-role")
3. [Step 3: Create Lambda connector](#connectors-lambda-create-connector "#connectors-lambda-create-connector")

## Step 1: Create and configure Lambda functions

If you don't have existing Lambda functions, you must first create them. To learn more about
creating Lambda functions, see the [AWS Lambda Developer Guide](../../../lambda/latest/dg.md "../../../lambda/latest/dg.md").

## Step 2: Create an IAM role to give App Studio access to Lambda resources

To use Lambda resources with App Studio, administrators must create an IAM role to give App Studio
permissions to access the resources. The IAM role controls the resources or operations applications can access from Lambda.

We recommend creating at least one IAM role per service and policy.

###### To create an IAM role to give App Studio access to Lambda resources

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

Choose **Next**. 5. In **Add permissions**, search for and select the policies that grant the appropriate permissions for the role. Choosing the
**+** next to a policy will expand the policy to show the permissions granted by it and choosing the checkbox selects the policy. For Lambda, you may consider adding
the `AWSLambdaRole` policy, which grants permissions to invoke Lambda functions.

For more information about using IAM policies with Lambda, including a list of managed policies and their descriptions, see
[Identity and Access Management for AWS Lambda](../../../lambda/latest/dg/security-iam.md "../../../lambda/latest/dg/security-iam.md")
in the _AWS Lambda Developer Guide_.

Choose **Next**. 6. On the **Name, review, and create** page, provide a **Role name** and **Description**. 7. In **Step 3: Add tags**,
choose **Add new tag** to add the following tag to provide App Studio access:

    * **Key:** `IsAppStudioDataAccessRole`
    * **Value:** `true`

8. Choose **Create role** and make note of the generated Amazon Resource Name (ARN), you
   will need it when [creating
   the Lambda connector in App Studio](#connectors-lambda-create-connector "#connectors-lambda-create-connector").

## Step 3: Create Lambda connector

Now that you have your Lambda resources and IAM policy and role configured, use that information to create the connector in App Studio that builders
can use to connect their apps to Lambda.

###### Note

You must have the Admin role in App Studio to create connectors.

###### To create a connector for Lambda

1. Navigate to App Studio.
2. In the left-side navigation pane, choose **Connectors** in the **Manage** section.
   You will be taken to a page displaying a list of existing connectors with some details about each.
3. Choose **+ Create connector**.
4. Choose **Other AWS Services** from the list of connector types.
5. Configure your connector by filling out the following fields:
   - **Name:** Enter a name for your Lambda connector.
   - **Description:** Enter a description for your Lambda connector.
   - **IAM role:** Enter the Amazon Resource Name (ARN) from
     the IAM role created in [Step 2: Create an IAM role to give App Studio access to Lambda resources](#connectors-lambda-iam-role "#connectors-lambda-iam-role").
     For more information about IAM, see the [IAM User Guide](../../../IAM/latest/UserGuide/introduction.md "../../../IAM/latest/UserGuide/introduction.md").
   - **Service:** Choose **Lambda**.
   - **Region:** Choose the AWS Region where your Lambda resources are located.

6. Choose **Create**.
7. The newly created connector will appear in the **Connectors** list.
