# Performing common system

tasks for Amazon RDS for Db2 DB instances

You can perform certain common database administrator tasks related to the system on your
Amazon RDS DB instances running Db2. To deliver a managed service experience, Amazon RDS doesn't
provide shell access to DB instances, and restricts access to certain system procedures and
tables that require advanced privileges.

For information about granting and revoking privileges and attaching to the remote database for RDS for Db2, see the following topics.

###### Topics

- [Granting and revoking privileges for RDS for Db2](db2-granting-revoking-privileges.md "db2-granting-revoking-privileges.md")
- [Attaching to the remote RDS for Db2
  DB instance](db2-attaching-to-remote.md "db2-attaching-to-remote.md")

## Creating a custom database

endpoint

When you migrate to Amazon RDS for Db2, you can use custom database endpoint URLs to minimize
changes to your application. For example, if you use `db2.example.com` as your
current DNS record, you can add it to Amazon Route 53. In Route 53, you can use private hosted zones
to map your current DNS database endpoint to an RDS for Db2 database endpoint. To add a custom
`A` or `CNAME` record for an Amazon RDS database endpoint, see [Registering and
managing domains using Amazon Route 53](../../../Route53/latest/DeveloperGuide/registrar.md "../../../Route53/latest/DeveloperGuide/registrar.md") in the
_Amazon Route 53 Developer Guide_.

###### Note

If you can't transfer your domain to Route 53, you can use your DNS provider to create a
`CNAME` record for the RDS for Db2 database endpoint URL. Consult your DNS
provider documentation.
