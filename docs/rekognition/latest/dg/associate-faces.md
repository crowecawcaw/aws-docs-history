# Associating faces to a user

You can use the [AssociateFaces](../APIReference/API_AssociatingFaces.md "../APIReference/API_AssociatingFaces.md") operation to associate multiple individual faces with a
single user. In order to associate a face with a user, you must first create a
collection and a user. Note that the face vectors must reside in the same collection
where the user vector resides.

###### To associate faces (SDK)

1. If you haven't already:
   1. Create or update a user with `AmazonRekognitionFullAccess`
      permissions. For more information, see [Step 1: Set up an AWS account and create a
      User](setting-up.md#setting-up-iam "setting-up.md#setting-up-iam").
   2. Install and configure the AWS CLI and the AWS SDKs. For more
      information, see [Step 2: Set up the AWS CLI and AWS SDKs](setup-awscli-sdk.md "setup-awscli-sdk.md").

2. Use the following examples to call the `AssociateFaces`
   operation.

Java
This Java code example associates a face with a user.

```
import java.util.Arrays;
import java.util.List;

import com.amazonaws.services.rekognition.AmazonRekognition;
import com.amazonaws.services.rekognition.AmazonRekognitionClientBuilder;
import com.amazonaws.services.rekognition.model.AssociateFacesRequest;
import com.amazonaws.services.rekognition.model.AssociateFacesResult;


public class AssociateFaces {

    public static void main(String[] args) throws Exception {


        AmazonRekognition rekognitionClient = AmazonRekognitionClientBuilder.defaultClient();

        /* Replace the below configurations to allow you successfully run the example

           @collectionId: The collection where user and faces are stored
           @userId: The user which faces will get associated to
           @faceIds: The list of face IDs that will get associated to the given user
           @userMatchThreshold: Minimum User match confidence required for the face to
                               be associated with a User that has at least one faceID already associated
         */

        String collectionId = "MyCollection";
        String userId = "demoUser";
        String faceId1 = "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx";
        String faceId2 = "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx";
        List<String> faceIds = Arrays.asList(faceid1,faceid2);

        float userMatchThreshold = 0f;
        System.out.println("Associating faces to the existing user: " +
                userId);

        AssociateFacesRequest request = new AssociateFacesRequest()
                .withCollectionId(collectionId)
                .withUserId(userId)
                .withFaceIds(faceIds)
                .withUserMatchThreshold(userMatchThreshold);

        AssociateFacesResult result = rekognitionClient.associateFaces(request);

        System.out.println("Successful face associations: " + result.getAssociatedFaces().size());
        System.out.println("Unsuccessful face associations: " + result.getUnsuccessfulFaceAssociations().size());
    }

}
```

AWS CLI
This AWS CLI command associates a face with a user, using the
`associate-faces` CLI operation.

```
aws rekognition associate-faces --user-id `user-id` --face-ids `face-id-1` `face-id-2`
--collection-id `collection-name`
--region `region-name`
```

Python
This Python code example associates a face with a user.

```
from botocore.exceptions import ClientError
import boto3
import logging

logger = logging.getLogger(__name__)
session = boto3.Session(profile_name='profile-name')
client = session.client('rekognition')

def associate_faces(collection_id, user_id, face_ids):
    """
    Associate stored faces within collection to the given user

    :param collection_id: The ID of the collection where user and faces are stored.
    :param user_id: The ID of the user that we want to associate faces to
    :param face_ids: The list of face IDs to be associated to the given user

    :return: response of AssociateFaces API
    """
    logger.info(f'Associating faces to user: {user_id}, {face_ids}')
    try:
        response = client.associate_faces(
            CollectionId=collection_id,
            UserId=user_id,
            FaceIds=face_ids
        )
        print(f'- associated {len(response["AssociatedFaces"])} faces')
    except ClientError:
        logger.exception("Failed to associate faces to the given user")
        raise
    else:
        print(response)
        return response

def main():
    face_ids = ["faceId1", "faceId2"]
    collection_id = "collection-id"
    user_id = "user-id"
    associate_faces(collection_id, user_id, face_ids)

if __name__ == "__main__":
    main()
```

## AssociateFaces operation

response

The response for `AssociateFaces` includes the `UserStatus`,
which is the status of the disassociation request, as well as a list of
`FaceIds` to be associated. A list of
`UnsuccessfulFaceAssociations` is also returned. After submitting a
request to `AssociateFaces`, the operation may take a minute or so to
complete.

For this reason, the UserStatus is returned, which can have the following values:

- CREATED - Denotes that the ‘User’ is created successfully and no faces are
  associated to it currently. ‘User’ will be in this state before any
  successful ‘AssociateFaces’ call is made.
- UPDATING - Denotes that the ‘User’ is being updated to reflect the newly
  associated/disassociated faces and will become ACTIVE in few seconds. Search
  results may contain ‘User’ in this state and customers can choose to ignore
  them from the returned results.
- ACTIVE - Denotes that the **‘**User**’** is updated to reflect all
  associated/disassociated faces and is in a searchable state.

```
{
    "UnsuccessfulFaceAssociations": [
        {
            "Reasons": [
                "LOW_MATCH_CONFIDENCE"
            ],
            "FaceId": "f5817d37-94f6-0000-bfee-1a2b3c4d5e6f",
            "Confidence": 0.9375374913215637
        },
        {
            "Reasons": [
                "ASSOCIATED_TO_A_DIFFERENT_IDENTITY"
            ],
            "FaceId": "851cb847-dccc-1111-bfee-1a2b3c4d5e6f",
            "UserId": "demoUser2"
        }
    ],
    "UserStatus": "UPDATING",
    "AssociatedFaces": [
        {
            "FaceId": "35ebbb41-7f67-2222-bfee-1a2b3c4d5e6f"
        }
    ]
}

```
