Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Creating a Redshift-managed

VPC endpoint

If you own a cluster or workgroup, or you have been granted access to manage it, you
can create a Redshift-managed VPC endpoint for it.

###### To create a Redshift-managed VPC endpoint

1. Sign in to the AWS Management Console and open the Amazon Redshift console at
   [https://console.aws.amazon.com/redshiftv2/](https://console.aws.amazon.com/redshiftv2/ "https://console.aws.amazon.com/redshiftv2/").
2. On the navigation menu, choose **Configurations**.

The **Configurations** page displays the Redshift-managed VPC
endpoints that have been created. To view details for an endpoint, choose its
name. For Amazon Redshift Serverless, the VPC endpoints are under the **Data
access** tab, when you choose the workgroup. 3. Choose **Create endpoint** to display a form to enter
information about the endpoint to add. 4. Enter values for **Endpoint name**, the 12-digit
**AWS account ID**, the **Virtual private cloud
(VPC)** where the endpoint is located, the
**Subnet** and the **VPC security
group**.

The subnet in **Subnet** defines the subnets and IP addresses
where Amazon Redshift deploys the endpoint. Amazon Redshift chooses a subnet that has IP addresses
available for the network interface associated with the endpoint.

The security group rules in **VPC security group** define the
ports, protocols, and sources for inbound traffic that you are authorizing for
your endpoint. You allow access to the selected port via the security group or
the CIDR range where your workloads run. 5. Choose **Create endpoint** to create the endpoint.
After your endpoint is created, you can access the cluster or workgroup through the
URL shown in **Endpoint** URL in the configuration settings for your
Redshift-managed VPC endpoint.
