# Alation integration

The integration between Amazon SageMaker Catalog and Alation synchronizes catalog metadata between
both systems. Alation is a data intelligence platform that helps organizations make data
discoverable, governed, and actionable. This integration creates a unified metadata experience
where technical teams working in Amazon SageMaker Unified Studio and business teams working in Alation
collaborate on top of the same metadata. For detailed setup instructions, see [Build a trusted foundation for data and AI using Alation and Amazon SageMaker Unified
Studio](https://aws.amazon.com/blogs/big-data/build-a-trusted-foundation-for-data-and-ai-using-alation-and-amazon-sagemaker-unified-studio/ "https://aws.amazon.com/blogs/big-data/build-a-trusted-foundation-for-data-and-ai-using-alation-and-amazon-sagemaker-unified-studio/").

## Capabilities

The current phase of the Alation integration extracts metadata from Amazon SageMaker Catalog
into Alation. The integration synchronizes the following metadata:

- Domains, projects, and asset names.
- Descriptions, owners, and glossary terms.
- Custom metadata fields (metadata forms).
- Provenance metadata, including the originating service, the actor who made the
  change, and the timestamp.

You can run metadata extractions on demand or schedule them to run automatically. The
system performs an initial bulk extraction and then keeps data current through incremental
updates.

## How it works

The integration connects through AWS Identity and Access Management authentication. You can use either an IAM
role (recommended) or an IAM user with access keys. The connector uses scoped IAM
permissions following least-privilege principles. Communication uses encrypted APIs, and only
metadata is synchronized. Your data files and artifacts remain in their original AWS
locations.

You set up this integration by installing the SageMaker enhanced connector in Alation and
configuring a data source connection.
