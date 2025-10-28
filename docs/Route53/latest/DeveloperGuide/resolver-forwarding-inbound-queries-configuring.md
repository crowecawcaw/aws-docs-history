# Configuring inbound forwarding

To create an inbound endpoint, perform the following procedure.

###### To create an inbound endpoint

1. Sign in to the AWS Management Console and open the Route 53 console at
   [https://console.aws.amazon.com/route53/](https://console.aws.amazon.com/route53/ "https://console.aws.amazon.com/route53/").
2. In the navigation pane, choose **Inbound endpoints**.
3. On the navigation bar, choose the Region where you want to create an inbound endpoint.
4. Choose **Create inbound endpoint**.
5. Enter the applicable values. For more information, see
   [Values that you specify when you create or edit inbound endpoints](resolver-forwarding-inbound-queries-values.md "resolver-forwarding-inbound-queries-values.md").
6. Choose **Create**.
7. Configure DNS resolvers on your network to forward the applicable DNS queries to the IP addresses for your
   inbound endpoint. For more information, refer to the documentation for your DNS application.
