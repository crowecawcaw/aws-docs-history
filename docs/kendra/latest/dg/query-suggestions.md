# Query suggestions

###### Note

Feature support varies by index type and search API being used. To see if this
feature is supported for the index type and search API you’re using, see [Index
types](hiw-index-types.md "hiw-index-types.md").

Amazon Kendra
_Query suggestions_ can help your users type their search queries
faster and guide their search.

Amazon Kendra suggests queries relevant to your users based on one of the
following:

- Popular queries in the query history or query log
- The contents of document fields/attributes
  You can set your preference for using the query history or document fields by setting
  `SuggestionTypes` as either
  `QUERY` or `DOCUMENT_ATTRIBUTES`
  and calling [GetQuerySuggestions](../APIReference/API_GetQuerySuggestions.md "../APIReference/API_GetQuerySuggestions.md"). By default, Amazon Kendra uses
  the query history to base suggestions on. If the query history and document fields are
  both activated when you call [UpdateQuerySuggestionsConfig](../APIReference/API_UpdateQuerySuggestionsConfig.md "../APIReference/API_UpdateQuerySuggestionsConfig.md") and you haven't set your
  `SuggestionTypes` preference to use document fields,
  then Amazon Kendra uses the query history.

If you use the console, you can base query suggestions on either the query history or
document fields. You first select your index and then select **Query
suggestions** under **Enrichments** in the navigation
menu. Then select **Configure query suggestions**. After you configure
query suggestions, you are directed to a search console where you can select either the
**Query history** or **Document fields** in the
right panel and enter a search query in the search bar.

By default, query suggestions using the query history and document fields are both
activated at no additional cost. You can deactivate these types of query suggestions at
any time by using the `UpdateQuerySuggestionsConfig` API. To
deactivate query suggestions based on the query history, set
`Mode` to `DISABLED` when
calling `UpdateQuerySuggestionsConfig`. To deactivate query
suggestions based on document fields, set
`AttributeSuggestionsMode` to
`INACTIVE` in the document fields configuration and
then call `UpdateQuerySuggestionsConfig>`. If you use the
console, you can deactivate query suggestions in the **Query suggestions
settings**.

Query suggestions are case insensitive. Amazon Kendra converts the query prefix
and the suggested query to lower case, ignores all single and double quotation marks,
and replaces multiple white space characters with a single space. Amazon Kendra
matches all other special characters as they are. Amazon Kendra does not show any
suggestions if a user types fewer than two characters or more than 60 characters.

###### Topics

- [Query suggestions using query
  history](#query-suggestions-history "#query-suggestions-history")
- [Query suggestions using document
  fields](#query-suggestions-doc-fields "#query-suggestions-doc-fields")
- [Block certain queries or document
  field content from suggestions](#query-suggestions-blocklist "#query-suggestions-blocklist")

## Query suggestions using query

history

###### Note

Feature support varies by index type and search API being used. To see if this
feature is supported for the index type and search API you’re using, see [Index
types](hiw-index-types.md "hiw-index-types.md").

###### Topics

- [Settings for selecting
  queries for suggestions](#query-suggestions-history-settings "#query-suggestions-history-settings")
- [Clear suggestions while
  retaining query history](#query-suggestions-history-clear "#query-suggestions-history-clear")
- [No suggestions
  available](#query-suggestions-history-none "#query-suggestions-history-none")

You can choose to suggest queries relevant to your users based on popular queries
in the query history or query log. Amazon Kendra uses all of the queries that
your users search for and learns from these queries to make suggestions to your
users. Amazon Kendra suggests popular queries to users when they start typing
their query. Amazon Kendra suggests a query if the prefix or first few
characters of the query matches what the user starts typing as their query.

For example, a user starts typing the query 'upcoming events'. Amazon Kendra
has learned from the query history that many users have searched for 'upcoming
events 2050' many times. The user sees 'upcoming events 2050' appear directly
underneath their search bar, autocompleting their search query. The user selects
this query suggestion, and the document 'New events: What's happening in 2050' is
returned in the search results.

You can specify how Amazon Kendra selects eligible queries to suggest to your
users. For example, you can specify that a query suggestion must have been searched
by at least 10 unique users (default is three), have been searched within the last
30 days, and does not contain any words or phrases from your [block
list](query-suggestions.md#query-suggestions-blocklist "query-suggestions.md#query-suggestions-blocklist"). Amazon Kendra requires that a query has at least one search
result and contains at least one word of more than four characters.

### Settings for selecting

queries for suggestions

You can configure the following settings for selecting queries for suggestions
by using the [UpdateQuerySuggestionsConfig](../APIReference/API_UpdateQuerySuggestionsConfig.md "../APIReference/API_UpdateQuerySuggestionsConfig.md") API:

- **Mode**—Query suggestions using
  the query history are either `ENABLED` or
  `LEARN_ONLY`. Amazon Kendra
  activates query suggestions by default.
  `LEARN_ONLY` turns off query suggestions.
  If turned off, Amazon Kendra continues to learn suggestions but
  doesn't make query suggestions to users.
- **Query log time window**—How
  recent your queries are in your query log time window. The time window
  is an integer value for the number of days from current day to past
  days.
- **Queries without user
  information**—Set to `TRUE` to
  include all queries, or set to `FALSE` to only
  include queries with user information. You can use this setting if your
  search application includes user information, such as the user ID, when
  a user issues a query. By default, this setting doesn't filter out
  queries if there's no specific user information associated with the
  queries. However, you can use this setting to only make suggestions
  based on queries that include user information.
- **Unique users**—The minimum
  number of unique users who must search a query for the query to be
  eligible to suggest to your users. This number is an integer
  value.
- **Query count**—The minimum number
  of times a query must be searched for the query to be eligible to
  suggest to your users. This number is an integer value.

These settings affect how queries are selected as popular queries to suggest
to your users. How you tune your settings will depend on your specific needs,
for example:

- If your users usually search once a month on average, then you can set
  the number of days in the query log time window to 30 days. By using
  that setting, you capture most of your users' recent queries before they
  become outdated in the time window.
- If only a small number of your queries include user information, and
  you don't want to suggest queries based on a small sample size, then you
  can set queries to include all users.
- If you define popular queries as being searched by at least 10 unique
  users and searched at least 100 times, then you set the unique users to
  10 and the query count to 100.

###### Warning

Your changes to settings might not take effect immediately. You can track
the settings changes by using the [DescribeQuerySuggestionsConfig](../APIReference/API_DescribeQuerySuggestionsConfig.md "../APIReference/API_DescribeQuerySuggestionsConfig.md") API. The time
for your updated settings to take effect depends on the updates that you
make and the number of search queries in your index. Amazon Kendra
automatically updates suggestions every 24 hours, after you change a setting
or after you apply a [block list](query-suggestions.md#query-suggestions-blocklist "query-suggestions.md#query-suggestions-blocklist").

CLI
**To retrieve query
suggestions**

```
aws kendra get-query-suggestions \
 --index-id `index-id` \
 --query-text "query-text" \
 --suggestion-types '["QUERY"]' \
 --max-suggestions-count 1 // If you want to limit the number of suggestions
```

**To update query
suggestions**

For example, to change the query log time window and the minimum
number of times a query must be searched:

```
aws kendra update-query-suggestions-config \
 --index-id `index-id` \
 --query-log-look-back-window-in-days 30 \
 --minimum-query-count 100
```

Python
**To retrieve query
suggestions**

```
import boto3
from botocore.exceptions import ClientError

kendra = boto3.client("kendra")

print("Get query suggestions.")

# Provide the index ID
index_id = "index-id"

# Provide the query text
query_text = "query"

# Provide the query suggestions type
query_suggestions_type = "QUERY"


# If you want to limit the number of suggestions
num_suggestions = 1

try:
    query_suggestions_response = kendra.get_query_suggestions(
        IndexId = index_id,
        QueryText = query_text,
        SuggestionTypes = query_suggestions_type,
        MaxSuggestionsCount = num_suggestions
    )

    # Print out the suggestions you received
    if ("Suggestions" in query_suggestions_response.keys()) {
        for (suggestion: query_suggestions_response["Suggestions"]) {
            print(suggestion["Value"]["Text"]["Text"]);
        }
    }

except ClientError as e:
        print("%s" % e)

print("Program ends.")
```

**To update query
suggestions**

For example, to change the query log time window and the minimum
number of times a query must be searched:

```
import boto3
from botocore.exceptions import ClientError
import pprint
import time

kendra = boto3.client("kendra")

print("Updating query suggestions settings/configuration for an index.")

# Provide the index ID
index_id = "index-id"

# Configure the settings you want to update
minimum_query_count = 100
query_log_look_back_window_in_days = 30

try:
    kendra.update_query_suggestions_config(
        IndexId = index_id,
        MinimumQueryCount = minimum_query_count,
        QueryLogLookBackWindowInDays = query_log_look_back_window_in_days
    )

    print("Wait for Amazon Kendra to update the query suggestions.")

    while True:
        # Get query suggestions description of settings/configuration
        query_sugg_config_response = kendra.describe_query_suggestions_config(
            IndexId = index_id
        )

        # If status is not UPDATING, then quit
        status = query_sugg_config_response["Status"]
        print(" Updating query suggestions config. Status: " + status)
        if status != "UPDATING":
            break
        time.sleep(60)

except ClientError as e:
        print("%s" % e)

print("Program ends.")
```

### Clear suggestions while

retaining query history

###### Note

Feature support varies by index type and search API being used. To see if
this feature is supported for the index type and search API you’re using,
see [Index types](hiw-index-types.md "hiw-index-types.md").

You can clear query suggestions by using the [ClearQuerySuggestions](../APIReference/API_DescribeQuerySuggestionsConfig.md "../APIReference/API_DescribeQuerySuggestionsConfig.md") API. Clearing suggestions
deletes existing query suggestions only, not the queries in the query history.
When you clear suggestions, Amazon Kendra learns new suggestions based on
new queries added to the query log from the time you cleared suggestions.

CLI
**To clear query suggestions**

```
aws  kendra clear-query-suggestions \
 --index-id `index-id`
```

Python
**To clear query suggestions**

```
import boto3
from botocore.exceptions import ClientError

kendra = boto3.client("kendra")

print("Clearing out query suggestions for an index.")

# Provide the index ID
index_id = "index-id"

try:
    kendra.clear_query_suggestions(
        IndexId = index_id
    )

    # Confirm last cleared date-time and that there are no suggestions
    query_sugg_config_response = kendra.describe_query_suggestions_config(
        IndexId = index_id
    )
    print("Query Suggestions last cleared at: " + str(query_sugg_config_response["LastClearTime"]));
    print("Number of suggestions available from the time of clearing: " + str(query_sugg_config_response["TotalSuggestionsCount"]));

except ClientError as e:
        print("%s" % e)

print("Program ends.")
```

### No suggestions

available

If you don't see suggestions for a query, it could be for one of the following
reasons:

- There are not enough queries in your index for Amazon Kendra to
  learn from.
- Your query suggestions settings are too strict, resulting in most
  queries being filtered out from suggestions.
- You recently cleared suggestions, and Amazon Kendra still needs
  time for new queries to accumulate in order to learn new
  suggestions.

You can check your current settings using the [DescribeQuerySuggestionsConfig](../APIReference/API_DescribeQuerySuggestionsConfig.md "../APIReference/API_DescribeQuerySuggestionsConfig.md") API.

## Query suggestions using document

fields

###### Topics

- [Settings for selecting
  fields for suggestions](#query-suggestions-doc-fields-settings "#query-suggestions-doc-fields-settings")
- [User control in
  document fields](#query-suggestions-doc-fields-user-control "#query-suggestions-doc-fields-user-control")

You can choose to suggest queries relevant to your users based on the contents of
document fields. Instead of using the query history to suggest other popular
relevant queries, you can use information contained within a document field that is
useful to autocompleting the query. Amazon Kendra looks for relevant content in
fields set to `Suggestable` and that closely aligns with
your user's query. Then, Amazon Kendra suggests this content to your user when
they start typing their query.

For example, if you specify the title field to base suggestions on and a user
starts typing the query 'How amazon ken...', the most relevant title 'How Amazon Kendra works' could be suggested to autocomplete the search. The user sees
'How Amazon Kendra works' appear directly underneath their search bar,
autocompleting their search query. The user selects this query suggestion, and the
document 'How Amazon Kendra works' is returned in the search results.

You can use the contents of any document field of
`String` and `StringList`
type to suggest a query by setting the field to
`Suggestable` as part of your fields configuration for
query suggestions. You can also use a [block
list](query-suggestions.md#query-suggestions-blocklist "query-suggestions.md#query-suggestions-blocklist") so that suggested document fields that contain certain words or
phrases are not shown to your users. You can use one block list. The block list
applies whether you set query suggestions to use the query history or document
fields.

### Settings for selecting

fields for suggestions

You can configure the following settings for selecting document fields for
suggestions using [AttributeSuggestionsConfig](../APIReference/API_AttributeSuggestionsConfig.md "../APIReference/API_AttributeSuggestionsConfig.md") and calling the
[UpdateQuerySuggestionsConfig](../APIReference/API_UpdateQuerySuggestionsConfig.md "../APIReference/API_UpdateQuerySuggestionsConfig.md") API to update the
settings at the index level:

- **Field/attribute suggestions
  mode**—Query suggestions using document fields are
  either `ACTIVE` or
  `INACTIVE`. Amazon Kendra
  activates query suggestions by default.
- **Suggestible
  fields/attributes**—The field names or field keys to
  base suggestions on. These fields must be set to
  `TRUE` for
  `Suggestable`, as part of the fields
  configuration. You can override the fields configuration at the query
  level while maintaining the configuration at the index level. Use the
  [GetQuerySuggestions](../APIReference/API_GetQuerySuggestions.md "../APIReference/API_GetQuerySuggestions.md") API to change
  `AttributeSuggestionConfig` at the
  query level. This configuration at the query level can be useful for
  quickly experimenting with using different document fields without
  having to update the configuration at the index level.
- **Additional
  fields/attributes**—The additional fields that you want
  to include in the response for a query suggestion. These fields are used
  to provide extra information in the response; however, they are not used
  to base suggestions on.

###### Warning

Your changes to settings might not take effect immediately. You can track
the settings changes by using the [DescribeQuerySuggestionsConfig](../APIReference/API_DescribeQuerySuggestionsConfig.md "../APIReference/API_DescribeQuerySuggestionsConfig.md") API. The time
for your updated settings to take effect depends on the updates that you
make. Amazon Kendra automatically updates suggestions every 24 hours,
after you change a setting or after you apply a [block list](query-suggestions.md#query-suggestions-blocklist "query-suggestions.md#query-suggestions-blocklist").

CLI
To retrieve query suggestions and override the document fields
configuration at the query level instead of having to change the
configuration at the index level.

```
aws kendra get-query-suggestions \
 --index-id `index-id` \
 --query-text "query-text" \
 --suggestion-types '["DOCUMENT_ATTRIBUTES"]' \
 --attribute-suggestions-config '{"SuggestionAttributes":'["field/attribute key 1", "field/attribute key 2"]', "AdditionalResponseAttributes":'["response field/attribute key 1", "response field/attribute key 2"]'}' \
 --max-suggestions-count 1 // If you want to limit the number of suggestions
```

**To update query
suggestions**

For example, to change the document fields configuration at the
index level:

```
aws kendra update-query-suggestions-config \
 --index-id index-id \
 --attribute-suggestions-config '{"SuggestableConfigList": '[{"SuggestableConfig": "_document_title", "Suggestable": true}]', "AttributeSuggestionsMode": "ACTIVE"}'
```

Python
To retrieve query suggestions and override the document fields
configuration at the query level instead of having to change the
configuration at the index level.

```
import boto3
from botocore.exceptions import ClientError

kendra = boto3.client("kendra")

print("Get query suggestions.")

# Provide the index ID
index_id = "index-id"

# Provide the query text
query_text = "query"

# Provide the query suggestions type
query_suggestions_type = "DOCUMENT_ATTRIBUTES"

# Override fields/attributes configuration at query level
configuration = {"SuggestionAttributes":
    '["field/attribute key 1", "field/attribute key 2"]',
      "AdditionalResponseAttributes":
          '["response field/attribute key 1", "response field/attribute key 2"]'
          }

# If you want to limit the number of suggestions
num_suggestions = 1

try:
    query_suggestions_response = kendra.get_query_suggestions(
        IndexId = index_id,
        QueryText = query_text,
        SuggestionTypes = [query_suggestions_type],
        AttributeSuggestionsConfig = configuration,
        MaxSuggestionsCount = num_suggestions
    )

    # Print out the suggestions you received
    if ("Suggestions" in query_suggestions_response.keys()) {
        for (suggestion: query_suggestions_response["Suggestions"]) {
            print(suggestion["Value"]["Text"]["Text"]);
        }
    }

except ClientError as e:
        print("%s" % e)

print("Program ends.")
```

**To update query
suggestions**

For example, to change the document fields configuration at the
index level:

```
import boto3
from botocore.exceptions import ClientError
import pprint
import time

kendra = boto3.client("kendra")

print("Updating query suggestions settings/configuration for an index.")

# Provide the index ID
index_id = "index-id"

# Configure the settings you want to update at the index level
configuration = {"SuggestableConfigList":
    '[{"SuggestableConfig": "_document_title", "Suggestable": true}]',
       "AttributeSuggestionsMode": "ACTIVE"
       }

try:
    kendra.update_query_suggestions_config(
        IndexId = index_id,
        AttributeSuggestionsConfig = configuration
    )

    print("Wait for Amazon Kendra to update the query suggestions.")

    while True:
        # Get query suggestions description of settings/configuration
        query_sugg_config_response = kendra.describe_query_suggestions_config(
            IndexId = index_id
        )

        # If status is not UPDATING, then quit
        status = query_sugg_config_response["Status"]
        print(" Updating query suggestions config. Status: " + status)
        if status != "UPDATING":
            break
        time.sleep(60)

except ClientError as e:
        print("%s" % e)

print("Program ends.")
```

### User control in

document fields

You can apply user context filtering to the document fields that you want to
base query suggestions on. This filters document field information based on the
user or their group access to documents. For example, an intern searches the
company's portal and doesn't have access to a top-secret company document.
Therefore, suggested queries based on the top-secret document's title, or any
other suggestible field, is not shown to the intern.

You can index your documents with an access control list (ACL), defining which
users and groups are assigned access to which documents. Then, you can apply
user context filtering to your documents fields for query suggestions. User
context filtering that is currently set for your index is the same user context
filtering applied to your document fields configuration for query suggestions.
User context filtering is part of your document fields configuration. You use
the [AttributeSuggestionsGetConfig](../APIReference/API_AttributeSuggestionsConfig.md "../APIReference/API_AttributeSuggestionsConfig.md") and call [GetQuerySuggestions](../APIReference/API_GetQuerySuggestions.md "../APIReference/API_GetQuerySuggestions.md").

## Block certain queries or document

field content from suggestions

A _block list_ stops Amazon Kendra from
suggesting certain queries to your users. A block list is a list of words or phrases
that you want to exclude from query suggestions. Amazon Kendra excludes queries
containing an exact match of the words or phrases in the block list.

You can use a block list to safeguard against offensive words or phrases that
commonly appear in your query history or document fields and that Amazon Kendra
could select as suggestions. A block list can also prevent Amazon Kendra from
suggesting queries that contain information that is not ready to be publicly
released or announced. For example, your users frequently query about an upcoming
release of a potential new product. However, you don't want to suggest the product
because you're not ready to release it.You can block queries that contain the
product name and product information from suggestions.

You can create a block list for queries by using the [CreateQuerySuggestionsBlockList](../APIReference/API_CreateQuerySuggestionsBlockList.md "../APIReference/API_CreateQuerySuggestionsBlockList.md") API. You put each
block word or phrase on a separate line in a text file. Then you upload the text
file to your Amazon S3 bucket and provide the path or location to the file in Amazon S3. Amazon Kendra currently supports creating only one block
list.

You can replace the text file of your blocked words and phrases in your Amazon S3 bucket. To update the block list in Amazon Kendra, use the [UpdateQuerySuggestionsBlockList](../APIReference/API_UpdateQuerySuggestionsBlockList.md "../APIReference/API_UpdateQuerySuggestionsBlockList.md") API.

Use the [DescribeQuerySuggestionsBlockList](../APIReference/API_DescribeQuerySuggestionsBlockList.md "../APIReference/API_DescribeQuerySuggestionsBlockList.md") API to get the
status of your block list.
`DescribeQuerySuggestionsBlockList` can also provide
you with other useful information, such as the following:

- When your block list was last updated
- How many words or phrases are in your current block list
- Helpful error messages when creating a block list

You can also use the [ListQuerySuggestionsBlockLists](../APIReference/API_ListQuerySuggestionsBlockLists.md "../APIReference/API_ListQuerySuggestionsBlockLists.md") API to get a list of
block list summaries for an index.

To delete your block list, use the [DeleteQuerySuggestionsBlockList](../APIReference/API_DeleteQuerySuggestionsBlockList.md "../APIReference/API_DeleteQuerySuggestionsBlockList.md") API.

Your updates to the block list might not take effect right away. You can track
updates by using the `DescribeQuerySuggestionsBlockList`
API.

CLI
**To create a block list**

```
aws kendra create-query-suggestions-block-list \
 --index-id `index-id` \
 --name "block-list-name" \
 --description "block-list-description" \
 --source-s3-path "Bucket=bucket-name,Key=query-suggestions/block_list.txt" \
 --role-arn `role-arn`
```

**To update a block list**

```
aws kendra update-query-suggestions-block-list \
 --index-id `index-id` \
 --name "new-block-list-name" \
 --description "new-block-list-description" \
 --source-s3-path "Bucket=bucket-name,Key=query-suggestions/new_block_list.txt" \
 --role-arn `role-arn`
```

**To delete a block list**

```
aws kendra delete-query-suggestions-block-list \
 --index-id `index-id` \
 --id `block-list-id`
```

Python
**To create a block list**

```
import boto3
from botocore.exceptions import ClientError
import pprint
import time

kendra = boto3.client("kendra")

print("Create a query suggestions block list.")

# Provide a name for the block list
block_list_name = "block-list-name"
# Provide an optional description for the block list
block_list_description = "block-list-description"
# Provide the IAM role ARN required for query suggestions block lists
block_list_role_arn = "role-arn"

# Provide the index ID
index_id = "index-id"

s3_bucket_name = "bucket-name"
s3_key = "query-suggestions/block_list.txt"
source_s3_path = {
    'Bucket': s3_bucket_name,
    'Key': s3_key
}

try:
    block_list_response = kendra.create_query_suggestions_block_list(
        Description = block_list_description,
        Name = block_list_name,
        RoleArn = block_list_role_arn,
        IndexId = index_id,
        SourceS3Path = source_s3_path
    )

    print(block_list_response)

    block_list_id = block_list_response["Id"]

    print("Wait for Amazon Kendra to create the block list.")

    while True:
        # Get block list description
        block_list_description = kendra.describe_query_suggestions_block_list(
            Id = block_list_id,
            IndexId = index_id
        )
        # If status is not CREATING, then quit
        status = block_list_description["Status"]
        print("Creating block list. Status: " + status)
        if status != "CREATING":
            break
        time.sleep(60)

except ClientError as e:
        print("%s" % e)

print("Program ends.")
```

**To update a block list**

```
import boto3
from botocore.exceptions import ClientError
import pprint
import time

kendra = boto3.client("kendra")

print("Update a block list for query suggestions.")

# Provide the block list name you want to update
block_list_name = "new-block-list-name"
# Provide the block list description you want to update
block_list_description = "new-block-list-description"
# Provide the IAM role ARN required for query suggestions block lists
block_list_role_arn = "role-arn"

# Provide the block list ID
block_list_id = "block-list-id"
# Provide the index ID
index_id = "index-id"

s3_bucket_name = "bucket-name"
s3_key = "query-suggestions/new_block_list.txt"
source_s3_path = {
'Bucket': s3_bucket_name,
'Key': s3_key
}

try:
    kendra.update_query_suggestions_block_list(
        Id = block_list_id,
        IndexId = index_id,
        Description = block_list_description,
        Name = block_list_name,
        RoleArn = block_list_role_arn,
        SourceS3Path = source_s3_path
    )

    print("Wait for Amazon Kendra to update the block list.")

    while True:
        # Get block list description
        block_list_description = kendra.describe_query_suggestions_block_list(
            Id = block_list_id,
            IndexId = index_id
        )
        # If status is not UPDATING, then the update has finished
        status = block_list_description["Status"]
        print("Updating block list. Status: " + status)
        if status != "UPDATING":
            break
        time.sleep(60)

except ClientError as e:
print("%s" % e)

print("Program ends.")
```

**To delete a block list**

```
import boto3
from botocore.exceptions import ClientError

kendra = boto3.client("kendra")

print("Delete a block list for query suggestions.")

# provide the block list ID
query_suggestions_block_list_id = "query-suggestions-block-list-id"
# Provide the index ID
index_id = "index-id"

try:
    kendra.delete_query_suggestions_block_list(
        Id = query_suggestions_block_list_id,
        IndexId = index_id
    )

except ClientError as e:
        print("%s" % e)

print("Program ends.")
```
