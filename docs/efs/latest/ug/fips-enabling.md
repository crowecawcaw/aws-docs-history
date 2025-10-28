# Enabling FIPS mode

If your operating system is using Federal Information Processing Standards (FIPS) endpoints
when mounting your file system, then you must enable FIPS mode in the Amazon EFS client. Enabling the
FIPS mode involves modifying the `efs-utils.conf` file on the operating system.

###### Note

FIPS mode requires that the installed version of OpenSSL is compiled with FIPS. For
more information on how to configure OpenSSL with FIPS see the [OpenSSL FIPS README](https://github.com/openssl/openssl/blob/master/README-FIPS.md "https://github.com/openssl/openssl/blob/master/README-FIPS.md").

###### To enable FIPS mode in the Amazon EFS client

1. Access the terminal for your Amazon EC2 instance through Secure Shell (SSH), and log in with
   the appropriate user name. For more information, see [Connect to your EC2 instance](../../../AWSEC2/latest/UserGuide/connect.md "../../../AWSEC2/latest/UserGuide/connect.md")
   in the _Amazon Elastic Compute Cloud User Guide_.
2. Using your text editor of choice, open the `/etc/amazon/efs/efs-utils.conf` file.
3. Find the line containing the following text:

```
"fips_mode_enabled = false"
```

4. Change the text to the following:

```
"fips_mode_enabled = true"
```

5. Save your changes.
