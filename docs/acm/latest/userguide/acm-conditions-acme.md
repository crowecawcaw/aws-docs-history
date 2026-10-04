

# Condition keys for ACME certificate requests
<a name="acm-conditions-acme"></a>

Certificate issuance and revocation through an ACME endpoint are authorized as standard ACM actions. This authorization uses the IAM role attached to the ACME client's external account binding. The ACM condition keys therefore apply to ACME requests as well, and you can use them in the role's permissions policy, in an IAM policy, in a Service Control Policy (SCP), or in a VPC endpoint policy.

For the full list of keys and the operations that support them, see [Use condition keys with ACM](acm-conditions.md). For more information about the role, see [IAM for ACME certificate automation](security-iam-acme.md).

What differs is the set of keys available on each action, and the values ACM supplies. An ACME client sends a certificate signing request (CSR) rather than an ACM API request. As a result, ACM derives some values from the CSR, sets others to a fixed value, and leaves some keys unpopulated. Write conditions against the keys listed for the action you are restricting: a condition on a key that an action does not carry denies that action outright.

## Condition keys for ACME issuance
<a name="acm-conditions-acme-issuance"></a>

When an ACME client finalizes an order, ACM authorizes the `acm:RequestCertificate` action against the certificates in your account and populates the following condition keys.


**Condition key values for ACME issuance**  

| Condition key | Value | 
| --- | --- | 
| `acm:CertificateKeyPairOrigin` | Always `ACME`. Use this key to write policies that apply only to ACME issuance, or only to issuance that does not use ACME. | 
| `acm:DomainNames` | The domain names the certificate is requested for, taken from the subject alternative name (SAN) entries of the CSR. | 
| `acm:KeyAlgorithm` | The key algorithm of the CSR's public key: `RSA_2048`, `EC_prime256v1`, or `EC_secp384r1`. | 
| `acm:ValidationMethod` | Always `DNS`. ACME issuance uses the domain validations configured on the endpoint, which are DNS validations. | 
| `acm:CertificateTransparencyLogging` | Always `ENABLED`. Certificate transparency logging cannot be disabled for public certificates. | 
| `acm:Export` | Always `ENABLED`. The ACME client generates and holds the private key, so an ACME certificate is exported by definition. A policy that denies issuance when `acm:Export` is `ENABLED` therefore denies all ACME issuance. | 

**Note**  
ACM does not set `acm:CertificateAuthority` for ACME issuance. To restrict which certificate authority an ACME endpoint issues from, configure the endpoint itself. For more information, see [Endpoint configuration](acm-acme-endpoints.md#acm-acme-endpoint-configuration).

## Condition keys for ACME revocation
<a name="acm-conditions-acme-revocation"></a>

Revocation through the ACME endpoint's revoke-cert URL is authorized as the `acm:RevokeCertificate` action. This action is scoped to the ARN of the certificate being revoked.

**Important**  
`acm:CertificateKeyPairOrigin`, set to `ACME`, is the only condition key ACM populates for ACME revocation. In particular, `acm:KeyAlgorithm` is not available. This condition key is read from a certificate request, but an ACME client identifies the certificate to revoke by its bytes, not by a request that carries a key algorithm. A statement that requires `acm:KeyAlgorithm` with a `StringEquals` condition never matches a revocation request, and so denies all ACME revocation.

## Condition keys for tagging an ACME certificate
<a name="acm-conditions-acme-tags"></a>

If the ACME endpoint is configured with certificate tags, ACM applies those tags to each certificate it issues from the endpoint. ACM authorizes that as a separate `acm:AddTagsToCertificate` action. This action must also be allowed for issuance to succeed, and it populates the following condition keys.


**Condition key values for tagging an ACME certificate**  

| Condition key | Type | Value | 
| --- | --- | --- | 
| `aws:RequestTag/{{tag-key}}` | String | The value of each certificate tag configured on the endpoint. | 
| `aws:TagKeys` | ArrayOfString | The keys of all certificate tags configured on the endpoint. | 
| `aws:ResourceTag/{{tag-key}}` | String | The value of each tag being applied to the new certificate. | 
| `acm:CertificateKeyPairOrigin` | String | Always `ACME`. | 

**Important**  
If your external account binding role allows only `acm:RequestCertificate`, it cannot issue certificates from an endpoint that carries certificate tags. Grant `acm:AddTagsToCertificate` as well, or remove the tags from the endpoint.

## How a denial appears to the ACME client
<a name="acm-conditions-acme-denials"></a>

When a policy condition denies an ACME certificate request, the client receives the ACME error type `urn:ietf:params:acme:error:unauthorized`. The error detail names the denied ACM action. Certbot and other clients report this at the finalize step of the order.

A request that the endpoint's own configuration rejects looks different. For example, suppose the CSR uses a key algorithm that the endpoint's allowed key algorithms do not permit. In this case, the client receives `urn:ietf:params:acme:error:badCSR`, which names the permitted algorithms. That is a configuration result rather than an authorization result, so check the endpoint configuration rather than your policies when you see it.

## Example: Restricting ACME issuance and revocation
<a name="acm-conditions-acme-example"></a>

The following permissions policy for an external account binding role allows ACME issuance only for subdomains of `example.com` and only with an ECDSA P-384 key. It also allows revocation of any ACME certificate in the account.

Issuance and revocation are separate statements because the two actions do not carry the same condition keys. Adding the `acm:KeyAlgorithm` or `acm:DomainNames` condition to the revocation statement would prevent the client from revoking anything.

```
{
  "Version": "2012-10-17",		 	 	 
  "Statement": [
    {
      "Sid": "AllowAcmeIssuance",
      "Effect": "Allow",
      "Action": "acm:RequestCertificate",
      "Resource": "*",
      "Condition": {
        "StringEquals": {
          "acm:CertificateKeyPairOrigin": "ACME",
          "acm:KeyAlgorithm": "EC_secp384r1"
        },
        "ForAllValues:StringLike": {
          "acm:DomainNames": "*.example.com"
        }
      }
    },
    {
      "Sid": "AllowAcmeRevocation",
      "Effect": "Allow",
      "Action": "acm:RevokeCertificate",
      "Resource": "*",
      "Condition": {
        "StringEquals": {
          "acm:CertificateKeyPairOrigin": "ACME"
        }
      }
    }
  ]
}
```

If the ACME endpoint is configured with certificate tags, add a statement allowing `acm:AddTagsToCertificate` as well.