# Quick create an Aurora PostgreSQL Knowledge Base for Amazon Bedrock

Amazon Bedrock's retrieval augmented generation (RAG) workflow relies on vector data stored in an Aurora PostgreSQL database to power content retrieval.
Previously, setting up Aurora PostgreSQL as the vector data store for Bedrock Knowledge Bases was a multi-step process, requiring
numerous manual actions across different user interfaces. This made it challenging for data scientists and developers to leverage Aurora
for their Bedrock projects.

To improve the user experience, AWS has created a new CloudFormation-based quick create option that simplifies the setup process.
With Aurora quick create, you can now provision a pre-configured Aurora PostgreSQL DB cluster as the vector store for your Amazon Bedrock Knowledge Bases with a single click.

###### Topics

- [Supported regions and Aurora PostgreSQL versions](#AuroraPostgreSQL.quickcreatekb.avail "#AuroraPostgreSQL.quickcreatekb.avail")
- [Understanding the quick create process](#AuroraPostgreSQL.quickcreatekb.using "#AuroraPostgreSQL.quickcreatekb.using")
- [Benefits of using Aurora quick create](#AuroraPostgreSQL.quickcreatekb.adv "#AuroraPostgreSQL.quickcreatekb.adv")
- [Limitations of Aurora quick create process](#AuroraPostgreSQL.quickcreatekb.limit "#AuroraPostgreSQL.quickcreatekb.limit")

## Supported regions and Aurora PostgreSQL versions

The Aurora quick create option is available in all the AWS regions that support Amazon Bedrock Knowledge Bases.
By default, it creates an Aurora PostgreSQL DB cluster with version 15.7. For more information about supported Regions, see
[Supported models and regions for Amazon Bedrock Knowledge Bases](../../../bedrock/latest/userguide/knowledge-base-supported.md "../../../bedrock/latest/userguide/knowledge-base-supported.md").

## Understanding the quick create process

The quick create process automatically provisions the following resources to set up an Amazon Aurora PostgreSQL database as the vector data store for your Bedrock Knowledge Base:

An Aurora PostgreSQL DB cluster in your account, configured with default settings.

- ACUs (Aurora Capacity Units) are set from 0 to 16. This lets your vector store scale down to zero when not in use, saving on compute costs.
  The ACUs can be adjusted later in the Amazon RDS console.
- (Hierarchical Navigable Small World) HNSW index using Euclidean distance as a similarity measure for the Bedrock vector embeddings stored in Aurora.
- The DB instance is a serverless v2 instance.
- The cluster is associated with the default VPC and subnets, and has the RDS Data API enabled.
- The cluster admin credentials are managed by AWS Secrets Manager.

Besides the default settings, the following settings are set up for you. As you go through the process, you'll see screens that explains the workflow.

- Seeding the Aurora cluster with the necessary database objects:
  - Create the pgvector extension, schema, role, and tables required for the Bedrock Knowledge Base.
  - Register a limited-privilege database user for Bedrock to interact with the cluster.

- A progress banner will be displayed throughout the resource provisioning process, allowing you to track the status of the following sub-events:

      + Aurora cluster creation
      + Seeding the Aurora cluster
      + Knowledge Base creation

  The banner stays visible until the knowledge base is fully created, even if you navigate away from the page and return.

- You can click `View details` on the progress banner to see the status of each step. For more information about events
  during knowledge base creation, choose the CloudFormation link in the view details screen. Once the process is complete, your new Bedrock
  Knowledge Base will be ready to use.
- The stack IDs for all the quick create resources can be found in the tags of the Bedrock Knowledge Base, should you need to reference them.

A Bedrock Knowledge Base, with the configuration to the newly provisioned Aurora cluster as the vector store is created.

## Benefits of using Aurora quick create

- The CloudFormation-based quick create process significantly reduces the time and complexity required to use Aurora as the vector store.
- Aurora offers excellent performance, vector scalability and cost benefits with the ability to scale to zero compute charges when not in use.
- The quick create process streamlines the end-to-end experience, allowing you to easily create and configure your Bedrock Knowledge Bases using Aurora.
- Customers can build upon CloudFormation template to customize the provisioning with their own configurations.

## Limitations of Aurora quick create process

- With Aurora quick create option, the DB cluster is provisioned with default configurations. However, these default settings may not meet your specific requirements or intended use case.
  Quick create does not offer options to modify the configurations during the provisioning process. The configurations are set automatically to streamline the deployment experience. If you need
  to customize the Aurora DB cluster configuration, you can do so after the initial deployment by quick create in the Amazon RDS console.
- While quick create flow simplifies the setup process, the time to create the Aurora DB cluster is still approximately 10 minutes, the same as a manual deployment. This is due to the
  time required to provision the Aurora infrastructure.
- The quick create option is designed for experimentation and quick setup. The resources created through quick create may not be suitable for production use,
  and you won't be able to directly migrate them to a production environment in your VPC.
