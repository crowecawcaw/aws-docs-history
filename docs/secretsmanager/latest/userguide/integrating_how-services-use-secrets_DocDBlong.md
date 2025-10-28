# How Amazon DocumentDB (with MongoDB compatibility) uses

AWS Secrets Manager

Amazon DocumentDB (with MongoDB compatibility) is a fully managed document database service that supports MongoDB workloads.
Amazon DocumentDB integrates with Secrets Manager to manage primary user passwords for your clusters, enhancing
security and simplifying credential management.

Amazon DocumentDB generates the password, stores it in Secrets Manager, and manages the secret settings.
By default, Amazon DocumentDB rotates the secret every seven days, but you can modify the rotation
schedule if needed. When you create or modify an Amazon DocumentDB cluster, you can specify that it
should manage the primary user password in Secrets Manager. For more information, see [Password management with Amazon DocumentDB and Secrets Manager](../../../documentdb/latest/developerguide/docdb-secrets-manager.md "../../../documentdb/latest/developerguide/docdb-secrets-manager.md") in the
_Amazon DocumentDB Developer Guide_.
