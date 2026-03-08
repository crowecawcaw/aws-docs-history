# Atlan integration

The integration between Amazon SageMaker Catalog and Atlan enables bidirectional metadata
synchronization across both platforms. Atlan is a data workspace that helps business users,
analysts, and engineers collaborate on data projects. This integration connects teams working
in Atlan with technical teams working in Amazon SageMaker Unified Studio for analytics and machine
learning. For detailed setup instructions, see [Unifying governance and metadata across Amazon SageMaker Unified Studio and
Atlan](https://aws.amazon.com/blogs/big-data/unifying-governance-and-metadata-across-amazon-sagemaker-unified-studio-and-atlan/ "https://aws.amazon.com/blogs/big-data/unifying-governance-and-metadata-across-amazon-sagemaker-unified-studio-and-atlan/").

## Capabilities

The Atlan integration supports the following capabilities:

- On-demand and scheduled bidirectional metadata synchronization.
- Synchronization of glossary terms and descriptions, including parent-child
  relationships.
- Ingestion of projects, published and subscribed assets, domains, data products,
  metadata forms, and column descriptions from Amazon SageMaker Catalog into Atlan.
- Automatic association of glossary terms with related data assets.
- Real-time reverse sync of metadata updates from Atlan back to Amazon SageMaker
  Catalog.

## How it works

The integration uses AWS Identity and Access Management roles to establish a secure connection between your
AWS account and Atlan. You deploy an AWS CloudFormation template that creates the required IAM
role and policies. This role follows the principle of least privilege, granting Atlan access
only to the resources required for cataloging and governance.

After you configure the connection, the Atlan connector calls Amazon SageMaker Unified Studio APIs to
ingest assets and metadata. The connector transforms ingested assets into Atlan's metadata
model, making them discoverable and governable inside Atlan. When users update metadata in
Atlan, the real-time reverse sync pipeline detects changes and pushes updates back to
Amazon SageMaker Catalog.

You set up this integration by configuring a connection to Amazon SageMaker Unified Studio from within
Atlan.
