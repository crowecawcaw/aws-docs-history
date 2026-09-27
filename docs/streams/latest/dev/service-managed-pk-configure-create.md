

# Create a stream with service-managed record distribution
<a name="service-managed-pk-configure-create"></a>

To create a new stream with service-managed record distribution, include the `RecordDistributionStrategy` parameter set to `AUTO` in your [CreateStream](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_CreateStream.html) API call. If you do not specify this parameter, the stream defaults to `USER_PARTITION_KEY` (user-managed partition keys).

**Example Create a stream with service-managed distribution (AWS CLI)**  

```
aws kinesis create-stream \
    --stream-name my-telemetry-stream \
    --stream-mode-details StreamMode=ON_DEMAND \
    --record-distribution-strategy AUTO
```

**Example Create a stream with service-managed distribution (AWS SDK for Java)**  

```
CreateStreamRequest request = CreateStreamRequest.builder()
    .streamName("my-telemetry-stream")
    .streamModeDetails(StreamModeDetails.builder()
        .streamMode(StreamMode.ON_DEMAND)
        .build())
    .recordDistributionStrategy(RecordDistributionStrategy.AUTO)
    .build();

kinesisClient.createStream(request);
```