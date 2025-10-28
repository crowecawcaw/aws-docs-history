# Connect to Amazon Simple Email Service

To connect App Studio with Amazon SES to enable builders to use it to send email notifications from their apps, you must perform
the following steps:

1. [Step 1: Configure Amazon SES resources](#connectors-ses-create-resources "#connectors-ses-create-resources")
2. [Step 2: Create an IAM policy and role with appropriate Amazon SES permissions](#connectors-ses-iam-policy-role "#connectors-ses-iam-policy-role")
3. [Step 3: Create Amazon SES connector](#connectors-ses-create-connector "#connectors-ses-create-connector")

## Step 1: Configure Amazon SES resources

If you haven't, you must first configure Amazon SES to use it to send emails. To learn more about
setting up Amazon SES, see [Getting started with Amazon Simple Email Service](../../../ses/latest/dg/getting-started.md "../../../ses/latest/dg/getting-started.md") in
the _Amazon Simple Email Service Developer Guide_.

## Step 2: Create an IAM policy and role with appropriate Amazon SES permissions

To use Amazon SES resources with App Studio, administrators must create an IAM role to give App Studio
permissions to access the resources. The IAM role controls what Amazon SES functions or resources can be used in App Studio apps.

We recommend creating at least one IAM role per service and policy.

### Step 2a: Create an IAM policy with appropriate Amazon SES permissions

The IAM policy that you create and use with App Studio should contain only the minimally necessary permissions on the appropriate resources
for the application to follow best security practices.

###### To create an IAM policy with appropriate Amazon SES permissions

1. Sign in to the [IAM console](https://console.aws.amazon.com/iam "https://console.aws.amazon.com/iam") with a user that has permissions to create IAM policies. We recommend
   using the administrative user created in
   [Create an administrative user for managing AWS resources](setting-up-first-time-admin.md#setting-up-create-admin-user "setting-up-first-time-admin.md#setting-up-create-admin-user").
2. In the left-side navigation pane, choose **Policies**.
3. Choose **Create policy**.
4. In the **Policy editor** section, choose the **JSON** option.
5. Type or paste in the following JSON policy document.

###### Note

The following policies apply to all Amazon SES resources using the wildcard (`*`). For best security practices, you should replace
the wildcard with the Amazon Resource Name (ARN) of the resources you want to use with App Studio.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "VisualEditor0",
 "Effect": "Allow",
 "Action": "ses:SendEmail",
 "Resource": "*"
 }
 ]
}`

```

6. Choose **Next**.
7. On the **Review and create** page, provide a **Policy name**, such as `SESForAppStudioPolicy`,
   and **Description** (optional).
8. Choose **Create policy** to create the policy.

### Step 2b: Create an IAM role to give App Studio access to Amazon SES

Now, create an IAM role that uses the policy you previously created. App Studio will use this policy to get access
to Amazon SES.

###### To create an IAM role to give App Studio access to Amazon SES

1. Sign in to the [IAM console](https://console.aws.amazon.com/iam "https://console.aws.amazon.com/iam") with a user that has permissions to create IAM roles. We recommend
   using the administrative user created in
   [Create an administrative user for managing AWS resources](setting-up-first-time-admin.md#setting-up-create-admin-user "setting-up-first-time-admin.md#setting-up-create-admin-user").
2. In the left-side navigation pane, choose **Roles**
3. Choose **Create role**.
4. In **Trusted entity type**, choose **Custom trust policy**.
5. Replace the default policy with the following policy to allow App Studio applications to assume this role in your account.

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

Choose **Next**. 6. In **Add permissions**, search for and select the policy that you created in the previous step (`SESForAppStudioPolicy`). Choosing the **+** next to a policy will expand the policy to show the
permissions granted by it and choosing the checkbox selects the policy.

Choose **Next**. 7. On the **Name, review, and create** page, provide a **Role name** and **Description**. 8. In **Step 3: Add tags**,
choose **Add new tag** to add the following tag to provide App Studio access:

    * **Key:** `IsAppStudioDataAccessRole`
    * **Value:** `true`

9. Choose **Create role** and make note of the generated Amazon Resource Name (ARN), you will need it when
   [creating
   the Amazon SES connector in App Studio](#connectors-ses-create-connector "#connectors-ses-create-connector").

## Step 3: Create Amazon SES connector

Now that you Amazon SES and an IAM policy and role configured, use that information to create the connector in App Studio that builders
can use to use Amazon SES in their apps.

###### Note

You must have the Admin role in App Studio to create connectors.

###### To create a connector for Amazon SES

1. Navigate to App Studio.
2. In the left-side navigation pane, choose **Connectors** in the **Manage** section.
   You will be taken to a page displaying a list of existing connectors with some details about each.
3. Choose **+ Create connector**.
4. Choose **Other AWS Services** from the list of connector types.
5. Configure your connector by filling out the following fields:
   - **Name:** Enter a name for your Amazon SES connector.
   - **Description:** Enter a description for your Amazon SES connector.
   - **IAM role:** Enter the Amazon Resource Name (ARN) from
     the IAM role created in [Step 2b: Create an IAM role to give App Studio access to Amazon SES](#connectors-ses-iam-role "#connectors-ses-iam-role").
     For more information about IAM, see the [IAM User Guide](../../../IAM/latest/UserGuide/introduction.md "../../../IAM/latest/UserGuide/introduction.md").
   - **Service:** Choose **Simple Email Service**.
   - **Region:** Choose the AWS Region where your Amazon SES resources are located.

6. Choose **Create**.
7. The newly created connector will appear in the **Connectors** list.
