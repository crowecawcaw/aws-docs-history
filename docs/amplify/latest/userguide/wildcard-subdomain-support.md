

# Setting up wildcard subdomains
<a name="wildcard-subdomain-support"></a>

Amplify Hosting now supports wildcard subdomains. A wildcard subdomain is a catch-all subdomain that enables you to point existing and non-existing subdomains to a specific branch of your application. When you use a wildcard to associate all subdomains in an app to a specific branch, you can serve the same content to your app's users in any subdomain and avoid configuring each subdomain individually.

To create a wildcard subdomain, specify an asterisk (\*) as the subdomain name. For example, if you specify the wildcard subdomain `*.example.com` for a specific branch of your app, any URL that ends with example.com will be routed to the branch. In this case, requests for `dev.example.com` and `prod.example.com` will be routed to the `*.example.com` subdomain.

Note that Amplify supports wildcard subdomains only for a custom domain. You can't use this feature with the default `amplifyapp.com` domain.

The following requirements apply to wildcard subdomains:
+ The subdomain name must be specified with an asterisk (\*) only.
+ You can't use a wildcard to replace part of a subdomain name, like this: \*domain.example.com.
+ You can't replace a subdomain in the middle of a domain name, like this: subdomain.\*.example.com.
+ By default, all Amplify provisioned certificates cover all subdomains for a custom domain.

## To add or delete a wildcard subdomain
<a name="to-add-or-edit-a-wildcard-subdomain"></a>

After adding a custom domain to an app, you can add a wildcard subdomain for an app branch.

1. Sign in to the AWS Management Console and open the [Amplify Hosting console](https://console.aws.amazon.com/amplify/).

1. Choose your app that you want to manage wildcard subdomains for.

1. In the navigation pane, choose **Hosting**, and then choose **Custom domains**.

1. On the **Custom domains** page, choose **Domain configuration**.

1. In the **Subdomains** section, you can add or delete wildcard subdomains.
   + To add a new wildcard subdomain

     1. Choose **Add new**.

     1. For the subdomain, enter an **\***.

     1. For your app branch, select a branch name from the list.

     1. Choose **Save**. 
   + To delete a wildcard subdomain

     1. Choose **Remove** next to the subdomain name. Traffic to a subdomain that is not explicitly configured stops, and Amplify Hosting returns a 404 status code to those requests.

     1. Choose **Save**.