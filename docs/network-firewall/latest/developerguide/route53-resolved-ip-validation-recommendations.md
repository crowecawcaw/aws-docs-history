

# Recommendations for configuring resolved IP validation
<a name="route53-resolved-ip-validation-recommendations"></a>

The following recommendations help you roll out resolved IP validation safely and apply it across your network.

Starting in alert mode so that DNS caches can refresh  
When you first enable the feature, set `Action` to `ALERT` and keep it there for about 24 hours before you switch to `DROP` or `REJECT`. Resolved IP validation recognizes a destination only after the domain has been resolved through your VPC's Amazon Route 53 Resolver. This period gives clients time to refresh their DNS caches and repopulate resolutions. Watch the flow logs and metrics during this window (see [Monitoring and troubleshooting resolved IP validation](route53-resolved-ip-validation-troubleshooting.md)) and switch to enforcement after the rate of unresolved flows settles.

Scoping the rule group to one firewall deployment  
To protect more than one VPC with the same firewall, associate the *same* Amazon Route 53 Resolver DNS Firewall rule group with each of those VPCs. This is the rule group that your policy's resolved IP validation references. Associating the same rule group is what brings each VPC's resolutions into the set that the firewall validates against.  
Don't reuse that rule group for other firewalls or for unrelated deployments. Every associated VPC contributes to one shared pool of resolutions. A destination that any of those VPCs resolved becomes valid for all of them. That includes VPCs that never send traffic through this firewall. Sharing a rule group across unrelated deployments therefore widens what each firewall accepts. Use a separate rule group for each firewall deployment.

Keeping traffic in its Availability Zone, or using a transit gateway-attached firewall  
Validation is scoped to the Availability Zone: a firewall endpoint validates against the resolutions recorded in its own Availability Zone. Multi-zone deployments work as long as routing is zone-aligned—clients in an Availability Zone reach the firewall endpoint in that same zone. A connection can cross zones to reach a firewall endpoint. In that case, the firewall can't tell that the client is in a different zone. The connection fails validation as *unresolved*, and Network Firewall applies your `Action` setting to it.  
For a centralized deployment that inspects traffic from multiple zones, use a transit gateway-attached firewall. The transit gateway attachment carries the client's Availability Zone with the traffic, so the firewall validates against the correct zone. For more information, see [Transit gateway-attached firewalls](https://docs.aws.amazon.com/network-firewall/latest/developerguide/tgw-firewall.html).