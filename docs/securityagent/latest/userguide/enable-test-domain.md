# Enable an application domain for penetration testing

Before you can run a penetration test on an application, you need to add a target domain and verify ownership. AWS Security Agent will only perform penetration tests against verified domains.

###### Note

You do not need to validate ancillary domains that your application may use. You only need to validate the domain you will actively run penetration tests against.

## Step 1: Add a target domain

To add a target domain, navigate to the **Penetration test** tab on the Agent Space overview page. Depending on whether you have already configured penetration testing, use one of the following methods:

- **First-time setup**: Choose **Set up penetration test** to open the penetration test wizard. In the first step, enter the domain and choose a verification method.
- **Adding a domain to an existing configuration**: In the **Target Domains** table, choose **Add domain**. Enter the domain and choose a verification method in the modal.

You can add a base domain or a sub-domain, such as `example.com` or `billing.example.com`. AWS suggests using a sub-domain where you have permission to create `TXT` records.

###### Note

When you verify a domain using DNS TXT or HTTP route verification, sub-domains of that domain are automatically covered. For example, verifying `example.com` allows you to test `api.example.com` or `billing.example.com` without additional verification. For Private VPC verification, the target endpoint domain name must match the full domain name configured for verification.

Choose one of the following verification methods:

- **DNS TXT record**: Prove domain ownership by creating a DNS TXT record with your DNS provider.
- **HTTP route**: Prove domain ownership by creating a route on your web server that contains a unique token provided by AWS Security Agent.
- **Private VPC**: Only usable for private VPC penetration testing. Verifies that the domain resolves to an IP in a private CIDR range. The domain name configured must match the full domain name of any associated target endpoints

## Step 2: Verify domain ownership

After adding the domain, verify ownership using the method you selected. You can trigger verification at any time from the **Target Domains** table by selecting the domain and choosing **Verify**.

### Verify using a DNS TXT record

AWS Security Agent generates a TXT DNS record value. You must add this record with your DNS provider to prove ownership.

**If the domain is registered in Route 53 (same AWS account):**

AWS Security Agent can create the DNS record automatically. Select the domain from the Target Domains table and choose **One-click verification**. AWS Security Agent creates the DNS validation record and completes verification automatically.

**If the domain is registered with another DNS provider:**

1. Copy the TXT record value provided by AWS Security Agent.
2. Add the TXT record with your DNS registrar.
3. Return to the Target Domains table, select the domain, and choose **Verify**.

### Verify using HTTP route validation

This method proves domain ownership by placing a unique token on your web server. Only domain owners or authorized web administrators can create routes on a web server, which proves ownership.

1. Create a file at the following path on your web server:

```
.well-known/aws/securityagent-domain-verification.json
```

2. Place the token provided by AWS Security Agent in the file using this format:

```
{
  "tokens": ["<insert-token>"]
}
```

3. Return to the Target Domains table, select the domain, and choose **Verify**. AWS Security Agent sends an HTTPS GET request to the verification URL and validates the token.
4. If the domain is accessible on the public internet, make sure that your domain has a valid SSL certificate before running verification.

###### Note

If your domain is registered in multiple Agent Spaces and you are using HTTP route validation, you can place the tokens for both Agent Spaces in the same `tokens` array.

## Bypass domain ownership verification

Customers who have authorization to perform penetration testing on an endpoint but cannot complete ownership verification can request manual verification from us. Please open a customer support case to make this request. Your request must include your business use case and your justification for manual ownership verification (i.e., why you are authorized to perform penetration testing on the endpoint).
