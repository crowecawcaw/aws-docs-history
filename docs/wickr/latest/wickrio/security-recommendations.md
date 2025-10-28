This guide provides documentation for Wickr IO Integrations. If you're
using AWS Wickr, see [AWS Wickr
Administration Guide](../adminguide/what-is-wickr.md "../adminguide/what-is-wickr.md").

# Security Recommendations

We recommend following best practices and if applicable, your organization's security
policies to secure your bot deployment. This can include, but isn't restricted to, firewall
rules, host system access auditing, regular host system OS updates, and monitoring. We designed
Wickr IO bots to be both powerful and flexible for custom use cases and while they inherit many
security protections from our standard Wickr clients, it falls on you to secure the host system
appropriately to protect it (and your bot) from unauthorized access. For more information on
shared responsibility, see [Shared Responsibility
Model](https://aws.amazon.com/compliance/shared-responsibility-model/ "https://aws.amazon.com/compliance/shared-responsibility-model/").

The Wickr IO bot container is moderately hardened to remove unnecessary services, etc.,
but its threat model assumes that it is deployed on an internal network segment and configured as
a client system. Don't forget to augment your security controls as you expand your use cases. The
bottom line is if you lose control of your bot host, you will likely lose control of your bot and
all the data. Log only what you need to log, encrypt what you need to encrypt, and use strong
access controls.

Bots are not isolated by default. Users outside your network can interact with bots if they
guess the bot username and your security group allows external federation. For more information,
see [Security groups for AWS Wickr](../adminguide/security-groups.md "../adminguide/security-groups.md") .
