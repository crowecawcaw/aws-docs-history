

# Multi-tenant Amazon Cognito authentication
<a name="sec-cognito-auth"></a>

AVX authenticates all callers through Amazon Cognito. Each channel — voice (Amazon Connect), chat, and mobile or web — terminates at a Cognito-protected entry point before any agent work begins. The auth layer is intentionally uniform across channels so that the security model does not fragment by modality.

## Tenant user pools and OEM-branded sign-in
<a name="sec-cognito-tenant-pools"></a>

Each automotive organization (OEM, rental company, fleet operator) that deploys AVX maintains its own Amazon Cognito user pool. This pool-per-tenant model provides strong isolation at the identity layer: tokens issued by one tenant’s pool are not accepted by another tenant’s workloads, and the branded hosted-UI domain (`https://<tenant>.auth.<region>.amazoncognito.com`) allows each automotive brand to present its own sign-in experience to drivers and vehicle owners.

The per-tenant pool holds the claims that the rest of AVX uses as security inputs:


| Claim | Purpose in AVX | 
| --- | --- | 
|  `sub`  | Stable subject identifier; used as the caller’s canonical user ID in audit logs and DynamoDB partition keys. | 
|  `custom:tenantId`  | Tenant identifier; propagated to every downstream service call, IAM condition key, and log dimension. | 
|  `custom:vehicleId`  | VIN or internal vehicle ID associated with this user at enrolment time; used for initial vehicle context resolution before the session-init step performs a full vehicle lookup. | 
|  `cognito:groups` / `custom:role`  | Role claim; input to server-side persona inference (see [Server-side persona inference as a privilege boundary](sec-persona-privilege.md)). | 

## Cross-pool trust: the EXTRA\_USER\_POOL\_IDS pattern
<a name="sec-extra-pool-trust"></a>

AVX’s API Gateway Cognito authorizer is configured to trust more than one user pool via an `EXTRA_USER_POOL_IDS` environment variable. This lets an AVX deployment accept tokens issued by a secondary pool — for example, a fleet management platform’s own user pool or an OEM-branded identity provider — without requiring callers to re-authenticate against AVX’s primary pool. The pattern works as follows:

1. The AVX API Gateway Lambda authorizer reads the `EXTRA_USER_POOL_IDS` list at runtime.

1. For each inbound bearer token, the authorizer validates the signature against each configured pool’s public JWKS endpoint until a match is found or all are exhausted.

1. A validated token from any trusted pool produces the same downstream claim set; no behavioral difference exists between the primary pool and secondary pools from the agent’s perspective.

1. Tenant isolation is enforced by `custom:tenantId`, not by pool identity — the pool is the authentication mechanism; the tenant claim is the authorization scope.

When adding a new automotive organization to an AVX deployment, you register the organization’s user pool ARN in `EXTRA_USER_POOL_IDS` and provide a tenant config record in the `vsa-tenant-config` DynamoDB table. No code change is required.