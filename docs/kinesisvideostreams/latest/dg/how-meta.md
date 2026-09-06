

# Using streaming metadata with Kinesis Video Streams
<a name="how-meta"></a>

You can use the Amazon Kinesis Video Streams producer SDK to embed metadata at the individual fragment level in a Kinesis video stream. Metadata in Kinesis Video Streams is a mutable key-value pair. You can use it to describe the content of the fragment, embed associated sensor readings that must be transferred along with the actual fragment, or meet other custom needs. The metadata is made available as part of the [GetMedia](https://docs.aws.amazon.com/kinesisvideostreams/latest/APIReference/API_dataplane_GetMedia.html) or [GetMediaForFragmentList](https://docs.aws.amazon.com/kinesisvideostreams/latest/APIReference/API_reader_GetMediaForFragmentList.html) API operations. It's stored along with the fragments for the entire duration of the stream's retention period. Your consuming applications can read, process, and react based on the metadata using the [Watch output from cameras using parser library](parser-library.md). 

There are two modes in which the metadata can be embedded with fragments in a stream: 
+ **Nonpersistent** – You can affix metadata on a one-time, or ad hoc basis to fragments in a stream, based on business-specific criteria that have occurred. An example is a smart camera that detects motion and adds metadata to the corresponding fragments that contain the motion before sending the fragments to its Kinesis video stream. You might apply metadata to the fragment in the following format: `Motion = true`.
+ **Persistent** – You can affix metadata to successive, consecutive fragments in a stream based on a continuing need. An example is a smart camera that sends the current latitude and longitude coordinates associated with all fragments that it sends to its Kinesis video stream. You might apply metadata to all the fragments in the following format: `Lat = 47.608013N , Long = -122.335167W`

You can affix metadata in both of these modes to the same fragment simultaneously, based on your application's needs. The embedded metadata might include objects detected, activity tracked, GPS coordinates, or any other custom data that you want to associate with the fragments in the stream. Metadata is encoded as key-value string pairs.

## Adding metadata to a Kinesis video stream
<a name="how-meta-add"></a>

Metadata that you add to a Kinesis video stream is modeled as MKV tags, which are implemented as key-value pairs. 

Metadata can either be *transient*, such as to mark an event within the stream, or *persistent*, such as to identify fragments where a given event is taking place. A persistent metadata item remains, and is applied to each consecutive fragment, until it's canceled.

**Note**  
The metadata items added using the [Upload to Kinesis Video Streams](producer-sdk.md) are distinct from the stream-level tagging APIs implemented with [TagStream](https://docs.aws.amazon.com/kinesisvideostreams/latest/APIReference/API_TagStream.html), [UntagStream](https://docs.aws.amazon.com/kinesisvideostreams/latest/APIReference/API_UntagStream.html), and [ListTagsForStream](https://docs.aws.amazon.com/kinesisvideostreams/latest/APIReference/API_ListTagsForStream.html).

### Streaming metadata API
<a name="how-meta-api"></a>

You can use the following operations in the producer SDK to implement streaming metadata.

**Topics**
+ [PIC](#how-meta-api-pic)
+ [C\+\+ producer SDK](#how-meta-api-cpp)
+ [Java producer SDK](#how-meta-api-java)
+ [Persistent and nonpersistent metadata](#how-meta-api-persistence)

#### PIC
<a name="how-meta-api-pic"></a>

```
PUBLIC_API STATUS putKinesisVideoFragmentMetadata(STREAM_HANDLE streamHandle, 
    PCHAR name, 
    PCHAR value, 
    BOOL persistent);
```

#### C\+\+ producer SDK
<a name="how-meta-api-cpp"></a>

```
/**
 * Appends a "tag" or metadata - a key/value string pair into the stream.
 */
bool putFragmentMetadata(const std::string& name, const std::string& value, bool persistent = true);
```

#### Java producer SDK
<a name="how-meta-api-java"></a>

You can use the Java producer SDK, to add metadata to a `MediaSource` using `MediaSourceSink.onCodecPrivateData`:

```
void onFragmentMetadata(final @Nonnull String metadataName, final @Nonnull String metadataValue, final boolean persistent)
throws KinesisVideoException;
```

#### Persistent and nonpersistent metadata
<a name="how-meta-api-persistence"></a>

For nonpersistent metadata, you can add multiple metadata items with the same *name*. The producer SDK collects the metadata items in the metadata queue until they are prepended to the next fragment. The metadata queue is cleared as the metadata items are applied to the stream. To repeat the metadata, call `putKinesisVideoFragmentMetadata` or `putFragmentMetadata` again. 

For persistent metadata, the producer SDK collects the metadata items in the metadata queue in the same way as for nonpersistent metadata. However, the metadata items aren't removed from the queue when they are prepended to the next fragment.

Calling `putKinesisVideoFragmentMetadata` or `putFragmentMetadata` with `persistent` set to `true` has the following behavior: 
+ Calling the API puts the metadata item in the queue. The metadata is added as an MKV tag to every fragment while the item is in the queue.
+ Calling the API with the same *name* and a different *value* as a previously added metadata item overwrites the item.
+ Calling the API with an empty *value* removes (cancels) the metadata item from the metadata queue.

