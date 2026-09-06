

AWS IoT FleetWise is no longer open to new customers. Existing AWS IoT FleetWise customers can continue using the service. The [Guidance for Connected Mobility on AWS](https://aws.amazon.com/solutions/guidance/connected-mobility-on-aws/) provides guidance on how to develop and deploy modular services for connected mobility solutions that can be used to achieve equivalent capabilities as AWS IoT FleetWise.

# Monitor AWS IoT FleetWise with Amazon CloudWatch
<a name="monitoring-cloudwatch"></a>

**Important**  
Access to certain AWS IoT FleetWise features is currently gated. For more information, see [AWS Region and feature availability in AWS IoT FleetWise](fleetwise-regions.md).

Amazon CloudWatch metrics are a way to monitor your AWS resources and how they're performing. AWS IoT FleetWise sends metrics to CloudWatch. You can use the AWS Management Console, the AWS CLI, or an API to list the metrics that AWS IoT FleetWise sends to CloudWatch. For more information, see the [Amazon CloudWatch User Guide](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/).

**Important**  
You must configure settings so that AWS IoT FleetWise can send metrics to CloudWatch. For more information, see [Configure your AWS IoT FleetWise settings](configure-settings.md).

The `AWS/IoTFleetWise` namespace includes the following metrics.


**Signal metrics**  

| Metric | Description | 
| --- | --- | 
| IllegalMessageFromEdge | A message sent from the vehicle and received by AWS IoT FleetWise didn't match the required format.<br />Units: Count<br />Dimensions: None<br />Valid statistics: Sum | 
| MessageThrottled | A message sent from the vehicle to AWS IoT FleetWise was throttled. This is because you exceeded the [service limits](https://docs.aws.amazon.com/general/latest/gr/iotfleetwise.html) for this account in the current Region.<br />Units: Count<br />Dimensions: None<br />Valid statistics: Sum | 
| ModelingError | A message sent from the vehicle and received by AWS IoT FleetWise contains signals that fail to validate against the vehicle model.<br />Units: Count<br />Dimensions: ModelName, StateTemplateName (Optional), SignalCatalogName (Optional) | 
| DecodingError | A message sent from the vehicle and received by AWS IoT FleetWise contains signals that fail to decoder against the vehicle's decoder manifest.<br />Units: Count<br />Dimensions: DecoderName<br />Valid statistics: Sum | 
| MessageSizeLimitExceeded | A message sent from the vehicle to AWS IoT FleetWise was dropped. This is because you exceeded the maximum size of a message [service limit](https://docs.aws.amazon.com/general/latest/gr/iotfleetwise.html) for this account in the current Region.<br />Units: Count<br />Dimensions: None<br />Valid statistics: Sum | 
| CallCount | The number of messages ingested over the specified time period.<br />Units: Count<br />Dimensions: AccountID | 
| CheckInThrottled | A check-in sent from the vehicle to AWS IoT FleetWise was throttled. This is because you exceeded the [service limit](https://docs.aws.amazon.com/general/latest/gr/iotfleetwise.html) for this account in the current Region. <br />Units: Count<br />Dimensions: VehicleName<br />Valid statistics: Sum | 
| VehicleAttributeNotFound | A message sent from the vehicle and received by AWS IoT FleetWise could not be enriched with the specified vehicle attributes.<br />Units: Count<br />Dimensions: campaignName (optional), stateTemplateName (optional), vehicleName<br />Valid statistics: Sum | 


**Vehicle metrics**  

| Metric | Description | 
| --- | --- | 
| VehicleNotFound | A message received by AWS IoT FleetWise, where the vehicle is unknown.<br />Units: Count<br />Dimensions: None<br />Valid statistics: Sum | 


**Deployment metrics**  

| Metric | Description | 
| --- | --- | 
| PayloadSize | Size of the message sent from AWS IoT FleetWise to the vehicle.<br />Units: KB<br />Dimensions: VehicleName, ResourceTypes (StateTemplates, Campaigns, DecoderManifest) | 
| PayloadSizeLimitExceeded | A message sent from AWS IoT FleetWise to the vehicle exceeded the maximum size of a payload [service limit](https://docs.aws.amazon.com/general/latest/gr/iotfleetwise.html) for this account in the current Region.<br />Units: KB<br />Dimensions: VehicleName<br />Valid statistics: Sum | 


**Campaign metrics**  

| Metric | Description | 
| --- | --- | 
| CampaignInvalid | A message sent from the vehicle and received by AWS IoT FleetWise, where the campaign isn't valid.<br />Units: Count<br />Dimensions: CampaignName<br />Valid statistics: Sum | 
| CampaignNotFound | A message sent from the vehicle and received by AWS IoT FleetWise, where the campaign is unknown.<br />Units: Count<br />Dimensions: CampaignName<br />Valid statistics: Sum | 


**State template metrics**  

| Metric | Description | 
| --- | --- | 
| NoStateTemplatesAssociated | A message sent from the vehicle and received by AWS IoT FleetWise, where no state templates are associated with the vehicle.<br />Units: Count<br />Valid statistics: Sum | 


**Campaign data destination metrics**  

| Metric | Description | 
| --- | --- | 
| TimestreamWriteError | AWS IoT FleetWise couldn't write a message from the vehicle to the Amazon Timestream table.<br />Units: Count<br />Dimensions: DatabaseName, TableName<br />Valid statistics: Sum | 
| S3WriteError | AWS IoT FleetWise couldn't write a message from the vehicle to the Amazon Simple Storage Service (Amazon S3) bucket.<br />Units: Count<br />Dimensions: BucketName<br />Valid statistics: Sum | 
| S3ReadError | AWS IoT FleetWise couldn't read an object key from the vehicle in the Amazon Simple Storage Service (Amazon S3) bucket.<br />Units: Count<br />Dimensions: BucketName<br />Valid statistics: Sum | 


**Customer managed AWS KMS key metrics**  

| Metric | Description | 
| --- | --- | 
| KMSKeyAccessDenied | AWS IoT FleetWise couldn't write a message from the vehicle to the Timestream table or the Amazon S3 bucket because of an AWS KMS key access denied error.<br />Units: Count<br />Dimensions: KMSKeyId<br />Valid statistics: Sum | 