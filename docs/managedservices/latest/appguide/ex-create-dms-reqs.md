# AWS DMS, required data for setup

For each of the following AWS DMS walkthroughs, some data in common is needed.

- `Description`: Meaningful information about the resource, this is separate from other parameter `Description` options.
- `VpcId`: The VPC to use. You can find this out by running the ListVpcSummaries operation of the SKMS API
  (`list-vpc-summaries` in the CLI) or by looking on the **VPCs** page in the AMS Console. For the AMS SKMS API reference, see the **Reports** tab in the AWS Artifact Console.
- `Name`: A name for the stack or stack component; this becomes the Stack Name.
- `TimeoutInMinutes`: How many minutes are allowed for the creation of the stack before the RFC is failed. This setting will not
  delay the RFC execution, but you must give enough time (for example, don't specify `"5"`).
- `ChangeTypeId`, `ChangeTypeVersion`, and `StackTemplateId`: These are required but vary per CT and their
  values are provided in each relevant section, following.
