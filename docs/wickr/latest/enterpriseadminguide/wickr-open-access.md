

This guide provides documentation for Wickr Enterprise. If you're using AWS Wickr, see [AWS Wickr Administration Guide](https://docs.aws.amazon.com/wickr/latest/adminguide/what-is-wickr.html).

# Wickr Open Access (WOA) configuration
<a name="wickr-open-access"></a>

Wickr Open Access (WOA) is an additional layer of network obfuscation that uses various connection methods deployed through our external partner.

This is not a default service and requires an additional license provided by Wickr.

If enabled, it can also be forced to **ON** for every user in a security group.

**Note**  
Enterprise deployments planning to use Wickr Open Access must turn on **Enable TCP Proxy** using the KOTS Admin Console.

## Wickr Open Access (WOA) through deeplink
<a name="wickr-open-access-deeplink"></a>

Wickr Open Access can be enforced for initial client setup through deeplink configuration. WOA must be force enabled in the user's security group for this capability to function.