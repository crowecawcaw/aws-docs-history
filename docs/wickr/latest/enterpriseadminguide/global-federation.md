This guide provides documentation for Wickr Enterprise. If you're using AWS Wickr, see [AWS Wickr
Administration Guide](../adminguide/what-is-wickr.md "../adminguide/what-is-wickr.md").

# Global Federation

Global Federation (GF) allows Wickr Enterprise to communicate with other Enterprise
deployments as well as Wickr Pro, AWS Wickr, and guest users.

This access must be approved and enabled on both deploys for a successful connection. It
cannot be federated without mutual agreement of all parties.

- For Wickr Pro federation, contact Wickr Support to allow list your deployment.
- For Global Federation, see the Global Federation: Setup and Configuration guide.
  Global Federation requires domain names and a new username style to be used.

- **Federated Wickr Infrastructures:** These are the
  **EXTERNAL** domains allowed to communicate with this deployment. The API key
  for that domain must be added with the domain name.
- **Local Domains for Federation:** These are the
  **INTERNAL** domains used for usernames within this deployment. A DNS record
  or other identifying information is needed for other Enterprise deployments to connect
  successfully. These local domains will be the only allowed domain names used when creating new
  users.
  For example, if the domain “example.com” and “testing.com” were added here, the following
  users would be valid:

- userone@example.com
- georgio@testing.com

## Restricted federation

Restricted federation is the ability to federate with specific networks (Enterprise or
AWS) belonging to different regions. Admins can allowlist specific networks their users can
federate with. After the restriction, users can only communicate with users in the allowlisted
networks. Both networks must allowlist each other from the security group settings in the
federation tab to use restricted federation.
