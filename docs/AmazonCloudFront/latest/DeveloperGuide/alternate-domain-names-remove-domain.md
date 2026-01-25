# Remove an alternate domain name

If you want to stop routing traffic for a domain or subdomain to a CloudFront distribution, follow the
steps in this section to update both the DNS configuration and the CloudFront distribution.

It’s important that you remove the alternate domain names from the distribution as well as update your DNS
configuration. This helps prevent issues later if you want to associate the domain name with another CloudFront distribution.
If an alternate domain name is already associated with one distribution, it can’t be set up with another.

###### Note

If you want to remove the alternate domain name from this distribution so you can add it to another one,
follow the steps in [Move an alternate domain name](alternate-domain-names-move.md "alternate-domain-names-move.md"). If you
follow the steps here instead (to remove a domain) and then add the domain to another distribution, there will be a
period of time during which the domain won’t link to the new distribution because CloudFront is propagating to the
updates to edge locations.

###### To remove an alternate domain name from a distribution

1. To start, route internet traffic for your domain to another resource that isn’t your CloudFront distribution,
   such as an Elastic Load Balancing load balancer. Or you can delete the DNS record that’s routing traffic to CloudFront.

Do one of the following, depending on the DNS service for your domain:

    * **If you’re using Route 53**, update or delete alias records or
     CNAME records. For more information, see [Editing records](../../../Route53/latest/DeveloperGuide/resource-record-sets-editing.md "../../../Route53/latest/DeveloperGuide/resource-record-sets-editing.md") or [Deleting records](../../../Route53/latest/DeveloperGuide/resource-record-sets-deleting.md "../../../Route53/latest/DeveloperGuide/resource-record-sets-deleting.md").
    * **If you’re using another DNS service provider**, use the method
     provided by the DNS service provider to update or delete the CNAME
     record that directs traffic to CloudFront. For more information, see the
     documentation provided by your DNS service provider.

2. After you update your domain’s DNS records, wait until the changes have propagated and DNS
   resolvers are routing traffic to the new resource. You can check to see when
   this is complete by creating some test links that use your domain in the
   URL.
3. Sign in to the AWS Management Console and open the CloudFront console at [https://console.aws.amazon.com/cloudfront/v4/home](https://console.aws.amazon.com/cloudfront/v4/home "https://console.aws.amazon.com/cloudfront/v4/home"), and update your CloudFront distribution
   to remove the domain name by doing the following:
   1. Choose the ID for the distribution that you want to update.
   2. On the **General** tab, choose **Edit**.
   3. In **Alternate Domain Names (CNAMEs)**, remove the alternate
      domain name (or domain names) that you no longer want to use for your distribution.
   4. Choose **Yes, Edit**.
