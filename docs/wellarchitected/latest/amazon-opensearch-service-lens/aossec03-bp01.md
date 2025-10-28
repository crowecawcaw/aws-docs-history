# AOSSEC03-BP01 Implement fine-grained access control to manage

access to your data on Amazon OpenSearch Service

Control user access to OpenSearch Service domains and dashboards
using fine-grained access control, and only provide sensitive data
access to authorized users.

**Level of risk exposed if this best practice
is not established:** High

**Desired outcome:** User access to
OpenSearch Service domains and Dashboards is controlled using
fine-grained access control.

**Benefits of establishing this best
practice:**

- **Enhanced data security**:
  Controlling user access to OpenSearch Service domains and
  Dashboards using fine-grained access control verifies that
  sensitive data is only accessible to authorized users,
  maintaining a high level of security.
- **Improved compliance**: By
  implementing fine-grained access control, organizations can meet
  regulatory requirements by providing precise control over who
  has access to specific indexes, documents, or fields within
  OpenSearch Service, reducing the risk of non-compliance.

## Implementation guidance

For added control over who can access your data on OpenSearch Service, fine-grained access control provides several options. For
instance, you might need to restrict search results to only one
index based on the user making the request or hide specific fields
in documents or exclude certain documents entirely.

Fine-grained access control offers a range of benefits, including:

- **Role-based access control:**
  Provides tailored permissions based on individual roles
- **Security at multiple
  levels:** Index, document, and field, giving you
  precise control over data access
- **Multi-tenancy support in OpenSearch
  Dashboards:** Create separate, secure environments
  for different users or organizations
- **HTTP basic authentication for both
  OpenSearch and OpenSearch Dashboards:** Provides an
  additional layer of security.

To understand key concepts and features, see
[Fine-grained
access control in Amazon OpenSearch Service](../../../opensearch-service/latest/developerguide/fgac.md "../../../opensearch-service/latest/developerguide/fgac.md").

### Implementation steps

To enable fine-grained access control on your domain:

- Navigate to the Amazon OpenSearch Service console.
- Create a new domain or modify an existing domain:
  - For a new domain, choose **Create domain**. For an
    existing domain, select the domain name and choose
    **Actions**, then **Edit security configuration**.
  - **For new domains:** If
    you choose Easy create under Domain creation method
    box, then fine-grained access control will be enabled by
    default, and you can't change it. However, if you choose
    Standard create, you have more options available, such
    as Enable fine-grained access control and selecting a
    master user. You can choose the master user to be an IAM
    ARN or a normal user with a username and password. For a
    simple setup, choose **Create master user**.
  - **For existing domains:**
    Choose **Enable fine-grained access control** located
    under Fine-grained access control box. You can choose
    the master user to be an IAM ARN or a normal user with a
    username and password. For a simple setup, choose
    **Create master user**.

- Continue with other desired options
- Choose **Create** or **Save changes**.
