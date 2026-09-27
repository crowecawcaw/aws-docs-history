

# Error handling
<a name="service-managed-pk-producing-errors"></a>

The following errors are specific to writing records to service-managed streams:


**Producer errors for service-managed streams**  

| Error | Cause | Status | 
| --- | --- | --- | 
| InvalidArgumentException | `SequenceNumberForOrdering` was provided in a `PutRecord` request. This field must not be included when writing to a service-managed stream, because ordering is not applicable. (`PutRecords` has no `SequenceNumberForOrdering` field.) A supplied `ExplicitHashKey` is ignored and does not cause an error. The service returns a message similar to the following:<br />`Stream has SERVICE_DEFINED PartitionKey enabled. SequenceNumberForOrdering must not be provided.` | 400 | 