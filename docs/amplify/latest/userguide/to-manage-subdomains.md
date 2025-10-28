# Managing subdomains

A subdomain is the part of your URL that appears before your domain name. For example,
**www** is the subdomain of **www.amazon.com** and **aws** is the subdomain of
**aws.amazon.com**. If you already have a production
website, you might want to only connect a subdomain. Subdomains can also be multilevel, for
example **beta.alpha.example.com** has the multilevel
subdomain **beta.alpha**.

## To add a subdomain only

1. Sign in to the AWS Management Console and open the [Amplify console](https://console.aws.amazon.com/amplify/ "https://console.aws.amazon.com/amplify/").
2. Choose your app that you want to add a subdomain to.
3. In the navigation pane, choose **Hosting**, and then choose
   **Custom domains**.
4. On the **Custom domains** page, choose **Add
   domain**.
5. Enter the name of your root domain and then choose **Configure
   domain**. For example, if the name of your domain is **https://example.com**, enter **example.com**.
6. Choose **Exclude root** and modify the name of the subdomain.
   For example if the domain is **example.com** you can
   modify it to only add the subdomain **alpha**.
7. Choose **Add domain**.

## To add a multilevel subdomain

1. Sign in to the AWS Management Console and open the [Amplify console](https://console.aws.amazon.com/amplify/ "https://console.aws.amazon.com/amplify/").
2. Choose your app that you want to add a multilevel subdomain to.
3. In the navigation pane, choose **Hosting**, and then choose
   **Custom domains**.
4. On the **Custom domains** page, choose **Add
   domain**.
5. Enter the name of a domain with a subdomain, choose **Exclude
   root**, and modify the subdomain to add a new level.

For example, if you have a domain called **alpha.example.com** and you want to create a multilevel subdomain
**beta.alpha.example.com**, you would enter
**beta** as the subdomain value. 6. Choose **Add domain**.

## To add or edit a subdomain

After adding a custom domain to an app, you can edit an existing subdomain or add a
new subdomain.

1. Sign in to the AWS Management Console and open the [Amplify console](https://console.aws.amazon.com/amplify/ "https://console.aws.amazon.com/amplify/").
2. Choose your app that you want to manage subdomains for.
3. In the navigation pane, choose **Hosting**, and then choose
   **Custom domains**.
4. On the **Custom domains** page, choose **Domain
   configuration**.
5. In the **Subdomains** section, you can edit your existing
   subdomains as needed.
6. (Optional) To add a new subdomain, choose **Add new**.
7. Choose **Save**.
