# Amazon DataZone built-in blueprints

A blueprint with which an environment is created defines what tools and services members
of the project to which the environment belongs can use as they work with assets in the
Amazon DataZone catalog. In the current release of Amazon DataZone, there are the following built-in
blueprints:

- Data lake blueprint
- Data warehouse blueprint
- Amazon SageMaker blueprint
  You can run through the steps of the following procedures to enable default blueprints in
  Amazon DataZone:

- [Enable built-in blueprints in the AWS
  account that owns the Amazon DataZone domain](#enable-default-blueprint "#enable-default-blueprint")
- [Add Amazon SageMaker as a trusted
  service in the AWS account that owns the Amazon DataZone domain](#add-sagemaker-as-trusted-service "#add-sagemaker-as-trusted-service")

## Enable built-in blueprints in the AWS

account that owns the Amazon DataZone domain

A blueprint with which an environment is created defines what tools and services
members of the project to which the environment belongs can use as they work with assets
in the Amazon DataZone catalog.

In the current release of Amazon DataZone, there are several built-in blueprints: data lake
blueprint, data warehouse blueprint, and Amazon SageMaker blueprint.

- Data lake blueprint contains the definition for launching and configuring a
  set of services (AWS Glue, AWS Lake Formation, Amazon Athena) to publish and
  use data lake assets in the Amazon DataZone catalog.
- Data warehouse blueprint contains the definition for launching and configuring
  a set of services (Amazon Redshift) to publish and use Amazon Redshift assets in
  the Amazon DataZone catalog.
- Amazon SageMaker blueprint contains the definition for launching and
  configuring a set of services (Amazon SageMaker Studio) to publish and use
  Amazon SageMaker assets in the Amazon DataZone catalog.

For more information, see [Amazon DataZone terminology and concepts](datazone-concepts.md "datazone-concepts.md").

While creating an Amazon DataZone domain, you have the option to choose the **Quick
setup** which automatically enables the default data lake and the default
data warehouse built-in blueprints as part of the domain creation process.
**Quick setup** also creates default environment profiles and
default environments for you using these built-in blueprints.

If you don't choose **Quick setup** as part of creating your
Amazon DataZone domain, you can use the procedure below to enable the available built-in
blueprints in the AWS account that houses this Amazon DataZone domain. You must enable
these built-in blueprints before you can use them to create envrionment profiles and
environments in this domain.

To enable built-in blueprints in an Amazon DataZone domain via the Amazon DataZone management
console, you must assume an IAM role in the account with administrative permissions.
[Configure the IAM permissions required to use the
Amazon DataZone management console](create-iam-roles.md "create-iam-roles.md") to obtain the
minimum permissions.

###### Enable built-in blueprints in an Amazon DataZone

domain

1.  Navigate to the Amazon DataZone console at [https://console.aws.amazon.com/datazone](https://console.aws.amazon.com/datazone "https://console.aws.amazon.com/datazone") and sign in with your
    account credentials.
2.  Choose **View domains** and choose the domain where you want
    to enable one or more built-in blueprints.
3.  On the domain details page, navigate to the **Blueprints**
    tab.
4.  From the **Blueprints** list, choose either the
    **DefaultDataLake** or the
    **DefaultDataWarehouse**, or the **Amazon
    SageMaker** blueprint.
5.  On the chosen blueprint's details page, choose **Enable in this
    account**.
6.  On the Permissions and resources page, specify the following:
    - If you're enabling the **DefaultDataLake** blueprint,
      for **Glue Manage Access role**, specify a new or
      existing service role that grants Amazon DataZone authorization to ingest and
      manage access to tables in AWS Glue and AWS Lake Formation.
    - If you're enabling the **DefaultDataWarehouse**
      blueprint, for **Redshift Manage Access role**, specify
      a new or existing service role that grants Amazon DataZone authorization to
      ingest and manage access to datashares, tables and views in Amazon
      Redshift.
    - If you're enabling the **Amazon SageMaker**
      blueprint, for **SageMaker Manage Access role**,
      specify a new or existing service role that grants Amazon DataZone
      permissions to publish Amazon SageMaker data to the catalog. It also
      gives Amazon DataZone permissions to grant access or revoke access to Amazon
      SageMaker published assets in the catalog.

    ###### Important

    When you're enabling the **Amazon SageMaker**
    blueprint, Amazon DataZone checks whether the following IAM roles for
    Amazon DataZone exist in the current account and region. If these roles
    do not exist, Amazon DataZone automatically creates them.

        + AmazonDataZoneGlueAccess-<region>-<domainId>
        + AmazonDataZoneRedshiftAccess-<region>-<domainId>

    - For **Provisioning role**, specify a new or existing
      service role that grants Amazon DataZone authorization to create and
      configure environment resources using AWS CloudFormation in the
      environment account and region.
    - If you're enabling the **Amazon SageMaker**
      blueprint, for the **Amazon S3 bucket for SageMaker-Glue data
      source**, specify an Amazon S3 bucket that is to be used by
      all SageMaker environments in the AWS account. The bucket prefix that
      you specify must be one of the following:
      - amazon-datazone\*
      - datazone-sagemaker\*
      - sagemaker-datazone\*
      - DataZone-Sagemaker\*
      - Sagemaker-DataZone\*
      - DataZone-SageMaker\*
      - SageMaker-DataZone\*

7.  Choose **Enable blueprint**.

Once you enable the chosen blueprint(s), you can control which projects can use the
blueprint(s) in your account to create environment profiles. You can do this by
assigning managing projects to the blueprint’s configuration.

###### Important

By default, no managing projects are specified for for the environment blueprints,
which means that any Amazon DataZone user can create profiles for an environment
blueprint. Therefore, it is strongly recommended that you always specify managing
projects for your environment blueprints to ensure stronger governance.

###### Specify managing projects on enabled

blueprints

1. Navigate to the Amazon DataZone console at [https://console.aws.amazon.com/datazone](https://console.aws.amazon.com/datazone "https://console.aws.amazon.com/datazone") and sign in with your
   account credentials.
2. Choose **View Domains** and then choose the domain where you
   want to add the managing project(s) for the chosen blueprint(s).
3. Choose the **Blueprints** tab and then choose the blueprint
   that you want to work with.
4. By default, all projects within the domain can use the DefaultDataLake or
   DefaultDataWareshouse, or the Amazon SageMaker blueprints in the account to
   create environment profiles. However, you can restrict this by assigning
   managing projects to the blueprints. To add managing projects, choose
   **Select managing project**, then choose the projects that
   you want to add as managing projects from the drop down menu, and then choose
   **Select managing projects(s)**.

Once you enable the DefaultDataWarehouse blueprint in your AWS account, you can add
parameter sets to the blueprint configuration. A parameter set is a group of keys and
values, required for Amazon DataZone to establish a connection to your Amazon Redshift
cluster and is used to create data warehouse environments. These parameters include the
name of your Amazon Redshift cluster, database, and the AWS secret that holds
credentials to the cluster.

###### Adding parameter sets to the DefaultDataWarehouse blueprint

1. Navigate to the Amazon DataZone console at [https://console.aws.amazon.com/datazone](https://console.aws.amazon.com/datazone "https://console.aws.amazon.com/datazone") and sign in with your
   account credentials.
2. Choose **View domains** and then choose the domain where you
   want to add the parameter set.
3. Choose the **Blueprints** tab and then choose the
   DefaultDataWareshouse blueprint to open the blueprint details page.
4. Under the **Parameter sets** tab on the blueprint details
   page, choose **Create parameter set**.
   - Provide a Name for the parameter set.
   - Optionally, provide a description for the parameter set.
   - Select a region
   - Select either Amazon Redshift cluster or Amazon Redshift
     Serverless.
   - Select the AWS secret ARN that holds the credentials to the selected
     Amazon Redshift cluster or the Amazon Redshift Serverless workgroup. The
     AWS secret must be tagged with the `AmazonDataZoneDomain :
[Domain_ID]` tag in order to be eligible for use within a
     parameter set.
     - If you do not have an existing AWS secret, you can also
       create a new secret by choosing **Create New AWS
       Secret**. This opens a dialog box where you can
       provide the name of the secret, username, and password. Once you
       choose **Create New AWS Secret**, Amazon DataZone
       creates a new secret in the AWS Secrets Manager service and
       ensures that the secret is tagged with the domain in which you
       are trying to create the parameter set.

   - If you chose Amazon Redshift cluster in the step above, now choose a
     cluster from the dropdown. If you chose Amazon Redshift workgroup in the
     step above, now choose a workgroup from the drop down.
   - Enter the name of the database within the selected Amazon Redshift
     cluster or Amazon Redshift Serverless workgroup.
   - Choose **Create parameter set**.

###### Note

You can only add up to 10 parameter sets to the DefaultDataWarehouse
blueprint.

Once you enable the Amazon SageMaker blueprint in your AWS account, you can add
parameter sets to the blueprint configuration. A parameter set is a group of keys and
values, required for Amazon DataZone to establish a connection to your Amazon SageMaker and
is used to create sagemaker environments.

###### Adding parameter sets to the Amazon SageMaker blueprint

1. Navigate to the Amazon DataZone console at [https://console.aws.amazon.com/datazone](https://console.aws.amazon.com/datazone "https://console.aws.amazon.com/datazone") and sign in with your
   account credentials.
2. Choose **View domains** and then choose the domain that
   contains the enabled blueprint where you want to add the parameter set.
3. Choose the **Blueprints** tab and then choose the Amazon
   SageMaker blueprint to open the blueprint's details page.
4. Under the **Parameter sets** tab on the blueprint details
   page, choose **Create parameter set**, and then specify the
   following:
   - Provide a **Name** for the parameter set.
   - Optionally, provide a **Description** for the
     parameter set.
   - Specify the Amazon SageMaker domain authentication type. You can
     choose either IAM or IAM Identity Center (SSO).
   - Specify an AWS region.
   - Specify an AWS KMS key for data encryption. You can choose an
     existing key or create a new key.
   - Under **Environment parameters**, specify the
     following:
     - VPC ID - the ID that you're using for the VPC of the Amazon
       SageMaker environment. You can specify an existing or create a
       new VPC.
     - Subnets - one or more IDs for a range of IP addresses for
       specific resources within your VPC.
     - Network access - choose either **VPC only**
       or **Public internet only**.
     - Security group - the security group to use when configuring
       VPC and subnets.

   - Under Data source parameters, choose one of the following:
     - AWS Glue only
     - AWS Glue + Amazon Redshift Serverless. If you choose this
       option, specify the following:
       - Specify the AWS secret ARN that holds the
         credentials to the selected Amazon Redshift cluster. The
         AWS secret must be tagged with the
         `AmazonDataZoneDomain : [Domain_ID]` tag
         in order to be eligible for use within a parameter set.

       If you do not have an existing AWS secret, you can
       also create a new secret by choosing **Create
       New AWS Secret**. This opens a dialog box
       where you can provide the name of the secret, username,
       and password. Once you choose **Create New AWS
       Secret**, Amazon DataZone creates a new secret
       in the AWS Secrets Manager service and ensures that
       the secret is tagged with the domain in which you are
       trying to create the parameter set.
       - Specify the Amazon Redshift workgroup you want to use
         when creating environments.
       - Specify the name of the database (within the workgroup
         you've chosen) that you want to use when creating
         environments.

     - AWS Glue only + Amazon Redshift Cluster
       - Specify the AWS secret ARN that holds the
         credentials to the selected Amazon Redshift cluster. The
         AWS secret must be tagged with the
         `AmazonDataZoneDomain : [Domain_ID]` tag
         in order to be eligible for use within a parameter set.

       If you do not have an existing AWS secret, you can
       also create a new secret by choosing **Create
       New AWS Secret**. This opens a dialog box
       where you can provide the name of the secret, username,
       and password. Once you choose **Create New AWS
       Secret**, Amazon DataZone creates a new secret
       in the AWS Secrets Manager service and ensures that
       the secret is tagged with the domain in which you are
       trying to create the parameter set.
       - Specify the Amazon Redshift cluster you want to use
         when creating environments.
       - Specify the name of the database (within the cluster
         you've chosen) that you want to use when creating
         environments.

5. Choose **Create parameter set**.

## Add Amazon SageMaker as a trusted

service in the AWS account that owns the Amazon DataZone domain

If you've enabled the Amazon SageMaker blueprint, you must also add SageMaker as one
of the trusted services within Amazon DataZone. To do this, complete the following
procedure:

1. Navigate to the Amazon DataZone console at [https://console.aws.amazon.com/datazone](https://console.aws.amazon.com/datazone "https://console.aws.amazon.com/datazone") and sign in with your
   account credentials.
2. Choose **View domains** and then choose the domain that
   contains the enabled SageMaker blueprint.
3. Choose the **Trusted services**, then choose the
   **Amazon SageMaker**, and then choose
   **Enable**.
