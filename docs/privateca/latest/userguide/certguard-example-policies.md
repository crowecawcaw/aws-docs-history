

# Example policies

The following examples show common certificate governance controls. Most examples are `Deny` statements that you can use in an identity-based policy, SCP, RCP, or VPC endpoint policy. The example that allows only an approved DNS name is an `Allow` statement, for example in an AWS RAM customer managed permission. Combine statements as needed, and scope them to the principals or CAs they're meant for.

## Require approved key algorithms and sizes
<a name="certguard-example-key-strength"></a>

The following policy denies keys other than RSA and EC, RSA keys shorter than 2048 bits, and EC keys that don't use P-256 or P-384. The third statement also denies EC keys with explicit parameters that don't match a known curve, because `acm-pca:x509Key/curve` is absent for those keys.

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "DenyUnapprovedKeyAlgorithms",
            "Effect": "Deny",
            "Action": "acm-pca:IssueCertificate",
            "Resource": "*",
            "Condition": {
                "StringNotEquals": {
                    "acm-pca:x509Key/algorithm": ["RSA", "EC"]
                }
            }
        },
        {
            "Sid": "DenyShortRSAKeys",
            "Effect": "Deny",
            "Action": "acm-pca:IssueCertificate",
            "Resource": "*",
            "Condition": {
                "StringEquals": {
                    "acm-pca:x509Key/algorithm": "RSA"
                },
                "NumericLessThan": {
                    "acm-pca:x509Key/size": "2048"
                }
            }
        },
        {
            "Sid": "DenyUnapprovedCurves",
            "Effect": "Deny",
            "Action": "acm-pca:IssueCertificate",
            "Resource": "*",
            "Condition": {
                "StringEquals": {
                    "acm-pca:x509Key/algorithm": "EC"
                },
                "StringNotEquals": {
                    "acm-pca:x509Key/curve": ["prime256v1", "secp384r1"]
                }
            }
        }
    ]
}
```

## Require named curves
<a name="certguard-example-named-curve"></a>

The following policy denies EC and SM2 keys that spell out explicit curve parameters instead of naming the curve.

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "DenyExplicitCurveParameters",
            "Effect": "Deny",
            "Action": "acm-pca:IssueCertificate",
            "Resource": "*",
            "Condition": {
                "StringEquals": {
                    "acm-pca:x509Key/algorithm": ["EC", "SM2"]
                },
                "Bool": {
                    "acm-pca:x509Key/namedCurve": "false"
                }
            }
        }
    ]
}
```

## Require post-quantum keys
<a name="certguard-example-post-quantum"></a>

The following policy denies subject keys that don't use ML-DSA.

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "DenyNonMLDSAKeys",
            "Effect": "Deny",
            "Action": "acm-pca:IssueCertificate",
            "Resource": "*",
            "Condition": {
                "StringNotEquals": {
                    "acm-pca:x509Key/algorithm": ["ML-DSA-44", "ML-DSA-65", "ML-DSA-87"]
                }
            }
        }
    ]
}
```

## Deny SHA-256 signatures
<a name="certguard-example-signature"></a>

The following policy denies certificates that the CA would sign with a SHA-256 based algorithm.

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "DenySha256Signatures",
            "Effect": "Deny",
            "Action": "acm-pca:IssueCertificate",
            "Resource": "*",
            "Condition": {
                "StringEquals": {
                    "acm-pca:x509Signature/algorithm": [
                        "sha256WithRSAEncryption",
                        "ecdsa-with-SHA256"
                    ]
                }
            }
        }
    ]
}
```

## Limit the validity period
<a name="certguard-example-validity"></a>

The following policy denies certificates that are valid for more than 90 days.

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "DenyLongLivedCertificates",
            "Effect": "Deny",
            "Action": "acm-pca:IssueCertificate",
            "Resource": "*",
            "Condition": {
                "NumericGreaterThan": {
                    "acm-pca:x509Validity/durationDays": "90"
                }
            }
        }
    ]
}
```

## Restrict DNS names to approved domains
<a name="certguard-example-dns"></a>

The following policy denies certificates with any DNS name outside `example.com`. The pattern `*.example.com` doesn't match `example.com` itself, so the policy lists both. Certificates with no DNS names aren't affected. To require a DNS name in an `Allow` statement, see [Allow only certificates for an approved DNS name](#certguard-example-dns-only).

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "DenyUnapprovedDomains",
            "Effect": "Deny",
            "Action": "acm-pca:IssueCertificate",
            "Resource": "*",
            "Condition": {
                "ForAnyValue:StringNotLike": {
                    "acm-pca:x509SAN/DNS": ["example.com", "*.example.com"]
                }
            }
        }
    ]
}
```

## Allow only certificates for an approved DNS name
<a name="certguard-example-dns-only"></a>

A `ForAllValues` condition is `true` when the certificate has no values for the key. In an `Allow` statement, such as one in an AWS RAM customer managed permission, a `ForAllValues:StringLike` condition on `acm-pca:x509SAN/DNS` therefore allows a certificate that has no DNS names and identifies its subject only by IP address, URI, email address, directory name, or other name. To close these gaps, combine the pattern match with `Null` conditions and a count of SAN entries.

The following policy allows a certificate only when its SAN extension has exactly one entry, that entry is a DNS name in `example.com`, and any subject common name is also in `example.com`.

```json
{
    "Version": "2012-10-17",		 	 	 
    "Statement": [
        {
            "Sid": "AllowOneApprovedDnsName",
            "Effect": "Allow",
            "Action": "acm-pca:IssueCertificate",
            "Resource": "*",
            "Condition": {
                "Null": {
                    "acm-pca:x509SAN/DNS": "false",
                    "acm-pca:x509SAN/IP": "true",
                    "acm-pca:x509SAN/URI": "true",
                    "acm-pca:x509SAN/RFC822": "true",
                    "acm-pca:x509SAN/Name/CN": "true"
                },
                "NumericEquals": {
                    "acm-pca:x509SAN/count": "1"
                },
                "ForAllValues:StringLike": {
                    "acm-pca:x509SAN/DNS": ["example.com", "*.example.com"],
                    "acm-pca:x509Subject/CN": ["example.com", "*.example.com"]
                }
            }
        }
    ]
}
```

The conditions in this policy work as follows:
+ `"acm-pca:x509SAN/DNS": "false"` requires at least one DNS name.
+ The `"true"` values for the IP address, URI, email, and directory name keys reject certificates that have any of those SAN entries.
+ Other name entries use a key for each type ID, such as `acm-pca:x509SAN/OtherName/1.3.6.1.4.1.311.20.2.3` for the Microsoft user principal name. No single `Null` condition covers every type ID. The `acm-pca:x509SAN/count` condition rejects a certificate with any SAN entry beyond the one DNS name, including other name entries of any type.
+ The `ForAllValues:StringLike` condition limits DNS names and subject common names to `example.com`. A certificate with no common name still matches. To require a common name, add `"acm-pca:x509Subject/CN": "false"` to the `Null` condition. Common names aren't lowercased, so this condition doesn't match a common name that uses different letter case.

To allow more than one DNS name, you can't use the count to exclude other name entries. Instead, add a `"true"` value to the `Null` condition for each other name type that you want to reject. The policy doesn't reject other name types that you don't list.

## Restrict the subject common name
<a name="certguard-example-common-name"></a>

The following policy denies certificates with any common name that isn't one of the listed names, in any letter case. Certificates with no common name aren't affected.

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "DenyUnapprovedCommonNames",
            "Effect": "Deny",
            "Action": "acm-pca:IssueCertificate",
            "Resource": "*",
            "Condition": {
                "ForAnyValue:StringNotEqualsIgnoreCase": {
                    "acm-pca:x509Subject/CN": ["api.example.com", "www.example.com"]
                }
            }
        }
    ]
}
```

## Restrict IP addresses to private ranges
<a name="certguard-example-ip"></a>

The following policy denies certificates with any IP address outside the private IPv4 ranges and the IPv6 unique local range.

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "DenyPublicIPAddresses",
            "Effect": "Deny",
            "Action": "acm-pca:IssueCertificate",
            "Resource": "*",
            "Condition": {
                "ForAnyValue:NotIpAddress": {
                    "acm-pca:x509SAN/IP": [
                        "10.0.0.0/8",
                        "172.16.0.0/12",
                        "192.168.0.0/16",
                        "fd00::/8"
                    ]
                }
            }
        }
    ]
}
```

## Deny code signing and OCSP signing certificates
<a name="certguard-example-eku"></a>

The following policy denies certificates that include the code signing or OCSP signing purpose. To deny purposes that RFC 5280 doesn't name, such as vendor-specific purposes, list their OIDs.

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "DenyCodeSigningAndOCSPSigning",
            "Effect": "Deny",
            "Action": "acm-pca:IssueCertificate",
            "Resource": "*",
            "Condition": {
                "ForAnyValue:StringEquals": {
                    "acm-pca:x509Ext/ExtendedKeyUsage": ["codeSigning", "OCSPSigning"]
                }
            }
        }
    ]
}
```

## Deny CA certificates for tagged principals
<a name="certguard-example-ca-certs"></a>

The following policy denies CA certificates to principals tagged `CertificateType=EndEntityOnly`. Use principal tags like this to apply different rules to different teams without separate policies for each account.

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "DenyCACertificatesForEndEntityRoles",
            "Effect": "Deny",
            "Action": "acm-pca:IssueCertificate",
            "Resource": "*",
            "Condition": {
                "Bool": {
                    "acm-pca:x509Ext/BasicConstraints/CA": "true"
                },
                "StringEquals": {
                    "aws:PrincipalTag/CertificateType": "EndEntityOnly"
                }
            }
        }
    ]
}
```

## Require a subject country
<a name="certguard-example-country"></a>

The following policy requires a subject country and denies any country other than Germany or France. You need the first statement because a `ForAnyValue` condition is `false` when the certificate has no country.

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "DenyMissingCountry",
            "Effect": "Deny",
            "Action": "acm-pca:IssueCertificate",
            "Resource": "*",
            "Condition": {
                "Null": {
                    "acm-pca:x509Subject/C": "true"
                }
            }
        },
        {
            "Sid": "DenyOtherCountries",
            "Effect": "Deny",
            "Action": "acm-pca:IssueCertificate",
            "Resource": "*",
            "Condition": {
                "ForAnyValue:StringNotEquals": {
                    "acm-pca:x509Subject/C": ["DE", "FR"]
                }
            }
        }
    ]
}
```