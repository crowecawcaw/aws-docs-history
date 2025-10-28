# Creating an index

You can create an index using the console, or by calling the [CreateIndex](../APIReference/API_CreateIndex.md "../APIReference/API_CreateIndex.md") API. You can
use the AWS Command Line Interface (AWS CLI) or SDK with the API. After you created
your index, you can add documents directly to it or from a data source.

To create an index, you must provide the Amazon Resource Name (ARN) of an AWS Identity and Access Management (IAM) role for indexes to access CloudWatch. For
more information, see [IAM roles for
indexes](iam-roles.md#iam-roles-index "iam-roles.md#iam-roles-index").

The following tabs provide a procedure for creating an index by using the AWS Management Console, and
code examples for using the AWS CLI, and Python and Java SDKs.

Console

###### To create an index

1. Sign in to the AWS Management Console and open the
   Amazon Kendra console at [https://console.aws.amazon.com/kendra/](https://console.aws.amazon.com/kendra/ "https://console.aws.amazon.com/kendra/").
2. Select **Create index** in the
   **Indexes** section.
3. In **Specify index details**, give your index a name
   and a description.
4. In **IAM role** provide an IAM role. To find a role, choose from roles in your account
   that contain the word "kendra" or enter the name of another role. For
   more information about the permissions that the role requires, see
   [IAM roles for indexes](iam-roles.md#iam-roles-index "iam-roles.md#iam-roles-index").
5. Choose **Next**.
6. On the **Configure user access control** page, choose
   **Next**. You can update your index to use tokens
   for access control after you create an index. For more information, see
   [Controlling
   access to documents](create-index-access-control.md "create-index-access-control.md").
7. On the **Provisioning details** page, choose
   **Create**.
8. It might take some time for the index to create. Check the list of
   indexes to watch the progress of creating your index. When the status of
   the index is `ACTIVE`, your index is ready to use.

AWS CLI

###### To create an index

1. Use the following command to create an index. The
   `role-arn` must be the Amazon Resource Name (ARN) of an
   IAM role that can run Amazon Kendra actions. For
   more information, see [IAM
   roles](iam-roles.md "iam-roles.md").

The command is formatted for Linux and macOS. If you are using
Windows, replace the Unix line continuation character (\) with a caret
(^).

```
aws kendra create-index \
 --name `index name` \
 --description "`index description`" \
 --role-arn arn:aws:iam::`account ID`:role/`role name`

```

2. It might take some time for the index to create. To check the state of
   your index, use the index ID returned by `create-index` with
   the following command. When the status of the index is
   `ACTIVE`, your index is ready to use.

```
aws kendra describe-index \
 --index-id `index ID`

```

Python

###### To create an index

- Provide values for the following variables in the code example that
  follows:
  - `description`—A description of the index
    that you're creating. This is optional.
  - `index_name`—The name of the index that
    you're creating.
  - `role_arn`—The Amazon Resource Name (ARN) of
    a role that can run Amazon Kendra APIs. For more
    information, see [IAM
    roles](iam-roles.md "iam-roles.md").

```
import boto3
from botocore.exceptions import ClientError
import pprint
import time

kendra = boto3.client("kendra")

print("Create an index.")

# Provide a name for the index
index_name = "index-name"
# Provide an optional description for the index
description = "index description"
# Provide the IAM role ARN required for indexes
role_arn = "arn:aws:iam::${account id}:role/${role name}"

try:
    index_response = kendra.create_index(
        Name = index_name,
        Description = description,
        RoleArn = role_arn
    )

    pprint.pprint(index_response)

    index_id = index_response["Id"]

    print("Wait for Amazon Kendra to create the index.")

    while True:
        # Get the details of the index, such as the status
        index_description = kendra.describe_index(
            Id = index_id
        )
        # If status is not CREATING, then quit
        status = index_description["Status"]
        print(" Creating index. Status: "+status)
        if status != "CREATING":
            break
        time.sleep(60)

except  ClientError as e:
        print("%s" % e)

print("Program ends.")
```

Java

###### To create an index

- Provide values for the following variables in the code example that
  follows:
  - `description`—A description of the index
    that you're creating. This is optional.
  - `index_name`—The name of the index that
    you're creating.
  - `role_arn`—The Amazon Resource Name (ARN) of
    a role that can run Amazon Kendra APIs. For more
    information, see [IAM
    roles](iam-roles.md "iam-roles.md").

```
package com.amazonaws.kendra;

import java.util.concurrent.TimeUnit;
import software.amazon.awssdk.services.kendra.KendraClient;
import software.amazon.awssdk.services.kendra.model.CreateIndexRequest;
import software.amazon.awssdk.services.kendra.model.CreateIndexResponse;
import software.amazon.awssdk.services.kendra.model.DescribeIndexRequest;
import software.amazon.awssdk.services.kendra.model.DescribeIndexResponse;
import software.amazon.awssdk.services.kendra.model.IndexStatus;


public class CreateIndexExample {

    public static void main(String[] args) throws InterruptedException {

        String indexDescription = "Getting started index for Kendra";
        String indexName = "java-getting-started-index";
        String indexRoleArn = "arn:aws:iam::<your AWS account ID>:role/KendraRoleForGettingStartedIndex";

        System.out.println(String.format("Creating an index named %s", indexName));
        CreateIndexRequest createIndexRequest = CreateIndexRequest
            .builder()
            .description(indexDescription)
            .name(indexName)
            .roleArn(indexRoleArn)
            .build();
        KendraClient kendra = KendraClient.builder().build();
        CreateIndexResponse createIndexResponse = kendra.createIndex(createIndexRequest);
        System.out.println(String.format("Index response %s", createIndexResponse));

        String indexId = createIndexResponse.id();

        System.out.println(String.format("Waiting until the index with ID %s is created.", indexId));
        while (true) {
            DescribeIndexRequest describeIndexRequest = DescribeIndexRequest.builder().id(indexId).build();
            DescribeIndexResponse describeIndexResponse = kendra.describeIndex(describeIndexRequest);
            IndexStatus status = describeIndexResponse.status();
            if (status != IndexStatus.CREATING) {
                break;
            }

            TimeUnit.SECONDS.sleep(60);
        }

        System.out.println("Index creation is complete.");
    }
}

```

After you created your index, you add documents to it. You can add them directly or create
a data source that updates your index on a regular schedule.

###### Topics

- [Adding documents directly to an index with batch
  upload](in-adding-documents.md "in-adding-documents.md")
- [Adding frequently asked questions (FAQs) to an
  index](in-creating-faq.md "in-creating-faq.md")
- [Creating custom document fields](custom-attributes.md "custom-attributes.md")
- [Controlling user access to documents with
  tokens](create-index-access-control.md "create-index-access-control.md")
