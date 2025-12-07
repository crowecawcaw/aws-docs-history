# Configure inbound JWT authorizer

The inbound authorizer authenticates and authorizes incoming OAuth 2.0 API requests to
AgentCore Runtime and AgentCore Gateway. It validates JSON Web Tokens (JWTs) before allowing
access to agents or gateways. The authorizer is Identity Provider (IdP) agnostic and works
with any OAuth 2.0 compatible identity provider. When AgentCore Runtime or AgentCore Gateway receives
an inbound request, the authorizer will use the configured discovery URL to fetch the public
keys and authorization server endpoint to perform the JWT validation. You can configure the
authorizer based on your IdP and allowed authorization scopes or claims.

## Configure an Inbound Authorizer

You can configure your agent runtime or gateway to accept JWT bearer tokens by
providing an authorizer configuration during agent creation. The authorization
configuration is the same for either AgentCore Runtime or AgentCore Gateway.

- **Discovery URL**: A string that must match the pattern `^.+/\.well-known/openid-configuration$` for OpenID Connect (OIDC)
  discovery URLs. You can find your discovery URL from your identity provider. A
  discovery URL is a specific web address that AgentCore Identity can use to find
  information about the authentication endpoint details. It allows AgentCore Identity to
  dynamically configure itself to interact with your service without needing
  pre-programmed knowledge of its specific URLs.
- **Allowed audiences**: A list of permitted audiences that
  will be validated against the `aud` claim in the JWT token. An
  audience claim (`aud`) in OAuth 2.0 specifies which resource server (API)
  the token is intended for. The resource server validates the `aud`
  claim to ensure it is the correct recipient before processing the request,
  preventing a token from being reused at a different API it was not issued for.
- **Allowed clients**: A list of permitted client identifiers
  that will be validated against the `client_id` claim in the JWT
  token. A `client_id` in OAuth 2.0 is a public, unique identifier for an
  application that is requesting access to AgentCore Runtime or AgentCore Gateway. It acts
  like a username for the application, distinguishing it from other clients
  (applications) registered with the authorizer.
- **Allowed scopes**: A list of required permissions, defined
  as scopes, needed to invoke the runtime or gateway. An OAuth 2.0 scope is a string
  that defines a specific level of access that is defined in the JWT. Scopes act
  as permissions to limit what an application can do.
- **Required custom claims**: A set of rules to match specific
  claims in the incoming token against predefined values for validating JWT
  tokens. You can create a rule by specifying the following:
  - **InboundTokenClaimName**: Name of the custom claim.

  **InboundTokenClaimValueType**: Either `STRING`
  or `STRING_ARRAY`.

  **ClaimMatchOperator**: If `InboundTokenClaimValueType` equals `STRING`, this can
  be `EQUALS` or `CONTAINS`. If `InboundTokenClaimValueType` equals `STRING_ARRAY`, this
  must be `CONTAINS_ANY`.

  **AuthorizingClaimMatchValue**: Required value of the
  custom claim.

  **Example**: You can define a rule that enforces: `Group
 must equal Developer`.

- **Note**: At least one of the fields is required for the
  configuration: allowed audiences, allowed clients, allowed scopes, or required custom
  claims. If more than one is used, the authorizer will verify them all.
