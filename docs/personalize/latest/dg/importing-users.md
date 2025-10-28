# Importing users individually

After you complete [Creating a schema and a dataset](data-prep-creating-datasets.md "data-prep-creating-datasets.md") to create a Users dataset, you can individually import one or
more new users into the dataset. Individually importing users allows you to
keep your Users dataset current with small batch imports as your catalog grows. You can import
up to 10 users at a time. If you have a large
amount of new users, we recommend that you first import data in bulk and
then import user data individually as necessary. See [Importing bulk data into Amazon Personalize with a
dataset import job](bulk-data-import-step.md "bulk-data-import-step.md").

You can use the Amazon Personalize console, the AWS Command Line Interface (AWS CLI), or AWS SDKs to
import users. If you import a user with the same `userId` as a
user that's already in your Users dataset, Amazon Personalize replaces the user with the
new one. You can import up to 10 users at a time.

For information about how Amazon Personalize updates filters for new records and how
new records influence recommendations, see [Importing individual records into an Amazon Personalize dataset](incremental-data-updates.md "incremental-data-updates.md").

###### Topics

- [Importing users individually
  (console)](#importing-users-console "#importing-users-console")
- [Importing users individually
  (AWS CLI)](#importing-users-cli "#importing-users-cli")
- [Importing users individually
  (AWS SDKs)](#importing-users-sdk "#importing-users-sdk")

## Importing users individually

(console)

You can import up to 10 users at a time. This procedure assumes you
have already created a Users dataset. For information about creating
datasets, see [Creating a schema and a dataset](data-prep-creating-datasets.md "data-prep-creating-datasets.md").

###### To import users individually (console)

1. Open the Amazon Personalize console at [https://console.aws.amazon.com/personalize/home](https://console.aws.amazon.com/personalize/home "https://console.aws.amazon.com/personalize/home") and sign in to your
   account.
2. On the **Dataset groups** page, choose the
   dataset group with the Users dataset that you want to import the user
   to.
3. In the navigation pane, choose **Datasets**.
4. On the **Datasets** page, choose the Users
   dataset.
5. On the dataset details page, at the top right, choose
   **Modify dataset** and choose **Create
   record**.
6. On the **Create user record(s)** page, for record
   input, enter the user details in JSON format. The user's field names
   and values must match the schema you used when you created the Users
   dataset. Amazon Personalize provides a JSON template with field names and data
   types from this schema.
7. Choose **Create record(s)**. In
   **Response**, the result of the import is listed
   and a success or failure message is displayed.

## Importing users individually

(AWS CLI)

Add one or more users to your Users dataset with the [PutUsers](API_UBS_PutUsers.md "API_UBS_PutUsers.md") operation.
You can import up to 10 users with a single `PutUsers` call.
This section assumes that you have already created an Users dataset. For
information about creating datasets, see [Creating a schema and a dataset](data-prep-creating-datasets.md "data-prep-creating-datasets.md").

Use the following `put-users` command to add one or more
users with the AWS CLI. Replace `dataset arn` with the Amazon
Resource Name (ARN) of your dataset and `user Id` with the ID
of the user. If an user with the same `userId` is already in
your Users dataset, Amazon Personalize replaces it with the new one.

For `properties`, for each field in your Users dataset,
replace the `propertyName` with the field name from your schema
in camel case. For example, GENDER would be `gender` and
MEMBERSHIP_TYPE would be `membershipType`. Replace `user
 data` with the data for the user. For categorical string data, to
include multiple categories for a single property, separate each category
with a pipe (`|`). For example `\"Premium Class|Legacy
 Member\"`.

```
aws personalize-events put-users \
  --dataset-arn `dataset arn` \
  --users '[{
      "userId": "`user Id`",
      "properties": "{\"`propertyName`\": "\`user data`\"}"
    },
    {
      "userId": "`user Id`",
      "properties": "{\"`propertyName`\": "\`user data`\"}"
    }]'
```

## Importing users individually

(AWS SDKs)

Add one or more users to your Users dataset with the [PutUsers](API_UBS_PutUsers.md "API_UBS_PutUsers.md") operation.
If a user with the same
`userId` is already in your Users dataset, Amazon Personalize
replaces it with the new one. You can import up to 10 users with a single `PutUsers` call.
This section assumes that you have already created a Users dataset. For
information about creating datasets, see [Creating a schema and a dataset](data-prep-creating-datasets.md "data-prep-creating-datasets.md").

The following code shows how to add one or more users to your Users
dataset. For each property name parameter, pass the field name from your
schema in camel case. For example, GENDER would be
`gender` and MEMBERSHIP_TYPE would be
`membershipType`. For each property value parameter,
pass the data for the user.

For categorical string data, to include
multiple categories for a single property separate each category
with a pipe (`|`). For example `"Premium
 class|Legacy Member"`.

SDK for Python (Boto3)

```
import boto3

personalize_events = boto3.client(service_name='personalize-events')

personalize_events.put_users(
    datasetArn = '`dataset arn`',
    users = [{
      'userId': '`user ID`',
      'properties': "{\"`propertyName`\": \"`user data`\"}"
      },
      {
      'userId': '`user ID`',
      'properties': "{\"`propertyName`\": \"`user data`\"}"
      }]
)
```

SDK for Java 2.x

```
public static int putUsers(PersonalizeEventsClient personalizeEventsClient,
                         String datasetArn,
                         String user1Id,
                         String user1PropertyName,
                         String user1PropertyValue,
                         String user2Id,
                         String user2PropertyName,
                         String user2PropertyValue) {

    int responseCode = 0;
    ArrayList<User> users = new ArrayList<>();

    try {
        User user1 = User.builder()
          .userId(user1Id)
          .properties(String.format("{\"%1$s\": \"%2$s\"}", user1PropertyName, user1PropertyValue))
          .build();

        users.add(user1);

        User user2 = User.builder()
          .userId(user2Id)
          .properties(String.format("{\"%1$s\": \"%2$s\"}", user2PropertyName, user2PropertyValue))
          .build();

        users.add(user2);

        PutUsersRequest putUsersRequest = PutUsersRequest.builder()
          .datasetArn(datasetArn)
          .build();

        responseCode = personalizeEventsClient.putUsers(putUsersRequest).sdkHttpResponse().statusCode();
        System.out.println("Response code: " + responseCode);
        return responseCode;

    } catch (PersonalizeEventsException e) {
        System.out.println(e.awsErrorDetails().errorMessage());
    }
    return responseCode;
}
```

SDK for JavaScript v3

```
import {
  PutUsersCommand,
  PersonalizeEventsClient,
} from "@aws-sdk/client-personalize-events";

const personalizeEventsClient = new PersonalizeEventsClient({
  region: "`REGION`",
});

// set the put users parameters
var putUsersParam = {
  datasetArn:
    "`DATASET ARN`",
  users: [
    {
      userId: "`userId`",
      properties: '{"`column1Name`": "`value`", "`column2Name`": "`value`"}',
    },
    {
      userId: "`userId`",
      properties: '{"`column1Name`": "`value`", "`column2Name`": "`value`"}',
    },
  ],
};
export const run = async () => {
  try {
    const response = await personalizeEventsClient.send(
      new PutUsersCommand(putUsersParam)
    );
    console.log("Success!", response);
    return response; // For unit tests.
  } catch (err) {
    console.log("Error", err);
  }
};
run();
```
