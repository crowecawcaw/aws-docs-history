# Enable an application domain for penetration testing

Before you can run a penetration test on an application, you need to verify its domain name. AWS Security Agent will only perform penetration tests against validated domains.

###### Note

You do not need to validate ancillary domains that your application may use. You only need to validate the domain you will actively run penetration tests against.

1. Navigate to the Agent Space overview page
2. Select the **Penetration test** tab
3. Select **Add domain**
4. Enter the domain you want to validate. You can validate a base domain, or a sub-domain, such as `example.com` or `billing.example.com`. AWS suggests validating a sub-domain where you have permission to create `TXT` records.
5. Validate the domain. You can validate the domain in two ways:
   - **DNS_TXT validation**: You prove domain ownership by creating a DNS TXT record.
     - **Domains registered in Route53**: AWS Security Agent can automatically create the validation DNS records if the domain is registered in the same AWS Account.
     - **Other domains**: AWS Security Agent will generate a `TXT` DNS record. Update your DNS records with your registrar to include this validation record.

   - **HTTP_ROUTE validation**: You prove domain ownership by creating a route path containing a unique token provided by the service in a certain JSON format on your web server. This method leverages the fact that only domain owners (or their authorized web administrators) can create routes to their web servers.
     - The route path should be created at the root of the domain. The route path is `.well-known/aws/securityagent-domain-verification.json`
     - The format for placing the tokens is:

     ```
     {
       "tokens": ["<insert-token>"]
     }
     ```

     - After you have placed the token, you can verify your ownership. The Security Agent service will do an HTTPS GET request call to the entire verification URL and will verify the token.
     - If the domain is accessible on the public internet, make sure that your domain has a valid SSL certificate.

###### Note

If your domain is registered in multiple agent spaces and you are using HTTP_ROUTE verification method, you can place the tokens provided to you for both agent spaces in the same `tokens` array.
