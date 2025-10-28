# Connect to Amazon Redshift

To connect App Studio with Amazon Redshift to enable builders to access and use Amazon Redshift resources in applications, you must perform
the following steps:

1. [Step 1: Create and configure Amazon Redshift resources](#connectors-redshift-create-resources "#connectors-redshift-create-resources")
2. [Step 2: Create an IAM policy and role with appropriate Amazon Redshift permissions](#connectors-redshift-iam "#connectors-redshift-iam")
3. [Step 3: Create Amazon Redshift connector](#connectors-redshift-create-connector "#connectors-redshift-create-connector")

## Step 1: Create and configure Amazon Redshift resources

Use the following procedure to create and configure Amazon Redshift resources to be used with App Studio.

###### To set up Amazon Redshift for use with App Studio

1. Sign in to the AWS Management Console and open the Amazon Redshift console at
   [https://console.aws.amazon.com/redshiftv2/](https://console.aws.amazon.com/redshiftv2/ "https://console.aws.amazon.com/redshiftv2/").

We recommend
using the administrative user created in
[Create an administrative user for managing AWS resources](setting-up-first-time-admin.md#setting-up-create-admin-user "setting-up-first-time-admin.md#setting-up-create-admin-user"). 2. Create a Redshift Serverless data warehouse or a provisiond cluster. For more information, see
[Creating a data warehouse with Redshift Serverless](../../../redshift/latest/gsg/new-user-serverless.md#serverless-console-resource-creation "../../../redshift/latest/gsg/new-user-serverless.md#serverless-console-resource-creation")
or [Creating a cluster](../../../redshift/latest/mgmt/managing-clusters-console.md#create-cluster "../../../redshift/latest/mgmt/managing-clusters-console.md#create-cluster") in the
_Amazon Redshift User Guide_. 3. Once provisioning is complete, choose **Query Data** to open the query editor. Connect to your database. 4. Change the following settings:

    1. Set **Isolated session** toggle to `OFF`.
     This is needed so that you can see data changes made by other users, such as from a running App Studio application.
    2. Choose the “gear” icon. Choose **Account settings**. Increase **Maximum concurrent
     connections** to `10`. This is the limit on the number of query editor sessions that can connect to a Amazon Redshift database.
     It does not apply to other clients such as App Studio applications.

5. Create your data tables under the `public` schema. `INSERT` any initial data into these tables.
6. Run the following commands in query editor:

The following command creates a database user and connects it with an IAM role named `AppBuilderDataAccessRole` that is used by
App Studio. You will create
the IAM role in a later step, and the name here must match the name given to that role.

```
CREATE USER "IAMR:`AppBuilderDataAccessRole`" WITH PASSWORD DISABLE;
```

The following command grants all permissions on all tables to App Studio.

###### Note

For best security practices, you should
scope down the permissions here to the minimal required permissions on the appropriate tables. For more information about the `GRANT`
command, see [GRANT](../../../redshift/latest/dg/r_GRANT.md "../../../redshift/latest/dg/r_GRANT.md") in the Amazon Redshift Database Developer Guide.

```
GRANT ALL ON ALL TABLES IN SCHEMA public to "IAMR:`AppBuilderDataAccessRole`";
```

## Step 2: Create an IAM policy and role with appropriate Amazon Redshift permissions

To use Amazon Redshift resources with App Studio, administrators must create an IAM policy and role to give App Studio
permissions to access the resources. The IAM policy controls the scope of data that builders can use and what operations can
be called against that data, such as Create, Read, Update, or Delete. The IAM policy is then attached to an IAM role that is used by App Studio.

We recommend creating at least one IAM role per service and policy. For example, if builders are creating
two applications backed by different tables in Amazon Redshift, an administrator should create two IAM policies and roles, one for each of
the tables in Amazon Redshift.

### Step 2a: Create an IAM policy with appropriate Amazon Redshift permissions

The IAM policy that you create and use with App Studio should contain only the minimally necessary permissions on the appropriate resources
for the application to follow best security practices.

###### To create an IAM policy with appropriate Amazon Redshift permissions

1. Sign in to the [IAM console](https://console.aws.amazon.com/iam "https://console.aws.amazon.com/iam") with a user that has permissions to create IAM policies. We recommend
   using the administrative user created in
   [Create an administrative user for managing AWS resources](setting-up-first-time-admin.md#setting-up-create-admin-user "setting-up-first-time-admin.md#setting-up-create-admin-user").
2. In the left-side navigation pane, choose **Policies**.
3. Choose **Create policy**.
4. In the **Policy editor** section, choose the **JSON** option.
5. Type or paste in a JSON policy document. The following tabs contain example policies for both provisioned and serverless Amazon Redshift.

###### Note

The following policies apply to all Amazon Redshift resources using the wildcard (`*`). For best security practices, you should replace
the wildcard with the Amazon Resource Name (ARN) of the resources you want to use with App Studio.

Provisioned
JSONJSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "ProvisionedRedshiftForAppStudio",
 "Effect": "Allow",
 "Action": [
 "redshift:DescribeClusters",
 "redshift:GetClusterCredentialsWithIAM",
 "redshift-data:ListDatabases",
 "redshift-data:ListTables",
 "redshift-data:DescribeTable",
 "redshift-data:DescribeStatement",
 "redshift-data:ExecuteStatement",
 "redshift-data:GetStatementResult"
 ],
 "Resource": "*"
 }
 ]
}`

```

Serverless
JSONJSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "ServerlessRedshiftForAppStudio",
 "Effect": "Allow",
 "Action": [
 "redshift-serverless:ListNamespaces",
 "redshift-serverless:GetCredentials",
 "redshift-serverless:ListWorkgroups",
 "redshift-data:ListDatabases",
 "redshift-data:ListTables",
 "redshift-data:DescribeTable",
 "redshift-data:DescribeStatement",
 "redshift-data:ExecuteStatement",
 "redshift-data:GetStatementResult"
 ],
 "Resource": "*"
 }
 ]
}`

```

6. Choose **Next**.
7. On the **Review and create** page, provide a **Policy name**, such as `RedshiftServerlessForAppStudio`
   or `RedshiftProvisionedForAppStudio`, and **Description** (optional).
8. Choose **Create policy** to create the policy.

### Step 2b: Create an IAM role to give App Studio access to Amazon Redshift resources

Now, create an IAM role that uses the policy you previously created. App Studio will use this policy to get access
to the configured Amazon Redshift resources.

###### To create an IAM role to give App Studio access to Amazon Redshift resources

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

Choose **Next**. 6. In **Add permissions**, search for and select the policy that you created in the previous step (`RedshiftServerlessForAppStudio`
or `RedshiftProvisionedForAppStudio`). Choosing the **+** next to a policy will expand the policy to show the
permissions granted by it and choosing the checkbox selects the policy.

Choose **Next**. 7. On the **Name, review, and create** page, provide a **Role name** and **Description**.

###### Important

The role name here must match the role name used in the `GRANT` command in
[Step 1: Create and configure Amazon Redshift resources](#connectors-redshift-create-resources "#connectors-redshift-create-resources")
(`AppBuilderDataAccessRole`). 8. In **Step 3: Add tags**,
choose **Add new tag** to add the following tag to provide App Studio access:

    * **Key:** `IsAppStudioDataAccessRole`
    * **Value:** `true`

9. Choose **Create role** and make note of the generated Amazon Resource Name (ARN), you will need it when [creating
   the Amazon Redshift connector in App Studio](#connectors-redshift-create-connector "#connectors-redshift-create-connector").

## Step 3: Create Amazon Redshift connector

Now that you have your Amazon Redshift resources and IAM policy and role configured, use that information to create the connector in App Studio that builders
can use to connect their apps to Amazon Redshift.

###### Note

You must have the Admin role in App Studio to create connectors.

###### To create a connector for Amazon Redshift

1. Navigate to App Studio.
2. In the left-side navigation pane, choose **Connectors** in the **Manage** section.
   You will be taken to a page displaying a list of existing connectors with some details about each.
3. Choose **+ Create connector**.
4. Choose the **Amazon Redshift** connector.
5. Configure your connector by filling out the following fields:
   - **Name:** Provide a name for your connector.
   - **Description:** Provide a description for your connector.
   - **IAM Role:** Enter the Amazon Resource Name (ARN) from
     the IAM role created in [Step 2b: Create an IAM role to give App Studio access to Amazon Redshift resources](#connectors-redshift-iam-role "#connectors-redshift-iam-role"). For more information about IAM, see the [IAM User Guide](../../../IAM/latest/UserGuide/introduction.md "../../../IAM/latest/UserGuide/introduction.md").
   - **Region:** Choose the AWS Region where your Amazon Redshift resources are located.
   - **Compute type:** Choose if you are using Amazon Redshift Serverless or a provisioned cluster.
   - **Cluster or Workgroup selection:** If **Provisioned** is chosen, choose the cluster you want
     to connect to App Studio. If **Serverless** is chosen, choose the workgroup.
   - **Database selection:** Choose the database you want to connect to App Studio.
   - **Available tables:** Select the tables you want to connect to App Studio.

6. Choose **Next**. Review the connection information and choose **Create**.
7. The newly created connector will appear in the **connectors** list.
