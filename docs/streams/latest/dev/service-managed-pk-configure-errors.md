

# Error handling
<a name="service-managed-pk-configure-errors"></a>

The following errors can occur when configuring the record distribution strategy:


**Configuration errors**  

| Error | Cause | Status | 
| --- | --- | --- | 
| InvalidArgumentException | Attempting to enable service-managed record distribution on a provisioned stream. Service-managed record distribution is only supported for on-demand streams. The service returns a message similar to the following: RecordDistributionStrategy=AUTO is only supported for on-demand streams. Stream [StreamName] is using PROVISIONED mode. | 400 | 
| ResourceNotFoundException | The specified stream does not exist. | 400 | 
| LimitExceededException | Too many concurrent stream configuration changes. Wait and retry. | 400 | 