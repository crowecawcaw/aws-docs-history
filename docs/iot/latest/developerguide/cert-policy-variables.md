

# X.509 Certificate AWS IoT Core policy variables
<a name="cert-policy-variables"></a>

X.509 certificate policy variables assist with writing AWS IoT Core policies. These policies grant permissions based on X.509 certificate attributes. The following sections describe how to use these certificate policy variables.

**Important**  
If your X.509 certificate doesn't include a particular certificate attribute but the corresponding certificate policy variable is used in your policy document, the policy evaluation might lead to unexpected behavior.

## CertificateId
<a name="cert-policy-variables-certid"></a>

In the [RegisterCertificate](https://docs.aws.amazon.com/iot/latest/apireference/API_RegisterCertificate.html) API, the `certificateId` appears in the response body. To get information about your certificate, use the `certificateId` in [DescribeCertificate](https://docs.aws.amazon.com/iot/latest/apireference/API_DescribeCertificate.html).

## Issuer attributes
<a name="issuer-attributes"></a>

The following AWS IoT Core policy variables support the allowing or denying of permissions, based on certificate attributes set by the certificate issuer.
+ `iot:Certificate.Issuer.DistinguishedNameQualifier`
+ `iot:Certificate.Issuer.Country`
+ `iot:Certificate.Issuer.Organization`
+ `iot:Certificate.Issuer.OrganizationalUnit`
+ `iot:Certificate.Issuer.State`
+ `iot:Certificate.Issuer.CommonName`
+ `iot:Certificate.Issuer.SerialNumber`
+ `iot:Certificate.Issuer.Title`
+ `iot:Certificate.Issuer.Surname`
+ `iot:Certificate.Issuer.GivenName`
+ `iot:Certificate.Issuer.Initials`
+ `iot:Certificate.Issuer.Pseudonym`
+ `iot:Certificate.Issuer.GenerationQualifier` 

## Subject attributes
<a name="subject-attributes"></a>

The following AWS IoT Core policy variables support the granting or denying of permissions, based on certificate subject attributes set by the certificate issuer.
+ `iot:Certificate.Subject.DistinguishedNameQualifier`
+ `iot:Certificate.Subject.Country`
+ `iot:Certificate.Subject.Organization`
+ `iot:Certificate.Subject.OrganizationalUnit`
+ `iot:Certificate.Subject.State`
+ `iot:Certificate.Subject.CommonName`
+ `iot:Certificate.Subject.SerialNumber`
+ `iot:Certificate.Subject.Title`
+ `iot:Certificate.Subject.Surname`
+ `iot:Certificate.Subject.GivenName`
+ `iot:Certificate.Subject.Initials`
+ `iot:Certificate.Subject.Pseudonym`
+ `iot:Certificate.Subject.GenerationQualifier` 

X.509 certificates provide these attributes with the option to contain one or more values. By default, the policy variables for each multi-value attribute return the first value. For example, the `Certificate.Subject.Country` attribute might contain a list of country names, but when evaluated in a policy, `iot:Certificate.Subject.Country` is replaced by the first country name.

You can request a specific attribute value other than the first value by using a one-based index. For example, `iot:Certificate.Subject.Country.1` is replaced by the second country name in the `Certificate.Subject.Country` attribute. If you specify an index value that does not exist (for example, if you ask for a third value when there are only two values assigned to the attribute), no substitution is made and authorization fails. You can use the `.List` suffix on the policy variable name to specify all values of the attribute.

## Issuer alternate name attributes
<a name="issuer-alternate-name-attributes"></a>

The following AWS IoT Core policy variables support the granting or denying of permissions, based on issuer alternate name attributes set by the certificate issuer.
+ `iot:Certificate.Issuer.AlternativeName.RFC822Name`
+ `iot:Certificate.Issuer.AlternativeName.DNSName`
+ `iot:Certificate.Issuer.AlternativeName.DirectoryName`
+ `iot:Certificate.Issuer.AlternativeName.UniformResourceIdentifier`
+ `iot:Certificate.Issuer.AlternativeName.IPAddress`

## Subject alternate name attributes
<a name="subject-alternate-name-attributes"></a>

The following AWS IoT Core policy variables support the granting or denying of permissions, based on subject alternate name attributes set by the certificate issuer.
+ `iot:Certificate.Subject.AlternativeName.RFC822Name`
+ `iot:Certificate.Subject.AlternativeName.DNSName`
+ `iot:Certificate.Subject.AlternativeName.DirectoryName`
+ `iot:Certificate.Subject.AlternativeName.UniformResourceIdentifier`
+ `iot:Certificate.Subject.AlternativeName.IPAddress`

## Other attributes
<a name="other-attributes"></a>

You can use `iot:Certificate.SerialNumber` to allow or deny access to AWS IoT Core resources, based on the serial number of a certificate. The `iot:Certificate.AvailableKeys` policy variable contains the name of all certificate policy variables that contain values.