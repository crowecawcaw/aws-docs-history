

# Set up to use AWS Certificate Manager
<a name="setup"></a>

With AWS Certificate Manager (ACM) you can provision and manage SSL/TLS certificates for your AWS based websites and applications. You use ACM to create or import and then manage a certificate. You must use other AWS services to deploy the certificate to your website or application. For more information about the services integrated with ACM, see [Managed automation with integrated services](acm-services.md). The following sections discuss the steps you need to perform before using ACM.

**Topics**
+ [Sign up for an AWS account](#sign-up-for-aws)
+ [Register a domain name for ACM](#setup-domain)
+ [(Optional) Configure a CAA record](#setup-caa)

## Sign up for an AWS account
<a name="sign-up-for-aws"></a>

To get started with AWS, you need an AWS account. For information about creating an AWS account, see [Getting started with an AWS account](https://docs.aws.amazon.com/accounts/latest/reference/getting-started.html) in the *AWS Account Management Reference Guide*.

## Register a domain name for ACM
<a name="setup-domain"></a>

A fully qualified domain name (FQDN) is the unique name of an organization or individual on the Internet followed by a top-level domain extension such as `.com `or `.org`. If you do not already have a registered domain name, you can register one through Amazon Route 53 or dozens of other commercial registrars. Typically you go to the registrar's website and request a domain name. Domain name registration usually lasts for a set period of time such as one or two years before it must be renewed.

For more information about registering domain names with Amazon Route 53, see [Registering Domain Names Using Amazon Route 53](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/registrar.html) in the *Amazon Route 53 Developer Guide*. 

## (Optional) Configure a CAA record
<a name="setup-caa"></a>

A CAA record specifies which certificate authorities (CAs) are allowed to issue certificates for a domain or subdomain. Creating a CAA record for use with ACM helps to prevent the wrong CAs from issuing certificates for your domains. A CAA record isn't a substitute for the security requirements that are specified by your certificate authority, such as the requirement to validate that you're the owner of a domain.

After ACM validates your domain during the certificate request process, it checks for the presence of a CAA record to make sure it can issue a certificate for you. Configuring a CAA record is optional.

Use the following values when you configure your CAA record:

**flags**  
Specifies whether the value of the **tag** field is supported by ACM. Set this value to **0**.

**tag**  
The **tag** field can be one of the following values. Note that the **iodef** field is currently ignored.     
**issue**  
Indicates that the ACM CA that you specify in the **value** field is authorized to issue a certificate for your domain or subdomain.   
**issuewild**  
Indicates that the ACM CA that you specified in the **value** field is authorized to issue a wildcard certificate for your domain or subdomain. A wildcard certificate applies to the domain or subdomain and all of its subdomains. Note that if you plan to use HTTP validation, this setting won't apply because HTTP validation doesn't support wildcard certificates. Use DNS or email validation instead for wildcard certificates.

**value**  
The value of this field depends on the value of the **tag** field. You must enclose this value in quotation marks ("").     
When **tag** is **issue**  
The **value** field contains the CA domain name. This field can contain the name of a CA other than an Amazon CA. However, if you do not have a CAA record that specifies one of the following four Amazon CAs, ACM cannot issue a certificate to your domain or subdomain:   
+ amazon.com
+ amazontrust.com
+ awstrust.com
+ amazonaws.com
The **value** field can also contain a semicolon (;) to indicate that no CA should be permitted to issue a certificate for your domain or subdomain. Use this field if you decide at some point that you no longer want a certificate issued for a particular domain.  
When **tag** is **issuewild**  
The **value** field is the same as that for when **tag** is **issue** except that the value applies to wildcard certificates.   
When there is an **issuewild** CAA record present that does not include an ACM CA value, then no wild cards can be issued by ACM. If there is no **issuewild** present, but there is an **issue** CAA record for ACM, then wild cards may be issued by ACM. 

**Example CAA Record Examples**  
In the following examples, your domain name comes first followed by the record type (CAA). The **flags** field is always 0. The **tags** field can be **issue** or **issuewild**. If the field is **issue** and you type the domain name of a CA server in the **value** field, the CAA record indicates that your specified server is permitted to issue your requested certificate. If you type a semicolon ";" in the **value** field, the CAA record indicates that no CA is permitted to issue a certificate. The configuration of CAA records varies by DNS provider.   
If you plan to use HTTP validation with CloudFront, you don't need to configure **issuewild** records because HTTP validation doesn't support wildcard certificates. For wildcard certificates, use DNS or email validation instead.

```
Domain       Record type  Flags  Tag      Value   
example.com.   CAA            0        issue      "SomeCA.com"
```

```
Domain       Record type  Flags  Tag      Value 
example.com.   CAA            0        issue      "amazon.com"
```

```
Domain       Record type  Flags  Tag      Value 
example.com.   CAA            0        issue      "amazontrust.com"
```

```
Domain       Record type  Flags  Tag      Value 
example.com.   CAA            0        issue      "awstrust.com"
```

```
Domain       Record type  Flags  Tag      Value 
example.com.   CAA            0        issue      "amazonaws.com"
```

```
Domain       Record type  Flags  Tag      Value 
example.com    CAA            0        issue      ";"
```

For more information about how to add or modify DNS records, check with your DNS provider. Route 53 supports CAA records. If Route 53 is your DNS provider, see [CAA Format](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/ResourceRecordTypes.html#CAAFormat) for more information about creating a record. 