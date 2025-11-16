# Getting started with Route 53 Resolver on

AWS Outposts

After you have ordered your AWS Outposts racks and they have been delivered, as described
here: [Create an AWS Outposts](../../../outposts/latest/userguide/order-outpost-capacity.md "../../../outposts/latest/userguide/order-outpost-capacity.md")
in the _AWS Outposts guide_, you can set up Resolver on Outpost.

###### Important

Resolver on Outpost can only be created by the AWS account that owns the AWS Outposts rack. If the
AWS Outposts rack is shared with other accounts, those accounts cannot create Resolver on Outpost on
the shared rack.

You can also use APIs to manage Route 53 on Outposts. For more information, see [Resolver on Outpost actions](../APIReference/API-actions-by-function.md#actions-by-function-outpost-resolver "../APIReference/API-actions-by-function.md#actions-by-function-outpost-resolver").

###### Important

It can take up to 30-150 minutes to create a Resolver cache on an AWS Outposts.

After you have your AWS Outposts racks delivered, you can opt in to Route 53 on Outposts.

###### To configure Resolver on Outpost

1. Sign in to the AWS Management Console and open the Route 53 console at
   [https://console.aws.amazon.com/route53/](https://console.aws.amazon.com/route53/ "https://console.aws.amazon.com/route53/").
2. In the left navigation pane, expand **Resolver**, and then
   navigate to **Outposts**.
3. On the navigation bar, choose the Region where your AWS Outposts is located.
4. On the **Resolver on Outpost** page, choose **Create
   Resolver**.
5. On the **Create Resolver** page:
   - Under **AWS Outposts** select an AWS Outposts you want to create
     the Resolver on.
   - Type in a name for the Resolver in the **Resolver name**
     text box.
   - After the **Recommended instance types for Resolver**
     populates with Amazon EC2 instances, choose one.

   For more information about the instance types, see [Quotas on
   Resolver on Outpost](DNSLimitations.md#limits-api-entities-resolver-on-outposts "DNSLimitations.md#limits-api-entities-resolver-on-outposts").
   - For **Number of instances**, choose the number of
     elastic interface instances for the VPC Resolver. The default value is
   4.

   If your AWS Outposts doesn't have an instance type that supports Resolver, you
   won't be able to create a Resolver.

6. Choose **Create Resolver**.

You can monitor the Resolver creation on the **Resolver on Outpost**
page.
