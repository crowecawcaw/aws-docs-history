# AOSSEC01-BP01 Launch your OpenSearch Service domains within a Virtual

Private Cloud

Host OpenSearch Service domains in a Virtual Private Cloud (VPC) for
improved security, isolation, and network control.

**Level of risk exposed if this best practice
is not established:** High

**Desired outcome**: Your
organization launches its OpenSearch Service domain within a VPC.

**Benefits of establishing this best
practice:**

- Improved security and isolation of the domain
- Protect network perimeter of your OpenSearch Service domain reducing
  risks of public exposures
- Enhanced ability to control and monitor network traffic

## Implementation guidance

You can launch an OpenSearch Service domain in a VPC. A VPC
is a dedicated virtual network that is logically isolated from
other virtual networks in the AWS Cloud and is specific to your
AWS account. By placing an OpenSearch Service domain within a VPC,
you enable secure communication between OpenSearch Service and
other services within the VPC without requiring an internet
gateway, NAT device, or VPN connection. All traffic remains
securely within the AWS Cloud, with no need for external
connectivity.

When creating an OpenSearch Service domain, you must choose whether it
will have a public endpoint or reside within a VPC. This decision
cannot be changed afterwards, as doing so would require that you
create a new domain and either manually reindex or migrate your
data. However, using a custom snapshot repository can simplify
this process, as you can set up an S3 bucket as a snapshot
repository on both domains and then transfer snapshots between
them. For detailed instructions on implementing custom
repositories, see
[Creating
index snapshots in Amazon OpenSearch Service](../../../opensearch-service/latest/developerguide/managedomains-snapshots.md "../../../opensearch-service/latest/developerguide/managedomains-snapshots.md"),
[Registering
a manual snapshot repository](../../../opensearch-service/latest/developerguide/managedomains-snapshots.md#managedomains-snapshot-registerdirectory "../../../opensearch-service/latest/developerguide/managedomains-snapshots.md#managedomains-snapshot-registerdirectory"), and
[Take
manual snapshots and restore in a different domain spanning across
various Regions and accounts in Amazon OpenSearch Service](https://aws.amazon.com/blogs/big-data/take-manual-snapshots-and-restore-in-a-different-domain-spanning-across-various-regions-and-accounts-in-amazon-opensearch-service/ "https://aws.amazon.com/blogs/big-data/take-manual-snapshots-and-restore-in-a-different-domain-spanning-across-various-regions-and-accounts-in-amazon-opensearch-service/").

### Implementation steps

To create a domain inside a VPC, do the following:

- **Create a VPC:** See
  [Working
  with VPCs](../../../vpc/latest/userguide/working-with-vpcs.md "../../../vpc/latest/userguide/working-with-vpcs.md") in the Amazon VPC User Guide. If you
  already have a VPC, you can skip this step.
- **Reserve IP addresses:**
  OpenSearch Service enables the connection of a VPC to a
  domain by placing network interfaces in a subnet of the VPC.
  Each network interface is associated with an IP address. You
  must reserve a sufficient number of IP addresses in the
  subnet for the network interfaces. For more information,
  see [Reserving
  IP addresses in a VPC subnet](../../../opensearch-service/latest/developerguide/vpc.md#reserving-ip-vpc-endpoints "../../../opensearch-service/latest/developerguide/vpc.md#reserving-ip-vpc-endpoints").
- Navigate to the Amazon OpenSearch Service console.
- To create a new domain, choose **Create domain**.
- In the Network box, select **VPC access - recommended**.
- The IP address type – new option provides a choice between
  having a dual-stack mode, in which IPv6 and IPv4 are enabled
  and your resources can communicate using any of them, or an
  IPv4-only option. We recommend you to use Dual-stack mode -
  recommended option.
- Under the VPC option, choose the VPC you want your
  OpenSearch Service domain to reside in.
- Continue with other options, then review and choose **Create**.

## Resources

- [Launching
  your OpenSearch Service domains within a VPC](../../../opensearch-service/latest/developerguide/vpc.md "../../../opensearch-service/latest/developerguide/vpc.md")
- [Creating
  index snapshots in Amazon OpenSearch Service](../../../opensearch-service/latest/developerguide/managedomains-snapshots.md "../../../opensearch-service/latest/developerguide/managedomains-snapshots.md")
- [Registering
  a manual snapshot repository](../../../opensearch-service/latest/developerguide/managedomains-snapshots.md#managedomains-snapshot-registerdirectory "../../../opensearch-service/latest/developerguide/managedomains-snapshots.md#managedomains-snapshot-registerdirectory")
- [Take
  manual snapshots and restore in a different domain spanning
  across various Regions and accounts in Amazon OpenSearch Service](https://aws.amazon.com/blogs/big-data/take-manual-snapshots-and-restore-in-a-different-domain-spanning-across-various-regions-and-accounts-in-amazon-opensearch-service/ "https://aws.amazon.com/blogs/big-data/take-manual-snapshots-and-restore-in-a-different-domain-spanning-across-various-regions-and-accounts-in-amazon-opensearch-service/")
- [Working
  with VPCs](../../../vpc/latest/userguide/working-with-vpcs.md "../../../vpc/latest/userguide/working-with-vpcs.md")
- [Reserving
  IP addresses in a VPC subnet](../../../opensearch-service/latest/developerguide/vpc.md#reserving-ip-vpc-endpoints "../../../opensearch-service/latest/developerguide/vpc.md#reserving-ip-vpc-endpoints")
