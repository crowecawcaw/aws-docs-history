# Understanding the Kinesis face

recognition JSON frame record

Amazon Rekognition Video can recognize faces in a streaming video. For each analyzed frame, Amazon Rekognition Video
outputs a JSON frame record to a Kinesis data stream. Amazon Rekognition Video doesn't analyze every frame
that's passed to it through the Kinesis video stream.

The JSON frame record contains information about the input and output stream, the
status of the stream processor, and information about faces that are recognized in the
analyzed frame. This section contains reference information for the JSON frame
record.

The following is the JSON syntax for a Kinesis data stream record. For more information, see [Working with streaming video events](streaming-video.md "streaming-video.md").

###### Note

The Amazon Rekognition Video API works by comparing the faces in your input stream to a collection
of faces, and returning the closest found matches, along with a similarity score.

```
{
    "InputInformation": {
        "KinesisVideo": {
            "StreamArn": "string",
            "FragmentNumber": "string",
            "ProducerTimestamp": number,
            "ServerTimestamp": number,
            "FrameOffsetInSeconds": number
        }
    },
    "StreamProcessorInformation": {
        "Status": "RUNNING"
    },
    "FaceSearchResponse": [
        {
            "DetectedFace": {
                "BoundingBox": {
                    "Width": number,
                    "Top": number,
                    "Height": number,
                    "Left": number
                },
                "Confidence": number,
                "Landmarks": [
                    {
                        "Type": "string",
                        "X": number,
                        "Y": number
                    }
                ],
                "Pose": {
                    "Pitch": number,
                    "Roll": number,
                    "Yaw": number
                },
                "Quality": {
                    "Brightness": number,
                    "Sharpness": number
                }
            },
            "MatchedFaces": [
                {
                    "Similarity": number,
                    "Face": {
                        "BoundingBox": {
                            "Width": number,
                            "Top": number,
                            "Height": number,
                            "Left": number
                        },
                        "Confidence": number,
                        "ExternalImageId": "string",
                        "FaceId": "string",
                        "ImageId": "string"
                    }
                }
            ]
        }
    ]
}
```

## JSON record

The JSON record includes information about a frame that's processed by Amazon Rekognition Video.
The record includes information about the streaming video, the status for the
analyzed frame, and information about faces that are recognized in the frame.

**InputInformation**

Information about the Kinesis video stream that's used to stream video into Amazon Rekognition Video.

Type: [InputInformation](#streaming-video-kinesis-output-reference-inputinformation "#streaming-video-kinesis-output-reference-inputinformation")
object

**StreamProcessorInformation**

Information about the Amazon Rekognition Video stream processor. This includes status information
for the current status of the stream processor.

Type: [StreamProcessorInformation](streaming-video-kinesis-output-reference-streamprocessorinformation.md "streaming-video-kinesis-output-reference-streamprocessorinformation.md")
object

**FaceSearchResponse**

Information about the faces detected in a streaming video frame and the matching faces found in the input collection.

Type: [FaceSearchResponse](#streaming-video-kinesis-output-reference-facesearchresponse "#streaming-video-kinesis-output-reference-facesearchresponse") object array

## InputInformation

Information about a source video stream that's used by Amazon Rekognition Video. For more
information, see [Working with streaming video events](streaming-video.md "streaming-video.md").

**KinesisVideo**

Type: [KinesisVideo](#streaming-video-kinesis-output-reference-kinesisvideostreams-kinesisvideo "#streaming-video-kinesis-output-reference-kinesisvideostreams-kinesisvideo") object

## KinesisVideo

Information about the Kinesis video stream that streams the source video into Amazon Rekognition Video. For
more information, see [Working with streaming video events](streaming-video.md "streaming-video.md").

**StreamArn**

The Amazon Resource Name (ARN) of the Kinesis video stream.

Type: String

**FragmentNumber**

The fragment of streaming video that contains the frame that this record
represents.

Type: String

**ProducerTimestamp**

The producer-side Unix time stamp of the fragment. For more information, see [PutMedia](../../../kinesisvideostreams/latest/dg/API_dataplane_PutMedia.md "../../../kinesisvideostreams/latest/dg/API_dataplane_PutMedia.md").

Type: Number

**ServerTimestamp**

The server-side Unix time stamp of the fragment. For more information, see [PutMedia](../../../kinesisvideostreams/latest/dg/API_dataplane_PutMedia.md "../../../kinesisvideostreams/latest/dg/API_dataplane_PutMedia.md").

Type: Number

**FrameOffsetInSeconds**

The offset of the frame (in seconds) inside the fragment.

Type: Number

## FaceSearchResponse

Information about a face detected in a streaming video frame and the faces in a collection that match the detected face. You specify the collection in a call to [CreateStreamProcessor](../APIReference/API_CreateStreamProcessor.md "../APIReference/API_CreateStreamProcessor.md"). For more information, see [Working with streaming video events](streaming-video.md "streaming-video.md").

**DetectedFace**

Face details for a face detected in an analyzed video
frame.

Type: [DetectedFace](#streaming-video-kinesis-output-reference-detectedface "#streaming-video-kinesis-output-reference-detectedface")
object

**MatchedFaces**

An array of face details for faces in a collection that matches the face detected in `DetectedFace`.

Type: [MatchedFace](#streaming-video-kinesis-output-reference-facematch "#streaming-video-kinesis-output-reference-facematch")
object array

## DetectedFace

Information about a face that's detected in a streaming video frame. Matching faces in the input collection are available in
[MatchedFace](#streaming-video-kinesis-output-reference-facematch "#streaming-video-kinesis-output-reference-facematch") object field.

**BoundingBox**

The bounding box coordinates for a face that's detected within an analyzed video
frame. The BoundingBox object has the same properties as the BoundingBox object
that's used for image analysis.

Type: [BoundingBox](../APIReference/API_BoundingBox.md "../APIReference/API_BoundingBox.md") object

**Confidence**

The confidence level (1-100) that Amazon Rekognition Video has that the detected face is actually a
face. 1 is the lowest confidence, 100 is the highest.

Type: Number

**Landmarks**

An array of facial landmarks.

Type: [Landmark](../APIReference/API_Landmark.md "../APIReference/API_Landmark.md") object array

**Pose**

Indicates the pose of the face as determined by its pitch, roll, and yaw.

Type: [Pose](../APIReference/API_Pose.md "../APIReference/API_Pose.md") object

**Quality**

Identifies face image brightness and sharpness.

Type: [ImageQuality](../APIReference/API_ImageQuality.md "../APIReference/API_ImageQuality.md") object

## MatchedFace

Information about a face that matches a face detected in an analyzed video frame.

**Face**

Face match information for a face in the input collection that matches the face in the
[DetectedFace](#streaming-video-kinesis-output-reference-detectedface "#streaming-video-kinesis-output-reference-detectedface") object.

Type: [Face](../APIReference/API_Face.md "../APIReference/API_Face.md") object

**Similarity**

The level of confidence (1-100) that the faces match. 1 is the lowest confidence, 100 is the highest.

Type: Number
