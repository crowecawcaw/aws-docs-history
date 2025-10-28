AWS Resource Explorer now provides immediate access to resource search and
discovery capabilities in a Region. With this launch, you no longer need to activate
Resource Explorer to discover your resources. [Learn more](manage-immediate-resource-discovery-experience.md "manage-immediate-resource-discovery-experience.md")

# Considerations for AWS opt-in

Regions

Opt-in Regions have higher security requirements than commercial Regions as it
pertains to sharing IAM data through accounts in opt-in Regions. All of the data
managed through the IAM service is considered identity data.

You can activate opt-in Regions using the [AWS Resource Explorer console](https://console.aws.amazon.com/resource-explorer "https://console.aws.amazon.com/resource-explorer"). See [Completing setup for Resource Explorer in an
AWS Region to index your resources](manage-service-turn-on-region.md "manage-service-turn-on-region.md") for more information.

## Opt-out behaviors

Consider the following behaviors before you opt-out of an opt-in Region:

###### Important

Before you opt-out of a Region with an aggregator index, we suggest that you
delete the aggregator index or demote it to a local index. Resource Explorer supports one
aggregator index across all Regions within the partition.

- Your index isn't deleted, it's only disabled. If you choose to opt-in
  again later, your settings will revert.
- IAM disables IAM access to resources in the Region.
- Resource Explorer disables the index for the opted-out Region and stops ingesting
  data. The `ListIndexes` API won't show the Region index
  anymore.
- If your aggregator index is in a different Region, Resource Explorer stops data
  replication from the opted-out Region and cleans up the data within 24
  hours.
- If you opt-out of your aggregator index Region, you will have to opt-in
  again to delete or demote the index.
- If you opt-in to the Region again, Resource Explorer re-enables the index and starts
  to ingest data.
- Any changes to the status of an opt-in Region takes about 24 hours to go
  into effect.
