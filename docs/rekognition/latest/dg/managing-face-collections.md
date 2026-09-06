

# Managing face collections, faces, and users
<a name="managing-face-collections"></a>

 The face collection is the resource used by Amazon Rekognition for containing information related to faces and users. You use various Rekognition API operations to manage the collection itself, as well as any faces or face vectors stored in the collection. 

## Managing a collection
<a name="managing-collections"></a>

The face collection is the primary Amazon Rekognition resource, and each face collection you create has a unique Amazon Resource Name (ARN). You create each face collection in a specific AWS Region in your account. When a collection is created, it's associated with the most recent version of the face detection model. For more information, see [Understanding model versioning](face-detection-model.md). 

You can perform the following management operations on a collection:
+ Create a collection with [CreateCollection](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_CreateCollection.html). For more information, see [Creating a collection](create-collection-procedure.md).
+ List the available collections with [ListCollections](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_ListCollections.html). For more information, see [Listing collections](list-collection-procedure.md).
+ Describe a collection with [DescribeCollection](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_DescribeCollection.html). For more information, see [Describing a collection](describe-collection-procedure.md).
+ Delete a collection with [DeleteCollection](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_DeleteCollection.html). For more information, see [Deleting a collection](delete-collection-procedure.md).

## Managing faces in a collection
<a name="collections-index-faces"></a>

After you create a face collection, you can store faces in it. Amazon Rekognition provides the following operations for managing faces in a collection:
+  The [IndexFaces](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_IndexFaces.html) operation detects faces in the input image (JPEG or PNG), and adds them to the specified face collection. A unique face ID is returned for each face that's detected in the image. After you persist faces, you can search the face collection for face matches. For more information, see [Adding faces to a collection](add-faces-to-collection-procedure.md).
+ The [ListFaces](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_ListFaces.html) operation lists the faces in a collection. For more information, see [Adding faces to a collection](add-faces-to-collection-procedure.md).
+ The [DeleteFaces](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_DeleteFaces.html) operation deletes faces from a collection. For more information, see [Deleting faces from a collection](delete-faces-procedure.md).

## Managing users in a collection
<a name="collections-manage-users"></a>

After you store multiple face vectors from the same person, you can improve accuracy by associating all of those face vectors into one user vector. You can use the following operations to manage your users:
+ [CreateUser](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_CreateUser.html) - Operation creates a new user in a collection with a provided unique user ID.
+ [AssociateUsers](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_AssociateUsers.html) - Add 1 - 100 unique face IDs to a user ID. After you associate at least one face ID to a user, you can search for matches against that user in your collection.
+ [ListUsers](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_ListUsers.html) - Lists the users in a collection.
+ [DeleteUsers](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_DeleteUsers.html) - Deletes a user from a collection with the provided user ID.
+ [DisassociateFaces](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_DisassociateFaces.html) - Removes one or more face IDs from a user.