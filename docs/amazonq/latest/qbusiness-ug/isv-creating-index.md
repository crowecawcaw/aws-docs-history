# Creating an Amazon Q index on behalf of a

customer

We recommend creating one Amazon Q Business application environment per customer for better security
and data segregation. Alternatively, you can create one Amazon Q Business application environment and
share it with multiple customers. This is only recommended when you index documents that
are visible to all users in your application.

###### Topics

- [Determine the identity
  management for your customer's Amazon Q Business application](#isv-creating-index-identity-management "#isv-creating-index-identity-management")
- [Calling the SearchRelevantContent API to an
  Amazon Q index with an IAM Identity Center application environment](#isv-calling-api-idc "#isv-calling-api-idc")
- [Calling the SearchRelevantContent API on an
  Amazon Q application environment with IAM Federation](#isv-calling-api-iam "#isv-calling-api-iam")

## Determine the identity

management for your customer's Amazon Q Business application

All Amazon Q Business application environments require user access through AWS Identity and Access Management (IAM)
identity management. You can choose one of two types of user IAM identity management
methods supported by Amazon Q Business. These are IAM Identity Center and IAM Federation.
Both IAM Identity Center and IAM Federation require an external identity provider
setup to allow end users to log in through their identity provider.

IAM Identity Center provides advanced user group management, while Identity and
Access Management (IAM) Federation provides more service quotas for the external
identity providers. You can choose the identity management that's best suited for
you and your end customer when creating their Amazon Q Business application environment. For more
information, see [Configuring an
Amazon Q Business application environment using AWS IAM Identity Center](create-application.md "create-application.md") and [Creating an
Amazon Q Business application environment using Identity Federation through IAM](create-application-iam.md "create-application-iam.md")

After the Amazon Q Business application environment is created, set up the retriever and connect the
data sources. For a complete list of data source connectors,see [supported connectors](connectors-list.md "connectors-list.md"). You will need your customers to provide the relevant
credentials for each connector that you intend to retrieve data from. For more
information, see [Creating a retriever for an
Amazon Q Business application](select-retriever.md "select-retriever.md") and [Connecting Amazon Q Business data
sources](data-sources.md "data-sources.md").

## Calling the SearchRelevantContent API to an

Amazon Q index with an IAM Identity Center application environment

Before end users can retrieve content from the Amazon Q index that you have been
granted access to, you need to be able to make authenticated Amazon Q Business API calls,
like the `SearchRelevantContent` API operation.

To do this you, must complete the steps in [Make
authenticated Amazon Q Business API calls using IAM Identity Center](making-sigv4-authenticated-api-calls.md "making-sigv4-authenticated-api-calls.md").

###### Note

Use the instructions from the previous topic, but modify the
`QBusinessConversationPermission` permission by adding the
additional action `, "qbusiness:SearchRelevantContent"` to the list
of allowed actions, as shown in the following sample snippet of the full
permission.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "QBusinessConversationPermission",
 "Effect": "Allow",
 "Action": [
 "qbusiness:Chat",
 "... ",
 "qbusiness:SearchRelevantContent"
 ]
 }
 ]
}`

```

When configuring access scopes for your Amazon Q Businessapplication environment, add the following
using the AWS CLI to enable calling the `SearchRelevantContent` API:

```

    aws sso-admin put-application-access-scope \
    --application-arn identity-center-custom-application-arn \
    --scope "qbusiness:conversations:access"

    aws sso-admin put-application-access-scope \
    --application-arn identity-center-custom-application-arn \
    --scope "qbusiness:content:access"

```

The following AWS CLI example shows how to call this
`SearchRelevantContent` API operation after you have these
credentials.

```

    aws qbusiness search-relevant-content \
      --application-id ${qbusiness_application_id} \
      --query-text "What is Amazon Q?" \
      --content-source '{"retriever": {"retrieverId": "${retriever_id"}}'

```

## Calling the SearchRelevantContent API on an

Amazon Q application environment with IAM Federation

Before end users can retrieve content from the Amazon Q index that you have been
granted access to, you need to be able to make authenticated Amazon Q Business API calls,
like the `SearchRelevantContent` API operation.

To do this, complete the steps in [Make authenticated Amazon Q Business API calls using IAM federation](making-sigv4-authenticated-api-calls-iam.md "making-sigv4-authenticated-api-calls-iam.md").

###### Note

Use the instructions in the previous topic, but modify the
`trustpolicyforfederation` policy by adding the additional
action, `"qbusiness:SearchRelevantContent"` to the list of allowed
actions, as shown in the following sample snippet of the full permission.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "QBusinessConversationPermissions",
 "Effect": "Allow",
 "Action": [
 "qbusiness:Chat",
 "qbusiness:SearchRelevantContent"
 ],
 "Resource": "arn:aws:qbusiness:us-east-1:111122223333:application/`application-id`"
 }
 ]
}`

```

The following AWS CLI; example shows how to call this
`SearchRelevantContent` API operation after you have these
credentials.

```

    aws qbusiness search-relevant-content \
      --application-id ${qbusiness_application_id} \
      --query-text "What is Amazon Q?" \
      --content-source '{"retriever": {"retrieverId": "${retriever_id"}}'

```
