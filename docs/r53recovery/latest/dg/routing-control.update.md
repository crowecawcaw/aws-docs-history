#

Getting and updating routing control states in the AWS Management Console

You can get and update routing control states in the AWS Management Console. Be aware, though, that you can't
choose different Regional cluster endpoints in the console. That is, there isn't a process
for choosing and rotating through cluster endpoints in the console as you can do by using the Amazon Application Recovery Controller (ARC) API.
In addition, the console is not highly available while the ARC data plane offers extreme reliability. For
these reasons, we recommend that you use the ARC API to get and update routing control states for production operations.

For more recommendations about using ARC for failover, see [Best practices for routing control in ARC](route53-arc-best-practices.md "route53-arc-best-practices.md").

To view and update routing controls in the console, follow the steps in the following procedures.

# To get routing control states

1. Open the ARC console at [https://console.aws.amazon.com/route53recovery/home#/dashboard](https://console.aws.amazon.com/route53recovery/home#/dashboard "https://console.aws.amazon.com/route53recovery/home#/dashboard").
2. Choose **Routing control**.
3. From the list, choose a control panel and view the routing controls.

# To update one or multiple routing control states

1. Open the Amazon Route 53 console at [https://console.aws.amazon.com/route53/home](https://console.aws.amazon.com/route53/home "https://console.aws.amazon.com/route53/home").
2. Under **Application Recovery Controller**, choose **Routing control**.
3. Choose **Action**, and then choose **Change traffic routing**.
4. Update the states of one or more routing controls to be `Off` or `On`, depending on where you want
   traffic to flow or stop flowing for your application.
5. Enter `confirm` in the text box.
6. Choose **Update traffic routing**.
