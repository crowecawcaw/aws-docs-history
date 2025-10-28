# SQL analytics project profile

The SQL analytics project profiles enables your users to query Amazon SageMaker Lakehouse,
Amazon Redshift and Amazon Athena data in their Amazon SageMaker Unified Studio projects. Amazon SageMaker Unified Studio project members
can analyze their data in Amazon SageMaker Lakehouse using SQL.

You can complete the following procedures to create a SQL analytics project profile for
your Amazon SageMaker unified domain.

###### Topics

- [Configure SQL analytics for your Amazon SageMaker
  unified domain](#configure-sql-analytics "#configure-sql-analytics")
- [Create a SQL analytics project
  profile](#create-sql-analytics-project-profile "#create-sql-analytics-project-profile")

## Configure SQL analytics for your Amazon SageMaker

unified domain

Complete the following procedure to configure SQL analytics capability for your Amazon
SageMaker unified domain.

1. Navigate to the Amazon SageMaker management console at [https://console.aws.amazon.com/datazone](https://console.aws.amazon.com/datazone "https://console.aws.amazon.com/datazone") and use the region selector in the
   top navigation bar to choose the appropriate AWS Region.
2. Either create a new domain or choose an existing domain where you want to configure
   SQL analytics.
3. On the domain's details page, under the **Next steps for your
   domain** section, choose the **Configure** button next to
   the **SQL** capability.
4. On the **Create project profile - SQL analytics** page, in the
   **SQL analytics** section, review the capabilities, tools, and
   functionalities that are enabled for this project profile.
5. On the **Create project profile: SQL analytics**, expand the
   **Default tooling blueprint deployment settings** section and review
   the settings, including the Tooling blueprint deployment account and region.

###### Important

Note that by configuring the SQL analytics capability for your domain (this
procedure), you can only enable the Tooling blueprint in the same AWS account and
region as your domain. To enable the Tooling blueprint in an account or region that's
different from that of your domain's, see [Create a SQL analytics project
profile](#create-sql-analytics-project-profile "#create-sql-analytics-project-profile") or [Custom project profile](custom.md "custom.md"). 6. On the **Create project profile: SQL analytics** page, in the
**Enable blueprints** section, review the following blueprints that
will be enabled for this project profile.

###### Important

Note that by configuring SQL analytics for your domain (this procedure), you can
only enable these blueprints in the same AWS account and region as your domain. To
enable these blueprints in an account or region that's different from that of your
domain's, see [Create a SQL analytics project
profile](#create-sql-analytics-project-profile "#create-sql-analytics-project-profile") and [Custom project profile](custom.md "custom.md").

    * LakehouseCatalog
    * RedshiftServerless
    * DataLake

7. On the **Create project profile: SQL analytics** page, in the
   **Manage access role** section, specify a service role that gives
   Amazon SageMaker Unified Studio authorization to ingest and manage access to datashares, tables and views in
   Amazon Redshift. You can create a new or using an existing role.
8. On the **Create project profil: SQL analytics** page, in the
   **Provisioning role** section, specify a service role that gives
   Amazon SageMaker Unified Studio authorization to ingest and manage access to datashares, tables and views in
   Amazon Redshift.
9. On the **Create project profile: SQL analytics** page, in the
   **Amazon S3 bucket for blueprints** section, specify an Amazon S3
   bucket for blueprints in your AWS account.
10. On the **Create project profile: SQL analytics** page, in the
    **Networking** section, specify a VPC in which to provision your
    Amazon SageMaker unified domain. VPCs tagged with Amazon SageMaker Unified Studio should
    be correctly configured. In the **Subnets** section, select at least 3
    subnets in different **Availability Zones** that contain required VPC
    Endpoints. Private subnets are recommended, not all functionality is available when
    selecting public subnets.
11. In the **Data encryption** section, specify the encryption
    settings. Your data is encrypted by default with a key that AWS owns and manages for
    you. To choose a different key, customize your encryption settings.
12. In the **User role policy** section, you have the option to specify
    your own user role policy. Amazon SageMaker Unified Studio creates IAM roles for project users to perform data
    analytics, AI, and ML actions. You can attach your own AWS IAM policies to the role
    rather than using the default system-managed policy. This provides more granular control
    over permissions but requires knowledge of IAM policy configuration. The IAM policy must
    include all necessary permissions required for the service to function properly.
13. On the **Create project profile: SQL analytics** page, in the
    **Authorization - optional** section, specify who can use this
    project profile to create projects in all domain units. This can also be done per domain
    unit in the Amazon SageMaker Unified Studio. Choose either **Selected users and groups**
    (select which users and groups are authorized to use this project profile) or
    **Allow all users and groups** (allow any user to use this project
    profile).

###### Note

Projects do not provide strong security isolation. To limit cross-domain and
cross-project resource discovery you can consider creating projects in separate
accounts. 14. Choose **Create project profile**.

## Create a SQL analytics project

profile

Complete the following procedure to create a SQL analytics project profile for your
Amazon SageMaker unified domain. Once this procedure is complete, your SQL analytics project
profile will only include the capabilities defined in the [Tooling
blueprint](blueprints.md "blueprints.md"). To configure the full data analytics and SQL analytics capability for
your Amazon SageMaker unified domain, you must then use the **Blueprints**
tab and configure the following blueprints for this project profile:

- LakehouseCatalog
- RedshiftServerless
- DataLake

###### Important

Note that when you enable a blueprint, by default, you are enabling it in the same
region as your domain. When you are enabling blueprints for a project profile that is
created and enabled in a different region from your domain, you must enable these
blueprints in same region where this project profile is enabled (in addition to enabling
this blueprint in the same region as your domain). You can do this via the
**Regions** tab in the blueprint details page. This applies to all
blueprints, including the Tooling blueprint.

1. Navigate to the Amazon SageMaker management console at [https://console.aws.amazon.com/datazone](https://console.aws.amazon.com/datazone "https://console.aws.amazon.com/datazone") and use the region selector in the
   top navigation bar to choose the appropriate AWS Region.
2. Either create a new domain or choose an existing domain where you want to create a
   SQL analytics project profile.
3. On the domain's details page, choose the **Project profiles** tab
   and then choose **Create**.
4. On the **Create project profile** page, in the **Project
   profile name and description** section, specify the name of the project
   profile and the description.
5. On the **Create project profile** page, in the **Project
   profile creation options** section, choose **Create from a
   template**, and then under **Project profile templates**,
   choose **SQL analytics**.
6. On the **Create project profile** page, in the **Default
   tooling blueprint deployment settings** section, review the selections for
   the default deployment settings for the Tooling blueprint and update them as needed.
   1. On the **Create project profile** page, in the
      **Project files storage** section, choose a storage configuration
      type from Amazon S3 - new and Git repository. For more information on storage types,
      see [.\_unified-storage.xml](._unified-storage.md "._unified-storage.md")###### Important

Note that by creating this project profile from a template, you can either enable
the Tooling blueprint in the same AWS account and region as your domain
(prepopulated by default) or you can enable the Tooling blueprint in a different AWS
account and region from this domain (an associated account). 7. On the **Create project profile** page, in the
**Authorization - optional** section, specify who can use this
project profile to create projects in all domain units. This can also be done per domain
unit in Amazon SageMaker Unified Studio. You can specify **Selected users and groups** or
**Allow all users and groups** options.

###### Note

Projects do not provide strong security isolation. To limit cross-domain and
cross-project resource discovery you can consider creating projects in separate
accounts. 8. On the **Create project profile** page, in the **Project
profile readiness** section, specify whether you want to enable this project
profile on creation. Unless you check the **Enable project profile on
creation** checkbox, your project profile is disabled and not available to
use for Amazon SageMaker Unified Studio projects after its creation. Leaving a project profile in a disabled
state upon creation gives you the opportunity to customize your blueprints before making
the project profile available. 9. Choose **Create project profile**.

###### Important

After you complete this procedure, your SQL project profile will only include the
capabilities defined in the [Tooling blueprint](blueprints.md "blueprints.md"). You can
further customize this project profile and configure it to include the full supported SQL
analytics capability by using the **Bluerpints** tab to enable the rest
of its required bluerpints. They are the following:

- LakehouseCatalog
- RedshiftServerless
- DataLake
