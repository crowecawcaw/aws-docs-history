# Copying threat signature rules into your own AWS Network Firewall rule group

Network Firewall provides full visibility into the threat signature rule content of its AWS managed rules.
This enables you to choose between using the rule group as-is in your firewall policy
or copying the rule group's rules into your own rule group and customizing them for your specific needs.

###### Important

Copied rules don't automatically inherit rule updates that AWS makes to managed rule group rules. We recommend that you subscribe to Amazon SNS topics for updates made to the originating rule group. For more information, see [Notifications for threat signature rule group updates](using-managed-rule-groups-sns.md "using-managed-rule-groups-sns.md"). You're responsible for validating rule changes and making sure that your own rules are up-to-date.

To copy a managed threat signature rule group's rules, create a local copy of the rule group rules, make your modifications, then create your own rule group. The following procedure explains how to copy a threat signature rule group's rules, and then create your own rule group.

Console

###### To copy a managed threat signature rule group's rules using the console

1. Sign in to the AWS Management Console and open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the navigation pane, under **Network Firewall**, choose **Network Firewall rule groups**.
3. In the **AWS managed rule groups** tab, under **Threat signature rule groups**, select a rule group to view its details.
4. Choose **Duplicate rule group** to copy the rules into your own rule group. You can modify the rule group details, and then choose **Create rule group**.

Alternatively, you can choose **Copy** to copy the rules to your clipboard. You can then modify them in a text editor, or create a new rule group and paste the rules into your own stateful rule group. For information about how to create your own stateful rule group, see [Creating a stateful rule group](rule-group-stateful-creating.md "rule-group-stateful-creating.md").

CLI

###### To copy a managed threat

signature
rule group's rules using the
AWS CLI

1. Run `aws network-firewall
list-rule-groups --scope MANAGED --managed-type
AWS_MANAGED_THREAT_SIGNATURES` to filter the
   AWS managed threat signature rule
   groups.
2. In the following command, replace `rulegroup-arn` with the Amazon Resource Name (ARN) of the threat signature managed rule group that you'd like to copy:

`aws network-firewall describe-rule-group --rule-group-arn `rulegroup-arn``.

Network Firewall returns the rule group details in the response, which you can parse and modify in your text editor. Then, you can use the modified rule group details to create your own rule group using the command [create-rule-group](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/network-firewall/create-rule-group.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/network-firewall/create-rule-group.html").
