

# Parse user pool tokens safely
<a name="user-pool-parse-tokens-safely"></a>

An Amazon Cognito token's claim set is not fixed. The claims that your token carries vary with the authentication flow, the user's group membership, and the identity provider, and with the features that you enable on your user pool. Amazon Cognito adds new claims additively over time: it introduces new keys, but it does not rename, change the type of, or remove the existing claims that this guide documents. These rules apply to both ID tokens and access tokens.

Don't write your own token parser. Use a JSON Web Token (JWT) library and a JSON parser that keep working as the token grows. The two rules that prevent almost every real-world break are the first two below: tolerate claims you don't recognize, and make the right assumptions about the type and cardinality of each claim you read.

Ignore claims that you don't recognize  
Read the claims your application needs and leave the rest alone. Don't reject, fail, or throw an error when a token carries a claim that isn't listed in this guide. New claims are added additively, and a token that contains an unlisted claim is still valid.

Read each claim in its documented type  
A JSON parser identifies each value's primitive type from the JSON itself, so the risk is in the assumptions your code then makes about that value. Treat each claim as the type and cardinality this guide documents for it. A claim that is documented as an array is always an array, even when it currently holds a single value. Don't collapse it to a string. For example, `cognito:groups`, `cognito:roles`, and `identities` are always arrays. The same principle applies to claims defined by other specifications. For example, `amr`, when present, is an array of strings as defined in [RFC 8176](https://tools.ietf.org/html/rfc8176) on the IETF website, so read it in that type.

Don't over-validate claim formats  
Validate what the specification for a claim requires, and no more. For example, `sub` is a unique string but is not guaranteed to be in any particular UUID format. Some values inside custom claims such as `identities` are serialized as strings rather than as JSON booleans or numbers, and opaque values aren't guaranteed to be any particular length. Imposing a stricter format than the documentation states causes valid tokens to fail.

Don't assume the number of claims or their order  
The claims in a token can appear in any order, and the count can change between tokens and over time. Address each claim by name rather than by position, and parse the token as a general JSON object rather than a fixed structure.

Budget for growth in token size  
Because the claim set grows, the overall size of the token grows too. Don't assume a fixed or maximum token size in buffers, column widths, headers, or cookies.

The `openid-configuration` discovery document follows the same additive, forward-compatible approach. For more information about parsing that document safely, see [Prepare for changes to the discovery document](federation-endpoints.md#user-pool-oidc-discovery-parse-safely).