# Preparing user metadata for training

The user data that you can import into Amazon Personalize includes numerical data, such as user age, and categorical metadata, such as gender
or loyalty membership. You import metadata about your users into an Amazon Personalize _Users dataset_.

Depending on your domain use case or custom recipe, user metadata can help Amazon Personalize recommend more relevant items to users
or recommend more meaningful user segments. And after training, it can help your model recommend items for users without any interactions
data. For more information about what use cases or recipes use user metadata, see the data requirements for your domain use
case or recipe in [Matching your use case to Amazon Personalize resources](use-cases-and-recipes.md "use-cases-and-recipes.md").

When training, Amazon Personalize doesn't use non-categorical string user data, such as user's names, keywords about the user, or tags.
However, importing this data can still enhance recommendations. For more information, see [Non-categorical string data](#user-string-data "#user-string-data").

For all domain use cases and custom recipes, your bulk user data must be in a CSV file. Each row in the file should represent a unique user.
After you finish preparing your data, you are ready to create a schema JSON file. This file tells Amazon Personalize about the
structure of your data. For more information, see [Creating schema JSON files for Amazon Personalize schemas](how-it-works-dataset-schema.md "how-it-works-dataset-schema.md").

The following sections provide more information on how to prepare your user data for Amazon Personalize. For
bulk data format guidelines for all types of data, see [bulk data format guidelines](preparing-training-data.md#general-formatting-guidelines "preparing-training-data.md#general-formatting-guidelines")

###### Topics

- [User data requirements](#user-data-requirements "#user-data-requirements")
- [Categorical metadata](#user-categorical-data "#user-categorical-data")
- [Non-categorical string data](#user-string-data "#user-string-data")
- [Users metadata example](#users-data-example "#users-data-example")

## User data requirements

The following are user data
requirements for Amazon Personalize. You are free to add additional custom columns depending on your use case and your data.

- Your data must have an USER_ID column that stores the unique identifier for each user. Every user must have an user ID. It
  must be a `string` with a max length of 256 characters.
- Your data must have least one categorical string or numerical metadata column. User metadata columns can include empty/null values for some users.
  We recommend that these columns be at minimum 70 percent complete.
- The maximum number of metadata columns is 25.

If you aren't sure you have enough data or if you have questions about its quality, you can import your data into an
Amazon Personalize dataset and use Amazon Personalize to analyze it. For more information, see [Analyzing quality and quantity of data in Amazon Personalize datasets](analyzing-data.md "analyzing-data.md").

## Categorical metadata

With some recipes and all domain use cases, Amazon Personalize uses categorical metadata, such as a user's gender, interests, or membership status, when identifying underlying patterns that
reveal the most relevant items for your users. You define your own range of values based on your use case. Categorical metadata can be in any language.

For users with multiple categories, separate each value with the
vertical bar, '|'. For example, for an INTERESTS field, your data for a user
might be `Movies|TV Shows|Music`.

With all recipes and domains, you can import categorical metadata and use it to filter recommendations based on a user's attributes.
For information about filtering recommendations see [Filtering recommendations and user segments](filter.md "filter.md").

Categorical values can have at most 1000 characters. If you have a user with a categorical
value with more than 1000 characters, your dataset import job will fail.

## Non-categorical string data

Except for user IDs, Amazon Personalize doesn't use non-categorical string data when training, such as user's names, keywords about the user, or tags.
However, Amazon Personalize can use it when filtering recommendations. You can create filters to include or remove items from
recommendations based on non-categorical string data about the user you are getting recommendations for (the CurrentUser). For more
information about filters, see [Filtering recommendations and user segments](filter.md "filter.md"). Non-categorical values can have a maximum of
1000 characters.

## Users metadata example

The first few lines of user metadata in a CSV file might look like the following.

```
USER_ID,AGE,GENDER,INTEREST
5,34,Male,hiking
6,56,Female,music
8,65,Male,movies|TV shows|music
...
...
```

The `USER_ID` column is required and stores unique identifiers for each individual user. The
`AGE` column is numerical metadata. The `GENDER` and `INTEREST` columns store categorical metadata for each user.

After you finish preparing your data, you are ready to create a schema JSON file. This file tells Amazon Personalize about the
structure of your data. For more information, see [Creating schema JSON files for Amazon Personalize schemas](how-it-works-dataset-schema.md "how-it-works-dataset-schema.md").
This is what the schema JSON file would look like for
the above sample data.

```
{
  "type": "record",
  "name": "Users",
  "namespace": "com.amazonaws.personalize.schema",
  "fields": [
      {
          "name": "USER_ID",
          "type": "string"
      },
      {
          "name": "AGE",
          "type": "int"
      },
      {
          "name": "GENDER",
          "type": "string",
          "categorical": true
      },
      {
          "name": "INTEREST",
          "type": "string",
          "categorical": true
      }
  ],
  "version": "1.0"
}
```
