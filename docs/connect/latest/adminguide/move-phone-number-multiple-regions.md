# Move a claimed phone number to

multiple Amazon Connect instances across AWS Regions

###### Note

**New user?** Check out the [Amazon Connect Global Resiliency
Workshop](https://catalog.workshops.aws/amazon-connect-global-resiliency/en-US "https://catalog.workshops.aws/amazon-connect-global-resiliency/en-US"). This online course guides you through the process of onboarding and testing phone number
and agent failover using new APIs through the AWS CLI.

Global Resiliency is available only for Amazon Connect instances created in the following AWS Regions: US East (N. Virginia),
US West (Oregon), Asia Pacific (Osaka), Asia Pacific (Tokyo), Europe (Frankfurt), and Europe (London).

- You can only create a replica in the US East (N. Virginia) Region if your source is US West (Oregon), or the other way around.
- You can only create a replica in the Europe (Frankfurt) Region if your source
  is Europe (London), or the other way around.
- You can only create a replica in Asia Pacific (Osaka) Region if your source is Asia Pacific (Tokyo).
  To obtain access to this feature, contact your Amazon Connect Solutions Architect or Technical Account Manager.

You can move a phone number that was previously claimed to an instance, and
instead assign it to multiple instances across AWS Regions. You do
this by assigning the phone number to a traffic distribution group.

###### To assign a phone number to a traffic distribution group

1. Create a traffic distribution group using the [CreateTrafficDistributionGroup](../APIReference/API_CreateTrafficDistributionGroup.md "../APIReference/API_CreateTrafficDistributionGroup.md") API.
2. Describe your traffic distribution group using the [DescribeTrafficDistributionGroup](../APIReference/API_DescribeTrafficDistributionGroup.md "../APIReference/API_DescribeTrafficDistributionGroup.md") API to determine whether it
   has been created successfully (`Status` must be
   `ACTIVE`).
3. After your traffic distribution group is created successfully (`Status` is
   `ACTIVE`), you can assign phone numbers that were previously
   claimed to other instances or other traffic distribution groups. Use the
   [UpdatePhoneNumber](../APIReference/API_UpdatePhoneNumber.md "../APIReference/API_UpdatePhoneNumber.md") API.
