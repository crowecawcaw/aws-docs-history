Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026.
We will start enforcing it in phases. For more information on the details of Python end of life
and migration options, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") that was published on June 30, 2025.

# Downloading and installing the Amazon Redshift ODBC driver

To download and install the Amazon Redshift ODBC driver version 2.x for Linux:

1. Download the following driver:

   - [x86 64-bit RPM driver version 2.2.0.0](https://s3.amazonaws.com/redshift-downloads/drivers/odbc/2.2.0.0/AmazonRedshiftODBC-64-bit-2.2.0.0.x86_64.rpm "https://s3.amazonaws.com/redshift-downloads/drivers/odbc/2.2.0.0/AmazonRedshiftODBC-64-bit-2.2.0.0.x86_64.rpm")

     - Linux artifact signature key: [Key](https://s3.amazonaws.com/redshift-downloads/drivers/odbc/2.2.0.0/AmazonRedshiftODBC-64-bit-2.2.0.0.x86_64-certificate.pem "https://s3.amazonaws.com/redshift-downloads/drivers/odbc/2.2.0.0/AmazonRedshiftODBC-64-bit-2.2.0.0.x86_64-certificate.pem")
     - Linux artifact signed hash: [Hash](https://s3.amazonaws.com/redshift-downloads/drivers/odbc/2.2.0.0/AmazonRedshiftODBC-64-bit-2.2.0.0.x86_64-signature.bin "https://s3.amazonaws.com/redshift-downloads/drivers/odbc/2.2.0.0/AmazonRedshiftODBC-64-bit-2.2.0.0.x86_64-signature.bin")

   - [ARM 64-bit RPM driver version 2.2.0.0](https://s3.amazonaws.com/redshift-downloads/drivers/odbc/2.2.0.0/AmazonRedshiftODBC-64-bit-2.2.0.0.aarch64.rpm "https://s3.amazonaws.com/redshift-downloads/drivers/odbc/2.2.0.0/AmazonRedshiftODBC-64-bit-2.2.0.0.aarch64.rpm")

     - Linux artifact signature key: [Key](https://s3.amazonaws.com/redshift-downloads/drivers/odbc/2.2.0.0/AmazonRedshiftODBC-64-bit-2.2.0.0.aarch64-certificate.pem "https://s3.amazonaws.com/redshift-downloads/drivers/odbc/2.2.0.0/AmazonRedshiftODBC-64-bit-2.2.0.0.aarch64-certificate.pem")
     - Linux artifact signed hash: [Hash](https://s3.amazonaws.com/redshift-downloads/drivers/odbc/2.2.0.0/AmazonRedshiftODBC-64-bit-2.2.0.0.aarch64-signature.bin "https://s3.amazonaws.com/redshift-downloads/drivers/odbc/2.2.0.0/AmazonRedshiftODBC-64-bit-2.2.0.0.aarch64-signature.bin")

   - [x86 64-bit DEB driver version 2.2.0.0](https://s3.amazonaws.com/redshift-downloads/drivers/odbc/2.2.0.0/AmazonRedshiftODBC-64-bit-2.2.0.0.amd64.deb "https://s3.amazonaws.com/redshift-downloads/drivers/odbc/2.2.0.0/AmazonRedshiftODBC-64-bit-2.2.0.0.amd64.deb")

     - Linux artifact signature key: [Key](https://s3.amazonaws.com/redshift-downloads/drivers/odbc/2.2.0.0/AmazonRedshiftODBC-64-bit-2.2.0.0.amd64-certificate.pem "https://s3.amazonaws.com/redshift-downloads/drivers/odbc/2.2.0.0/AmazonRedshiftODBC-64-bit-2.2.0.0.amd64-certificate.pem")
     - Linux artifact signed hash: [Hash](https://s3.amazonaws.com/redshift-downloads/drivers/odbc/2.2.0.0/AmazonRedshiftODBC-64-bit-2.2.0.0.amd64-signature.bin "https://s3.amazonaws.com/redshift-downloads/drivers/odbc/2.2.0.0/AmazonRedshiftODBC-64-bit-2.2.0.0.amd64-signature.bin")

   - [ARM 64-bit DEB driver version 2.2.0.0](https://s3.amazonaws.com/redshift-downloads/drivers/odbc/2.2.0.0/AmazonRedshiftODBC-64-bit-2.2.0.0.arm64.deb "https://s3.amazonaws.com/redshift-downloads/drivers/odbc/2.2.0.0/AmazonRedshiftODBC-64-bit-2.2.0.0.arm64.deb")

     - Linux artifact signature key: [Key](https://s3.amazonaws.com/redshift-downloads/drivers/odbc/2.2.0.0/AmazonRedshiftODBC-64-bit-2.2.0.0.arm64-certificate.pem "https://s3.amazonaws.com/redshift-downloads/drivers/odbc/2.2.0.0/AmazonRedshiftODBC-64-bit-2.2.0.0.arm64-certificate.pem")
     - Linux artifact signed hash: [Hash](https://s3.amazonaws.com/redshift-downloads/drivers/odbc/2.2.0.0/AmazonRedshiftODBC-64-bit-2.2.0.0.arm64-signature.bin "https://s3.amazonaws.com/redshift-downloads/drivers/odbc/2.2.0.0/AmazonRedshiftODBC-64-bit-2.2.0.0.arm64-signature.bin")

###### Note

32-bit ODBC drivers are discontinued. Further updates will not be
released, except for urgent security patches. 2. Before installing, verify that AWS signed the driver package.
After downloading the package, its signature key (certificate), and
its signed hash (detached signature), run the following
commands:

```
openssl x509 -in `SignatureKeyFile` -pubkey -noout > redshift-odbc-pubkey.pem
openssl dgst -sha256 -verify redshift-odbc-pubkey.pem \
    -signature `SignedHashFile` \
    `PackageFile`
```

If the package is authentic, `openssl` prints
`Verified OK`. If the output is anything else, do not
install the package. Re-download the files or contact AWS
Support.

For example, to verify the x86 64-bit RPM:

```
openssl x509 -in AmazonRedshiftODBC-64-bit-2.2.0.0.x86_64-certificate.pem -pubkey -noout > redshift-odbc-pubkey.pem
openssl dgst -sha256 -verify redshift-odbc-pubkey.pem \
    -signature AmazonRedshiftODBC-64-bit-2.2.0.0.x86_64-signature.bin \
    AmazonRedshiftODBC-64-bit-2.2.0.0.x86_64.rpm
```

3. Go to the location where you downloaded the package, and then run one of
   the following commands. Use the command that corresponds to your Linux
   distribution.

On RHEL and CentOS operating systems (RPM), run the following command:

```
sudo yum --nogpgcheck localinstall `RPMFileName`
```

Replace `RPMFileName` with the RPM package file name. For
example, the following command demonstrates installing the 64-bit
driver:

```

sudo yum --nogpgcheck localinstall AmazonRedshiftODBC-64-bit-2.x.xx.xxxx.x86_64.rpm

```

On Debian and Ubuntu operating systems (DEB), navigate to the
directory containing the downloaded .deb file and run the following
command:

```
sudo apt install ./`DEBFileName`
```

Replace `DEBFileName` with the DEB package file name.
For example:

```

sudo apt install ./AmazonRedshiftODBC-64-bit-2.x.xx.xxxx.amd64.deb

```
