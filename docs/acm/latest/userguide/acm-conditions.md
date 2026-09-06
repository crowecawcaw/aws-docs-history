

# Use condition keys with ACM
<a name="acm-conditions"></a>

AWS Certificate Manager uses AWS Identity and Access Management (IAM)[ condition keys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition.html) to limit access to certificate requests. With condition keys from IAM policies or Service Control Policies (SCP) you can create certificate requests that conform to your organization's guidelines. 

**Note**  
Combine ACM condition keys with AWS [ global condition keys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html) such as `aws:PrincipalArn` to further restrict actions to specific users or roles.

## Supported conditions for ACM
<a name="acm-conditions-supported"></a>

Use the scroll bars to see the rest of the table.


**ACM API operations and supported conditions**  

| Condition Key | Supported ACM API Operations | Type | Description | 
| --- | --- | --- | --- | 
| `acm:ValidationMethod` | [RequestCertificate](https://docs.aws.amazon.com/acm/latest/APIReference/API_RequestCertificate.html) | String (`DNS`, `EMAIL`, `HTTP`) | Filter requests based on ACM [validation method](https://docs.aws.amazon.com/acm/latest/userguide/domain-ownership-validation.html) | 
| `acm:DomainNames` | [RequestCertificate](https://docs.aws.amazon.com/acm/latest/APIReference/API_RequestCertificate.html) | ArrayOfString | Filter based on [domain names](https://docs.aws.amazon.com/acm/latest/userguide/acm-concepts.html#concept-dn) in the ACM request | 
| `acm:KeyAlgorithm` | [RequestCertificate](https://docs.aws.amazon.com/acm/latest/APIReference/API_RequestCertificate.html) | String | Filter requests based on ACM [key algorithm and size](https://docs.aws.amazon.com/acm/latest/userguide/acm-certificate.html#algorithms) | 
| `acm:CertificateTransparencyLogging` | [RequestCertificate](https://docs.aws.amazon.com/acm/latest/APIReference/API_RequestCertificate.html) | String (`ENABLED`, `DISABLED`) | Deprecated. This condition will continue to be enforced but [certificate transparency logging](https://docs.aws.amazon.com/acm/latest/userguide/acm-concepts.html#concept-transparency) is always enabled for public certificates and cannot be disabled. | 
| `acm:CertificateAuthority` | [RequestCertificate](https://docs.aws.amazon.com/acm/latest/APIReference/API_RequestCertificate.html) | ARN | Filter requests based on [certificate authorities](https://docs.aws.amazon.com/acm/latest/userguide/acm-concepts.html#concept-ca) in the ACM request | 
| `acm:CertificateKeyPairOrigin` | [RequestCertificate](https://docs.aws.amazon.com/acm/latest/APIReference/API_RequestCertificate.html), [AddTagsToCertificate](https://docs.aws.amazon.com/acm/latest/APIReference/API_AddTagsToCertificate.html), [RevokeCertificate](https://docs.aws.amazon.com/acm/latest/APIReference/API_RevokeCertificate.html) | String (`AWS_MANAGED`, `ACME`, `CUSTOMER_PROVIDED`) | Filter requests based on the certificate's key pair origin. For `RequestCertificate`, the value is always `AWS_MANAGED`. When requesting certificates through an ACME client, the value is `ACME`. For `AddTagsToCertificate` and `RevokeCertificate`, the value is read from the existing certificate. | 

## Example 1: Restricting validation method
<a name="conditions-validation"></a>

The following policy denies new certificate requests using the [Email Validation](https://docs.aws.amazon.com/acm/latest/userguide/domain-ownership-validation.html) method except for a request made using the `arn:aws:iam::123456789012:role/AllowedEmailValidation` role.

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement":{
        "Effect":"Deny",
        "Action":"acm:RequestCertificate",
        "Resource":"*",
        "Condition":{
            "StringLike" : {
                "acm:ValidationMethod":"EMAIL"
            },
            "ArnNotLike": {
                "aws:PrincipalArn": [ "arn:aws:iam::123456789012:role/AllowedEmailValidation"]
            }
        }
    }
}
```

------

## Example 2: Preventing wildcard domains
<a name="conditions-wildcards"></a>

The following policy denies any new ACM certificate request that uses wildcard domains.

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement":{
        "Effect":"Deny",
        "Action":"acm:RequestCertificate",
        "Resource":"*",
        "Condition": {
            "ForAnyValue:StringLike": {
                "acm:DomainNames": [
                    "${*}.*"
                ]
            }
        }
    }
}
```

------

## Example 3: Restricting certificate domains
<a name="conditions-restrictdomains"></a>

The following policy denies any new ACM certificate request for domains that don't end with `*.amazonaws.com`

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement":{
        "Effect":"Deny",
        "Action":"acm:RequestCertificate",
        "Resource":"*",
        "Condition": {
            "ForAnyValue:StringNotLike": {
                "acm:DomainNames": ["*.amazonaws.com"]
            }
        }
    }
}
```

------

The policy could be further restricted to specific subdomains. This policy would only allow requests where every domain matches at least one of the conditional domain names.

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement":{
        "Effect":"Deny",
        "Action":"acm:RequestCertificate",
        "Resource":"*",
        "Condition": {
            "ForAllValues:StringNotLike": {
                "acm:DomainNames": ["support.amazonaws.com", "developer.amazonaws.com"]
            }
        }
    }
}
```

------

## Example 4: Restricting key algorithm
<a name="conditions-keyalgorithm"></a>

The following policy uses the condition key `StringNotLike` to allow only certificates requested with the ECDSA 384 bit (`EC_secp384r1`) key algorithm.

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
        "Statement":{
        "Effect":"Deny",
        "Action":"acm:RequestCertificate",
        "Resource":"*",
        "Condition":{
            "StringNotLike" : {
                "acm:KeyAlgorithm":"EC_secp384r1"
            }
        }
    }
}
```

------

The following policy uses the condition key `StringLike` and wildcard `*` matching to prevent requests for new certificates in ACM with any `RSA` key algorithm.

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement":{
        "Effect":"Deny",
        "Action":"acm:RequestCertificate",
        "Resource":"*",
        "Condition":{
            "StringLike" : {
                "acm:KeyAlgorithm":"RSA*"
            }
        }
    }
}
```

------

## Example 5: Restricting certificate authority
<a name="conditions-publicca"></a>

The following policy would only allow requests for private certificates using the provided Private Certificate Authority (PCA) ARN. 

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement":{
        "Effect":"Deny",
        "Action":"acm:RequestCertificate",
        "Resource":"*",
        "Condition":{
            "StringNotLike": {
                "acm:CertificateAuthority":" arn:aws:acm-pca:{{region}}:{{account}}:certificate-authority/{{CA_ID}}"
            }
        }
    }
}
```

------

This policy uses the `acm:CertificateAuthority` condition to allow only requests for publicly trusted certificates issued by Amazon Trust Services. Setting the Certificate Authority ARN to `false` prevents requests for private certificates from PCA.

------
#### [ JSON ]

****  

```
{
"Version":"2012-10-17",		 	 	 
    "Statement":{
        "Effect":"Deny",
        "Action":"acm:RequestCertificate",
        "Resource":"*",
        "Condition":{
            "Null" : {
                "acm:CertificateAuthority":"false"
            }
        }
    }
}
```

------

## Example 6: Restricting actions by certificate key pair origin
<a name="conditions-ckpo"></a>

The following policy allows tagging only on ACME certificates. This is useful when you want to restrict tagging operations to certificates issued through the ACME protocol.

```
{
  "Version": "2012-10-17",		 	 	 
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "acm:AddTagsToCertificate",
      "Resource": "*",
      "Condition": {
        "StringEquals": {
          "acm:CertificateKeyPairOrigin": "ACME"
        }
      }
    }
  ]
}
```