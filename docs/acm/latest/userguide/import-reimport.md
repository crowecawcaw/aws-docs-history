

# Reimport a certificate
<a name="import-reimport"></a>

If you imported a certificate and associated it with other AWS services, you can reimport that certificate before it expires while preserving the AWS service associations of the original certificate. For more information about AWS services integrated with ACM, see [Managed automation with integrated services](acm-services.md). 

 The following conditions apply when you reimport a certificate: 
+ You can add or remove domain names.
+ You cannot remove all of the domain names from a certificate.
+ If **Key Usage** extensions are present in the originally imported certificate, you can add new extension values, but you cannot remove existing values.

  **Exception:** You can remove the `keyEncipherment` Key Usage from ECDSA certificates. This accommodates [RFC 5480 Section 3](https://www.rfc-editor.org/rfc/rfc5480#section-3), which does not include `keyEncipherment` as a permitted Key Usage for ECDSA keys.
+ If **Extended Key Usage** extensions are present in the originally imported certificate, you can add new extension values, but you cannot remove existing values.

  **Exception:** You can remove the Client Authentication Extended Key Usage. This accommodates industry changes where certificate authorities no longer issue certificates with ClientAuth EKU to comply with Chrome's root program requirements. 
**Important**  
If you require Client Authentication functionality, you must implement additional validations on your side, as ACM does not support rollback to previously imported certificates.
+ The key type and size cannot be changed.
+ You cannot apply resource tags when reimporting a certificate.

**Topics**
+ [Reimport (console)](#reimport-certificate-api)
+ [Reimport (AWS CLI)](#reimport-certificate-cli)

## Reimport (console)
<a name="reimport-certificate-api"></a>

The following example shows how to reimport a certificate using the AWS Management Console.

1. Open the ACM console at [https://console.aws.amazon.com/acm/home](https://console.aws.amazon.com/acm/home).

1. Select or expand the certificate to reimport.

1. Open the details pane of the certificate and choose the **Reimport certificate** button. If you selected the certificate by checking the box beside its name, choose **Reimport certificate** on the **Actions** menu.

1. For **Certificate body**, paste the PEM-encoded end-entity certificate.

1. For **Certificate private key**, paste the unencrypted PEM-encoded private key associated with the certificate's public key.

1. (Optional) For **Certificate chain**, paste the PEM-encoded certificate chain. The certificate chain includes one or more certificates for all intermediate issuing certification authorities, and the root certificate. If the certificate to be imported is self-assigned, no certificate chain is necessary.

1. Review the information about your certificate. If there are no errors, choose **Reimport**.

## Reimport (AWS CLI)
<a name="reimport-certificate-cli"></a>

The following example shows how to reimport a certificate using the [AWS Command Line Interface (AWS CLI)](https://aws.amazon.com/cli/). The example assumes the following:
+ The PEM-encoded certificate is stored in a file named `Certificate.pem`.
+ The PEM-encoded certificate chain is stored in a file named `CertificateChain.pem`.
+ (Private certificates only) The PEM-encoded, unencrypted private key is stored in a file named `PrivateKey.pem`.
+ You have the ARN of the certificate you want to reimport.

To use the following example, replace the file names and the ARN with your own and type the command on one continuous line. The following example includes line breaks and extra spaces to make it easier to read.

**Note**  
To reimport a certificate, you must specify the certificate ARN.

```
$ aws acm import-certificate --certificate fileb://{{Certificate.pem}} \
      --certificate-chain fileb://{{CertificateChain.pem}} \
      --private-key fileb://{{PrivateKey.pem}} \
      --certificate-arn {{arn:aws:acm:region:123456789012:certificate/12345678-1234-1234-1234-12345678901}}
```

If the `import-certificate` command is successful, it returns the [Amazon Resource Name (ARN)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) of the certificate. 