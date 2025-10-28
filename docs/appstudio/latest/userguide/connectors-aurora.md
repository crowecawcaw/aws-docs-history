# Connect to Amazon Aurora

To connect App Studio with Aurora to enable builders to access and use Aurora resources in applications, you must perform
the following steps:

1. [Step 1: Create and configure Aurora resources](#connectors-aurora-create-resources "#connectors-aurora-create-resources")
2. [Step 2: Create an IAM policy and role with appropriate Aurora permissions](#connectors-aurora-iam "#connectors-aurora-iam")
3. [Step 3: Create Aurora connector in App Studio](#connectors-aurora-create-connector "#connectors-aurora-create-connector")
   App Studio supports the following Aurora versions:

- Aurora MySQL Serverless V1: 5.72
- Aurora PostgreSQL Serverless V1: 11.18, 13.9
- Aurora MySQL Serverless V2: 13.11 or higher, 14.8 or higher, and 15.3 or higher
- Aurora PostgreSQL Serverless V2: 13.11 or higher, 14.8 or higher, and 15.3 or higher

## Step 1: Create and configure Aurora resources

To use Aurora databases with App Studio, you must first create them and configure them appropriately. There are two Aurora database types supported by App Studio: Aurora PostgreSQL and Aurora MySQL. To compare the types, see
[What's the difference between MySQL and PostgreSQL?](https://aws.amazon.com/compare/the-difference-between-mysql-vs-postgresql/ "https://aws.amazon.com/compare/the-difference-between-mysql-vs-postgresql/"). Choose
the appropriate tab and follow the procedure to set up Aurora for use with App Studio apps.

Aurora PostgreSQL
Use the following procedure to create and configure an Aurora PostgreSQL database cluster to be used with App Studio.

###### To set up Aurora for use with App Studio

1. Sign in to the AWS Management Console and open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. Choose **Create database**.
3. Choose **Aurora (PostgreSQL Compatible)**.
4. In **Available versions**, choose any version greater than or equal to version
   `13.11`, `14.8`, and `15.3`.
5. In **Settings**, enter a **DB cluster identifier**.
6. In **Instance configuration**, choose **Serverless v2** and choose an appropriate
   capacity.
7. In **Connectivity**, select **Enable the RDS Data API**.
8. In **Database authentication**, select **IAM database authentication**.
9. In **Additional configuration**, in **Initial database name**,
   enter an initial database name for your database.

Aurora MySQL
Use the following procedure to create and configure an Aurora MySQL database cluster to be used with App Studio.

Aurora MySQL doesn’t support creation from the UI for the versions that support Data API or Serverless v1.
To create a Aurora MySQL cluster that supports the Data API, you must use the AWS CLI.

###### Note

To use Aurora MySQL databases with App Studio, they must be in a virtual private cloud (VPC). For more information, see
[Working with a DB cluster in a VPC](../../../AmazonRDS/latest/AuroraUserGuide/USER_VPC.md "../../../AmazonRDS/latest/AuroraUserGuide/USER_VPC.md")
in the _Amazon Aurora User Guide_.

###### To set up Aurora MySQL for use with App Studio

1. If necessary, install the AWS CLI by following the instructions in
   [Install or update to the latest version of the AWS CLI](../../../cli/latest/userguide/getting-started-install.md "../../../cli/latest/userguide/getting-started-install.md") in the
   _AWS Command Line Interface User Guide_.
2. Sign in to the AWS Management Console and open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
3. In the left-side navigation, choose **Subnet groups**.
4. Choose **Create DB subnet group**.
5. Fill out the information and create the sunbnet group. For more information about subnet groups and using VPCs, see
   [Working with a DB cluster in a VPC](../../../AmazonRDS/latest/AuroraUserGuide/USER_VPC.md "../../../AmazonRDS/latest/AuroraUserGuide/USER_VPC.md")
   in the _Amazon Aurora User Guide_.
6. Run the following AWS CLI command:

```
aws rds create-db-cluster --database-name `db_name` \
    --db-cluster-identifier `db_cluster_identifier` \
    --engine aurora-mysql \
    --engine-version 5.7.mysql_aurora.2.08.3 \
    --engine-mode serverless \
    --scaling-configuration MinCapacity=`4`,MaxCapacity=`32`,SecondsUntilAutoPause=`1000`,AutoPause=true \
    --master-username `userName` \
    --master-user-password `userPass` \
    --availability-zones `us-west-2b` `us-west-2c` \
    --db-subnet-group-name `subnet-group-name`
```

Replace the following fields:

    * Replace `db_name` with the desired database name.
    * Replace `db_cluster_identifier` with the desired database cluster identifier.
    * (Optional) Replace the numbers in the `scaling-configuration` field as desired.
    * Replace `userName` with a desired username.
    * Replace `userPass` with a desired password.
    * In `availability-zones`, add the availability zones from the subnet group you created.
    * Replace `subnet-group-name` with the name of the subnet group you created.

## Step 2: Create an IAM policy and role with appropriate Aurora permissions

To use Aurora resources with App Studio, administrators must create an IAM policy and attach it to an IAM role that is used
to give App Studio permissions to access the configured resources. The IAM policy and role control the scope of data that builders can use and what operations can
be called against that data, such as Create, Read, Update, or Delete.

We recommend creating at least one IAM role per service and policy.

### Step 2a: Create an IAM policy with appropriate Aurora permissions

The IAM policy that you create and use with App Studio should contain only the minimally necessary permissions on the appropriate resources
for the application to follow best security practices.

###### To create an IAM policy with appropriate Aurora permissions

1. Sign in to the [IAM console](https://console.aws.amazon.com/iam "https://console.aws.amazon.com/iam") with a user that has permissions to create IAM roles. We recommend
   using the administrative user created in
   [Create an administrative user for managing AWS resources](setting-up-first-time-admin.md#setting-up-create-admin-user "setting-up-first-time-admin.md#setting-up-create-admin-user").
2. In the left-side navigation pane, choose **Policies**.
3. Choose **Create policy**.
4. In the **Policy editor** section, choose the **JSON** option.
5. Replace the existing snippet with the following snippet, replacing `111122223333` with the AWS
   account number in which the Amazon Redshift and Aurora resources are contained.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "BaselineAuroraForAppStudio",
 "Effect": "Allow",
 "Action": [
 "rds-data:ExecuteStatement",
 "secretsmanager:GetSecretValue"
 ],
 "Resource": [
 "arn:aws:rds:*:`111122223333`:cluster:*",
 "arn:aws:secretsmanager:*:`111122223333`:secret:rds*"
 ]
 }
 ]
}`

```

6. Choose **Next**.
7. On the **Review and create** page, provide a **Policy name**, such as `Aurora_AppStudio`
   and **Description** (optional).
8. Choose **Create policy** to create the policy.

### Step 2b: Create an IAM role to give App Studio access to Aurora resources

Now, create an IAM role that uses the policy you previously created. App Studio will use this policy to get access
to the configured Aurora resources.

###### To create an IAM role to give App Studio access to Aurora resources

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

Choose **Next**. 5. In **Add permissions**, search and select the policy you created earlier (`Aurora_AppStudio`). Choosing the **+** next to a policy will expand the policy to show the
permissions granted by it and choosing the checkbox selects the policy.

Choose **Next**. 6. On the **Name, review, and create** page, provide a **Role name** and **Description**. 7. In **Step 3: Add tags**,
choose **Add new tag** to add the following tag to provide App Studio access:

    * **Key:** `IsAppStudioDataAccessRole`
    * **Value:** `true`

8. Choose **Create role** and make note of the generated Amazon Resource Name (ARN), you
   will need it when [creating
   the Aurora connector in App Studio](#connectors-aurora-create-connector "#connectors-aurora-create-connector").

## Step 3: Create Aurora connector in App Studio

Now that you have your Aurora resources and IAM policy and role configured, use that information to create the connector in App Studio that builders
can use to connect their apps to Aurora.

###### Note

You must have the Admin role in App Studio to create connectors.

###### To create a connector for Aurora

1. Navigate to App Studio.
2. In the left-side navigation pane, choose **Connectors** in the **Manage** section.
   You will be taken to a page displaying a list of existing connectors with some details about each.
3. Choose **+ Create connector**.
4. Choose the **Amazon Aurora** connector.
5. Configure your connector by filling out the following fields:
   - **Name:** Enter a name for your Aurora connector.
   - **Description:** Enter a description for your Aurora connector.
   - **IAM role:** Enter the Amazon Resource Name (ARN) from
     the IAM role created in [Step 2b: Create an IAM role to give App Studio access to Aurora resources](#connectors-aurora-iam-role "#connectors-aurora-iam-role").
     For more information about IAM, see the [IAM User Guide](../../../IAM/latest/UserGuide/introduction.md "../../../IAM/latest/UserGuide/introduction.md").
   - **Secret ARN:** Enter the secret ARN of the database cluster. For information about where to find the secret ARN, see
     [Viewing the details about a secret for a DB cluser](../../../AmazonRDS/latest/AuroraUserGuide/rds-secrets-manager.md#rds-secrets-manager-view-db-cluster "../../../AmazonRDS/latest/AuroraUserGuide/rds-secrets-manager.md#rds-secrets-manager-view-db-cluster")
     in the _Amazon Aurora User Guide_.
   - **Region:** Choose the AWS Region where your Aurora resources are located.
   - **Database ARN:** Enter the ARN of the database cluster. The ARN can be found in the **Configuration** tab of the database
     cluster, similar to the secret ARN.
   - **Database type:** Choose the database type, **MySQL** or **PostgreSQL**, that matches the
     type of database created in [Step 1: Create and configure Aurora resources](#connectors-aurora-create-resources "#connectors-aurora-create-resources").
   - **Database name:** Enter the name of the database, which can also be found in the **Configuration** tab
     of the database cluster.
   - **Available tables:** Select the tables you want to use with App Studio using this connector.

6. Choose **Next** to review or define the entity mappings.
7. Choose **Create** to create the Aurora connector. The newly created connector will appear in the **Connectors** list.
