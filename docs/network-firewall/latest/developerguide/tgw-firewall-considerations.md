# Considerations for transit gateway-attached firewalls

Before you create or use a transit gateway-attached firewall, consider the following points. For considerations that apply to all firewalls, see [Considerations for working with firewalls and firewall endpoints](firewall-and-firewall-endpoints-considerations.md "firewall-and-firewall-endpoints-considerations.md").

- A transit gateway-attached firewall involves multiple AWS services: AWS Network Firewall, AWS Transit Gateway, and AWS RAM.
- If the Transit Gateway owner and Network Firewall owner are different AWS accounts:
  - The Network Firewall account owner depends on the Transit Gateway owner to share the transit gateway.
  - Either account can delete the transit gateway-attached firewall.
  - The Transit Gateway owner has limited visibility into firewall details.
  - The Transit Gateway owner cannot delete the shared transit gateway until they remove all transit gateways attachments, including related transit gateway-attached firewalls.

- When you use stateful domain list rule groups or other stateful rule group types that reference `HOME_NET` or `EXTERNAL_NET`, you must configure these rule groups to use values for `HOME_NET` and `EXTERNAL_NET` that are different from the default values used in the firewall policy. For more information, see [Limitations and caveats
  for stateful rules in AWS Network Firewall](suricata-limitations-caveats.md "suricata-limitations-caveats.md").
- A transit gateway-attached firewall must be configured in the same Availability Zone where the shared transit gateway is already enabled.
- Traffic for transit gateway-attached firewalls must be routed through transit gateway route tables, not VPC route tables.
- Appliance mode is always enabled on transit gateway-attached firewalls.
