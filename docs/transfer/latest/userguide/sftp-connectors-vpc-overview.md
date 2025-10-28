# VPC connectivity for SFTP connectors

AWS Transfer Family SFTP connectors support connectivity to remote SFTP servers through your VPC
environments using Amazon VPC Lattice. This enables you to connect with privately hosted SFTP
servers or route internet traffic through your VPC's security controls, and use your own NAT
gateways and Elastic IP addresses.

**Egress types**

SFTP connectors can use one of two egress types:

- **Service Managed** (default): The connector uses NAT
  gateways and IP addresses owned by AWS Transfer Family to route connections over the public
  internet.
- **VPC_LATTICE**: The connector routes traffic through
  your VPC environment using Cross-VPC Resource Access.
  **When to use VPC connectivity**

Use VPC connectivity for SFTP connectors in these scenarios:

- **Private SFTP servers**: Connect to SFTP servers
  that are only accessible from your VPC.
- **On-premises connectivity**: Connect to on-premises
  SFTP servers through AWS Direct Connect or AWS Site-to-Site VPN
  connections.
- **Custom IP addresses**: Use your own NAT gateways
  and Elastic IP addresses, including BYOIP scenarios.
- **Centralized security controls**: Route file
  transfers through your organization's central ingress/egress controls.
  **Requirements**

Before creating a VPC_LATTICE-enabled SFTP connector, you need:

- VPC and related infrastructure (subnets, route tables, security groups)
- Resource Gateway in your VPC (minimum two Availability Zones)
- Resource Configuration specifying the target SFTP server
  For detailed setup instructions, see [Create a VPC_LATTICE-enabled SFTP
  connector](create-vpc-sftp-connector-procedure.md#create-vpc-connector-procedure "create-vpc-sftp-connector-procedure.md#create-vpc-connector-procedure"). And, for examples, see [VPC connectivity examples for SFTP
  connectors](create-vpc-sftp-connector-procedure.md#sftp-connectors-vpc-examples "create-vpc-sftp-connector-procedure.md#sftp-connectors-vpc-examples").
