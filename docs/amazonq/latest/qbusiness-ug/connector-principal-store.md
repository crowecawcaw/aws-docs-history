# Understanding Amazon Q Business

User Store

With the Amazon Q Business
_User Store_ feature, end users see Amazon Q Business chat
responses generated _only_ from the documents that
they have access to within an Amazon Q Business application. To achieve this,
Amazon Q creates a mapping within the data sources attached to that
application. The mapping is between every unique user accessing the application environment
and all the user IDs and user groups that they are associated with. Amazon Q Business stores this principal mapping information in its internal User
Store. During chat, Amazon Q Business uses the mapping information to return
answers that are scoped to a user’s identity.

When you use the API, you use the User Store API actions to customize and
configure your user management solution. For more details, see [Using User Store APIs](principal-store-hiw.md#principal-store-hiw-api "principal-store-hiw.md#principal-store-hiw-api").

When you use the console, Amazon Q Business automatically crawls user and
group information during the connector setup process. You can't create, add, or
customize users and groups to the user store using the AWS Management Console.

###### Note

As of Dec 17, 2024, Amazon Q Business will recognize all email addresses
as case-insensitive and recognize subaddresses as equivalent to the original
email address. For example, JohnDoe@example.com, johndoe@example.com, and
johndoe+work@example.com will be considered the same email address. For
assistance with applications or to report a concern, contact Support sign into the
[AWS Support Center](https://console.aws.amazon.com/support/home#/ "https://console.aws.amazon.com/support/home#/") .

###### Note

The User Store feature is not available for the Amazon S3 and Amazon Q Web Crawler connectors that are used with Amazon Q Business. For more information about using access control information for user
identity specific chat responses for these connectors, see [Amazon S3](s3-connector.md#s3-user-management "s3-connector.md#s3-user-management") and [Amazon Q Business Web Crawler](connector-webcrawler.md "connector-webcrawler.md").

###### Topics

- [Principal mapping](principal-mapping.md "principal-mapping.md")
- [How the User Store works](principal-store-hiw.md "principal-store-hiw.md")
