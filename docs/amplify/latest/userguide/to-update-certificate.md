# Updating the SSL/TLS certificate for a domain

You can change the SSL/TLS certificate that is in use for a domain at any time. For
example, you can change from using a managed certificate to using a custom certificate.
This is helpful if you want to manage the certificate and its expiration notifications. You
can also change the custom certificate that is in use for the domain. Making changes to the
SSL certificate won't incur any downtime for your active domain. For more information about
certificates, see [Using SSL/TLS
certificates](using-certificates.md "using-certificates.md").

Use the following procedure to update the type of certificate or the custom certificate
that is in use for a domain.

###### To update a domain's certificate

1. Sign in to the AWS Management Console and open the [Amplify console](https://console.aws.amazon.com/amplify/ "https://console.aws.amazon.com/amplify/").
2. Choose your app that you want to update.
3. In the navigation pane, choose **Hosting**, **Custom
   domains**.
4. On the **Custom domains** page, choose **Domain
   configuration**.
5. On the details page for your
   domain, locate the **Custom SSL certificate** section. The procedure
   for updating your certificate varies depending on the type of change you want to
   make.
   - To change from a custom certificate to the default Amplify managed
     certificate
     1. Choose **Amplify managed certificate**.

   - To change from a managed certificate to a custom certificate
     1. Choose **Custom SSL certificate**.
     2. Select the certificate to use from the list.

   - To change a custom certificate to a different custom certificate
     1. For **Custom SSL certificate**, select the new
        certificate to use from the list.

6. Choose **Save**. The status details for the domain will indicate
   that Amplify has initiated the SSL creation process for a managed certificate or
   the configuration process for a custom certificate.
