# Resolving issues with installing stunnel

If you are unable to install stunnel, try disabling certificate hostname checking.
Additionally, provide the strongest security possible by enabling Online Certificate Status Protocol (OCSP).

###### Topics

- [Disabling Certificate Hostname Checking](#disable-cert-hn-checking "#disable-cert-hn-checking")
- [Enabling Online Certificate Status Protocol](#tls-ocsp "#tls-ocsp")

## Disabling Certificate Hostname Checking

If you are unable to install the required dependencies, you can optionally disable
certificate hostname checking inside the Amazon EFS mount helper configuration. We do not recommend
that you disable this feature in production environments. To disable certificate host
name checking, do the following:

1. Access the terminal for your EC2 instance through Secure Shell (SSH), and
   log in with the appropriate user name. For more information, see [Connect to your
   EC2 instance](../../../AWSEC2/latest/UserGuide/connect.md "../../../AWSEC2/latest/UserGuide/connect.md") in the
   _Amazon EC2 User Guide_.
2. Using your text editor of choice, open the
   `/etc/amazon/efs/efs-utils.conf` file.
3. Set the `stunnel_check_cert_hostname` value to false.
4. Save the changes to the file and close it.

For more information on using encryption of data in transit, see [Mounting EFS file systems](mounting-fs.md "mounting-fs.md").

## Enabling Online Certificate Status Protocol

In order to maximize file system availability in the event that the CA is not reachable
from your VPC, the Online Certificate Status Protocol (OCSP) is not enabled by default when you
choose to encrypt data in transit. Amazon EFS uses an [Amazon certificate authority](https://www.amazontrust.com "https://www.amazontrust.com") (CA) to issue and sign its TLS certificates, and the CA
instructs the client to use OCSP to check for revoked certificates. The OCSP endpoint must be
accessible over the Internet from your Virtual Private Cloud in order to check a certificate's
status. Within the service, Amazon EFS continuously monitors certificate status, and issues new
certificates to replace any revoked certificates it detects.

In order to provide the strongest security possible, you can enable OCSP so that your Linux
clients can check for revoked certificates. OCSP protects against malicious use of revoked
certificates, which is unlikely to occur within your VPC. In the event that an EFS
TLS certificate is revoked, Amazon publishes a security bulletin and release a new version of
EFS mount helper that rejects the revoked certificate.

###### To enable OCSP on your Linux client for all future TLS connections to EFS

1. Open a terminal on your Linux client.
2. Using your text editor of choice, open the `/etc/amazon/efs/efs-utils.conf` file.
3. Set the `stunnel_check_cert_validity` value to true.
4. Save the changes to the file and close it.

######

To enable OCSP as part of the `mount` command

- Use the following mount command to enable OCSP when mounting the file system.

```

       `$` sudo mount -t efs -o tls,ocsp `fs-12345678`:/ /mnt/efs

```
