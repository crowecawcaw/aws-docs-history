# Using IAM policy conditions for fine-grained

access control

When you grant permissions in DynamoDB, you can specify conditions that determine how a
permissions policy takes effect.

## Overview

In DynamoDB, you have the option to specify conditions when granting permissions using an
IAM policy (see
[Identity and Access Management for Amazon DynamoDB](security-iam.md "security-iam.md")). For example, you can:

- Grant permissions to allow users read-only access to certain items and
  attributes in a table or a secondary index.
- Grant permissions to allow users write-only access to certain attributes in a
  table, based upon the identity of that user.

In DynamoDB, you can specify conditions in an IAM policy using condition keys, as
illustrated in the use case in the following section.

### Permissions use case

In addition to controlling access to DynamoDB API actions, you can also control
access to individual data items and attributes. For example, you can do the
following:

- Grant permissions on a table, but restrict access to specific items in
  that table based on certain primary key values. An example might be a social
  networking app for games, where all users' saved game data is stored in a
  single table, but no users can access data items that they do not own, as
  shown in the following illustration:

![A use case which grants table-level access to a user but restricts access to specific data items.](images/info-hiding-horizontal.png)

- Hide information so that only a subset of attributes is visible to the
  user. An example might be an app that displays flight data for nearby
  airports, based on the user's location. Airline names, arrival and departure
  times, and flight numbers are all displayed. However, attributes such as
  pilot names or the number of passengers are hidden, as shown in the
  following illustration:

![A use case that displays only a subset of data to users, but hides certain attributes of the data.](images/info-hiding-vertical.png)

To implement this kind of fine-grained access control, you write an IAM
permissions policy that specifies conditions for accessing security credentials and
the associated permissions. You then apply the policy to users, groups, or
roles that you create using the IAM console. Your IAM policy can restrict access
to individual items in a table, access to the attributes in those items, or both at
the same time.

You can optionally use web identity federation to control
access by users who are authenticated by Login with Amazon, Facebook, or Google. For
more information, see [Using web identity federation](WIF.md "WIF.md").

You use the IAM `Condition` element to implement a fine-grained
access control policy. By adding a `Condition` element to a permissions
policy, you can allow or deny access to items and attributes in DynamoDB tables and
indexes, based upon your particular business requirements.

As an example, consider a mobile gaming app that lets players select from and play
a variety of different games. The app uses a DynamoDB table
named `GameScores` to keep track of high scores and other user data.
Each item in the table is uniquely identified by a user ID and the name of the game
that the user played. The `GameScores` table has a primary key consisting
of a partition key (`UserId`) and sort key (`GameTitle`).
Users only have access to game data associated with their user ID. A user who wants
to play a game must belong to an IAM role named `GameRole`, which has a
security policy attached to it.

To manage user permissions in this app, you could write a permissions policy such
as the following:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement":[
 {
 "Sid":"AllowAccessToOnlyItemsMatchingUserID",
 "Effect":"Allow",
 "Action":[
 "dynamodb:GetItem",
 "dynamodb:BatchGetItem",
 "dynamodb:Query",
 "dynamodb:PutItem",
 "dynamodb:UpdateItem",
 "dynamodb:DeleteItem",
 "dynamodb:BatchWriteItem"
 ],
 "Resource":[
 "arn:aws:dynamodb:us-west-2:123456789012:table/GameScores"
 ],
 "Condition":{
 "ForAllValues:StringEquals":{
 "dynamodb:LeadingKeys":[
 "${www.amazon.com:user_id}"
 ],
 "dynamodb:Attributes":[
 "UserId",
 "GameTitle",
 "Wins",
 "Losses",
 "TopScore",
 "TopScoreDateTime"
 ]
 },
 "StringEqualsIfExists":{
 "dynamodb:Select":"SPECIFIC_ATTRIBUTES"
 }
 }
 }
 ]
}`

```

In addition to granting permissions for specific DynamoDB actions
(`Action` element) on the `GameScores` table
(`Resource` element), the `Condition` element uses the
following condition keys specific to DynamoDB that limit the permissions as
follows:

- `dynamodb:LeadingKeys` – This condition key allows users
  to access only the items where the partition key value matches their user
  ID. This ID, `${www.amazon.com:user_id}`, is a substitution
  variable. For more information about substitution variables, see [Using web identity federation](WIF.md "WIF.md").
- `dynamodb:Attributes` – This condition key limits access
  to the specified attributes so that only the actions listed in the
  permissions policy can return values for these attributes. In addition, the
  `StringEqualsIfExists` clause ensures that the app must
  always provide a list of specific attributes to act upon and that the app
  can't request all attributes.

When an IAM policy is evaluated, the result is always either true (access is
allowed) or false (access is denied). If any part of the `Condition`
element is false, the entire policy evaluates to false and access is denied.

###### Important

If you use `dynamodb:Attributes`, you must specify the names of all
of the primary key and index key attributes for the table and any secondary
indexes that are listed in the policy. Otherwise, DynamoDB can't use these key
attributes to perform the requested action.

IAM policy documents can contain only the following Unicode characters: horizontal
tab (U+0009), linefeed (U+000A), carriage return (U+000D), and characters in the
range U+0020 to U+00FF.

## Specifying conditions: Using condition

keys

AWS provides a set of predefined condition keys (AWS-wide condition keys) for all
AWS services that support IAM for access control. For example, you can use the
`aws:SourceIp` condition key to check the requester's IP address before
allowing an action to be performed. For more information and a list of the AWS-wide
keys, see [Available Keys for Conditions](../../../IAM/latest/UserGuide/reference_policies_elements.md#AvailableKeys "../../../IAM/latest/UserGuide/reference_policies_elements.md#AvailableKeys") in the IAM User Guide.

The following table shows the DynamoDB service-specific condition keys that apply to
DynamoDB.

| DynamoDB Condition Key            | Description                                                                                                                                                                                                                                                                                                                                                                                                             |
| --------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `dynamodb:LeadingKeys`            | Represents the first key attribute of a table—in other<br>words, the partition key. The key name `LeadingKeys` is<br>plural, even if the key is used with single-item actions. In<br>addition, you must use the `ForAllValues` modifier when<br>using `LeadingKeys` in a condition.                                                                                                                                     |
| `dynamodb:Select`                 | Represents the `Select` parameter of a<br>`Query` or `Scan` request.<br>`Select` can be any of the following values:<br>• `ALL_ATTRIBUTES`<br>• `ALL_PROJECTED_ATTRIBUTES`<br>• `SPECIFIC_ATTRIBUTES`<br>• `COUNT`                                                                                                                                                                                                      |
| `dynamodb:Attributes`             | Represents a list of the \*top-level<br>• attributes accessed by a request. A top-level attribute is accessed by a request if it, or any nested attribute that it contains, is specified in the request parameters or returned from the request. For example, a `GetItem` request that specifies a `ProjectionExpression` of `"Name, Address.City"`, the `dynamodb:Attributes` list would include "Name" and "Address". |
| `dynamodb:ReturnValues`           | Represents the `ReturnValues` parameter of a request.<br>`ReturnValues` can be any of the following values:<br>• `ALL_OLD`<br>• `UPDATED_OLD`<br>• `ALL_NEW`<br>• `UPDATED_NEW`<br>• `NONE`                                                                                                                                                                                                                             |
| `dynamodb:ReturnConsumedCapacity` | Represents the `ReturnConsumedCapacity` parameter of a<br>request. `ReturnConsumedCapacity` can be one of the<br>following values:<br>• `TOTAL`<br>• `NONE`                                                                                                                                                                                                                                                             |

### Limiting user access

Many IAM permissions policies allow users to access only those items in a table
where the partition key value matches the user identifier. For example, the game app
preceding limits access in this way so that users can only access game data that is
associated with their user ID. The IAM substitution variables
`${www.amazon.com:user_id}`, `${graph.facebook.com:id}`,
and `${accounts.google.com:sub}` contain user identifiers for Login with
Amazon, Facebook, and Google. To learn how an application logs in to one of these
identity providers and obtains these identifiers, see [Using web identity federation](WIF.md "WIF.md").

###### Important

Fine-grained access control isn't supported for restricting global tables
replication. Applying policy conditions for fine-grained access control to DynamoDB
[service principals or service-linked roles](globaltables-security.md "globaltables-security.md") used for global tables
replication may interrupt replication within a global table.

###### Note

Each of the examples in the following section sets the `Effect`
clause to `Allow` and specifies only the actions, resources, and
parameters that are allowed. Access is permitted only to what is explicitly
listed in the IAM policy.

In some cases, it is possible to rewrite these policies so that they are
deny-based (that is, setting the `Effect` clause to `Deny`
and inverting all of the logic in the policy). However, we recommend that you
avoid using deny-based policies with DynamoDB because they're difficult to write
correctly, compared to allow-based policies. In addition, future changes to the
DynamoDB API (or changes to existing API inputs) can render a deny-based policy
ineffective.

### Example policies: Using conditions for

fine-grained access control

This section shows several policies for implementing fine-grained access control
on DynamoDB tables and indexes.

###### Note

All examples use the us-west-2 Region and contain fictitious account
IDs.

The video below explains fine-grained access control in DynamoDB using IAM
policy conditions.

#### 1: Grant permissions that limit access to

items with a specific partition key value

The following permissions policy grants permissions that allow a set of DynamoDB
actions on the `GamesScore` table. It uses the
`dynamodb:LeadingKeys` condition key to limit user actions only
on the items whose `UserID` partition key value matches the Login
with Amazon unique user ID for this app.

###### Important

The list of actions does not include permissions for `Scan`
because `Scan` returns all items regardless of the leading
keys.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement":[
 {
 "Sid":"FullAccessToUserItems",
 "Effect":"Allow",
 "Action":[
 "dynamodb:GetItem",
 "dynamodb:BatchGetItem",
 "dynamodb:Query",
 "dynamodb:PutItem",
 "dynamodb:UpdateItem",
 "dynamodb:DeleteItem",
 "dynamodb:BatchWriteItem"
 ],
 "Resource":[
 "arn:aws:dynamodb:us-west-2:123456789012:table/GameScores"
 ],
 "Condition":{
 "ForAllValues:StringEquals":{
 "dynamodb:LeadingKeys":[
 "${www.amazon.com:user_id}"
 ]
 }
 }
 }
 ]
}`

```

###### Note

When using policy variables, you must explicitly specify version
`2012-10-17` in the policy. The default version of the access
policy language, `2008-10-17`, does not support policy variables.

To implement read-only access, you can remove any actions that can modify the
data. In the following policy, only those actions that provide read-only access
are included in the condition.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement":[
 {
 "Sid":"ReadOnlyAccessToUserItems",
 "Effect":"Allow",
 "Action":[
 "dynamodb:GetItem",
 "dynamodb:BatchGetItem",
 "dynamodb:Query"
 ],
 "Resource":[
 "arn:aws:dynamodb:us-west-2:123456789012:table/GameScores"
 ],
 "Condition":{
 "ForAllValues:StringEquals":{
 "dynamodb:LeadingKeys":[
 "${www.amazon.com:user_id}"
 ]
 }
 }
 }
 ]
}`

```

###### Important

If you use `dynamodb:Attributes`, you must specify the names of
all of the primary key and index key attributes, for the table and any
secondary indexes that are listed in the policy. Otherwise, DynamoDB can't use these key
attributes to perform the requested action.

#### 2: Grant permissions that limit access to

specific attributes in a table

The following permissions policy allows access to only two specific attributes
in a table by adding the `dynamodb:Attributes` condition key. These
attributes can be read, written, or evaluated in a conditional write or scan
filter.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement":[
 {
 "Sid":"LimitAccessToSpecificAttributes",
 "Effect":"Allow",
 "Action":[
 "dynamodb:UpdateItem",
 "dynamodb:GetItem",
 "dynamodb:Query",
 "dynamodb:BatchGetItem",
 "dynamodb:Scan"
 ],
 "Resource":[
 "arn:aws:dynamodb:us-west-2:123456789012:table/GameScores"
 ],
 "Condition":{
 "ForAllValues:StringEquals":{
 "dynamodb:Attributes":[
 "UserId",
 "TopScore"
 ]
 },
 "StringEqualsIfExists":{
 "dynamodb:Select":"SPECIFIC_ATTRIBUTES",
 "dynamodb:ReturnValues":[
 "NONE",
 "UPDATED_OLD",
 "UPDATED_NEW"
 ]
 }
 }
 }
 ]
}`

```

###### Note

The policy takes an _allow list_ approach, which allows
access to a named set of attributes. You can write an equivalent policy that
denies access to other attributes instead. We don't recommend this
_deny list_ approach. Users can determine the names
of these denied attributes by follow the _principle of least
privilege_, as explained in Wikipedia at [http://en.wikipedia.org/wiki/Principle_of_least_privilege](http://en.wikipedia.org/wiki/Principle_of_least_privilege "http://en.wikipedia.org/wiki/Principle_of_least_privilege"), and
use an _allow list_ approach to enumerate all of the
allowed values, rather than specifying the denied attributes.

This policy doesn't permit `PutItem`, `DeleteItem`, or
`BatchWriteItem`. These actions always replace the entire
previous item, which would allow users to delete the previous values for
attributes that they are not allowed to access.

The `StringEqualsIfExists` clause in the permissions policy ensures
the following:

- If the user specifies the `Select` parameter, then its
  value must be `SPECIFIC_ATTRIBUTES`. This requirement
  prevents the API action from returning any attributes that aren't
  allowed, such as from an index projection.
- If the user specifies the `ReturnValues` parameter, then
  its value must be `NONE`, `UPDATED_OLD`, or
  `UPDATED_NEW`. This is required because the
  `UpdateItem` action also performs implicit read
  operations to check whether an item exists before replacing it, and so
  that previous attribute values can be returned if requested. Restricting
  `ReturnValues` in this way ensures that users can only
  read or write the allowed attributes.
- The `StringEqualsIfExists` clause assures that only one of
  these parameters — `Select` or
  `ReturnValues` — can be used per request, in the
  context of the allowed actions.

The following are some variations on this policy:

- To allow only read actions, you can remove `UpdateItem`
  from the list of allowed actions. Because none of the remaining actions
  accept `ReturnValues`, you can remove
  `ReturnValues` from the condition. You can also change
  `StringEqualsIfExists` to `StringEquals`
  because the `Select` parameter always has a value
  (`ALL_ATTRIBUTES`, unless otherwise specified).
- To allow only write actions, you can remove everything except
  `UpdateItem` from the list of allowed actions. Because
  `UpdateItem` does not use the `Select`
  parameter, you can remove `Select` from the condition. You
  must also change `StringEqualsIfExists` to
  `StringEquals` because the `ReturnValues`
  parameter always has a value (`NONE` unless otherwise
  specified).
- To allow all attributes whose name matches a pattern, use
  `StringLike` instead of `StringEquals`, and
  use a multi-character pattern match wildcard character (\*).

#### 3: Grant permissions to prevent updates

on certain attributes

The following permissions policy limits user access to updating only the
specific attributes identified by the `dynamodb:Attributes` condition
key. The `StringNotLike` condition prevents an application from
updating the attributes specified using the `dynamodb:Attributes`
condition key.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement":[
 {
 "Sid":"PreventUpdatesOnCertainAttributes",
 "Effect":"Allow",
 "Action":[
 "dynamodb:UpdateItem"
 ],
 "Resource":"arn:aws:dynamodb:us-west-2:123456789012:table/GameScores",
 "Condition":{
 "ForAllValues:StringNotLike":{
 "dynamodb:Attributes":[
 "FreeGamesAvailable",
 "BossLevelUnlocked"
 ]
 },
 "StringEquals":{
 "dynamodb:ReturnValues":[
 "NONE",
 "UPDATED_OLD",
 "UPDATED_NEW"
 ]
 }
 }
 }
 ]
}`

```

Note the following:

- The `UpdateItem` action, like other write actions, requires
  read access to the items so that it can return values before and after
  the update. In the policy, you limit the action to accessing only the
  attributes that are allowed to be updated by specifying the
  `dynamodb:ReturnValues` condition key. The condition key
  restricts `ReturnValues` in the request to specify only
  `NONE`, `UPDATED_OLD`, or
  `UPDATED_NEW` and doesn't include `ALL_OLD` or
  `ALL_NEW`.
- The `PutItem` and `DeleteItem` actions replace
  an entire item, and thus allows applications to modify any attributes.
  So when limiting an application to updating only specific attributes,
  you should not grant permission for these APIs.

#### 4: Grant permissions to query only

projected attributes in an index

The following permissions policy allows queries on a secondary index
(`TopScoreDateTimeIndex`) by using the
`dynamodb:Attributes` condition key. The policy also limits
queries to requesting only specific attributes that have been projected into the
index.

To require the application to specify a list of attributes in the query, the
policy also specifies the `dynamodb:Select` condition key to require
that the `Select` parameter of the DynamoDB `Query` action is
`SPECIFIC_ATTRIBUTES`. The list of attributes is limited to a
specific list that is provided using the `dynamodb:Attributes`
condition key.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement":[
 {
 "Sid":"QueryOnlyProjectedIndexAttributes",
 "Effect":"Allow",
 "Action":[
 "dynamodb:Query"
 ],
 "Resource":[
 "arn:aws:dynamodb:us-west-2:123456789012:table/GameScores/index/TopScoreDateTimeIndex"
 ],
 "Condition":{
 "ForAllValues:StringEquals":{
 "dynamodb:Attributes":[
 "TopScoreDateTime",
 "GameTitle",
 "Wins",
 "Losses",
 "Attempts"
 ]
 },
 "StringEquals":{
 "dynamodb:Select":"SPECIFIC_ATTRIBUTES"
 }
 }
 }
 ]
}`

```

The following permissions policy is similar, but the query must request all of
the attributes that have been projected into the index.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement":[
 {
 "Sid":"QueryAllIndexAttributes",
 "Effect":"Allow",
 "Action":[
 "dynamodb:Query"
 ],
 "Resource":[
 "arn:aws:dynamodb:us-west-2:123456789012:table/GameScores/index/TopScoreDateTimeIndex"
 ],
 "Condition":{
 "StringEquals":{
 "dynamodb:Select":"ALL_PROJECTED_ATTRIBUTES"
 }
 }
 }
 ]
}`

```

#### 5: Grant permissions to limit access to

certain attributes and partition key values

The following permissions policy allows specific DynamoDB actions (specified in
the `Action` element) on a table and a table index (specified in the
`Resource` element). The policy uses the
`dynamodb:LeadingKeys` condition key to restrict permissions to
only the items whose partition key value matches the user’s Facebook ID.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement":[
 {
 "Sid":"LimitAccessToCertainAttributesAndKeyValues",
 "Effect":"Allow",
 "Action":[
 "dynamodb:UpdateItem",
 "dynamodb:GetItem",
 "dynamodb:Query",
 "dynamodb:BatchGetItem"
 ],
 "Resource":[
 "arn:aws:dynamodb:us-west-2:123456789012:table/GameScores",
 "arn:aws:dynamodb:us-west-2:123456789012:table/GameScores/index/TopScoreDateTimeIndex"
 ],
 "Condition":{
 "ForAllValues:StringEquals":{
 "dynamodb:LeadingKeys":[
 "${graph.facebook.com:id}"
 ],
 "dynamodb:Attributes":[
 "attribute-A",
 "attribute-B"
 ]
 },
 "StringEqualsIfExists":{
 "dynamodb:Select":"SPECIFIC_ATTRIBUTES",
 "dynamodb:ReturnValues":[
 "NONE",
 "UPDATED_OLD",
 "UPDATED_NEW"
 ]
 }
 }
 }
 ]
}`

```

Note the following:

- Write actions allowed by the policy (`UpdateItem`) can only
  modify `attribute-A` or `attribute-B`.
- Because the policy allows `UpdateItem`, an application can
  insert new items, and the hidden attributes will be null in the new
  items. If these attributes are projected into
  `TopScoreDateTimeIndex`, the policy has the added benefit
  of preventing queries that cause fetches from the table.
- Applications cannot read any attributes other than those listed in
  `dynamodb:Attributes`. With this policy in place, an
  application must set the `Select` parameter to
  `SPECIFIC_ATTRIBUTES` in read requests, and only
  attributes in the allow list can be requested. For write requests, the
  application cannot set `ReturnValues` to `ALL_OLD`
  or `ALL_NEW` and it cannot perform conditional write
  operations based on any other attributes.

## Related topics

- [Identity and Access Management for Amazon DynamoDB](security-iam.md "security-iam.md")
- [DynamoDB API permissions: Actions, resources,
  and conditions reference](api-permissions-reference.md "api-permissions-reference.md")
