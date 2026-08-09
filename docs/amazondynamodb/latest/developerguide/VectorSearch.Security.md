# Security and access control

IAM policies control access to vector index operations. The following
permissions apply:

- **Creating and deleting vector indexes** –
  Requires `dynamodb:CreateTable` or
  `dynamodb:UpdateTable` permissions on the table resource. No
  additional permissions are needed for vector index management.
- **Searching a vector index** – Requires
  `dynamodb:SearchVectors` permission on the index resource. The
  resource ARN format is
  `arn:aws:dynamodb:`region`:`account-id`:table/`table-name`/index/`index-name``.
- **Writing items with vectors** – Uses the
  same permissions as standard write operations (`dynamodb:PutItem`,
  `dynamodb:UpdateItem`). No additional permissions are required for
  the vector data itself.

###### FGAC condition keys don't apply to SearchVectors

You can't use Amazon DynamoDB fine-grained access control (FGAC) with the
`SearchVectors` API. The `dynamodb:` IAM condition context
keys that enforce FGAC — such as `dynamodb:LeadingKeys`,
`dynamodb:Attributes`, and `dynamodb:Select` — have no
effect on `SearchVectors`. This means you can't use them to restrict
which items or attributes you can search. Instead, control access at the index
level by granting the `dynamodb:SearchVectors` action on the index
resource ARN.

DynamoDB encrypts vector data at rest using the same encryption as the base table.
The vector index inherits the table's encryption configuration, whether that is an
AWS owned key, an AWS managed key, or a customer managed key in AWS KMS. You do not
configure encryption separately for a vector index.

For example IAM policies, including least-privilege policies for search-only
access, see [IAM
policy to grant access to search a vector index](iam-policy-example-search-vectors.md "iam-policy-example-search-vectors.md").
