

# Configuring Multi-Region Access Point opt-in Regions
<a name="ConfiguringMrapOptInRegions"></a>

An AWS opt-in Region is a Region that isn’t enabled by default in your AWS account. In contrast, Regions that are enabled by default are known as AWS Regions or commercial Regions.

To start using Multi-Region Access Points in AWS opt-in Regions, you must manually enable the opt-in Region for your AWS account before creating your Multi-Region Access Point. After you enable the opt-in Region, you can create Multi-Region Access Points with buckets in the selected opt-in Region. For instructions on how to enable or disable an opt-in Region for your AWS account or AWS Organization, see [Enable or disable a Region for standalone accounts](https://docs.aws.amazon.com/accounts/latest/reference/manage-acct-regions.html#manage-acct-regions-enable-standalone) or [Enable or disable a Region in your organization](https://docs.aws.amazon.com/accounts/latest/reference/manage-acct-regions.html#manage-acct-regions-enable-organization).

**Note**  
Multi-Region Access Point opt-in Regions are currently only supported through AWS SDKs and AWS CLI.

 S3 Multi-Region Access Points supports the following AWS opt-in Regions:
+ `Africa (Cape Town)`
+ `Asia Pacific (Hong Kong)`
+ `Asia Pacific (Jakarta)`
+ `Asia Pacific (Melbourne)`
+ `Asia Pacific (Hyderabad)`
+ `Canada West (Calgary)`
+ `Europe (Zurich)`
+ `Europe (Milan)`
+ `Europe (Spain)`
+ `Israel (Tel Aviv)`
+ `Middle East (Bahrain)`
+ `Middle East (UAE)`

**Note**  
There are no additional costs for enabling an opt-in Region. However, creating or using a resource in a Multi-Region Access Point results in billing charges.

## Using a Multi-Region Access Point in an AWS opt-in Region
<a name="UsingMrapOptInRegions"></a>

To perform a [data plane operation](https://docs.aws.amazon.com/AmazonS3/latest/userguide/MrapOperations.html) on your Multi-Region Access Point, all associated AWS accounts must enable the opt-in Regions that are part of the Multi-Region Access Point. This requirement applies to the requester account, the Multi-Region Access Point owner, S3 bucket owners, and the VPC endpoint owner. If any of these accounts don’t enable AWS opt-in Regions, the Multi-Region Access Point requests fail. For more information about the `InvalidToken` or `AllAccessDisabled` errors, see [List of error codes](https://docs.aws.amazon.com/AmazonS3/latest/API/ErrorResponses.html#ErrorCodeList).

**Note**  
[Control plane operations](https://docs.aws.amazon.com/AmazonS3/latest/userguide/MrapOperations.html) such as updating your Multi-Region Access Point policy or updating your failover configuration aren’t impacted by the opt-in Region status of any Region that is part of your Multi-Region Access Point. You also don’t need to disable any active opt-in Regions before deleting a Multi-Region Access Point.

## Disabling an active AWS opt-in Region
<a name="DisablingMrapOptInRegions"></a>

If you disable opt-in Region that is part of your Multi-Region Access Point, requests routed to this Region result in a `403 AllAccessDisabled` error. To safely disable an opt-in Region, we recommend that you first identify an alternate Region in your Multi-Region Access Point configuration to route the traffic to. You can then use Multi-Region Access Point failover controls to mark the alternate Region as active, and mark the Region to be disabled as passive. After changing the failover controls, you can disable the Region you want to opt out of.

## Enabling a previously disabled AWS opt-in Region
<a name="EnablingDisabledMrapOptInRegions"></a>

To enable an opt-in AWS Region that was previously disabled for your Multi-Region Access Point, make sure to update your AWS account settings. After you re-enable the opt-in Region, run the [PutMultiRegionAccessPointPolicy](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_PutMultiRegionAccessPointPolicy.html) API operation to apply the Multi-Region Access Points policy to the opt-in Region.

If your Multi-Region Access Point is accessed through a VPC endpoint, we recommend that you update your VPCE policy and use the [ModifyVpcEndpoint](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyVpcEndpoint.html) API operation to apply the updated VPC endpoint policy to the re-enabled opt-in Region.

## Multi-Region Access Points policy and multiple AWS accounts
<a name="UsingMrapPolicyOptInRegions"></a>

If your Multi-Region Access Points policy grants access to multiple AWS accounts, all requester accounts must also enable the same opt-in Regions in their account settings. If the requester account submits a Multi-Region Access Point request without enabling the opt-in Regions that are part of the Multi-Region Access Point, it’ll result in a `400 InvalidToken` error.

## AWS opt-in Region considerations
<a name="MrapOptInRegionsConsiderations"></a>

When you access a Multi-Region Access Point from an opt-in Region, be aware of the following:
+ When you enable an opt-in Region, it allows you to create a Multi-Region Access Point using the buckets from the opt-in Region. When you disable an opt-in Region, the Multi-Region Access Point is no longer supported in the opt-in Region. If you no longer want an opt-in Region enabled for your Multi-Region Access Point, make sure to [disable the Region for your account](https://docs.aws.amazon.com/accounts/latest/reference/manage-acct-regions.html#manage-acct-regions-enable-standalone) first. Then, create a new Multi-Region Access Point with your preferred list of opt-in Regions.
+ If you attempt to create your Multi-Region Access Point with a disabled opt-in Region, you’ll receive a `403 InvalidRegion` error. After you enable the opt-in Region, try creating the Multi-Region Access Point again.
+ The maximum number of supported Regions for a Multi-Region Access Point is 17 Regions. This includes both opt-in Regions and commercial Regions. For more information, see [Multi-Region Access Points restrictions and limitations](https://docs.aws.amazon.com/AmazonS3/latest/userguide/MultiRegionAccessPointRestrictions.html).
+ Control plane requests for Multi-Region Access Points will work, even if you haven't opted in to any Regions.
+ When you're trying to create a Multi-Region Access Point for the first time, you must opt into all Regions that are part of the Multi-Region Access Point.
+ Any AWS accounts that are granted access to an S3 Multi-Region Access Point through the Multi-Region Access Point policy must also enable the same opt-in Regions that are part of the Multi-Region Access Point.