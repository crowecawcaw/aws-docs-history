# Best practice 3.8 – Enforce downstream systems to honor the data classifications

Since other data-consuming systems will access the data that
the analytics workload shares, the workload should require
the downstream systems to implement the required data
classification policies. For example, if the analytics
workload shares the data that is required to be encrypted
using customer managed private keys in AWS Key Management Service (AWS KMS), then the downstream systems should also
acknowledge and implement such a data protection policy.

This helps to ensure that the data is protected throughout
the data pipelines.

## Suggestion 3.8.1 – Have a centralized, shareable catalog with cross-account access to ensure that data owners manage permissions for downstream systems

Downstream systems can run on independent AWS accounts,
different from the AWS account running the majority of the
analytics workload. Downstream systems should be able to
discover the data, acknowledge the required data
protection policies, and enforce those policies across the
analytics platform.

To allow the downstream systems to use the data from
analytics workload, the analytics workload should provide
cross-account access based on least privileges for each
dataset.

For more details, refer to the following information:

- AWS Big Data Blog: [Cross-account AWS Glue Data Catalog access with Amazon Athena](https://aws.amazon.com/blogs/big-data/cross-account-aws-glue-data-catalog-access-with-amazon-athena/ "https://aws.amazon.com/blogs/big-data/cross-account-aws-glue-data-catalog-access-with-amazon-athena/")
- AWS Big Data Blog:
  [How
  JPMorgan Chase built a data mesh architecture to drive
  significant value to](https://aws.amazon.com/blogs/big-data/how-jpmorgan-chase-built-a-data-mesh-architecture-to-drive-significant-value-to-enhance-their-enterprise-data-platform/ "https://aws.amazon.com/blogs/big-data/how-jpmorgan-chase-built-a-data-mesh-architecture-to-drive-significant-value-to-enhance-their-enterprise-data-platform/")
  [enhance
  their enterprise data platform](https://aws.amazon.com/blogs/big-data/how-jpmorgan-chase-built-a-data-mesh-architecture-to-drive-significant-value-to-enhance-their-enterprise-data-platform/ "https://aws.amazon.com/blogs/big-data/how-jpmorgan-chase-built-a-data-mesh-architecture-to-drive-significant-value-to-enhance-their-enterprise-data-platform/")

## Suggestion 3.8.2 – Monitor the downstream systems’ eligibility to access classified data from the analytics workload

Monitor the downstream systems’ eligibility to handle
sensitive data. For example, you do not want development
or test Amazon Redshift clusters to read sensitive data
from the analytics workload. If your organization runs a
program that certifies which systems are eligible to
process various classes of data, periodically verify that
each downstream system’s data processing eligibility
levels are correct and the list of data that it accesses
are appropriate.
