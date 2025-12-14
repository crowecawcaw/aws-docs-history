**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the console](working-with-console.md "working-with-console.md").

# Resource protections in AWS Shield Advanced

You can add and configure AWS Shield Advanced protections for your resources. You can manage
protections for a single resource and you can group your protected resources into logical
collections for better event management. You can also track changes to your Shield Advanced protections using AWS Config.

###### Note

Shield Advanced protects only resources that you have specified either in Shield Advanced or through
an AWS Firewall Manager Shield Advanced policy. It doesn't automatically protect your resources.

If you're using an AWS Firewall Manager Shield Advanced policy, you don't need to manage protections for
resources that are in scope of the policy. Firewall Manager automatically manages protections for
accounts and resources that are in scope of a policy, according to the policy configuration.
For more information, see [Using AWS Shield Advanced policies in Firewall Manager](shield-policies.md "shield-policies.md").

###### Topics

- [List of resources that AWS Shield Advanced protects](ddos-protections-by-resource-type.md "ddos-protections-by-resource-type.md")
- [Protecting Amazon EC2 instances and Network Load Balancers with Shield Advanced](ddos-protections-ec2-nlb.md "ddos-protections-ec2-nlb.md")
- [Protecting the application layer (layer 7) with AWS Shield Advanced and AWS WAF](ddos-app-layer-protections.md "ddos-app-layer-protections.md")
- [Health-based detection using
  health checks with Shield Advanced and Route 53](ddos-advanced-health-checks.md "ddos-advanced-health-checks.md")
- [Adding AWS Shield Advanced protection to AWS resources](configure-new-protection.md "configure-new-protection.md")
- [Editing AWS Shield Advanced protections](manage-protection.md "manage-protection.md")
- [Creating alarms and notifications for resources protected by Shield Advanced](add-alarm-ddos.md "add-alarm-ddos.md")
- [Removing AWS Shield Advanced protection from an AWS resource](remove-protection.md "remove-protection.md")
- [Grouping your AWS Shield Advanced protections](ddos-protection-groups.md "ddos-protection-groups.md")
- [Tracking Shield Advanced resource protection changes in AWS Config](ddos-add-config.md "ddos-add-config.md")
