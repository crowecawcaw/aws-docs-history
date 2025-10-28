# DNS | Update Group Managed Service Account

Update an existing Active Directory (AD) Group Managed Service Account (gMSA). For multi-account landing zone (MALZ), use this change type in the shared services account.

**Full classification:** Management | Directory Service | DNS | Update group managed service account

## Change Type Details

|                             |                  |
| --------------------------- | ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Change type ID              | ct-15gyrpzjx1yac |
| Current version             | 1.0              |
| Expected execution duration | 60 minutes       |
| AWS approval                | Required         |
| Customer approval           | Not required     |
| Execution mode              | Automated        | ## Additional Information Info not available. ## Execution Input Parameters For detailed information about the execution input parameters, see [Schema for Change Type ct-15gyrpzjx1yac](schemas.md#ct-15gyrpzjx1yac-schema-section "schemas.md#ct-15gyrpzjx1yac-schema-section"). ## Example: Required Parameters `{ "DocumentName": "AWSManagedServices-UpdateADGroupManagedServiceAccount-Admin", "Region": "us-east-1", "Parameters": { "AccountName": ["Sample-account"] } }` ## Example: All Parameters `{ "DocumentName": "AWSManagedServices-UpdateADGroupManagedServiceAccount-Admin", "Region": "us-east-1", "Parameters": { "AccountName": ["Sample-account"], "PrincipalAllowedToRetrievePassword": ["Sample_Principal"], "ComputerName": ["Sample-Computer"], "DNSHostName": ["test.domain.com"], "KerberosEncryptionType": ["RC4,AES128,AES256"] } }` |
