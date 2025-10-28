# Assign claimed

phone numbers to traffic distribution groups in Amazon Connect

- You created a new traffic distribution group and it's status is
  `ACTIVE`. We recommend using the [DescribeTrafficDistributionGroup](../APIReference/API_DescribeTrafficDistributionGroup.md "../APIReference/API_DescribeTrafficDistributionGroup.md") API to verify the
  status.
- You have already claimed phone numbers to instances or other traffic
  distribution groups.
  Now you can assign those claimed phone numbers to your new traffic distribution
  group by using the [UpdatePhoneNumber](../APIReference/API_UpdatePhoneNumber.md "../APIReference/API_UpdatePhoneNumber.md") API. Provide the traffic distribution group ARN in
  the `TargetArn` parameter.

###### Note

To update the **Description** field, you must use the Amazon Connect
console.

## Example workflow

Following is an example workflow to assign claimed phone numbers to your
traffic distribution group:

1. Call the [UpdatePhoneNumber](../APIReference/API_UpdatePhoneNumber.md "../APIReference/API_UpdatePhoneNumber.md") API to assign the phone number to a new
   `TargetArn`.

The `TargetArn` can be for another Amazon Connect instance or for a
traffic distribution group created in the same Region where the phone
number was initially claimed. 2. Perform the following steps to associate flows to phone numbers.

These steps ensure your telephony traffic will route correctly to your
flows to support your traffic distribution configuration.

    1. In your existing Amazon Connect instance in the Region where the traffic distribution group
     was created, do the following steps:


    	1. Call the [ListContactFlows](../APIReference/API_ListContactFlows.md "../APIReference/API_ListContactFlows.md") API. Provide the
    	 `InstanceId` that corresponds to the
    	 instance that was replicated.
    	2. A list of flow ARNs is returned. Use these flow ARNs
    	 to associate a flow to a phone number; call the [AssociatePhoneNumberContactFlow](../APIReference/API_AssociatePhoneNumberContactFlow.md "../APIReference/API_AssociatePhoneNumberContactFlow.md") API.The phone number to flow association will be mirrored between Amazon Connect

instances across AWS Regions.

## Why an

AssociatePhoneNumberContactFlow call fails

If the number is claimed to a traffic distribution group, and you are calling [AssociatePhoneNumberContactFlow](../APIReference/API_AssociatePhoneNumberContactFlow.md "../APIReference/API_AssociatePhoneNumberContactFlow.md") using an instance in the AWS Region where the traffic distribution group was created, you can use either a full
phone number ARN or UUID value for the `PhoneNumberId` URI request
parameter.

However, if the number is claimed to a traffic distribution group and you are calling this API
using an instance in the replica AWS Region associated with the
traffic distribution group, you must provide a full phone number ARN. If a UUID is provided
in
this scenario, you will receive a
`ResourceNotFoundException`.

## Why an UpdatePhoneNumber call

fails

Your [UpdatePhoneNumber](../APIReference/API_UpdatePhoneNumber.md "../APIReference/API_UpdatePhoneNumber.md") API call will fail with a
`ResourceNotFoundException` in the following case:

- The specified traffic distribution group does not exist, the status of
  the traffic distribution group is not `ACTIVE`, or you do not
  have ownership of the traffic distribution group.

[UpdatePhoneNumber](../APIReference/API_UpdatePhoneNumber.md "../APIReference/API_UpdatePhoneNumber.md") will fail with a
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
  message indicating the failure reason. A common reason for a failure is
  that the `TargetArn` value you are claiming or updating a
  phone number to has reached its limit of total claimed numbers.
