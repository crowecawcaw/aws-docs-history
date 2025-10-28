# IAM roles for native integration with Apache

Ranger

The integration between Amazon EMR and Apache Ranger relies on three key roles that you
should create before you launch your cluster:

- A custom Amazon EC2 instance profile for Amazon EMR
- An IAM role for Apache Ranger Engines
- An IAM role for other AWS services
  This section gives an overview of these roles and the policies that you need to
  include for each IAM role. For information about creating these roles, see [Set up a Ranger Admin server to integrate with Amazon EMR](emr-ranger-admin.md "emr-ranger-admin.md").
