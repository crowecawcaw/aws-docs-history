# Amazon SageMaker Unified Studio terminology and concepts

As you get started with Amazon SageMaker Unified Studio, it is important that you understand its key concepts,
terminology, and components.

**Amazon SageMaker Unified Studio**

This is a browser-based web application where you can use all your data and tools for
analytics and AI. Amazon SageMaker Unified Studio can authenticate you with your IAM user credentials or with
credentials from your identity provider through the IAM Identity Center or with your SAML credentials. You
can obtain the Amazon SageMaker Unified Studio URL for your domains by accessing the SageMaker AI management console at
[https://console.aws.amazon.com/datazone](https://console.aws.amazon.com/datazone "https://console.aws.amazon.com/datazone").

**Amazon SageMaker management console**

You can use the SageMaker AI management console at [https://console.aws.amazon.com/datazone](https://console.aws.amazon.com/datazone "https://console.aws.amazon.com/datazone")
to access and conﬁgure your domains for user management, account associations, project
profiles, blueprints, Amazon Bedrock models, Git connections, and Amazon Q usage.

**Amazon Bedrock in SageMaker Unified Studio**

Use Amazon Bedrock in SageMaker Unified Studio to build and scale generative AI applications. Amazon Bedrock in SageMaker Unified Studio provides a web
interface that allow users to interact with [Amazon Bedrock](../../../bedrock/latest/userguide/what-is-bedrock.md "../../../bedrock/latest/userguide/what-is-bedrock.md") foundation models and use Amazon Bedrock tools, such as agents, guardrails, prompts,
flows, evaluation, and functions in a seamless unified fashion. Users can interact with models
in a generative AI playground or collaborate on developing generative AI applications in
projects.

**Amazon Q Developer**

Amazon Q Developer is an AI coding assistant that can chat about code, provide inline code
completions, generate net new code, scan your code for security vulnerabilities, and make code
upgrades and improvements.

In the current release of Amazon SageMaker Unified Studio, by default, all users of an Amazon SageMaker Unified Studio domain have
access to the Free Tier release of Amazon Q.

**lakehouse architecture**

lakehouse architecture unifies
your data across Amazon S3 data lakes and Amazon Redshift data warehouses. lakehouse architecture
helps you build powerful analytics, machine learning (ML), and generative AI
applications on a single copy of data.

lakehouse architecture is accessible via Amazon SageMaker Unified Studio.

**Amazon SageMaker Data Processing Visual ETL**

In Amazon SageMaker Unified Studio you can author highly scalable extract, transform, load (ETL) data
integration flows for distributed processing without becoming an Apache Spark expert. You can
define your data integration flow in the simple visual interface and Amazon SageMaker Unified Studio automatically
generates the code to move and transform your data. The code is generated in Python and written
for Apache Spark. Additionally, you can choose to author your visual flows in English using
generative AI prompts from Amazon Q.

**Asset**

In Amazon SageMaker Unified Studio, an asset is an entity that presents a single physical data object (for
example, a table, a dashboard, a file) or virtual data object (for example, a view).

**Asset type**

Asset types define how assets are represented in the Amazon SageMaker Catalog. An asset
type defines the schema for a specific type of asset. When assets are created, they are
validated against the schema defined by their asset type (by default, the latest version). When
an asset update occurs, Amazon SageMaker Unified Studio creates a new asset version and enables Amazon SageMaker Unified Studio users to
operate on all asset versions.

**Associated accounts**

Use account associations in Amazon SageMaker Unified Studio to publish data from other AWS accounts into the
Amazon SageMaker Catalog and create projects to work with data across multiple AWS accounts.
AWS accounts where Amazon SageMaker unified root domains are created initiate the account
association requests. You can request association from the Amazon SageMaker management console.
Account association requests must be accepted by the administrators of the AWS accounts
invited for account association. You can authorize the domain account to use data or allow
infrastructure deployment with the right IAM permissions as part of approval. Once an
associated account is linked to a domain, projects in Amazon SageMaker Unified Studio can use
resources from those accounts and also other types of assets. You can deploy resources in
specific AWS accounts through project profiles.

**Authorization policy**

Authorization policies are a set of controls within Amazon SageMaker Unified Studio applied to entities such as
projects, blueprints, environments, glossary, and metadata forms.

Within an Amazon SageMaker Unified Studio domain unit, you can assign the following authorization policies to
your users and groups to grant them specific permissions:

- Domain unit creation policy
- Project creation policy
- Project membership policy
- Domain unit ownership assumption policy
- Project ownership assumption policy

Within an Amazon SageMaker Unified Studio domain unit, you can assign the following authorization policies to
your projects to grant them specific permissions:

- Glossary creation policy
- Metadata forms creation policy
- Custom asset type creation policy

Within a specific blueprint configuration, you can assign the following authorization
policies to projects and domain unit owners:

- Create environment profiles using this blueprint. This policy can be assigned to
  Amazon SageMaker Unified Studio projects, and it authorizes them to create environment profiles using this
  blueprint.
- Grant permissions to create environment profiles using this blueprint . This policy can
  be assigned to domain unit owners and it authorizes them to grant permissions to projects to
  create environment profiles using this blueprint.

**AWS account owner**

In Amazon SageMaker Unified Studio, AWS account owners create roles, policies, and permissions in their
AWS accounts that enable these AWS accounts to be associated with Amazon SageMaker Unified Studio domains.

**Blueprint**

A blueprint is used to create the project profile that defines which AWS tools and
services project members can use as they work with data in the Amazon SageMaker Catalog.

In the current release of Amazon SageMaker Unified Studio the following default blueprints are supported:

| Blueprint name             | Description                                                                                                                                                                                                                                                                                    | Resources created                                                                                                                                                                                                                                                            |
| -------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| AmazonBedrockGenerativeAI  | This is the combined Amazon Bedrock blueprint which contains seven sub-Amazon Bedrock<br>blueprints. Users create project profiles with this blueprint to build generative AI applications using tools such as agents, knowledge bases,<br>guardrails, flows, functions, and model evaluation. |
| AmazonBedrockChatAgent     | Provides a reusable AWS CloudFormation template to create an Amazon Bedrock Agent<br>and supporting resources, including an execution role and a consumption role.                                                                                                                             | Bedrock Agent, Bedrock Agent Execution role, Bedrock Agent Consumption role                                                                                                                                                                                                  |
| AmazonBedrockEvaluation    | Creates one IAM role as the service role for an Amazon Bedrock evaluation<br>job.                                                                                                                                                                                                              | Bedrock Evaluation job execution role                                                                                                                                                                                                                                        |
| AmazonBedrockFlow          | Provides a reusable AWS CloudFormation template to create an Amazon Bedrock Prompt<br>Flow and supporting resources such as an execution role.                                                                                                                                                 | Amazon Bedrock Flow, Amazon Bedrock Flow Execution role                                                                                                                                                                                                                      |
| AmazonBedrockFunction      | Provides a reusable AWS CloudFormation template to create an AWS Lamda function<br>and supporting resources, such as an execution role, and a secret manager.                                                                                                                                  | Secrets Manager secret, AWS Lambda function, AWS Lambda function execution role,<br>Log group                                                                                                                                                                                |
| AmazonBedrockGuardrail     | Provides an AWS CloudFormation template to create an Amazon Bedrock Guardrail and<br>supporting resources such as an execution role.                                                                                                                                                           | Amazon Bedrock Guardrail                                                                                                                                                                                                                                                     |
| AmazonBedrockKnowledgeBase | Provides an AWS CloudFormation template to create a reusable Amazon Bedrock<br>Knowledge Base and supporting resources such as an execution role.                                                                                                                                              | Amazon Bedrock Knowledge Base, OpenSearch Serverless collection, Amazon Bedrock<br>Knowledge Base Execution role, AWS Lambdas, including OpenSearch Index Lambda and KB<br>Ingestion Trigger Lambda, AWS Lambda Execution role, Amazon Bedrock Knowledge Base data<br>source |
| AmazonBedrockPrompt        | Provides a reusable AWS CloudFormation template to create an Amazon Bedrock Prompt<br>and supporting resources, such as an execution role, and a consumption role.                                                                                                                             | Amazon Bedrock Prompt, Amazon Bedrock Prompt Consumption role                                                                                                                                                                                                                |
| LakeHouseDatabase          | Provides a reusable AWS CloudFormation template to create a data lake environment<br>with a AWS Glue database for data management and an Amazon Athena workgroup for querying<br>data.                                                                                                         | AWS Glue databases, lake formation permissions, Amazon Athena workgroups                                                                                                                                                                                                     |
| EMRonEC2                   | Provides a reusable AWS CloudFormation template to create an Amazon EMR on EC2<br>cluster to run and scale Apache Spark, Hive, and other big data workloads.                                                                                                                                   | EMR on EC2 clusters                                                                                                                                                                                                                                                          |
| EMRServerless              | Provides a reusable AWS CloudFormation template to create an Amazon EMR Serverless<br>application that is ready to serve Apache Spark batch jobs and interactive<br>sessions.                                                                                                                  | EMR on Serverless applications                                                                                                                                                                                                                                               |
| LakehouseCatalog           | Provisions a new catalog in the lakehouse architecture that is backed by Amazon<br>Redshift Managed Storage                                                                                                                                                                                    |
| MLExperiments              | Provides OnDemand blueprint to enable MLflow tracking server for the experimentation<br>inside a project.                                                                                                                                                                                      | MLflow tracking server (on demand)                                                                                                                                                                                                                                           |
| PartnerApps                | Creates an IAM role and a Connection that enables access to Partner AI Apps. Through<br>Partner AI Apps you can leverage integrated and fully-managed thrid-party solutions for<br>AI/Ml development.                                                                                          | Amazon SageMaker Partner AI Apps IAM role, Amazon SageMaker Partner AI Apps<br>Connection                                                                                                                                                                                    |
| RedshiftServerless         | Provides a reusable AWS CloudFormation template to create an Amazon Redshift<br>Serverless environment to get insights from data without managing infrastructure.                                                                                                                              | Amazon Redshift Serverless warehouses                                                                                                                                                                                                                                        |
| Tooling                    | Creates resources for the project, including IAM user roles, security groups, and<br>Amazon SageMaker unified domains.                                                                                                                                                                         | IAM user roles, Amazon SageMaker unified domains, security groups                                                                                                                                                                                                            |
| Workflows                  | Provides an AWS CloudFormation template to create the MWAA environment for Airflow<br>based Workflows                                                                                                                                                                                          | Enables project workflows on MWAA                                                                                                                                                                                                                                            |

**Amazon SageMaker Catalog**

This is a catalog of all the published assets from various projects. The scope of the
Amazon SageMaker Catalog is the domain, therefore published assets are discoverable by all projects in
that domain. The Amazon SageMaker Catalog enables discovery that crosses the account and Region
boundary. You can publish assets to the Amazon SageMaker Catalogso that other projects can subscribe
to them, or you can subscribe to assets in the catalog that were published from other projects.
Every asset that lives in the Amazon SageMaker Catalog has an owner project (also known as the
producer project) which controls policies around how subscriptions can be fulfilled. A
subscriber (also known as a consumer project) can make a request to the owner project to gain
access to the asset. Once the request is approved, the owner project provides the necessary
permissions to the subscriber project so that it may gain access to that asset.

**Business glossary**

In Amazon SageMaker Unified Studio, a business glossary is a collection of business terms that may be associated
with assets. A business glossary helps ensure that the same terms and definitions are used
across an organization throughout its various data analytics tasks. You can add terms in a
business glossary to assets and columns to classify or enhance the identification of those
attributes during search. You can select glossary as the value type for a field in a metadata
form that is associated with an asset. When you select a particular term as the value for an
asset's metadata form field, users can search for the business glossary term and find the
associated assets.

**Git connection**

Use git connections to check in and check out files and manage your code repository. When
you create an Amazon SageMaker unified domain, a default git connection to CodeCommit is
provided for you to manage your code. You can also create and enable new 3P Git connections to
GitHub, GitHub Enterprise Server, GitLab, and GitLab Self-Managed.

**Data source**

An entity which brings in metadata from a source and adds metadata forms (such as the
ingestion job). This entity allows publishers to capture ingestion configuration including what
metadata forms to attach and whether to run BNG. Since this configuration has a one-to-many
mapping with the credentials provided by the publisher, we believe that it should be captured
in a separate entity.

In Amazon SageMaker Unified Studio, you can use data sources to import technical metadata of assets (data) from
the source databases or data warehouses into Amazon SageMaker Unified Studio. In the current release of Amazon SageMaker Unified Studio,
you can create and run data sources for AWS Glue and Amazon Redshift. By creating a data
source, you establish a connection between Amazon SageMaker Unified Studio and the source (AWS Glue Data Catalog or
Amazon Redshift Warehouse), which you can then use to read technical metadata, including table
names, columns names, and data types. By creating a data source, you also begin the initial
data source run that creates new or updates existing assets in Amazon SageMaker Unified Studio. While creating a data
source or after the data source is successfully created, you also have the option to specify a
schedule for your data source runs.

**Data source run**

In Amazon SageMaker Unified Studio, a data source run is a task that Amazon SageMaker Unified Studio performs in order to create
assets in project inventories and also optionally to publish project inventory assets to the
Amazon SageMaker Catalog. Data source runs can be automated (started when a data source is
initially created), scheduled, or manual. Use data selection criteria to fine-tune the existing
and future data sets to be ingested into project inventories or the Amazon SageMaker Catalog
and the frequency of metadata updates to those inventory or catalog assets.

**Domain**

In Amazon SageMaker Unified Studio, a domain is the organizing entity for connecting together your assets,
users, and their projects. With Amazon SageMaker unified domains, you have the flexibility to
reflect the data and analytics needs of your organizational structure, whether it's creating a
single Amazon SageMaker unified domain for your enterprise or multiple domains for different
business units.

**Domain administrator**

The IAM principal ID that has the super administrative permissions to edit entities in the
domain.

In Amazon SageMaker Unified Studio, an IAM principal who creates an Amazon SageMaker Unified Studio domain is the default domain
administrator of that domain. Domain administrators in Amazon SageMaker Unified Studio perform key functionalities
for the domain, including creating domains, assigning other domain administrators, creating and
managing project profiles, configuring blueprints, user management, account associations,
Amazon Bedrock models, Git connections, and Amazon Q.

**Domain unit**

Use domain units to organize your assets and other domain entities under specific business
units and teams. To set up secure and efficient data sharing within and across business units
of your organization, you can create domain units within Amazon SageMaker Unified Studio and grant access to selected
users within each business unit to log in and share their assets to the Amazon SageMaker Catalog. Domain units
can also be used for resource owners, such as AWS account owners, to set up Amazon SageMaker Unified Studio
authorization permissions on their resources. Domain units provide a delegated authority from
account owners to domain unit owners and they can set up authorization permissions on behalf of
account owners.

**JupyterLab**

Amazon SageMaker Unified Studio provides a JupyterLab interactive development environment (IDE) for you to use
as you perform data integration, analytics, or machine learning in your projects. JupyterLab
IDE is built on JupyterLab spaces and Amazon SageMaker Distribution.

**Metadata form type**

A metadata form type is a template that defines the metadata that is collected and saved
when assets are created as inventory or published in an Amazon SageMaker unified domain.
Metadata form types can be associated with a data asset. Metadata form types help domain
administrators to define metadata forms needed for that domain, such as compliance information,
regulation information, or classifications. Domain administrators can use this to customize
additional metadata for their assets. Amazon SageMaker Unified Studio has system metadata form types such as
asset-common-details-form-type, column-business-metadata-form-type, glue-table-form-type,
glue-view-form-type, redshift-table-form-type, redshift-view-form-type,
s3-object-collection-form-type, subscription-terms-form-type, and suggestion-form-type.

**Metadata form**

In Amazon SageMaker Unified Studio, metadata forms define the metadata that is collected and saved when assets
are created as inventory or published in an Amazon SageMaker unified domain. Metadata form
definitions are created in the domain catalog by a domain administrator. A metadata form
definition is composed of one or more field definitions, with support for boolean, date,
decimal, integer, string, and business glossary field value data types. A domain administrator
applies a metadata form to assets in their domain by adding the metadata form to their domain.
Asset publishers then provide any optional and required field values in the metadata form.

**Project profile**

In Amazon SageMaker Unified Studio, a project profile is a template for projects in your Amazon SageMaker
unified domains. A project profile is a collection of blueprints, which are configurations
used to create projects. A project profile can define if a particular blueprint is enabled
during the creation of the project, or available later for the project users to enable on
demand.

You must be an administrator of a Amazon SageMaker Unified Studio domain to create and manage project profiles.
In the current release of Amazon SageMaker Unified Studio, you can create the following project profiles:

- Data analytics and AI/ML model development project profile
- SQL analytics project profile
- Generative AI application development project profile
- Custom project profile

**Projects in Identity Center-based domains**

The project entity is the mechanism by which Amazon SageMaker Unified Studio users organize their work and
provide business context over the jobs they are performing. A project is a container for all
the user's code, including notebooks, queries, dashboards, workflows, and more.
A
project provides three capabilities:

1. Business context for the user’s work which provides a
   level of audit to the functionality being performed.
2. A collaboration boundary where the users
   can work with each other by interacting with the project’s source control repository.
3. A permissions boundary which gives users access to all the project artifacts and data/compute
   permissions after the users are added to the project.

A project exists within
a domain. A single Amazon SageMaker unified domain can have several projects and each user can
be added to multiple projects.

Each project is created using a template called a project profile, which is enabled by an
administrator during the setup phase. A project profile controls the tools available within the
project. Project members can request access to assets from the Amazon SageMaker Catalog and
produce new artifacts using one or more of the tools available inside the project. Artifacts in
a project are not accessible outside of the project unless they are published to the Amazon SageMaker Catalog which is discussed later.

Each project has one or multiple owners, who can add or remove other users (called project
members) as owners or contributors and can modify or delete projects. Other restrictions on
contributors can be defined with policies. When a user creates a project, they become the first
owner of that project.

**Project S3 path**

The purpose of the project S3 path in Amazon SageMaker Unified Studio is to provide a secure, project-isolated
location for storing temporary execution data and other project-related artifacts. The project
S3 path follows a standardized structure of
"<bucket>/<domain_id>/<project_id>/<project_scope>/" to ensure
separation between projects and prevent objects from being shared across projects. The project
S3 path is also used to store specific types of data, such as the location for the provisioned
consumer AWS Glue database, Athena Workgroup output, and temporary storage for individual
workflow runs.

**Project Git repository**

A project includes a dedicated git repository which serves as a central hub for users to
manage version control for the code associated with their Amazon SageMaker Unified Studio projects. This enables
collaboration across users within a project. All tools that generate file-based assets must use
the project git repository for version control, for example, the query editor, JupyterLab IDE,
and more. By default, Amazon SageMaker Unified Studio uses AWS CodeCommit as the project’s repository which is
created when a project is created. However, administrators can modify this to connect a
third-party Git repository such as Github, Github Enterprise Server, GitLab, or BitBucket
instead of the default repository.

**Project member**

A project member is any user who has been added to a project and given access to the
project data and resources. Users can be enterprise users sourced from the IDP, or IAM
Principals from one of the domain associated accounts. Project owners can add members either by
adding them directly or by selecting enterprise groups. A project member is added to a project
with a designation that defines the set of permissions it has within the project. Users can
collaborate on various activities such as accessing data assets, performing data analysis or
machine learning activities.

**Subscription request**

A request to use a data product.

In Amazon SageMaker Unified Studio, a subscription request is a process that an Amazon SageMaker Unified Studio project must follow in
order to be granted access to a speciﬁc asset. Subscription requests can be approved, rejected,
revoked, or granted.

**Subscription grant**

An object representing a fulfilled request for a particular project.

**Querybook**

Use querybooks to develop, run, and share multiple SQL queries in a single interactive
notebook. They provide an environment for data scientists, analysts, and developers to query,
analyze, and visualize data using Amazon Redshift or Amazon Athena as the query engine. Cells
in a Querybook contain SQL statements or markdown and can be run individually, like a
traditional query editor, or sequentially. Query results appear in-line with each cell, where
you can toggle between multiple results and create data visualizations. To accelerate query
development, Querybooks integrate with Amazon Q to generate SQL queries from natural language
input, and provide auto-complete suggestions for table names, column names, and SQL keywords as
you type. Amazon SageMaker Unified Studio automatically saves your work as you progress. When ready, you can publish
your Querybook to your project for collaboration with teammates.

**Space**

A space in Amazon SageMaker Unified Studio refers to a personalized workspace that provides an isolated,
sandboxed environment for users to run arbitrary code without interfering with other workers in
a project. Each space consists of a compute instance, an EBS volume, and the JupyterLab
application. Users can access their spaces through various entry points in Amazon SageMaker Unified Studio, the
developer tools section, or by selecting Notebook files. The project Git repository is cloned
into the space when you create the space. SageMaker Distribution is the image that is used to
provide all the libraries, extensions, and packages in the IDE application.
