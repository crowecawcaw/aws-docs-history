

# Configuring your quote-signing key

Your endpoint signs each x402 quote with a private key that you control. AWS Marketplace verifies each quote with the matching public key before it charges the buyer. You register the public key in the product's delivery option, as one of these key sources:
+ **JWKS URL** – A JSON Web Key Set (JWKS) document that you host.
+ **AWS KMS key** – An asymmetric signing key in AWS Key Management Service (AWS KMS) in your AWS account. AWS Marketplace reads only the public key.

AWS Marketplace reads your key source to verify each quote when a buyer pays. If it can't read your JWKS URL or use your AWS KMS key, payment requests for your quotes fail. While your product has Limited visibility, test a paid request before you make the product public. For more information, see [Configure the allowlist](listing-saas-ai-agents.md#step-8-allowlist).

## Use a JWKS URL
<a name="agentic-commerce-jwks"></a>

Your JWKS URL must meet the following requirements:
+ It uses HTTPS, on a host name that resolves to a public IP address.
+ It returns the JWKS document directly. AWS Marketplace doesn't follow redirects.
+ It's a stable URL whose path contains `/.well-known/` and ends in `.json`, with no query string, for example `https://api.example.com/.well-known/jwks.json`. AWS Marketplace rejects other paths.
+ Each key in the document has a unique `kid` (key ID). Each quote names its signing key in the `kid` header.
+ The key that signs your quotes is an Elliptic Curve (EC) key on the P-256, P-384, or P-521 curve. AWS Marketplace doesn't accept RSA keys.
+ The document is no larger than 5 KB (5,120 bytes), and the URL returns it within 1.5 seconds.

**To register a JWKS URL**

1. Publish the public key in a JWKS document at your HTTPS URL.

1. In the product's delivery option, for **Public key source**, choose **JWKS endpoint URL**, and enter the URL.

1. Save the delivery option.

## Use an AWS KMS key
<a name="agentic-commerce-kms"></a>

With an AWS KMS key, the private key never leaves AWS KMS. AWS Marketplace assumes an IAM role in your account to call `kms:GetPublicKey` on the key. It can't sign with your key or use it in any other way.

**To create the AWS KMS key and the role**

1. In the US East (N. Virginia) Region, create an asymmetric AWS KMS key with the key usage `SIGN_VERIFY` and the key spec `ECC_NIST_P256`, `ECC_NIST_P384`, or `ECC_NIST_P521`, and create an alias for it. AWS Marketplace doesn't accept RSA keys.

1. Create an IAM role that AWS Marketplace can assume. Use the following trust policy. The trust policy allows only the AWS Marketplace Agentic Commerce service principal to assume the role. As an additional safeguard, the `sts:ExternalId` condition requires the service principal name as the external ID. This value is fixed and isn't a secret. Enter it exactly as shown, or AWS Marketplace can't assume the role.

   ```json
   {
       "Version": "2012-10-17"		 	 	 ,
       "Statement": [
           {
               "Effect": "Allow",
               "Principal": {
                   "Service": "agentcore-payments.marketplace.amazonaws.com"
               },
               "Action": "sts:AssumeRole",
               "Condition": {
                   "StringEquals": {
                       "sts:ExternalId": "agentcore-payments.marketplace.amazonaws.com"
                   }
               }
           }
       ]
   }
   ```

1. Attach the following permissions policy to the role. It allows only `kms:GetPublicKey` on the key. Replace the key ARN with your own.

   ```json
   {
       "Version": "2012-10-17"		 	 	 ,
       "Statement": [
           {
               "Effect": "Allow",
               "Action": "kms:GetPublicKey",
               "Resource": "arn:aws:kms:us-east-1:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"
           }
       ]
   }
   ```

1. Make sure that the key policy allows the role to call `kms:GetPublicKey`. For example, add the following statement to the key policy.

   ```json
   {
       "Sid": "AllowMarketplaceToReadPublicKey",
       "Effect": "Allow",
       "Principal": {
           "AWS": "arn:aws:iam::111122223333:role/MarketplaceQuoteKeyAccess"
       },
       "Action": "kms:GetPublicKey",
       "Resource": "*"
   }
   ```

**To register the AWS KMS key**

1. In the product's delivery option, for **Public key source**, choose **KMS key**. Enter the key alias ARN and the role ARN.

1. Save the delivery option.

## Rotate your quote-signing key
<a name="agentic-commerce-key-rotation"></a>

After you publish the product, the public key source stays editable so that you can rotate keys. Rotate on a regular schedule, and immediately if you think that a private key is compromised.
+ **JWKS URL** – Add the new key, with a new `kid`, to your JWKS document. Start signing quotes with the new key. Remove the old key after the last quote that it signed has expired. AWS Marketplace might keep using a key that it already fetched for a `kid` for a short time. Always use a new `kid` for a new key.
+ **AWS KMS key** – AWS KMS doesn't rotate asymmetric keys automatically. Create a new key, and update the role's permissions policy and the new key's key policy so that the role can call `kms:GetPublicKey` on the new key. Then point your alias at the new key. If the role can't read the new key, payment requests fail. An alias refers to one key at a time, so quotes that the old key signed fail verification after you move the alias. If you need the old and new keys to overlap, use a JWKS URL.