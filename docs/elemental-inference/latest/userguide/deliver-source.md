

# Step C: Deliver the source media
<a name="deliver-source"></a>

To deliver the source media, you must use an AWS API or SDK. You can't deliver the media using the Elemental Inference console.

1. Obtain the data endpoint for the feed:
   + Using an AWS API or SDK: Use the `GetFeed` operation of Elemental Inference. For information about the operation and parameters, see [https://docs.aws.amazon.com/elemental-inference/latest/APIReference/API_GetFeed](https://docs.aws.amazon.com/elemental-inference/latest/APIReference/API_GetFeed). 
   + Using the Elemental Inference console: Choose Feed in the left navigation bar, then select the feed. In the details page, the data endpoint is in the **Integration** field. 

1. Use the Elemental Inference PutMedia operation to deliver the source media to that data endpoint. Make sure to stay within the quotas for the Request rate for PutMedia and the Request rate for PutMedia (in a burst). To view the current quotas, open the [Service Quotas console](https://console.aws.amazon.com/servicequotas/home). In the navigation pane, choose **AWS services** and select **AWS Elemental Inference**.

## Streaming requirements
<a name="deliver-source-requirements"></a>

You must deliver the source media according to the CMAF Ingest (Interface-1) version 1.2 specification. 

The following table identifies specific requirements for Elemental Inference.


| Characteristic | Requirement | 
| --- | --- | 
| Media segment duration | 0-1.2 seconds | 
| Ingestion order | Elemental Inference will ingest all media segments (audio and video) for a given sequence number before proceeding to the next sequence number | 
| End of Stream indicator (workaround) | Typically, the last media segment includes `lmsg`.<br />However, if you can't signal the end of stream in this way (for example, you are using FFMG), then flush the Elemental Inference internal buffer as follows:+  Send up to 10 seconds of slate.  | 
| Manifest | CMAF Ingest doesn't support manifests. | 

## Example
<a name="deliver-source-example"></a>

The following code sample shows how to use CURL to use the PUT operation to send the content to the data endpoint of a feed. (The example assumes that you have exported your AWS credentials as environment variables, which is standard practice when using the AWS REST API.)

```
# Initialization
$ awscurl --region <{{region}}> --service elemental-inference -X PUT \
  'https://<{{data-endpoint}}>/v1/feed/<{{feed-id}}>/input/0/media/Streams(default-audio.cmfa)/InitializationSegment' \
  --data-binary -d '@Streams(default-audio.cmfa)/InitializationSegment'

$ awscurl --region <{{region}}> --service elemental-inference -X PUT \
  'https://<data-endpoint>/v1/feed/<{{feed-id}}>/input/0/media/Streams(default-video.cmfv)/InitializationSegment' \
  --data-binary -d '@Streams(default-video.cmfv)/InitializationSegment'
        
# Media
$ awscurl --region <{{region}}> --service elemental-inference -X PUT \
 'https://<{{data-endpoint}}>/v1/feed/<{{feed-id}}>/input/0/media/Streams(default-audio.cmfa)/Segment(<{{sequence}}>)' \
 --data-binary -d '@Streams(default-audio.cmfa)/Segment(<{{sequence}}>)'

$ awscurl --region <{{region}}> --service elemental-inference -X PUT \
  'https://<{{data-endpoint}}>/v1/feed/<{{feed-id}}>/input/0/media/Streams(default-video.cmfv)/Segment(<{{sequence}}>)' \
  --data-binary -d '@Streams(default-video.cmfv)/Segment(<{{sequence}}>)'
```