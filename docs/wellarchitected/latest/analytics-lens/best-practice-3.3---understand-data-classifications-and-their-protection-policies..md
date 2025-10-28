# Best practice 3.3 – Understand data classifications and their protection policies

Data classification in your organization is key to
determining how data must be protected while at rest and in
transit. For example, since an analytics workload
necessarily copies and shares data between operations and
systems, we recommend that access be controlled to certain
data classifications. Such a data protection strategy helps
to prevent data loss, theft, and corruption, and helps to
minimize the impact caused by malicious activities or
unintended access.

## Suggestion 3.3.1 – Identify classification levels

Use the
[Data
Classification whitepaper](../../../whitepapers/latest/data-classification/data-classification.md "../../../whitepapers/latest/data-classification/data-classification.md") to help you identify
different classification levels. Four common levels used
are restricted, confidential, internal, and public,
however, these levels can vary based on the industry and
compliance requirements of your organization.

## Suggestion 3.3.2 – Define access rules

The data owners should define the data access rules based
on the sensitivity and criticality of the data. For
example, with AWS Lake Formation, you can define and
enforce access controls that operate at the table, column,
row, and cell level for all the users that access your
data lake.

For more details, refer to the following information:

- AWS Security Blog:
  [How
  to scale your authorization needs by using
  attribute-based access control with](https://aws.amazon.com/blogs/security/how-to-scale-authorization-needs-using-attribute-based-access-control-with-s3/ "https://aws.amazon.com/blogs/security/how-to-scale-authorization-needs-using-attribute-based-access-control-with-s3/")
  [S3](https://aws.amazon.com/blogs/security/how-to-scale-authorization-needs-using-attribute-based-access-control-with-s3/ "https://aws.amazon.com/blogs/security/how-to-scale-authorization-needs-using-attribute-based-access-control-with-s3/").
- AWS Big Data Blog:
  [Create
  a secure data lake by masking, encrypting data, and
  enabling fine-grained access with AWS Lake Formation.](https://aws.amazon.com/blogs/big-data/create-a-secure-data-lake-by-masking-encrypting-data-and-enabling-fine-grained-access-with-aws-lake-formation/ "https://aws.amazon.com/blogs/big-data/create-a-secure-data-lake-by-masking-encrypting-data-and-enabling-fine-grained-access-with-aws-lake-formation/")
- AWS Big Data Blog:
  [Control
  data access and permissions with AWS Lake Formation and
  Amazon EMR](https://aws.amazon.com/blogs/big-data/control-data-access-and-permissions-with-aws-lake-formation-and-amazon-emr/ "https://aws.amazon.com/blogs/big-data/control-data-access-and-permissions-with-aws-lake-formation-and-amazon-emr/").
- AWS Big Data Blog:
  [Enforce
  column-level authorization with Quick Suite and
  AWS Lake](https://aws.amazon.com/blogs/big-data/enforce-column-level-authorization-with-amazon-quicksight-and-aws-lake-formation/ "https://aws.amazon.com/blogs/big-data/enforce-column-level-authorization-with-amazon-quicksight-and-aws-lake-formation/")
  [Formation](https://aws.amazon.com/blogs/big-data/enforce-column-level-authorization-with-amazon-quicksight-and-aws-lake-formation/ "https://aws.amazon.com/blogs/big-data/enforce-column-level-authorization-with-amazon-quicksight-and-aws-lake-formation/").

## Suggestion 3.3.3 – Identify security zone models to isolate data based on classification

Design the security zone models from AWS account levels
down to AWS resource levels. For example, consider
building AWS multi-account models to isolate different
classes of data from AWS account level. Or, you can
consider separating out development and test resources
from production ones from AWS account level or from
resource levels.

For more details, refer to the following information:

- AWS Whitepaper:
  [An
  Overview of the AWS Cloud Adoption Framework](../../../whitepapers/latest/overview-aws-cloud-adoption-framework/welcome.md "../../../whitepapers/latest/overview-aws-cloud-adoption-framework/welcome.md").
- AWS Whitepaper:
  [Organizing
  Your AWS Environment Using Multiple Accounts](../../../whitepapers/latest/organizing-your-aws-environment/organizing-your-aws-environment.md "../../../whitepapers/latest/organizing-your-aws-environment/organizing-your-aws-environment.md").
- AWS Whitepaper:
  [Security
  Pillar – AWS Well-Architected Framework](../security-pillar/welcome.md "../security-pillar/welcome.md").

## Suggestion 3.3.4 – Identify sensitive information and define protection policies

Discover sensitive data by using custom data identifiers in Amazon Macie or using AWS Glue sensitive data detection. Based on
the sensitivity and criticality of the data, implement data protection policies to prevent
unauthorized access. Due to compliance requirements, data might be masked or deleted after
processing in some cases.

For more details, refer to the following information:

- AWS Blog:
  [Introducing
  PII data identification and handling using AWS Glue DataBrew](https://aws.amazon.com/blogs/big-data/introducing-pii-data-identification-and-handling-using-aws-glue-databrew/ "https://aws.amazon.com/blogs/big-data/introducing-pii-data-identification-and-handling-using-aws-glue-databrew/")
- AWS Blog:
  [Create
  a secure data lake by masking, encrypting data, and
  enabling fine-grained access with AWS Lake Formation](https://aws.amazon.com/blogs/big-data/create-a-secure-data-lake-by-masking-encrypting-data-and-enabling-fine-grained-access-with-aws-lake-formation/ "https://aws.amazon.com/blogs/big-data/create-a-secure-data-lake-by-masking-encrypting-data-and-enabling-fine-grained-access-with-aws-lake-formation/")
- AWS Info: [AWS Glue detect and process sensitive data](../../../glue/latest/dg/detect-PII.md "../../../glue/latest/dg/detect-PII.md")
