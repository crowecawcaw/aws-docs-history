# Connect to Amazon DynamoDB

To connect App Studio with DynamoDB to enable builders to access and use DynamoDB resources in applications, you must perform
the following steps:

1. [Step 1: Create and configure DynamoDB resources](#connectors-dynamodb-create-resources "#connectors-dynamodb-create-resources")
2. [Step 2: Create an IAM policy and role with appropriate DynamoDB permissions](#connectors-dynamodb-iam "#connectors-dynamodb-iam")
3. [Create DynamoDB connector](#connectors-dynamodb-create-connector "#connectors-dynamodb-create-connector")

## Step 1: Create and configure DynamoDB resources

Use the following procedure to create and configure DynamoDB resources to be used with App Studio.

###### To set up DynamoDB for use with App Studio

1. Sign in to the AWS Management Console and open the DynamoDB console at
   [https://console.aws.amazon.com/dynamodb/](https://console.aws.amazon.com/dynamodb/ "https://console.aws.amazon.com/dynamodb/").

We recommend
using the administrative user created in
[Create an administrative user for managing AWS resources](setting-up-first-time-admin.md#setting-up-create-admin-user "setting-up-first-time-admin.md#setting-up-create-admin-user"). 2. In the left navigation pane, choose **Tables**. 3. Choose **Create table**. 4. Enter a name and keys for your table. 5. Choose **Create table**. 6. After your table is created, add some items to it so they will appear once the table is connected to App Studio.

    1. Choose your table, choose **Actions**, and choose **Explore items**.
    2. In **Items returned**, choose **Create item**.
    3. (Optional): Choose **Add new attribute** to add more attributes to your table.
    4. Enter values for each attribute and choose **Create item**.

## Step 2: Create an IAM policy and role with appropriate DynamoDB permissions

To use DynamoDB resources with App Studio, administrators must create an IAM policy and role to give App Studio
permissions to access the resources. The IAM policy controls the scope of data that builders can use and what operations can
be called against that data, such as Create, Read, Update, or Delete. The IAM policy is then attached to an IAM role that is used by App Studio.

We recommend creating at least one IAM role per service and policy. For example, if builders are creating two
applications backed by the same tables in DynamoDB, one that only requires read access, and one that
requires read, create, update and delete; an administrator should create two IAM roles, one using read only permissions,
and one with full CRUD permissions to the applicable tables in DynamoDB.

### Step 2a: Create an IAM policy with appropriate DynamoDB permissions

The IAM policy that you create and use with App Studio should contain only the minimally necessary permissions on the appropriate resources
for the application to follow best security practices.

###### To create an IAM policy with appropriate DynamoDB permissions

1. Sign in to the [IAM console](https://console.aws.amazon.com/iam "https://console.aws.amazon.com/iam") with a user that has permissions to create IAM policies. We recommend
   using the administrative user created in
   [Create an administrative user for managing AWS resources](setting-up-first-time-admin.md#setting-up-create-admin-user "setting-up-first-time-admin.md#setting-up-create-admin-user").
2. In the left-side navigation pane, choose **Policies**.
3. Choose **Create policy**.
4. In the **Policy editor** section, choose the **JSON** option.
5. Type or paste in a JSON policy document. The following tabs contain example policies for read only and full access to DynamoDB tables,
   along with examples of policies that include AWS KMS permissions for DynamoDB tables encrypted with an AWS KMS customer-managed key (CMK).

###### Note

The following policies apply to all DynamoDB resources using the wildcard (`*`). For best security practices, you should replace
the wildcard with the Amazon Resource Name (ARN) of the resources you want to use with App Studio.

Read only
The following policy grants read access to the configured DynamoDB resources.

JSONJSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "ReadOnlyDDBForAppStudio",
 "Effect": "Allow",
 "Action": [
 "dynamodb:ListTables",
 "dynamodb:DescribeTable",
 "dynamodb:PartiQLSelect"
 ],
 "Resource": "*"
 }
 ]
}`

```

Full access
The following policy grants create, read, update, and delete access to the configured DynamoDB resources.

JSONJSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "FullAccessDDBForAppStudio",
 "Effect": "Allow",
 "Action": [
 "dynamodb:ListTables",
 "dynamodb:DescribeTable",
 "dynamodb:PartiQLSelect",
 "dynamodb:PartiQLInsert",
 "dynamodb:PartiQLUpdate",
 "dynamodb:PartiQLDelete"
 ],
 "Resource": "*"
 }
 ]
}`

```

Read only - KMS encrypted
The following policy grants read access to the configured encrypted DynamoDB resources by providing AWS KMS permissions. You must replace the ARN with the ARN of the
AWS KMS key.

JSONJSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "ReadOnlyDDBForAppStudio",
 "Effect": "Allow",
 "Action": [
 "dynamodb:ListTables",
 "dynamodb:DescribeTable",
 "dynamodb:PartiQLSelect"
 ],
 "Resource": "*"
 },
 {
 "Sid": "KMSPermissionsForEncryptedTable",
 "Effect": "Allow",
 "Action": [
 "kms:Decrypt",
 "kms:DescribeKey"
 ],
 "Resource": "arn:aws:kms:`us-west-2`:`111122223333`:key/`1234abcd-12ab-34cd-56ef-1234567890ab`"
 }
 ]
}`

```

Full access - KMS encrypted
The following policy grants read access to the configured encrypted DynamoDB resources by providing AWS KMS permissions. You must replace the ARN with the ARN of the
AWS KMS key.

JSONJSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "ReadOnlyDDBForAppStudio",
 "Effect": "Allow",
 "Action": [
 "dynamodb:ListTables",
 "dynamodb:DescribeTable",
 "dynamodb:PartiQLSelect",
 "dynamodb:PartiQLInsert",
 "dynamodb:PartiQLUpdate",
 "dynamodb:PartiQLDelete"
 ],
 "Resource": "*"
 },
 {
 "Sid": "KMSPermissionsForEncryptedTable",
 "Effect": "Allow",
 "Action": [
 "kms:Decrypt",
 "kms:DescribeKey"
 ],
 "Resource": "arn:aws:kms:`us-west-2`:`111122223333`:key/`1234abcd-12ab-34cd-56ef-1234567890ab`"
 }
 ]
}`

```

6. Choose **Next**.
7. On the **Review and create** page, provide a **Policy name**, such as `ReadOnlyDDBForAppStudio`
   or `FullAccessDDBForAppStudio`, and **Description** (optional).
8. Choose **Create policy** to create the policy.

### Step 2b: Create an IAM role to give App Studio access to DynamoDB resources

Now, create an IAM role that uses the policy you previously created. App Studio will use this policy to get access
to the configured DynamoDB resources.

###### To create an IAM role to give App Studio access to DynamoDB resources

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

Choose **Next**. 5. In **Add permissions**, search for and select the policy that you created in the previous step (`ReadOnlyDDBForAppStudio`
or `FullAccessDDBForAppStudio`). Choosing the **+** next to a policy will expand the policy to show the
permissions granted by it and choosing the checkbox selects the policy.

Choose **Next**. 6. On the **Name, review, and create** page, provide a **Role name** and **Description**. 7. In **Step 3: Add tags**,
choose **Add new tag** to add the following tag to provide App Studio access:

    * **Key:** `IsAppStudioDataAccessRole`
    * **Value:** `true`

8. Choose **Create role** and make note of the generated Amazon Resource Name (ARN), you
   will need it when [creating
   the DynamoDB connector in App Studio](#connectors-dynamodb-create-connector "#connectors-dynamodb-create-connector").

## Create DynamoDB connector

Now that you have your DynamoDB resources and IAM policy and role configured, use that information to create the connector in App Studio that builders
can use to connect their apps to DynamoDB.

###### Note

You must have the Admin role in App Studio to create connectors.

###### To create a connector for DynamoDB

1. Navigate to App Studio.
2. In the left-side navigation pane, choose **Connectors** in the **Manage** section.
   You will be taken to a page displaying a list of existing connectors with some details about each.
3. Choose **+ Create connector**.
4. Choose **Amazon DynamoDB** from the list of connector types.
5. Configure your connector by filling out the following fields:
   - **Name:** Enter a name for your DynamoDB connector.
   - **Description:** Enter a description for your DynamoDB connector.
   - **IAM role:** Enter the Amazon Resource Name (ARN) from
     the IAM role created in [Step 2b: Create an IAM role to give App Studio access to DynamoDB resources](#connectors-dynamodb-iam-role "#connectors-dynamodb-iam-role").
     For more information about IAM, see the [IAM User Guide](../../../IAM/latest/UserGuide/introduction.md "../../../IAM/latest/UserGuide/introduction.md").
   - **Region:** Choose the AWS Region where your DynamoDB resources are located.
   - **Available tables:** Select the tables you want to connect to App Studio.

6. Choose **Next**. Review the connection information and choose **Create**.
7. The newly created connector will appear in the **Connectors** list.
