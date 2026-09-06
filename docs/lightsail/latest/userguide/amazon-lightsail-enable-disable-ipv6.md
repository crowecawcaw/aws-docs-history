

# Enable or disable dual-stack networking for Lightsail resources
<a name="amazon-lightsail-enable-disable-ipv6"></a>

IPv6 is enabled by default for Lightsail dual-stack instances, container services, and load balancers created on or after January 12, 2021. You can optionally enable IPv6 for those resources that were created before January 12, 2021. In this guide, we show you how to enable or disable IPv6 networking for a dual-stack instance. For more information about IPv6, see [IP addresses](understanding-public-ip-and-private-ip-addresses-in-amazon-lightsail.md).

## Dual-stack considerations
<a name="ipv6-considerations"></a>

IPv6 became available in Lightsail on January 12, 2021; therefore, you might need to manually enable or disable IPv6 for some of your resources according to the following guidelines:
+ Instances and load balancers created *before* January 12 have IPv6 disabled until you enable it. However, instances and load balancers created *after* January 12 have IPv6 enabled when they are created.
+ Container services created *before* or *after* January 12 have IPv6 enabled.
+ IPv6 can be manually enabled or disabled for instances, and load balancers at any time. It cannot be disabled for container services.

Keep the following in mind when you enable and use IPv6:
+ Your resources can communicate over IPv4 only, or over IPv4 and IPv6 (in dual-stack mode) when you enable IPv6 for a resource.
+ When you enable IPv6 for an instance, Lightsail automatically assigns an IPv6 address to that instance; you cannot choose or specify the IPv6 address yourself. When you enable IPv6 for a container service or load balancer, that resource will begin accepting internet traffic over IPv6.
+ The IPv6 address for an instance persists when you stop and start your instance. It's released only when you delete your instance, or disable IPv6 for your instance. You cannot get the IPv6 address back after you perform either of those actions.
+ All IPv6 addresses that are assigned to your instances are public and reachable over the internet. There are no private IPv6 addresses that are assigned to your instances.
+ IPv4 and IPv6 addresses for instances are independent of each other; you must configure instance firewall rules separately for IPv4 and IPv6. For more information, see [Instance firewalls](understanding-firewall-and-port-mappings-in-amazon-lightsail.md).
+ Not all instance blueprints available in Lightsail are automatically configured for IPv6 when IPv6 is enabled. Instances that use the following blueprints require additional configuration steps after you enable IPv6 for them:
  + **cPanel** – For more information, see [Configure IPv6 for cPanel instances](amazon-lightsail-configure-ipv6-on-cpanel.md).
  + **GitLab** – For more information, see [Configure IPv6 for GitLab instances](amazon-lightsail-configure-ipv6-on-gitlab.md).
  + **Nginx** – For more information, see [Configure IPv6 for Nginx instances](amazon-lightsail-configure-ipv6-on-nginx.md).
  + **Plesk** – For more information, see [Configure IPv6 for Plesk instances](amazon-lightsail-configure-ipv6-on-plesk.md).

**Topics**
+ [Dual-stack considerations](#ipv6-considerations)
+ [Enable IPv6 networking for Lightsail resources](enable-ipv6.md)
+ [Disable IPv6 networking for Lightsail resources](disable-ipv6.md)