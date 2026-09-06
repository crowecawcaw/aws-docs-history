

AWS IoT FleetWise is no longer open to new customers. Existing AWS IoT FleetWise customers can continue using the service. The [Guidance for Connected Mobility on AWS](https://aws.amazon.com/solutions/guidance/connected-mobility-on-aws/) provides guidance on how to develop and deploy modular services for connected mobility solutions that can be used to achieve equivalent capabilities as AWS IoT FleetWise.

# Store and forward issues
<a name="troubleshooting-campaign"></a>

**Important**  
Access to certain AWS IoT FleetWise features is currently gated. For more information, see [AWS Region and feature availability in AWS IoT FleetWise](fleetwise-regions.md).

## Issue: Receiving an `AccessDeniedException` with all required IAM permissions
<a name="troubleshooting-campaign-issue1"></a>

**Solution: ** The store and forward feature for data partitioning in campaigns requires gated access through allow listing. Contact the service team to ensure that your resources have adequate permissions through allow listing.

## Issue: The data uploaded to AWS IoT Jobs ignores the `endTime`
<a name="troubleshooting-campaign-issue2"></a>

**Solution: **You have specified an invalid `endtime` in the job document. For example, the `endtime` doesn't following ISO 8601 UTC format). On AWS IoT FleetWise Agent logs, there could be a warning-level statement that says, `Malformed IoT Job endTime: customer configured endTime. Not setting endTime`.

## Issue: The data upload to AWS IoT Jobs has a `REJECTED` execution status.
<a name="troubleshooting-campaign-issue3"></a>

**Solution: **You have specified an invalid `campaignArn` in the job document. For example, if you specify an ARN for a campaign that is not running on a vehicle, there could be a error-level statement that says, `CampaignArn value in the received job document does not match the ARN of a Store and Forward campaign` in the AWS IoT FleetWise Agent logs.