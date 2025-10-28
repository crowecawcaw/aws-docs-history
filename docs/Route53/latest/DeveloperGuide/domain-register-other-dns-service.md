# Updating name servers to use another

registrar

If you want to move DNS management to another registrar, you need to update the name
servers to point to

###### To update the name

servers for your domain when you want to use another DNS service

1. Use the process that is provided by your DNS service to get the name servers
   for the domain.
2. Sign in to the AWS Management Console and open the Route 53 console at
   [https://console.aws.amazon.com/route53/](https://console.aws.amazon.com/route53/ "https://console.aws.amazon.com/route53/").
3. In the navigation pane, choose **Registered domains**.
4. Choose the name of the domain that you want to configure to use another DNS
   service.
5. In the **Details** section, under the
   **Actions** drop-down, choose **Edit name
   servers**.
6. Delete the existing name servers, and then add the names of the name servers
   to the name servers that you got from your DNS service in step 1.
7. Choose **Save changes**.
8. (Optional) Delete the hosted zone that Route 53 created automatically when you
   registered your domain. This prevents you from being charged for a hosted zone
   that you aren't using.
   1. In the navigation pane, choose **Hosted
      Zones**.
   2. Select the radio button for the hosted zone that has the same name as
      your domain.
   3. Choose **Delete Hosted Zone**.
   4. Choose **Confirm** to confirm that you want to delete
      the hosted zone.
