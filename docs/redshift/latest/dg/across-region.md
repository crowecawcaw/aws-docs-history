Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Sharing data across AWS Regions

You can share data for read purposes across Amazon Redshift clusters in AWS Regions.
With cross-Region data sharing, you can share data across AWS Regions without the
need to copy data manually. You don't have to unload your data into Amazon S3 and
copy the data into a new Amazon Redshift cluster or perform cross-Region snapshot copy.

With cross-Region data sharing, you can share data across clusters in the same
AWS account, or in different AWS accounts even when the clusters are in different
Regions. When sharing data with Amazon Redshift clusters that are in the same AWS account but
different AWS Regions, follow the same workflow as sharing data within an
AWS account. For more information, see [Sharing read access to data within an
AWS account](within-account.md "within-account.md").

If clusters sharing data are in different AWS accounts and AWS Regions, you
can follow the same workflow as sharing data across AWS accounts and include
Region-level associations on the consumer cluster. Cross-Region data sharing supports
datashare association with the entire AWS account, the entire AWS Region, or
specific namespaces within an AWS Region. For more information about sharing data
across AWS accounts, see [Sharing data across AWS accounts](across-account.md "across-account.md").

When consuming data from a different Region, the consumer pays the Cross-Region
data transfer fee from the producer region to the consumer Region.

To use the datashare, a consumer account administrator can associate the datashare
in one of the following three ways.

- Association with an entire AWS account spanning all its
  AWS Regions
- Association with a specific AWS Region in an AWS account
- Association with specific namespaces within an AWS Region
  When the administrator chooses the entire AWS account, all existing and future
  namespaces across different AWS Regions in the account have access to the
  datashares. A consumer account administrator can also choose specific AWS Regions
  or namespaces within a Region to grant them access to the datashares.

**If you are a producer administrator or database
owner**, create a datashare, add database objects and data consumers to
the datashare, and grant permissions to data consumers. For more information, see
[producer administrator actions](producer-cluster-admin.md "producer-cluster-admin.md").

**If you are a producer account administrator**,
authorize datashares using the AWS Command Line Interface (AWS CLI) or the Amazon Redshift console and choose the
data consumers.

**If you are a consumer account administrator**
– follow these steps:

To associate one or more datashares that are shared from other accounts to your
entire AWS account or specific AWS Regions or namespaces within an AWS Region,
use the Amazon Redshift console.

With cross-Region data sharing, you can add clusters in a specific AWS Region
using the AWS Command Line Interface (AWS CLI) or Amazon Redshift console.

To specify one or more AWS Regions, you can use the
`associate-data-share-consumer` CLI command with the optional
`consumer-region` option.

With the CLI, the following example associates the `Salesshare` with
the entire AWS account with the `associate-entire-account` option. You
can only associate one Region at a time.

```
aws redshift associate-data-share-consumer
--region {PRODUCER_REGION}
--data-share-arn arn:aws:redshift:{PRODUCER_REGION}:{PRODUCER_ACCOUNT}:datashare:{PRODUCER_CLUSTER_NAMESPACE}/Salesshare
--associate-entire-account
```

The following example associates the `Salesshare` with the
US East (Ohio) Region (`us-east-2`).

```
aws redshift associate-data-share-consumer
--region {PRODUCER_REGION}
--data-share-arn arn:aws:redshift:{PRODUCER_REGION}:0123456789012:datashare:{PRODUCER_CLUSTER_NAMESPACE}/Salesshare
--consumer-region 'us-east-2'
```

The following example associates the `Salesshare` with a specific
consumer namespace in another AWS account in the Asia Pacific (Sydney) Region
(`ap-southeast-2`).

```
aws redshift associate-data-share-consumer
--data-share-arn arn:aws:redshift:{PRODUCER_REGION}:{PRODUCER_ACCOUNT}:datashare:{PRODUCER_CLUSTER_NAMESPACE}/Salesshare
--consumer-arn 'arn:aws:redshift:ap-southeast-2:{CONSUMER_ACCOUNT}:namespace:{ConsumerImmutableClusterId}'
```

You can use the Amazon Redshift console to associate datashares with your entire
AWS account or specific AWS Regions or namespaces within an AWS Region. To do
this, sign in to the [https://console.aws.amazon.com/redshiftv2/](https://console.aws.amazon.com/redshiftv2/ "https://console.aws.amazon.com/redshiftv2/"). Then associate one or more datashares that are
shared from other accounts with your entire AWS account, the entire AWS Region,
or a specific namespace within an AWS Region. For more information, see [Associating a datashare from a different
AWS account in Amazon Redshift](writes-associating.md "writes-associating.md").

After the AWS account or specific namespaces are associated, the datashares
become available for consumption. You can also change datashare association at any
time. When changing association from individual namespaces to an AWS account,
Amazon Redshift overwrites the namespaces with the AWS account information. When changing
association from an AWS account to specific namespaces, Amazon Redshift overwrites the
AWS account information with the namespace information. When changing association
from an entire AWS account to specific AWS Regions and namespaces, Amazon Redshift
overwrites the AWS account information with the specific Region and namespace
information.

**If you are a consumer administrator**, you can
create local databases that reference to the datashares and grant permissions on
databases created from the datashares to user or roles in the consumer cluster as
needed. You can also create views on shared objects and create external schemas to
refer and assign granular permissions to specific schemas in the consumer database
imported on the consumer cluster. For more information, see [consumer administrator actions](consumer-cluster-admin.md "consumer-cluster-admin.md").
