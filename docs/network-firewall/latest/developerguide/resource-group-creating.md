# Creating a resource group in AWS Network Firewall

Use tag-based resource groups to identify collections of AWS resources. You can track the resource groups in your Network Firewall stateful rule groups, to ensure that your rules stay in sync as your resources change.

You can create a resource group for use in AWS Network Firewall either in the Network Firewall console or with the AWS Resource Groups [CreateGroup](../../../ARG/latest/APIReference/API_CreateGroup.md "../../../ARG/latest/APIReference/API_CreateGroup.md") API. Use the following procedure to create a resource group in the Network Firewall console. For information about creating a resource group in Resource Groups, see [AWS::NetworkFirewall::RuleGroup](../../../ARG/latest/userguide/about-slg.md#about-slg-types-network-firewall-rulegroup "../../../ARG/latest/userguide/about-slg.md#about-slg-types-network-firewall-rulegroup") in the _Resource Groups User Guide_.

###### To create a resource group in the console

1. Sign in to the AWS Management Console and open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the navigation pane, under **Network Firewall**, choose **Network Firewall resource groups**.
3. Choose **Create resource group**.
4. Enter a **Name** to identify the resource group.

###### Note

You can't change the name after you create the resource group. 5. (Optional) Enter a **Description** for the resource group. 6. For **Grouping criteria**, choose the resource types and tags to associate to this resource group. As you create, update, or delete resources in your account in the current Region that match the grouping criteria, Network Firewall automatically updates this resource group with those changes.

    * **Resource types** - Choose the resource types to include in the resource group. Network Firewall supports the following resource types:




    	+ Amazon EC2 instances
    	+ Amazon EC2 network interfaces
    * **Tags** - Add key value tags to the resource types. A tag consists of a key and a value, both of which you define. For example, if you have two Amazon EC2 instances, you might assign both a tag key of "Stack." But the value of "Stack" might be "Testing" for one and "Production" for the other. You can choose from the existing tags in your account, or add your own tags. For information about best practices for tagging resources, see [Best practices for tag names](../../../tag-editor/latest/userguide/tagging.md#id_tags_naming_best_practices "../../../tag-editor/latest/userguide/tagging.md#id_tags_naming_best_practices") in the *AWS Tag Editor User Guide*.

7. Select the **Preview resources** button to preview the resources in your account in the current Region that match the grouping criteria. The resources that match the grouping criteria display in the **Preview resources** section. If there aren't resources that match the grouping criteria, no resources will display. However, if at any time you create resources that match the grouping criteria, Network Firewall will automatically display these resources in the **Preview resources** pane.
8. (Optional) In the **Add tags** section, enter a key and optional value for any
   tag that you want added to this resource group. Tags help you organize and
   manage your AWS resources. For more information about tagging your
   resources, see [Tagging AWS Network Firewall resources](tagging.md "tagging.md").
9. Choose **Create resource group**.
   Your new resource group is added to the list in the **Resource group**
   page.

To use a resource group, include the resource group's Amazon Resource Name (ARN) in a stateful rule's IP set reference. For information about using resource groups in IP set references, see [Referencing resource groups](rule-groups-ip-set-references.md#rule-groups-referencing-resource-groups "rule-groups-ip-set-references.md#rule-groups-referencing-resource-groups").
