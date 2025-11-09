# Common Parameters

This section describes parameters used by Amazon SimpleDB operations.

Some parameters are required by all operations and are not repeated in the documentation unless
the usage is unique for that operation. Other parameters are conditional which indicates they are
required for some operations and optional for others.

## Request Parameters

| Name                         | Description                                                                                                                                                                     | Type        |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| `Action`                     | Name of the action.                                                                                                                                                             | Required    |
| `Attribute.X.Name` (REST)    | Name of \*attribute<br>• associated with an item. Required by<br>`PutAttributes` and `BatchPutAttributes`. Optional for<br>`DeleteAttributes` and `BatchDeleteAttributes`.      | Conditional |
| `Attribute.X.Value` (REST)   | Value of attribute associated with an item. Required by<br>`PutAttributes` and `BatchPutAttributes`. Optional for<br>`DeleteAttributes` and `BatchDeleteAttributes`.            | Conditional |
| `Attribute.X.Replace` (REST) | Flag to specify whether to replace the attribute/value or to add a new<br>attribute/value. Used by `PutAttributes` and `BatchPutAttributes`. The default setting is<br>`false`. | Optional    |
| `AttributeName`              | Name of attribute to return. Optional for `GetAttributes`.                                                                                                                      | Conditional |
| `AWSAccessKeyId`             | For more information, see [Request Authentication](RequestAuthentication.md "RequestAuthentication.md").                                                                        | Required    |
| `DomainName`                 | Name of the domain used in the operation.                                                                                                                                       | Required    |
| `ItemName`                   | Unique identifier of an item. Required by `PutAttributes`, `BatchPutAttributes`,<br>`GetAttributes`, `DeleteAttributes`, and `BatchDeleteAttributes`.                           | Conditional |
| `MaxNumberOfDomains`         | The maximum number of domain names you want returned. Used by<br>`ListDomains`. The range is 1 to 100. The default setting is<br>100.                                           | Optional    |
| `MaxNumberOfItems`           | Maximum number of items to return in the response. The range is 1 to 2500.<br>The default setting is 100.                                                                       | Optional    |
| `NextToken`                  | String that tells Amazon SimpleDB where to start the next list of domain or item<br>names. Used by `ListDomains` and `GetAttributes`.                                           | Optional    |
| `SelectExpression`           | String that specifies the query that is executed against the domain.                                                                                                            | Optional    |
| `Signature`                  | For more information, see [Signing REST Requests](HMACAuth.md#REST_RESTAuth "HMACAuth.md#REST_RESTAuth").                                                                       | Required    |
| `SignatureMethod`            | Required when you use signature version 2 with REST requests. For more<br>information, see [Signing REST Requests](HMACAuth.md#REST_RESTAuth "HMACAuth.md#REST_RESTAuth").      | Conditional |
| `SignatureVersion`           | For more information, see [Signing REST Requests](HMACAuth.md#REST_RESTAuth "HMACAuth.md#REST_RESTAuth").                                                                       | Required    |
| `Timestamp`                  | For more information, see [Request Authentication](RequestAuthentication.md "RequestAuthentication.md").                                                                        | Required    |
| `Version`                    | Version of the API. The version of the API described in this document is<br>2009-04-15.                                                                                         | Required    |

## Request Parameter Formats

The following are specifications for Amazon SimpleDB user data:

###### User Data Specifications

- Domain names—Allowed characters are a-z,
  A-Z, 0-9, '\_', '-', and '.' .

Domain names can be between 3 and 255 characters long.

- Item names, attribute names, and attribute
  values—Allowed characters are all UTF-8 characters valid in XML
  documents.

Control characters and any sequences that are not valid in XML are returned
Base64-encoded. For more information, see [Working with XML-Restricted Characters](InvalidCharacters.md "InvalidCharacters.md").

### Quotes and escape characters

User data in query expressions must be enclosed in single quotes. If a single quote is
used within the user data, it must be _escaped_ using a backslash. If a
backslash is used within user data, it must be escaped as well. Examples:

| Original String        | Escaped String          |
| ---------------------- | ----------------------- |
| `'John's AWS account'` | `'John\'s AWS account'` |
| `c:\path\constant`     | `'c:\\path\\constant'`  |
