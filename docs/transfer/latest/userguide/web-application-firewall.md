# Add a web application firewall

AWS WAF is a web application firewall that helps protect web applications and APIs from
attacks. You can use it to configure a set of rules known as a _web
access control list_ (web ACL) that allow, block, or count web requests based
on customizable web security rules and conditions that you define. For more information, see
[Using
AWS WAF to protect your APIs](../../../apigateway/latest/developerguide/apigateway-control-access-aws-waf.md "../../../apigateway/latest/developerguide/apigateway-control-access-aws-waf.md").

###### To add AWS WAF

1. Open the API Gateway console at [https://console.aws.amazon.com/apigateway/](https://console.aws.amazon.com/apigateway/ "https://console.aws.amazon.com/apigateway/").
2. In the **APIs** navigation pane, and then choose your
   custom identity provider template.
3. Choose **Stages**.
4. In the **Stages** pane, choose the name of the
   stage.
5. In the **Stage Editor** pane, choose the
   **Settings** tab.
6. Do one of the following:
   - Under **Web Application Firewall (WAF)**, for
     **Web ACL**, choose the web ACL that you want
     to associate with this stage.
   - If the web ACL you need doesn't exist, you will need to create one
     by doing the following:
     1. Choose **Create Web ACL**.
     2. On the AWS WAF service homepage, choose **Create
        web ACL**.
     3. In **Web ACL details**, for
        **Name**, type the name of the web
        ACL.
     4. In **Rules**, choose **Add
        rules**, then choose **Add my own rules
        and rule groups**.
     5. For **Rule type**, choose IP set to
        identify a specific list of IP addresses.
     6. For **Rule**, enter the name of the
        rule.
     7. For **IP set**, choose an existing IP
        set. To create an IP set, see [Creating an IP set](../../../waf/latest/developerguide/waf-ip-set-creating.md "../../../waf/latest/developerguide/waf-ip-set-creating.md").
     8. For **IP address to use as the originating
        address**, choose **IP address in
        header**.
     9. For **Header field name**, enter
        `SourceIP`.
     10. For **Position inside header**, choose
         **First IP address**.
     11. For **Fallback for missing IP address**,
         choose **Match** or **No
         Match** depending on how you want to handle an
         invalid (or missing) IP address in the header.
     12. For **Action**, choose the action of the
         IP set.
     13. For **Default web ACL action for requests that
         don't match any rules**, choose
         **Allow** or **Block**
         and then click **Next**.
     14. For steps 4 and 5, choose
         **Next**.
     15. In **Review and create**, review your
         choices, and then choose **Create web
         ACL**.

7. Choose **Save Changes**.
8. Choose **Resources**.
9. For **Actions**, choose **Deploy
   API**.

For information on how secure Transfer Family with AWS web application firewall, see
[Securing Transfer Family with AWS application firewall and Amazon API Gateway](https://aws.amazon.com/blogs/storage/securing-aws-transfer-family-with-aws-web-application-firewall-and-amazon-api-gateway/ "https://aws.amazon.com/blogs/storage/securing-aws-transfer-family-with-aws-web-application-firewall-and-amazon-api-gateway/")
in the AWS storage blog.
