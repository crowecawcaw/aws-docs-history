# Disable AWS WAF security protections

If your distribution doesn't need AWS WAF security protections, you can disable this
feature by using the CloudFront console.

If you previously enabled AWS WAF protection and didn't choose an existing WAF configuration
(also known as one-click protection), CloudFront automatically created a web ACL for you. For web ACLs
created this way, the CloudFront console will disassociate the resource and delete the web ACL.

Disassociating a web ACL is different from deleting it. Disassociating removes the web ACL
from your distribution, but it's not deleted from your AWS account. For more information, see
[Associating or
disassociating a web ACL with an AWS resource](../../../waf/latest/developerguide/web-acl-associating-aws-resource.md "../../../waf/latest/developerguide/web-acl-associating-aws-resource.md") in the _AWS WAF, AWS Firewall Manager, and
AWS Shield Advanced Developer Guide_.

See the following procedure to disable AWS WAF protections and disassociate the web ACL from
your distribution.

###### To disable AWS WAF security protections in CloudFront

1. Open the CloudFront console at [https://console.aws.amazon.com/cloudfront/v4/home](https://console.aws.amazon.com/cloudfront/v4/home "https://console.aws.amazon.com/cloudfront/v4/home").
2. In the navigation pane, choose **Distributions**, and then choose the
   distribution that you want to change.
3. Choose the **Security** tab and then choose
   **Edit**.
4. In the **Web Application Firewall (WAF)** section, choose
   **Disable AWS WAF protection**.
5. Choose **Save changes**.

###### Notes

- If you disabled AWS WAF security protection and you still want to delete the web ACL from
  your AWS account, you can delete it manually. Follow the procedure to [delete a web
  ACL](../../../waf/latest/developerguide/web-acl-deleting.md "../../../waf/latest/developerguide/web-acl-deleting.md"). In the AWS WAF & Shield console, for the **Web ACLs** page,
  you _must_ choose the **Global (CloudFront)** list to find the
  web ACLs.
- When you delete a distribution from the CloudFront console, CloudFront will attempt to also delete
  the web ACL if you chose one-click protection. This is best effort and isn't always
  guaranteed. For more information, see [Delete a distribution](HowToDeleteDistribution.md "HowToDeleteDistribution.md").
