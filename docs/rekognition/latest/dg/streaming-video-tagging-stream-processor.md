# Add tags to a new stream processor

###### Note

Amazon Rekognition Streaming Video Analysis will no longer be
open to new customers starting April 30, 2026. If you would like to use Streaming Video Analysis, sign up prior to
that date. Existing customers for accounts that have used this feature within the last 12 months can continue
to use the service as normal. For more information, see
[Rekognition Streaming Video Analysis availability change](rekognition-streaming-video-analysis-availability-change.md "rekognition-streaming-video-analysis-availability-change.md").

You can identify, organize, search for, and filter Amazon Rekognition stream processors by using tags. Each tag is a label consisting of a
user-defined key and value.

You can add tags to a stream processor as you create it using the `CreateStreamProcessor` operation. Specify one or more tags in the `Tags` array input parameter.
The following is a JSON
example for the `CreateStreamProcessor` request with tags.

```
{
       "Name": "streamProcessorForCam",
       "Input": {
              "KinesisVideoStream": {
                     "Arn": "arn:aws:kinesisvideo:us-east-1:nnnnnnnnnnnn:stream/inputVideo"
              }
       },
       "Output": {
              "KinesisDataStream": {
                     "Arn": "arn:aws:kinesis:us-east-1:nnnnnnnnnnnn:stream/outputData"
              }
       },
       "RoleArn": "arn:aws:iam::nnnnnnnnnnn:role/roleWithKinesisPermission",
       "Settings": {
              "FaceSearch": {
                     "CollectionId": "collection-with-100-faces",
                     "FaceMatchThreshold": 85.5
              },
              "Tags": {
      "Dept": "Engineering",
        "Name": "Ana Silva Carolina",
        "Role": "Developer"
       }
}

```
