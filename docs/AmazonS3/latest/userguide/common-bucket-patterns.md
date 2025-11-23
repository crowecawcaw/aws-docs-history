# Common general purpose bucket patterns for building applications on

Amazon S3

When you build applications on Amazon S3, you can use unique general purpose buckets to separate different datasets or workloads. When you build applications
that serve end users or different user groups, use our best practices design
patterns to build applications that can best take advantage of Amazon S3 features and
scalability.

###### Important

We recommend that you create general purpose bucket names that are not predictable. Do not write code
assuming your chosen bucket name is available unless you have already created the
bucket. One method for creating bucket names that are not predictable is to append a
Globally Unique Identifier (GUID) to your bucket name, for example,
`amzn-s3-demo-bucket-a1b2c3d4-5678-90ab-cdef-EXAMPLE11111`.
For more information about general purpose bucket naming rules, see [General purpose bucket naming rules](bucketnamingrules.md "bucketnamingrules.md").

###### Topics

- [Multi-tenant general purpose bucket pattern](#multi-tenant-buckets "#multi-tenant-buckets")
- [Bucket-per-use pattern](#bucket-per-customer "#bucket-per-customer")

## Multi-tenant general purpose bucket pattern

With multi-tenant buckets, you create a single general purpose bucket for a team or workload. You use
[unique S3 prefixes](using-prefixes.md "using-prefixes.md") to organize the objects
that you store in the bucket. A prefix is a string of characters at the beginning of the
object key name. A prefix can be any length, subject to the maximum length of the object
key name (1,024 bytes). You can think of prefixes as a way to organize your data in a
similar way to directories. However, prefixes are not directories.

For example, to store information about cities, you might organize it by continent,
then by country, then by province or state. Because these names don't usually contain
punctuation, you might use slash (/) as the delimiter. The following examples shows
prefixes being used to organize city names by continent, country, and then province or
state, using a slash (/) delimiter.

- Europe/France/NouvelleA-Aquitaine/Bordeaux
- North America/Canada/Quebec/Montreal
- North America/USA/Washington/Bellevue
- North America/USA/Washington/Seattle

This pattern scales well when you have hundreds of unique datasets within a general purpose bucket.
With prefixes, you can easily organize and group these datasets.

However, one potential drawback to the multi-tenant general purpose bucket pattern is that many S3
bucket-level features like [default bucket
encryption](bucket-encryption.md "bucket-encryption.md"), [S3 Versioning](versioning-workflows.md "versioning-workflows.md"), and
[S3 Requester Pays](RequesterPaysBuckets.md "RequesterPaysBuckets.md") are set at the
bucket-level and not the prefix-level. If the different datasets within the multi-tenant
bucket have unique requirements, the fact that you can't configure many S3 bucket-level
features at the prefix-level can make it difficult for you to specify the correct
settings for each dataset. Additionally, in a multi-tenant bucket, [cost allocation](BucketBilling.md "BucketBilling.md") can become complex as you work to
understand the storage, requests, and data transfer associated with specific prefixes.

## Bucket-per-use pattern

With the bucket-per-use pattern, you create a general purpose bucket for each distinct dataset, end
user, or team. Because you can configure S3 bucket-level features for each of these
buckets, you can use this pattern to configure unique bucket-level settings. For
example, you can configure features like [default
bucket encryption](bucket-encryption.md "bucket-encryption.md"), [S3 Versioning](versioning-workflows.md "versioning-workflows.md"),
and [S3 Requester Pays](RequesterPaysBuckets.md "RequesterPaysBuckets.md") in a way that is
customized to the dataset in each bucket. Using one bucket for each distinct dataset,
end user, or team can also help you simplify both your access management and cost
allocation strategies.

A potential drawback to this strategy is that you will need to manage potentially
thousands of buckets. All AWS accounts have a default quota of 10,000 general
purpose buckets. You can increase the bucket quota for an account by submitting a quota
increase request. To request an increase for general purpose buckets, visit the [Service Quotas console](https://console.aws.amazon.com/servicequotas/home/services/s3/quotas/ "https://console.aws.amazon.com/servicequotas/home/services/s3/quotas/").

To manage your bucket-per-use pattern and simplify your infrastructure management, you
can use [AWS CloudFormation](../../../AWSCloudFormation/latest/UserGuide/Welcome.md#welcome-simplify-infrastructure-management "../../../AWSCloudFormation/latest/UserGuide/Welcome.md#welcome-simplify-infrastructure-management"). You can create a custom CloudFormation template for your pattern that
already defines all of your desired settings for your S3 general purpose buckets so that you can easily
deploy and track any changes to your infrastructure. For more information, see [AWS::S3::Bucket](../../../AWSCloudFormation/latest/UserGuide/aws-resource-s3-bucket.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-s3-bucket.md") in the _AWS CloudFormation User Guide_.

![A diagram showing you how you can create a CloudFormation template customized to your application that defines settings for your S3 buckets.](images/create-stack-diagram.png)
