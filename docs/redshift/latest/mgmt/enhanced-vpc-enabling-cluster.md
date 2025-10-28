Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Turning on enhanced VPC routing

You can turn on enhanced VPC routing when you create or modify a cluster, and when you create or modify a Amazon Redshift Serverless workgroup.

To work with enhanced VPC routing, your cluster or Serverless workgroup must meet the following requirements
and constraints:

- Your cluster must be in a VPC.

If you attach an Amazon S3 VPC endpoint, the VPC endpoint is used only
for access to Amazon S3 buckets in the same AWS Region. To access buckets in another
AWS Region (not using the VPC endpoint) or to access other AWS services, make
your cluster or Serverless workgroup publicly accessible or use a [network address translation (NAT)
gateway](../../../vpc/latest/userguide/vpc-nat-gateway.md "../../../vpc/latest/userguide/vpc-nat-gateway.md"). For more information, see [Creating a Redshift provisioned
cluster or Amazon Redshift Serverless workgroup in a VPC](getting-started-cluster-in-vpc.md "getting-started-cluster-in-vpc.md").

- You must enable Domain Name Service (DNS) resolution in your VPC.
  Alternatively, if you're using your own DNS server, make sure that DNS requests
  to Amazon S3 are resolved correctly to the IP addresses that are maintained by AWS.
  For more information, see [Using DNS with
  Your VPC](../../../vpc/latest/userguide/vpc-dns.md "../../../vpc/latest/userguide/vpc-dns.md") in the _Amazon VPC User Guide._
- DNS hostnames must be enabled in your VPC. DNS hostnames are enabled by
  default.
- Your VPC endpoint policies must allow access to any Amazon S3 buckets used with
  COPY, UNLOAD, or CREATE LIBRARY calls in Amazon Redshift, including access to any manifest
  files involved. For COPY from remote hosts, your endpoint policies must allow
  access to each host machine. For more information, see [IAM Permissions for COPY, UNLOAD, and CREATE LIBRARY](../dg/copy-usage_notes-access-permissions.md#copy-usage_notes-iam-permissions "../dg/copy-usage_notes-access-permissions.md#copy-usage_notes-iam-permissions") in the
  _Amazon Redshift Database Developer Guide._

###### To turn on enhanced VPC routing for a provisioned cluster

1. Sign in to the AWS Management Console and open the Amazon Redshift console at
   [https://console.aws.amazon.com/redshiftv2/](https://console.aws.amazon.com/redshiftv2/ "https://console.aws.amazon.com/redshiftv2/").
2. On the navigation menu, choose **Provisioned clusters dashboard**, then choose **Create cluster** and enter the
   **Cluster details** properties.
3. To display the **Additional configurations** section, choose to switch off **Use defaults**.
4. Navigate to the **Network and security** section.
5. To turn on **Enhanced VPC routing**, choose **Turn on** to force cluster traffic through the VPC.
6. Choose **Create cluster** to create the cluster. The
   cluster might take several minutes to be ready to use.

###### To turn on enhanced VPC routing for an Amazon Redshift Serverless

1. Sign in to the AWS Management Console and open the Amazon Redshift console at
   [https://console.aws.amazon.com/redshiftv2/](https://console.aws.amazon.com/redshiftv2/ "https://console.aws.amazon.com/redshiftv2/").
2. On the navigation menu, choose **Serverless dashboard**, then choose **Create workgroup** and enter the
   properties for your workgroup.
3. Navigate to the **Network and security** section.
4. Select **Turn on enhanced VPC routing** to route network traffic through the VPC.
5. Choose **Next** and finish entering your workgroup properties until you **Create** the workgroup.
