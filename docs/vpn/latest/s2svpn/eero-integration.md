# AWS Site-to-Site VPN and eero Integration

AWS Site-to-Site VPN has collaborated with [eero](http://eero.com "http://eero.com") to make it
simple and convenient for organizations to establish secure connectivity between their remote sites
and AWS in just a few clicks.

This solution leverages eero’s WiFi access points and network gateways to provide local connectivity.
Using eero’s gateway appliances and Site-to-Site VPN, customers can automatically establish VPN
connectivity to access their applications hosted in AWS such as payment gateways for point of sales
systems in just a few clicks. This makes it simple and faster for customers to scale their remote
site connectivity across hundreds of sites and eliminates the need for an onsite technician with
networking expertise to set-up the connectivity. This solution is suitable for distributed enterprises
with up to 500 remote offices, with each office having up to 100 users.

To learn more about this integration, including detailed set-up guide, check the
[eero documentation](https://support.eero.com/hc/en-us/articles/42827838351899-AWS-Account-and-VPN-Configuration "https://support.eero.com/hc/en-us/articles/42827838351899-AWS-Account-and-VPN-Configuration").

###### Note

There are no changes to the functionality of AWS Site-to-Site VPN as part of this integration.

**Considerations:**

- Available only for VPN connections attached to a Transit Gateway or to Cloud WAN. Not supported for Virtual Private Gateway attachments.
- 5 Gbps tunnels are not supported.
- Site-to-Site VPN Concentrator is not supported.
- Site-to-Site VPN
  [quotas](vpn-limits.md "vpn-limits.md")
  do not change with this integration.
