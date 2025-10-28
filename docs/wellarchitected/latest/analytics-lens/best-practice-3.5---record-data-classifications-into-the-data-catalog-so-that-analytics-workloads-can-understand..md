# Best practice 3.5 – Record data classifications into the Data Catalog so that analytics workloads can understand

Allow processes to update the Data Catalog so it can provide
a reliable record of where the data is located and its
precise classification. To protect the data effectively,
analytics systems should know the classifications of the
source data so that the systems can govern the data
according to business needs. For example, if the business
requires that confidential data be encrypted using team-owned
private keys, such as from AWS Key Management Service (AWS KMS), then the analytics workload should be able to
determine which data is classified as confidential by
referencing its data catalog.

## Suggestion 3.5.1 – Use tags to indicate the data classifications

Use a tagging ontology to designate the classiﬁcation of sensitive data in data stores with a data catalog. A tagging ontology allows discoverability of data sensitivity without directly exposing the underlying data.
They also can be used to authorize access in
[tag-based access control (TBAC)](../../../IAM/latest/UserGuide/introduction_attribute-based-access-control.md "../../../IAM/latest/UserGuide/introduction_attribute-based-access-control.md") schemes.

For more details, refer to the following information:

- AWS Lake Formation Developer Guide:
  [What
  Is AWS Lake Formation?](../../../lake-formation/latest/dg/what-is-lake-formation.md "../../../lake-formation/latest/dg/what-is-lake-formation.md")
- AWS Whitepaper: [Tagging
  Best Practices](../../../whitepapers/latest/tagging-best-practices/tagging-best-practices.md "../../../whitepapers/latest/tagging-best-practices/tagging-best-practices.md")
- AWS Lake Formation: [Easily manage your data lake at scale using AWS Lake Formation Tag-based access control](https://aws.amazon.com/blogs/big-data/easily-manage-your-data-lake-at-scale-using-tag-based-access-control-in-aws-lake-formation/ "https://aws.amazon.com/blogs/big-data/easily-manage-your-data-lake-at-scale-using-tag-based-access-control-in-aws-lake-formation/")

## Suggestion 3.5.2 – Record lineage of data to track changes in the Data Catalog

Data lineage is a relation among data and the processing
systems. For example, the data lineage tells where the
source system of the data has come from, what changes
occurred to the data, and which downstream systems have
access to it. Your organization should be able to
discover, record, and visualize the data lineage from
source to target systems.

For more details, refer to the following information:

- AWS Big Data Blog:
  [Metadata
  classification, lineage, and discovery using Apache
  Atlas on Amazon EMR](https://aws.amazon.com/blogs/big-data/metadata-classification-lineage-and-discovery-using-apache-atlas-on-amazon-emr/ "https://aws.amazon.com/blogs/big-data/metadata-classification-lineage-and-discovery-using-apache-atlas-on-amazon-emr/")
