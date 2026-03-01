# Custom domain names for private APIs in API Gateway

You can create a custom domain name for your private APIs. Use a
private custom domain name to provide API
callers with a simpler and more intuitive URL. With a private custom domain name, you can reduce complexity,
configure security measures during the TLS handshake, and control the certificate lifecycle of your domain name
using AWS Certificate Manager (ACM). For more information, see
[Securing your certificate's private key for your custom domain name](#apigateway-private-custom-domains-secure-certificate-private-key "#apigateway-private-custom-domains-secure-certificate-private-key").

Custom domain names for private APIs don’t need to be unique across multiple accounts. You can create
`example.private.com` in account 111122223333 and in account 555555555555, as long as
your ACM certificate covers the domain name. To identify a private custom domain name, use the private custom
domain name ARN. This identifier is unique to private custom domain names.

When you create a private custom domain name in API Gateway, you're an _API provider_. You can
provide your private custom domain name to other AWS accounts using API Gateway or AWS Resource Access Manager (AWS RAM).

When you invoke a
private custom domain name, you're an _API consumer_. You can consume a private custom domain
name from your own AWS account or from another AWS account.

When you consume a private custom domain
name, you create a domain name access association between a VPC endpoint and a private custom domain name. With a
domain name access association, API consumers can invoke your private custom domain name while isolated from the
public internet. For more information, see [Tasks of API providers and API consumers for custom domain names for private APIs](apigateway-private-custom-domains-associations.md "apigateway-private-custom-domains-associations.md").

## Securing your certificate's private key for your custom domain name

When you request an SSL/TLS certificate using ACM to create your custom domain name for private APIs, ACM generates a
public/private key pair. When you import a certificate, you generate the key pair.
The public key becomes part of the certificate. To safely store the private key,
ACM creates another key using AWS KMS, called the KMS key, with the alias **aws/acm**. AWS KMS uses this key to encrypt your certificate’s
private key. For more information, see [Data protection in
AWS Certificate Manager](../../../acm/latest/userguide/data-protection.md "../../../acm/latest/userguide/data-protection.md") in the _AWS Certificate Manager User Guide_.

API Gateway uses AWS TLS Connection Manager, a service that is only accessible
to AWS services, to secure and use your certificate's private keys. When you
use your ACM certificate to create a API Gateway custom domain name, API Gateway associates your
certificate with AWS TLS Connection Manager. We do this by creating a grant in
AWS KMS against your AWS managed key. This grant allows TLS Connection Manager to
use AWS KMS to decrypt your certificate's private key. TLS Connection Manager uses the
certificate and the decrypted (plaintext) private key to establish a secure
connection (SSL/TLS session) with clients of API Gateway services. When the
certificate is disassociated from a API Gateway service, the grant is retired. For
more information, see [Grants](../../../kms/latest/developerguide/grants.md "../../../kms/latest/developerguide/grants.md") in
the _AWS Key Management Service Developer Guide_.

For more information, see [Data encryption at rest in Amazon API Gateway](data-protection-encryption.md#data-protection-at-rest "data-protection-encryption.md#data-protection-at-rest").

## Considerations for private custom domain names

The following considerations might impact your use of private custom domain names:

- It takes about 15 minutes for API Gateway to provision your private custom domain name.
- If you update your ACM certificate, it takes about 15 minutes for API Gateway to complete the update. During
  this time, your domain name is in the `UPDATING` state, and you can still access it.
- To invoke a private custom domain name, you must create a domain name access association. After you create
  a domain name access association, it takes about 15 minutes to be ready.
- The private custom domain name ARN contains the `account-id` and the
  `domain-name-id`. When you create a
  domain name, API Gateway uses the ARN format of `arn:`partition`:apigateway:`region`::/domainnames/domain-name`. When you access a
  private custom domain name, you use the ARN format of
  `arn:`partition`:apigateway:`region`:`account-id`:/domainnames/domain-name+`domain-name-id``.

You might need to modify your IAM
permissions to allow access to a private domain name after you create it.

- You can't invoke private custom domain names with the same name from the same VPC endpoint. For example,
  if you wanted to invoke
  `arn:aws:apigateway:us-west-2:111122223333:/domainnames/private.example.com+abcd1234` and
  `arn:aws:apigateway:us-west-2:111122223333:/domainnames/private.example.com+xyz000`, associate
  each private custom domain name with a different VPC endpoint.
- Wildcard certificates are supported, such as a certificate for `*.private.example.com`.
- Wildcard custom domain names aren't supported.
- Only RSA certificates with a 2048-bit key length and ECDSA
  certificates with 256-bit and 384-bit key lengths are supported.
- You can't set the IP address type for private APIs to only allow IPv4 addresses to invoke your private
  API. Only dualstack is supported. For more information, see [IP address types for REST APIs in API Gateway](api-gateway-ip-address-type.md "api-gateway-ip-address-type.md").
- To send traffic using your private API, you can use all IP address types supported by Amazon VPC. You can send dualstack and IPv6
  traffic by configuring the settings on your VPC endpoint. You can't modify this using API Gateway. For more
  information, see [Add IPv6
  support for your VPC](../../../vpc/latest/userguide/vpc-migrate-ipv6-add.md "../../../vpc/latest/userguide/vpc-migrate-ipv6-add.md").
- Multi-level base path mapping, such as mapping your private API to `/developers/feature`, isn't
  supported, but you can use a routing rule to create a multi-level path condition. For more information, see
  [Send traffic to your APIs through your custom domain name in API Gateway](rest-api-routing-mode.md "rest-api-routing-mode.md").
- You can’t set a minimum TLS version for your private custom domain name. All private custom domain names
  have the security policy of `TLS-1-2`.
- You can use VPC endpoint policy to control access to a private custom domain name. For more information,
  see examples 4 and 5 in [Use VPC endpoint policies for private APIs in API Gateway](apigateway-vpc-endpoint-policies.md "apigateway-vpc-endpoint-policies.md").
- You must create a separate resource policy for your private API and for your private custom domain name.
  To invoke a private custom domain name, an API consumer needs access from the private custom domain name
  resource policy, the private API resource policy, and any VPC endpoint policies or authorization on the
  private API.

## Considerations for using private custom domain names with other API Gateway resources

The following considerations might impact how you use private custom domain names with other API Gateway resources:

- You can't send traffic from a private custom domain name to a public API.
- When a private API is mapped to a private custom domain name, you can't change the API's endpoint type.
- You can't migrate a public custom domain name to a private custom domain name.
- If you have a VPC endpoint that you use to access a public custom domain name, don't use it to create a domain name
  access association with a private custom domain name.

## Differences between private custom domain names and public custom domain names

The following describes the differences between private and public custom domain names:

- Private custom domain names don’t need to be unique across multiple accounts.
- A private domain name has a domain name ID. This ID uniquely identifies a private
  custom domain name and isn't generated for public
  custom domain names.
- When you use the AWS CLI to update or delete your private custom domain name, you must
  provide the domain name ID. If you have a private custom domain name called `example.com` and a
  public custom domain name called `example.com` and you don't provide
  the domain name ID, API Gateway will modify or delete your public custom domain name.

## Next steps for custom domain names for private APIs

For information about the tasks of an API provider and an API consumer, see [Tasks of API providers and API consumers for custom domain names for private APIs](apigateway-private-custom-domains-associations.md "apigateway-private-custom-domains-associations.md").

For instructions on creating a private custom domain name that you can invoke in your own AWS account, see
[Tutorial: Create and invoke a custom domain name for private APIs](apigateway-private-custom-domains-tutorial.md "apigateway-private-custom-domains-tutorial.md").

For instructions on providing another AWS account access to your private custom domain
name, see [API provider: Share your private custom domain name using AWS RAM](apigateway-private-custom-domains-provider-share.md "apigateway-private-custom-domains-provider-share.md"). For instructions on associating your VPC endpoint with a
private custom domain name in another AWS account, see
[API consumer: Associate your VPC endpoint with a private custom domain name shared with you](apigateway-private-custom-domains-consumer-create.md "apigateway-private-custom-domains-consumer-create.md").
