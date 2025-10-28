# Configure Amazon Route 53 alias record for your target DNS

###### Note

You don't need to follow this procedure if Amazon Route 53 is your DNS provider. In this case App Runner automatically configures your Route 53 domain with the
required certificate validation and DNS records to link to your App Runner web application.

If App Runner's automatic configuration attempt failed, follow this procedure to complete the DNS configuration. If the same domain name was
previously unlinked from a service, without the DNS provider records that point to the service being deleted afterward, App Runner is blocked from
automatically overwriting these records. This procedure explains how to manually copy them to your Route 53 DNS.

You can use Amazon Route 53 as your DNS provider to route traffic to your App Runner service. It's a highly available and scalable Domain Name System (DNS) web
service. The Amazon Route 53 record contains the settings that control how traffic is routed to your App Runner service. You create either a CNAME record or an ALIAS
record. For a comparison on CNAME and alias records, see [Choosing between alias and non-alias
records](../../../Route53/latest/DeveloperGuide/resource-record-sets-choosing-alias-non-alias.md "../../../Route53/latest/DeveloperGuide/resource-record-sets-choosing-alias-non-alias.md") , in the _Amazon Route 53 Developer Guide_.

###### Note

Amazon Route 53 currently supports alias record for services that are created after August 1, 2022.

Amazon Route 53 console

###### To configure Amazon Route 53 alias record

1. Sign in to the AWS Management Console and open the [Route 53 console](https://console.aws.amazon.com/route53/ "https://console.aws.amazon.com/route53/").
2. In the navigation pane, choose **Hosted zones**.
3. Choose the name of the hosted zone that you want to use to route traffic to your App Runner service.
4. Choose **Create record**.
5. Specify the following values:
   - **Routing policy**: Choose the applicable routing policy. For more information, see [Choosing a routing policy](../../../Route53/latest/DeveloperGuide/routing-policy.md "../../../Route53/latest/DeveloperGuide/routing-policy.md").
   - **Record name**: Enter the domain name that you want to use to route traffic to your App Runner service. The default value is
     the name of the hosted zone. For example, if the name of the hosted zone is `example.com` and you want to use
     `acme.example.com` to route traffic to your environment, enter `acme`.
   - **Value/Route traffic to**: Choose **Alias to App Runner Application**, then choose the
     **Region** that the endpoint is from. Choose the domain name of the application that you want to route traffic to.
   - **Record type**: Accept the default, **A – IPv4 address**.
   - **Evaluate target health**: Accept the default value, **Yes**.

6. Choose **Create records**.

The Route 53 alias record that you created gets propagated on all Route 53 servers within 60 seconds. When the Route 53 servers are propagated with your
alias record, you can route traffic to your App Runner service by using the name of the alias record that you created.

For information about how to troubleshoot if the DNS changes are taking too long to propagate, see [Why is it taking so long for my DNS changes to
propagate in Route 53 and public resolvers?](https://aws.amazon.com/premiumsupport/knowledge-center/route-53-propagate-dns-changes/ "https://aws.amazon.com/premiumsupport/knowledge-center/route-53-propagate-dns-changes/").

Amazon Route 53 API or AWS CLI
To configure Amazon Route 53 alias record using the Amazon Route 53 API or AWS CLI call the [ChangeResourceRecordSets](../../../Route53/latest/APIReference/API_ChangeResourceRecordSets.md "../../../Route53/latest/APIReference/API_ChangeResourceRecordSets.md") API action. To learn about the target hosted zone id of Route 53, see [Service endpoints](../../../general/latest/gr/apprunner.md "../../../general/latest/gr/apprunner.md").
