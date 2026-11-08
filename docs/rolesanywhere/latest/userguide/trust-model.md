

# The IAM Roles Anywhere trust model
<a name="trust-model"></a>

 AWS Identity and Access Management Roles Anywhere works by bridging the trust model of IAM and Public Key Infrastructure (PKI). The model connects the role, the IAM Roles Anywhere service principal, and identities encoded in X.509 certificates, that are issued by a Certificate Authority (CA). 

## Role trusts
<a name="role-trusts"></a>

To use an IAM role with IAM Roles Anywhere, you must create a trust relationship with the IAM Roles Anywhere service principal `rolesanywhere.amazonaws.com`. To create the trust relationship, you create a  *trust policy*, a JSON policy document. The policy must grant the permissions: 
+ `sts:AssumeRole`
+ `sts:SetSourceIdentity`
+ `sts:TagSession`

Sessions issued by IAM Roles Anywhere have the source identity set to the common name(s) (CN) of the subject(s) you use in end-entity certificate(s) authenticating to the target role. IAM Roles Anywhere extracts values from the subject, issuer, and Subject Alternative Name (SAN) fields of the authenticating certificate and makes them available for policy evaluation via the sourceIdentity and principal tags. The [sts:SourceIdentity](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_iam-condition-keys.html#ck_sourceidentity) key is present in the request when IAM Roles Anywhere initially sets the source identity while assuming a role. You can apply more authorization constraints by using condition clauses in the policy statement. The tags will also be evaluated against policies on any resources accessed with the issued session. 

Additionally, sessions issued by AWS have a Session Name property that is used as part of the assumed role ARN. IAM Roles Anywhere sets this automatically, using the hex-encoded serial number of the authenticating certificate.

To examine the contents of a certificate, use the following command: 

```
$openssl x509 -text -noout -in certificate.pem
```

```
      Certificate:
      Data:
          Version: 3 (0x2)
          Serial Number:
              1f:71:c5:11:4a:11:9f:c0:cc:5a:5a:52:fb:37:20:ad
      Signature Algorithm: sha256WithRSAEncryption
          Issuer: C=US, O=Amazon, OU=IAM, ST=Washington, CN=Roles Anywhere, L=Seattle
          Validity
              Not Before: Apr 20 14:13:43 2022 GMT
              Not After : Jan 10 15:13:43 2023 GMT
          Subject: CN=awsUser
          # remainder omitted...
```

In this case, the value `awsUser` becomes the source identity. The values from the `Issuer` field become principal tags in the resulting session. 

For more information, see:
+ [IAM roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html)
+ [IAM roles terms and concepts: trust policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_terms-and-concepts.html#term_trust-policy)
+ [Policies and permissions in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html)
+ [Things to know about source identity](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_control-access_monitor.html#id_credentials_temp_control-access_monitor-know)
+ [Passing session tags in AWS Security Token Service](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_session-tags.html)

## Signature validation
<a name="signature-verification"></a>

To authenticate a request for credentials, IAM Roles Anywhere validates the incoming signature by using the signature validation algorithm required by the key type of the certificate, for example RSA or ECDSA. After validating the signature, IAM Roles Anywhere checks that the certificate was issued by a certificate authority configured as a trust anchor in the account using algorithms defined by public key infrastructure X.509 (PKIX) standards. 

End entity certificates must satisfy the following constraints to be used for authentication: 
+ The certificates MUST be X.509v3.
+ If the `CA` field is present in the basic constraints extension, its value MUST be `false`.
+ The key usage MUST include `Digital Signature`.
+ The signing algorithm MUST include `SHA256` or stronger. `MD5` and `SHA1` signing algorithms are rejected.

Certificates used as trust anchors must satisfy the same requirements for signature algorithm, but with the following differences: 
+ The key usage MUST include `Certificate Sign`, and MAY include `CRL Sign`. Certificate Revocation Lists (CRLs) are an optional feature of IAM Roles Anywhere.
+ Basic constraints MUST include `CA: true`.

**Important**  
For AWS Private CA trust anchors, only the validity period can be modified after creation. When the validity period changes, you must call UpdateTrustAnchor to register this change. IAM Roles Anywhere honors certificates based on the validity period found during the most recent TrustAnchor Create/Update event.

## Trust policy
<a name="trust-policy"></a>

Temporary credentials for IAM roles are issued to IAM Roles Anywhere clients via the API method `CreateSession`. For the call to be authorized, the target role of the `CreateSession` API call must have an Assume Role Policy Document to trust the IAM Roles Anywhere service principal (`rolesanywhere.amazonaws.com`).

**Important**  
It is also recommended to have additional condition statements to further restrict authorization based on attributes that are extracted from the X.509 certificate. 

When you use X.509 certificates, IAM Roles Anywhere extracts the following fields and makes them available as `PrincipalTag` elements in the session:
+ `Subject`
+ `Issuer`
+ `Subject Alternative Name (SAN)`

These values need to match the pattern defined in [STS session tags](https://docs.aws.amazon.com/STS/latest/APIReference/API_Tag.html). The service ignores values that do not match this pattern. You cannot use these values in policy conditions.

**Note**  
These tags are also available to be used in conditions in the identity-based policy attached to the role.

 **Certificate Subject fields mapping** 

 IAM Roles Anywhere maps Relative Distinguished Names (RDNs) from an authenticating certificate's Subject into distinct `PrincipalTag` elements in the session.

 The following example shows a trust policy that adds a condition based on the `Subject Common Name (CN)` of the certificate. For example, if the identity asserted in the certificate is `Alice`, a condition can be created on the `CN` of the Subject.

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
      {
        "Effect": "Allow",
        "Principal": {
          "Service": "rolesanywhere.amazonaws.com"
        },
        "Action": [
          "sts:AssumeRole",
          "sts:TagSession",
          "sts:SetSourceIdentity"
        ],
        "Condition": {
          "StringEquals": {
            "aws:PrincipalTag/x509Subject/CN": "Alice"
          },
          "ArnEquals": {
            "aws:SourceArn": [
              "arn:aws:rolesanywhere:{{us-east-1}}:{{123456789012}}:trust-anchor/{{TA_ID}}"
            ]
          }
        }
      }
    ]
  }
```

------

 **Certificate Issuer fields mapping** 

 IAM Roles Anywhere maps RDNs from an authenticating certificate’s Issuer into distinct `PrincipalTag` elements in the session.

 The following example shows a trust policy that adds a condition based on the `Issuer Common Name (CN)` of the certificate. For example, if the issuer identity asserted in the certificate is `Bob`, a condition can be created on the `CN` of the Issuer.

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
      {
        "Effect": "Allow",
        "Principal": {
          "Service": "rolesanywhere.amazonaws.com"
        },
        "Action": [
          "sts:AssumeRole",
          "sts:TagSession",
          "sts:SetSourceIdentity"
        ],
        "Condition": {
          "StringEquals": {
            "aws:PrincipalTag/x509Issuer/CN": "Bob"
          },
          "ArnEquals": {
            "aws:SourceArn": [
              "arn:aws:rolesanywhere:{{us-east-1}}:{{123456789012}}:trust-anchor/{{TA_ID}}"
            ]
          }
        }
      }
    ]
  }
```

------

 **Certificate Subject Alternative Name (SAN) fields mapping** 

X.509v3 certificates may include an extension to define additional identities, call Subject Alternative Names (SANs). The SAN can have multiple values, each of which can be one of nine types – Domain Name System (DNS) names, Uniform Resource Indicators (URIs), Directory Names, IP addresses, "Other" names, EDI party names, X400 addresses, RFC 822 names, or registered OIDs. IAM Roles Anywhere will map the **first** value of the following types: `DNS Names`, `Directory Name (DN)`, and `URI Names`. The resulting tags will be prefixed with x509SAN, with a corresponding type code. The type code will be one of DNS, URI, or Name. For values of type DN, the individual RDNs will be parsed, as with Subject and Issuer.

```
      Certificate:
      Data:
          Version: 3 (0x2)
          Serial Number:
              1f:71:c5:11:4a:11:9f:c0:cc:5a:5a:52:fb:37:20:ad
      Signature Algorithm: sha256WithRSAEncryption
          Issuer: C=US, O=Amazon, OU=IAM, ST=Washington, CN=RolesAnywhere, L=Seattle
          Validity
              Not Before: Apr 20 14:13:43 2022 GMT
              Not After : Jan 10 15:13:43 2023 GMT
          Subject: CN=Alice
          X509v3 extensions:
            X509v3 Subject Alternative Name:
                DNS:example.com,
                URI:spiffe://example.com/workload/alice,
                DirName:/CN=Alice
          # remainder omitted...
```

For the above certificate, the session principal tags and the SAN fields will look like the following:

```
        "aws:PrincipalTag/x509Subject/CN": "Alice",
        "aws:PrincipalTag/x509Issuer/C": "US",
        "aws:PrincipalTag/x509Issuer/O": "Amazon",
        "aws:PrincipalTag/x509Issuer/OU": "IAM",
        "aws:PrincipalTag/x509Issuer/ST": "Washington",
        "aws:PrincipalTag/x509Issuer/L": "Seattle",
        "aws:PrincipalTag/x509Issuer/CN": "RolesAnywhere",
        "aws:PrincipalTag/x509SAN/DNS": "example.com",
        "aws:PrincipalTag/x509SAN/URI": "spiffe://example.com/workload/alice",
        "aws:PrincipalTag/x509SAN/Name/CN": "Alice"
        // Additional principal tags may be available...
```

Some X.509 certificate fields can contain multiple values. For example, a Subject can have multiple Organization Unit (OU) values in the certificate. Because principal tags do not support multiple values, IAM Roles Anywhere combines multiple values into a single string, separating them with forward slashes (/) in the order they appear in the certificate.

For example, consider a certificate with these Subject values:

```
CN=alice, OU=Security, OU=Engineering, OU=Research
```

IAM Roles Anywhere creates the following principal tag:

```
"aws:PrincipalTag/x509Subject/OU": "Security/Engineering/Research"
```

This same behavior applies to any certificate field that contains multiple values. The order of values in the principal tag matches their order in the certificate.

 The following example shows a trust policy that adds a condition based on the `SAN` fields of the certificate.

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
      {
        "Effect": "Allow",
        "Principal": {
          "Service": "rolesanywhere.amazonaws.com"
        },
        "Action": [
          "sts:AssumeRole",
          "sts:TagSession",
          "sts:SetSourceIdentity"
        ],
        "Condition": {
          "StringEquals": {
            "aws:PrincipalTag/x509SAN/DNS": "example.com",
            "aws:PrincipalTag/x509SAN/URI": "spiffe://example.com/workload/alice",
            "aws:PrincipalTag/x509SAN/Name/CN": "Alice"
          },
          "ArnEquals": {
            "aws:SourceArn": [
              "arn:aws:rolesanywhere:{{us-east-1}}:{{123456789012}}:trust-anchor/{{TA_ID}}"
            ]
          }
        }
      }
    ]
  }
```

------

**Note**  
[RFC 5280](https://datatracker.ietf.org/doc/html/rfc5280) allows certificates with empty subjects if and only if the SAN extension is present and marked critical. Certificates with empty subjects are NOT yet supported, since IAM Roles Anywhere uses the certificate subject as the key of the Subject resource to visualize and audit activities for certificates that are authenticated with IAM Roles Anywhere. For more information about Subject resource, see [Monitoring with IAM Roles Anywhere subjects](monitoring-subjects.md).

 **Using the `aws:SourceArn` or `aws:SourceAccount` or `sts:SourceIdentity` condition keys** 

 In general, it is strongly recommended that you use the [aws:SourceArn](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-sourceaccount) or the [aws:SourceAccount](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-sourcearn) global condition keys or the [sts:SourceIdentity](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_iam-condition-keys.html#ck_sourceidentity) condition key in your role trust policies. This combination of conditions implements least privilege permissions and prevents IAM Roles Anywhere from acting as a potential [confused deputy](https://docs.aws.amazon.com/IAM/latest/UserGuide/confused-deputy.html). When a client obtains temporary security credentials from IAM Roles Anywhere, the `aws:SourceArn` and `aws:SourceAccount` will be set based on the ARN of the trust anchor specified in the call to `CreateSession`.

 To use the `aws:SourceArn` and `aws:SourceAccount` global condition keys, set the value to the Amazon Resource Name (ARN) or account of the trust anchor that you expect to use for authentication. As an example, consider the following role trust policy. 

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
      {
        "Effect": "Allow",
        "Principal": {
          "Service": "rolesanywhere.amazonaws.com"
        },
        "Action": [
          "sts:AssumeRole",
          "sts:TagSession",
          "sts:SetSourceIdentity"
        ],
        "Condition": {
          "ArnEquals": {
            "aws:SourceArn": [
              "arn:aws:rolesanywhere:{{us-east-1}}:{{123456789012}}:trust-anchor/{{TA_ID}}"
            ]
          },
          "StringEquals": {
            "aws:PrincipalTag/x509Issuer/CN": "{{YourCN}}"
          }
        }
      }
    ]
  }
```

------

 To use the `sts:SourceIdentity` condition key, set the source identity prefix and source identity value according to the following [rules](#source-identity-rules). As an example, consider the following role trust policy. 

------
#### [ JSON ]

****  

```
{
  "Version":"2012-10-17",		 	 	 
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": "rolesanywhere.amazonaws.com"
      },
      "Action": [
        "sts:AssumeRole",
        "sts:SetSourceIdentity"
      ],
      "Condition": {
        "StringEquals": {
          "sts:SourceIdentity": [
            "{{${sourceIdentityPrefix}${sourceIdentityValue}}}"
          ]
        },
        "ArnEquals": {
          "aws:SourceArn": [
            "arn:aws:rolesanywhere:{{us-east-1}}:{{123456789012}}:trust-anchor/{{TA_ID}}"
          ]
        }
      }
    },
    {
      "Effect": "Allow",
      "Principal": {
        "Service": "rolesanywhere.amazonaws.com"
      },
      "Action": [
        "sts:TagSession"
      ],
      "Condition": {
        "StringEquals": {
          "aws:PrincipalTag/x509Issuer/CN": "{{YourCN}}"
        }
      }
    }
  ]
}
```

------

## Source identity rules
<a name="source-identity-rules"></a>

 We define a source identity prefix as follows: 
+ `"CN="`: the common name of the subject in the certificate is set and less than or equal to 61 characters.
+ `"ID="`: the common name of the subject in the certificate is not set. This value is left-padded with zero to be even in length.
+ `""` (empty string): the common name of the subject in the certificate is set and has a length from 62 to 256 characters.

IAM Roles Anywhere does not support subject common names longer than 256 characters, and the `CreateSession` request fails.

Hex encoding example:
+ Decimal serial number 291 converts to hex 123, which becomes `ID=0123`
+ Decimal serial number 17767 converts to hex 4567, which becomes `ID=4567`

## Revocation
<a name="revocation"></a>

A certificate authority (CA) can *revoke* a certificate when it is compromised or is no longer trusted, even though the certificate has not yet expired. With IAM Roles Anywhere, you can check whether the certificate that a workload uses to authenticate has been revoked and, if it has, prevent credentials from being issued for it. You have two ways to check revocation status:
+ **Import certificate revocation lists (CRLs) yourself.** You upload the CRLs that your CA generates, and IAM Roles Anywhere checks authenticating certificates against them.
+ **Turn on automatic revocation checking.** With this option, you don't need any per-certificate setup. Automatic revocation checking reads the CRL distribution point URLs in your certificates, downloads the CRLs, and checks revocation status for you.

You can use either approach on its own, or both together. When you use both, a certificate that appears on either list is treated as revoked.

You can't use the Online Certificate Status Protocol (OCSP) to check revocation status with IAM Roles Anywhere.

**Topics**
+ [Imported certificate revocation lists](#imported-crls)
+ [Automatic revocation checking with CRL distribution points](#crl-distribution-point-revocation)

### Imported certificate revocation lists
<a name="imported-crls"></a>

You can import a CRL that is generated from your CA using the [ImportCrl](https://docs.aws.amazon.com/rolesanywhere/latest/APIReference/API_ImportCrl.html) API or the [import-crl](https://docs.aws.amazon.com/cli/latest/reference/rolesanywhere/import-crl.html) CLI command. IAM Roles Anywhere then checks the certificates used for authentication against the CRLs that you imported. IAM Roles Anywhere uses an imported CRL only for certificates that are issued by the same CA that issued and signed the CRL. You can't use indirect CRLs, which are issued by a different entity. You can import CRLs only through the API and CLI.

**Important**  
IAM Roles Anywhere does not check the expiration date of a CRL that you import. IAM Roles Anywhere continues to use an imported CRL for revocation checks even after the CRL's `nextUpdate` date has passed. To make sure that revocation checks reflect the current state of your CA, re-import your CRL whenever your CA publishes an updated version.

### Automatic revocation checking with CRL distribution points
<a name="crl-distribution-point-revocation"></a>

Many certificate authorities add one or more URLs to every certificate they issue. Each URL points to the CA's current CRL. These URLs are called *CRL distribution points (CDPs)*. When automatic revocation checking is turned on, IAM Roles Anywhere reads the distribution point URLs directly from the certificates presented during authentication, downloads the matching CRLs, and checks whether a certificate has been revoked. Because the distribution points are read from the certificate, you don't import or register them.

**Note**  
Because IAM Roles Anywhere discovers these distribution points automatically from your certificates, they are not created as resources in your account. You can't view or manage individual distribution points.

**Turn on automatic revocation checking**

Automatic revocation checking is controlled by a setting on the trust anchor, named `crlDpRevocationEnabled`. This setting is turned off (`false`) by default, so no automatic revocation checking happens until you turn it on. To use automatic revocation checking, set `crlDpRevocationEnabled` to `true` on the trust anchor that authenticates your certificates. The setting applies to every request that authenticates against that trust anchor.

**Which distribution points are checked**

IAM Roles Anywhere ignores the following distribution points. Ignoring them doesn't cause a request to be denied.
+ URLs that don't use the HTTP or HTTPS scheme, such as LDAP URLs.
+ Distribution points that include a CRL issuer field. For more information, see [Indirect CRLs](#indirect-crls).
+ HTTP or HTTPS URLs beyond the first five in a certificate. IAM Roles Anywhere checks at most five distribution point URLs for each certificate.

IAM Roles Anywhere checks every other distribution point URL in the certificate.

**Requirements for the distribution points that are checked**

Each distribution point that IAM Roles Anywhere checks must meet all of the following requirements:
+ The URL is no longer than 2,048 characters.
+ The URL uses the default port for its scheme: port 80 for HTTP or port 443 for HTTPS.
+ The URL's host name resolves to public IP addresses and is reachable from the internet.
+ The URL returns the CRL directly. IAM Roles Anywhere does not follow redirects.
+ The URL responds promptly.
+ The URL returns a single CRL that is at most 1 MB in size.

If a distribution point that IAM Roles Anywhere checks doesn't meet these requirements and IAM Roles Anywhere doesn't have a valid CRL from an earlier download, IAM Roles Anywhere can't confirm revocation status, and the `CreateSession` request is denied.

**What happens during CreateSession**

When automatic revocation checking is turned on for a trust anchor, each time a workload calls `CreateSession` with a certificate, IAM Roles Anywhere does the following for each certificate in the chain, for each distribution point that it checks:
+ Obtains the current CRL for the distribution point.
+ Confirms that the CRL was issued and signed by the CA that issued the certificate, and that the CRL has not passed its `nextUpdate` date.
+ Checks whether the certificate appears on that list. If the certificate has been revoked, IAM Roles Anywhere denies the request and does not issue credentials.

If IAM Roles Anywhere can't obtain a valid CRL for any distribution point that it checks, the `CreateSession` request is denied. This behavior makes sure that credentials are not issued when revocation status can't be confirmed.

**Note**  
The first time IAM Roles Anywhere encounters a distribution point URL, it downloads the CRL during the `CreateSession` request, which can add latency to that request.

<a name="indirect-crls"></a>**Indirect CRLs**

An *indirect certificate revocation list (CRL)* is a CRL that is issued by an entity other than the CA that issued the certificate. A certificate signals an indirect CRL by including a CRL issuer (`cRLIssuer`) field in its distribution point. Automatic revocation checking supports only CRLs that are issued and signed by the same CA that issued the certificate.
+ IAM Roles Anywhere skips any distribution point that includes a CRL issuer field.
+ If a distribution point does not include a CRL issuer field but the CRL it returns is issued or signed by a different entity than the certificate's CA, IAM Roles Anywhere can't confirm revocation status and denies the request.

**How IAM Roles Anywhere keeps CRLs up to date**

IAM Roles Anywhere periodically refreshes the CRLs it obtains from your distribution points. After your CA publishes an updated CRL, it can take up to 30 minutes for IAM Roles Anywhere to use it for revocation checks.

IAM Roles Anywhere honors the `nextUpdate` date in each CRL. As long as a CRL is still within its `nextUpdate` date, IAM Roles Anywhere continues to use it even if a later refresh fails, so a temporary problem reaching your distribution point does not immediately fail revocation checks. Once a CRL has passed its `nextUpdate` date, IAM Roles Anywhere no longer uses it: if IAM Roles Anywhere can't obtain a current CRL to replace it, the revocation status can't be confirmed and the `CreateSession` request is denied. A CRL that does not specify a `nextUpdate` date is not treated as expired. Make sure your CA publishes an updated CRL at each distribution point before the previous CRL reaches its `nextUpdate` date.

**AWS Private CA trust anchors**

If you use AWS Private Certificate Authority (AWS Private CA) to issue your certificates, AWS Private CA publishes each CRL in an Amazon S3 bucket. Make sure that the CRL location in your AWS Private CA configuration meets the requirements for the distribution points that are checked, including being publicly accessible from the internet. For more information, see [Planning a certificate revocation list (CRL)](https://docs.aws.amazon.com/privateca/latest/userguide/crl-planning.html) in the *AWS Private CA User Guide*.