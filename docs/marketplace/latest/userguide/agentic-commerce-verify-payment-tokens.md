

# Verifying payment tokens

After a buyer's agent pays your quote, it sends the request again with a payment token. The payment token is a JSON Web Token (JWT) that AWS Marketplace signs. Your endpoint verifies the token locally, without calling AWS Marketplace, and serves the request only if every check passes.

**Important**  
Always check the `iss` (issuer) claim. Your endpoint holds keys for two kinds of tokens: the quotes that you sign, and the payment tokens that AWS Marketplace signs. If you don't check the issuer, your endpoint could accept one of its own quotes as proof of payment, and serve the request without a charge. Verify payment tokens only against the AWS Marketplace key set, never against your own quote-signing key.

**To verify a payment token**

1. Get the AWS Marketplace public keys from the AWS Marketplace JWKS URL:

   `https://agenticcommerce-marketplace.us-east-1.api.aws/.well-known/jwks.json`

   If a token names a `kid` that isn't in your copy of the key set, fetch the key set again before you reject the token. Don't fetch the key set for every request. AWS Marketplace rotates its signing keys regularly.

1. Read the `kid` from the token header, and find the key with that `kid` in the AWS Marketplace key set. Reject the token if no key matches.

1. Verify the token signature with that key. AWS Marketplace signs payment tokens with `ES384`, the Elliptic Curve Digital Signature Algorithm (ECDSA) using P-384 and SHA-384. Reject any token that uses another algorithm.

1. Require the `iss` claim to equal `agentcore-payments.marketplace.amazonaws.com`. Reject any other value. Also require the `aud` claim to equal your endpoint's own issuer value, the `iss` that you put in your quotes. Reject any other value.

1. Check the token's time claims, and reject a token that has expired.

1. Confirm that the quote inside the payment token is one that your endpoint issued for this request, and that its amount matches what you charge.

1. Treat the payment token as a bearer credential. Accept each payment token for only the one request that its quote priced. Keep a record of each accepted token until the token expires, so that you can reject a token that is sent again.

## Seller SDKs
<a name="agentic-commerce-seller-sdks"></a>

Open-source seller SDKs help you sign quotes and verify payment tokens:
+ [Seller SDK for Python on the GitHub website](https://github.com/aws/fiat-extension-for-x402-py)
+ [Seller SDK for TypeScript on the GitHub website](https://github.com/aws/fiat-extension-for-x402)

Check whether the SDK version that you use verifies the `iss` claim. If it doesn't, add the issuer check from this procedure to your code.