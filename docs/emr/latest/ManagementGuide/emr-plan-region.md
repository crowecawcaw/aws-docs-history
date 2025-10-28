# Choose an AWS Region for your Amazon EMR cluster

Amazon Web Services run on servers in data centers around the world. Data centers are organized by
geographical Region. When you launch an Amazon EMR cluster, you must specify a
Region. You might choose a Region to reduce latency,
minimize costs, or address regulatory requirements. For the list of Regions
and endpoints supported by Amazon EMR, see [Regions and endpoints](../../../general/latest/gr.md#emr_region "../../../general/latest/gr.md#emr_region") in the
_Amazon Web Services General Reference_.

For best performance, you should launch the cluster in the same Region as
your data. For example, if the Amazon S3 bucket storing your input data is in the US West (Oregon) Region,
you should launch your cluster in the US West (Oregon) Region to avoid cross-Region
data transfer fees. If you use an Amazon S3 bucket to receive the output of the cluster, you
would also want to create it in the US West (Oregon) Region.

If you plan to associate an Amazon EC2 key pair with the cluster (required for using SSH to log on
to the master node), the key pair must be created in the same Region as the
cluster. Similarly, the security groups that Amazon EMR creates to manage the cluster are created
in the same Region as the cluster.

If you signed up for an AWS account on or after May 17, 2017,
the default Region when you access a resource from the AWS Management Console
is US East (Ohio) (us-east-2); for older accounts, the default Region
is either US West (Oregon) (us-west-2) or US East (N. Virginia) (us-east-1). For more information, see
[Regions and Endpoints](../../../general/latest/gr/rande.md "../../../general/latest/gr/rande.md").

Some AWS features are available only in limited Regions. For example,
Cluster Compute instances are available only in the US East (N. Virginia) Region, and the
Asia Pacific (Sydney) Region supports only Hadoop 1.0.3 and later. When choosing a
Region, check that it supports the features you want to use.

For best performance, use the same Region for all of your AWS resources
that will be used with the cluster. The following table maps the Region
names between services. For a list of Amazon EMR Regions, see [AWS Regions and endpoints](../../../general/latest/gr/rande.md#emr_region "../../../general/latest/gr/rande.md#emr_region") in the
_Amazon Web Services General Reference_.

## Choose a Region with the

console

Your default Region is displayed to the left of your account information
on the navigation bar. To switch Regions in both the new and old
consoles, choose the Region dropdown menu and select a new
option.

## Specify a Region with the AWS CLI

Specify a default Region in the AWS CLI using either the **aws
configure** command or the `AWS_DEFAULT_REGION` environment
variable. For more information, see [Configuring the AWS Region](../../../cli/latest/userguide/cli-chap-getting-started.md#cli-installing-specifying-region "../../../cli/latest/userguide/cli-chap-getting-started.md#cli-installing-specifying-region") in the
_AWS Command Line Interface User Guide_.

## Choose a Region with an SDK or the

API

To choose a Region using an SDK, configure your application to use that
Region's endpoint. If you are creating a client application using an
AWS SDK, you can change the client endpoint by calling `setEndpoint`, as
shown in the following example:

```
client.setEndpoint("elasticmapreduce.us-west-2.amazonaws.com");
```

After your application has specified a Region by setting the endpoint, you
can set the Availability Zone for your cluster's EC2 instances. Availability Zones are
distinct geographical locations that are engineered to be insulated from failures in
other Availability Zones and provide inexpensive, low latency network connectivity to
other Availability Zones in the same Region. A Region
contains one or more Availability Zones. To optimize performance and reduce latency, all
resources should be located in the same Availability Zone as the cluster that uses them.
