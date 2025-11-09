# Creating SFTP connectors

This topic describes how to create SFTP connectors. Each connector provides the
ability to connect with one remote SFTP server. You perform the following high-level
tasks to configure an SFTP connector.

###### Note

For VPC-based connectors that route traffic through your Virtual Private Cloud,
see [Create an SFTP connector with
VPC-based egress](create-vpc-sftp-connector-procedure.md "create-vpc-sftp-connector-procedure.md").

1. Store the authentication credentials for the connector in AWS Secrets Manager.
2. Create the connector, by specifying the secret ARN, the remote server's URL or
   Resource Configuration ARN, the security policy containing the algorithms that
   will be supported by the connector, and other configuration settings.
3. After you create the connector, you can test it to ensure that it can
   establish connections with the remote SFTP server.

## Choosing SFTP connector egress type

When you create a SFTP connector, you choose the Egress Type between "Service
managed" and "VPC Lattice".

- **Service managed** (default): The connector
  uses NAT gateways and IP addresses owned by AWS Transfer Family to route connections
  over the public internet. The service provides 3 static IP addresses for
  your connectors that need to be allowlisted on the remote servers to
  establish connections.
- **VPC Lattice**: The connector routes traffic
  through your VPC environment using Amazon VPC Lattice. Use VPC connectivity for
  SFTP connectors in these scenarios:
  - **Private SFTP servers**: Connect to
    SFTP servers that are only accessible from your VPC
  - **On-premises connectivity**: Connect
    to on-premises SFTP servers through AWS Direct Connect or AWS Virtual Private Network
    connections
  - **Custom IP addresses**: Present your
    own NAT gateways and Elastic IP addresses to the remote
    server
  - **Centralized security controls**:
    Route file transfers through your organization's central
    ingress/egress controls

The following matrix helps you choose the right connector type for your
use-cases.

| SFTP Connector Egress Type matrix                                                     | Capability                                                                       | Egress Type = Service managed                                                          | Egress Type = VPC Lattice |
| ------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | ------------------------- |
| Connectivity to Publicly hosted (internet-accessible) SFTP<br>servers                 | Supported                                                                        | Supported1                                                                             |
| Connectivity to Privately hosted (on-premises) SFTP<br>servers                        | Not supported                                                                    | Supported2                                                                             |
| Connectivity to Privately hosted (in-VPC) SFTP servers                                | Not supported                                                                    | Supported                                                                              |
| Static IP addresses presented to remote SFTP server                                   | Supported via service supplied static IP addresses                               | Supported via customer owned static IP addresses                                       |
| Bandwidth available                                                                   | 50 MBPS per account                                                              | Higher bandwidth, as available from customer owned Resource<br>Gateway and NAT Gateway |
| Traffic routing to internet over customer-owned NAT Gateways and<br>Network Firewalls | Not supported. NAT Gateways are owned and managed by Transfer Family<br>service. | Supported                                                                              |

1
_With Egress Type = VPC Lattice, connectivity to publicly hosted servers is
supported using the egress infrastructure (NAT Gateways) setup in your egress
VPCs._

2
_With Egress Type = VPC Lattice, connectivity to privately hosted servers is
supported using existing networks in your VPC, such as AWS Direct Connect or
VPN._

###### Topics

- [Store authentication credentials
  for SFTP connectors in Secrets Manager](sftp-connector-secret-procedure.md "sftp-connector-secret-procedure.md")
- [Create an SFTP connector with
  service-managed egress](create-sftp-connector-procedure.md "create-sftp-connector-procedure.md")
- [Create an SFTP connector with
  VPC-based egress](create-vpc-sftp-connector-procedure.md "create-vpc-sftp-connector-procedure.md")
- [Test an SFTP connector](test-sftp-connector.md "test-sftp-connector.md")
