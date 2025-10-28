# Understanding non-storage and storage

API operations

Amazon Rekognition provides two types of API operations. They are non-storage operations where
no information is stored by Amazon Rekognition, and storage operations where certain facial
information is stored by Amazon Rekognition.

## Non-storage operations

Amazon Rekognition provides the following non-storage API operations for images:

- [DetectLabels](../APIReference/API_DetectLabels.md "../APIReference/API_DetectLabels.md")
- [DetectFaces](../APIReference/API_DetectFaces.md "../APIReference/API_DetectFaces.md")
- [CompareFaces](../APIReference/API_CompareFaces.md "../APIReference/API_CompareFaces.md")
- [DetectModerationLabels](../APIReference/API_DetectModerationLabels.md "../APIReference/API_DetectModerationLabels.md")
- [DetectProtectiveEquipment](../APIReference/API_DetectProtectiveEquipment.md "../APIReference/API_DetectProtectiveEquipment.md")
- [RecognizeCelebrities](../APIReference/API_RecognizeCelebrities.md "../APIReference/API_RecognizeCelebrities.md")
- [DetectText](../APIReference/API_DetectText.md "../APIReference/API_DetectText.md")
- [GetCelebrityInfo](../APIReference/API_GetCelebrityInfo.md "../APIReference/API_GetCelebrityInfo.md")

Amazon Rekognition provides the following non-storage API operations for videos:

- [StartLabelDetection](../APIReference/API_StartlabelDetection.md "../APIReference/API_StartlabelDetection.md")
- [StartFaceDetection](../APIReference/API_StartFaceDetection.md "../APIReference/API_StartFaceDetection.md")
- [StartPersonTracking](../APIReference/API_StartPersonTracking.md "../APIReference/API_StartPersonTracking.md")
- [StartCelebrityRecognition](../APIReference/API_StartCelebrityRecognition.md "../APIReference/API_StartCelebrityRecognition.md")
- [StartContentModeration](../APIReference/API_StartContentModeration.md "../APIReference/API_StartContentModeration.md")

These are referred to as _non-storage_ API operations because
when you make the operation call, Amazon Rekognition does not persist any information
discovered about the input image. Like all other Amazon Rekognition API operations, no input
image bytes are persisted by non-storage API operations.

The following example scenarios show where you might integrate non-storage API
operations in your application. These scenarios assume that you have a local
repository of images.

###### Example 1: An application that finds images in your local repository that contain

specific labels

First, you detect labels (objects and concepts) using the Amazon Rekognition
`DetectLabels` operation in each of the images in your repository
and build a client-side index, as shown following:

```
Label        ImageID

tree          image-1
flower        image-1
mountain      image-1
tulip         image-2
flower        image-2
apple         image-3

```

Then, your application can search this index to find images in your local
repository that contain a specific label. For example, display images that
contain a tree.

Each label that Amazon Rekognition detects has a confidence value associated. It
indicates the level of confidence that the input image contains that label. You
can use this confidence value to optionally perform additional client-side
filtering on labels depending on your application requirements about the level
of confidence in the detection. For example, if you require precise labels, you
might filter and choose only the labels with higher confidence (such as 95% or
higher). If your application doesn't require higher confidence value, you might
choose to filter labels with lower confidence value (closer to 50%).

###### Example 2: An application to display enhanced face images

First, you can detect faces in each of the images in your local repository
using the Amazon Rekognition `DetectFaces` operation and build a client-side
index. For each face, the operation returns metadata that includes a bounding
box, facial landmarks (for example, the position of mouth and ear), and facial
attributes (for example, gender). You can store this metadata in a client-side
local index, as shown following:

```
ImageID     FaceID     FaceMetaData

image-1     face-1     <boundingbox>, etc.
image-1     face-2     <boundingbox>, etc.
image-1     face-3     <boundingbox>, etc.
...

```

In this index, the primary key is a combination of both the
`ImageID` and `FaceID`.

Then, you can use the information in the index to enhance the images when your
application displays them from your local repository. For example, you might add
a bounding box around the face or highlight facial features.

 

## Storage-based API operations

Amazon Rekognition Image supports the [IndexFaces](../APIReference/API_IndexFaces.md "../APIReference/API_IndexFaces.md")
operation, which you can use to detect faces in an image and persist information
about facial features detected in an Amazon Rekognition collection. This is an example of a
_storage-based_ API operation because the service persists
information on the server.

Amazon Rekognition Image provides the following storage API operations:

- [IndexFaces](../APIReference/API_IndexFaces.md "../APIReference/API_IndexFaces.md")
- [ListFaces](../APIReference/API_ListFaces.md "../APIReference/API_ListFaces.md")
- [SearchFacesByImage](../APIReference/API_SearchFacesByImage.md "../APIReference/API_SearchFacesByImage.md")
- [SearchFaces](../APIReference/API_SearchFaces.md "../APIReference/API_SearchFaces.md")
- [DeleteFaces](../APIReference/API_DeleteFaces.md "../APIReference/API_DeleteFaces.md")
- [DescribeCollection](../APIReference/API_DescribeCollection.md "../APIReference/API_DescribeCollection.md")
- [DeleteCollection](../APIReference/API_DeleteCollection.md "../APIReference/API_DeleteCollection.md")
- [ListCollections](../APIReference/API_ListCollections.md "../APIReference/API_ListCollections.md")
- [CreateCollection](../APIReference/API_CreateCollection.md "../APIReference/API_CreateCollection.md")

Amazon Rekognition Video provides the following storage API operations:

- [StartFaceSearch](../APIReference/API_StartFaceSearch.md "../APIReference/API_StartFaceSearch.md")
- [CreateStreamProcessor](../APIReference/API_CreateStreamProcessor.md "../APIReference/API_CreateStreamProcessor.md")

To store facial information, you must first create a face collection in one of the
AWS Regions in your account. You specify this face collection when you call the
`IndexFaces` operation. After you create a face collection and store
facial feature information for all faces, you can search the collection for face
matches. For example, you can detect the largest face in an image and search for
matching faces in a collection by calling `searchFacesByImage.`

Facial information stored in collections by `IndexFaces` is accessible
to Amazon Rekognition Video operations. For example, you can search a video for persons whose faces
match those in an existing collection by calling [StartFaceSearch](../APIReference/API_StartFaceSearch.md "../APIReference/API_StartFaceSearch.md").

For information about creating and managing collections, see [Searching faces in a collection](collections.md "collections.md").

###### Note

Collections store face vectors, which are mathematical representations of
faces. Collections do not store images of faces.

###### Example 1: An application that authenticates access to a building

You start by creating a face collection to store scanned badge images using
the `IndexFaces` operation, which extracts faces and stores them as
searchable image vectors. Then, when an employee enters the building, an image
of the employee's face is captured and sent to the
`SearchFacesByImage` operation. If the face match produces a
sufficiently high similarity score (say 99%), you can authenticate the
employee.
