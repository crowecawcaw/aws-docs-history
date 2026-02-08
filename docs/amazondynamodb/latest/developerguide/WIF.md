# Using web identity federation

If you are writing an application targeted at large numbers of users, you can
optionally use _web identity federation_ for authentication and
authorization. Web identity federation removes the need for creating individual users.
Instead, users can sign in to an identity provider and then obtain temporary
security credentials from AWS Security Token Service (AWS STS). The app can then use these credentials
to access AWS services.

Web identity federation supports the following identity providers:

- Login with Amazon
- Facebook
- Google

## Additional resources for web identity

federation

The following resources can help you learn more about web identity
federation:

- The post [Web Identity Federation using the AWS SDK for .NET](https://aws.amazon.com/blogs/developer/web-identity-federation-using-the-aws-sdk-for-net "https://aws.amazon.com/blogs/developer/web-identity-federation-using-the-aws-sdk-for-net") on the AWS
  Developer blog walks through how to use web identity federation with
  Facebook. It includes code snippets in C# that show how to assume an IAM
  role with web identity and how to use temporary security credentials to
  access an AWS resource.
- The [AWS Mobile SDK for iOS](https://aws.amazon.com/sdkforios/ "https://aws.amazon.com/sdkforios/") and the
  [AWS Mobile SDK for Android](https://aws.amazon.com/sdkforandroid/ "https://aws.amazon.com/sdkforandroid/")
  contain sample apps. They include code that shows how to invoke the identity
  providers, and then how to use the information from these providers to get
  and use temporary security credentials.
- The article [Web
  Identity Federation with Mobile Applications](https://aws.amazon.com/articles/4617974389850313 "https://aws.amazon.com/articles/4617974389850313") discusses web
  identity federation and shows an example of how to use web identity
  federation to access an AWS resource.

## Example policy for web identity federation

To show how you can use web identity federation with DynamoDB, revisit the
_GameScores_ table that was introduced in [Using IAM policy conditions for fine-grained
access control](specifying-conditions.md "specifying-conditions.md"). Here is
the primary key for _GameScores_.

| Table Name                             | Primary Key Type | Partition Key Name and Type         | Sort Key Name and Type                 |
| -------------------------------------- | ---------------- | ----------------------------------- | -------------------------------------- |
| GameScores (UserId,<br>GameTitle, ...) | Composite        | Attribute Name: UserId Type: String | Attribute Name: GameTitle Type: String |

Now suppose that a mobile gaming app uses this table, and that
app needs to support thousands, or even millions, of users. At this scale, it
becomes very difficult to manage individual app users, and to guarantee that each
user can only access their own data in the _GameScores_ table.
Fortunately, many users already have accounts with a third-party identity provider,
such as Facebook, Google, or Login with Amazon. So it makes sense to use one of
these providers for authentication tasks.

To do this using web identity federation, the app developer must register the app
with an identity provider (such as Login with Amazon) and obtain a unique app ID.
Next, the developer needs to create an IAM role. (For this example, this role is
named _GameRole_.) The role must have an IAM policy document
attached to it, specifying the conditions under which the app can access
_GameScores_ table.

When a user wants to play a game, they sign in to their Login with Amazon account
from within the gaming app. The app then calls AWS Security Token Service (AWS STS), providing the
Login with Amazon app ID and requesting membership in _GameRole_.
AWS STS returns temporary AWS credentials to the app and allows it to access
the _GameScores_ table, subject to the
_GameRole_ policy document.

The following diagram shows how these pieces fit together.

![A gaming app’s workflow. The app uses Amazon ID and AWS STS to obtain temporary credentials for accessing a DynamoDB table.](images/wif-overview.png)

**Web identity federation overview**

1. The app calls a third-party identity provider to authenticate the user and
   the app. The identity provider returns a web identity token to the
   app.
2. The app calls AWS STS and passes the web identity token as input.
   AWS STS authorizes the app and gives it temporary AWS access
   credentials. The app is allowed to assume an IAM role
   (_GameRole_) and access AWS resources in accordance
   with the role's security policy.
3. The app calls DynamoDB to access the _GameScores_ table.
   Because it has assumed the _GameRole_, the app is subject
   to the security policy associated with that role. The policy document
   prevents the app from accessing data that does not belong to the
   user.

Once again, here is the security policy for _GameRole_ that was
shown in [Using IAM policy conditions for fine-grained
access control](specifying-conditions.md "specifying-conditions.md"):

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

The `Condition` clause determines which items in
_GameScores_ are visible to the app. It does this by
comparing the Login with Amazon ID to the `UserId` partition key values
in `GameScores`. Only the items belonging to the current user can be
processed using one of DynamoDB actions that are listed in this policy. Other items in
the table cannot be accessed. Furthermore, only the specific attributes listed in
the policy can be accessed.
