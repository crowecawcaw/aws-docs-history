

# Signing keys and troubleshooting JWT authorizers

A JWT authorizer verifies token signatures with the public keys that the issuer publishes. API Gateway finds those keys through the issuer's OIDC discovery document.

## How API Gateway finds signing keys
<a name="rest-api-jwt-authorizer-keys.discovery"></a>

Each issuer must publish an OIDC discovery document at `/.well-known/openid-configuration`. When you create or update an authorizer, API Gateway reads this document and records the location of the issuer's key set, which the discovery document names as the `jwks_uri`. API Gateway then retrieves the key set and caches the keys.

The discovery document and the key set must be reachable from the public internet.

The `get-authorizer` command returns the resolved key set location as a `jwksUri` for each issuer.

## Key rotation and caching
<a name="rest-api-jwt-authorizer-keys.rotation"></a>

API Gateway caches each issuer's signing keys for up to 1 hour on a best-effort basis. Routine key rotation needs no change in API Gateway. To rotate keys, publish the new key in your key set before you sign tokens with it. When API Gateway receives a token signed with a key it hasn't seen, it retrieves the key set again. Keep the old key published until the tokens that it signed have expired.

A token remains valid until its `exp` time, so use short token lifetimes for sensitive operations.

## Troubleshooting token failures
<a name="rest-api-jwt-authorizer-keys.troubleshooting"></a>

The following table lists common reasons that API Gateway rejects a token, and how to resolve each one. API Gateway records authorizer failures in the execution logs for the stage. For more information, see [Execution logging for REST APIs](rest-api-execution-logging.md).


| Symptom | Cause | Resolution | 
| --- | --- | --- | 
| Every token from an issuer receives a 401 | The configured issuer does not match the token's iss claim, often because of a trailing slash | Decode a token and copy its iss claim. Set the issuer to that exact value, including any trailing slash. | 
| The authorizer fails to create or update | API Gateway cannot reach the issuer's discovery document | Confirm that the issuer publishes a document at /.well-known/openid-configuration, that the issuer's host resolves to a public address, and that its certificate is issued by a [supported certificate authority](api-gateway-supported-certificate-authorities-for-http-endpoints.md). | 
| update-authorizer returns a 400 error with the message Invalid value for patch operation 'replace' and path '/jwtConfiguration' | The configuration includes jwksUri, which get-authorizer returns | Remove jwksUri from each issuer, and then send the configuration again. | 
| A token receives a 401 after a signing change | The token is signed with an algorithm that you did not allow, or with an unsupported algorithm | Add the algorithm to defaultAlgorithms. API Gateway supports RS256, RS384, RS512, ES256, ES384, and ES512, and rejects HMAC algorithms and alg: none. | 
| A newly issued or recently expired token receives a 401 | The client clock and the API Gateway clock differ by more than the allowed skew | API Gateway allows 60 seconds of clock skew on exp, nbf, and iat. Synchronize the client clock. | 
| A valid token receives a 403 | The token does not carry a scope that the method requires, or it fails an additional claim rule | Confirm that the token's scope or scp claim carries at least one of the method's scopes, and that the token satisfies the issuer's claim rules. | 
| Tokens from a correctly configured issuer receive a 401 | The token's aud value isn't in the issuer's audiences | Decode a token and add its aud value to the issuer's audiences. | 
| A change to the authorizer or a method has no effect | The API isn't redeployed | Deploy the API to the stage. | 

API Gateway reads method scopes only from the token's `scope` or `scp` claim. If your identity provider carries permissions in a different claim, and every method that uses the authorizer requires the same single string value, add a claim rule to the issuer. For more information, see [Additional claims](rest-api-jwt-authorizer-create.md#rest-api-jwt-authorizer-create.claims). If different methods require different values, or the claim is an array, use a Lambda authorizer.