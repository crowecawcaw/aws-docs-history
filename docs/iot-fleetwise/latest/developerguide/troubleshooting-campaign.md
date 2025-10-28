# Store and forward issues

###### Important

Access to certain AWS IoT FleetWise features is currently gated. For more information, see [AWS Region and feature availability in AWS IoT FleetWise](fleetwise-regions.md "fleetwise-regions.md").

## Issue: Receiving an

`AccessDeniedException` with all required IAM
permissions

**Solution:** The store and forward feature for data partitioning in campaigns requires gated access through allow listing. Contact the service team to ensure that your resources have adequate permissions through allow listing.

## Issue: The data uploaded to AWS IoT

Jobs ignores the `endTime`

**Solution:** You have specified an invalid `endtime` in the job document. For
example, the `endtime` doesn't following ISO 8601 UTC format). On AWS IoT FleetWise
Agent logs, there could be a warning-level statement that says, `Malformed IoT
 Job endTime: `customer configured endTime`. Not setting
 endTime`.

## Issue: The data upload to AWS IoT

Jobs has a `REJECTED` execution status.

**Solution:** You have specified an invalid `campaignArn` in the job document. For
example, if you specify an ARN for a campaign that is not running on a vehicle,
there could be a error-level statement that says, `CampaignArn value in the
 received job document does not match the ARN of a Store and Forward
 campaign` in the AWS IoT FleetWise Agent logs.
