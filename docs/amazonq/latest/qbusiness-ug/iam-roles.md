# IAM roles for Amazon Q Business

When you create an application or a web experience with Amazon Q Business, or
connect a data source to it, Amazon Q Business needs access to the required AWS resources.

If you use the AWS CLI or an AWS SDK, you must create an AWS Identity and Access Management (IAM)
policy before you create the Amazon Q Business resource. When you call an API
operation, you provide the Amazon Resource Name (ARN) role with the policy attached.

If you use the AWS Management Console, you can create a new IAM role in the Amazon Q console or use an existing IAM role. The console displays
roles that have the string **qbusiness** or **QBusiness**
in the role name.

To learn more about IAM roles, see [IAM roles](../../../IAM/latest/UserGuide/id_roles.md "../../../IAM/latest/UserGuide/id_roles.md") in the _AWS Identity and Access Management User
Guide_.

The following topics provide details for the required policies. If you create IAM roles using the Amazon Q Business console, these policies are created
on your behalf, unless otherwise noted.

###### Topics

- [IAM role for an Amazon Q Business application](create-application-iam-role.md "create-application-iam-role.md")
- [IAM role for an Amazon Q Business web
  experience](deploy-experience-iam-role.md "deploy-experience-iam-role.md")
- [IAM role for Amazon Q Business data
  source connectors](iam-roles-ds.md "iam-roles-ds.md")
- [IAM role for Amazon Q Business
  plugins](plugin-iam-role.md "plugin-iam-role.md")
- [IAM roles for custom document enrichment in
  Amazon Q Business](cde-iam-roles.md "cde-iam-roles.md")
- [IAM role for an Amazon Kendra
  retriever](kendra-retriever-iam-role.md "kendra-retriever-iam-role.md")
