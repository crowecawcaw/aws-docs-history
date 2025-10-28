# Delete Amazon DataZone domains

In Amazon DataZone, a domain is an organizing entity for connecting together your assets,
users, and their projects. For more information, see [Amazon DataZone terminology and concepts](datazone-concepts.md "datazone-concepts.md").

The act of deleting a domain is final. Deletion irrevocably removes every Amazon DataZone
entity, including data sources, projects, environments, assets, glossaries, and metadata
forms. Deletion does not delete non-Amazon DataZone AWS resources that Amazon DataZone may have
helped you create, such as IAM roles, S3 buckets, AWS Glue databases, and subscription
grants via LakeFormation or Redshift. If you no longer need these resources, delete them
in the respective AWS service.

To prevent someone from deleting a domain maliciously, deleting a domain requires
administrative IAM permissions for Amazon DataZone, which you can configure with IAM. To
prevent someone from deleting a domain accidentally, deleting a domain requires a
confirmation word (in the Amazon DataZone console).

To delete a domain, complete the following steps:

1. Sign in to the AWS Management Console and open the Amazon DataZone console at
   [https://console.aws.amazon.com/datazone](https://console.aws.amazon.com/datazone "https://console.aws.amazon.com/datazone").
2. Choose **View domains** and choose the domain’s name from the
   list. The name is a hyperlink.
3. Choose **Delete** and review the informational
   warnings.
4. Type in the requested text to confirm that you understand these warnings.
   Choose **Delete**.

###### Important

Deleting your domain is an irrevocable action that cannot be undone by you or by
AWS.

###### Note

When you or your domain users create an environment in a project, Amazon DataZone
creates AWS resources in your domain or associated accounts to provide you and
your domain users with functionality. Below is the list of AWS resources that
Amazon DataZone may create for projects in your domain, along with the default name.
Deleting a domain does not delete any of these AWS resources in your AWS
accounts.

- IAM roles: datazone_usr\_<environmentId>.
- Glue databases: (1) <environmentName>\_pub_db-\*, (2)
  <environmentName>\_sub_db-\*. If there was already an existing database
  of this name, Amazon DataZone will add the environment ID.
- Athena workgroups: <environmentName>-\*. If there was already an
  existing workgroup of this name, Amazon DataZone will add the environment
  ID.
- CloudWatch log group: datazone\_<environmentId>
