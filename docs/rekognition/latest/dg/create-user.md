# Creating a user

You can use the [CreateUser](../APIReference/API_CreateUser.md "../APIReference/API_CreateUser.md")
operation to create a new user in a collection using a unique user ID you provide. You
can then associate multiple faces with the newly created user.

###### To create a user (SDK)

1. If you haven't already:
   1. Create or update an IAM user account with
      `AmazonRekognitionFullAccess` permissions. For more
      information, see [Step 1: Set up an AWS account and create a
      User](setting-up.md#setting-up-iam "setting-up.md#setting-up-iam").
   2. Install and configure the AWS CLI and the AWS SDKs. For more
      information, see [Step 2: Set up the AWS CLI and AWS SDKs](setup-awscli-sdk.md "setup-awscli-sdk.md").

2. Use the following examples to call the `CreateUser`
   operation.

Java
This Java code example creates a user.

```
import com.amazonaws.services.rekognition.AmazonRekognition;
import com.amazonaws.services.rekognition.AmazonRekognitionClientBuilder;
import com.amazonaws.services.rekognition.model.CreateUserRequest;
import com.amazonaws.services.rekognition.model.CreateUserResult;


public class CreateUser {

    public static void main(String[] args) throws Exception {


        AmazonRekognition rekognitionClient = AmazonRekognitionClientBuilder.defaultClient();

        //Replace collectionId and userId with the name of the user that you want to create in that target collection.

        String collectionId = "MyCollection";
        String userId = "demoUser";
        System.out.println("Creating new user: " +
                userId);

        CreateUserRequest request = new CreateUserRequest()
                .withCollectionId(collectionId)
                .withUserId(userId);

        rekognitionClient.createUser(request);
    }

}
```

AWS CLI
This AWS CLI command creates a user, using the
`create-user` CLI operation.

```
aws rekognition create-user --user-id `user-id` --collection-id `collection-name` --region `region-name`
--client-request-token `request-token`
```

Python
This Python code example creates a user.

```
# Copyright 2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.
# PDX-License-Identifier: MIT-0 (For details, see https://github.com/awsdocs/amazon-rekognition-developer-guide/blob/master/LICENSE-SAMPLECODE.)

import boto3
from botocore.exceptions import ClientError
import logging

logger = logging.getLogger(__name__)
session = boto3.Session(profile_name='profile-name')
client = session.client('rekognition')

def create_user(collection_id, user_id):
    """
    Creates a new User within a collection specified by CollectionId.
    Takes UserId as a parameter, which is a user provided ID which
    should be unique within the collection.

    :param collection_id: The ID of the collection where the indexed faces will be stored at.
    :param user_id: ID for the UserID to be created. This ID needs to be unique within the collection.

    :return: The indexFaces response
    """
    try:
        logger.info(f'Creating user: {collection_id}, {user_id}')
        client.create_user(
            CollectionId=collection_id,
            UserId=user_id
        )
    except ClientError:
        logger.exception(f'Failed to create user with given user id: {user_id}')
        raise

def main():
    collection_id = "collection-id"
    user_id = "user-id"
    create_user(collection_id, user_id)

if __name__ == "__main__":
    main()
```

Go
This Go code example uses the AWS Go SDK V2 and it creates a user.

```

package main

import (
	"context"
	"fmt"
	"log"

	"github.com/aws/aws-sdk-go-v2/aws"
	"github.com/aws/aws-sdk-go-v2/config"
	"github.com/aws/aws-sdk-go-v2/service/rekognition"
)

func main() {
	// Load the AWS SDK configuration
	cfg, err := config.LoadDefaultConfig(context.TODO(), config.WithRegion("us-west-2"))
	if err != nil {
		log.Fatalf("Failed to load configuration: %v", err)
	}

	// Create a Rekognition client
	client := rekognition.NewFromConfig(cfg)

	// Set up the input parameters
	input := &rekognition.CreateUserInput{
		CollectionId: aws.String("my-new-collection"), // Replace with your collection ID
		UserId:       aws.String("user12345678910"),   // Replace with desired user ID
	}

	// Call the CreateUser operation
	result, err := client.CreateUser(context.TODO(), input)
	if err != nil {
		log.Fatalf("Failed to create user: %v", err)
	}

	// Print out the results
	fmt.Printf("User created successfully:\n")

}


```
