

# Categorize Lightsail resources with tags
<a name="amazon-lightsail-adding-tags-to-a-resource"></a>

Use tags in Amazon Lightsail to categorize your resources by purpose, owner, environment, or other criteria. Tags can be added to resources at or after they are created. Follow these steps to add tags to a resource after it’s been created.

**Note**  
For more information about tags, what resources can be tagged, and the restrictions, see [Tags](amazon-lightsail-tags.md).

**To add tags to a resource**

1. Sign in to the [Lightsail console](https://lightsail.aws.amazon.com/).

1. In the left navigation pane, choose the tab for the resource type that you want to tag. For example, to add a tag to a DNS zone, choose the **Networking** tab. Or choose the **Instances** tab to add a tag to an instance.
**Note**  
Instances, container services, CDN distributions, buckets, databases, disks, DNS zones, and load balancers can be tagged using the Lightsail console. However, more Lightsail resources can be tagged using the [Lightsail API operations](https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/Welcome.html), or the [AWS Command Line Interface](https://docs.aws.amazon.com/cli/latest/reference/lightsail/) (AWS CLI) or SDKs. For a full list of Lightsail resources that support tagging, see [Tags](amazon-lightsail-tags.md).

1. Choose the resource that you want to tag.

1. On the management page for the resource that you selected, choose the **Tags** tab.  
![Tags tab in the Lightsail console.](http://docs.aws.amazon.com/lightsail/latest/userguide/images/amazon-lightsail-tags-tab.png)

1. Choose **Manage tags**.

1. Use one of the following options, depending on the type of tag that you want to create—you can also edit tags that have already been added from this tab:
   + Create key-only tags

     1. Choose **Add new tag**.

     1. Enter a value for the **Key** for each tag that you want to create.

     1. Choose **Save** when you're done entering your tags, or choose **Cancel** to not add them.  
![Key-only tags in the Lightsail console.](http://docs.aws.amazon.com/lightsail/latest/userguide/images/amazon-lightsail-key-only-tags.png)
   + Create key-value tags

     1. Choose **Add new tag**.

     1. Enter a value for the **Key** and **Value** for each tag that you want to create.

     1. Choose **Save** when you're done entering your tags, or choose **Cancel** to not add them.  
![Key-value tags in the Lightsail console.](http://docs.aws.amazon.com/lightsail/latest/userguide/images/amazon-lightsail-key-value-tag.png)

## Next steps
<a name="adding-tags-to-a-resource-next-steps"></a>

For more information about tasks that you can perform after adding tags to a resource, see the following guides:
+ [Use tags to organize your resources](amazon-lightsail-organizing-resources-using-tags.md)
+ [Use tags to organize costs for your resources](amazon-lightsail-organizing-costs-using-tags.md)
+ [Use tags to control access to your resources](amazon-lightsail-controlling-access-using-tags.md)
+ [Delete tags](amazon-lightsail-deleting-tags.md)