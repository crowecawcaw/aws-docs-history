# Managing Your Rule Groups

## Creating Rule Groups

###### Note

Network Firewall Proxy is in public preview release and is subject to change.

A Rule Group in VPC Proxy is a reusable collection of ordered access control rules (ACLs) used to evaluate and filter HTTP/s traffic.

###### To create a Rule Group

1. Sign in to the AWS Management Console and open the Amazon VPC console.
2. In the navigation pane, under **Network Firewall Proxy**, choose **Proxy rule groups**.
3. Choose **Create rule group**.
4. Enter a name.
5. (Optional) Enter a description for your rule group and add a tag.
6. Choose **Next**.
7. Enter the phase to which this rule applies. To apply the rule to all three phases, select all three phases. This creates three different rules for each phase.
8. Enter the action that you want to take on the traffic. This can be allow, deny, or alert.
9. (Optional) Enter a description for the rule.
10. Enter the conditions, operators, and values. Condition operators define how to perform a match. Condition keys define what is to be matched. Condition values specify the exact value that needs to be matched against.
11. Choose **Next**.
12. Review the details and choose **Create**.

## Rule group operations

Network Firewall Proxy enables you to organize and manage collections of rules through rule groups. These rule groups can exist independently of proxy configurations and provide efficient rule management. Here are the available rule group management actions:

**Create rule group**

Creates a new rule group that can contain multiple rules. The rule group can exist independently without requiring a proxy configuration.

**Modify rule groups**

Remove/ add rules to a rule group.

**Modify rule priorities**

Reorders rules within a rule group based on phase type. This allows you to adjust rule priorities, where rules with lower index positions receive higher priority.

**Delete rule group**

Removes the specified rule group and all its associated rules.

1. Make sure your rule groups is not being used in any proxy. If rule group is being used, you will receive an error.
2. Click on rule group.
3. Click on the delete button.
4. It will take a while for this rule group to get deleted but the rule group cannot be used anymore.

**Describe rule group**

Retrieves detailed information about a specific rule group configuration.

1. On the AWS console, click on rule groups.
2. Select the rule group to list all the rules under that rule group.

**List rule groups**

Displays all proxy rule group resource names present in an account.
