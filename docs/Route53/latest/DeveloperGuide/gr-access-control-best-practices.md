# Access control best practices and security

considerations

Follow these best practices to maintain secure and effective access controls for your
Route 53 Global Resolver infrastructure.

## Security best practices

Implement these security measures to protect your DNS infrastructure:

- **Use layered authentication** - Combine access sources for trusted networks with tokens for mobile users. This approach
  provides defense in depth and accommodates different client scenarios.
- **Implement least privilege access** - Grant access only to the IP ranges and protocols that clients actually need. Avoid
  overly broad access source rules that could expose your infrastructure to unauthorized
  use.
- **Rotate tokens regularly** - Replace access tokens on a regular schedule, even before they expire. This practice
  limits the impact of compromised tokens and maintains security hygiene.
- **Monitor access patterns** - Review DNS query logs to identify unusual access patterns or potential security issues.
  Set up alerts for queries from unexpected IP ranges or using expired tokens.

## Operational best practices

Follow these operational practices to maintain reliable access controls:

- **Document your access control strategy** - Maintain clear
  documentation of which access sources and tokens serve which client groups.
- **Test access controls regularly** - Verify that your access
  source rules and tokens work correctly from different client locations and scenarios.
- **Plan for token renewal** - Establish processes for
  distributing new tokens before old ones expire to avoid service disruptions.
- **Review access controls periodically** - Remove unused
  access source rules and expired tokens to maintain a clean configuration.
