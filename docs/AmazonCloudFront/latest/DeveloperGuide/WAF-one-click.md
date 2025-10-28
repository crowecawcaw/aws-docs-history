# Enable AWS WAF for distributions

You can enable AWS WAF when you create a distribution, or you can enable security protections for an existing access control list (ACL).

If you enable AWS WAF for your CloudFront distribution, you can also enable bot control and configure security protection by bot category.

###### Topics

- [Enable AWS WAF for a new distribution](#enable-waf-new-distribution "#enable-waf-new-distribution")
- [Use an existing web ACL](#acl-new-configuration "#acl-new-configuration")
- [Enable bot control](#bot-traffic "#bot-traffic")
- [Configure protection by bot category](#configure-bot-category-protection "#configure-bot-category-protection")

## Enable AWS WAF for a new distribution

The following procedure shows you how to enable AWS WAF when you create a new CloudFront distribution.

###### To enable AWS WAF for a new distribution

1. Open the CloudFront console at [https://console.aws.amazon.com/cloudfront/v4/home](https://console.aws.amazon.com/cloudfront/v4/home "https://console.aws.amazon.com/cloudfront/v4/home").
2. In the navigation pane, choose **Distributions**, and then choose
   **Create distribution**.
3. As needed, follow the steps in [Create a distribution](distribution-web-creating-console.md "distribution-web-creating-console.md").
4. In the **Web Application Firewall** section, choose
   **Edit**, then choose **Enable security protections**.
5. Complete the following fields:
   - **Use monitor mode** – You enable monitor mode when you want to
     first collect data to test how protection will work. When you enable monitor mode, requests
     aren't blocked if the protections were active. Instead, monitor mode collects data about
     requests that would be blocked if the protections were active. When you're ready to begin
     blocking, you can enable blocking on the **Security** page.
   - **Additional protections** – Choose any options that you want to
     enable. If you enable rate limiting, see [Set up rate limiting](WAF-one-click-rate-limiting.md "WAF-one-click-rate-limiting.md") for
     more information.
   - **Price estimate** – You can open the section to display a field
     where you enter a different number of requests/month and see a new estimate.

6. Review the remaining distribution settings, then choose **Create
   distribution**.

After you create a distribution, CloudFront creates a **Security** dashboard. You
can use this dashboard to disable or enable AWS WAF. If you haven't enabled AWS WAF yet, the charts
and graphs in the dashboard remain blank.

## Use an existing web ACL

If you have an existing web ACL, you can use it instead of the protection offered by AWS WAF.

###### To use an existing AWS WAF configuration

1. Open the CloudFront console at [https://console.aws.amazon.com/cloudfront/v4/home](https://console.aws.amazon.com/cloudfront/v4/home "https://console.aws.amazon.com/cloudfront/v4/home").
2. Do one of the following:
   1. Choose **Create distribution** and follow the steps in [Create a distribution](distribution-web-creating-console.md "distribution-web-creating-console.md"), then return to this topic.
   2. Choose an existing configuration, and then choose the **Security**
      tab.

3. In the **Web Application Firewall (WAF)** section, choose
   **Edit**, then **Enable security protections**.
4. Choose **Use existing WAF configuration**. This option appears only if
   you have web ACLs configured.
5. Choose your existing web ACL from the **Choose a web ACL** table.
6. Review the remaining distribution settings, and then choose **Create
   distribution**.

## Enable bot control

If you enable AWS WAF for your CloudFront distribution, you can view bot requests for a given time range under the security dashboard in the CloudFront console. You can also enable or disable bot control here.

You incur charges when you enable bot control. The security dashboard provides a cost estimate.

If you enable bot control, the security dashboard displays bot traffic by each bot type and category. If you disable bot control,
bot traffic is displayed based on request sampling.

###### To enable bot control

1. Open the CloudFront console at [https://console.aws.amazon.com/cloudfront/v4/home](https://console.aws.amazon.com/cloudfront/v4/home "https://console.aws.amazon.com/cloudfront/v4/home").
2. In the navigation pane, choose **Distributions**, then choose the distribution that you want to change.
3. Choose the **Security** tab.
4. Scroll down to the **Bot requests for a given time range** section and choose **Enable Bot Control**.
5. In the **Bot Control** dialog box, under **Configuration**, select the
   **Enable Bot Control for common bots** check box.
6. Choose **Save changes**.

## Configure protection by bot category

When you enable bot control, you can configure how each unverified bot is handled per bot category. For example, you can set an
HTTP library bot to **Monitor mode** and assign a **Challenge** to a link checker.

###### Note

Bots that are known by AWS to be common and verifiable, such as known search engine
crawlers, aren't subject to the actions you set here. Bot
control
confirms that validated bots come from the source that they claim before marking them as
verified.

###### To configure protection for a bot category

1. Open the CloudFront console at [https://console.aws.amazon.com/cloudfront/v4/home](https://console.aws.amazon.com/cloudfront/v4/home "https://console.aws.amazon.com/cloudfront/v4/home").
2. In the navigation pane, choose **Distributions**, then choose the distribution that you want to change.
3. Choose the **Security** tab.
4. In the **Requests by bot category** chart, point to any of the items in the **Unverified bot action** column and
   choose the pencil icon to edit it.
5. Open the resulting list and choose one of the following:
   - **Block**
   - **Allow**
   - **Monitor mode**
   - **CAPTCHA**
   - **Challenge**

6. Select the check mark next to the list to save your change.
