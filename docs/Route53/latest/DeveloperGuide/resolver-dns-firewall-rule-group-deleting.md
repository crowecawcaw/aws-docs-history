# Deleting a rule

group

To delete a rule group, perform
the following procedure.

###### Important

If you delete a rule group that's associated with a VPC, DNS Firewall removes
the association and stops the protections that the rule group was providing
to the VPC.

###### Deleting DNS Firewall entities

When you delete an entity that you can use in DNS Firewall, like a domain list that might be in use in a rule group, or a rule group that might be associated with a VPC, DNS Firewall checks to see if the entity is currently being
used. If it finds that it is in use, DNS Firewall warns you. DNS Firewall is almost
always able to determine if an entity is in use. However, in
rare cases it might not be able to do so. If you need to be sure that nothing is
currently using the entity, check for it in your DNS Firewall configurations before deleting
it. If the entity is a referenced domain list, check that no rule groups are using it. If the entity is a rule group,
check that it is not associated with any VPCs.

###### To delete a rule group

1. Sign in to the AWS Management Console and open the Route 53 console at
   [https://console.aws.amazon.com/route53/](https://console.aws.amazon.com/route53/ "https://console.aws.amazon.com/route53/").

Choose **DNS Firewall**
in the navigation pane to open the DNS Firewall **Rule groups** page on
the Amazon VPC console. Continue to step 3.

- OR -

Sign in to the
AWS Management Console and open the

the Amazon VPC console under [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/"). 2. In the navigation pane, under **DNS Firewall**,
choose **Rule
groups**. 3. On the navigation bar, choose the Region for the rule group. 4. Select the rule group that you want to delete, then choose **Delete**, and confirm the deletion.
