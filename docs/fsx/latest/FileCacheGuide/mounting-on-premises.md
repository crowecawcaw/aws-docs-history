# Mounting caches from on-premises or

a peered Amazon VPC

You can access your cache in two ways. One is from Amazon EC2 instances located in an Amazon VPC
that's peered to the cache's VPC. The other is from on-premises clients that are connected to
your cache's VPC using Direct Connect or VPN.

Connect the client's VPC and your Amazon File Cache's VPC using either a VPC peering
connection or a VPC transit gateway. When you use either option, Amazon EC2 instances that are in
one VPC can access caches in another VPC, even if the VPCs belong to different
accounts.

Before using the following the procedure, you must set up either a VPC peering connection
or a VPC transit gateway.

A _transit gateway_ is a network transit hub that you can
use to interconnect your VPCs and on-premises networks. For more information about using VPC
transit gateways, see [Getting Started with
Transit Gateways](../../../vpc/latest/tgw/tgw-getting-started.md "../../../vpc/latest/tgw/tgw-getting-started.md") in the _Amazon VPC Transit Gateways
Guide_.

A _VPC peering connection_ is a networking connection
between two VPCs. This type of connection enables you to route traffic between them using
private Internet Protocol version 4 (IPv4) or Internet Protocol version 6 (IPv6) addresses.
You can use VPC peering to connect VPCs within the same AWS Region or between AWS
RegionsAWS Regions. For more information about VPC peering, see [What is VPC Peering?](../../../vpc/latest/peering/Welcome.md "../../../vpc/latest/peering/Welcome.md") in the _Amazon VPC Peering Guide_.

You can mount your cache from outside its VPC using the IP address of its primary network
interface. The primary network interface is the first network interface returned when you run
the `aws fsx describe-file-caches` AWS Command Line Interface (AWS CLI) command. You can also get this
IP address from the AWS Management Console.

###### To retrieve the IP address of the primary network interface for a cache

1. Open the AWS console at [https://console.aws.amazon.com/fsx/](https://console.aws.amazon.com/fsx/ "https://console.aws.amazon.com/fsx/").
2. In the navigation pane, choose **Caches**.
3. Choose your cache from the dashboard.
4. From the **Summary** details page, choose **Network &
   security**.
5. For **Network interface**, choose the ID for your primary elastic
   network interface. This takes you to the Amazon EC2 console.
6. On the **Details** tab, find the **Primary private IPv4 IP**. This is the IP address for your primary
   network interface.

###### Note

You can't use Domain Name System (DNS) name resolution when mounting an
Amazon File Cache resource from outside the VPC it's associated with.
