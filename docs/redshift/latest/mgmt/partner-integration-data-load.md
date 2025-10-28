Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Loading data with AWS partners

Aside from integrating a partner with an Amazon Redshift cluster, you can also move data from
more than 30 sources into your Amazon Redshift cluster using our partner's data loading tools.
Before you do so, you must add the partner's IP addresses (found below) to the allowlist
of inbound rules. For more information about adding rules to an Amazon EC2 security group,
see [Authorizing
Inbound Traffic for Your Instances](../../../AWSEC2/latest/UserGuide/authorizing-access-to-an-instance.md "../../../AWSEC2/latest/UserGuide/authorizing-access-to-an-instance.md") in the
_Amazon EC2 User Guide_. Note that while the Informatica Data Loader
tool is free, data ingress charges might apply depending on the data sources and targets
you choose.

You can load data from the following partners:

- [Informatica](https://www.informatica.com/solutions/explore-ecosystems/aws.html "https://www.informatica.com/solutions/explore-ecosystems/aws.html") – [IP
  addresses](https://knowledge.informatica.com/s/article/611041?language=en_US "https://knowledge.informatica.com/s/article/611041?language=en_US")

###### To load data to an Amazon Redshift cluster with a partner

1. Sign in to the AWS Management Console and open the Amazon Redshift console at
   [https://console.aws.amazon.com/redshiftv2/](https://console.aws.amazon.com/redshiftv2/ "https://console.aws.amazon.com/redshiftv2/").
2. On the navigation menu, choose AWS partner integration, then choose the
   partner you want to integrate your cluster with.
3. Choose **Complete <partner-name> integration**. You
   will be redirected to the partner's integration site.
4. Enter the necessary details on the partner's site and complete the
   integration.
