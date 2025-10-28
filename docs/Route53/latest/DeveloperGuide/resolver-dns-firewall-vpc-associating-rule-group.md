# Managing

associations between your VPC and Route 53 Resolver DNS Firewall rule group

###### To view a rule group's VPC associations

1. Sign in to the AWS Management Console and open the Route 53 console at
   [https://console.aws.amazon.com/route53/](https://console.aws.amazon.com/route53/ "https://console.aws.amazon.com/route53/").

Choose **DNS Firewall** in the navigation pane to open the DNS Firewall
**Rule groups** page on the Amazon VPC console.

- OR -

Sign in to the AWS Management Console and open the

the Amazon VPC console under [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/"). 2. In the navigation pane, under **DNS Firewall**, choose **Rule groups**. 3. On the navigation bar, choose the Region for the rule group. 4. Select the rule group that you want to associate. 5. Choose **View details**. The rule group page displays. 6. Toward the bottom, you can see a tabbed details area that includes rules
and associated VPCs. Choose the tab **Associated
VPCs**.

###### To associate a rule group with a VPC

1. Locate the rule group's VPC associations by following the instructions in
   [the preceding
   procedure](resolver-dns-firewall-rule-group-sharing.md "resolver-dns-firewall-rule-group-sharing.md")
   **To view a rule group's VPC associations**.
2. In the **Associated VPCs** tab, choose
   **Associate VPC**.
3. Locate the VPC that you want to associate with the rule group in the
   dropdown. Select it, then choose **Associate**.
   In the rule group page, your VPC is listed in the **Associated
   VPCs** tab. At first, the association's **Status**
   reports **Updating**. When the association is complete, the status
   changes to **Complete**.
