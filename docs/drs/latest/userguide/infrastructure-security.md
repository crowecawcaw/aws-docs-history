# Infrastructure security in AWS Elastic Disaster Recovery

As a managed service, AWS Elastic Disaster Recovery is protected by the AWS global network security
procedures that are described in the [Amazon Web Services: Overview of Security Processes](https://d0.awsstatic.com/whitepapers/Security/AWS_Security_Whitepaper.pdf "https://d0.awsstatic.com/whitepapers/Security/AWS_Security_Whitepaper.pdf") whitepaper.

You use AWS published API calls to access application recovery Service through the
network. Clients must support Transport Layer Security (TLS) 1.2 or later. Clients must
also support cipher suites with perfect forward secrecy (PFS) such as Ephemeral
Diffie-Hellman (DHE) or Elliptic Curve Ephemeral Diffie-Hellman (ECDHE). Most modern
systems such as Java 7 and later support these modes.

All parties involved in the communication authenticate each other using TLS, IAM
policies and tokens. The communication between the Agents and the replication server are
based on TLS 1.2 only with the highest standard of cipher suite (PFS, ECDHE). Requests
between the agent and AWS Elastic Disaster Recovery as well as between the replication server and AWS Elastic Disaster Recovery
are signed using an access key ID and a secret access key that is associated with an IAM
principal.

Additionally, requests must be signed using an access key ID and a secret access key that
is associated with an IAM principal. Or you can use the
[AWS Security Token Service](../../../STS/latest/APIReference/Welcome.md "../../../STS/latest/APIReference/Welcome.md")
(AWS STS) to generate
temporary security credentials to sign requests.

AWS Elastic Disaster Recovery customers must ensure that they manually delete their access keys after
installing the AWS Replication Agent and successful recovery. AWS does not delete these
keys automatically. AWS Elastic Disaster Recovery does delete the keys from source servers after they are
disconnected from the service. If you want your keys to automatically stop working at a
certain date after you have finished using them so that you do not have to worry about
manually deleting them, you can do so though the [IAM permissions boundary](../../../IAM/latest/UserGuide/access_policies_boundaries.md "../../../IAM/latest/UserGuide/access_policies_boundaries.md") and the [aws:CurrentTime global context key](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-currenttime "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-currenttime").

AWS Elastic Disaster Recovery customers should use [Amazon
EBS encryption.](../../../AWSEC2/latest/UserGuide/EBSEncryption.md "../../../AWSEC2/latest/UserGuide/EBSEncryption.md")

AWS Elastic Disaster Recovery customers should secure their replication servers by reducing their exposure
to the public internet. This can be done through:

1. Using Security Groups to only allow permitted IP addresses to connect to the
   replication servers. [Learn more about Security Groups.](../../../vpc/latest/userguide/VPC_SecurityGroups.md "../../../vpc/latest/userguide/VPC_SecurityGroups.md")
2. Using a VPN to connect to the replication servers, such as the AWS
   site-to-site VPN. [Learn more
   about the AWS Site-to-site VPN.](../../../vpn/latest/s2svpn/VPC_VPN.md "../../../vpn/latest/s2svpn/VPC_VPN.md")
   AWS Elastic Disaster Recovery creates and uses the "aws-replication" user within the Source server. The
   AWS Elastic Disaster Recovery replication server and AWS Replication Agent run under this user. Although
   this is not a root user, this user needs to be part of the disk group that grants this user
   full read and write permissions to block devices.

###### Note

AWS Elastic Disaster Recovery only uses these permissions to read from block devices.

AWS Elastic Disaster Recovery customers should only grant access to the AWS Elastic Disaster Recovery Failback Client to
trusted administrators in order to prevent unauthorized entities from gaining access to
your systems through the client.

## AWS GovCloud

AWS GovCloud (US) are isolated AWS Regions designed to allow U.S. government agencies and customers
to move sensitive workloads into [the cloud](https://aws.amazon.com/what-is-cloud-computing/ "https://aws.amazon.com/what-is-cloud-computing/").

- AWS GovCloud (US) uses FIPS 140-2 approved cryptographic modules for all AWS service API
  endpoints, unless otherwise indicated in the [Service Endpoints](../../../govcloud-us/latest/UserGuide/using-govcloud-endpoints.md "../../../govcloud-us/latest/UserGuide/using-govcloud-endpoints.md") section.
- AWS GovCloud (US) is appropriate for all types of Controlled Unclassified Information (CUI)
  and unclassified data. For more details, see
  [Maintaining U.S. International Traffic in Arms Regulations (ITAR) Compliance](../../../govcloud-us/latest/UserGuide/govcloud-itar.md "../../../govcloud-us/latest/UserGuide/govcloud-itar.md") .
- The AWS GovCloud (US) Regions are physically isolated and have logical network isolation
  from all other AWS Regions.
- AWS restricts all physical and logical access for those staff supporting AWS GovCloud (US)
  to US Citizens. AWS allows only vetted U.S. citizens with distinct access controls separate
  from other AWS Regions to administer AWS GovCloud (US). Any customer data fields that are
  defined as outside of the ITAR boundary (such as S3 bucket names) are explicitly documented
  in the service-specific section as not permitted to contain export-controlled data.
- AWS GovCloud (US) authentication is completely isolated from commercial regions.
