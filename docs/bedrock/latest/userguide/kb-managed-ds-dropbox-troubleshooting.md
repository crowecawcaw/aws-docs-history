

# Troubleshoot a Dropbox data source

Use this page to diagnose common issues with Dropbox authentication and syncing. For issues specific to document-level access control, see [Troubleshooting Dropbox ACL awareness](kb-managed-ds-dropbox-acl.md#kb-managed-ds-dropbox-acl-troubleshooting).

## Authentication and data source creation errors
<a name="kb-managed-ds-dropbox-troubleshooting-auth"></a>

The following table describes common authentication and configuration errors, their likely causes, and how to fix them.


**Authentication and configuration errors**  

| Symptom | Likely cause | Fix | 
| --- | --- | --- | 
| CreateDataSource fails because the secret is missing a required field. | The secret does not contain all of clientId, clientSecret, and refreshToken, or a key is misspelled. | Store all three keys, with exactly these names. See [Step 5: Create the AWS Secrets Manager secret](kb-managed-dropbox-auth-setup.md#kb-managed-dropbox-auth-step5). | 
| CreateDataSource fails because the secret cannot be read. | The knowledge base execution role lacks secretsmanager:GetSecretValue on the secret (or kms:Decrypt on its customer managed AWS KMS key), or the secret is in a different Region. | Grant the permissions, and create the secret in the knowledge base's Region. | 
| The sync fails with an access denied error that says the credentials were rejected. | Dropbox rejected the refresh token (invalid\_grant): the app was revoked or deleted, the token belongs to a different app than clientId, or the token was copied incorrectly. | Authorize the app again and update refreshToken in the secret. See [Step 3: Authorize the app and get a refresh token](kb-managed-dropbox-auth-setup.md#kb-managed-dropbox-auth-step3). | 
| A TEAM\_ADMIN sync fails because the token is not a team token. | The refresh token is user-linked because the app has no team scopes, or because you authorized it as a user who is not a team admin. | Grant the TEAM\_ADMIN scopes, and authorize the app as a team admin. | 
| The sync fails with a missing-scope error. | A required scope was not granted, or was granted after the refresh token was issued. | Grant the scope on the app's Permissions tab, then authorize the app again and update refreshToken. | 
| CreateDataSource rejects the configuration. | The configuration combines fields that cannot be used together, such as a path filter with a dataEntityConfiguration field, or team-only fields with OAUTH2. | See [Configuration rules](kb-managed-ds-dropbox-connect.md#kb-managed-dropbox-config-rules). | 

## Missing or skipped content
<a name="kb-managed-ds-dropbox-troubleshooting-content"></a>

The following table describes why expected content might not be in the knowledge base.


**Missing or skipped content**  

| Symptom | Likely cause | Fix | 
| --- | --- | --- | 
| CreateDataSource rejects a folder path. | The inclusionFolderPaths entry does not start and end with /. | Add a leading and trailing /, for example /Finance/Reports/. | 
| A sync completes with 0 documents. | The filters match nothing. Either a path does not exist in the Dropbox it is looked up in, or the member, MIME type, or date filters exclude every file. | Check the paths in Dropbox and widen the filters. A path that does not exist matches nothing and does not fail the sync. | 
| A folder path in a TEAM\_ADMIN data source finds nothing. | Each path is looked up in the Dropbox of each team member in scope, so a path that none of those members can see matches nothing. | Add a member who has the folder in their Dropbox to inclusionUserEmailAddresses, or remove the member filter. | 
| A folder path in an OAUTH2 data source finds nothing, and the user has an individual Dropbox account (Basic, Plus, or Essentials plan). | The path does not start with the user's member folder name. | Prefix each path with the display name on the user's Dropbox account, for example /Alice Smith/Projects/Handbook/. See [Folder paths for individual Dropbox accounts](kb-managed-ds-dropbox-connect.md#kb-managed-dropbox-individual-paths). | 
| An OAUTH2 data source does not crawl a team folder or shared folder. | The authorizing user cannot see it in their Dropbox. | Share the folder with that user, or use TEAM\_ADMIN. | 
| Some files are reported as skipped. | The file is larger than maxFileSizeInMegaBytes, is excluded by a MIME type filter, or has a file type that the knowledge base cannot parse. | Skipped files appear in the ingestion job's statistics. Adjust the filters if the files should be crawled. | 

## Sync performance
<a name="kb-managed-ds-dropbox-troubleshooting-performance"></a>

The following table describes a common sync performance issue and how to resolve it.


**Sync performance issues**  

| Symptom | Likely cause | Fix | 
| --- | --- | --- | 
| A first sync takes hours on a large team. | Without filters, a TEAM\_ADMIN data source downloads every file in every member's folders, including folders shared with them, and every team folder. | Scope the crawl with dataEntityConfiguration, the member filters, or the path filters, and exclude large or unparseable file types with excludeMimeTypes and maxFileSizeInMegaBytes. See [Connector parameters](kb-managed-ds-dropbox-connect.md#kb-managed-config-dropbox). | 