Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Namespaces

In Amazon Redshift Serverless, a namespace defines a logical container for database
objects. It can hold tables, workgroups, and other database resources. If you
haven't created a workgroup and a namespace, and you are looking for instructions in
how to get started with Amazon Redshift Serverless, see [Setting up
Amazon Redshift Serverless for the first time](serverless-console-first-time-setup.md "serverless-console-first-time-setup.md").

## Namespace properties

In Amazon Redshift Serverless, a namespace defines a container for database objects.
You can choose **Namespace configuration** from the
navigation list, choose a namespace from the list, and edit its settings.

General information for the namespace includes the following:

- **Namespace** - The name.
- **Namespace ID** - The unique identifier.
- **ARN** - A unique identifier used to specify the
  resource across AWS. It contains properties like the region and the
  service.
- **Status** - The status, such as
  **Available**.
- **Date created** - The date (UTC) that the namespace was
  created.
- **Storage used** - The storage space used by the
  namespace and all of its objects.
- **Admin user name** - The admin account. This is
  typically the account used to create the namespace.
- **Database name** - The name of the database
  contained by the namespace.
- **Total table count** - The count of tables in all
  schemas.

Additional settings and properties for the namespace are on several tabs.
These include the following:

- **Workgroup** - Shows the workgroup associated with
  the namespace.
- **Data back up** - On this panel, you can configure
  and create snapshots, and configure recovery points.
- **Security and encryption** - You can manage IAM
  role permissions and view or edit your security and encryption settings.
  These include your encryption key status, and the setting to turn on
  audit logging. For more information about audit logging for
  Amazon Redshift Serverless, see [Audit logging for
  Amazon Redshift Serverless](serverless-audit-logging.md "serverless-audit-logging.md").
- **Datashares** - Shows datashares. With data sharing,
  you can provide access to data without the need to copy it or move it.
  For more information about data sharing, see [Data sharing in
  Amazon Redshift Serverless](serverless-datasharing.md "serverless-datasharing.md").
