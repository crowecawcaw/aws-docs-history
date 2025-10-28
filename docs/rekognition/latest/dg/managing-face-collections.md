# Managing face collections, faces, and users

The face collection is the resource used by Amazon Rekognition for containing information
related to faces and users. You use various Rekognition API operations to manage the collection itself,
as well as any faces or face vectors stored in the collection.

## Managing a collection

The face collection is the primary Amazon Rekognition resource, and each face collection you
create has a unique Amazon Resource Name (ARN). You create each face collection in a
specific AWS Region in your account. When a collection is created, it's associated
with the most recent version of the face detection model. For more information, see
[Understanding model versioning](face-detection-model.md "face-detection-model.md").

You can perform the following management operations on a collection:

- Create a collection with [CreateCollection](../APIReference/API_CreateCollection.md "../APIReference/API_CreateCollection.md"). For more information, see [Creating a collection](create-collection-procedure.md "create-collection-procedure.md").
- List the available collections with [ListCollections](../APIReference/API_ListCollections.md "../APIReference/API_ListCollections.md"). For more information, see [Listing collections](list-collection-procedure.md "list-collection-procedure.md").
- Describe a collection with [DescribeCollection](../APIReference/API_DescribeCollection.md "../APIReference/API_DescribeCollection.md"). For more information, see [Describing a collection](describe-collection-procedure.md "describe-collection-procedure.md").
- Delete a collection with [DeleteCollection](../APIReference/API_DeleteCollection.md "../APIReference/API_DeleteCollection.md"). For more information, see [Deleting a collection](delete-collection-procedure.md "delete-collection-procedure.md").

## Managing faces in a collection

After you create a face collection, you can store faces in it. Amazon Rekognition provides the
following operations for managing faces in a collection:

- The [IndexFaces](../APIReference/API_IndexFaces.md "../APIReference/API_IndexFaces.md")
  operation detects faces in the input image (JPEG or PNG), and adds them to the
  specified face collection. A unique face ID is returned for each face that's
  detected in the image. After you persist faces, you can search the face
  collection for face matches. For more information, see [Adding faces to a collection](add-faces-to-collection-procedure.md "add-faces-to-collection-procedure.md").
- The [ListFaces](../APIReference/API_ListFaces.md "../APIReference/API_ListFaces.md")
  operation lists the faces in a collection. For more information, see [Adding faces to a collection](add-faces-to-collection-procedure.md "add-faces-to-collection-procedure.md").
- The [DeleteFaces](../APIReference/API_DeleteFaces.md "../APIReference/API_DeleteFaces.md") operation deletes faces from a collection. For more
  information, see [Deleting faces from a collection](delete-faces-procedure.md "delete-faces-procedure.md").

## Managing users in a collection

After you store multiple face vectors from the same person, you can improve accuracy
by associating all of those face vectors into one user vector. You can use the following
operations to manage your users:

- [CreateUser](../APIReference/API_CreateUser.md "../APIReference/API_CreateUser.md")

* Operation creates a new user in a collection with a provided unique user
  ID.

- [AssociateUsers](../APIReference/API_AssociateUsers.md "../APIReference/API_AssociateUsers.md") - Add 1 - 100 unique face IDs to a user ID. After
  you associate at least one face ID to a user, you can search for matches against
  that user in your collection.
- [ListUsers](../APIReference/API_ListUsers.md "../APIReference/API_ListUsers.md") -
  Lists the users in a collection.
- [DeleteUsers](../APIReference/API_DeleteUsers.md "../APIReference/API_DeleteUsers.md") - Deletes a user from a collection with the provided
  user ID.
- [DisassociateFaces](../APIReference/API_DisassociateFaces.md "../APIReference/API_DisassociateFaces.md") - Removes one or more face IDs from a
  user.
