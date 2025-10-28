# Getting started with Route 53 Resolver

The Route 53 Resolver console includes a wizard that guides you through the following steps for getting started with Resolver:

- Create endpoints: inbound, outbound, or both.
- For outbound endpoints, create one or more forwarding rules, which specify the domain names for which
  you want to route DNS queries to your network.
- If you created an outbound endpoint, choose the VPC that you want to associate the rules with.

###### To configure Route 53 Resolver using the wizard

1. Sign in to the AWS Management Console and open the Resolver console at
   [https://console.aws.amazon.com/route53resolver/](https://console.aws.amazon.com/route53resolver/ "https://console.aws.amazon.com/route53resolver/").
2. On the **Welcome to Route 53 Resolver** page, choose **Configure endpoints**.
3. On the navigation bar, choose the Region where you want to create a Resolver endpoint.
4. Under **Basic configuration**, choose the direction that you want to forward DNS queries:
   - **Inbound and outbound**: The wizard guides you through settings that let you both
     forward DNS queries from resolvers on your network to Resolver in a VPC, and forward specified queries (such as example.com or
     example.net) from a VPC to resolvers on your network.
   - **Inbound only**: The wizard guides you through settings that let you forward DNS queries
     from resolvers on your network to Resolver in a VPC.
   - **Outbound only**: The wizard guides you through settings that let you forward specified queries
     from a VPC to resolvers on your network.

5. Choose **Next**.
6. If you chose **Inbound and outbound** or **Inbound only**, enter the applicable values
   for configuring an inbound endpoint. Then continue with step 7. For more information, see
   [Values that you specify when you create or edit inbound endpoints](resolver-forwarding-inbound-queries-values.md "resolver-forwarding-inbound-queries-values.md").

If you choose **Outbound only**, skip to step 7. 7. Enter the applicable values for configuring an outbound endpoint. For more information, see
[Values that you specify when you create or edit
outbound endpoints](resolver-forwarding-outbound-queries-endpoint-values.md "resolver-forwarding-outbound-queries-endpoint-values.md"). 8. If you chose **Inbound and outbound** or **Outbound only**, enter the applicable values
for creating a rule. For more information, see
[Values that you specify when you create or edit rules](resolver-forwarding-outbound-queries-rule-values.md "resolver-forwarding-outbound-queries-rule-values.md"). 9. On the **Review and create** page, confirm that the settings that you specified on previous pages are correct.
If necessary, choose **Edit** for the applicable section, and update settings. When you're satisfied with the settings,
choose **Submit**.

###### Note

Creating an outbound endpoint takes a minute or two. You can't create another outbound endpoint until
the first one is created. 10. If you want to create more rules, see [Managing forwarding rules](resolver-rules-managing.md "resolver-rules-managing.md"). 11. If you created an inbound endpoint, configure DNS resolvers on your network to forward the applicable DNS queries to the
IP addresses for your inbound endpoint. For more information, refer to the documentation for your DNS application.
