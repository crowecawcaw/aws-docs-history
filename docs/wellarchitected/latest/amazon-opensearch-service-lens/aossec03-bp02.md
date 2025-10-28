# AOSSEC03-BP02 Secure your indices, documents, and fields using

fine-grained access control

Protect sensitive data in Amazon OpenSearch Service by implementing
fine-grained access control to secure indices, documents, and
fields.

**Level of risk exposed if this best practice
is not established:** High

**Desired outcome:** Indices,
documents, and fields on Amazon OpenSearch Service are secured using
fine-grained access control.

**Benefits of establishing this best
practice:**

- **Improved data security**:
  Implementing fine-grained access control to secure indices,
  documents, and fields in Amazon OpenSearch Service verifies that
  sensitive data is only accessible to authorized users.
- **Enhanced compliance**: By
  setting up strict access controls on specific data using
  fine-grained access control, organizations can meet regulatory
  requirements and reduce the risk of non-compliance.

## Implementation guidance

With fine-grained access control, you can implement strict access
controls on your indices, documents, and fields in Amazon OpenSearch Service. This verifies that only authorized users have
access to specific data.

To set up these controls, navigate through OpenSearch Dashboards
to create roles, map users, configure permissions, and define
filter queries. For a detailed step-by-step guide on how to
implement field-level security or document-level security, see
[Field-level
security in Amazon OpenSearch Service](https://aws.amazon.com/blogs/big-data/field-level-security-in-amazon-opensearch-service/ "https://aws.amazon.com/blogs/big-data/field-level-security-in-amazon-opensearch-service/"),
[Document-level
security](https://opensearch.org/docs/latest/security/access-control/document-level-security/ "https://opensearch.org/docs/latest/security/access-control/document-level-security/") and
[Field-level
security](https://opensearch.org/docs/latest/security/access-control/field-level-security/ "https://opensearch.org/docs/latest/security/access-control/field-level-security/").

## Resources

- [Document-level
  security (DLS)](https://opensearch.org/docs/latest/security/access-control/document-level-security/ "https://opensearch.org/docs/latest/security/access-control/document-level-security/")
