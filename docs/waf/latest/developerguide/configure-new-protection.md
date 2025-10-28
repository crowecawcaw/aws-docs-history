**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the updated console experience](working-with-console.md "working-with-console.md").

# Adding AWS Shield Advanced protection to AWS resources

Follow the guidance in this section to add Shield Advanced protection to one or more
resources.

###### To add protection for an AWS resource

1. Sign in to the AWS Management Console and open the AWS WAF & Shield console at
   [https://console.aws.amazon.com/wafv2/](https://console.aws.amazon.com/wafv2/ "https://console.aws.amazon.com/wafv2/").
2. In the navigation pane, under AWS Shield choose **Protected
   resources**.
3. Choose **Add resources to protect**.
4. In the **Choose resources to protect with Shield Advanced** page, in **Specify the Region and resource types**, provide the Region and resource type specifications for the resources that you want to protect. You can protect resources in multiple Regions by selecting **All Regions** and you can narrow the selection to global resources by selecting **Global**. You can deselect any resource types that you do not want to protect. For information about protections for your resource types, see [List of resources that AWS Shield Advanced protects](ddos-protections-by-resource-type.md "ddos-protections-by-resource-type.md").
5. Choose **Load resources**. Shield Advanced populates the **Select Resources** section with the AWS
   resources that match your criteria.
6. In the **Select Resources** section, you can filter the list of resources by entering a string to search for in the resource listings.

Select the resources that you want
to protect. 7. In the **Tags** section, if you want to add tags to the Shield Advanced
protections that you are creating, specify those. For information about tagging
AWS resources, see [Working with Tag
Editor](../../../awsconsolehelpdocs/latest/gsg/tag-editor.md "../../../awsconsolehelpdocs/latest/gsg/tag-editor.md"). 8. Choose **Protect with Shield Advanced**. This adds Shield Advanced protections to the resources.
