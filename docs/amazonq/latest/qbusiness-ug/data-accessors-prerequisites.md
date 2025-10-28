# Prerequisites

To add an ISV as a data accessor, complete the following prerequisites:

1. [Get started with
   Amazon Q Business](getting-started.md "getting-started.md")
2. [Create an Identity
   and Access Management (IAM) Identity Center-integrated application](create-application.md "create-application.md")
   (IAM Federated application environments are not supported at this time).
3. Set up the retriever and connect your data sources. For a complete list of
   data source connectors (see [supported
   connectors](connectors-list.md "connectors-list.md")). You need the relevant credentials from each connector
   that you want to retrieve data from. For more information, see [Creating a retriever for an Amazon Q Business application environment](select-retriever.md "select-retriever.md") and [Connecting Amazon Q Business data sources](data-sources.md "data-sources.md").
4. If you are using a customer managed key in your Amazon Q Business Application, you
   must set your key policy to allow the ISV principal access to the KMS key with
   the following policy:

JSON

```
`{
 "Version":"2012-10-17",
 "Id": "isv-key-consolepolicy",
 "Statement": [
 {
 "Sid": "EnableIAMUserPermissions",
 "Effect": "Allow",
 "Principal": {
 "AWS": "arn:aws:iam::111122223333:role/`isv-role`"
 },
 "Action": "kms:Decrypt",
 "Resource": "arn:aws:kms:us-east-1:111122223333:key/`key-id`",
 "Condition": {
 "StringLike": {
 "kms:ViaService": [
 "qbusiness.us-east-1.amazonaws.com"
 ]
 }
 }
 }
 ]
}`

```
