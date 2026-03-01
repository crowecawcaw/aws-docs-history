# Setting up automatic subdomains for an Amazon Route 53 custom domain

After an app is connected to a custom domain in Route 53, Amplify enables you to
automatically create subdomains for newly connected branches. For example, if you connect
your **dev** branch, Amplify can automatically create
**dev.exampledomain.com**. When you delete a branch, any
associated subdomains are automatically deleted.

###### To set up automatic subdomain creation for newly connected branches

1. Sign in to the AWS Management Console and open the [Amplify console](https://console.aws.amazon.com/amplify/ "https://console.aws.amazon.com/amplify/").
2. Choose an app that is connected to a custom domain managed in Route 53.
3. In the navigation pane, choose **Hosting**, and then choose
   **Custom domains**.
4. On the **Custom domains** page, choose **Domain
   configuration**.
5. In the **Automatic subdomain creation** section, turn on the
   feature.

###### Note

This feature is available only for root domains, for example, **exampledomain.com**. The Amplify console doesn't display this check box
if your domain is already a subdomain, such as **dev.exampledomain.com**.

## Web previews with subdomains

After you enable **Automatic subdomain creation** using the
preceding instructions, your app’s pull request web previews will also be accessible
with automatically created subdomains. When a pull request is closed, the associated
branch and subdomain are automatically deleted. For more information on setting up web
previews for pull requests, see [Web previews for pull requests](pr-previews.md "pr-previews.md").
