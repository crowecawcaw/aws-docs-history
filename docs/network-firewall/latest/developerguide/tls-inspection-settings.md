# TLS inspection configuration settings in AWS Network Firewall

When you configure TLS inspection configuration you provide the following settings.

- **Name** – The identifier for the TLS inspection configuration. You
  assign a unique name to every TLS inspection configuration. You can't change the name of a
  TLS inspection configuration after you create it.
- **Description** – Optional additional
  information about the TLS inspection configuration. Fill in information that might help you to remember
  the purpose of the TLS inspection configuration and how you want to use it. The description is included
  in TLS inspection configuration lists in the console and the APIs.
- **Associate SSL/TLS certificates** – The
  certificates to associate with the TLS inspection configuration for inbound and outbound inspection.
  Network Firewall uses certificates to decrypt and re-encrypt the SSL/TLS traffic that's
  going to your firewall.
- **Define scope** – Defines the scope of
  the traffic to decrypt based on source and destination addresses and port ranges
  in a scope configuration. For each scope configuration that you add, Network Firewall adds
  a mirrored scope configuration with reverse sources and destinations when it
  creates the TLS inspection configuration. This allows Network Firewall to
  decrypt—and subsequently inspect—traffic in both directions, which
  is required for TLS termination.
- **Customer managed key** (Optional) – Network Firewall
  encrypts and decrypts the TLS inspection configuration, to protect against unauthorized access. By
  default, Network Firewall uses AWS owned keys for this. If you want to use your own
  keys, you can configure customer managed keys from AWS Key Management Service and provide them to Network Firewall.
  For information about this option, see [Encryption at rest with AWS Key Management Service](kms-encryption-at-rest.md "kms-encryption-at-rest.md").
- **Certificate revocation status** (Optional)
  – Network Firewall checks if the certificate that's presented by the server in the
  TLS session is revoked or has an unknown status. If this is turned on, Network Firewall
  handles the outbound traffic based on the actions that you configure in the
  certificate revocation check.
- **Tags** – A tag is an optional label that
  you assign to an AWS resource. You can use tags to search and filter your
  resources and to track your AWS costs. For more information about tags, see
  [Tagging AWS Network Firewall resources](tagging.md "tagging.md").
