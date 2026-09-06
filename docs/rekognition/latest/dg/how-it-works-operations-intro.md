

# Understanding Rekognition's image and video operations
<a name="how-it-works-operations-intro"></a>

Amazon Rekognition offers two primary API sets for image and video analysis:
+ Amazon Rekognition Image: This API is designed for analyzing images.
+ Amazon Rekognition Video: This API focuses on analyzing both stored and streaming videos.

Both APIs can detect various entities such as faces and objects. For a comprehensive understanding of the comparison and detection types supported, refer to the section on [Understanding Rekognition's types of analysis](how-it-works-types.md).

## Amazon Rekognition Image operations
<a name="how-it-works-operations-images"></a>

Amazon Rekognition Image operations are synchronous. The input and response are in JSON format. Amazon Rekognition Image operations analyze an input image that is in .jpg or .png image format. The image passed to an Amazon Rekognition Image operation can be stored in an Amazon S3 bucket. If you are not using the AWS CLI, you can also pass Base64 encoded images bytes directly to an Amazon Rekognition operation. For more information, see [Working with images](https://docs.aws.amazon.com/rekognition/latest/dg/images.html).

## Amazon Rekognition Video operations
<a name="how-it-works-operations-video-intro"></a>

The Amazon Rekognition Video API facilitates the analysis of videos either stored in an Amazon S3 bucket or streamed via Amazon Kinesis Video Streams.

For stored video operations, note the following:
+ Operations are asynchronous.
+ Analysis must be initiated with a “Start” operation (e.g., [StartFaceDetection](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_StartFaceDetection.html) for face detection in stored videos).
+ The completion status of analysis is published to an Amazon SNS topic.
+ To retrieve the results of an analysis, use the corresponding “Get” operation (e.g., [GetFaceDetection](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_GetFaceDetection.html)).
+ For more information, see [Working with stored video analysis](https://docs.aws.amazon.com/rekognition/latest/dg/video.html).

For streaming video analysis:
+ Capabilities include face search in Rekognition Video collections and label (object or concept) detection.
+ Analysis results for labels are sent as Amazon SNS and Amazon S3 notifications.
+ Face search results are output to a Kinesis data stream.
+ Management of streaming video analysis is done via an Amazon Rekognition Video stream processor (e.g., create a processor using [CreateStreamProcessor](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_CreateStreamProcessor.html)).
+ For more information, see [Working with streaming video events](https://docs.aws.amazon.com/rekognition/latest/dg/streaming-video.html).

Each video analysis operation returns metadata about the video being analyzed, as well as a job ID and a job tag. Operations like Label Detection and Content Moderation for video allow sorting by timestamp or label name, and aggregating results by timestamp or by segment.

## Non-storage and storage-based operations
<a name="how-it-works-operations-video-storage"></a>

Amazon Rekognition operations are grouped into the following categories.
+ **Non-storage API operations** – In these operations, Amazon Rekognition doesn't persist any information. You provide input images and videos, the operation performs the analysis, and returns results, but nothing is saved by Amazon Rekognition. For more information, see [Non-storage operations](how-it-works-storage-non-storage.md#how-it-works-non-storage).
+ **Storage-based API operations** – Amazon Rekognition servers can store detected facial information in containers known as collections. Amazon Rekognition provides additional API operations you can use to search the persisted face information for face matches. For more information, see [Storage-based API operations](how-it-works-storage-non-storage.md#how-it-works-storage-based).

## Using the AWS SDK or HTTP to call Amazon Rekognition API operations
<a name="images-java-http"></a>

You can call Amazon Rekognition API operations using either the AWS SDK or directly by using HTTP. Unless you have a good reason not to, you should always use the AWS SDK. The Java examples in this section use the [AWS SDK](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/setup-install.html). A Java project file is not provided, but you can use the [AWS Toolkit for Eclipse](https://docs.aws.amazon.com/AWSToolkitEclipse/latest/GettingStartedGuide/) to develop AWS applications using Java. 

The .NET examples in this section use the [AWS SDK for .NET](https://docs.aws.amazon.com/sdk-for-net/latest/developer-guide/welcome.html). You can use the [AWS Toolkit for Visual Studio](https://docs.aws.amazon.com/AWSToolkitVS/latest/UserGuide/welcome.html) to develop AWS applications using .NET. It includes helpful templates and the AWS Explorer for deploying applications and managing services. 

The [API Reference](https://docs.aws.amazon.com/rekognition/latest/APIReference/Welcome.html) in this guide covers calling Amazon Rekognition operations using HTTP. For Java reference information, see [AWS SDK for Java](https://docs.aws.amazon.com/sdk-for-java/latest/reference/index.html).

The Amazon Rekognition service endpoints you can use are documented at [AWS Regions and Endpoints](https://docs.aws.amazon.com/general/latest/gr/rande.html#rekognition_region). 

When calling Amazon Rekognition with HTTP, use POST HTTP operations.