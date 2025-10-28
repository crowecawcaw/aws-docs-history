# Set up a CRL for AWS Private CA

Before you can configure a certificate revocation list (CRL) as part of the [CA creation process](create-CA.md "create-CA.md"), some prior setup may be
necessary. This section explains the prerequisites and options that you should
understand before creating a CA with a CRL attached.

For information about using Online Certificate Status Protocol (OCSP) as an
alternative or a supplement to a CRL, see [Certificate revocation options](create-CA.md#PcaCreateRevocation "create-CA.md#PcaCreateRevocation") and [Customize OCSP URL for AWS Private CA](ocsp-customize.md "ocsp-customize.md").

###### Topics

- [CRL types](#crl-type "#crl-type")
- [CRL structure](#crl-structure "#crl-structure")
- [Access policies for CRLs in Amazon S3](#s3-policies "#s3-policies")
- [Enable S3 Block Public Access (BPA) with CloudFront](#s3-bpa "#s3-bpa")
- [Determining the CRL Distribution Point (CDP) URI](#crl-url "#crl-url")
-

## CRL types

- **Complete** - The default setting.
  AWS Private CA maintains a single, unpartitioned CRL file for all unexpired
  certificates issued by a CA that have been revoked. Each certificate
  that AWS Private CA issues is bound to a specific CRL through its CRL
  distribution point (CDP) extension, as defined in [RFC 5280](https://datatracker.ietf.org/doc/html/rfc5280#section-4.2.1.9 "https://datatracker.ietf.org/doc/html/rfc5280#section-4.2.1.9"). You can have up to 1 million private certificates
  for each CA with complete CRL enabled. For more information, see the
  [AWS Private CA quotas](../../../general/latest/gr/pca.md#limits_pca "../../../general/latest/gr/pca.md#limits_pca").
- **Partitioned** - Compared to complete
  CRLs, partitioned CRLs dramatically increase the number of certiﬁcates
  your private CA can issue, and saves you from frequently rotating your
  CAs.

###### Important

When using partitioned CRLs, you must validate that the CRL's
associated issuing distribution point (IDP) URI matches the
certiﬁcate's CDP URI to ensure the right CRL has been fetched.
AWS Private CA marks the IDP extension as critical, which your client
must be able to process.

## CRL structure

Each CRL is a DER encoded file. To download the file and use [OpenSSL](https://www.openssl.org/ "https://www.openssl.org/") to view it, use a command
similar to the following:

```
openssl crl -inform DER -in `path-to-crl-file` -text -noout
```

CRLs have the following format:

```
Certificate Revocation List (CRL):
		        Version 2 (0x1)
		    Signature Algorithm: sha256WithRSAEncryption
		        Issuer: /C=US/ST=WA/L=Seattle/O=Example Company CA/OU=Corporate/CN=www.example.com
		        Last Update: Feb 26 19:28:25 2018 GMT
		        Next Update: Feb 26 20:28:25 2019 GMT
		        CRL extensions:
		            X509v3 Authority Key Identifier:
		                keyid:AA:6E:C1:8A:EC:2F:8F:21:BC:BE:80:3D:C5:65:93:79:99:E7:71:65

		            X509v3 CRL Number:
		                1519676905984
		Revoked Certificates:
		    Serial Number: E8CBD2BEDB122329F97706BCFEC990F8
		        Revocation Date: Feb 26 20:00:36 2018 GMT
		        CRL entry extensions:
		            X509v3 CRL Reason Code:
		                Key Compromise
		    Serial Number: F7D7A3FD88B82C6776483467BBF0B38C
		        Revocation Date: Jan 30 21:21:31 2018 GMT
		        CRL entry extensions:
		            X509v3 CRL Reason Code:
		                Key Compromise
		    Signature Algorithm: sha256WithRSAEncryption
		         82:9a:40:76:86:a5:f5:4e:1e:43:e2:ea:83:ac:89:07:49:bf:
		         c2:fd:45:7d:15:d0:76:fe:64:ce:7b:3d:bb:4c:a0:6c:4b:4f:
		         9e:1d:27:f8:69:5e:d1:93:5b:95:da:78:50:6d:a8:59:bb:6f:
		         49:9b:04:fa:38:f2:fc:4c:0d:97:ac:02:51:26:7d:3e:fe:a6:
		         c6:83:34:b4:84:0b:5d:b1:c4:25:2f:66:0a:2e:30:f6:52:88:
		         e8:d2:05:78:84:09:01:e8:9d:c2:9e:b5:83:bd:8a:3a:e4:94:
		         62:ed:92:e0:be:ea:d2:59:5b:c7:c3:61:35:dc:a9:98:9d:80:
		         1c:2a:f7:23:9b:fe:ad:6f:16:7e:22:09:9a:79:8f:44:69:89:
		         2a:78:ae:92:a4:32:46:8d:76:ee:68:25:63:5c:bd:41:a5:5a:
		         57:18:d7:71:35:85:5c:cd:20:28:c6:d5:59:88:47:c9:36:44:
		         53:55:28:4d:6b:f8:6a:00:eb:b4:62:de:15:56:c8:9c:45:d7:
		         83:83:07:21:84:b4:eb:0b:23:f2:61:dd:95:03:02:df:0d:0f:
		         97:32:e0:9d:38:de:7c:15:e4:36:66:7a:18:da:ce:a3:34:94:
		         58:a6:5d:5c:04:90:35:f1:8b:55:a9:3c:dd:72:a2:d7:5f:73:
		         5a:2c:88:85

```

###### Note

The CRL will only be deposited in Amazon S3 after a certificate has been issued
that refers to it. Prior to that, there will only be an
`acm-pca-permission-test-key` file visible in the Amazon S3
bucket.

## Access policies for CRLs in Amazon S3

If you plan to create a CRL, you need to prepare an Amazon S3 bucket to store it
in. AWS Private CA automatically deposits the CRL in the Amazon S3 bucket you designate
and updates it periodically. For more information, see [Creating a bucket.](../../../AmazonS3/latest/userguide/create-bucket.md "../../../AmazonS3/latest/userguide/create-bucket.md")

Your S3 bucket must be secured by an attached IAM permissions policy.
Authorized users and service principals require `Put` permission to
allow AWS Private CA to place objects in the bucket, and `Get` permission
to retrieve them. During the console procedure for [creating](create-CA.md "create-CA.md") a CA, you can choose to let AWS Private CA create a new bucket
and apply a default permissions policy.

###### Note

The IAM policy configuration depends on the AWS Regions involved.
Regions fall into two categories:

- **Default-enabled Regions** –
  Regions that are _enabled_ by
  default for all AWS accounts.
- **Default-disabled Regions** –
  Regions that are _disabled_ by
  default, but may be manually enabled by the customer.
  For more information and a list of the default-disabled Regions, see
  [Managing
  AWS Regions](../../../general/latest/gr/rande-manage.md "../../../general/latest/gr/rande-manage.md"). For a discussion of service principals in the
  context of IAM, see [AWS service principals in opt-in Regions](../../../IAM/latest/UserGuide/reference_policies_elements_principal.md#principal-services-in-opt-in-regions "../../../IAM/latest/UserGuide/reference_policies_elements_principal.md#principal-services-in-opt-in-regions").

When you configure CRLs as the certificate revocation method, AWS Private CA
creates a CRL and publishes it to an S3 bucket. The S3 bucket requires an
IAM policy that allows the AWS Private CA service principal to write to the
bucket. The name of the service principal varies according to the Regions
used, and not all possibilities are supported.

| PCA                 | S3                      | Service principal                |
| ------------------- | ----------------------- | -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Both in same Region | `acm-pca.amazonaws.com` |
| Enabled             | Enabled                 | `acm-pca.amazonaws.com`          |
| Disabled            | Enabled                 | `acm-pca.`Region`.amazonaws.com` |
| Enabled             | Disabled                | Not supported                    | The default policy applies no `SourceArn` restriction on the CA. We recommend that you apply a less permissive policy such as the following, which restricts access to both a specific AWS account and a specific private CA. Alternatively, you can use the [aws:SourceOrgID](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourceorgid "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourceorgid") condition key to constrain access to a specific organization in AWS Organizations. For more information about bucket policies, see [Bucket policies for Amazon Simple Storage Service](../../../AmazonS3/latest/userguide/bucket-policies.md "../../../AmazonS3/latest/userguide/bucket-policies.md"). If you choose to allow the default policy, you can always [modify](../../../AmazonS3/latest/userguide/add-bucket-policy.md "../../../AmazonS3/latest/userguide/add-bucket-policy.md") it later. ## Enable S3 Block Public Access (BPA) with CloudFront New Amazon S3 buckets are configured by default with the Block Public Access (BPA) feature activated. Included in the Amazon S3 [security best practices](../../../AmazonS3/latest/userguide/security-best-practices.md "../../../AmazonS3/latest/userguide/security-best-practices.md"), BPA is a set of access controls that customers can use to fine-tune access to objects in their S3 buckets and to the buckets as a whole. When BPA is active and correctly configured, only authorized and authenticated AWS users have access to a bucket and its contents. AWS recommends the use of BPA on all S3 buckets to avoid exposure of sensitive information to potential adversaries. However, additional planning is required if your PKI clients retrieve CRLs across the public internet (that is, while not logged into an AWS account). This section describes how to configure a private PKI solution using Amazon CloudFront, a content delivery network (CDN), to serve CRLs without requiring authenticated client access to an S3 bucket. ###### Note Using CloudFront incurs additional costs on your AWS account. For more information, see [Amazon CloudFront Pricing](https://aws.amazon.com/cloudfront/pricing/ "https://aws.amazon.com/cloudfront/pricing/"). If you choose to store your CRL in an S3 bucket with BPA enabled, and you do not use CloudFront, you must build another CDN solution to ensure that your PKI client has access to your CRL. ### Set up CloudFront for BPA Create a CloudFront distribution that will have access to your private S3 bucket, and can serve CRLs to unauthenticated clients. ###### To configure a CloudFront distribution for the CRL 1. Create a new CloudFront distribution using the procedure in [Creating a Distribution](../../../AmazonCloudFront/latest/DeveloperGuide/distribution-web-creating-console.md "../../../AmazonCloudFront/latest/DeveloperGuide/distribution-web-creating-console.md") in the _Amazon CloudFront Developer Guide_. While completing the procedure, apply the following settings: <br>• In **Origin Domain Name**, choose your S3 bucket. <br>• Choose **Yes** for **Restrict Bucket Access**. <br>• Choose **Create a New Identity** for **Origin Access Identity**. <br>• Choose **Yes, Update Bucket Policy** under **Grant Read Permissions on Bucket**. ###### Note In this procedure, CloudFront modifies your bucket policy to allow it to access bucket objects. Consider [editing](../../../AmazonS3/latest/userguide/add-bucket-policy.md "../../../AmazonS3/latest/userguide/add-bucket-policy.md") this policy to allow access only to objects under the `crl` folder. 2. After the distribution has initialized, locate its domain name in the CloudFront console and save it for the next procedure. ###### Note If your S3 bucket was newly created in a Region other than us-east-1, you might get an HTTP 307 temporary redirect error when you access your published application through CloudFront. It might take several hours for the address of the bucket to propagate. ### Set up your CA for BPA While configuring your new CA, include the alias to your CloudFront distribution. ###### To configure your CA with a CNAME for CloudFront <br>• Create your CA using [Create a private CA in AWS Private CA](create-CA.md "create-CA.md"). When you perform the procedure, the revocation file `revoke_config.txt` should include the following lines to specify a non-public CRL object and to provide a URL to the distribution endpoint in CloudFront: ``"S3ObjectAcl":"BUCKET_OWNER_FULL_CONTROL", "CustomCname":"`abcdef012345.cloudfront.net`"`` Afterward, when you issue certificates with this CA, they will contain a block like the following: `X509v3 CRL Distribution Points: Full Name: URI:http://abcdef012345.cloudfront.net/crl/01234567-89ab-cdef-0123-456789abcdef.crl` ###### Note If you have older certificates that were issued by this CA, they will be unable to access the CRL. ## Determining the CRL Distribution Point (CDP) URI If you need to use the CRL Distribution Point (CDP) URI in your workﬂow, you can either issue a certiﬁcate use the CRL URI on that certificate or use the following method. This only works for complete CRLs. Partitioned CRLs have a random GUID appended to them. If you use the S3 bucket as the CRL Distribution Point (CDP) for your CA, the CDP URI can be in one of the following formats. <br>• `http://`amzn-s3-demo-bucket`.s3.`region-code`.amazonaws.com/crl/`CA-ID`.crl` <br>• `http://s3.`region-code`.amazonaws.com/`amzn-s3-demo-bucket`/crl/`CA-ID`.crl` If you have configured your CA with a custom CNAME, the CDP URI will include the CNAME, for example, `http://`alternative.example.com`/crl/`CA-ID`.crl` ## By default, AWS Private CA writes CDP extensions using regional, IPv4-only `amazonaws.com` endpoints. To use CRLs over IPv6, do one of the following steps so that CDPs are written with URLs that point to [S3's dualstack endpoints](../../../AmazonS3/latest/API/dual-stack-endpoints.md "../../../AmazonS3/latest/API/dual-stack-endpoints.md"): <br>• Set your [CRL custom name](create-CA.md#PcaCreateRevocation "create-CA.md#PcaCreateRevocation") to the S3 dualstack endpoint domain. For example, ``bucketname`.s3.dualstack.`region-code`.amazonaws.com` <br>• Set up your own CNAME DNS record pointing at the relevant S3 dualstack endpoint, then use it as your CRL custom name |
