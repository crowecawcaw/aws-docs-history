# Collibra integration

The integration between Amazon SageMaker Catalog and Collibra provides bidirectional metadata
synchronization and access governance across both platforms. Collibra is a data intelligence
platform that helps organizations centralize governance workflows, define business glossaries,
and enforce policies across data assets. This integration is available as an open-source
solution on [GitHub](https://github.com/aws-samples/amazon-datazone-examples/tree/main/blogs/unifying_metadata_governance_across_amazon_sagemaker_catalog_and_collibra "https://github.com/aws-samples/amazon-datazone-examples/tree/main/blogs/unifying_metadata_governance_across_amazon_sagemaker_catalog_and_collibra"), co-developed by AWS and Collibra. For detailed setup instructions, see
[Unifying metadata governance across Amazon SageMaker and Collibra](https://aws.amazon.com/blogs/big-data/unifying-metadata-governance-across-amazon-sagemaker-and-collibra/ "https://aws.amazon.com/blogs/big-data/unifying-metadata-governance-across-amazon-sagemaker-and-collibra/").

## Capabilities

### Metadata synchronization

The Collibra integration synchronizes the following metadata between Amazon SageMaker Catalog
and Collibra:

- Bidirectional synchronization of glossary terms and descriptions.
- Preservation of glossary structure, including parent-child relationships.
- Association of terms with data assets such as datasets, tables, and columns.
- Synchronization of classifications, data categories, and tags.
- Alignment of technical descriptions for datasets and columns.

Core metadata elements synchronize every 5 minutes. Subscription requests that originate
in Amazon SageMaker Catalog synchronize to Collibra instantly.

### Access request workflows

The Collibra integration extends Collibra's access governance workflows to assets
cataloged in Amazon SageMaker Catalog. Users can discover and request access to datasets from within
Collibra or Amazon SageMaker Unified Studio using familiar approval processes.

Key capabilities of the access request workflow include:

- Access request initiation from either Collibra or Amazon SageMaker Unified Studio.
- Centralized review and approval managed within Collibra by designated business
  stewards.
- Automatic access provisioning through the Amazon SageMaker Catalog grant mechanism.
- Status tracking of subscription requests across both platforms.

## How it works

The integration uses the APIs of both Amazon SageMaker and Collibra Data Governance Center. You
deploy an AWS CloudFormation template that provisions the required AWS resources, including IAM
roles and AWS Lambda functions. On the Collibra side, you configure operating model changes,
import workflows, and assign business stewards to assets.

The solution is available as an open-source project on [GitHub](https://github.com/aws-samples/amazon-datazone-examples/tree/main/blogs/unifying_metadata_governance_across_amazon_sagemaker_catalog_and_collibra "https://github.com/aws-samples/amazon-datazone-examples/tree/main/blogs/unifying_metadata_governance_across_amazon_sagemaker_catalog_and_collibra").
