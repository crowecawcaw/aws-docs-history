

# Getting started with VPC Resolver on AWS Outposts
<a name="outpost-resolver-getting-started"></a>

After you have ordered your AWS Outposts racks and they have been delivered, as described here: [Create an AWS Outposts](https://docs.aws.amazon.com/outposts/latest/userguide/order-outpost-capacity.html) in the *AWS Outposts guide*, you can set up Resolver on Outpost.

**Important**  
Resolver on Outpost can only be created by the AWS account that owns the AWS Outposts rack. If the AWS Outposts rack is shared with other accounts, those accounts cannot create Resolver on Outpost on the shared rack.

You can also use APIs to manage Route 53 on Outposts. For more information, see [Resolver on Outpost actions](https://docs.aws.amazon.com/Route53/latest/APIReference/API-actions-by-function.html#actions-by-function-outpost-resolver).

**Important**  
It can take up to 30-150 minutes to create a VPC Resolver cache on an AWS Outposts.

After you have your AWS Outposts racks delivered, you can opt in to Route 53 on Outposts.

**To configure Resolver on Outpost**

1. Sign in to the AWS Management Console and open the Route 53 console at [https://console.aws.amazon.com/route53/](https://console.aws.amazon.com/route53/).

1. In the left navigation pane, expand **Resolver**, and then navigate to **Outposts**.

1. On the navigation bar, choose the Region where your AWS Outposts is located.

1. On the **Resolver on Outpost** page, choose **Create VPC Resolver**.

1. On the **Create VPC Resolver** page:
   + Under **AWS Outposts** select an AWS Outposts you want to create the VPC Resolver on.
   + Type in a name for the VPC Resolver in the **VPC Resolver name** text box.
   + After the **Recommended instance types for VPC Resolver** populates with Amazon EC2 instances, choose one.

     For more information about the instance types, see [Quotas on Resolver on Outpost](DNSLimitations.md#limits-api-entities-resolver-on-outposts). 
   + For **Number of instances**, choose the number of elastic interface instances for the VPC VPC Resolver. The default value is 4.

     If your AWS Outposts doesn't have an instance type that supports VPC Resolver, you won't be able to create a VPC Resolver.

1. Choose **Create VPC Resolver**.

   You can monitor the VPC Resolver creation on the **Resolver on Outpost** page.