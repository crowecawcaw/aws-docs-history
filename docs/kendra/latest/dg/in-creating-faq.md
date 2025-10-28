# Adding frequently asked questions (FAQs) to an

index

###### Note

Feature support varies by index type and search API being used. To see if this
feature is supported for the index type and search API you’re using, see [Index
types](hiw-index-types.md "hiw-index-types.md").

You can add frequently asked questions (FAQs) directly to your index using the console
or the [CreateFaq](../APIReference/API_CreateFaq.md "../APIReference/API_CreateFaq.md") API. Adding FAQs to an index is an asynchronous operation. You
put the data for the FAQ in a file that you store in an Amazon Simple Storage Service bucket.
You can use CSV or JSON files as input for your FAQ:

- Basic CSV—A CSV file where each row contains a question, answer, and an
  optional source URI.
- Custom CSV—A CSV file that contains questions, answers, and headers for
  custom fields/attributes that you can use to facet, display, or sort FAQ
  responses. You can also define access control fields to limit the FAQ response
  to certain users and groups that are allowed to see the FAQ response.
- JSON—A JSON file that contains questions, answers, and custom
  fields/attributes that you can use to facet, display, or sort FAQ responses. You
  can also define access control fields to limit the FAQ response to certain users
  and groups that are allowed to see the FAQ response.
  For example, the following is a basic CSV file that provides answers to questions
  about free clinics in Spokane, Washington USA and Mountain View, Missouri, USA.

```
How many free clinics are in Spokane WA?, 13
How many free clinics are there in Mountain View Missouri?, 7
```

###### Note

The FAQ file must be a UTF-8-encoded file.

###### Topics

- [Creating index fields for an FAQ file](#in-custom-fields-faq "#in-custom-fields-faq")
- [Basic CSV file](#faq-basic-csv "#faq-basic-csv")
- [Custom CSV file](#faq-custom-csv "#faq-custom-csv")
- [JSON file](#faq-custom-json "#faq-custom-json")
- [Using your FAQ file](#using-faq-file "#using-faq-file")
- [FAQ files in languages other than English](#faq-languages "#faq-languages")

## Creating index fields for an FAQ file

###### Note

Feature support varies by index type and search API being used. To see if this
feature is supported for the index type and search API you’re using, see [Index
types](hiw-index-types.md "hiw-index-types.md").

When you use a [custom CSV](in-creating-faq.md#faq-custom-csv "in-creating-faq.md#faq-custom-csv") or [JSON](in-creating-faq.md#faq-custom-json "in-creating-faq.md#faq-custom-json") file for input, you can declare custom fields for your FAQ
questions. For example, you can create a custom field that assigns each FAQ question
a business department. When the FAQ is returned in a response, you can use the
department as a facet to narrow the search to "HR" or "Finance" only, for
example.

A custom field must map to an index field. In the console, you use the
**Facet definition** page to create an index field. When using
the API, you must first create an index field using the [UpdateIndex](../APIReference/API_UpdateIndex.md "../APIReference/API_UpdateIndex.md")
API.

The field/attribute type in the FAQ file must match the type of the associated
index field. For example, the "Department" field is a `STRING_LIST` type
field. So, you must provide values for the department field as a string list in your
FAQ file. You can check the type of index fields using the **Facet
definition** page in the console or by using the [DescribeIndex](../APIReference/API_DescribeIndex.md "../APIReference/API_DescribeIndex.md") API.

When you create an index field that maps to a custom attribute, you can mark it
displayable, facetable, or sortable. You can't make a custom attribute
searchable.

In addition to the custom attributes, you can also use the Amazon Kendra
reserved or common fields in a custom CSV or JSON file. For more information, see
[Document attributes or fields](hiw-document-attributes.md "hiw-document-attributes.md").

## Basic CSV file

Use a basic CSV file when you want to use a simple structure for your FAQs. In a
basic CSV file, each row has two or three fields: a question, an answer, and an
optional source URI that points to a document with more information.

The contents of the file must follow the [RFC 4180 Common Format and MIME Type
for Comma-Separated Values (CSV) Files](https://tools.ietf.org/html/rfc4180 "https://tools.ietf.org/html/rfc4180").

The following is a FAQ file in the basic CSV format.

```
How many free clinics are in Spokane WA?, 13, https://s3.region.company.com/bucket-name/directory/faq.csv
How many free clinics are there in Mountain View Missouri?, 7, https://s3.region.company.com/bucket-name/directory/faq.csv
```

## Custom CSV file

Use a custom CSV file when you want to add custom fields/attributes to your FAQ
questions. For a custom CSV file, you use a header row in your CSV file to define
the additional attributes.

The CSV file must contain the following two required fields:

- `_question`—The frequently asked question
- `_answer`—The answer to the frequently asked
  question

Your custom CSV file can contain both Amazon Kendra reserved fields (except
`_faq_id`, `_data_source_id`,
`_document_title`, and `_file_type`) and any custom fields.

The following is an example of a custom CSV file.

```
_question,_answer,_last_updated_at,custom_string
How many free clinics are in Spokane WA?, 13, 2012-03-25T12:30:10+01:00, Note: Some free clinics require you to meet certain criteria in order to use their services
How many free clinics are there in Mountain View Missouri?, 7, 2012-03-25T12:30:10+01:00, Note: Some free clinics require you to meet certain criteria in order to use their services
```

The contents of the custom file must follow the [RFC 4180 Common Format and MIME Type
for Comma-Separated Values (CSV) Files](https://tools.ietf.org/html/rfc4180 "https://tools.ietf.org/html/rfc4180").

The following lists the types of custom fields:

- Date—ISO 8601-encoded date and time values.

For example, 2012-03-25T12:30:10+01:00 is the ISO 8601 date-time format
for March 25, 2012, at 12:30PM (plus 10 seconds) in the Central European
Time time zone.

- Long—Numbers, such as `1234`.
- String—String values. If your string contains commas, enclose the
  entire value in double quotation marks (") (for example, `"custom
attribute, and more"`).
- String list—A list of string values. List the values in a
  comma-separated list that's enclosed in quotation marks (") (for example,
  `"item1, item2, item3"`). If the list contains only a single
  entry, you can omit the quotation marks (for example,
  `item1`).

A custom CSV file can contain user access control fields. You can use these fields
to limit access to the FAQ to certain users and groups. To filter on user context,
the user must provide user and group information in the query. Otherwise, all
relevant FAQs are returned. For more information, see [User context
filtering](user-context-filter.md "user-context-filter.md").

There following lists the user context filters for FAQs:

- `_acl_user_allow`—Users in the allow list can see the
  FAQ in the query response. The FAQ isn't returned to other users.
- `_acl_user_deny`—Users in the deny list can't see the
  FAQ in the query response. The FAQ is returned to all other users when it's
  relevant to the query.
- `_acl_group_allow`—Users that are members of an allowed
  group can see the FAQ in the query response. The FAQ isn't returned to users
  that are members of another group.
- `_acl_group_deny`—Users that are members of a denied
  group can't see the FAQ in the query response. The FAQ is returned to other
  groups when it's relevant to the query.

Provide the values for the allow and deny lists in comma-separated lists enclosed
in quotation marks (for example, `"user1,user2,user3"`). You can include
a user or a group in either an allow list or a deny list, but not both where the
same user is individually allowed but also group denied. If you include a user or
group in both, you receive an error.

The following is an example of a custom CSV file with user context
information.

```
_question, _answer, _acl_user_allow, _acl_user_deny, _acl_group_allow, _acl_group_deny
How many free clinics are in Spokane WA?, 13, "userID6201,userID7552", "userID1001,userID2020", groupBasicPlusRate, groupPremiumRate
```

## JSON file

You can use a JSON file to provide questions, answers, and fields for your index.
You can add any of the Amazon Kendra reserved fields or custom fields to the
FAQ.

The following is the schema for the JSON file.

```
{
    "SchemaVersion": 1,
    "FaqDocuments": [
        {
            "Question": string,
            "Answer": string,
            "Attributes": {
                string: object
                additional attributes
            },
            "AccessControlList": [
               {
                   "Name": string,
                   "Type": enum( "GROUP" | "USER" ),
                   "Access": enum( "ALLOW" | "DENY" )
               },
               `additional user context`
            ]
        },
        `additional FAQ documents`
    ]
}
```

The following example JSON file shows two FAQ documents. One of the documents has
the required question and answer only. The other document also includes additional
field and user context or access control information.

```
{
    "SchemaVersion": 1,
    "FaqDocuments": [
        {
            "Question": "How many free clinics are in Spokane WA?",
            "Answer": "13"
        },
        {
            "Question": "How many free clinics are there in Mountain View Missouri?",
            "Answer": "7",
            "Attributes": {
                "_source_uri": "https://s3.region.company.com/bucket-name/directory/faq.csv",
                "_category": "Charitable Clinics"
            },
            "AccessControlList": [
               {
                   "Name": "user@amazon.com",
                   "Type": "USER",
                   "Access": "ALLOW"
               },
               {
                   "Name": "Admin",
                   "Type": "GROUP",
                   "Access": "ALLOW"
               }
            ]
        }
    ]
}
```

The following lists the types of custom fields:

- Date—A JSON string value with ISO 8601-encoded date and time
  values. For example, 2012-03-25T12:30:10+01:00 is the ISO 8601 date-time
  format for March 25, 2012, at 12:30PM (plus 10 seconds) in the Central
  European Time time zone.
- Long—A JSON number value, such as `1234`.
- String—A JSON string value (for example, `"custom
attribute"`).
- String list—A JSON array of string values (for example,
  `["item1,item2,item3"]`).

A JSON file can contain user access control fields. You can use these fields to
limit access to the FAQ to certain users and groups. To filter on user context, the
user must provide user and group information in the query. Otherwise, all relevant
FAQs are returned. For more information, see [User context
filtering](user-context-filter.md "user-context-filter.md").

You can include a user or a group in either an allow list or a deny list, but not
both where the same user is individually allowed but also group denied. If you
include a user or group in both, you receive an error.

The following is an example of including user access control to a JSON FAQ.

```
"AccessControlList": [
                {
                    "Name": "group or user name",
                    "Type": "GROUP | USER",
                    "Access": "ALLOW | DENY"
                },
                `additional user context`
            ]

```

## Using your FAQ file

After you store your FAQ input file in an S3 bucket, you use the console or the
`CreateFaq` API to put the questions and answers into your index. If
you want to update a FAQ, delete the FAQ and create it again. You use the
`DeleteFaq` API to delete a FAQ.

You must provide an IAM role that has access to the S3 bucket that
contains your source files. You specify the role in the console or in the
`RoleArn` parameter. The following is an example of adding a FAQ file
to an index.

Python

```
import boto3

kendra = boto3.client("kendra")

# Provide the index ID
index_id = "index-id"
# Provide the IAM role ARN required to index documents in an S3 bucket
role_arn = "arn:aws:iam::${accountId}:role/${roleName}"

# Provide the S3 bucket path information to the FAQ file
faq_path = {
    "Bucket": "bucket-name",
    "Key": "FreeClinicsUSA.csv"
}

response = kendra.create_faq(
    S3Path =  faq_path,
    Name = "FreeClinicsUSA",
    IndexId = index_id,
    RoleArn = role_arn
)

print(response)
```

Java

```
package com.amazonaws.kendra;

import software.amazon.awssdk.services.kendra.KendraClient;
import software.amazon.awssdk.services.kendra.model.CreateFaqRequest;
import software.amazon.awssdk.services.kendra.model.CreateFaqResponse;
import software.amazon.awssdk.services.kendra.model.S3Path;

public class AddFaqExample {
    public static void main(String[] args) {
        KendraClient kendra = KendraClient.builder().build();

        String indexId = "yourIndexId";
        String roleArn = "your role for accessing S3 files";

        CreateFaqRequest createFaqRequest = CreateFaqRequest
            .builder()
            .indexId(indexId)
            .name("FreeClinicsUSA")
            .roleArn(roleArn)
            .s3Path(
                S3Path
                    .builder()
                    .bucket("amzn-s3-demo-bucket")
                    .key("FreeClinicsUSA.csv")
                    .build())
            .build();

        CreateFaqResponse response = kendra.createFaq(createFaqRequest);

        System.out.println(String.format("The result of creating FAQ: %s", response));

    }
}
```

## FAQ files in languages other than English

You can index a FAQ in a supported language. Amazon Kendra indexes FAQs in
English by default if you don't specify a language. You specify the language code
when you call the [CreateFaq](../APIReference/API_CreateFaq.md "../APIReference/API_CreateFaq.md") operation
or you can include the language code for a FAQ in the FAQ metadata as a field. If a
FAQ doesn't have a language code in its metadata specified in a metadata field, the
FAQ is indexed using the language code specified when you call the
`CreateFAQ` operation. To index a FAQ document in a supported
language in the console, go to **FAQs** and select **Add
FAQ**. You choose a language from the dropdown
**Language**.
