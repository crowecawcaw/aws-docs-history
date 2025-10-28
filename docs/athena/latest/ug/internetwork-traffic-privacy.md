# Internetwork traffic privacy

Traffic is protected both between Athena and on-premises applications and between Athena
and Amazon S3. Traffic between Athena and other services, such as AWS Glue and AWS Key Management Service,
uses HTTPS by default.

- For traffic between Athena and on-premises clients and
  applications, query results that stream to JDBC or ODBC clients are
  encrypted using Transport Layer Security (TLS).

You can use one of the connectivity options between your private network and
AWS:

    + A Site-to-Site VPN AWS VPN connection. For more information, see [What is Site-to-Site VPN AWS VPN](../../../vpn/latest/s2svpn/VPC_VPN.md "../../../vpn/latest/s2svpn/VPC_VPN.md") in the
     *AWS Site-to-Site VPN User Guide*.
    + An AWS Direct Connect connection. For more information, see [What is AWS Direct Connect](../../../directconnect/latest/UserGuide/Welcome.md "../../../directconnect/latest/UserGuide/Welcome.md") in the
     *AWS Direct Connect User Guide*.

- For traffic between Athena and Amazon S3 buckets,
  Transport Layer Security (TLS) encrypts objects in-transit between Athena and
  Amazon S3, and between Athena and customer applications accessing it, you should allow
  only encrypted connections over HTTPS (TLS) using the [`aws:SecureTransport condition`](../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md#Conditions_Boolean "../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md#Conditions_Boolean") on Amazon S3 bucket IAM
  policies. Although Athena currently uses the public endpoint to access data in
  Amazon S3 buckets, this doesn't mean that the data traverses the public internet. All
  traffic between Athena and Amazon S3 is routed over the AWS network and is encrypted
  using TLS.
- Compliance programs – Amazon Athena complies
  with multiple AWS compliance programs, including SOC, PCI, FedRAMP, and
  others. For more information, see [AWS services in scope by compliance
  program](https://aws.amazon.com/compliance/services-in-scope/ "https://aws.amazon.com/compliance/services-in-scope/").
