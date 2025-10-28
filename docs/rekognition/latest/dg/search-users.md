# Searching for users (face ID/ user ID)

You can use the [SearchUsers](../APIReference/API_SearchUsers.md "../APIReference/API_SearchUsers.md")
operation to to search for users in a specified collection that match a supplied face ID
or user ID. The operation lists the returned `UserIds` ranked by the highest
similarity score above the requested UserMatchThreshold. The user ID is created in the
CreateUsers operation. For more information, see [Managing users in a collection](managing-face-collections.md#collections-manage-users "managing-face-collections.md#collections-manage-users").

###### To search users (SDK)

1. If you haven't already:
   1. Create or update a user with `AmazonRekognitionFullAccess`
      permissions. For more information, see [Step 1: Set up an AWS account and create a
      User](setting-up.md#setting-up-iam "setting-up.md#setting-up-iam").
   2. Install and configure the AWS CLI and the AWS SDKs. For more
      information, see [Step 2: Set up the AWS CLI and AWS SDKs](setup-awscli-sdk.md "setup-awscli-sdk.md").

2. Use the following examples to call the `SearchUsers`
   operation.

Java
This Java example searchers the users in a collection using the
`SearchUsers` operation.

```
import com.amazonaws.services.rekognition.AmazonRekognition;
import com.amazonaws.services.rekognition.AmazonRekognitionClientBuilder;
import com.amazonaws.services.rekognition.model.UserMatch;
import com.amazonaws.services.rekognition.model.SearchUsersRequest;
import com.amazonaws.services.rekognition.model.SearchUsersResult;
import com.amazonaws.services.rekognition.model.UserMatch;

public class SearchUsers {
    //Replace collectionId and faceId with the values you want to use.

    public static final String collectionId = "MyCollection";
    public static final String faceId = "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx";

    public static final String userd = 'demo-user';

    public static void main(String[] args) throws Exception {

        AmazonRekognition rekognitionClient = AmazonRekognitionClientBuilder.defaultClient();

        // Search collection for faces matching the user id.
        SearchUsersRequest request = new SearchUsersRequest()
                .withCollectionId(collectionId)
                .withUserId(userId);

        SearchUsersResult result =
                rekognitionClient.searchUsers(request);

        System.out.println("Printing first search result with matched user and similarity score");
        for (UserMatch match: result.getUserMatches()) {
            System.out.println(match.getUser().getUserId() + " with similarity score " + match.getSimilarity());
        }

        // Search collection for faces matching the face id.
        SearchUsersRequest request1 = new SearchUsersRequest()
                .withCollectionId(collectionId)
                .withFaceId(faceId);

        SearchUsersResult result1 =
                rekognitionClient.searchUsers(request1);

        System.out.println("Printing second search result with matched user and similarity score");
        for (UserMatch match: result1.getUserMatches()) {
            System.out.println(match.getUser().getUserId() + " with similarity score " + match.getSimilarity());
        }
    }

```

AWS CLI
This AWS CLI command searches the users in a collection with the
`SearchUsers` operation.

```
aws rekognition search-users --face-id `face-id` --collection-id `collection-id` --region `region-name`
```

Python
The following example searches the users in a collection with the
`SearchUsers` operation.

```
# Copyright 2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.
# PDX-License-Identifier: MIT-0 (For details, see https://github.com/awsdocs/amazon-rekognition-developer-guide/blob/master/LICENSE-SAMPLECODE.)

import boto3
from botocore.exceptions import ClientError
import logging

logger = logging.getLogger(__name__)
session = boto3.Session(profile_name='profile-name')
client = session.client('rekognition')

def search_users_by_face_id(collection_id, face_id):
    """
    SearchUsers operation with face ID provided as the search source

    :param collection_id: The ID of the collection where user and faces are stored.
    :param face_id: The ID of the face in the collection to search for.

    :return: response of SearchUsers API
    """
    logger.info(f'Searching for users using a face-id: {face_id}')
    try:
        response = client.search_users(
            CollectionId=collection_id,
            FaceId=face_id
        )
        print(f'- found {len(response["UserMatches"])} matches')
        print([f'- {x["User"]["UserId"]} - {x["Similarity"]}%' for x in response["UserMatches"]])
    except ClientError:
        logger.exception(f'Failed to perform SearchUsers with given face id: {face_id}')
        raise
    else:
        print(response)
        return response

def search_users_by_user_id(collection_id, user_id):
    """
    SearchUsers operation with user ID provided as the search source

    :param collection_id: The ID of the collection where user and faces are stored.
    :param user_id: The ID of the user in the collection to search for.

    :return: response of SearchUsers API
    """
    logger.info(f'Searching for users using a user-id: {user_id}')
    try:
        response = client.search_users(
            CollectionId=collection_id,
            UserId=user_id
        )
        print(f'- found {len(response["UserMatches"])} matches')
        print([f'- {x["User"]["UserId"]} - {x["Similarity"]}%' for x in response["UserMatches"]])
    except ClientError:
        logger.exception(f'Failed to perform SearchUsers with given face id: {user_id}')
        raise
    else:
        print(response)
        return response

def main():
    collection_id = "collection-id"
    user_id = "user-id"
    face_id = "face_id"
    search_users_by_face_id(collection_id, face_id)
    search_users_by_user_id(collection_id, user_id)

if __name__ == "__main__":
    main()
```

## SearchUsers operation request

Given a FaceID or UserID, SearchUsers searches the specified CollectionID for user
matches. By default, SearchUsers returns UserIDs for which the similarity score is
greater than 80%. The similarity indicates how closely the UserID matches the
provided FaceID or UserID. If multiple UserIDs are returned, they are listed in
order of highest similarity score to lowest. Optionally, you can use the
UserMatchThreshold to specify a different value. For more information, see [Managing users in a collection](managing-face-collections.md#collections-manage-users "managing-face-collections.md#collections-manage-users").

The following is an example of a SearchUsers request using
`UserId`:

```

{
   "CollectionId": "MyCollection",
   "UserId": "demoUser1",
   "MaxUsers": 2,
   "UserMatchThreshold": 99
}

```

The following is an example of a SearchUsers request using
`FaceId`:

```

{
    "CollectionId": "MyCollection",
    "FaceId": "bff43c40-cfa7-4b94-bed8-8a08b2205107",
    "MaxUsers": 2,
    "UserMatchThreshold": 99
}

```

## SearchUsers operation response

If searching with a `FaceId`, the response for SearchUsers includes the
`FaceId` for the `SearchedFace`, as well as a list of
`UserMatches` and the `UserId` and `UserStatus`
for each User.

```

{
    "SearchedFace": {
        "FaceId": "bff43c40-cfa7-4b94-bed8-8a08b2205107"
    },
    "UserMatches": [
        {
            "User": {
                "UserId": "demoUser1",
                "UserStatus": "ACTIVE"
            },
            "Similarity": 100.0
        },
        {
            "User": {
                "UserId": "demoUser2",
                "UserStatus": "ACTIVE"
            },
            "Similarity": 99.97946166992188
        }
    ],
    "FaceModelVersion": "6"
}


```

If searching with a `UserId`, the response for SearchUsers includes the
`UserId` for the `SearchedUser`, in addition to the other
response elements.

```

{
    "SearchedUser": {
        "UserId": "demoUser1"
    },
    "UserMatches": [
        {
            "User": {
                "UserId": "demoUser2",
                "UserStatus": "ACTIVE"
            },
            "Similarity": 99.97946166992188
        }
    ],
    "FaceModelVersion": "6"
}

```
