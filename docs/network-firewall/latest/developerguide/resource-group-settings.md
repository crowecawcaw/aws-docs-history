# Settings for the resource groups that you use in AWS Network Firewall

The tag-based resource groups that you configure for Network Firewall help ensure that your rules stay in sync as your AWS resources change. You can reference a resource group in your Network Firewall stateful rule groups.

The following settings apply to resource groups.

- **Name** – The identifier for the resource group. You
  assign a unique name to every resource group. You can't change the name of a
  resource group after you create it.
- **Description** – Optional additional
  information about the resource group. Fill in any information that might help
  you remember the purpose of the resource group and how you want to use it. The
  description is included in resource group lists in the console and through the
  APIs.
- **Grouping criteria** – Tag the resource types to add to the resource group. A tag consists of a key and a value, both of which you define. A resource type is a type of AWS resource, such as an Amazon EC2 instance. Network Firewall adds to the resource group all the resource types within your account matching the tags. As you create, update, or delete resource types that match the tags, Network Firewall automatically updates the resource group to include the resources. Network Firewall constantly checks your account for resources that match the grouping criteria.
- **Preview resources** – A list of all of the resources within your account in the current Region that match the grouping criteria.
- **Tags** – Optional key-value tag pairs. These tags apply to the resource group itself, not the individual resources within it. You can use tags to search and filter your resources and to track your AWS costs. For more information about tags, see
  [Tagging AWS Network Firewall resources](tagging.md "tagging.md").
