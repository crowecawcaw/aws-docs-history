After careful consideration, we decided to end support for Amazon FinSpace, effective October 7, 2026. Amazon FinSpace will no longer accept new customers beginning October 7, 2025. As an existing customer with an Amazon FinSpace environment created before October 7, 2025, you can continue to use the service as normal. After October 7, 2026, you will no longer be able to use Amazon FinSpace. For more information, see
[Amazon FinSpace end of support](amazon-finspace-end-of-support.md "amazon-finspace-end-of-support.md").

# Validating your VPC connection

###### Important

Amazon FinSpace Dataset Browser will be discontinued on `March 26,
 2025`. Starting `November 29, 2023`, FinSpace will no longer accept the creation of new Dataset Browser
environments. Customers using [Amazon FinSpace with Managed Kdb Insights](https://aws.amazon.com/finspace/features/managed-kdb-insights/ "https://aws.amazon.com/finspace/features/managed-kdb-insights/") will not be affected. For more information, review the [FAQ](https://aws.amazon.com/finspace/faqs/ "https://aws.amazon.com/finspace/faqs/") or contact [AWS Support](https://aws.amazon.com/contact-us/ "https://aws.amazon.com/contact-us/") to assist with your
transition.

After your connection is set up, you can test connectivity to your network. There are
two types of connectivity testing available.

- Basic testing – You can use the `curl` command in the SageMaker AI
  Studio notebook environment that is included with FinSpace for basic testing.
- Advanced testing – You can use the file upload capability in the SageMaker AI
  Studio notebook to upload your own network diagnostic utilities to test.

## Basic connectivity testing using Amazon FinSpace

notebooks

If you're testing connectivity to an HTTP/HTTPS endpoint, you can use a FinSpace
notebook to test basic connectivity using curl.

###### To validate the connection using a notebook

1. Sign in to the FinSpace web application. For more information, see [Signing in to the Amazon FinSpace web application](signing-into-amazon-finspace.md "signing-into-amazon-finspace.md").
2. Open a FinSpace notebook. For more information, see [Opening the notebook environment](opening-the-notebook-environment.md "opening-the-notebook-environment.md").
3. From the notebook menu bar, choose the plus (+) icon to create a new cell.
   In the cell, run the `curl` command in the shell to test
   connectivity to the host.

`%local`

`!curl <hostname or URL>`

For example, run the following command:

`%local`

`!curl www.google.com`

###### Tip

Keep your cursor in the cell and choose the (>) arrow button from the
notebook menu to run the command.

If successful, the results of the `curl` command display in your
notebook.

###### Note

After the VPC connectivity is set up for the environment, the internet
connection is disabled by default. This is the default unless you have an explicit
static route entry in your transit gateway route table that specifies forwarding
all traffic `0.0.0.0/0` to your VPC attachment that has an internet
gateway.

## Configuring internet access

###### To ensure FinSpace can connect to your internet gateway

1. Check that your transit gateway attachment has a private subnet and public
   subnet with a NAT gateway. The private subnet should be attached to the transit
   gateway attachment.
2. Check that the VPC attachment has all Availability Zones (AZ) included in
   the FinSpace response.
3. Add a route for private subnets for directing traffic destined to
   `100.64.0.0/26` to the dedicated account VPC attachment.
4. Create a transit gateway static route to direct traffic destined to
   `0.0.0.0/0` to the customer account attachment. For more
   information, see [Create a
   static route](../../../vpc/latest/tgw/tgw-route-tables.md#tgw-create-static-route "../../../vpc/latest/tgw/tgw-route-tables.md#tgw-create-static-route") in the _AWS Transit Gateway User
   Guide_.

Wait a few minutes before running the next command because there might be a
delay before the routes are installed.
