# Create a private CA in AWS Private CA

You can use the procedures in this section to create either root CAs or subordinate
CAs, resulting in an auditable hierarchy of trust relationships that matches your
organizational needs. You can create a CA using the AWS Management Console, the PCA portion of the
AWS CLI, or AWS CloudFormation.

For information about updating the configuration of a CA that you have already
created, see [Update a private CA in AWS Private Certificate Authority](PCAUpdateCA.md "PCAUpdateCA.md").

For information about using a CA to sign end-entity certificates for your users,
devices, and applications, see [Issue private end-entity certificates](PcaIssueCert.md "PcaIssueCert.md").

###### Note

Your account is charged a monthly price for each private CA starting from the time
that you create it.

For the latest AWS Private CA pricing information, see [AWS Private Certificate Authority Pricing](https://aws.amazon.com/private-ca/pricing/ "https://aws.amazon.com/private-ca/pricing/"). You can also use the [AWS pricing
calculator](https://calculator.aws/#/createCalculator/certificateManager "https://calculator.aws/#/createCalculator/certificateManager") to estimate costs.

###### Topics

- [CLI examples for creating a private CA](#create-ca-cli-examples "#create-ca-cli-examples")

Console

###### To create a private CA using the console

1. Complete the following steps to create a private CA using the AWS Management Console.

**To get started using the console**

Sign in to your AWS account and open the AWS Private CA console at `https://console.aws.amazon.com/acm-pca/home`.

    * If you are opening the console in a Region where you have no private CAs,
     the introductory page appears. Choose **Create a private
     CA**.
    * If you are opening the console in a Region where you have already created
     a CA, the **Private certificate authorities** page opens
     with a list of your CAs. Choose **Create CA**.

2. Under **Mode options**, choose the
   expiration mode of the certificates that your CA issues.
   - **General-purpose** – Issues certificates that
     can be configured with any expiration date. This is the default.
   - **Short-lived certificate** – Issues
     certificates with a maximum validity period of seven days. A short
     validity period can substitute in some cases for a revocation
     mechanism.

3. On the **Type options** section of the console, choose the
   type of private certificate authority that you want to create.
   - Choosing **Root** establishes a new CA hierarchy.
     This CA is backed by a self-signed certificate. It serves as the
     ultimate signing authority for other CAs and end-entity certificates
     in the hierarchy.
   - Choosing **Subordinate** creates a CA that must be
     signed by a parent CA above it in the hierarchy. Subordinate CAs are
     typically used to create other subordinate CAs or to issue end-entity
     certificates to users, computers, and applications.

   ###### Note

   AWS Private CA provides an automated signing process when your
   subordinate CA's parent CA is also hosted by AWS Private CA. All you do
   is choose the parent CA to use.

   Your subordinate CA might need to be signed by an external trust
   services provider. If so, AWS Private CA provides you with a certificate
   signing request (CSR) that you must download and use to obtain a
   signed CA certificate. For more information, see [Install a subordinate CA certificate
   signed by an external parent CA](PCACertInstall.md#InstallSubordinateExternal "PCACertInstall.md#InstallSubordinateExternal").

4. Under **Subject distinguished name options**, configure the
   subject name of your private CA. You must enter a value for at least one of the
   following options:
   - **Organization (O)** – For example, a company
     name
   - **Organization Unit (OU)** – For example, a division within a
     company
   - **Country name (C)** – A two-letter country code
   - **State or province name** – Full name of a
     state or province
   - **Locality name** – The name of a city
   - **Common Name (CN)** – A human-readable string to identify the CA.

###### Note

You can further customize the subject name of a certificate by applying an
APIPassthrough template at the time of issue. For more information and a
detailed example, see [Issue a certificate with a custom subject name using
an APIPassthrough template](PcaIssueCert.md#custom-subject-1 "PcaIssueCert.md#custom-subject-1").

Because the backing certificate is self-signed, the subject information that
you provide for a private CA is probably more sparse than what a public CA would
contain. For more information about each of the values that make up a subject
distinguished name, see [RFC
5280](https://datatracker.ietf.org/doc/html/rfc5280#section-4.1.2.4 "https://datatracker.ietf.org/doc/html/rfc5280#section-4.1.2.4"). 5. Under **Key algorithm options**, choose the key algorithm and
the bit-size of the key. The default value is an RSA algorithm with a 2048-bit
key length. You can choose from the following algorithms:

    * RSA 2048
    * RSA 3072
    * RSA 4096
    * ECDSA P256
    * ECDSA P384
    * ECDSA P521

6.  Under **Certificate revocation options**, you can select from
    two methods of sharing revocation status with clients that use your
    certificates:

        * **Activate CRL distribution**
        * **Turn on OCSP**

    You can configure either, neither, or both of these revocation options for
    your CA. Although optional, managed revocation is recommended as a [best practice](ca-best-practices.md "ca-best-practices.md"). Before completing this
    step, see [Plan your AWS Private CA certificate revocation method](revocation-setup.md "revocation-setup.md")
    for information about the advantages of each method, the preliminary setup that
    might be required, and additional revocation features.

###### Note

If you create your CA without configuring revocation, you can always
configure it later. For more information, see [Update a private CA in AWS Private Certificate Authority](PCAUpdateCA.md "PCAUpdateCA.md").

To configure **Certificate revocation options**, perform the following steps.

    1. Under **Certificate revocation options**,
     choose **Activate CRL distribution**.
    2. To create an Amazon S3 bucket for your CRL entries, choose
     **Create a new S3 bucket** and
     type a unique bucket name. (You do not need to include the path
     to the bucket.) Otherwise, under **S3 bucket
     URI**, choose an existing bucket from the list.


    When you create a new bucket through the console, AWS Private CA
     attempts to attach the [required
     access policy](crl-planning.md#s3-policies "crl-planning.md#s3-policies") to the bucket, and to disable the S3
     default Block Public Access (BPA) setting on it. If you instead
     specify an existing bucket, you must ensure that BPA is disabled
     for the account and for the bucket. Otherwise, the operation to
     create the CA fail. If the CA is created successfully, you must
     still manually attach a policy to it before you can begin
     generating CRLs. Use one of the policy patterns described in
     [Access policies for CRLs in Amazon S3](crl-planning.md#s3-policies "crl-planning.md#s3-policies") .
     For more information, see [Adding a bucket policy using the Amazon S3
     console.](../../../AmazonS3/latest/user-guide/add-bucket-policy.md "../../../AmazonS3/latest/user-guide/add-bucket-policy.md")


    ###### Important

    An attempt to create a CA using the AWS Private CA console
     fails if all of the following conditions apply:



    	* You are setting up a CRL.
    	* You ask AWS Private CA to create an S3 bucket
    	 automatically.
    	* You are enforcing BPA settings in S3.In this situation, the console creates a bucket, but
     attempts and fails to make it publicly accessible. Check
     your Amazon S3 settings if this occurs, disable BPA as needed,
     and then repeat the procedure for creating a CA. For more
     information, see [Blocking public access to your Amazon S3
     storage](../../../AmazonS3/latest/userguide/access-control-block-public-access.md "../../../AmazonS3/latest/userguide/access-control-block-public-access.md").
    3. Expand **CRL settings** for
     additional configuration options.




    	* Choose **Enable partitioning**
    	 to enable partitioning of CRLs. If you don't enable partitioning, your CA is subject to the
    	 maximum number of revoked certificates. For more information, see
    	 [AWS Private Certificate Authority quotas](../../../general/latest/gr/pca.md#limits_pca "../../../general/latest/gr/pca.md#limits_pca").
    	 For more information about partitioned CRLs, see [CRL types](crl-planning.md#crl-type "crl-planning.md#crl-type").
    	* Add a **Custom CRL Name**
    	 to create an alias for your Amazon S3 bucket. This name is
    	 contained in certificates issued by the CA in the “CRL
    	 Distribution Points" extension that is defined by RFC
    	 5280. To use CRLs over IPv6, set this
    	 to your bucket's dualstack S3 endpoint as described in
    	 [Using CRLs over IPv6](crl-planning.md#crl-ipv6 "crl-planning.md#crl-ipv6").
    	* Add a **Custom path** to create a
    	 DNS alias for the file path in your Amazon S3 bucket.
    	* Type the **Validity in days**
    	 your CRL will remain valid. The default value is 7 days.
    	 For online CRLs, a validity period of 2-7 days is common.
    	 AWS Private CA tries to regenerate the CRL at the midpoint of the specified
    	 period.
    4. Expand **S3 settings** for optional
     configuration of **Bucket versioning** and
     **Bucket access logging**.

7.  For **Certificate revocation options**,
    choose **Turn on OCSP**.
    1. In the **Custom OCSP endpoint _- optional_** field, you can provide
       a fully qualified domain name (FQDN) for a non-Amazon OCSP
       endpoint. To use OCSP over IPv6, set this field to a dualstack endpoint
       as described in [Using OCSP over IPv6](ocsp-customize.md#ocsp-ipv6 "ocsp-customize.md#ocsp-ipv6").

    When you provide an FQDN in this field, AWS Private CA inserts
    the FQDN into the _Authority Information
    Access_ extension of each
    issued certificate in place of the default URL for the AWS OCSP
    responder. When an endpoint receives a certificate containing
    the custom FQDN, it queries that address for an OCSP response.
    For this mechanism to work, you need to take two additional
    actions:

        * Use a proxy server to forward traffic that
         arrives at your custom FQDN to the AWS OCSP
         responder.
        * Add a corresponding CNAME record to your DNS
         database.

    ###### Tip

    For more information about implementing a complete
    OCSP solution using a custom CNAME, see [Customize OCSP URL for AWS Private CA](ocsp-customize.md "ocsp-customize.md").

    For example, here is a CNAME record for customized
    OCSP as it would appear in Amazon Route 53.

    | Record name             | Type  | Routing policy | Differentiator | Value/Route traffic to |
    | ----------------------- | ----- | -------------- | -------------- | ---------------------- |
    | alternative.example.com | CNAME | Simple         | -              | proxy.example.com      |

    ###### Note

    The value of the CNAME must not include a protocol
    prefix such as "http://" or "https://".

8.  Under **Add tags**, you can optionally tag your CA. Tags are
    key-value pairs that serve as metadata for identifying and organizing AWS
    resources. For a list of AWS Private CA tag parameters and for instructions on how
    to add tags to CAs after creation, see [Add tags for your private CA](PcaCaTagging.md "PcaCaTagging.md").

###### Note

To attach tags to a private CA during the creation procedure, a CA administrator must
first associate an inline IAM policy with the `CreateCertificateAuthority` action and explicitly allow
tagging. For more information, see [Tag-on-create: Attaching tags to a CA at the
time of creation](auth-InlinePolicies.md#tag-on-create "auth-InlinePolicies.md#tag-on-create"). 9. Under **CA permissions options**, you can optionally delegate
automatic renewal permissions to the AWS Certificate Manager service principal. ACM can only
automatically renew private end-entity certificates generated by this CA if
this permission is granted. You can assign renewal permissions at any time with
the AWS Private CA [CreatePermission](../APIReference/API_CreatePermission.md "../APIReference/API_CreatePermission.md") API or [create-permission](../../../cli/latest/reference/acm-pca/create-permission.md "../../../cli/latest/reference/acm-pca/create-permission.md") CLI
command.

The default is to enable these permissions.

###### Note

AWS Certificate Manager does not support the automatic renewal of short-lived
certificates. 10. Under
**Pricing**, confirm that you understand the pricing for a
private CA.

###### Note

For the latest AWS Private CA pricing information, see [AWS Private Certificate Authority Pricing](https://aws.amazon.com/private-ca/pricing/ "https://aws.amazon.com/private-ca/pricing/"). You can also use the [AWS pricing
calculator](https://calculator.aws/#/createCalculator/certificateManager "https://calculator.aws/#/createCalculator/certificateManager") to estimate costs. 11. Choose **Create CA** after you have checked all of the
entered information for accuracy. The details page for the CA opens and displays
its status as **Pending certificate**.

###### Note

While on the details page, you can finish configuring your CA by choosing
**Actions**, **Install CA
certificate**, or you can return later to the **Private
certificate authorities** list and complete the installation
procedure that applies in your case:

    * [Install a root CA certificate](PCACertInstall.md#InstallRoot "PCACertInstall.md#InstallRoot")
    * [Install a subordinate CA certificate
     hosted by AWS Private CA](PCACertInstall.md#InstallSubordinateInternal "PCACertInstall.md#InstallSubordinateInternal")
    * [Install a subordinate CA certificate
     signed by an external parent CA](PCACertInstall.md#InstallSubordinateExternal "PCACertInstall.md#InstallSubordinateExternal")

CLI
Use the [create-certificate-authority](../../../cli/latest/reference/acm-pca/create-certificate-authority.md "../../../cli/latest/reference/acm-pca/create-certificate-authority.md") command to create a private CA. You
must specify the CA configuration (containing algorithm and subject-name
information), the revocation configuration (if you plan to use OCSP and/or a
CRL), and the CA type (root or subordinate). The configuration and revocation
configuration details are contained in two files that you supply as arguments to
the command. Optionally, you can also configure the CA usage mode (for issuing
standard or short-lived certificates), attach tags, and provide an idempotency
token.

If you are configuring a CRL, you must have a secured Amazon S3 bucket in place
_before_ you issue the
**create-certificate-authority** command. For more information,
see [Access policies for CRLs in Amazon S3](crl-planning.md#s3-policies "crl-planning.md#s3-policies") .

The CA configuration file specifies the following information:

- The name of the algorithm
- The key size to be used to create the CA private key
- The type of signing algorithm that the CA uses to sign its own Certificate Signing Request, CRLs, and OCSP responses
- X.500 subject information

The revocation configuration for OCSP defines an `OcspConfiguration`
object with the following information:

- The `Enabled` flag set to "true".
- (Optional) A custom CNAME declared as a value for
  `OcspCustomCname`.

The revocation configuration for a CRL defines a `CrlConfiguration`
object with the following information:

- The `Enabled` flag set to "true".
- The CRL expiration period in days (the validity period of the CRL).
- The Amazon S3 bucket that will contain the CRL.
- (Optional) An [S3ObjectAcl](../APIReference/API_CrlConfiguration.md#privateca-Type-CrlConfiguration-S3ObjectAcl "../APIReference/API_CrlConfiguration.md#privateca-Type-CrlConfiguration-S3ObjectAcl") value that determines whether the
  CRL is publicly accessible. In the example presented here, public access is
  blocked. For more information, see [Enable S3 Block Public Access (BPA) with CloudFront](crl-planning.md#s3-bpa "crl-planning.md#s3-bpa").
- (Optional) A CNAME alias for the S3 bucket that is included in
  certificates issued by the CA. If the CRL is not publicly accessible, this
  will point to a distribution mechanism such as Amazon CloudFront.
- (Optional) A `CrlDistributionPointExtensionConfiguration` object with the following information:
  - The `OmitExtension` flag set to "true" or "false". This controls whether the default value for the CDP extension will be written to a certificate issued by the CA. For more information about the CDP extension, see [Determining the CRL Distribution Point (CDP) URI](crl-planning.md#crl-url "crl-planning.md#crl-url") . A CustomCname cannot be set if OmitExtension is "true".

- (Optional) A custom path for the CRL in the S3 bucket.
- (Optional) A [CrlType](../APIReference/API_CrlConfiguration.md#privateca-Type-CrlConfiguration-CrlType "../APIReference/API_CrlConfiguration.md#privateca-Type-CrlConfiguration-CrlType") value that determines whether the CRL will be complete or partitioned. If not supplied, the CRL
  will default to complete.

###### Note

You can enable both revocation mechanisms on the same CA by defining both an
`OcspConfiguration` object and a `CrlConfiguration`
object. If you supply no **--revocation-configuration**
parameter, both mechanisms are disabled by default. If you need revocation
validation support later, see [Updating a CA (CLI)](PCAUpdateCA.md#ca-update-cli "PCAUpdateCA.md#ca-update-cli").

See the following section for CLI examples.

## CLI examples for creating a private CA

The following examples assume that you have set up your `.aws`
configuration directory with a valid default Region, endpoint, and credentials. For
information about configuring your AWS CLI environment, see [Configuration and credential file
settings](../../../cli/latest/reference/cli-configure-files.md "../../../cli/latest/reference/cli-configure-files.md"). For readability, we supply the CA configuration and revocation
input as JSON files in the example commands. Modify the example files as needed for
your use.

All of the examples use the following `ca_config.txt` configuration
file unless otherwise stated.

**File: ca_config.txt**

```
{
   "KeyAlgorithm":"RSA_2048",
   "SigningAlgorithm":"SHA256WITHRSA",
   "Subject":{
      "Country":"`US`",
      "Organization":"`Example Corp`",
      "OrganizationalUnit":"`Sales`",
      "State":"`WA`",
      "Locality":"`Seattle`",
      "CommonName":"`www.example.com`"
   }
}
```

### Example 1: Create a CA with OCSP enabled

In this example, the revocation file enables default OCSP support, which uses
the AWS Private CA responder to check certificate status.

**File: revoke_config.txt for OCSP**

```
{
   "OcspConfiguration":{
      "Enabled":true
   }
}
```

**Command**

```
`$` `aws acm-pca create-certificate-authority \
 --certificate-authority-configuration file://`ca_config.txt` \
 --revocation-configuration file://`revoke_config.txt` \
 --certificate-authority-type "ROOT" \
 --idempotency-token `01234567` \
 --tags Key=`Name`,Value=`MyPCA``
```

If successful, this command outputs the Amazon Resource Name (ARN) of the new
CA.

```
{
	"CertificateAuthorityArn":"arn:aws:acm-pca:`region`:`account`:
       certificate-authority/`CA_ID`"
}
```

**Command**

```
`$` `aws acm-pca create-certificate-authority \
 --certificate-authority-configuration file://`ca_config.txt` \
 --revocation-configuration file://`revoke_config.txt` \
 --certificate-authority-type "ROOT" \
 --idempotency-token `01234567` \
 --tags Key=`Name`,Value=`MyPCA-2``
```

If successful, this command outputs the Amazon Resource Name (ARN) of the
CA.

```
{
    "CertificateAuthorityArn":"arn:`aws`:acm-pca:`us-east-1`:`111122223333`:certificate-authority/`11223344-1234-1122-2233-112233445566`"
}
```

Use the following command to inspect the configuration of your CA.

```
`$` `aws acm-pca describe-certificate-authority \
 --certificate-authority-arn "arn:`aws`:acm-pca:`us-east-1`:`111122223333`:certificate-authority/`11223344-1234-1122-2233-112233445566`" \
 --output json`
```

This description should contain the following section.

```
"RevocationConfiguration": {
   ...
   "OcspConfiguration": {
      "Enabled": true
   }
   ...
}
```

### Example 2: Create a CA with OCSP and a custom CNAME

enabled

In this example, the revocation file enables customized OCSP support. The
`OcspCustomCname` parameter takes a fully qualified domain name
(FQDN) as its value.

When you provide an FQDN in this field, AWS Private CA inserts
the FQDN into the _Authority Information
Access_ extension of each
issued certificate in place of the default URL for the AWS OCSP
responder. When an endpoint receives a certificate containing
the custom FQDN, it queries that address for an OCSP response.
For this mechanism to work, you need to take two additional
actions:

- Use a proxy server to forward traffic that
  arrives at your custom FQDN to the AWS OCSP
  responder.
- Add a corresponding CNAME record to your DNS
  database.

###### Tip

For more information about implementing a complete
OCSP solution using a custom CNAME, see [Customize OCSP URL for AWS Private CA](ocsp-customize.md "ocsp-customize.md").

For example, here is a CNAME record for customized
OCSP as it would appear in Amazon Route 53.

| Record name             | Type  | Routing policy | Differentiator | Value/Route traffic to |
| ----------------------- | ----- | -------------- | -------------- | ---------------------- |
| alternative.example.com | CNAME | Simple         | -              | proxy.example.com      |

###### Note

The value of the CNAME must not include a protocol
prefix such as "http://" or "https://".

**File: revoke_config.txt for OCSP**

```
{
   "OcspConfiguration":{
      "Enabled":true,
      "OcspCustomCname":"`alternative.example.com`"
   }
}
```

**Command**

```
`$` `aws acm-pca create-certificate-authority \
 --certificate-authority-configuration file://`ca_config.txt` \
 --revocation-configuration file://`revoke_config.txt` \
 --certificate-authority-type "ROOT" \
 --idempotency-token `01234567` \
 --tags Key=`Name`,Value=`MyPCA-3``
```

If successful, this command outputs the Amazon Resource Name (ARN) of the
CA.

```
{
    "CertificateAuthorityArn":"arn:`aws`:acm-pca:`us-east-1`:`111122223333`:certificate-authority/`11223344-1234-1122-2233-112233445566`"
}
```

Use the following command to inspect the configuration of your CA.

```
`$` `aws acm-pca describe-certificate-authority \
 --certificate-authority-arn "arn:`aws`:acm-pca:`us-east-1`:`111122223333`:certificate-authority/`11223344-1234-1122-2233-112233445566`" \
 --output json`
```

This description should contain the following section.

```
"RevocationConfiguration": {
   ...
   "OcspConfiguration": {
      "Enabled": true,
      "OcspCustomCname": "`alternative.example.com`"
   }
   ...
}
```

### Example 3: Create a CA with an attached CRL

In this example, the revocation configuration defines CRL parameters.

**File: revoke_config.txt**

```
{
   "CrlConfiguration":{
      "Enabled":true,
      "ExpirationInDays":`7`,
      "S3BucketName":"`amzn-s3-demo-bucket`"
   }
}
```

**Command**

```
`$` `aws acm-pca create-certificate-authority \
 --certificate-authority-configuration file://`ca_config.txt` \
 --revocation-configuration file://`revoke_config.txt` \
 --certificate-authority-type "ROOT" \
 --idempotency-token `01234567` \
 --tags Key=`Name`,Value=`MyPCA-1``
```

If successful, this command outputs the Amazon Resource Name (ARN) of the
CA.

```
{
    "CertificateAuthorityArn":"arn:`aws`:acm-pca:`us-east-1`:`111122223333`:certificate-authority/`11223344-1234-1122-2233-112233445566`"
}
```

Use the following command to inspect the configuration of your CA.

```
`$` `aws acm-pca describe-certificate-authority \
 --certificate-authority-arn "arn:`aws`:acm-pca:`us-east-1`:`111122223333`:certificate-authority/`11223344-1234-1122-2233-112233445566`" \
 --output json`
```

This description should contain the following section.

```
"RevocationConfiguration": {
   ...
   "CrlConfiguration": {
      "Enabled": true,
      "ExpirationInDays": 7,
      "S3BucketName": "`amzn-s3-demo-bucket`"
   },
   ...
}
```

### Example 4: Create a CA with an attached CRL and a

custom CNAME enabled

In this example, the revocation configuration defines CRL parameters that
include a custom CNAME.

**File: revoke_config.txt**

```
{
   "CrlConfiguration":{
      "Enabled":true,
      "ExpirationInDays":`7`,
      "CustomCname": "`alternative.example.com`",
      "S3BucketName":"`amzn-s3-demo-bucket`"
   }
}
```

**Command**

```
`$` `aws acm-pca create-certificate-authority \
 --certificate-authority-configuration file://`ca_config.txt` \
 --revocation-configuration file://`revoke_config.txt` \
 --certificate-authority-type "ROOT" \
 --idempotency-token `01234567` \
 --tags Key=`Name`,Value=`MyPCA-1``
```

If successful, this command outputs the Amazon Resource Name (ARN) of the
CA.

```
{
    "CertificateAuthorityArn":"arn:`aws`:acm-pca:`us-east-1`:`111122223333`:certificate-authority/`11223344-1234-1122-2233-112233445566`"
}
```

Use the following command to inspect the configuration of your CA.

```
`$` `aws acm-pca describe-certificate-authority \
 --certificate-authority-arn "arn:`aws`:acm-pca:`us-east-1`:`111122223333`:certificate-authority/`11223344-1234-1122-2233-112233445566`" \
 --output json`
```

This description should contain the following section.

```
"RevocationConfiguration": {
   ...
   "CrlConfiguration": {
      "Enabled": true,
      "ExpirationInDays": 7,
      "CustomCname": "`alternative.example.com`",
      "S3BucketName": "`amzn-s3-demo-bucket`",
   ...
   }
}
```

### Example 5: Create a CA and specify the usage

mode

In this example, the CA usage mode is specified when creating a CA. If
unspecified, the usage mode parameter defaults to GENERAL_PURPOSE. In this
example, the parameter is set to SHORT_LIVED_CERTIFICATE, which means that the
CA will issue certificates with a maximum validity period of seven days. In
situations where it is inconvenient to configure revocation, a short-lived
certificate that has been compromised quickly expires as part of normal
operations. Consequently, this example CA lacks a revocation mechanism.

###### Note

AWS Private CA does not perform validity checks on root CA certificates.

```
`$` `aws acm-pca create-certificate-authority \
 --certificate-authority-configuration file://`ca_config.txt` \
 --certificate-authority-type "ROOT" \
 --usage-mode SHORT_LIVED_CERTIFICATE \
 --tags Key=usageMode,Value=SHORT_LIVED_CERTIFICATE`
```

Use the [**describe-certificate-authority**](../../../cli/latest/reference/acm-pca/describe-certificate-authority.md "../../../cli/latest/reference/acm-pca/describe-certificate-authority.md") command in
the AWS CLI to display details about the resulting CA, as shown in the following
command:

```
`$` **aws acm-pca describe-certificate-authority \
 --certificate-authority-arn arn:aws:acm:`region`:`account`:certificate-authority/`CA_ID`**
```

```
{
	   "CertificateAuthority":{
	      "Arn":"arn:aws:acm-pca:`region`:`account`:certificate-authority/`CA_ID`",
	      "CreatedAt":"2022-09-30T09:53:42.769000-07:00",
	      "LastStateChangeAt":"2022-09-30T09:53:43.784000-07:00",
	      "Type":"ROOT",
	      "UsageMode":"SHORT_LIVED_CERTIFICATE",
	      "Serial":"`serial_number`",
	      "Status":"PENDING_CERTIFICATE",
	      "CertificateAuthorityConfiguration":{
	         "KeyAlgorithm":"RSA_2048",
	         "SigningAlgorithm":"SHA256WITHRSA",
	         "Subject":{
	            "Country":"`US`",
	            "Organization":"`Example Corp`",
	            "OrganizationalUnit":"`Sales`",
	            "State":"`WA`",
	            "Locality":"`Seattle`",
	            "CommonName":"`www.example.com`"
	         }
	      },
	      "RevocationConfiguration":{
	         "CrlConfiguration":{
	            "Enabled":false
	         },
	         "OcspConfiguration":{
	            "Enabled":false
	         }
	      },
	...
```

### Example 6: Create a CA for Active Directory

login

You can create a private CA suitable for use in the Enterprise NTAuth store of
Microsoft Active Directory (AD), where it can issue card-logon or
domain-controller certificates. For information about importing a CA certificate
into AD, see [How to import third-party certification authority (CA) certificates into
the Enterprise NTAuth store](https://learn.microsoft.com/en-us/troubleshoot/windows-server/windows-security/import-third-party-ca-to-enterprise-ntauth-store "https://learn.microsoft.com/en-us/troubleshoot/windows-server/windows-security/import-third-party-ca-to-enterprise-ntauth-store").

The Microsoft [certutil](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/certutil "https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/certutil") tool can be used to publish CA certificates in AD by
invoking the **-dspublish** option. A certificate published to AD
with certutil is trusted across the entire forest. Using group policy, you can
also limit trust to a subset of the entire forest, for example, a single domain
or a group of computers in a domain. For logon to work, the issuing CA must also
be published in the NTAuth store. For more information, see [Distribute Certificates to Client Computers by Using Group
Policy](https://learn.microsoft.com/en-us/windows-server/identity/ad-fs/deployment/distribute-certificates-to-client-computers-by-using-group-policy "https://learn.microsoft.com/en-us/windows-server/identity/ad-fs/deployment/distribute-certificates-to-client-computers-by-using-group-policy").

This example uses the following `ca_config_AD.txt` configuration
file.

**File: ca_config_AD.txt**

```
{
   "KeyAlgorithm":"RSA_2048",
   "SigningAlgorithm":"SHA256WITHRSA",
   "Subject":{
      "CustomAttributes":[
         {
            "ObjectIdentifier":"2.5.4.3",
            "Value":"root CA"
         },
         {
            "ObjectIdentifier":"0.9.2342.19200300.100.1.25",
            "Value":"example"
         },
         {
            "ObjectIdentifier":"0.9.2342.19200300.100.1.25",
            "Value":"com"
         }
      ]
   }
}
```

**Command**

```
`$` `aws acm-pca create-certificate-authority \
 --certificate-authority-configuration file://`ca_config_AD.txt` \
 --certificate-authority-type "ROOT" \
 --tags Key=application,Value=ActiveDirectory`
```

If successful, this command outputs the Amazon Resource Name (ARN) of the
CA.

```
{
	"CertificateAuthorityArn":"arn:`aws`:acm-pca:`us-east-1`:`111122223333`:certificate-authority/`11223344-1234-1122-2233-112233445566`"
	}
```

Use the following command to inspect the configuration of your CA.

```
`$` `aws acm-pca describe-certificate-authority \
 --certificate-authority-arn "arn:`aws`:acm-pca:`us-east-1`:`111122223333`:certificate-authority/`11223344-1234-1122-2233-112233445566`" \
 --output json`
```

This description should contain the following section.

```
...

"Subject":{
   "CustomAttributes":[
      {
         "ObjectIdentifier":"2.5.4.3",
         "Value":"root CA"
      },
      {
         "ObjectIdentifier":"0.9.2342.19200300.100.1.25",
         "Value":"example"
      },
      {
         "ObjectIdentifier":"0.9.2342.19200300.100.1.25",
         "Value":"com"
      }
   ]
}
...
```

### Example 7: Create a Matter CA with an attached CRL and the CDP

extension omitted from issued certificates

You can create a private CA suitable for issuing certificates for the Matter smart home standard. In this example, the CA configuration in `ca_config_PAA.txt` defines a Matter Product Attestation Authority (PAA)
with the Vendor ID (VID) set to FFF1.

**File: ca_config_PAA.txt**

```
{
   "KeyAlgorithm":"EC_prime256v1",
   "SigningAlgorithm":"SHA256WITHECDSA",
   "Subject":{
      "Country":"`US`",
      "Organization":"`Example Corp`",
      "OrganizationalUnit":"`SmartHome`",
      "State":"`WA`",
      "Locality":"`Seattle`",
      "CommonName":"`Example Corp Matter PAA`",
	  "CustomAttributes":[
      {
        "ObjectIdentifier":"1.3.6.1.4.1.37244.2.1",
        "Value":`"FFF1"`
      }
    ]
  }
}
```

The revocation configuration enables CRLs, and configures the CA to omit the default CDP URL from any issued certificates.

**File: revoke_config.txt**

```
{
   "CrlConfiguration":{
      "Enabled":true,
      "ExpirationInDays":`7`,
      "S3BucketName":"`amzn-s3-demo-bucket`",
	  "CrlDistributionPointExtensionConfiguration":{
		"OmitExtension":true
	  }
   }
}
```

**Command**

```
`$` `aws acm-pca create-certificate-authority \
 --certificate-authority-configuration file://`ca_config_PAA.txt` \
 --revocation-configuration file://`revoke_config.txt` \
 --certificate-authority-type "ROOT" \
 --idempotency-token `01234567` \
 --tags Key=`Name`,Value=`MyPCA-1``
```

If successful, this command outputs the Amazon Resource Name (ARN) of the
CA.

```
{
    "CertificateAuthorityArn":"arn:`aws`:acm-pca:`us-east-1`:`111122223333`:certificate-authority/`11223344-1234-1122-2233-112233445566`"
}
```

Use the following command to inspect the configuration of your CA.

```
`$` `aws acm-pca describe-certificate-authority \
 --certificate-authority-arn "arn:`aws`:acm-pca:`us-east-1`:`111122223333`:certificate-authority/`11223344-1234-1122-2233-112233445566`" \
 --output json`
```

This description should contain the following section.

```
"RevocationConfiguration": {
   ...
   "CrlConfiguration": {
      "Enabled": true,
      "ExpirationInDays": 7,
      "S3BucketName": "`amzn-s3-demo-bucket`",
	  "CrlDistributionPointExtensionConfiguration":{
		"OmitExtension":true
	  }
   },
   ...
}
...
```
