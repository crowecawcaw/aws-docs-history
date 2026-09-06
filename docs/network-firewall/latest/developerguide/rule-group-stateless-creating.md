

# Creating a stateless rule group
<a name="rule-group-stateless-creating"></a>

Follow the guidance in this section to create a stateless rule group through the Network Firewall console.

**To create a stateless rule group**

1. Sign in to the AWS Management Console and open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, under **Network Firewall**, choose **Network Firewall rule groups**.

1. Choose **Create Network Firewall rule group**. 

1. On the **Describe rule group** page, provide the following information:

   1. Enter a name and description for the rule group. You'll use these to identify the rule group when you manage it and use it.
**Note**  
You can't change the name after you create the rule group.

   1. For **Capacity**, set the maximum capacity you want to allow for the stateless rule group, up to the maximum of 30,000. You can't change this setting after you create the rule group. For information about how to calculate this, see [Setting rule group capacity in AWS Network Firewall](nwfw-rule-group-capacity.md). For information about the maximum setting, see [AWS Network Firewall quotas](quotas.md).

   1. (Optional) Under **Customer managed key**, toggle the **Customize encryption settings** option to configure your customer managed key. For more information about this option, see [Encryption at rest with AWS Key Management Service](kms-encryption-at-rest.md).

   1. (Optional) Under **Tags**, enter a key and optional value for any tag that you want added to this rule group. Tags help you organize and manage your AWS resources. For more information about tagging your resources, see [Tagging AWS Network Firewall resources](tagging.md).

1. Choose **Next**.

1. On the **Choose rule group type** page, for the **Rule group format**, choose **Stateless rule group**.

1. Choose **Next**.

1. On the **Configure rules** page, review the rules that you want to add to the stateless rule group. Determine roughly what order you want Network Firewall to process them within the rule group. You need to provide unique, positive integer priority settings for your rules to indicate the processing order. Network Firewall processes from the lowest number up. We recommend using numbers with room in between, to allow for future insertions within the list of rules. For example, you might start with rule priorities numbered 100, 200, and so on. 

   Add each rule to the rule group as follows: 

   1. For **Priority**, provide the priority to set the processing order of your rule. 

   1. Choose the protocol and the source and destination settings for your rule. 

   1. (Optional) For **TCP flags** provide the masks and flags that you want to inspect for. In **Masks**, indicate the flags that you want to inspect. In **Flags**, indicate which of the flags that you selected in **Masks** must be set. The other flags that you selected in **Masks** must be unset. 

   1. For **Actions**, do the following: 

      1. For **Action**, select the standard action that you want Network Firewall to take when a packet matches the rule settings. 

      1. (Optional) For **Publish metrics**, add a new named custom action or select one that you've already created in the rule group. This option sends an Amazon CloudWatch metric dimension named `CustomAction` with a value that you specify. 

      For additional information on these options, see [Actions for stateless rules](rule-action.md#rule-action-stateless). 

   1. Choose **Add rule**. Your rule is added to the **Rules** list for the rule group, ordered by priority.

1. Choose **Next**.

1. Review the settings for the rule group, then choose **Create stateless rule group**. 

Your new rule group is added to the list in the **Network Firewall rule groups** page.

To use your rule group in a firewall policy, follow the procedures at [Managing your firewall policy](firewall-policy-managing.md).