# Import a certificate

You can import an externally obtained certificate (that is, one provided by a
third-party trust services provider) into ACM by using the AWS Management Console, the AWS CLI, or
the ACM API. The following topics show you how to use the AWS Management Console and the AWS CLI.
Procedures for obtaining a certificate from a non-AWS issuer are outside the scope of
this guide.

###### Important

Your selected signature algorithm must meet the [Prerequisites for importing ACM
certificates](import-certificate-prerequisites.md "import-certificate-prerequisites.md").

###### Topics

- [Import (console)](#import-certificate-api "#import-certificate-api")
- [Import (AWS CLI)](#import-certificate-cli "#import-certificate-cli")

## Import (console)

The following example shows how to import a certificate using the
AWS Management Console.

1. Open the ACM console at [https://console.aws.amazon.com/acm/home](https://console.aws.amazon.com/acm/home "https://console.aws.amazon.com/acm/home"). If this is your first time using
   ACM, look for the **AWS Certificate Manager** heading and
   choose the **Get started** button under
   it.
2. Choose **Import a certificate**.
3. Do the following:
   1. For **Certificate body**, paste the PEM-encoded
      certificate to import. It should begin with `-----BEGIN
CERTIFICATE-----` and end with `-----END
CERTIFICATE-----`.
   2. For **Certificate private key**, paste the
      certificate's PEM-encoded, unencrypted private key. It should begin
      with `-----BEGIN PRIVATE KEY-----` and end with
      `-----END PRIVATE KEY-----`.
   3. (Optional) For **Certificate chain**, paste the
      PEM-encoded certificate chain.

4. (Optional) To add tags to your imported certificate, choose
   **Tags**. A tag is a label that you assign to an AWS
   resource. Each tag consists of a key and an optional value, both of which
   you define. You can use tags to organize your resources or track your AWS
   costs.
5. Choose **Import**.

## Import (AWS CLI)

The following example shows how to import a certificate using the [AWS Command Line Interface (AWS CLI)](https://aws.amazon.com/cli/ "https://aws.amazon.com/cli/"). The example assumes the
following:

- The PEM-encoded certificate is stored in a file named
  `Certificate.pem`.
- The PEM-encoded certificate chain is stored in a file named
  `CertificateChain.pem`.
- The PEM-encoded, unencrypted private key is stored in a file named
  `PrivateKey.pem`.

To use the following example, replace the file names with your own and type the
command on one continuous line. The following example includes line breaks and extra
spaces to make it easier to read.

```
$ aws acm import-certificate --certificate fileb://`Certificate.pem` \
      --certificate-chain fileb://`CertificateChain.pem` \
      --private-key fileb://`PrivateKey.pem`
```

If the `import-certificate` command is successful, it returns the
[Amazon Resource Name
(ARN)](../../../general/latest/gr/aws-arns-and-namespaces.md "../../../general/latest/gr/aws-arns-and-namespaces.md") of the imported certificate.
