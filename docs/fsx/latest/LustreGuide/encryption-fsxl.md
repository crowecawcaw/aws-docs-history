

# Data encryption in Amazon FSx for Lustre
<a name="encryption-fsxl"></a>

Amazon FSx for Lustre supports two forms of encryption for file systems, encryption of data at rest and encryption in transit. Encryption of data at rest is automatically enabled when creating an Amazon FSx file system. Encryption of data in transit is automatically enabled when you access an Amazon FSx file system from [Amazon EC2 instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/data-protection.html#encryption-transit) that support this feature.

## When to use encryption
<a name="whenencrypt"></a>

If your organization is subject to corporate or regulatory policies that require encryption of data and metadata at rest, we recommend creating an encrypted file system and mounting your file system using encryption of data in transit.

For more information about creating a file system encrypted at rest using the console, see [Create your Amazon FSx for Lustre file system](getting-started.md#getting-started-step1).

**Topics**
+ [When to use encryption](#whenencrypt)
+ [Encrypting data at rest](encryption-at-rest.md)
+ [Encrypting data in transit](encryption-in-transit-fsxl.md)