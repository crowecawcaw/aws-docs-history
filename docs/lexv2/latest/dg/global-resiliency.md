# Use Global Resiliency to deploy bots to other Regions

Global Resiliency lets you replicate a bot in a secondary region. The secondary
region can be made active with the automatic replication of the user’s bot in both
regions. You will have a backup region in case of a regional outage. Once Global Resiliency
is active, new bots created are replicated in a second AWS region.

###### Note

This feature is available only for Amazon Connect and Amazon Lex V2 instances created in the US East (N. Virginia)
and US West (Oregon) Regions, and the Europe West (London) and Europe Central (Frankfurt) Regions.

To obtain access to this feature, contact your Amazon Connect Solutions Architect or Technical Account Manager.

After activating this feature, you can automate the replication of Amazon Lex V2 bots and
their resources, versions, and aliases across a paired AWS region in near real-time.
With this feature, you can monitor the version number of the original and replica bot
to ensure that the bot replica remains in sync with the original bot. When you enable
replication, you can activate the pre-determined AWS region you want the bot to be replicated in
(regions are based on pre-determined pairs). Any updates to the source bot in the
source region is automatically updated to the replicated bot in the second region.

###### Note

When Global Resiliency is enabled for a bot, all existing aliases and their associated
versions get replicated in the replica region. Versions which are not associated to an alias before
enabling replication are replicated when they get associated to an alias. Every version and alias
created after enabling replication, is automatically replicated. Users can use `ListBotVersionReplicas`
and `ListBotAliasReplicas` to review the status of replication of each individual version and alias.
Bot mutations are uni-directional from bot to its replica. Users cannot modify the replica bot because
it is always kept in sync with the bot.

Additional information about using Global Resiliency:

- Global Resiliency currently only works with pre-determined pairs of regions.

|           |              |
| --------- | ------------ |
| us-east-1 | us-west-2    |
| eu-west-2 | eu-central-1 |

- When Global Resiliency is enabled for a bot, all existing aliases and their associated versions get replicated in the replica region. Versions
  which are not associated to an alias before enabling replication, are replicated when they are associated to an alias. Every version and alias created after
  enabling replication, gets automatically replicated. Users can use `ListBotVersionReplicas` and `ListBotAliasReplicas` to know the status of replication for each
  individual version and alias. Bot mutations are uni-directional from bot to its replica. Users cannot modify the replica bot, because it is always kept in sync with the bot.
- Any Alias can be associated with any version. If the version is not replicated already, it will be replicated during the association with the Alias.
  Limitations:

- Global Resiliency does not replicate bots created with slots that use LLM such as CFAQ and Utterance Generation.
- Global Resiliency does not replicate a Network of Bots, but any bot that is part of the Network of Bots can still be individually replicated.

###### Topics

- [Permissions to replicate bots and manage bot replicas in Lex V2](gr-permissions.md "gr-permissions.md")
- [Deploying Global Resiliency with your Lex V2 bot](navigation-gr.md "navigation-gr.md")
