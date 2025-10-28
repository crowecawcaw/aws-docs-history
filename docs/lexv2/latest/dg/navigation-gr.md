# Deploying Global Resiliency with your Lex V2 bot

Global Resiliency lets you replicate a bot in a secondary region. The secondary region can be made active with the automatic
replication of the user’s bot in both regions. You will have a backup region in case of a regional outage. Once Global Resiliency
is active, new bots created are replicated in a second AWS region.

## Global Resiliency information panel displays details about your deployments

You can access the following information in the Global Resiliency
panel:

- **Source details** – Information
  about your bot's source region, replica type, replication enabled date,
  and last created version. Use this information to track iterations of
  your bot.
- **Replication details** – After
  creating your bot replica, you can track the replicated region, replica
  type, last version synced date, and last replicated version. Use this
  information to track the sync of your bot replica.
- **Source region** – The region
  where Global Resiliency is enabled. You can make changes in the source
  region to replicate the bot in both regions.
- **Replica type** – Indicates
  if the bot is read only or able to read and write based on the region.
- **Replica region** – The secondary region
  that is used to replicate your source bot for Global Resiliency. Global Resiliency currently only works with IAD/PDX and LDN/FRA regional pairs.
- **Replication enabled date** –
  The date and time the bot replica was enabled.
- **Last created version** – The
  last bot version associated with the replica in the source region.

## Enabling Global Resiliency for your Lex V2 bots

Before activating Global Resiliency in the Amazon Lex V2 console, you must ensure that the user that enables bot replication has permission
to create Service Linked Roles (SLR). Global Resiliency will use these FAS credentials to create a SLR in the enabled account when CreateReplica
is invoked. For more information on setting up the SLR for Global Resiliency in Amazon Lex V2, see [AWS managed policy: AmazonLexFullAccess](security-iam-awsmanpol.md#security-iam-awsmanpol-AmazonLexFullAccess "security-iam-awsmanpol.md#security-iam-awsmanpol-AmazonLexFullAccess") .

###### Note

This feature is available only for Amazon Connect and Amazon Lex V2 instances created in the US East (N. Virginia) and US West (Oregon) Regions, and the Europe West (London) and Europe Central (Frankfurt) Regions.

To obtain access to this feature, contact your Amazon Connect Solutions Architect or Technical Account Manager.

Activate Global Resiliency and set up bot replication for a second region:

1. Sign in to the AWS Management Console and open the Amazon Lex console
   at [https://console.aws.amazon.com/lex/](https://console.aws.amazon.com/lex/ "https://console.aws.amazon.com/lex/").
2. Choose the bot you want to replicate from the Bots navigation on the
   left side navigation panel.
3. Choose Deployment > Global Resiliency.
4. Select the **Create replica** button on the upper right corner of the window
   to create a draft version of your bot.

###### Note

Check to make certain you do not have any bots in the secondary region with the same name
as the bot you want to replicate. (Your bot must be uniquely named). 5. Go to **Global Resiliency**, Click **Create Replica** -
This action creates a draft version of your bot.
(you do not need to go back to the Global Resiliency tab except to review
status or see details of future builds).

###### Note

You can also create an Alias bot for replication in Global Resiliency by going to Alias and
selecting **Create New Alias** for Global Resiliency enabled bot. All aliases will be replicated,
even if created before replication was enabled. 6. Go to **Alias** - **Create New Alias** for the Global Resiliency enabled bot.
All aliases will be replicated, even if they were created before replication was enabled. 7. Go to **Version** - **Create New Version** for the Global Resiliency enabled bot.
Any version associated with an alias will be replicated, even if it was created before replication was enabled.

###### Note

Customers still have full control of managing their resource based policies and
tags for replicated bots. Lambda functions and CloudWatch Logs Groups will need to
be deployed in both regions with the same identifiers. Users will not have to
associate the lambda function again in the replica region.

## Disabling Global Resiliency

You can disable Global Resiliency at any time by selecting the **Disable
Global Resiliency** button. This action
stops your source bot and any aliases and versions associated with it from being
replicated in other regions.

## Using APIs with Global Resiliency for your Lex V2 bots

You can make API calls in Global Resiliency using the following APIs. Additional information
about Global Resiliency APIs and Amazon Lex V2 can be found in the
[Amazon Lex V2 API Guide](api_ref.md "api_ref.md").

- **CreateBotReplica**

Enable Global Resiliency and creates a replicated bot. Requires `replicaRegion`.

For more information, see [CreateBotReplica](../APIReference/API_CreateBotReplica.md "../APIReference/API_CreateBotReplica.md") in the API Guide.

- **DeleteBotReplica**

Disable Global Resiliency and delete the replicated bot. Requires `replicaRegion` and `botId`.

For more information, see [DeleteBotReplica](../APIReference/API_DeleteBotReplica.md "../APIReference/API_DeleteBotReplica.md") in the API Guide.

- **ListBotReplicas**

List the replicated bots in the secondary zone. Requires `botId`.

For more information, see [ListBotReplicas](../APIReference/API_ListBotReplicas.md "../APIReference/API_ListBotReplicas.md") in the API Guide.

- **DescribeBotReplica**

Summary of information for the replicated bot. Requires `replicaRegion` and `botId`.

For more information, see [DescribeBotReplica](../APIReference/API_DescribeBotReplica.md "../APIReference/API_DescribeBotReplica.md") in the API Guide.
