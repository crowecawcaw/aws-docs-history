# Troubleshoot certificate validation

If the ACM certificate request status is **Pending validation**, the
request is waiting for action from you. If you chose email validation when you made the
request, you or an authorized representative must respond to the validation email messages.
These messages were sent to the common email addresses for the requested domain. For more
information, see [AWS Certificate Manager email validation](email-validation.md "email-validation.md"). If you
chose DNS validation, you must write the CNAME record that ACM created for you to your DNS
database. For more information, see [AWS Certificate Manager DNS validation](dns-validation.md "dns-validation.md").

###### Important

You must validate that you own or control every domain name that you included in your
certificate request. If you chose email validation, you will receive validation email
messages for each domain. If you do not, then see [Not receiving validation email](troubleshooting-email-validation.md#troubleshooting-no-mail "troubleshooting-email-validation.md#troubleshooting-no-mail"). If you chose DNS validation, you must create
one CNAME record for each domain.

###### Note

Public ACM certificates can be installed on Amazon EC2 instances that are connected to a
[Nitro Enclave](acm-services.md#acm-nitro-enclave "acm-services.md#acm-nitro-enclave"). You can also [export a public certificate](export-public-certificate.md "export-public-certificate.md")
to use on any Amazon EC2 instance. For information about
setting up a standalone web server on an Amazon EC2 instance not connected to a Nitro Enclave, see [Tutorial: Install a LAMP web server
on Amazon Linux 2](../../../AWSEC2/latest/UserGuide/ec2-lamp-amazon-linux-2.md "../../../AWSEC2/latest/UserGuide/ec2-lamp-amazon-linux-2.md") or [Tutorial:
Install a LAMP web server with the Amazon Linux AMI](../../../AWSEC2/latest/UserGuide/install-LAMP.md "../../../AWSEC2/latest/UserGuide/install-LAMP.md").

We recommend that you use DNS validation rather than email validation.

Consult the following topics if you experience validation problems.

###### Topics

- [Troubleshoot DNS validation problems](troubleshooting-DNS-validation.md "troubleshooting-DNS-validation.md")
- [Troubleshoot email validation problems](troubleshooting-email-validation.md "troubleshooting-email-validation.md")
- [Troubleshooting HTTP validation problems](troubleshooting-HTTP-validation.md "troubleshooting-HTTP-validation.md")
