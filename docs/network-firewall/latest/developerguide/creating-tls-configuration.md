# Creating a TLS inspection configuration

in Network Firewall

This procedure explains how to create a TLS inspection configuration using Network Firewall. To follow this procedure,
you must have at least one certificate in AWS Certificate Manager (ACM) that's accessible by
your AWS account.

###### To create a TLS inspection configuration using the console

1. Sign in to the AWS Management Console and open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the navigation pane, under **Network Firewall**, choose **TLS inspection configurations**.
3. Choose **Create TLS inspection configuration**.
4. In the **Associate SSL/TLS certificates** page, configure **Server certificates for inbound SSL/TLS inspection**, **CA certificate for outbound SSL/TLS inspection**, or both.
5. Choose **Next** to go to the TLS inspection configuration's **Describe TLS inspection configuration** page.
6. Enter a **Name** to identify this TLS inspection configuration.

###### Warning

You can't change the name after you create the TLS inspection configuration. 7. (Optional) Enter a **Description** for the TLS inspection configuration. 8. Choose **Next** to go to the TLS inspection configuration's **Define scope** page. 9. In
the **Scope configuration** pane, choose the protocol,
source, source port range, destination, and destination port range of the
traffic that you want Network Firewall to decrypt. Network Firewall uses the
associated certificates to decrypt the SSL/TLS traffic that matches the
scope configuration. After Network Firewall decrypts the traffic, the service inspects
the traffic according to your firewall policy's stateful rules.

Network Firewall also automatically configures a reverse scope, ensuring that the service inspects the
traffic in both directions.

    1. For **Protocol**, choose the protocol to decrypt.
     Network Firewall currently supports TCP.
    2. For **Source IP**, choose the source IP addresses and
     ranges to decrypt. You can decrypt by **Custom** IP
     addresses or by **Any IPv4 address**.
    3. For **Source port**, choose the source ports and
     source port ranges to decrypt. You can decrypt by
     **Custom** port ranges or by **Any
     port**.
    4. For **Destination IP**, choose the destination IP
     addresses and ranges to decrypt. You can decrypt by
     **Custom** IP addresses or by **Any
     IPv4 address**.
    5. For **Destination port**, choose the destination
     ports and destination port ranges to decrypt. You can decrypt by
     **Custom** port ranges or by **Any
     port**.
    6. Choose **Add scope configuration**. To add more scope configurations, adjust the settings in the **scope configuration** pane, then select **Add scope configuration**.

10. Choose **Next**.
11. (Optional) On the **Advanced settings** page, under **Customer
    managed key**, you can change the key that Network Firewall uses to
    decrypt and encrypt the TLS inspection configuration, to protect against unauthorized access. By
    default, Network Firewall uses AWS owned keys. If you want to use your own keys, you
    can configure customer managed keys from the AWS Key Management Service and provide them to Network Firewall. For
    information about customer managed keys, see [Encryption at rest with AWS Key Management Service](kms-encryption-at-rest.md "kms-encryption-at-rest.md").
12. (Optional) In the **Certificate revocation status** section, choose whether
    Network Firewall should check if the certificate that's presented by the server in the
    TLS connection has a revoked status. To enable this option, you must first
    associate a certificate authority (CA) certificate for outbound inspection
    in the **Associate SSL/TLS certificates** step. You can
    also configure the actions that Network Firewall takes on outbound traffic if the
    certificate is revoked or has an unknown status.
13. Choose **Next**.
14. (Optional) On the **Add tags** page, enter a key and optional value for any
    tag that you want to add to this TLS inspection configuration. Tags help you to organize and manage
    your AWS resources. For more information about tagging your resources, see
    [Tagging AWS Network Firewall resources](tagging.md "tagging.md").
15. Choose **Next**.
16. On the **Review and confirm** page, check the TLS inspection configuration settings.
    If you want to change anything, choose **Edit** for that
    section. This returns you to the corresponding step in the create TLS inspection configuration
    wizard. Make your changes, then choose **Next** on each
    page until you come back to the review and confirm page.
17. Choose **Create TLS inspection configuration**.
    Your new TLS inspection configuration is added to the list in the Network Firewall TLS inspection configurations page.

If you've configured the inspection for certificate revocation checks on outbound traffic,
you can log failures for these checks by enabling TLS logging. For information,
see [Logging network traffic](firewall-logging.md "firewall-logging.md").

To use your TLS inspection configuration in a firewall policy, follow the procedures at [Managing your firewall policy](firewall-policy-managing.md "firewall-policy-managing.md").
