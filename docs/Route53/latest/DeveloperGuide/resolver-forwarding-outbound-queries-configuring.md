

# Configuring outbound forwarding
<a name="resolver-forwarding-outbound-queries-configuring"></a>

To configure VPC Resolver to forward DNS queries that originate in your VPC to your network, perform the following procedures.

**Important**  
After you create an outbound endpoint, you must create one or more rules and associate them with one or more VPCs. Rules specify the domain names of the DNS queries that you want to forward to your network.<a name="resolver-forwarding-outbound-queries-configuring-create-endpoint-procedure"></a>

**To create an outbound endpoint**

1. Sign in to the AWS Management Console and open the Route 53 console at [https://console.aws.amazon.com/route53/](https://console.aws.amazon.com/route53/).

1. In the navigation pane, choose **Outbound endpoints**.

1. On the navigation bar, choose the Region where you want to create an outbound endpoint.

1. Choose **Create outbound endpoint**.

1. Enter the applicable values. For more information, see [Values that you specify when you create or edit outbound endpoints](resolver-forwarding-outbound-queries-endpoint-values.md).

1. Choose **Create**.
**Note**  
Creating an outbound endpoint takes a minute or two. You can't create another outbound endpoint until the first one is created.

1. Create one or more rules to specify the domain names of the DNS queries that you want to forward to your network. For more information, see the next procedure.

To create one or more forwarding rules, perform the following procedure.<a name="resolver-forwarding-outbound-queries-configuring-create-rule-procedure"></a>

**To create forwarding rules and associate the rules with one or more VPCs**

1. Sign in to the AWS Management Console and open the Route 53 console at [https://console.aws.amazon.com/route53/](https://console.aws.amazon.com/route53/).

1. In the navigation pane, choose **Rules**.

1. On the navigation bar, choose the Region where you want to create the rule.

1. Choose **Create rule**.

1. Enter the applicable values. For more information, see [Values that you specify when you create or edit rules](resolver-forwarding-outbound-queries-rule-values.md).

1. Choose **Save**.

1. To add another rule, repeat steps 4 through 6. 