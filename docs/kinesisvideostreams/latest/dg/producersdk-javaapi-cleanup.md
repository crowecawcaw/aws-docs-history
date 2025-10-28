# Clean up resources

In order to avoid memory leaks, do the following to unregister a media source from the
client and free the client.

```
try {
    kinesisVideoClient.unregisterMediaSource(mediaSource);
    kinesisVideoClient.free();
} catch (final KinesisVideoException e) {
    throw new RuntimeException(e);
}
```

If you added any items to the cache using the [`CachedInfoMultiAuthServiceCallbacks`](https://github.com/awslabs/amazon-kinesis-video-streams-producer-sdk-java/blob/master/src/main/java/com/amazonaws/kinesisvideo/java/service/CachedInfoMultiAuthServiceCallbacksImpl.java "https://github.com/awslabs/amazon-kinesis-video-streams-producer-sdk-java/blob/master/src/main/java/com/amazonaws/kinesisvideo/java/service/CachedInfoMultiAuthServiceCallbacksImpl.java"), for example:

```
serviceCallbacks.addStreamInfoToCache(streamName, streamInfo);
serviceCallbacks.addStreamingEndpointToCache(streamName, dataEndpoint);
```

Clear the cache when you're done:

```
serviceCallbacks.removeStreamFromCache(streamName);
```
