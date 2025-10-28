# Configuring permissions for

collections

OpenSearch Serverless uses the following AWS Identity and Access Management (IAM) permissions for creating and managing
collections. You can specify IAM conditions to restrict users to specific
collections.

- `aoss:CreateCollection` – Create a collection.
- `aoss:ListCollections` – List collections in the current
  account.
- `aoss:BatchGetCollection` – Get details about one or more
  collections.
- `aoss:UpdateCollection` – Modify a collection.
- `aoss:DeleteCollection` – Delete a collection.
  The following sample identity-based access policy provides the minimum permissions
  necessary for a user to manage a single collection named `Logs`:

```
[
   {
      "Sid":"Allows managing logs collections",
      "Effect":"Allow",
      "Action":[
         "aoss:CreateCollection",
         "aoss:ListCollections",
         "aoss:BatchGetCollection",
         "aoss:UpdateCollection",
         "aoss:DeleteCollection",
         "aoss:CreateAccessPolicy",
         "aoss:CreateSecurityPolicy"
      ],
      "Resource":"*",
      "Condition":{
         "StringEquals":{
            "aoss:collection":"`Logs`"
         }
      }
   }
]
```

`aoss:CreateAccessPolicy` and `aoss:CreateSecurityPolicy` are
included because encryption, network, and data access policies are required in order for
a collection to function properly. For more information, see [Identity and Access Management for
Amazon OpenSearch Serverless](security-iam-serverless.md "security-iam-serverless.md").

###### Note

If you're creating the first collection in your account, you also need the
`iam:CreateServiceLinkedRole` permission. For more information, see
[Using service-linked roles to create
OpenSearch Serverless collections](serverless-service-linked-roles.md "serverless-service-linked-roles.md").
