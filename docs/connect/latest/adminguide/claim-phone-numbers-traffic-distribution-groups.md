# Claim phone

numbers to traffic distribution groups using Amazon Connect

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

After your traffic distribution group is created successfully (`Status` is
`ACTIVE`), you can use [SearchAvailablePhoneNumbers](../APIReference/API_SearchAvailablePhoneNumbers.md "../APIReference/API_SearchAvailablePhoneNumbers.md") to search for available phone numbers and
[ClaimPhoneNumber](../APIReference/API_ClaimPhoneNumber.md "../APIReference/API_ClaimPhoneNumber.md") to claim them.

Before you claim a phone number to your traffic distribution group, we recommend using the [DescribeTrafficDistributionGroup](../APIReference/API_DescribeTrafficDistributionGroup.md "../APIReference/API_DescribeTrafficDistributionGroup.md") API to verify the status of the traffic distribution group
is `ACTIVE`. Assigning a phone number to a traffic distribution group
that isn't `ACTIVE` results in `ResourceNotFoundException`.

You can claim a phone number to a traffic distribution group by providing the
traffic distribution group ARN in the **TargetArn** parameter when
calling the [ClaimPhoneNumber](../APIReference/API_ClaimPhoneNumber.md "../APIReference/API_ClaimPhoneNumber.md") API. You can also use the [UpdatePhoneNumber](../APIReference/API_UpdatePhoneNumber.md "../APIReference/API_UpdatePhoneNumber.md") API to assign a phone number previously claimed to an
instance to a traffic distribution group.

###### Note

To update the **Description** field, you must use the Amazon Connect
console.

## Example workflow

Following is an example workflow to claim phone numbers and use them across
multiple AWS Regions:

1. Create a replica of your instance:
   1. Call the [ReplicateInstance](../APIReference/API_ReplicateInstance.md "../APIReference/API_ReplicateInstance.md") API.

2. Create a traffic distribution group that links these instances
   together:
   1. Call the [CreateTrafficDistributionGroup](../APIReference/API_CreateTrafficDistributionGroup.md "../APIReference/API_CreateTrafficDistributionGroup.md") API.

3. Find available phone numbers that can be claimed to your traffic
   distribution group:
   1. Call the [SearchAvailablePhoneNumbers](../APIReference/API_SearchAvailablePhoneNumbers.md "../APIReference/API_SearchAvailablePhoneNumbers.md") API in the Region where
      the traffic distribution group was created. Provide the traffic
      distribution group ARN for the `TargetArn`
      parameter.

4. In the Region where the traffic distribution group was created, call
   the [ClaimPhoneNumber](../APIReference/API_ClaimPhoneNumber.md "../APIReference/API_ClaimPhoneNumber.md") API:
   1. Provide your traffic distribution group ARN for the
      `TargetArn` parameter.
   2. Provide the E164 phone number value that was returned by the
      [SearchAvailablePhoneNumbers](../APIReference/API_SearchAvailablePhoneNumbers.md "../APIReference/API_SearchAvailablePhoneNumbers.md") API call in step
      3.A `PhoneNumberId` and `PhoneNumberArn` are
      returned. You can use these values for follow-up operations.

5. Verify that the phone number status is `CLAIMED`:
   1. Call the [DescribePhoneNumber](../APIReference/API_DescribePhoneNumber.md "../APIReference/API_DescribePhoneNumber.md") API.

   (DescribePhoneNumber can also be called in the other Region
   associated with the traffic distribution group. It will return
   the same phone number details.)The phone number can be used by follow-up operations only after its
   status is `CLAIMED`.

For a description of possible statuses, see [Phone number statuses
defined](#claim-phone-number-status "#claim-phone-number-status"). 6. Repeat steps 3-5 for all phone numbers you need to claim to your
traffic distribution group. 7. Perform the following steps to associate flows to phone numbers. Do
them in both Regions where the traffic distribution group operates.

These steps ensure your telephony traffic will route correctly to your
flows to support your traffic distribution configuration.

    1. In your existing Amazon Connect instance in the Region where the traffic distribution group
     was created, do the following steps:


    	1. Call [ListContactFlows](../APIReference/API_ListContactFlows.md "../APIReference/API_ListContactFlows.md") API. Provide the
    	 `InstanceId` that corresponds to the
    	 instance that was replicated.
    	2. A list of flow ARNs is returned. Use these flow ARNs
    	 to associate a flow to a phone number; call the [AssociatePhoneNumberContactFlow](../APIReference/API_AssociatePhoneNumberContactFlow.md "../APIReference/API_AssociatePhoneNumberContactFlow.md") API.
    2. In the replicated Amazon Connect instance in the other AWS Region, do
     the following steps:


    	1. Call [ListContactFlows](../APIReference/API_ListContactFlows.md "../APIReference/API_ListContactFlows.md") API. Provide the
    	 `InstanceId` that corresponds to the
    	 instance that was replicated.
    	2. A list of flow ARNs is returned. Use these flow ARNs
    	 to associate a flow to a phone number; call the [AssociatePhoneNumberContactFlow](../APIReference/API_AssociatePhoneNumberContactFlow.md "../APIReference/API_AssociatePhoneNumberContactFlow.md") API.

## Why a ClaimPhoneNumber call

fails

Your [ClaimPhoneNumber](../APIReference/API_ClaimPhoneNumber.md "../APIReference/API_ClaimPhoneNumber.md") API call will fail with a
`ResourceNotFoundException` in the following cases:

- The specified traffic distribution group does not exist, the status of
  the traffic distribution group is not `ACTIVE`, or you do not
  have ownership of the traffic distribution group.
- The phone number is not available for claiming. In some cases, a phone
  number found from [SearchAvailablePhoneNumbers](../APIReference/API_SearchAvailablePhoneNumbers.md "../APIReference/API_SearchAvailablePhoneNumbers.md") may have been claimed by
  another customer.

[ClaimPhoneNumber](../APIReference/API_ClaimPhoneNumber.md "../APIReference/API_ClaimPhoneNumber.md") will fail with a
`InvalidParameterException` error in the following case:

- The endpoint you are calling is not in the same Region where the
  traffic distribution group was created.

## Phone number statuses

defined

Following is a description of phone number statuses:

- `CLAIMED` means the previous [ClaimPhoneNumber](../APIReference/API_ClaimPhoneNumber.md "../APIReference/API_ClaimPhoneNumber.md") or [UpdatePhoneNumber](../APIReference/API_UpdatePhoneNumber.md "../APIReference/API_UpdatePhoneNumber.md") operation succeeded.
- `IN_PROGRESS` means a [ClaimPhoneNumber](../APIReference/API_ClaimPhoneNumber.md "../APIReference/API_ClaimPhoneNumber.md"), [UpdatePhoneNumber](../APIReference/API_UpdatePhoneNumber.md "../APIReference/API_UpdatePhoneNumber.md") operation is still in progress and has
  not yet completed. You can call [DescribePhoneNumber](../APIReference/API_DescribePhoneNumber.md "../APIReference/API_DescribePhoneNumber.md") at a later time to verify if the
  previous operation has completed.
- `FAILED` indicates that the previous [ClaimPhoneNumber](../APIReference/API_ClaimPhoneNumber.md "../APIReference/API_ClaimPhoneNumber.md") or [UpdatePhoneNumber](../APIReference/API_UpdatePhoneNumber.md "../APIReference/API_UpdatePhoneNumber.md") operation has failed. It includes a
  message indicating the failure reason.

A common reason for a failure is that the `TargetArn`
value you are claiming or updating a phone number to has reached its
limit of total claimed numbers.

If you received a `FAILED` status from a
`ClaimPhoneNumber` API call, you have one day to retry
claiming the phone number before the number is released back to the
inventory for other customers to claim.
