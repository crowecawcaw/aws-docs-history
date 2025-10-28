# Disassociating faces from a user

You can use the [DisassociateFaces](../APIReference/API_DisassociateFaces.md "../APIReference/API_DisassociateFaces.md") operation to remove the association between a user ID and
a face ID.

###### To disassociate faces (SDK)

1. If you haven't already:
   1. Create or update a user with `AmazonRekognitionFullAccess`
      permissions. For more information, see [Step 1: Set up an AWS account and create a
      User](setting-up.md#setting-up-iam "setting-up.md#setting-up-iam").
   2. Install and configure the AWS CLI and the AWS SDKs. For more
      information, see [Step 2: Set up the AWS CLI and AWS SDKs](setup-awscli-sdk.md "setup-awscli-sdk.md").

2. Use the following examples to call the `DisassociateFaces`
   operation.

Java
This Java example removes the association between a FaceID and a
UserID with the `DisassociateFaces` operation.

```
import java.util.Arrays;
import java.util.List;

import com.amazonaws.services.rekognition.AmazonRekognition;
import com.amazonaws.services.rekognition.AmazonRekognitionClientBuilder;
import com.amazonaws.services.rekognition.model.DisassociateFacesRequest;
import com.amazonaws.services.rekognition.model.DisassociateFacesResult;


public class DisassociateFaces {

    public static void main(String[] args) throws Exception {


        AmazonRekognition rekognitionClient = AmazonRekognitionClientBuilder.defaultClient();

        /* Replace the below configurations to allow you successfully run the example

           @collectionId: The collection where user and faces are stored
           @userId: The user which faces will get disassociated from
           @faceIds: The list of face IDs that will get disassociated from the given user
         */

        String collectionId = "MyCollection";
        String userId = "demoUser";
        String faceId1 = "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx";
        String faceId2 = "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx";
        List<String> faceIds = Arrays.asList(faceid1,faceid2);

        System.out.println("Disassociating faces from existing user: " +
                userId);

        DisassociateFacesRequest request = new DisassociateFacesRequest()
                .withCollectionId(collectionId)
                .withUserId(userId)
                .withFaceIds(faceIds)

        DisassociateFacesResult result = rekognitionClient.disassociateFaces(request);

        System.out.println("Successful face disassociations: " + result.getDisassociatedFaces().size());
        System.out.println("Unsuccessful face disassociations: " + result.getUnsuccessfulFaceDisassociations().size());
    }

}
```

AWS CLI
This AWS CLI command removes the association between a FaceID and a
UserID with the `DisassociateFaces` operation.

```
aws rekognition disassociate-faces --face-ids `list-of-face-ids`
--user-id `user-id` --collection-id `collection-name` --region `region-name`
```

Python
The following example removes the association between a FaceID and
a UserID with the `DisassociateFaces` operation.

```
from botocore.exceptions import ClientError
import boto3
import logging

logger = logging.getLogger(__name__)
session = boto3.Session(profile_name='profile-name')
client = session.client('rekognition')

def disassociate_faces(collection_id, user_id, face_ids):
    """
    Disassociate stored faces within collection to the given user

    :param collection_id: The ID of the collection where user and faces are stored.
    :param user_id: The ID of the user that we want to disassociate faces from
    :param face_ids: The list of face IDs to be disassociated from the given user

    :return: response of AssociateFaces API
    """
    logger.info(f'Disssociating faces from user: {user_id}, {face_ids}')
    try:
        response = client.disassociate_faces(
            CollectionId=collection_id,
            UserId=user_id,
            FaceIds=face_ids
        )
        print(f'- disassociated {len(response["DisassociatedFaces"])} faces')
    except ClientError:
        logger.exception("Failed to disassociate faces from the given user")
        raise
    else:
        print(response)
        return response

def main():
    face_ids = ["faceId1", "faceId2"]
    collection_id = "collection-id"
    user_id = "user-id"
    disassociate_faces(collection_id, user_id, face_ids)

if __name__ == "__main__":
    main()
```

## DisassociateFaces operation

response

The response for `DisassociateFaces` includes the
`UserStatus`, which is the status of the disassociation request, as
well as a list of `FaceIds` to be unassociated. A list of
`UnsuccessfulFaceDisassociations` is also returned. After submitting
a request to DisassociateFaces, the operation may take a minute or so to complete.
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
    "UserStatus": "UPDATING",
    "DisassociatedFaces": [
        {
            "FaceId": "c92265d4-5f9c-43af-a58e-12be0ce02bc3"
        }
    ],
    "UnsuccessfulFaceDisassociations": [
        {
            "Reasons": [
                "ASSOCIATED_TO_A_DIFFERENT_IDENTITY"
            ],
            "FaceId": "f5817d37-94f6-4335-bfee-6cf79a3d806e",
            "UserId": "demoUser1"
        }
    ]
}
```
