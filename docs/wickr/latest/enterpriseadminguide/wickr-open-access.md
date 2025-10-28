This guide provides documentation for Wickr Enterprise. If you're using AWS Wickr, see [AWS Wickr
Administration Guide](../adminguide/what-is-wickr.md "../adminguide/what-is-wickr.md").

# Wickr Open Access (WOA) configuration

Wickr Open Access (WOA) is an additional layer of network obfuscation that uses
various connection methods deployed through our external partner.

This is not a default service and requires an additional license provided by
Wickr.

If enabled, it can also be forced to **ON** for every user in a
security group.

###### Note

Enterprise deployments planning to use Wickr Open Access must turn on
**Enable TCP Proxy** using the KOTS Admin Console.

## Wickr Open Access (WOA) through

deeplink

Wickr Open Access can be enforced for initial client setup through deeplink
configuration. WOA must be force enabled in the user's security group for this capability
to function.
