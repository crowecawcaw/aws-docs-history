**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the console](working-with-console.md "working-with-console.md").

# Adding and configuring resource protections with Shield Advanced

This page provides instructions for adding and configuring protections for your resources.

Shield Advanced only protects the resources that you specify, either through Shield Advanced or in a Firewall Manager
Shield Advanced policy. It doesn't automatically protect the resources of a subscribed account.

###### Note

If you use an AWS Firewall Manager Shield Advanced policy for your protections, you don't need to do this
step. You configure the policy with the types of resource to protect, and Firewall Manager
automatically adds protections to resources that are within scope of the policy.

If you don't use Firewall Manager, go through the following procedures for each account that has
resources to protect.

###### To choose the resources to protect using

Shield Advanced

1. Choose **Add resources to protect** from the subscription confirmation
   page of the prior procedure, or from the **Protected
   resources** or **Overview** page.
2. In the **Choose resources to protect with Shield Advanced** page, in **Specify the Region and resource types**, provide the Region and resource type specifications for the resources that you want to protect. You can protect resources in multiple Regions by selecting **All Regions** and you can narrow the selection to global resources by selecting **Global**. You can deselect any resource types that you do not want to protect. For information about protections for your resource types, see [List of resources that AWS Shield Advanced protects](ddos-protections-by-resource-type.md "ddos-protections-by-resource-type.md").
3. Choose **Load resources**. Shield Advanced populates the **Select Resources** section with the AWS
   resources that match your criteria.
4. In the **Select Resources** section, you can filter the list of resources by entering a string to search for in the resource listings.

Select the resources that you want
to protect. 5. In the **Tags** section, if you want to add tags to the Shield Advanced
protections that you are creating, specify those. For information about tagging
AWS resources, see [Working with Tag
Editor](../../../awsconsolehelpdocs/latest/gsg/tag-editor.md "../../../awsconsolehelpdocs/latest/gsg/tag-editor.md"). 6. Choose **Protect with Shield Advanced**. This adds Shield Advanced protections to the resources.
Continue through the console wizard screens to complete the configuration of
your resource protections.

###### Topics

- [Configuring application layer (layer 7) DDoS
  protections with AWS WAF](ddos-get-started-web-acl-rbr.md "ddos-get-started-web-acl-rbr.md")
- [Configuring health-based detection
  for your protections with Shield Advanced and Route 53](ddos-get-started-health-checks.md "ddos-get-started-health-checks.md")
- [Configuring alarms and
  notifications with Shield Advanced and Amazon SNS](ddos-get-started-create-alarms.md "ddos-get-started-create-alarms.md")
- [Reviewing and finishing your
  protection configuration in Shield Advanced](ddos-get-started-review-and-configure.md "ddos-get-started-review-and-configure.md")
