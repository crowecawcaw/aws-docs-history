

# Create a VPC endpoint for AWS STS OIDC discovery
<a name="reference_sts_oidc_vpc_endpoint_create"></a>

AWS Security Token Service (AWS STS) OIDC discovery is a pair of public endpoints that serve the metadata and verification keys relying parties need to validate JSON Web Tokens (JWTs) issued by [outbound identity federation](id_roles_providers_outbound.md).

When you enable outbound identity federation, AWS STS publishes an account-specific issuer URL. This URL hosts two OpenID Connect (OIDC) discovery endpoints. Relying parties fetch these endpoints to obtain the metadata and public keys they need to verify the JWTs that [GetWebIdentityToken](https://docs.aws.amazon.com/STS/latest/APIReference/API_GetWebIdentityToken.html) issues:
+ `{issuer_url}/.well-known/openid-configuration` — The OIDC discovery document
+ `{issuer_url}/.well-known/jwks.json` — The JSON Web Key Set (JWKS) that contains the token signature verification keys

By default, reaching these endpoints from your VPC requires an internet gateway, NAT device, VPN connection, or connection. To keep this traffic on the AWS network instead, create an interface VPC endpoint for the STS OIDC discovery endpoint.

**Note**  
The STS OIDC discovery endpoint serves only the two endpoints listed above. It does not serve any AWS STS API operation. To call `GetWebIdentityToken`, `AssumeRole`, or any other AWS STS operation privately, use the `com.amazonaws.{{region}}.sts` endpoint service. See [Create a VPC endpoint for AWS STS](reference_sts_vpc_endpoint_create.md).

## Choosing the right endpoint service
<a name="reference_sts_oidc_vpc_endpoint_choosing"></a>

Outbound identity federation uses two distinct network paths. Most workloads that both mint and verify tokens need both endpoint services.


| Task | Endpoint service | Authentication | 
| --- | --- | --- | 
| Mint a JWT (sts:GetWebIdentityToken) | com.amazonaws.{{region}}.sts | AWS SigV4 | 
| Read /.well-known/openid-configuration | com.amazonaws.{{region}}.sts-oidc | None (unauthenticated) | 
| Read /.well-known/jwks.json | com.amazonaws.{{region}}.sts-oidc | None (unauthenticated) | 

You do not need the STS OIDC discovery endpoint if the only party that verifies your tokens is an external service outside AWS. That service fetches your issuer URL over the public internet, and its traffic does not enter your VPC.

## Considerations
<a name="reference_sts_oidc_vpc_endpoint_considerations"></a>

Consider the following before you create an interface VPC endpoint for STS OIDC discovery.
+ **VPC endpoint policies are not supported.** Both discovery APIs serve publicly available data, and the STS OIDC discovery endpoint does not enforce VPC endpoint policies. Use security groups and subnet placement to control which resources can reach the endpoint.
+ **Only two paths are served.** The endpoint accepts HTTPS `GET` requests to `/.well-known/openid-configuration` and `/.well-known/jwks.json` only. All other paths and methods return an error.

## Creating an interface VPC endpoint for STS OIDC discovery
<a name="reference_sts_oidc_vpc_endpoint_creating"></a>

You can create a VPC endpoint for the STS OIDC discovery endpoint using either the Amazon Virtual Private Cloud console or the AWS Command Line Interface. For more information, see [Access an AWS service using an interface VPC endpoint](https://docs.aws.amazon.com/vpc/latest/privatelink/create-interface-endpoint.html) in the *Amazon VPC User Guide*.

Create a VPC endpoint for STS OIDC discovery using the following service name:
+ `com.amazonaws.{{region}}.sts-oidc`

If you enable private DNS for the endpoint, you can send requests to `sts-oidc.{{region}}.amazonaws.com` and they will resolve to the endpoint's network interfaces within your VPC.

## Sending requests through the endpoint
<a name="reference_sts_oidc_vpc_endpoint_sending_requests"></a>

When a relying party in your VPC needs to verify a JWT, it fetches the OIDC discovery document and JWKS from the issuer URL. The issuer hostname (for example, `{{uuid}}.tokens.sts.global.api.aws`) uses a different domain than the endpoint (`sts-oidc.{{region}}.amazonaws.com`), so it does not resolve to the VPC endpoint by default.

To route requests for the issuer hostname through the endpoint, create an Amazon Route 53 private hosted zone for your issuer hostname and add an alias record that points to the VPC endpoint. After you create the hosted zone, resources in the VPC resolve the issuer hostname to the endpoint's network interfaces. Standard OIDC libraries can then fetch the discovery documents with no code changes. For more information about creating a private hosted zone, see [Working with private hosted zones](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/hosted-zones-private.html) in the *Amazon Route 53 Developer Guide*.

**Note**  
The endpoint service is regional, but a single endpoint serves discovery requests for any issuer UUID in the partition. Create endpoints in the Regions where your verifiers run; you do not need one per issuer account.