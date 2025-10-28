# Use `DisassociateFaces` with an AWS SDK or CLI

The following code examples show how to use `DisassociateFaces`.

CLI

**AWS CLI**

```
aws rekognition disassociate-faces --face-ids list-of-face-ids
  --user-id user-id --collection-id collection-name --region region-name


```

- For API details, see
  [DisassociateFaces](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rekognition/disassociate-faces.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rekognition/disassociate-faces.html")
  in _AWS CLI Command Reference_.

Python

**SDK for Python (Boto3)**

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

- For API details, see
  [DisassociateFaces](../../../goto/boto3/rekognition-2016-06-27/DisassociateFaces.md "../../../goto/boto3/rekognition-2016-06-27/DisassociateFaces.md")
  in _AWS SDK for Python (Boto3) API Reference_.

For a complete list of AWS SDK developer guides and code examples, see
[Using Rekognition with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
