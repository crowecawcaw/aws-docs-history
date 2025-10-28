# Searching for faces and users within a

collection

After you create a face collection and store face vectors and/or user vectors, you can
search a face collection for face matches. With Amazon Rekognition, you can search for faces in a
collection that match:

- A supplied face ID ([SearchFaces](../APIReference/API_SearchFaces.md "../APIReference/API_SearchFaces.md")). For more information, see [Searching for a face with a face
  ID](search-face-with-id-procedure.md "search-face-with-id-procedure.md").
- The largest face in a supplied image ([SearchFacesByImage](../APIReference/API_SearchFacesByImage.md "../APIReference/API_SearchFacesByImage.md")). For more information, see [Searching for a face with an
  image](search-face-with-image-procedure.md "search-face-with-image-procedure.md").
- Faces in a stored video. For more information, see [Searching stored videos for
  faces](procedure-person-search-videos.md "procedure-person-search-videos.md").
- Faces in a streaming video. For more information, see [Working with streaming video events](streaming-video.md "streaming-video.md").
  You can use the `CompareFaces` operation to compare a face in a source
  image with faces in the target image. The scope of this comparison is limited to the
  faces that are detected in the target image. For more information, see [Comparing faces in images](faces-comparefaces.md "faces-comparefaces.md").

The various Search operations seen in the following list compare a face (identified
either by a `FaceId` or an input image) with all faces stored in a given face
collection:

- [SearchFaces](../APIReference/API_SearchFaces.md "../APIReference/API_SearchFaces.md")
- [SearchFacesByImage](../APIReference/API_SearchFacesByImage.md "../APIReference/API_SearchFacesByImage.md")
- [SearchUsers](../APIReference/API_SearchUsers.md "../APIReference/API_SearchUsers.md")
- [SearchUsersByImage](../APIReference/API_SearchUsersByImage.md "../APIReference/API_SearchUsersByImage.md")
