# Creating a CIDR

collection with CIDR locations and blocks

To get started, create a CIDR collection and add CIDR blocks and locations to it.

###### To create a CIDR collection

using the Route 53 console

1. Sign in to the AWS Management Console and open the Route 53 console at
   [https://console.aws.amazon.com/route53/](https://console.aws.amazon.com/route53/ "https://console.aws.amazon.com/route53/").
2. In the navigation pane, choose **IP-based routing**, and then
   **CIDR collections**.
3. Select **Create CIDR collection**.
4. In the **Create CIDR collection** pane, under
   **Details**, enter a name for the
   collection.
5. Choose **Create collection** to create an empty
   collection.

- or -

In the **Create CIDR locations** section, enter a name for the CIDR
location in the **CIDR location** box. The location name can be any identifying string, for example
`company 1`, or
`Seattle`. It doesn't have to be an actual
geographic location.

###### Important

The CIDR location name has a maximum length of 16 characters.

Enter the
CIDR blocks in the **CIDR blocks** box one per line.
These can be IPv4 or IPv6 addresses ranging from /0 to /24 for IPv4 and
/0 to /48 for IPv6. 6. After you have entered the CIDR blocks, choose **Create CIDR
collection**, or **Add another location**
to keep entering locations and CIDR block. You can enter multiple CIDR
locations per collection. 7. After you have entered CIDR locations, choose **Create CIDR
collection**.
