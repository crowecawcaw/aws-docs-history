# Update a private CA in AWS Private Certificate Authority

You can update the status of a private CA or change its [revocation configuration](revocation-setup.md "revocation-setup.md") after creating it. This
topic provides details about CA status and the CA lifecycle, along with examples of
console and CLI updates to CAs.

## Update a CA (console)

The following procedures show how to update existing CA configurations using the
AWS Management Console.

### Update CA status (console)

In this example, the status of an enabled CA is changed to disabled.

###### To update the status of a CA

1. Sign in to your AWS account and open the AWS Private CA console at
   [https://console.aws.amazon.com/acm-pca/home](https://console.aws.amazon.com/acm-pca/home "https://console.aws.amazon.com/acm-pca/home")
2. On the **Private certificate authorities** page,
   choose a private CA that is currently active from the list.
3. On the **Actions** menu, choose
   **Disable** to disable the private CA.

### Updating a CA's revocation configuration

(console)

You can update the [revocation
configuration](revocation-setup.md "revocation-setup.md") for your private CA, for example, by adding or removing
either OCSP or CRL support, or by modifying their settings.

###### Note

Changes to the revocation configuration of a CA do not affect certificates that
were already issued. For managed revocation to work, older certificates must be re-issued.

For OCSP, you change the following settings:

- Enable or disable OCSP.
- Enable or disable a custom OCSP fully qualified domain name
  (FQDN).
- Change the FQDN.

For a CRL, you can change any of the following settings:

- The CRL type (complete or partitioned)
- Whether the private CA generates a certificate revocation list
  (CRL)
- The number of days before a CRL expires. Note that AWS Private CA begins
  trying to regenerate the CRL at ½ the number of days you specify.
- The name of the Amazon S3 bucket where your CRL is saved.
- An alias to hide the name of your Amazon S3 bucket from public view.

###### Important

Changing any of the preceding parameters can have negative effects.
Examples include disabling CRL generation, changing the validity period, or
changing the S3 bucket after you have placed your private CA in production.
Such changes can break existing certificates that depend on the CRL and the
current CRL configuration. Changing the alias can be done safely as long as
the old alias remains linked to the correct bucket.

###### To update the revocation settings

1.  Sign in to your AWS account and open the AWS Private CA console at
    [https://console.aws.amazon.com/acm-pca/home](https://console.aws.amazon.com/acm-pca/home "https://console.aws.amazon.com/acm-pca/home").
2.  On the **Private certificate authorities** page,
    choose a private CA from the list. This opens the details panel for the
    CA.
3.  Choose the **Revocation configuration** tab, then
    choose **Edit**.
4.  Under **Certificate revocation options**, two options
    are displayed:

        * **Activate CRL distribution**
        * **Turn on OCSP**

    You can configure either, neither, or both of these revocation
    mechanisms for your CA. Although optional, managed revocation is
    recommended as a [best practice](ca-best-practices.md "ca-best-practices.md").
    Before completing this step, see [Plan your AWS Private CA certificate revocation method](revocation-setup.md "revocation-setup.md") for information about the
    advantages of each method, the preliminary setup that may be required,
    and additional revocation features.

5.  Select **Activate CRL
    distribution**.
6.  To create an Amazon S3 bucket for your CRL entries, select
    **Create a new S3 bucket**.
    Provide a unique bucket name. (You do not need to include the
    path to the bucket.) Otherwise, leave this option unselected and
    choose an existing bucket from the **S3 bucket
    name** list.

If you create a new bucket, AWS Private CA creates and attaches
the [required access policy](crl-planning.md#s3-policies "crl-planning.md#s3-policies") to
it. If you decide to use an existing bucket, you must attach an
access policy it before you can begin generating CRLs. Use one
of the policy patterns described in [Access policies for CRLs in Amazon S3](crl-planning.md#s3-policies "crl-planning.md#s3-policies") . For information about
attaching a policy, see [Adding a bucket policy by using the Amazon S3
console](../../../AmazonS3/latest/user-guide/add-bucket-policy.md "../../../AmazonS3/latest/user-guide/add-bucket-policy.md").

###### Note

When you are using the AWS Private CA console, an attempt to
create a CA fails if both of the following conditions
apply:

    * You are enforcing Block Public Access settings on
     your Amazon S3 bucket or account.
    * You asked AWS Private CA to create an Amazon S3 bucket
     automatically.In this situation, the console attempts, by default, to

create a publicly accessible bucket, and Amazon S3 rejects this
action. Check your Amazon S3 settings if this occurs. For more
information, see [Blocking public access to your Amazon S3
storage](../../../AmazonS3/latest/userguide/access-control-block-public-access.md "../../../AmazonS3/latest/userguide/access-control-block-public-access.md"). 3. Expand **Advanced** for
additional configuration options.

    * Choose **Enable partitioning**
     to enable partitioning of CRLs. If you don't enable partitioning,
     your CA is subject to the maximum number of revoked certificates,
     shown on the [AWS Private Certificate Authority quotas](../../../general/latest/gr/pca.md#limits_pca "../../../general/latest/gr/pca.md#limits_pca").
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

4. Choose **Save changes** when done.
1. On the **Certificate revocation** page,
   choose **Turn on OCSP**.
1. (Optional) In the **Custom OCSP endpoint**
   field, provide a fully qualified domain name (FQDN) for your
   OCSP endpoint. To use OCSP over IPv6, set this field to a dualstack endpoint
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
prefix such as "http://" or "https://". 3. Choose **Save changes** when done.

## Updating a CA (CLI)

The following procedures show how to update the status and [revocation configuration](revocation-setup.md "revocation-setup.md") of an existing CA
using the AWS CLI.

###### Note

Changes to the revocation configuration of a CA do not affect certificates that
were already issued. For managed revocation to work, older certificates must be re-issued.

###### To update the status of your private CA (AWS CLI)

Use the [update-certificate-authority](../../../cli/latest/reference/acm-pca/update-certificate-authority.md "../../../cli/latest/reference/acm-pca/update-certificate-authority.md") command.

This is useful when you have an existing CA with status `DISABLED` that
you want to set to `ACTIVE`. To begin, confirm the initial status of the
CA with the following command.

```
`$` `aws acm-pca describe-certificate-authority \
 --certificate-authority-arn "arn:`aws`:acm-pca:`us-east-1`:`111122223333`:certificate-authority/`11223344-1234-1122-2233-112233445566`" \
 --output json`
```

This results in output similar to the following.

```
{
    "CertificateAuthority": {
        "Arn": "arn:`aws`:acm-pca:`us-east-1`:`111122223333`:certificate-authority/`11223344-1234-1122-2233-112233445566`",
        "CreatedAt": "2021-03-05T14:24:12.867000-08:00",
        "LastStateChangeAt": "2021-03-08T13:17:40.221000-08:00",
        "Type": "ROOT",
        "Serial": "`serial_number`",
        "Status": "DISABLED",
        "NotBefore": "2021-03-08T07:46:27-08:00",
        "NotAfter": "2022-03-08T08:46:27-08:00",
        "CertificateAuthorityConfiguration": {
            "KeyAlgorithm": "RSA_2048",
            "SigningAlgorithm": "SHA256WITHRSA",
            "Subject": {
                "Country": "US",
                "Organization": "Example Corp",
                "OrganizationalUnit": "Sales",
                "State": "WA",
                "CommonName": "www.example.com",
                "Locality": "Seattle"
            }
        },
        "RevocationConfiguration": {
            "CrlConfiguration": {
                "Enabled": true,
                "ExpirationInDays": 7,
                "CustomCname": "alternative.example.com",
                "S3BucketName": "`amzn-s3-demo-bucket`"
			},
            "OcspConfiguration": {
                "Enabled": false
            }
        }
    }
}
```

The following command sets the status of the private CA to `ACTIVE`.
This is possible only if a valid certificate is installed on the CA.

```
`$` `aws acm-pca update-certificate-authority \
 --certificate-authority-arn arn:`aws`:acm-pca:`us-east-1`:`111122223333`:certificate-authority/`11223344-1234-1122-2233-112233445566` \
 --status "ACTIVE"`
```

Inspect the new status of the CA.

```
`$` `aws acm-pca describe-certificate-authority \
 --certificate-authority-arn "arn:`aws`:acm-pca:`us-east-1`:`111122223333`:certificate-authority/`11223344-1234-1122-2233-112233445566`" \
 --output json`
```

The status now appears as `ACTIVE`.

```
{
    "CertificateAuthority": {
        "Arn": "arn:`aws`:acm-pca:`us-east-1`:`111122223333`:certificate-authority/`11223344-1234-1122-2233-112233445566`",
        "CreatedAt": "2021-03-05T14:24:12.867000-08:00",
        "LastStateChangeAt": "2021-03-08T13:23:09.352000-08:00",
        "Type": "ROOT",
        "Serial": "`serial_number`",
        "Status": "ACTIVE",
        "NotBefore": "2021-03-08T07:46:27-08:00",
        "NotAfter": "2022-03-08T08:46:27-08:00",
        "CertificateAuthorityConfiguration": {
            "KeyAlgorithm": "RSA_2048",
            "SigningAlgorithm": "SHA256WITHRSA",
            "Subject": {
                "Country": "US",
                "Organization": "Example Corp",
                "OrganizationalUnit": "Sales",
                "State": "WA",
                "CommonName": "www.example.com",
                "Locality": "Seattle"
            }
        },
        "RevocationConfiguration": {
            "CrlConfiguration": {
                "Enabled": true,
                "ExpirationInDays": 7,
                "CustomCname": "alternative.example.com",
                "S3BucketName": "`amzn-s3-demo-bucket`"
            },
            "OcspConfiguration": {
                "Enabled": false
            }
        }
    }
}
```

In some cases, you might have an active CA with no revocation mechanism
configured. If you want to begin using a certificate revocation list (CRL), use the
following procedure.

###### To add a CRL to an existing CA (AWS CLI)

1. Use the following command to inspect the current status of the CA.

```
`$` `aws acm-pca describe-certificate-authority
 --certificate-authority-arn arn:`aws`:acm-pca:`us-east-1`:`111122223333`:certificate-authority/`11223344-1234-1122-2233-112233445566`
 --output json`
```

The output confirms that the CA has status `ACTIVE` but is not
configured to use a CRL.

```
{
    "CertificateAuthority": {
        "Arn": "arn:`aws`:acm-pca:`us-east-1`:`111122223333`:certificate-authority/`11223344-1234-1122-2233-112233445566`",
        "CreatedAt": "2021-03-08T14:36:26.449000-08:00",
        "LastStateChangeAt": "2021-03-08T14:50:52.224000-08:00",
        "Type": "ROOT",
        "Serial": "`serial_number`",
        "Status": "ACTIVE",
        "NotBefore": "2021-03-08T13:46:50-08:00",
        "NotAfter": "2022-03-08T14:46:50-08:00",
        "CertificateAuthorityConfiguration": {
            "KeyAlgorithm": "RSA_2048",
            "SigningAlgorithm": "SHA256WITHRSA",
            "Subject": {
                "Country": "US",
                "Organization": "Example Corp",
                "OrganizationalUnit": "Sales",
                "State": "WA",
                "CommonName": "www.example.com",
                "Locality": "Seattle"
            }
        },
        "RevocationConfiguration": {
            "CrlConfiguration": {
                "Enabled": false
            },
            "OcspConfiguration": {
                "Enabled": false
            }
        }
    }
}
```

2. Create and save a file with a name such as
   `revoke_config.txt` to define your CRL configuration
   parameters.

```
{
   "CrlConfiguration":{
      "Enabled": true,
      "ExpirationInDays": `7`,
      "S3BucketName": "`amzn-s3-demo-bucket`"
   }
}
```

###### Note

When updating a Matter device attestation CA to enable CRLs, you must configure it to omit the CDP extension from the issued certificates to help conform to the current Matter standard. To do this, define your CRL configuration
parameters as illustrated below:

```
{
   "CrlConfiguration":{
      "Enabled": true,
      "ExpirationInDays": `7`,
      "S3BucketName": "`amzn-s3-demo-bucket`"
      "CrlDistributionPointExtensionConfiguration":{
         "OmitExtension": true
      }
   }
}
```

3. Use the [update-certificate-authority](../../../cli/latest/reference/acm-pca/update-certificate-authority.md "../../../cli/latest/reference/acm-pca/update-certificate-authority.md") command and the revocation
   configuration file to update the CA.

```
`$` `aws acm-pca update-certificate-authority \
 --certificate-authority-arn arn:`aws`:acm-pca:`us-east-1`:`111122223333`:certificate-authority/`11223344-1234-1122-2233-112233445566` \
 --revocation-configuration file://`revoke_config.txt``
```

4. Again inspect the status of the CA.

```
`$` `aws acm-pca describe-certificate-authority
 --certificate-authority-arn arn:`aws`:acm-pca:`us-east-1`:`111122223333`:certificate-authority/`11223344-1234-1122-2233-112233445566`
 --output json`
```

The output confirms that CA is now configured to use a CRL.

```
{
    "CertificateAuthority": {
        "Arn": "arn:`aws`:acm-pca:`us-east-1`:`111122223333`:certificate-authority/`11223344-1234-1122-2233-112233445566`",
        "CreatedAt": "2021-03-08T14:36:26.449000-08:00",
        "LastStateChangeAt": "2021-03-08T14:50:52.224000-08:00",
        "Type": "ROOT",
        "Serial": "`serial_number`",
        "Status": "ACTIVE",
        "NotBefore": "2021-03-08T13:46:50-08:00",
        "NotAfter": "2022-03-08T14:46:50-08:00",
        "CertificateAuthorityConfiguration": {
            "KeyAlgorithm": "RSA_2048",
            "SigningAlgorithm": "SHA256WITHRSA",
            "Subject": {
                "Country": "US",
                "Organization": "Example Corp",
                "OrganizationalUnit": "Sales",
                "State": "WA",
                "CommonName": "www.example.com",
                "Locality": "Seattle"
            }
        },
        "RevocationConfiguration": {
            "CrlConfiguration": {
                "Enabled": true,
                "ExpirationInDays": 7,
                "S3BucketName": "`amzn-s3-demo-bucket`",
            },
            "OcspConfiguration": {
                "Enabled": false
            }
        }
    }
}
```

In some cases, you might want to add OCSP revocation support instead of
enabling a CRL as in the previous procedure. In that case, use the following
steps.

###### To add OCSP support to an existing CA (AWS CLI)

1. Create and save a file with a name such as
   `revoke_config.txt` to define your OCSP
   parameters.

```
{
   "OcspConfiguration":{
      "Enabled":true
   }
}
```

2. Use the [update-certificate-authority](../../../cli/latest/reference/acm-pca/update-certificate-authority.md "../../../cli/latest/reference/acm-pca/update-certificate-authority.md") command and the revocation
   configuration file to update the CA.

```
`$` `aws acm-pca update-certificate-authority \
 --certificate-authority-arn arn:`aws`:acm-pca:`us-east-1`:`111122223333`:certificate-authority/`11223344-1234-1122-2233-112233445566` \
 --revocation-configuration file://`revoke_config.txt``
```

3. Again inspect the status of the CA.

```
`$` `aws acm-pca describe-certificate-authority
 --certificate-authority-arnarn:`aws`:acm-pca:`us-east-1`:`111122223333`:certificate-authority/`11223344-1234-1122-2233-112233445566`
 --output json`
```

The output confirms that CA is now configured to use OCSP.

```
{
    "CertificateAuthority": {
        "Arn": "arn:`aws`:acm-pca:`us-east-1`:`111122223333`:certificate-authority/`11223344-1234-1122-2233-112233445566`",
        "CreatedAt": "2021-03-08T14:36:26.449000-08:00",
        "LastStateChangeAt": "2021-03-08T14:50:52.224000-08:00",
        "Type": "ROOT",
        "Serial": "`serial_number`",
        "Status": "ACTIVE",
        "NotBefore": "2021-03-08T13:46:50-08:00",
        "NotAfter": "2022-03-08T14:46:50-08:00",
        "CertificateAuthorityConfiguration": {
            "KeyAlgorithm": "RSA_2048",
            "SigningAlgorithm": "SHA256WITHRSA",
            "Subject": {
                "Country": "US",
                "Organization": "Example Corp",
                "OrganizationalUnit": "Sales",
                "State": "WA",
                "CommonName": "www.example.com",
                "Locality": "Seattle"
            }
        },
        "RevocationConfiguration": {
            "CrlConfiguration": {
                "Enabled": false
            },
            "OcspConfiguration": {
                "Enabled": true
            }
        }
    }
}
```

###### Note

You can also configure both CRL and OCSP support on a CA.
