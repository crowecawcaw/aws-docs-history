# Enable bot building and analytics in Connect Customer

Complete the following steps to enable users to create Amazon Lex bots in the Connect Customer admin website and view metrics
about bot performance.

Users can not edit LEX V1 bots or cross-regional bots from within Connect Customer.

1. Open the [Connect Customer
   console.](https://console.aws.amazon.com/connect/ "https://console.aws.amazon.com/connect/")
2. Select the Connect Customer instance that you want to integrate with your Amazon Lex bot.

![The Connect Customer virtual contact center instances page, the instance alias.](images/instance.png) 3. On the navigation menu, choose **Flows**. 4. Choose **Enable Lex Bot Management in Connect Customer** and **Enable Bot
Analytics and Transcripts in Connect Customer**, and then
**Save**.

![The Amazon Lex bots page, the options to enable Lex bot management and analytics Connect Customer.](images/lex-bot-service-linked-role.png)

###### Note

If you already have existing Service Control Policies (SCP) in place that block
access to Lex, Connect Customer respects those policies and does not enable the Bot Management
and Analytics feature. However, if you put those SCP policies in place after you've
already enabled this feature, they won't be respected. In that case, you'll need to
disable this feature.

Connect Customer displays the service role and service linked role name it uses. uses Amazon Lex
resource-based policies to make calls to your Amazon Lex bot. When you associate an Amazon Lex bot
with your Connect Customer instance, the resource-based policy on the bot is updated to give Connect Customer
permission to invoke the bot.

For more information about Amazon Lex resource-based policies, see [Resource-based policies within Amazon Lex V2](../../../lexv2/latest/dg/security_iam_service-with-iam.md#security_iam_service-with-iam-resource-based-policies "../../../lexv2/latest/dg/security_iam_service-with-iam.md#security_iam_service-with-iam-resource-based-policies") in the _Amazon Lex V2 Developer
Guide_. 5. Assign the following security profile permissions to users who need to create and manage
bots and bot analytics:

    * **Channels and Flows** - **Bots** -
     **View**, **Edit**,
     **Create** permissions
    * **Analytics and Optimization** - **Historical
     metrics** - **Access** permission
