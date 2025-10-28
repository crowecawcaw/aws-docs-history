# Working with data providers, instance profiles,

and migration projects in AWS DMS

When you use DMS Schema Conversion and homogeneous data migrations in AWS Database Migration Service, you work with migration projects. In turn,
AWS DMS migration projects use subnet groups, instance profiles, and data providers.

A _subnet_ is a range of IP addresses in your VPC. A replication _subnet group_
includes subnets from different Availability Zones which your instance profile can use. Note that a
replication _subnet group_ is a DMS resource, and is distinct from subnet groups that
Amazon VPC and Amazon RDS use.

An _instance profile_ specifies network and security settings for the serverless
environment where your migration project runs.

A _data provider_ stores a data store type and the location information
about your database. After you add a data provider to your migration project, you provide the
database credentials from AWS Secrets Manager. AWS DMS uses this information to connect to your database.

After you create data providers, your instance profile, and other AWS resources, you can
create a migration project. A _migration project_ describes your instance profile,
source and target data providers, and secrets from AWS Secrets Manager. You can
create multiple migration projects for different source and target data providers.

You perform most of your work in the migration project. For DMS Schema Conversion, you use a migration project to
assess the objects of your source data provider and convert them to a format compatible
with the target database. Then, you can apply converted code to your target data provider or
save it as a SQL script. For homogeneous data migrations, you use a migration project to migrate data from your
source database to a target database of the same type in the AWS Cloud.

Migration projects in AWS DMS are serverless only. AWS DMS automatically provisions the
cloud resources for your migration projects.

AWS DMS has the maximum number of instance profiles, data providers, and migration projects
that you can create for your AWS account. See the following section for information about
AWS DMS service quotas [Quotas for AWS Database Migration Service](CHAP_Limits.md "CHAP_Limits.md").

###### Topics

- [Creating a subnet group for an AWS DMS migration project](subnet-group.md "subnet-group.md")
- [Creating instance profiles for AWS Database Migration Service](instance-profiles.md "instance-profiles.md")
- [Creating data providers in AWS Database Migration Service](data-providers-create.md "data-providers-create.md")
- [Creating migration projects in AWS Database Migration Service](migration-projects-create.md "migration-projects-create.md")
- [Managing migration projects in AWS Database Migration Service](migration-projects-manage.md "migration-projects-manage.md")
