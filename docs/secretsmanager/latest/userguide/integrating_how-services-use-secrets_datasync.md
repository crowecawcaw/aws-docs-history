# How AWS DataSync uses

AWS Secrets Manager

AWS DataSync is an online data transfer service that simplifies, automates, and accelerates
moving data between storage systems and services.

Some of the storage systems supported by DataSync require credentials to read and write
data. DataSync uses Secrets Manager to store or access storage credentials. You can configure DataSync to
create secrets on your behalf or you can provide a custom secret. Service-managed secrets
begin with the prefix `aws-datasync`. You are charged only for the use of secrets
that you create outside of DataSync. See [Providing credentials for storage
locations](../../../datasync/latest/userguide/location-credentials.md "../../../datasync/latest/userguide/location-credentials.md") in the _AWS DataSync User Guide_.
