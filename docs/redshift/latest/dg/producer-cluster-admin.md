Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# producer administrator actions

With Amazon Redshift, you can perform administrative tasks on producer clusters to manage
data ingestion and load processing.

**If you are a producer administrator or database
owner** – follow these steps:

1. Create datashares in your cluster and add datashare objects to the
   datashares. For more detailed steps on how to create datashares and add
   datashare objects to datashares, see [Sharing read access to data within an
   AWS account](within-account.md "within-account.md"). For information about the CREATE
   DATASHARE and ALTER DATASHARE, see [CREATE DATASHARE](r_CREATE_DATASHARE.md "r_CREATE_DATASHARE.md") and [ALTER DATASHARE](r_ALTER_DATASHARE.md "r_ALTER_DATASHARE.md").

The following example adds different datashare objects to the datashare
`salesshare`.

```
-- Add schema to datashare
ALTER DATASHARE salesshare ADD SCHEMA PUBLIC;

-- Add table under schema to datashare
ALTER DATASHARE salesshare ADD TABLE public.tickit_sales_redshift;

-- Add view to datashare
ALTER DATASHARE salesshare ADD TABLE public.sales_data_summary_view;

-- Add all existing tables and views under schema to datashare (does not include future table)
ALTER DATASHARE salesshare ADD ALL TABLES in schema public;
```

You can also use the Amazon Redshift console to create or edit datashares. For more
information, see [Create a datashare](datashare-creation.md#create-datashare-console "datashare-creation.md#create-datashare-console") and [Editing datashares created in your
account](manage-datashare-existing-console.md#edit-datashare-console "manage-datashare-existing-console.md#edit-datashare-console"). 2. Delegate permissions to operate on the datashare. For more information,
see [GRANT](r_GRANT.md "r_GRANT.md") or [REVOKE](r_REVOKE.md "r_REVOKE.md").

The following example grants permissions to `dbuser` on
`salesshare`.

```
GRANT ALTER, SHARE ON DATASHARE salesshare TO dbuser;
```

Cluster superusers and the owners of the datashare can grant or revoke
modification permissions on the datashare to additional users. 3. Add consumers to or remove consumers from datashares. The following
example adds the AWS account ID to `salesshare`. For more
information, see [GRANT](r_GRANT.md "r_GRANT.md") or [REVOKE](r_REVOKE.md "r_REVOKE.md").

```
GRANT USAGE ON DATASHARE salesshare TO ACCOUNT '123456789012';
```

You can only grant permissions to one data consumer in a GRANT
statement.

Cluster superusers and the owners of datashare objects, or users that
have SHARE permissions on the datashare, can add consumers to or remove
consumers from a datashare. To do so, they use GRANT USAGE or REVOKE
USAGE.

You can also use the Amazon Redshift console to add or remove data consumers for
datashares. For more information, see [Add data consumers to
datashares](datashare-creation.md#add-data-consumer-console "datashare-creation.md#add-data-consumer-console") and [Removing data consumers from
datashares](manage-datashare-existing-console.md#remove-data-consumer-console "manage-datashare-existing-console.md#remove-data-consumer-console"). 4. (Optional) Revoke access to the datashare from AWS accounts if you
don't want to share the data with the consumers anymore.

```
REVOKE USAGE ON DATASHARE salesshare FROM ACCOUNT '123456789012';
```

**If you are a producer account administrator**
– follow these steps:

After granting usage to the AWS account, the datashare status is
`pending_authorization`. The producer account administrator should
authorize datashares using the Amazon Redshift console and choose the data consumers.

Sign in to the [https://console.aws.amazon.com/redshiftv2/](https://console.aws.amazon.com/redshiftv2/ "https://console.aws.amazon.com/redshiftv2/"). Then choose which data consumers to authorize
to access datashares or to remove authorization from. Authorized data consumers
receive notifications to take actions on datashares. If you are adding a namespace
as a data consumer, you don't have to perform authorization. After data
consumers are authorized, they can access datashare objects and create a consumer
database to query the data. For more information, see [Authorizing or removing authorization
from datashares](authorize-datashare-console.md "authorize-datashare-console.md").

## Sharing

write permissions to data across accounts

With Amazon Redshift, you can share data across AWS accounts and grant write
permissions, enabling collaboration and data sharing between teams or
organizations. Cross-account data sharing allows you to establish a data
provider account that creates and manages databases, schemas, and tables, which
can then be securely shared with data consumer accounts. The following sections
demonstrate the process of configuring cross-account data sharing and granting
write access in Amazon Redshift.
