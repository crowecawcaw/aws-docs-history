# Associated accounts in Amazon DataZone

Associating your AWS accounts with your Amazon DataZone domain enables domain users to publish
and consume data from these AWS accounts. There are three steps to setting up an account
association.

- First, share the domain with the desired AWS account by requesting association.
  Amazon DataZone uses AWS Resource Access Manager (RAM) if the AWS account is different from
  the domain’s AWS account. An account association can only be initiated by the Amazon DataZone
  domain.
- Second, have the account owner accept the association request.
- Third, have the account owner enable the desired environment blueprints. By enabling a
  blueprint, the account owner is providing users in the domain the IAM roles and resource
  configurations necessary to create and access resources in their account, such as AWS Glue
  databases and Amazon Redshift clusters.
  Complete the following step to associate an account with Amazon DataZone:

- Step 1 - [Request association with other AWS
  accounts](#invite-account-to-associate "#invite-account-to-associate")
- Step 2 - [Accept an account association request from an
  Amazon DataZone domain and enable an environment blueprint](#accept-invitation-to-associate "#accept-invitation-to-associate")
- Step 3 - [Enable an environment blueprint in an
  associated AWS account](#enable-blueprint-in-associated-account "#enable-blueprint-in-associated-account")

## Request association with other AWS

accounts

###### Note

By sending an association request to another AWS account, you are sharing your domain
with the other AWS account with AWS Resource Access Manager (RAM). Be sure to check the
accuracy of the account ID that you enter.

To request association with other AWS accounts in the Amazon DataZone console for an
Amazon DataZone domain, you must assume an IAM role in the account with administrative permissions.
[Configure the IAM permissions required to use the
Amazon DataZone management console](create-iam-roles.md "create-iam-roles.md") to obtain the minimum
permissions necessary to request an account association.

Complete the following procedure to request association with other AWS accounts.

1. Sign in to the AWS Management Console and open the Amazon DataZone management console at
   [https://console.aws.amazon.com/datazone](https://console.aws.amazon.com/datazone "https://console.aws.amazon.com/datazone").
2. Choose **View domains** and choose the domain’s name from the list.
   The name is a hyperlink.
3. Scroll down to the **Associated accounts** tab and choose
   **Request association**.
4. Enter the IDs of the accounts that you want to request association. When you are
   satisfied with the list of account IDs, choose **Request
   association**.
5. Under RAM Policy, specify the RAM policy for account association. You can either
   choose `AWSRAMPermissionDataZonePortalReadWrite` which will enable associated
   accounts to execute Amazon DataZone APIs and access the data portal or you can choose
   `AWSRAMPermissionDataZoneDefault`, whcih will allow associated accounts to
   only execute Amazon DataZone APIs and will not provide data portal access. Amazon DataZone then
   creates a resource share in the AWS Resource Access Manager on your account’s behalf,
   with the entered account ID(s) as principals.
6. You must notify the owner of the other AWS account(s) to accept your request.
   Invitations expire after seven (7) days.

### Provide

account access to your customer-managed KMS key

Amazon DataZone domains and their metadata are encrypted, either (by default) using a key
held by AWS, or (optionally) a customer-managed key from AWS Key Management Service
(KMS) that you own and provide during domain creation. If your domain is encrypted with a
customer-managed key, then follow the procedure below to give the associated account
permission to use the KMS key.

1. Sign in to the AWS Management Console and open the KMS console at [https://console.aws.amazon.com/kms/](https://console.aws.amazon.com/kms/ "https://console.aws.amazon.com/kms/").
2. To view the keys in your account that you create and manage, in the navigation pane
   choose **Customer managed keys**.
3. To view the keys in your account that you create and manage, in the navigation pane
   choose Customer managed keys.
4. In the list of KMS keys, choose the alias or key ID of the KMS key that you want to
   examine.
5. To allow or disallow external AWS accounts to use the KMS key, use the controls in
   the **Other AWS accounts** section of the page. IAM principals in
   these accounts (with proper KMS permissions themselves) can use the KMS key in
   cryptographic operations, such as encrypting, decrypting, re-encrypting, and generating
   data keys.

## Accept an account association request from an

Amazon DataZone domain and enable an environment blueprint

To accept association in the Amazon DataZone management console with an Amazon DataZone domain, you
must assume an IAM role in the account with administrative permissions. [Configure the IAM permissions required to use the
Amazon DataZone management console](create-iam-roles.md "create-iam-roles.md") to obtain the minimum
permissions.

Complete the following to accept association with an Amazon DataZone domain.

1. Sign in to the AWS Management Console and open the Amazon DataZone management console at
   [https://console.aws.amazon.com/datazone](https://console.aws.amazon.com/datazone "https://console.aws.amazon.com/datazone").
2. Choose **View requests** and select the inviting domain from the
   list. The state of the invitation should be **Requested**. Choose
   **Review request**.
3. Choose whether to enable the default data lake and/or data warehouse environment
   blueprints by selecting neither, both, or one of the boxes. You can do this later.
   - The data lake environment blueprint enables domain users to create and manage
     AWS Glue, Amazon S3, and Amazon Athena resources to publish and consume from a data
     lake.
   - The data warehouse environment blueprint enables domain users to create and manage
     Amazon Redshift resources to publish and consume from a data warehouse.

4. If you choose to select one or both of the default environment blueprints, then
   configure the following permissions and resources.
   - The **Manage access IAM role** provides permissions to Amazon DataZone
     to enable domain users to ingest and manage access to tables, like AWS Glue and
     Amazon Redshift. You can choose to have Amazon DataZone create and use a new IAM role, or
     you can choose from a list of existing IAM roles.
   - The **Provisioning IAM role** provides permissions to Amazon DataZone
     to enable domain users to create and configure environment resources, like AWS Glue
     databases. You can choose to have Amazon DataZone create and use a new IAM role, or you can
     choose from a list of existing IAM roles.
   - The **Amazon S3 bucket for Data Lake** is the bucket or path that
     Amazon DataZone will use when domain users store data lake data. You can use the default
     bucket selected by Amazon DataZone or choose your own existing Amazon S3 path by entering
     its path string. If you select your own Amazon S3 path, you will need to update IAM
     policies to provide Amazon DataZone with permissions to use it.

5. When you are satisfied with your configurations, choose **Accept and configure
   association**.

## Enable an environment blueprint in an

associated AWS account

To enable an environment blueprint in the Amazon DataZone management console, you must assume
an IAM role in the account with administrative permissions. [Configure the IAM permissions required to use the
Amazon DataZone management console](create-iam-roles.md "create-iam-roles.md") to obtain the minimum permissions.

Complete the following to enable a blueprint in an associated domain.

1. Sign in to the AWS Management Console and open the Amazon DataZone management console at
   [https://console.aws.amazon.com/datazone](https://console.aws.amazon.com/datazone "https://console.aws.amazon.com/datazone").
2. Open the left navigation panel and choose **Associated
   domains**.
3. Choose the domain for which you want to enable an environment blueprint.
4. From the **Blueprints** list, choose either the
   **DefaultDataLake** or the **DefaultDataWarehouse**,
   or the **Amazon SageMaker**, or the **Custom AWS
   Service** blueprint.

###### Note

If you are enabling the **Custom AWS service** blueprint, you do
not need to specify a manage access role. The permissions and the authorization
mechanism for the **Custom AWS service** bluerpint are handled when
you're creating environments using this blueprint. For more information, see [Create an environment using a custom AWS
service blueprint](create-custom-environment.md "create-custom-environment.md"). 5. On the chosen blueprint's details page, choose **Enable in this
account**. 6. On the Permissions and resources page, specify the following:

    * If you're enabling the **DefaultDataLake** blueprint, for
     **Glue Manage Access role**, specify a new or existing service role
     that grants Amazon DataZone authorization to ingest and manage access to tables in AWS
     Glue and AWS Lake Formation.
    * If you're enabling the **DefaultDataWarehouse** blueprint, for
     **Redshift Manage Access role**, specify a new or existing service
     role that grants Amazon DataZone authorization to ingest and manage access to datashares,
     tables and views in Amazon Redshift.
    * If you're enabling the **Amazon SageMaker** blueprint, for
     **SageMaker Manage Access role**, specify a new or existing service
     role that grants Amazon DataZone permissions to publish Amazon SageMaker data to the
     catalog. It also gives Amazon DataZone permissions to grant access or revoke access to
     Amazon SageMaker published assets in the catalog.


    ###### Important

    When you're enabling the **Amazon SageMaker** blueprint,
     Amazon DataZone checks whether the following IAM roles for Amazon DataZone exist in the
     current account and region. If these roles do not exist, Amazon DataZone automatically
     creates them.



    	+ AmazonDataZoneGlueAccess-<region>-<domainId>
    	+ AmazonDataZoneRedshiftAccess-<region>-<domainId>
    * For **Provisioning role**, specify a new or existing service role
     that grants Amazon DataZone authorization to create and configure environment resources
     using AWS CloudFormation in the environment account and region.
    * If you're enabling the **Amazon SageMaker** blueprint, for the
     **Amazon S3 bucket for SageMaker-Glue data source**, specify an
     Amazon S3 bucket that is to be used by all SageMaker environments in the AWS
     account. The bucket prefix that you specify must be one of the following:




    	+ amazon-datazone\*
    	+ datazone-sagemaker\*
    	+ sagemaker-datazone\*
    	+ DataZone-Sagemaker\*
    	+ Sagemaker-DataZone\*
    	+ DataZone-SageMaker\*
    	+ SageMaker-DataZone\*

7. Choose **Enable blueprint**.

Once you enable the chose blueprint(s), you can control which projects can use the
blueprint(s) in your account to create environment profiles. You can do this by assigning
managing projects to the blueprint’s configuration.

###### Specify managing projects on enabled

DefaultDataLake or DefaultDataWarehouse blueprint

1. Navigate to the Amazon DataZone console at [https://console.aws.amazon.com/datazone](https://console.aws.amazon.com/datazone "https://console.aws.amazon.com/datazone") and sign in with your account
   credentials.
2. Open the left navigation panel and choose **Associated domains** and
   then choose the domain where you want to add managing projects.
3. Choose the **Blueprints** tab and then choose DefaultDataLake or
   DefaultDataWareshouse blueprint.
4. By default, all projects within the domain can use the DefaultDataLake or
   DefaultDataWareshouse blueprint in the account to create environment profiles. However,
   you can restrict this by assigning managing projects to the blueprint. To add managing
   projects, choose **Select managing project**, then choose the projects
   that you want to add as managing projects from the drop down menu, and then choose
   **Select managing projects(s)**.

Once you enable the DefaultDataWarehouse blueprint in your AWS account, you can add
parameter sets to the blueprint configuration. A parameter set is a group of keys and values,
required for Amazon DataZone to establish a connection to your Amazon Redshift cluster and is used
to create data warehouse environments. These parameters include the name of your Amazon
Redshift cluster, database, and the AWS secret that holds credentials to the cluster.

###### Important

By default, no managing projects are specified for for the environment blueprints, which
means that any Amazon DataZone user can create profiles for an environment blueprint. Therefore,
it is strongly recommended that you always specify managing projects for your environment
blueprints to ensure stronger governance.

###### Adding parameter sets to the DefaultDataWarehouse

blueprint

1. Navigate to the Amazon DataZone console at [https://console.aws.amazon.com/datazone](https://console.aws.amazon.com/datazone "https://console.aws.amazon.com/datazone") and sign in with your account
   credentials.
2. Open the left navigation panel and choose **Associated domains** and
   then choose the domain where you want to add parameter sets.
3. Choose the **Blueprints** tab and then choose the
   DefaultDataWareshouse blueprint to open the blueprint details page.
4. Under the **Parameter sets** tab on the blueprint details page,
   choose **Create parameter set**.
   - Provide a Name for the parameter set.
   - Optionally, provide a description for the parameter set.
   - Select a region
   - Select either Amazon Redshift cluster or Amazon Redshift Serverless.
   - Select the AWS secret ARN that holds the credentials to the selected Amazon
     Redshift cluster or the Amazon Redshift Serverless workgroup. The AWS secret must be
     tagged with the `AmazonDataZoneDomain : [Domain_ID]` tag in order to be
     eligible for use within a parameter set.
     - If you do not have an existing AWS secret, you can also create a new secret
       by choosing **Create New AWS Secret**. This opens a dialog box
       where you can provide the name of the secret, username, and password. Once you
       choose **Create New AWS Secret**, Amazon DataZone creates a new
       secret in the AWS Secrets Manager service and ensures that the secret is tagged
       with the domain in which you are trying to create the parameter set.

   - Select either Amazon Redshift cluster or Amazon Redshift Serverless
     workgroup.
   - Enter the name of the database within the selected Amazon Redshift cluster or
     Amazon Redshift Serverless workgroup.
   - Choose **Create parameter set**.

###### Note

You can only add up to 10 parameter sets to the DefaultDataWarehouse blueprint.

Once you enable the Amazon SageMaker blueprint in your AWS account, you can add
parameter sets to the blueprint configuration. A parameter set is a group of keys and values,
required for Amazon DataZone to establish a connection to your Amazon SageMaker and is used to
create sagemaker environments.

###### Adding parameter sets to the Amazon SageMaker blueprint

1. Navigate to the Amazon DataZone console at [https://console.aws.amazon.com/datazone](https://console.aws.amazon.com/datazone "https://console.aws.amazon.com/datazone") and sign in with your account
   credentials.
2. Choose **View domains** and then choose the domain that contains the
   enabled blueprint where you want to add the parameter set.
3. Choose the **Blueprints** tab and then choose the Amazon SageMaker
   blueprint to open the blueprint's details page.
4. Under the **Parameter sets** tab on the blueprint details page,
   choose **Create parameter set**, and then specify the following:
   - Provide a **Name** for the parameter set.
   - Optionally, provide a **Description** for the parameter
     set.
   - Specify the Amazon SageMaker domain authentication type. You can choose either IAM
     or IAM Identity Center (SSO).
   - Specify an AWS region.
   - Specify an AWS KMS key for data encryption. You can choose an existing key or
     create a new key.
   - Under **Environment parameters**, specify the following:
     - VPC ID - the ID that you're using for the VPC of the Amazon SageMaker
       environment. You can specify an existing or create a new VPC.
     - Subnets - one or more IDs for a range of IP addresses for specific resources
       within your VPC.
     - Network access - choose either **VPC only** or
       **Public internet only**.
     - Security group - the security group to use when configuring VPC and subnets.

   - Under Data source parameters, choose one of the following:
     - AWS Glue only
     - AWS Glue + Amazon Redshift Serverless. If you choose this option, specify
       the following:
       - Specify the AWS secret ARN that holds the credentials to the selected
         Amazon Redshift cluster. The AWS secret must be tagged with the
         `AmazonDataZoneDomain : [Domain_ID]` tag in order to be eligible
         for use within a parameter set.

       If you do not have an existing AWS secret, you can also create a new
       secret by choosing **Create New AWS Secret**. This opens a
       dialog box where you can provide the name of the secret, username, and
       password. Once you choose **Create New AWS Secret**,
       Amazon DataZone creates a new secret in the AWS Secrets Manager service and
       ensures that the secret is tagged with the domain in which you are trying to
       create the parameter set.
       - Specify the Amazon Redshift workgroup you want to use when creating
         environments.
       - Specify the name of the database (within the workgroup you've chosen) that
         you want to use when creating environments.

     - AWS Glue only + Amazon Redshift Cluster
       - Specify the AWS secret ARN that holds the credentials to the selected
         Amazon Redshift cluster. The AWS secret must be tagged with the
         `AmazonDataZoneDomain : [Domain_ID]` tag in order to be eligible
         for use within a parameter set.

       If you do not have an existing AWS secret, you can also create a new
       secret by choosing **Create New AWS Secret**. This opens a
       dialog box where you can provide the name of the secret, username, and
       password. Once you choose **Create New AWS Secret**,
       Amazon DataZone creates a new secret in the AWS Secrets Manager service and
       ensures that the secret is tagged with the domain in which you are trying to
       create the parameter set.
       - Specify the Amazon Redshift cluster you want to use when creating
         environments.
       - Specify the name of the database (within the cluster you've chosen) that
         you want to use when creating environments.

5. Choose **Create parameter set**.
