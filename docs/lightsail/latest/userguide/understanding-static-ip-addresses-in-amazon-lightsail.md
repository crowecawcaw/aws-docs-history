# Static IP addresses in

Lightsail

A static IP is a fixed, public IP address that you can assign and reassign to an instance or
other resource. If you haven't set up a static IP address, each time you stop or restart your
instance, Lightsail assigns a new public IP address.

There are no costs associated with static IP addresses when they are attached to a
Lightsail instance. However, static IP addresses incur a charge when they aren't attached to
an instance. For more information, see [What do Lightsail static IPv4
addresses cost?](amazon-lightsail-frequently-asked-questions-faq-billing-and-account-management.md#what-do-lightsail-static-ips-cost "amazon-lightsail-frequently-asked-questions-faq-billing-and-account-management.md#what-do-lightsail-static-ips-cost").

###### Important

If you stop or restart your instance without first creating a static IP address and
attaching it to your instance, you lose your IP address when your instance restarts. You
should create a static IP address and attach it to your instance to ensure that your instance
always has the same public IP address. For more information, see [Create a static IP address](lightsail-create-static-ip.md "lightsail-create-static-ip.md").

###### Contents

- [Create a static IP
  address](lightsail-create-static-ip.md "lightsail-create-static-ip.md")
- [Delete a static IP address](how-to-delete-static-ip.md "how-to-delete-static-ip.md")
