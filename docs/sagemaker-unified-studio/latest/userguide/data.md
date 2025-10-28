# Data

Data in Amazon SageMaker Unified Studio includes data in projects of which you are a member and data that you can
discover and subscribe to from other projects.

The **Data** page in Amazon SageMaker Unified Studio displays a data browser in which you can
explore datasets, files, and artifacts that you connect to your project. Projects configured
with certain profiles contain an lakehouse architecture for accessing data within your project, as well as a
default Amazon Redshift connection and an Amazon S3 bucket. You can add data to the project
on the **Data** page by uploading data from your local desktop or by gaining
access to existing data sources and then adding a connection to them in your Amazon SageMaker Unified Studio project.
For more information about lakehouse architecture,
see [What is the lakehouse architecture of Amazon SageMaker?](../../../sagemaker-lakehouse-architecture/latest/userguide/what-is-smlh.md "../../../sagemaker-lakehouse-architecture/latest/userguide/what-is-smlh.md").

You can also connect to AWS Glue and Amazon Redshift data sources from
within your project catalog. The project catalog contains your data as data products and assets
with metadata. When you want to share your data with other projects in the domain, publish the
data from your project catalog into the Amazon SageMaker Catalog. If you want to create more detailed
access control for your data before allowing other users to subscribe to it, you can configure
fine-grained access control. For more information, see [Data inventory and publishing](data-publishing.md "data-publishing.md") and
[Fine-grained access control to data](fine-grained-access-control.md "fine-grained-access-control.md").

The Amazon SageMaker Catalog contains business glossaries and metadata forms. If you have been
granted access through the authorization policies, you can create business glossaries and
metadata forms. For more information, see [Domain units and authorization policies in Amazon SageMaker Unified Studio](../adminguide/domain-units.md "../adminguide/domain-units.md") and [Amazon SageMaker Unified Studio data catalog](working-with-business-catalog.md "working-with-business-catalog.md").

You can use the Amazon SageMaker Catalog to discover and subscribe to assets and data products. For
more information, see [Data discovery, subscription, and consumption](discover-data.md "discover-data.md").
