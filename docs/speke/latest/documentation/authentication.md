# Authentication required for SPEKE

SPEKE requires authentication for on-premises products and for services and features that run in the AWS Cloud.

###### Topics

- [Authentication for AWS cloud implementations](#aws-authentication "#aws-authentication")
- [Authentication for on-premises products](#authentication-on-prem "#authentication-on-prem")

## Authentication for AWS cloud implementations

SPEKE requires AWS authentication through IAM roles for use with an encryptor. IAM roles are created by the DRM provider or by the operator who owns the DRM endpoint in an AWS account. Each role is assigned an Amazon Resource Name (ARN), which the AWS Elemental service operator provides on the service console when requesting encryption. The role’s policy permissions must be configured to give permission to access the key provider API and no other AWS resource access. When the encryptor contacts the DRM key provider, it uses the role ARN to assume the role of the key provider account holder, which returns temporary credentials for the encryptor to use to access the key provider.

One common implementation is for the operator or DRM platform vendor to use Amazon API Gateway in front of the key provider, and then enable AWS Identity and Access Management (AWS IAM) authorization on the API Gateway resource. You can use the following policy definition example and attach it to a new role to give permissions to the appropriate resource. In this case, the permissions are for all API Gateway resources:

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "execute-api:Invoke"
            ],
            "Resource": [
                "arn:aws:execute-api:us-west-2:*:*/*/GET/*"
            ]
        }
    ]
}
```

Finally, the role requires the addition of a trust relationship, and the operator must be able to select the service.

The following example shows a role ARN that is created for accessing the DRM key provider:

```
arn:aws:iam::2949266363526:role/DRMKeyServer
```

For more information about the creation of a role, see [AWS AssumeRole](../../../STS/latest/APIReference/API_AssumeRole.md "../../../STS/latest/APIReference/API_AssumeRole.md"). For more information about signing a request, see [AWS Sigv4](../../../general/latest/gr/sigv4_signing.md "../../../general/latest/gr/sigv4_signing.md").

## Authentication for on-premises products

For on-premises products, we recommend that you use SSL/TLS and digest authentication for the best security, but at a minimum you should use basic authentication over HTTPS.

Both types of authentication use the `Authorization` header in the HTTP request:

- **Digest authentication** – The authorization header consists of the identifier `Digest` followed by a series of values that authenticate the request. Specifically, a response value is generated through a series of MD5 hash functions that include a unique, one-time-use nonce from the server that is used to ensure that the password travels securely.
- **Basic authentication** – The authorization header consists of the identifier `Basic` followed by a base-64 encoded string that represents the user name and password, separated by a colon.

For information about basic and digest authentication, including detailed information about the header, see the Internet Engineering Task Force (IETF) specification [RFC 2617 - HTTP Authentication: Basic and Digest Access Authentication](https://tools.ietf.org/html/rfc2617 "https://tools.ietf.org/html/rfc2617").
