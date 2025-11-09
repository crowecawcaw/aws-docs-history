# AWS Transfer Family for AS2

Applicability Statement 2 (AS2) is an RFC-defined file-transmission specification that
includes strong message protection and verification mechanisms. Protecting an AS2 payload in
transit uses Cryptographic Message Syntax (CMS) with encryption and digital signatures to
provide data protection and peer authentication. A signed Message Disposition Notice (MDN)
response payload provides verification (non-repudiation) that a message was received and
successfully decrypted.

The AS2 protocol is critical for workflows with compliance requirements that rely on
having data protection and security features built into the protocol. AWS Transfer Family AS2 endpoints
are [Drummond certified](https://aws.amazon.com/about-aws/whats-new/2023/06/aws-transfer-family-drummond-group-as2-certification/ "https://aws.amazon.com/about-aws/whats-new/2023/06/aws-transfer-family-drummond-group-as2-certification/"), enabling customers in industries such as retail, life
sciences, manufacturing, financial services, and utilities to securely transact with their
business partners.

When you use AS2 with Transfer Family, the transacted data is natively accessible in AWS
for:

- Processing, analysis, and machine learning
- Integration with enterprise resource planning (ERP) systems
- Integration with customer relationship management (CRM) systems
  To exchange files with a partner who has an AS2-enabled server, you must:

- Generate a public-private key pair for encryption
- Generate a public-private key pair for signing
- Exchange the public keys with your partner

###### Important

HTTPS AS2 server endpoints are not currently supported. You are responsible for TLS
termination.

Transfer Family provides a workshop that you can attend, in which you can
configure a Transfer Family endpoint with AS2 enabled, and a Transfer Family AS2 connector.
You can view the details for this workshop
[here](https://catalog.workshops.aws/transfer-family-as2/en-US "https://catalog.workshops.aws/transfer-family-as2/en-US").

For step-by-step instructions to configure AS2 in Transfer Family, see the following:

1. [Import AS2 certificates](managing-as2-partners.md#configure-as2-certificate "managing-as2-partners.md#configure-as2-certificate")
2. [Create AS2 profiles](configure-as2-profile.md "configure-as2-profile.md")
3. [Create an AS2 server](create-as2-transfer-server.md "create-as2-transfer-server.md")
4. [Create an AS2 agreement](create-as2-transfer-server.md#as2-agreements "create-as2-transfer-server.md#as2-agreements")
5. [Configure AS2 connectors](configure-as2-connector.md "configure-as2-connector.md")
   For a complete example, see [Setting up an AS2 configuration](as2-example-tutorial.md "as2-example-tutorial.md").

###### Note

To show support for AS2 Terraform templates, add a thumbs up reaction (👍) to the
[Transfer Family
Terraform templates feature request](https://github.com/aws-ia/terraform-aws-transfer-family/issues/62#issue-3364703944 "https://github.com/aws-ia/terraform-aws-transfer-family/issues/62#issue-3364703944"). You can also add a comment describing your use case.

## AS2 use cases

If you are an AWS Transfer Family customer who wants to exchange files with a partner who has an
AS2-enabled server, the most complex part of the setup involves generating one
public-private key pair for encryption and another for signing and exchanging the public
keys with the partner.

![Diagram that shows the use of public-private key pairs for encryption and signing.](images/as2-architecture-high-level.png)

Consider the following variations for using AWS Transfer Family with AS2.

###### Note

_Trading partner_ is the partner associated with that partner
profile.

All mentions of _MDN_ in the following table assume
_signed_ MDNs.

AS2 use cases| Inbound-only use cases<br>• Transfer encrypted AS2 messages from<br>a trading partner to a Transfer Family server.<br>In this case, you do the following:<br>1. Create profiles for your trading partner and<br>yourself.<br>2. Create a Transfer Family server that uses the AS2<br>protocol.<br>3. Create an agreement and add it to your<br>server.<br>4. Import a certificate with a private key and add it<br>to your profile, and then import the public key to<br>your partner profile for encryption.<br>5. After you have these items, send the public key<br>for your certificate to your trading partner.<br>Now your partner can send you encrypted messages and you<br>can decrypt them and store them in your Amazon S3 bucket.<br>• Transfer encrypted AS2 messages from<br>a trading partner to a Transfer Family server and add<br>signing.<br>In this scenario, you are still doing only inbound<br>transfers, but now you want to have your partner sign the<br>messages that they send. In this case, import the trading<br>partner's signing public key (as a signing certificate added<br>to your partner's profile).<br>• Transfer encrypted AS2 messages from<br>a trading partner to a Transfer Family server and add signing and<br>sending an MDN response.<br>In this scenario, you are still doing only inbound<br>transfers, but now, in addition to receiving signed<br>payloads, your trading partner wants to receive a signed MDN<br>response.<br>1. Import your public and private signing keys (as a<br>signing certificate to your profile).<br>2. Send the public signing key to your trading<br>partner. |
| Outbound-only use cases<br>• Transfer encrypted AS2 messages from<br>a Transfer Family server to a trading partner.<br>This case is similar to the inbound-only transfer use<br>case, except that instead of adding an agreement to your AS2<br>server, you create a connector. In this case, you import<br>your trading partner's public key to their profile.<br>• Transfer encrypted AS2 messages from<br>a Transfer Family server to a trading partner and add<br>signing.<br>You are still doing only outbound transfers, but now your<br>trading partner wants you to sign the message that you send<br>to them.<br>1. Import your signing private key (as a signing<br>certificate added to your profile).<br>2. Send your trading partner your public key.<br>• Transfer encrypted AS2 messages from<br>a Transfer Family server to a trading partner and add signing and<br>send an MDN response.<br>You are still doing only outbound transfers, but now, in<br>addition to sending signed payloads, you want to receive a<br>signed MDN response from your trading partner.<br>1. Your trading partner sends you their public<br>signing key.<br>2. Import your trading partner's public key (as a<br>signing certificate added to your partner<br>profile). |
| Inbound and outbound use cases<br>• Transfer encrypted AS2 messages in<br>both directions between a Transfer Family server and a trading<br>partner.<br>In this case, you do the following:<br>1. Create profiles for your trading partner and<br>yourself.<br>2. Create a Transfer Family server that uses the AS2<br>protocol.<br>3. Create an agreement and add it to your<br>server.<br>4. Create a connector.<br>5. Import a certificate with a private key and add it<br>to your profile, and then import the public key to<br>your partner profile for encryption.<br>6. Receive a public key from your trading partner and<br>add it to their profile for encryption.<br>7. After you have these items, send the public key<br>for your certificate to your trading partner.<br>Now you and your trading partner can exchange encrypted<br>messages, and you can both decrypt them. You can store the<br>messages that you receive in your Amazon S3 bucket, and your<br>partner can decrypt and store the messages that you send to<br>them.<br>• Transfer encrypted AS2 messages in<br>both directions between a Transfer Family server and a trading<br>partner and add signing.<br>Now you and your partner want signed messages.<br>1. Import your signing private key (as a signing<br>certificate added to your profile).<br>2. Send your trading partner your public key.<br>3. Import your trading partner's signing public key<br>and add it to their profile.<br>• Transfer encrypted AS2 messages in<br>both directions between a Transfer Family server and a trading<br>partner and add signing and send an MDN<br>response.<br>Now, you want to exchange signed payloads, and both you<br>and your trading partner want MDN responses.<br>1. Your trading partner sends you their public<br>signing key.<br>2. Import your trading partner's public key (as a<br>signing certificate to your partner profile).<br>3. Send your public key to your trading<br>partner. |

## AS2 CloudFormation templates

This topic provides information about AWS CloudFormation templates that you can use to quickly
deploy AS2 servers and configurations for AWS Transfer Family. These templates automate the setup
process and help you implement best practices for AS2 file transfers.

- The basic AS2 template is described in [Use a template to create a demo Transfer Family AS2
  stack](create-as2-transfer-server.md#as2-cfn-demo-template "create-as2-transfer-server.md#as2-cfn-demo-template")
- The AS2 template for customizing HTTP headers is described in [Customize HTTP headers for AS2 messages](as2-custom-http-headers.md "as2-custom-http-headers.md").

### Customizing AS2 templates

You can customize the provided templates to meet your specific
requirements:

1. Download the template from the S3 URL.
2. Modify the YAML code to adjust configurations such as:
   - Security settings and certificate configurations
   - Network architecture and VPC settings
   - Storage options and file handling
   - Monitoring and notification preferences

3. Upload your modified template to your own S3 bucket.
4. Deploy the customized template using the AWS CloudFormation console or AWS CLI.

###### Important

When customizing templates, ensure that you maintain the dependencies between
resources and follow security best practices.

### Testing your AS2 deployment

After deploying an AS2 server using a template, you can test the
configuration:

1. Check the CloudFormation stack outputs for sample commands and endpoint
   information.
2. Use the AWS CLI to send a test file:

```
aws s3api put-object --bucket `your-bucket-name` --key test.txt --body test.txt
aws transfer start-file-transfer --connector-id `your-connector-id` --send-file-paths /`your-bucket-name`/test.txt
```

3. Verify file delivery in the destination S3 bucket.
4. Check CloudWatch logs for successful processing and MDN responses.

For more comprehensive testing, consider using third-party AS2 clients to send
files to your Transfer Family AS2 server.

### Best practices for AS2 template

deployment

Follow these best practices when using AS2 CloudFormation templates:

Security

Use strong certificates and rotate them regularly.

Implement least-privilege IAM policies.

Restrict network access using security groups.

Reliability

Deploy across multiple Availability Zones.

Implement monitoring and alerting for failed transfers.

Set up automated retries for failed transfers.

Performance

Choose appropriate instance types for your transfer volume.

Implement S3 lifecycle policies for efficient file management.

Monitor and optimize network configurations.

Cost Optimization

Use auto-scaling for variable workloads.

Implement S3 storage classes for older files.

Monitor and adjust resources based on actual usage.
