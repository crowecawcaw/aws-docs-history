# Using list management

Amazon SES offers list management capabilities, which means customers can manage their own
mailing lists, known as contact lists. A _contact list_ is a list that
allows you to store all of your contacts that have subscribed to a particular topic or
topics. A _contact_ is an end-user who is receiving your emails. A
_topic_ is an interest group, theme, or label within a list. Lists
can have multiple topics.

By using the [`ListContacts`](../APIReference-V2/API_ListContacts.md "../APIReference-V2/API_ListContacts.md") operation in the Amazon SES API v2, you can retrieve a
list of all your contacts who have subscribed to a particular topic, to whom you can send
emails using the [`SendEmail`](../APIReference-V2/API_SendEmail.md "../APIReference-V2/API_SendEmail.md") operation.

For information about subscription management, see [Using subscription
management](sending-email-subscription-management.md "sending-email-subscription-management.md").

## List management overview

You should consider the following factors when you use list management:

- You can specify list topics while creating the list.
- Only one contact list is allowed per AWS account.
- A list can have a maximum of 20 topics.
- You can update an existing contact list, including adding new topics to the
  list, adding or deleting contacts from a list, and updating contact preferences
  for a list or topic.
- You can update topic metadata, such as the topic display name or
  description.
- You can get a list of contacts in a contact list, contacts subscribed to a
  topic, contacts unsubscribed from a topic, and contacts unsubscribed from all
  topics in the list.
- You can import your existing contact lists to SES using the [`CreateImportJob`](../APIReference-V2/API_CreateImportJob.md "../APIReference-V2/API_CreateImportJob.md") API.
- SES will issue a bounce event for a message that is sent to an
  unsubscribed contact on your contact list. For more information, see [Using subscription
  management](sending-email-subscription-management.md "sending-email-subscription-management.md").
- Each contact can have associated attributes which you can use to store
  information about that contact.

## Configuring list management

You can use the following operations to configure list management capabilities. For
the full list of contact list and contact operations, see the [Amazon SES API v2
Reference](../APIReference-V2/Welcome.md "../APIReference-V2/Welcome.md").

### Create a contact

list

You can use the [`CreateContactList`](../APIReference-V2/API_CreateContactList.md "../APIReference-V2/API_CreateContactList.md") operation in the SES API v2
to create a contact list. You can quickly and easily configure this setting by using
the AWS CLI. For more information about installing and configuring the AWS CLI, see the
[AWS Command Line Interface User Guide](../../../cli/latest/userguide.md "../../../cli/latest/userguide.md").

###### To create a contact list by using the AWS CLI

- At the command line, enter the following command:

```
aws sesv2 create-contact-list --cli-input-json file://`CONTACT-LIST-JSON`
```

In the preceding command, replace
`CONTACT-LIST-JSON` with the path to your JSON
file for your [`CreateContactList`](../APIReference-V2/API_CreateContactList.md "../APIReference-V2/API_CreateContactList.md") request.

An example `CreateContactList` input JSON file for the request
is as follows:

```
{
    "ContactListName": "ExampleContactListName",
    "Description": "Creating a contact list example",
    "Topics": [
     {
         "TopicName": "Sports",
         "DisplayName": "Sports Newsletter",
         "Description": "Sign up for our free newsletter to receive updates on all sports.",
         "DefaultSubscriptionStatus": "OPT_OUT"
     },
     {
         "TopicName": "Cycling",
         "DisplayName": "Cycling newsletter",
         "Description": "Never miss a cycling update by subscribing to our newsletter.",
         "DefaultSubscriptionStatus": "OPT_IN"
     },
     {
         "TopicName": "NewProducts",
         "DisplayName": "New products",
         "Description": "Hear about new products by subscribing to this mailing list.",
         "DefaultSubscriptionStatus": "OPT_IN"
     },
     {
         "TopicName": "DailyUpdates",
         "DisplayName": "Daily updates",
         "Description": "Start your day with sport updates, Monday through Friday.",
         "DefaultSubscriptionStatus": "OPT_OUT"
     }
    ]
}
```

### Create a contact

You can use the [`CreateContact`](../APIReference-V2/API_CreateContact.md "../APIReference-V2/API_CreateContact.md") operation in the SES API v2 to
create a contact. You can quickly and easily configure this setting by using the
AWS CLI. For more information about installing and configuring the AWS CLI, see the
[AWS Command Line Interface User Guide](../../../cli/latest/userguide.md "../../../cli/latest/userguide.md").

###### To create a contact by using the AWS CLI

- At the command line, enter the following command:

```
aws sesv2 create-contact --cli-input-json file://`CONTACT-JSON`
```

In the preceding command, replace `CONTACT-JSON`
with the path to your JSON file for your [`CreateContact`](../APIReference-V2/API_CreateContact.md "../APIReference-V2/API_CreateContact.md") request.

An example `CreateContact` input JSON file for the request is
as follows:

```
{
    "ContactListName": "ExampleContactListName",
    "EmailAddress": "example@amazon.com",
    "UnsubscribeAll": false,
    "TopicPreferences": [
        {
            "TopicName": "Sports",
            "SubscriptionStatus": "OPT_IN"
        }
    ],
    "AttributesData": "{\"Name\": \"John\", \"Location\": \"Seattle\"}"
}
```

In the example above, an `UnsubscribeAll` value of
`false` shows that the contact has not unsubscribed from all
topics, where a value of `true` would mean the contact has
unsubscribed from all topics.

`TopicPreferences` includes information about the contact’s
subscription status to topics. In the preceding example, the contact has
opted in to the "_Sports_" topic and will receive all
emails to the "_Sports_" topic.

The `AttributesData` is a JSON field where you can put any
metadata about our contact. It must be a valid JSON object.

### Bulk importing contacts to

your contact list

You can manually add addresses in bulk by first uploading your contacts into an
Amazon S3 object followed by using the [`CreateImportJob`](../APIReference-V2/API_CreateImportJob.md "../APIReference-V2/API_CreateImportJob.md") operation in the SES API v2 or
by using the SES console. For more information see [Adding
email addresses in bulk to your account-level suppression list](sending-email-suppression-list.md#sending-email-suppression-list-manual-add-bulk "sending-email-suppression-list.md#sending-email-suppression-list-manual-add-bulk").

You should create a contact list before importing your contacts.

###### Note

You can add up to 1 million contacts to a contact list per ImportJob.

To add contacts in bulk to your contact list, complete the following steps.

- Upload your contacts into an Amazon S3 object in either CSV or JSON
  format.

**CSV format**

The first line of the file that is uploaded to Amazon S3 should be a header
line.

The `topicPreferences` object needs to be flattened for the CSV
format. Every topic in the `topicPreferences` will have a
separate header field.

CSV format example for adding contacts in bulk to a contact list:

```

emailAddress,unsubscribeAll,attributesData,topicPreferences.Sports,topicPreferences.Cycling
example1@amazon.com,false,{"Name": "John"},OPT_IN,OPT_OUT
example2@amazon.com,true,,OPT_OUT,OPT_OUT

```

**JSON format**

Only newline-delimited JSON files are supported. In this format, each line
is a complete JSON object that contains one contact's information.

JSON format example for adding contacts in bulk to a contact list:

```
{
     "emailAddress": "example1@amazon.com",
     "unsubscribeAll": false,
     "attributesData": "{\"Name\":\"John\"}",
     "topicPreferences": [
      {
          "topicName": "Sports",
          "subscriptionStatus": "OPT_IN"
      },
      {
          "topicName": "Cycling",
          "subscriptionStatus": "OPT_OUT"
      }
     ]
}
{
     "emailAddress": "example2@amazon.com",
     "unsubscribeAll": true,
     "topicPreferences": [
      {
          "topicName": "Sports",
          "subscriptionStatus": "OPT_OUT"
      },
      {
          "topicName": "Cycling",
          "subscriptionStatus": "OPT_OUT"
      }
     ]
}


```

In the preceding examples, replace
`example1@amazon.com` and
`example2@amazon.com` with the email addresses
you want to add to the contact list. Replace the `attributesData`
values with the values specific to the contact. Additionally, replace
`Sports` and `Cycling`
with the `topicName` that applies to your contact. The acceptable
`topicPreferences` are `OPT_IN` and
`OPT_OUT`.

The following attributes are supported when uploading your contacts into
an Amazon S3 object in either CSV or JSON format:

| Attribute          | Description                                                                                |
| ------------------ | ------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `emailAddress`     | The contact's email address. This is a mandatory field.                                    |
| `unsubscribeAll`   | A boolean value status noting if the contact is unsubscribed from all contact list topics. |
| `topicPreferences` | The contact's preferences for being opted-in to or opted-out of topics.                    |
| `attributesData`   | The attribute data attached to a contact.                                                  | <br>• Give SES permission to read the Amazon S3 object. When applied to an Amazon S3 bucket, the following policy gives SES permission to read that bucket. For more information about attaching policies to Amazon S3 buckets, see [Using Bucket Policies and User Policies](../../../AmazonS3/latest/userguide/using-iam-policies.md "../../../AmazonS3/latest/userguide/using-iam-policies.md") in the _Amazon Simple Storage Service User Guide_. <br>• Give SES permission to use your AWS KMS key. If the Amazon S3 object is encrypted with an AWS KMS key, you need to give Amazon SES permission to use the KMS key. SES can only attain permission from a customer managed key, not a default KMS key. You must give SES permission to use the customer managed key by adding a statement to the key's policy. Paste the following policy statement into the key policy to permit SES to use your customer managed key. `{ "Sid": "AllowSESToDecrypt", "Effect": "Allow", "Principal": { "Service":"ses.amazonaws.com" }, "Action": [ "kms:Decrypt", ], "Resource": "*" }` <br>• Use the [`CreateImportJob`](../APIReference-V2/API_CreateImportJob.md "../APIReference-V2/API_CreateImportJob.md") operation in the SES API v2. ###### Note The following example assumes that you've already installed the AWS CLI. For more information about installing and configuring the AWS CLI, see the [AWS Command Line Interface User Guide](../../../cli/latest/userguide.md "../../../cli/latest/userguide.md"). At the command line, enter the following command. Replace `s3bucket` withe the name of the Amazon S3 bucket and `s3object` with the name of the Amazon S3 object name. `aws sesv2 create-import-job --import-destination ContactListDestination={ContactListName=ExampleContactListName,ContactListImportAction=PUT} --import-data-source S3Url="s3://s3bucket/s3object",DataFormat=CSV` ## List management walkthrough with examples The following walkthrough provides examples of how you can use list management to list your contacts, utilize `ListManagementOptions` to specify a contact list and topic name in your email, and how to insert unsubscribe links. 1. List contacts by using the AWS CLI – You can use the [`ListContacts`](../APIReference-V2/API_ListContacts.md "../APIReference-V2/API_ListContacts.md") operation to retrieve a list of all your contacts who have subscribed to a particular topic, in conjunction with the [`SendEmail`](../APIReference-V2/API_SendEmail.md "../APIReference-V2/API_SendEmail.md") operation, which allows you to send them emails. At the command line, enter the following command: `` aws sesv2 list-contacts --cli-input-json file://`LIST-CONTACTS-JSON` `` In the preceding command, replace `LIST-CONTACTS-JSON` with the path to your JSON file for your [`ListContacts`](../APIReference-V2/API_ListContacts.md "../APIReference-V2/API_ListContacts.md") request. An example `ListContacts` input JSON file for the request is as follows: `{ "ContactListName": "ExampleContactListName", "Filter": { "FilteredStatus": "OPT_IN", "TopicFilter": { "TopicName": "Cycling", "UseDefaultIfPreferenceUnavailable": true } }, "PageSize": 50 }` The `FilteredStatus` shows the subscription status for which you want to filter, which is either `OPT_IN` or `OPT_OUT`. The `TopicFilter` is an optional filter which specifies which topic you want results for, and in the example above, that is "_Cycling_." `UseDefaultIfPreferenceUnavailable` can have a value of `true` or `false`. If `true`, the topic default preference will be used if the contact doesn’t have any explicit preference for a topic. If `false`, only contacts with an explicitly set preference are considered for filtering. 2. Send mail with `ListManagementOptions` enabled – After listing the contacts in your list using the above [`ListContacts`](../APIReference-V2/API_ListContacts.md "../APIReference-V2/API_ListContacts.md") operation, you can use the [`SendEmail`](../APIReference-V2/API_SendEmail.md "../APIReference-V2/API_SendEmail.md") operation to send emails to each of your contacts by utilizing the [`ListManagementOptions`](../APIReference-V2/API_ListManagementOptions.md "../APIReference-V2/API_ListManagementOptions.md") header to specify your contact list and topic name. To use `ListManagementOptions` with the `SendEmail` operation, include the [`contactListName`](../APIReference-V2/API_ListManagementOptions.md "../APIReference-V2/API_ListManagementOptions.md") and [`topicName`](../APIReference-V2/API_ListManagementOptions.md "../APIReference-V2/API_ListManagementOptions.md") to which the email belongs (the `topicName` is optional): `ListManagementOptions: String contactListName String topicName` If you include `ListManagementOptions` in your `SendEmail` request to a recipient email address that is not on your contact list, then a contact will be created on your list automatically. SES will issue a bounce event for a message that is sent to an unsubscribed contact on your contact list, which means you won’t need to update your `SendEmail` requests to avoid sending to contacts who have unsubscribed. 3. Indicate the location for your unsubscribe links – When utilizing [`ListManagementOptions`](../APIReference-V2/API_ListManagementOptions.md "../APIReference-V2/API_ListManagementOptions.md") you have the option to enable SES to add unsubscribe footer links in your email using the `{{amazonSESUnsubscribeUrl}}` placeholder to specify where SES needs to insert the unsubscribe URL. Placeholder replacement is supported only for HTML and TEXT content types. You can include the placeholder two times maximum. If used more than two times, only the first two occurrences are replaced. For more information, see [Using subscription management](sending-email-subscription-management.md "sending-email-subscription-management.md"). Alternatively, if you're using the SMTP interface to send email, you can use the `X-SES-LIST-MANAGEMENT-OPTIONS` header to specify a list and topic name. To specify a list and topic name while sending email using the SMTP interface, add the following email header to your message: `X-SES-LIST-MANAGEMENT-OPTIONS: {contactListName}; topic={topicName}` |
