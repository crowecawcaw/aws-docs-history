# Release notes for Amazon SageMaker Unified Studio

The following sections describe the feature releases for Amazon SageMaker Unified Studio.

## September 2025

### September 12, 2025

**Continuous real-time ingestion of metadata from AWS Glue Data Catalog to SageMaker Catalog**

We have launched a new capability within SageMaker Catalog that enables continuous real-time ingestion of metadata from AWS Glue Data Catalog to SageMaker Catalog. With this launch, once you onboard your tables and views in AWS Glue Data Catalog to SageMaker Catalog, SageMaker Catalog continuously keeps metadata current via real-time ingestion. Any changes, such as new tables or schema updates made in AWS Glue Data Catalog, are automatically reflected in the SageMaker Catalog. This eliminates the need for periodic ingestion jobs, reduces stale metadata risk, and lowers operational costs for you while ensuring access to the freshest metadata. For more information, see [Onboarding data in Amazon SageMaker Unified Studio](../adminguide/data-onboarding.md "../adminguide/data-onboarding.md").

## August 2025

### August 22, 2025

**Amazon SageMaker Unified Studio adds S3 file sharing options to projects
experience**

Amazon SageMaker Unified Studio now supports Trusted Identity Propagation (TIP) for SQL analytics use cases with Amazon Redshift and Amazon Athena. This feature enables administrators to grant permissions based on user attributes from their corporate identity center. Users can single-sign into databases with permissions based on their identity or group membership, while auditors can track access across Unified Studio query editor and services like Redshift, Athena, and Lake Formation. To implement, create or update your domain with TIP enabled in the project profile. TIP automatically enables for Amazon Athena workgroup, while Amazon Redshift requires creating a connection with IAM Identity Center connection type. For more information, see User Guide.For more information, see [What's New](https://aws.amazon.com/about-aws/whats-new/2025/08/amazon-sagemaker-unified-studio-s3-file-sharing-options/ "https://aws.amazon.com/about-aws/whats-new/2025/08/amazon-sagemaker-unified-studio-s3-file-sharing-options/") [User
Guide](storage.md "storage.md") and [Admin
Guide](../../../ssagemaker-unified-studio/latest/adminguide/smus-admin-storage-guide.md "../../../ssagemaker-unified-studio/latest/adminguide/smus-admin-storage-guide.md").

### August 7, 2025

**Amazon SageMaker Unified Studio Redshift Managed Workgroup
experience**

Amazon SageMaker Unified Studio launched Redshift Managed Workgroup, a collection of Amazon Redshift compute resources that AWS Glue manages. It becomes visible as a managed workgroup in Amazon Redshift when users register a serverless namespace to AWS Glue Data Catalog and create a Lake Formation catalog. All management of these workgroups must be done through the AWS Glue Data Catalog interface. This eliminates the need for dedicated Redshift compute resources when querying Lakehouse catalogs, reducing costs, preserving data continuity, and accelerating project setup time.

### August 5, 2025

**Project deletion progress
experience**

Users can now track project deletion progress through a visual interface, providing clear visibility and status updates until the process is complete, enhancing the project management experience.

## July 2025

### July 16, 2025

**Amazon SageMaker streamlines the S3 Tables workflow
experience**

This update simplifies table creation and management by eliminating the need to navigate
multiple AWS consoles. Users can now create tables, load data, and run queries directly within
Amazon SageMaker Unified Studio using either Query Editor or Jupyter Notebook. The update enables administrators to
configure analytics integration with Amazon S3 and create custom profiles, allowing project
owners to set up pre-configured catalogs and S3 Tables support more efficiently. For more
information, see [What's New](https://aws.amazon.com/about-aws/whats-new/2025/07/amazon-sagemaker-streamlines-s3-tables-workflow/ "https://aws.amazon.com/about-aws/whats-new/2025/07/amazon-sagemaker-streamlines-s3-tables-workflow/") and [User
Guide](s3-tables-integration.md "s3-tables-integration.md").

### July 15, 2025

**Automatic approval of subscription requests based on project
membership**

A subscription request is now automatically approved if the requester is already authorized
to approve it manually. Specifically, if they are a member of both the project that published
the asset and the project requesting access. To qualify for auto-approval, the requester must be
listed as an owner or contributor in the project where the asset was originally published. And
the requester must also be listed as an owner or contributor in the project making the
subscription request. For more information, see [User
Guide](s3-tables-integration.md "s3-tables-integration.md").

### July 16, 2025

**Data lineage enhancements**

Amazon SageMaker Unified Studio has now contributed a 'custom transport' to the OpenLineage community that allows
builders to download the transport along with OpenLineage plugins to augment and automate
lineage events captured from OpenLineage-enabled systems. With this, customers can automate
lineage capture and send these lineage events to the Amazon SageMaker unified domain, enhancing
data governance and traceability within their data workflows. Additionally lineage enhancements
include automated lineage events capture for additional data sources using AWS Glue crawlers,
improved its SQL lineage support for stored procedures and materialized views in Amazon
Redshift, and from tools such as vETL processes and notebooks (interactive executions and remote
workflows). For more information, see [What's New](https://aws.amazon.com/about-aws/whats-new/2025/06/amazon-sagemaker-custom-transport-openlineage-community-lineage-capabilities/ "https://aws.amazon.com/about-aws/whats-new/2025/06/amazon-sagemaker-custom-transport-openlineage-community-lineage-capabilities/") and [User
Guide](datazone-support-matrix.md "datazone-support-matrix.md").

### July 15, 2025

**Amazon QuickSight Integration**

Amazon QuickSight Integration is now available, enabling users to seamlessly build and
visualize dashboards using project data directly from Amazon SageMaker Unified Studio. The integration automatically
creates secured QuickSight datasets, organizes dashboards within project folders, and allows
publishing to the SageMaker Catalog for broader discovery and reuse. This keeps your dashboards
organized, discoverable, shareable, and governed, making cross-team collaboration and asset
reuse much easier. For more information, see [What's New](https://aws.amazon.com/about-aws/whats-new/2025/07/amazon-sagemaker-integration-quicksight/ "https://aws.amazon.com/about-aws/whats-new/2025/07/amazon-sagemaker-integration-quicksight/"), [User Guide](quicksight-integration.md "quicksight-integration.md"),
[Admin Guide](../adminguide/amazon-quicksight.md "../adminguide/amazon-quicksight.md"),
[AWS News Blog](https://aws.amazon.com/blogs/aws/streamline-the-path-from-data-to-insights-with-new-amazon-sagemaker-capabilities/ "https://aws.amazon.com/blogs/aws/streamline-the-path-from-data-to-insights-with-new-amazon-sagemaker-capabilities/"), and the [AWS Big Data Blog](https://aws.amazon.com/blogs/big-data/unifying-data-insights-with-amazon-quicksight-and-amazon-sagemaker/ "https://aws.amazon.com/blogs/big-data/unifying-data-insights-with-amazon-quicksight-and-amazon-sagemaker/").

### July 15, 2025

**Data management with automated Lakehouse onboarding and metadata
ingestion**

Data management is simplified with the introduction of two key capabilities in Amazon
SageMaker. First, automated metadata ingestion for datasets into SageMaker Catalog during domain
creation or updates, and direct sharing of assets between projects. The automated onboarding
eliminates manual IAM configuration and metadata ingestion tasks, making datasets immediately
available for governance and analysis. Second, direct sharing enables seamless cross-team
collaboration while maintaining governance controls, reducing administrative overhead and
accelerating project timelines. For more information, see [What's New](https://aws.amazon.com/about-aws/whats-new/2025/07/amazon-sagemaker-data-management-lakehouse-onboarding/ "https://aws.amazon.com/about-aws/whats-new/2025/07/amazon-sagemaker-data-management-lakehouse-onboarding/"), [Admin Guide](../adminguide/data-onboarding.md "../adminguide/data-onboarding.md"), and
[AWS News Blog](https://aws.amazon.com/blogs/aws/streamline-the-path-from-data-to-insights-with-new-amazon-sagemaker-capabilities/ "https://aws.amazon.com/blogs/aws/streamline-the-path-from-data-to-insights-with-new-amazon-sagemaker-capabilities/").

### July 15, 2025

**Amazon SageMaker Catalog adds support for Amazon S3 general purpose
buckets**

Amazon SageMaker Catalog now supports Amazon S3 general purpose buckets to enable data
producers to share unstructured data as "S3 Object Collections" within the SageMaker Catalog.
Users can curate these assets with business metadata, making them discoverable and accessible to
data scientists, engineers, and analysts while maintaining granular security controls. This
feature streamlines cross-team data sharing, enhances data governance, and allows consumers to
subscribe to assets for ongoing access and updates. For more information, see [What's New](https://aws.amazon.com/about-aws/whats-new/2025/07/amazon-sagemaker-catalog-s3-general-purpose-buckets/ "https://aws.amazon.com/about-aws/whats-new/2025/07/amazon-sagemaker-catalog-s3-general-purpose-buckets/") and [User Guide](data-s3-publish.md "data-s3-publish.md").

### July 15, 2025

**Unified Metadata Governance with SageMaker-Collibra
solution**

Unified Metadata Governance with SageMaker-Collibra solution addresses organizational
challenges by connecting Amazon SageMaker Catalog with Collibra, enabling centralized metadata
management and streamlined access workflows. This integration reduces metadata duplication,
enhances governance controls, and builds data trust across analytics and AI platforms. For more
information, see [AWS Big Data Blog](https://aws.amazon.com/blogs/big-data/unifying-metadata-governance-across-amazon-sagemaker-and-collibra/ "https://aws.amazon.com/blogs/big-data/unifying-metadata-governance-across-amazon-sagemaker-and-collibra/").

### July 15, 2025

**Visual Workflows**

Visual Workflows introduces a drag-and-drop interface for creating and managing workflows
within Amazon SageMaker Unified Studio. This low-code feature allows users to visually represent a series of tasks,
such as data processing and analysis, with the option to customize further by switching from
visual to code. Leveraging Amazon Managed Workflows for Apache Airflow (MWAA), it enables users
to create, modify, schedule, and monitor workflows easily. This addition simplifies workflow
management and enhances usability for data engineers and scientists. For more information, see
[What's New](https://aws.amazon.com/about-aws/whats-new/2025/07/amazon-sagemaker-visual-workflows-builder/ "https://aws.amazon.com/about-aws/whats-new/2025/07/amazon-sagemaker-visual-workflows-builder/"), [User Guide](workflow-orchestration.md "workflow-orchestration.md"),
and [Blog Post](https://aws.amazon.com/blogs/big-data/orchestrate-data-processing-jobs-querybooks-and-notebooks-using-visual-workflow-experience-in-amazon-sagemaker/ "https://aws.amazon.com/blogs/big-data/orchestrate-data-processing-jobs-querybooks-and-notebooks-using-visual-workflow-experience-in-amazon-sagemaker/").

### July 15, 2025

**Data processing jobs experience**

A new data processing jobs experience is available within Amazon SageMaker Unified Studio. Jobs enables users to
author, manage, monitor and troubleshoot data processing workloads across their organization and
collaborate in projects to securely build and share data processing jobs and workflows. Users
can create jobs through multiple methods including ETL scripts, interactive notebooks, or the
Visual ETL editor, with options for on-demand execution, scheduling, or workflow orchestration.
The feature includes monitoring capabilities and AI-powered troubleshooting for failed jobs. For
more information, see [What's New](https://aws.amazon.com/about-aws/whats-new/2025/07/amazon-sagemaker-data-processing-jobs/ "https://aws.amazon.com/about-aws/whats-new/2025/07/amazon-sagemaker-data-processing-jobs/"), [User
Guide](sagemaker-unified-studio-jobs.md "sagemaker-unified-studio-jobs.md"), and [Blog
Post](https://aws.amazon.com/blogs/big-data/introducing-jobs-in-amazon-sagemaker/ "https://aws.amazon.com/blogs/big-data/introducing-jobs-in-amazon-sagemaker/").

### July 3, 2025

**Enhanced Data Explorer object actions**

Data Explorer is being enhanced with user-friendly actions that streamline database
operations, including a UI-based table definition creator, auto-generation of common SQL
queries, a quick actions menu, and direct object manipulation capabilities. These features
reduce the need for manual query writing and boost overall productivity.

### July 3, 2025

**Bring S3 buckets to your project**

To bring in Amazon S3 data either in the same account or a different account to your
project, you must first gain access to the data and then add the data to your project. You can
gain access to the data by using the project role or an access role. Then you have to create a
S3 connection using the Add Data option from data explorer. For more information, see [User
Guide](adding-existing-s3-data.md "adding-existing-s3-data.md").

### July 3, 2025

**Uploading data from your desktop to create a Redshift
table**

You can now upload data from your desktop in CSV, JSON, Parquet, or Delimiter formats to
create either a data lake or Amazon Redshift table using Amazon SageMaker Unified Studio. You can select Add data
option from the data explorer and then select create table. For more information, see [User
Guide](getting-started-sagemaker-gdc-s3.md "getting-started-sagemaker-gdc-s3.md").

### July 25, 2025

**Text search capability of Query history
experience**

Amazon SageMaker Unified Studio introduces text search capability for query history in both Athena and Redshift engines. This enhancement enables users to efficiently search through their historical queries, improving workflow productivity and query reusability. For more information, see User Guide.

### July 23, 2025

**Trusted identity propagation
experience**

Amazon SageMaker Unified Studio now supports Trusted Identity Propagation (TIP) for SQL analytics use cases with Amazon Redshift and Amazon Athena. This feature enables administrators to grant permissions based on user attributes from their corporate identity center. Users can single-sign into databases with permissions based on their identity or group membership, while auditors can track access across Unified Studio query editor and services like Redshift, Athena, and Lake Formation. To implement, create or update your domain with TIP enabled in the project profile. TIP automatically enables for Amazon Athena workgroup, while Amazon Redshift requires creating a connection with IAM Identity Center connection type. For more information, see User Guide.For more information, see [User
Guide](using-project-tip.md "using-project-tip.md") and [Admin
Guide](../adminguide/trusted-identity-propagation.md "../adminguide/trusted-identity-propagation.md").

### July 2, 2025

**Support of SQL generation actions in Data Explorer
experience**

Amazon SageMaker Unified Studio now supports SQL generation actions in Data Explorer, introducing automated generation of table definitions and common SQL queries (INSERT/UPDATE/SELECT/DROP). The feature includes a quick actions menu for frequently used operations and direct object manipulation capabilities. These enhancements significantly reduce manual query writing effort and improve overall productivity for data analysts and scientists.

## June 2025 (Additional)

### June 30, 2025

**Next Generation Amazon SageMaker user guide**

Next Generation Amazon SageMaker user guide was launched on 6/30 and it introduces the main
components of Next Generation Amazon SageMaker and includes 7 new use case-based tutorials to
help customers get started. For more information, see [Next Generation Amazon
SageMaker user guide](../../../next-generation-sagemaker/latest/userguide/what-is-sagemaker.md "../../../next-generation-sagemaker/latest/userguide/what-is-sagemaker.md").

### June 25, 2025

**Automatic file synchronization between project Git repositories and
Amazon S3 buckets**

Amazon SageMaker Unified Studio now offers automatic file synchronization between project Git repositories and
Amazon S3 buckets. This new capability streamlines data and AI development workflows by ensuring
your Git repository files are automatically mirrored to S3. For more information, see [What's New](https://aws.amazon.com/about-aws/whats-new/2025/06/amazon-sagemaker-automatic-synchronization-git-s3/ "https://aws.amazon.com/about-aws/whats-new/2025/06/amazon-sagemaker-automatic-synchronization-git-s3/"), [Admin
Guide](../adminguide/blueprints.md#manage-tooling-blueprint "../adminguide/blueprints.md#manage-tooling-blueprint"), and [AWS Big Data Blog](https://aws.amazon.com/blogs/big-data/unified-scheduling-for-visual-etl-flows-and-query-books-in-amazon-sagemaker-unified-studio/ "https://aws.amazon.com/blogs/big-data/unified-scheduling-for-visual-etl-flows-and-query-books-in-amazon-sagemaker-unified-studio/").

## June 2025

### June 12, 2025

**Workflow Improvements**

Enhanced default workflow template: The default start_date now uses a static date instead
of a relative date. This prevents potential workflow trigger failures, improves workflow
reliability and predictability.

Notebook output capabilities: Download notebook output directly, export results for offline
analysis and share findings more easily with your team.

### June 19, 2025

**Auto complete support for large number of tables and columns
experience**

Amazon SageMaker Unified Studio now delivers enhanced autocomplete capabilities for enterprise-scale Amazon Redshift databases. The feature supports seamless autocomplete functionality for massive databases containing up to 200,000 tables, while eliminating previous restrictions on the number of schemas or columns that can be indexed and suggested. Using real-time database metadata, it provides comprehensive coverage across your entire Redshift environment, including both user-defined native tables and critical system tables. This enables data analysts, engineers, and scientists working with complex, large-scale data warehouses to navigate their database structures effortlessly, dramatically reducing query development time and minimizing syntax errors.

### June 5, 2025

**CloudFormation template**

Amazon SageMaker Unified Studio now provides an [CloudFormation
template](https://github.com/aws/Unified-Studio-for-Amazon-Sagemaker/tree/main/cloudformation "https://github.com/aws/Unified-Studio-for-Amazon-Sagemaker/tree/main/cloudformation") to setup and create a new Amazon SageMaker Unified domain and project.

### June 2, 2025

**Amazon DataZone and Amazon SageMaker integration**

Amazon DataZone and Amazon SageMaker introduced a new UI feature that enables DataZone
domains to be upgraded and utilized within the next generation of Amazon SageMaker. This update
preserves customers' Amazon DataZone investments when transferring to Amazon SageMaker. The
integration allows all content and assets created in DataZone, including metadata forms,
glossaries, and subscriptions, to remain accessible through Amazon SageMaker Unified Studio post-upgrade. This upgrade
pathway demonstrates Amazon's commitment to providing continuity and value preservation for
customers using their machine learning and data management services. For more information, see
[What's New](https://aws.amazon.com/about-aws/whats-new/2025/06/amazon-datazone-upgrade-domain-sagemaker/ "https://aws.amazon.com/about-aws/whats-new/2025/06/amazon-datazone-upgrade-domain-sagemaker/") and [Upgrade Amazon DataZone domains to
Amazon SageMaker unified domains](../../../datazone/latest/userguide/upgrade-domain.md "../../../datazone/latest/userguide/upgrade-domain.md").

## May 2025

### May 30, 2025

**Increased concurrent spaces support**

Amazon SageMaker Unified Studio now supports up to 6,000 concurrent spaces per customer account, representing a
2.4x increase from the previous limit. This significant scaling improvement enables
organizations to support larger teams and more concurrent workloads within their Amazon SageMaker Unified Studio
environment.

### May 30, 2025

**Visual ETL improvements**

Amazon SageMaker Unified Studio visual ETL now supports cloning a visual ETL flow as a Jupyter notebook, allowing
users to continue editing the flow with code. This streamlines the workflow for users who prefer
to start authoring ETL pipelines visually and then transition to a code-based approach. Visual
ETL also added support for automatically inferring schemas from CSV files within S3 nodes,
improving the authoring process and reducing manual work needed.

### May 29, 2025

**Native Redshift table creation enhancements**

You can now create native Redshift tables directly through local file uploads, supporting
multiple file formats (CSV, JSON, PARQUET) with various compression options and increased file
size limit to 100MB. The enhancement includes automatic schema inference with preview
capabilities and adds PARQUET support in Glue upload flow. This eliminates the previous
multi-step process that required manual S3 file copying, table creation, and data insertion,
making the workflow more efficient and less error-prone.

### May 23, 2025

**Customer Managed Custom Master (CM-CMK) support for Persistent App
UI**

Customer Managed Custom Master (CM-CMK) support for Persistent App UI, an essential tool
for debugging big data applications. This feature extends SSE encryption applied to logs managed
in the EMR service bucket to honor Customer Managed Custom Master Key (CM-CMK). This feature
enables customers to manage accessibility of logs after their clusters terminate. For more
information, see [About Amazon EMR
Releases](../../../emr/latest/ReleaseGuide/emr-790-release.md#emr-790-relnotes "../../../emr/latest/ReleaseGuide/emr-790-release.md#emr-790-relnotes") and [Configure Amazon EMR cluster logging and debugging](../../../emr/latest/ManagementGuide/emr-plan-debugging.md#emr-plan-debugging-logs-archive "../../../emr/latest/ManagementGuide/emr-plan-debugging.md#emr-plan-debugging-logs-archive").

### May 22, 2025

**Global Search Bar**

Amazon SageMaker Unified Studio introduced a new Global Search Bar, providing a persistent search interface in
the top navigation and landing page, simplifying discover and access data without navigating
through multiple menus. The intuitive search functionality currently supports business catalog
data and projects, offering clear visual indicators for search result scope. This user-centric
enhancement represents AWS's commitment to improving the overall SageMaker Studio experience,
making data and resources more accessible to users.

### May 12, 2025

**Code Editor and Multiple Spaces support**

AWS launched two complementary capabilities in the next generation of Amazon SageMaker
that enhance the development experience for analytics, machine learning (ML), and GenAI teams:
Code Editor and Multiple Spaces support. The Code Editor, based on Code-OSS (Open Source Software) like VS Code, offers a powerful
IDE experience with familiar shortcuts, terminal access, and advanced development tools, while
supporting thousands of VS Code-compatible extensions from Open VSX. It enables seamless version
control through major Git platforms and comes preconfigured with Amazon SageMaker distribution
for ML frameworks. To maximize the benefits of Code Editor alongside other coding interfaces in
Unified Studio, including JupyterLab, SageMaker now supports multiple spaces per user per
project, allowing users to manage parallel workstreams with different computational needs. For
more information, see [What's New](https://aws.amazon.com/about-aws/whats-new/2025/05/code-editor-vs-code-open-source-sagemaker-unified-studio/ "https://aws.amazon.com/about-aws/whats-new/2025/05/code-editor-vs-code-open-source-sagemaker-unified-studio/") and [Using the Code Editor IDE in
Amazon SageMaker Unified Studio](code-editor.md "code-editor.md").

### May 12, 2025

**Bring Your Own Image (BYOI)**

Amazon SageMaker Unified Studio now allows you to bring your own image (BYOI). This feature benefits customers
who have regulatory and compliance requirements or who prefer not to use the framework
containers that come with the default SageMaker Distribution image. For more information, see
[What's New](https://aws.amazon.com/about-aws/whats-new/2025/05/amazon-sagemaker-unified-studio-byoi/ "https://aws.amazon.com/about-aws/whats-new/2025/05/amazon-sagemaker-unified-studio-byoi/") and [Bring your own image
(BYOI)](byoi.md "byoi.md").
