# What is new in Amazon DataZone?

This section describes new features and improvements in Amazon DataZone by release date.

###### Topics

- [2024](#2024 "#2024")
- [2023](#2023 "#2023")

## 2024

### Amazon DataZone launches metadata enforcement rules for subscription requests

Released on 11/20/2024

The new metadata enforcement rules for subscription requests in Amazon DataZone strengthens data
governance by enabling domain unit owners to establish clear metadata requirements for data
consumers, streamlining access requests and enhancing data governance. This feature enables
organizations to align with organization’s metadata standards, implement custom workflows, and
provide a consistent, governed data access experience. For more information,
see [Metadata enforcement rules for subscription
requests](metadata-rules.md "metadata-rules.md").

### Amazon DataZone custom AWS service blueprints now enable

Amazon SageMaker with a new set up experience for Amazon DataZone
projects

Released on 11/15/2024

With Amazon DataZone custom AWS service prints, you can migrate your existing Amazon
SageMaker domain into Amazon DataZone. With this capability, administrators can now
set up Amazon DataZone projects by importing their existing authorized users, security
configurations, and policies from Amazon SageMaker domains. For more information,
see [Set
up SageMaker Assets (administrator guide)](../../../sagemaker/latest/dg/sm-assets-set-up.md "../../../sagemaker/latest/dg/sm-assets-set-up.md").

### Amazon DataZone launches AWS CloudFormation support for

custom AWS service blueprints

Released on 9/12/2024

Amazon DataZone added AWS CloudFormation support for the custom AWS service
blueprints. This new capability enables you to use AWS CloudFormation to automate
environment creation in Amazon DataZone. With custom blueprints, administrators can now
seamlessly integrate Amazon DataZone into their existing data pipelines using existing
IAM roles to publish data assets to the Amazon DataZone catalog, facilitating governed
sharing of those assets and enhancing governance across the entire infrastructure.
For more information, see [Amazon DataZone resource type reference](../../../AWSCloudFormation/latest/UserGuide/AWS_DataZone.md "../../../AWSCloudFormation/latest/UserGuide/AWS_DataZone.md").

### Amazon DataZone launches domain units and authorization

policies

Released on 08/12/2024

Amazon DataZone introduces a set of new data governance capabilities called domain
units and authorization policies that enable customers to create business unit/team
level organization and manage policies per their business needs. With the addition
of domain units, users can organize, create, search, and find data assets and
projects associated with business units or teams. With authorization policies, those
domain unit users can set access policies for creating projects, glossaries, and
using compute resources within Amazon DataZone. For more information, see [Domain units and authorization policies in
Amazon DataZone](working-with-domain-units.md "working-with-domain-units.md").

### Amazon DataZone launches data products

Released on 08/05/2024

Amazon DataZone introduces data products, which enable the grouping of data assets into
well-defined, self-contained packages tailored for specific business use cases. For
example, a marketing analysis data product can bundle various data assets, such as
marketing campaign data, pipeline data, and customer data. With data products,
customers can simplify discovery and subscription processes, aligning them with
business objectives and reducing redundancy in handling individual assets. For more
information , see [Amazon DataZone data products](working-with-data-products.md "working-with-data-products.md") .

### Amazon DataZone launches fine-grained access control

functionality

Released on 07/02/2024

Amazon DataZone has introduced fine-grained access control, providing you with granular
control over your data assets in Amazon DataZone's business data catalog across data
lakes and data warehouses. With the new capability, data owners can now restrict
access to specific records of data at row and column levels, instead of granting
access to entire data assets. For example, if your data contains columns with
sensitive information such as Personally Identifiable Information (PII), you can
restrict access to only the necessary columns, ensuring that sensitive information
is protected while still allowing access to non-sensitive data. Similarly, you can
control access at the row level, allowing users to see only the records that are
relevant to their role or task. For more information, see [Fine-grained access control to data in
Amazon DataZone](fine-grained-access-control.md "fine-grained-access-control.md")

### Amazon DataZone launches data lineage functionality

Released on 06/27/2024

Amazon DataZone launches data lineage in preview, helping customers visualize lineage
events from OpenLineage-enabled systems or through API and trace data movement from
source to consumption. Using Amazon DataZone’s OpenLineage-compatible APIs, domain
administrators and data producers can capture and store lineage events beyond what
is available in Amazon DataZone, including transformations in Amazon S3, AWS Glue, and
other services. Additionally, Amazon DataZone versions lineage with each event, enabling
users to visualize lineage at any point in time or compare transformations across an
asset’s or job’s history. This historical lineage provides a deeper understanding of
how data has evolved, essential for troubleshooting, auditing, and validating the
integrity of data assets. For more information, see [Data lineage in Amazon DataZone](datazone-data-lineage.md "datazone-data-lineage.md")

### Amazon DataZone launches custom AWS service

blueprints

Released on 06/17/2024

With custom AWS service blueprints, if you have existing AWS resources
including IAM roles, data lakes, data meshes, Amazon S3 buckets, and Amazon Redshift
clusters, you are now able to specify permissions to these existing resources using
your own custom IAM role, so that your Amazon DataZone users can leverage publication and
subscription to share and govern these resources. With custom AWS service
blueprints, Amazon DataZone administrators can configure AWS service environments using
their own custom roles. They can configure actions links for these AWS service
environments and thus provide federated access to any of their existing AWS
resources. They can also configure subscription targets and data sources in these
custom AWS service environments. Administrators can set up AWS service
environments in their own Amazon DataZone domain account or in any associated accounts
from which they want to publish, subscribe to, discover, or govern data. For more
information, see [Amazon DataZone custom AWS service blueprints](working-with-custom-blueprint.md "working-with-custom-blueprint.md") .

### Enhancements to the data source creation flow

Released on 06/10/2024

Amazon DataZone has added enhancements to the data source creation flow to simplify
access management for data producers. With these updates, when a data producer
creates a data source for publishing their AWS Glue and Amazon Redshift assets,
Amazon DataZone grants read-only permissions to the project members. When creating an
AWS Glue data source, Amazon DataZone automatically grants 'read-only' permissions to
the IAM role of the environment used to create the data source, allowing access to
all tables in the associated AWS Glue databases. Similarly, for Amazon Redshift
data sources, Amazon DataZone grants 'read-only' access to all tables in the Amazon
Redshift schemas used in the data source. For more information, see [Create and run an Amazon DataZone data source for
the AWS Glue Data Catalog](create-glue-data-source.md "create-glue-data-source.md") and
[Create and run an Amazon DataZone data source
for Amazon Redshift](create-redshift-data-source.md "create-redshift-data-source.md").

### Amazon DataZone launches integration with Amazon SageMaker

Released on 05/06/2024

Amazon DataZone launches integration with [Amazon SageMaker](https://aws.amazon.com/sagemaker/ "https://aws.amazon.com/sagemaker/") to help data
producers and consumers to seamlessly switch to Amazon SageMaker to collaborate on
machine learning (ML) projects while enforcing access governance to data and ML
assets. With the new built-in integration between Amazon DataZone and Amazon SageMaker,
data consumers and producers can streamline ML governance across infrastructure
setup, collaborate on business initiatives, and easily govern data and ML assets.
For more information, see [Amazon DataZone built-in blueprints](working-with-blueprints.md "working-with-blueprints.md") and [Associated accounts in Amazon DataZone](working-with-associated-accounts.md "working-with-associated-accounts.md").

### Amazon DataZone launches integration with AWS Lake Formation

hybrid access mode

Released on 04/03/2024

Amazon DataZone has introduced an integration with AWS Lake Formation hybrid access
mode. This integration enables you to easily publish and share your AWS Glue
tables through Amazon DataZone, without the need to register them in AWS Lake Formation
first. To get started, administrators enable the data location registration setting
under the `DefaultDataLake` blueprint in the Amazon DataZone console. Then,
when a data consumer subscribes to an AWS Glue table managed through IAM
permissions, Amazon DataZone first registers the Amazon S3 locations of this table in
hybrid mode, and then grants access to the data consumer by managing permissions on
the table through AWS Lake Formation. This ensures that IAM permissions on the
table continue to exist with newly-granted AWS Lake Formation permissions, without
disrupting any existing workflows. For more information, see the [Amazon DataZone integration with AWS Lake Formation
hybrid mode](hybrid-mode.md "hybrid-mode.md") .

### Amazon DataZone launches integration with AWS Glue Data

Quality

Released on 04/03/2024

Amazon DataZone launches integration with AWS Glue Data Quality and offers APIs to
integrate data quality metrics from third-party data quality solutions. The new
integration enables you to auto-publish AWS Glue Data Quality scores into the
Amazon DataZone business data catalog. Amazon DataZone APIs can be used to ingest quality
metrics from third-party sources. Once published, data consumers can easily search
for data assets, view granular quality metrics, and identify failed checks and rules

- empowering business decisions. For more information, see the [Data quality in Amazon DataZone](datazone-data-quality.md "datazone-data-quality.md").

### General availability release of AI recommendations for

descriptions in Amazon DataZone

Released on 03/27/2024

Amazon DataZone announced the general availability release of the new generative
AI-based capability to improve data discovery, data understanding and data usage by
enriching the business data catalog. With a single click, data producers can
generate comprehensive business data descriptions and context, highlight impactful
columns, and include recommendations on analytical use cases. The launch adds
support for APIs that data producers can use to programmatically generate
descriptions for assets. For more information, see [Using machine learning and generative AI in Amazon DataZone](autodoc.md "autodoc.md").

### Amazon DataZone launches enhancements to Amazon Redshift

integration

Released on 03/21/2024

Amazon DataZone has introduced several enhancements to its Amazon Redshift integration,
simplifying the process of publishing and subscribing to Amazon Redshift tables and
views. These updates streamline the experience for both data producers and
consumers, allowing them to quickly create data warehouse environments using
pre-configured credentials and connection parameters provided by their Amazon DataZone
administrators. Additionally, these enhancements grant administrators greater
control over who can use the resources within their AWS accounts and Amazon
Redshift clusters, and for what purpose.

- **Blueprint configuration**: once you enable
  the `DefaultDataWarehouseBlueprint` blueprint, you can control
  which projects can use the `DefaultDataWarehouseBlueprint`
  blueprint in your account to create environment profiles by assigning
  managing projects to the enabled blueprint. You can also create parameter
  sets on top of `DefaultDataWarehouseBlueprint` by providing
  parameters such as cluster, database, and an AWS Secret. You can also
  create AWS Secrets from within the Amazon DataZone console.
- **Environment profile**: when creating an
  environment profile, you can choose to provide your own Amazon Redshift
  parameters or use one of the parameter sets from the blueprint
  configuration. If you choose to use the parameter set created in the
  blueprint configuration, the AWS secret only requires
  `AmazonDataZoneDomain` tag
  (`AmazonDataZoneProject` tag is only required if you choose
  to provide your own parameter sets in the environment profile). In the
  environment profile, you can specify a list of authorized projects. Only
  authorized projects can use this environment profile to create data
  warehouse environments. You can also specify what data authorized projects
  are allowed to publish. Currently you can choose one of the following
  options: 1) Publish from any schema, 2) Publish from the default environment
  schema, 3) Don't allow publishing.
- **Environment**: Data producers or consumers
  can now select an environment profile to create environments, without the
  need to provide their own Amazon Redshift parameters including AWS Secret,
  cluster, workgroup, and database. These parameters are ported over to the
  environment from the environment profile. Along with the environment
  creation, Amazon DataZone now also creates default schema for the environment.
  Members of the project have read and write access to this schema and can
  easily publish any tables created in this schema to the catalog by running
  the default data source created as part of environment creation. Amazon
  Redshift parameters used to create environment can also be used for creating
  new data sources (instead of data producer to provide their own parameters
  in the data source creation).

### AWS Cloud Formation Support for Amazon DataZone

Released on 01/18/2024

Users of Amazon DataZone can now leverage AWS CloudFormation to effectively model and
manage a suite of Amazon DataZone resources. This approach facilitates consistent
provisioning of resources, while also enabling lifecycle management through
infrastructure as code practices. With custom templates, you can precisely define
your required resources and their interdependencies. For more information, see the
[Amazon DataZone resource type reference](../../../AWSCloudFormation/latest/UserGuide/AWS_DataZone.md "../../../AWSCloudFormation/latest/UserGuide/AWS_DataZone.md").

### Add IAM principals directly as members of Amazon DataZone

projects

Released on 01/05/2024

You can now add IAM principals as project members, even if those IAM principals
have not yet logged into Amazon DataZone (previous requirement). After a domain
administrator or IT administrator adds `iam:GetUser` and
`iam:GetRole` to the domain’s domain execution role, project owners
can add IAM principals as members simply by providing the Amazon Resouce Name (ARN)
of the IAM role or IAM user. The IAM principal still must have the IAM permissions
required to access Amazon DataZone and those can be configured in the IAM console. For
more information, see [Add members to a project](add-members-to-project.md "add-members-to-project.md").

### Support for custom asset types from the Data

Portal

Released on 01/05/2024

The support for custom assets enables Amazon DataZone to catalog assets via the Data
Portal for unstructured data, including dashboards, queries, and models, making it
easier for you to add custom assets directly in the data portal along with the
previously available API support. The ability to create, update and publish custom
assets in Amazon DataZone, enables you to share, find, subscribe to any type of asset and
build a business workflow that provides governance of those assets. For more
information, see [Create custom asset types in Amazon DataZone](create-asset-types.md "create-asset-types.md").

## 2023

### Delete domain

Released on 12/27/2023

This is a feature that enables you to more easily delete your domains. Now, you
can proceed with domain deletion even if it's not empty (as in contains projects,
environments, assets, data sources, etc.). For more information, see [Delete Amazon DataZone domains](delete-domain.md "delete-domain.md").

### Hybrid mode

Released on 12/22/2023

Amazon DataZone has added support for the AWS Lake Formation hybrid mode. With this
support, if you publish an AWS Glue table to Amazon DataZone with its AWS S3 location
registered in Lake Formation under hybrid mode, Amazon DataZone treats this table as a
managed assets and can manage the subscription grants to this table. Prior to this
feature release, Amazon DataZone would treat this table as an unmanaged asset i.e.,
Amazon DataZone would not be able to grant subscriptions to this table. For more
information, see [Configure Lake Formation
permissions for Amazon DataZone](lake-formation-permissions-for-datazone.md "lake-formation-permissions-for-datazone.md").

### HIPAA eligibility

Released on 12/14/2023

Amazon DataZone is now U.S. Health Insurance Portability and Accountability Act of 1996
(HIPAA) compliant. To view the list of AWS services with HIPAA compliance see
[https://aws.amazon.com/compliance/hipaa-eligible-services-reference/](https://aws.amazon.com/compliance/hipaa-eligible-services-reference/ "https://aws.amazon.com/compliance/hipaa-eligible-services-reference/").

### AI recommendations for descriptions in Amazon DataZone

(Preview)

Released on 11/28/2023

AWS announces the preview of a new generative AI-based capability in Amazon DataZone
to improve data discovery, data understanding, and data usage by enriching the
business data catalog. With a single click, data producers can generate
comprehensive business data descriptions and context, highlight impactful columns,
and include recommendations on analytical use cases. With AI recommendations for
descriptions in Amazon DataZone, data consumers can identify data tables and columns
required for analysis, which enhances data discoverability and cuts down on
back-and-forth communications with data producers. The preview is available in
Amazon DataZone domains provisioned in the following AWS Regions: US East (N.
Virginia), US West (Oregon). For more information, see [Using machine learning and generative AI in Amazon DataZone](autodoc.md "autodoc.md").

### DefaultDataLake blueprint enhancement

Released on 11/20/2023

Amazon DataZone has added an enhancement to the DefaultDataLake blueprint that provides
you with better control over who can publish what data from your AWS account.
There are two key changes that were introduced with this feature launch.

- In the console, once you enable the DefaultDataLake blueprint, you can
  control which projects can use the DefaultDataLake blueprint in your account
  to create environment profiles by assigning managing projects to the enabled
  blueprint.
- The second change is in the portal. If you create an environment profile
  using the DefaultDataLake blueprint, you can also select the authorized
  projects that are allowed to use the environment profile for creating
  environments. By default, all projects are allowed to use the data lake
  environment profile, but you can restrict the environment profile to
  specific projects and also control what data can be published using the
  environments created with the profile.

For more information, see [Create an environment profile](create-environment-profile.md "create-environment-profile.md").
