

# Troubleshooting

**Migration Now Open**  
 AWS Agent Registry has launched under the new `agent-registry` namespace. Support for the public preview `bedrock-agentcore` namespace will be discontinued on October 30, 2026. For migration instructions, see [Comprehensive registry migration guide](registry-faq.md).

## Schema validation errors
<a name="registry-troubleshooting-schema-validation"></a>

When creating different types of records, you may see validation exception for the descriptors. See [Supported record types](registry-supported-record-types.md) section for valid schemas.

Common errors:
+ "Schema version '0.3.0' is not supported for descriptor type 'a2a'." — The schemaVersion field value should be `0.3` instead of `0.3.0`. This aligns with the [official A2A protocol version description](https://a2a-protocol.org/latest/specification/#446-agentinterface) on the A2A Protocol website: "Use the latest supported minor version per major version".
+ "Schema validation failed: content is not in compliance with schema version '0.3' for descriptor type 'a2a'." — You can find the schema on [Supported record types](registry-supported-record-types.md). Note that the content will be validated against \#/definitions/AgentCard in the json schema.

## Record synchronization errors
<a name="registry-troubleshooting-sync-errors"></a>

When you create or update record using synchronization feature, the record may transition to CREATE\_FAILED or UPDATE\_FAILED status, with a `statusReason` explaining what happened.

At high level, errors can be categorized as: permission errors, connection errors, validation errors, and server side errors.

### Permission errors
<a name="registry-troubleshooting-sync-permission"></a>

Synchronization configuration is wrong or expired:
+ "Unable to connect to MCP server because caller credentials have expired." — Your credentials for the create or update API have expired. You can retry with the UpdateRegistryRecord API.
+ "Received exception from GetWorkloadAccessToken API: <detailed message>" — The registry calls the [GetWorkloadAccessToken](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_GetWorkloadAccessToken.html) API on your behalf. Refer to the detailed message for the specific error. See [Synchronize records from external sources](registry-sync-records.md) if you see an access denied error.
+ "Unable to parse credential provider ARN: <arn>" — The credential provider ARN is malformed. Provide a valid [credential provider](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/identity-outbound-credential-provider.html) ARN created from AgentCore Identity.
+ "Received exception from GetResourceOauth2Token API: <detailed message>" — The registry calls the [GetResourceOauth2Token](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_GetResourceOauth2Token.html) API on your behalf. Refer to the detailed message for the specific error. See [Synchronize records from external sources](registry-sync-records.md) if you see an access denied error.
+ "Unable to assume the provided IAM role for MCP server authorization." — The registry calls the AssumeRole API on your behalf. See [Synchronize records from external sources](registry-sync-records.md) for the expected IAM permissions. For example, you must have the `iam:PassRole` permission.

### Connection errors
<a name="registry-troubleshooting-sync-connection"></a>

Can’t reach the server:
+ "Failed to fetch agent card from URL: %s" — A2A IOException
+ "MCP server returned HTTP <code>" — non-200/202 HTTP response from the MCP server. Please check if the URL is correct and the MCP server can be connected.
+ If the status code is 401 or 403, verify that you have configured the correct credential provider and that your credentials have permission to connect to the MCP server. To troubleshoot, acquire the credentials manually and connect directly to the MCP server.
+ "The provided URL resolves to a non-public IP address" — Registry only supports connecting to public IP address servers.
+ "Failed to connect to MCP server" — IOException/connection failure
+ "Invalid MCP server URL" — malformed URL
+ "Failed to initialize MCP connection" — initialize request exception
+ "Failed to send initialized notification" — notification exception
+ "Failed to list tools from MCP server" — tools/list exception
+ "MCP server tools/list pagination timed out" — registry only supports at most 30 seconds when paginating tools from MCP server. Contact AWS support if your MCP server needs more time for synchronization.

### Validation errors
<a name="registry-troubleshooting-sync-validation"></a>

Server responded but content is not supported:
+ "Failed to parse agent card JSON" — A2A content empty or malformed JSON
+ "Agent card exceeds maximum size limit" — A2A response too large
+ "Failed to parse MCP server response JSON" — MCP content empty or malformed
+ "MCP server returned invalid response: missing result" — MCP JSON-RPC missing result
+ "MCP server response exceeds maximum allowed size" — MCP response too large
+ "Descriptor type %s does not support URL synchronization" — unsupported descriptor type

### Server side errors
<a name="registry-troubleshooting-sync-server"></a>
+ "Unknown error" — This is a server side error. Please retry later or contact AWS support for help.

## Skill package and skill synchronization errors
<a name="registry-troubleshooting-skills"></a>

Errors with skill packages and skill synchronization reach you in one of two ways:
+  **Request errors** — `CreateRegistryRecord` or `UpdateRegistryRecord` fails immediately, usually with a `ValidationException`, and the registry doesn’t make the change.
+  **Status reasons** — AWS Agent Registry accepts the request, and then validates the package or reads the source. If that fails, the record’s status becomes `CREATE_FAILED` or `UPDATE_FAILED`, and its `statusReason` explains why. Call `GetRegistryRecord` to read the status reason. A record in `UPDATE_FAILED` status keeps serving its last package, unless the failed update switched between an uploaded package and a synchronized package. After you fix the cause, update the record again: upload the package again, or set `triggerSynchronization` to `true` to read the source again.

Error messages and status reasons don’t quote the source URL, the bucket, the object key, the repository, or the IAM role.

### Package upload errors
<a name="registry-troubleshooting-skills-upload"></a>

 `CreateRegistryRecord` and `UpdateRegistryRecord` return these errors for a request that uploads a package (`artifact`):
+ "The skill package is <size> bytes, which exceeds the maximum of <maximum> bytes. Reduce the size of the package and retry." — The package must be at most 5 MiB, measured before base64 encoding. See [Skill package limits](bedrock-agentcore-limits.md#registry-skill-package-limits). A package that is much larger can fail with a generic validation error, or with HTTP status 413, instead of this message.
+ "The skill package is not a ZIP archive. Provide a valid ZIP archive and retry." — The content must be a `.zip` archive. AWS Agent Registry validates the rest of the package after it accepts the request. See [Package validation failures](#registry-troubleshooting-skills-validation).
+ An empty `artifact.content` fails with a `ValidationException` before AWS Agent Registry checks the package.
+ "artifact.sha256 does not match the SHA-256 of the supplied skill package." — If you send `artifact.sha256`, which is optional, it must be the SHA-256 checksum of the package, as 64 lowercase hexadecimal characters.
+ "artifact is supported only on records with recordType SKILL." — Only skill records can have a package.
+ "A request can upload a skill package or synchronize from an s3:// skill source, not both. Send the artifact without triggerSynchronization or a new skill source to upload, or omit the artifact to synchronize." — A record gets its content from one source. For a GitHub source, the message says "a GitHub skill source".
+ "The request body did not arrive in time. Retry the request." (HTTP 408) — The upload was too slow. Retry the request.

### Package validation failures
<a name="registry-troubleshooting-skills-validation"></a>

 AWS Agent Registry validates every skill package before it serves it, whether you uploaded the package or AWS Agent Registry synchronized it from Amazon S3 or GitHub. When a package fails validation, the record’s `statusReason` starts with `The skill package failed validation.`, followed by up to five of the problems found, separated by semicolons. After the problems, `More problems were found.` follows if there were more than five.
+ A problem that concerns one file or folder in the package ends with `Entry:` and the entry’s path. If the registry uses a customer managed key, the status reason leaves out entry names. When a listed problem concerns an entry, the status reason includes `Entry names are not shown because the registry uses a customer managed key.` 
+ A problem that starts with `The package could not be fully checked:` means that a check couldn’t finish. The registry rejects the package as if the check had failed.

The following are common problems:
+ "The package has no SKILL.md at its root or at the top of a single top-level directory." — Put `SKILL.md` at the root of the archive, or directly inside a single top-level folder.
+ "The package has more than one top-level entry and no SKILL.md at its root." — When `SKILL.md` is inside a top-level folder, the archive must contain only that folder. Remove other top-level files and folders, such as `__MACOSX` folders and `.DS_Store` files that some archive tools add, or put `SKILL.md` at the root of the archive.
+ "The SKILL.md frontmatter name does not match its directory under every spelling of the SKILL.md entry name." — When `SKILL.md` is inside a top-level folder, the folder name must be the `name` in the `SKILL.md` frontmatter.
+ "SKILL.md does not begin with a frontmatter fence." — `SKILL.md` must start with a `---` line, with no byte order mark, blank lines, or spaces before it.
+ "The SKILL.md frontmatter name is not lowercase letters and digits joined by single hyphens." — Change the `name` in the frontmatter, for example to `my-skill`.
+ "The SKILL.md frontmatter description is longer than the specification allows." — Shorten the `description` to 1,024 characters or fewer.
+ "The package is larger than the maximum allowed size of 5 MiB.", "The package’s uncompressed size is larger than the maximum allowed size of 50 MiB.", "The entry’s uncompressed size is larger than the maximum allowed size of 10 MiB.", or "The package contains more entries than allowed." — Reduce the package to within the limits. See [Skill package limits](bedrock-agentcore-limits.md#registry-skill-package-limits).
+ "The entry is a symbolic link, which is not allowed." — A package can contain only regular files and folders.
+ "The entry’s header marks it encrypted, which is not allowed." or "The entry’s header declares a compression method that is not allowed." — Create the archive without encryption, with Deflate compression or no compression.
+ "The package uses ZIP64 end-of-archive records, which are not accepted." — Create the archive without ZIP64 records.

For the complete rules, see [Skill package format and validation](registry-skill-package-format.md).

### Record name errors
<a name="registry-troubleshooting-skills-name"></a>

A skill synchronization sets the record’s name to the `name` in SKILL.md. For an Amazon S3 or a GitHub source, the record’s `statusReason` can be one of the following:
+ "A record with name '<name>' and version '<version>' already exists in registry <registryId>" — Another record in the registry already has this name at the same record version. If the record has no record version, the message leaves out the version. Rename the skill in its SKILL.md, give one of the records another record version, or delete the other record, and then synchronize again.
+ "Unable to synchronize the skill: its SKILL.md name starts with aws-autodetected-, a prefix reserved for records that auto-detection creates. Give the skill another name in its SKILL.md." — Rename the skill in its SKILL.md, and then synchronize again.

### Amazon S3 synchronization errors
<a name="registry-troubleshooting-skills-s3"></a>

 `CreateRegistryRecord` and `UpdateRegistryRecord` return these errors for an Amazon S3 source:
+ "The s3:// source URL must name a single object, in the form s3://{bucket}/{key}." — The URL must name one object by bucket name and key. A prefix that ends with `/` or an access point ARN isn’t accepted.
+ "An s3:// agentSkillsDefinition.additionalData.skillMd.source must name a SKILL.md or skill.md object, such as s3://{bucket}/{folder}/SKILL.md." — To synchronize a `.zip` package, set `skillPackage.source` instead.
+ "An s3:// source takes no credential provider, for a public object, or exactly one, of type IAM, with iamCredentialProvider.roleArn set." — Use one IAM credential provider with a role ARN, or none for a public object.
+ "An Amazon S3 skill source with no credential provider is read as a public object, which requires agentSkillsDefinition.additionalData.sourceConfiguration.s3.bucketOwnerAccountId, the AWS account that owns its bucket." — Set `bucketOwnerAccountId`, or add an IAM credential provider.
+ "For an s3:// source, roleArn must be a valid IAM role ARN." or "For an s3:// source, roleArn must be in the same partition as the registry." — Use the ARN of an IAM role in the registry’s partition.
+ "For an s3:// source, iamCredentialProvider.service must be omitted or set to s3." or "For an s3:// source, iamCredentialProvider.region must be omitted or set to <Region>, the registry’s region." — Omit `service` and `region`.
+ "agentSkillsDefinition.additionalData.sourceConfiguration.s3 applies only to an Amazon S3 skill source without repositoryProvider: skillPackage.source when set, otherwise skillMd.source. Remove it for any other source."
+ "agentSkillsDefinition.additionalData.sourceConfiguration must contain exactly one member: s3, for an Amazon S3 skill source."
+ "repositoryProvider <repositoryProvider> can’t be used with an s3:// source; remove agentSkillsDefinition.additionalData.repositoryProvider to use an s3:// source."
+ "Cross-account pass role is not allowed" (`AccessDeniedException`) — The IAM role must be in the caller’s account. If the caller lacks `iam:PassRole` on the role, the request also fails with an `AccessDeniedException`. See [Pass the IAM role of an Amazon S3 source](registry-iam-permissions.md#registry-iam-skills-s3).

The record’s `statusReason` reports these errors:

 **Access denied** 
+ "Unable to assume the provided IAM role. Verify that the role exists and that its trust policy allows the Registry service principal to assume it, with aws:SourceAccount and aws:SourceArn conditions that match this registry record." — The role’s trust policy must allow the `agent-registry.amazonaws.com` service principal. If it uses conditions, `aws:SourceAccount` is the account that owns the registry, and `aws:SourceArn` is the ARN of the registry record, not of the registry. See [Synchronize a skill from Amazon S3](registry-skill-sync-s3.md).
+ "Unable to assume the provided IAM role. AWS STS is not activated in this Region for the role’s account; an administrator of that account must activate it."
+ "Unable to read the S3 source object: access was denied. Verify that the IAM role allows s3:GetObject on the object and that the bucket policy allows the role, which a bucket in another account must do explicitly. Verify that the bucket is owned by the account in bucketOwnerAccountId or, when it is not set, by the IAM role’s account. If the role does not have s3:ListBucket on the bucket, a missing object is also reported as access denied."
+ "Unable to read the S3 source object: access was denied to a request without credentials. Verify that the object is public and that the bucket is owned by the account in bucketOwnerAccountId, or add an IAM credential provider whose role can read it. If the bucket cannot be listed publicly, a missing object is also reported as access denied."

 **Encryption** 
+ "Unable to read the S3 source object: its AWS KMS key could not be used. Verify that the key is enabled and that the IAM role is allowed kms:Decrypt on it through Amazon S3. A key in another account must also allow the role in its key policy. An object encrypted with the AWS managed key aws/s3 cannot be read from another account; encrypt it with SSE-S3 or a customer managed key instead."
+ "Unable to read the S3 source object: it is encrypted with an AWS KMS key, which a request without credentials cannot use. Add an IAM credential provider whose role is allowed to read the object and kms:Decrypt on its key."
+ "Unable to read the S3 source object: objects encrypted with customer-provided keys (SSE-C) are not supported." — Encrypt the object with SSE-S3 or SSE-KMS.

 **Bucket owner** 
+ "Unable to read the S3 source object: a source without an IAM credential provider is read as a public object, which requires bucketOwnerAccountId, the AWS account that owns its bucket. Set bucketOwnerAccountId, or add an IAM credential provider whose role can read the object."
+ For a bucket in another account, set `bucketOwnerAccountId` to the account that owns the bucket. Otherwise, AWS Agent Registry expects the bucket to be owned by the IAM role’s account, and the read fails with the access denied reason.

 **Region and location** 
+ "Unable to read the S3 source object: the bucket must be in the registry’s Region (<Region>)." — Copy the object to a bucket in the registry’s Region.
+ "Unable to read the S3 source object: the bucket or the object does not exist." — Check the bucket name and key in the URL.
+ "Unable to read the S3 source object: objects in archived storage classes are not supported. Restore the object or copy it to a storage class that is not archived."

 **Object content** 
+ "The SKILL.md object in the S3 source exceeds the maximum size of 100 KiB."
+ "The skill package object in the S3 source exceeds the maximum size of 5 MiB."
+ "The skill package object in the S3 source is not a zip archive."
+ "The SKILL.md in the source is not valid UTF-8." — Save `SKILL.md` as UTF-8.
+ "The SKILL.md in the source is too large: together with the record’s other descriptors it must fit within 99 KiB." — Shorten `SKILL.md` or the record’s other descriptors.

 **Temporary errors** 
+ "Unable to read the S3 source object: Amazon S3 is throttling requests to it. Retry the synchronization later. If the bucket is yours, reduce the request rate on the object’s prefix."
+ "Unable to read the S3 source object: Amazon S3 is temporarily unavailable. Retry the synchronization."

 **Other errors** 
+ "Unable to read the S3 source object: Amazon S3 rejected the request."

When a synchronization reads only `SKILL.md`, a `SKILL.md` that breaks a frontmatter rule fails with a single status reason: `agentSkillsDefinition.additionalData.skillMd:`, followed by the first problem, in the same text as for a package. See [Package validation failures](#registry-troubleshooting-skills-validation).

### GitHub synchronization errors
<a name="registry-troubleshooting-skills-github"></a>

 `CreateRegistryRecord` and `UpdateRegistryRecord` return these errors for a GitHub source:
+ "Invalid GitHub source URL: the URL must have the form https://{host}/{owner}/{repo}/tree/{ref}/{path}" — Use the URL of the folder that contains the skill, such as `https://github.com/octo-org/skills/tree/main/my-skill`. A repository URL or a `/blob/` URL isn’t accepted.
+ "Invalid GitHub source URL: the ref is a commit SHA; use a branch or a tag" — The ref after `/tree/` must be a branch or a tag.
+ "Invalid GitHub source URL: the URL must have no user info", "Invalid GitHub source URL: the URL must have no port other than 443", or "Invalid GitHub source URL: the URL must have no query or fragment" — Remove the user name and password, the port, or the query string and fragment from the URL.
+ "Invalid GitHub source URL: the host must be a DNS name, not an IP address", "Invalid GitHub source URL: the host must be a public DNS name, not a reserved or internal one", or "Invalid GitHub source URL: the host must not be in a domain AWS owns" — Use the public host name of the GitHub host, in a domain that you own. See [Make GitHub Enterprise Server reachable](registry-skill-sync-github.md#registry-skill-sync-github-ghes).
+ "Invalid GitHub source URL: a ref or path segment is longer than 255 bytes in UTF-8" — Shorten the branch or tag name, or the folder names in the path.
+ "A GitHub agentSkillsDefinition.additionalData.skillMd.source must name the folder that contains SKILL.md, in the form https://{host}/{owner}/{repo}/tree/{ref}/{path}. Remove the file name from the URL."
+ "A GitHub source takes exactly one credential provider, of type OAUTH, with oauthCredentialProvider.providerArn set." — Add one `OAUTH` entry to `credentialProviderConfigurations`.
+ "A GitHub source requires credentialProvider.oauthCredentialProvider.grantType AUTHORIZATION\_CODE." — A GitHub source is read with the access that a GitHub user authorizes.
+ "credentialProvider.oauthCredentialProvider.providerArn must be in the registry’s account <account>, Region <Region> and partition <partition>" — Create the credential provider in the registry’s account and Region.
+ "credentialProvider.oauthCredentialProvider.returnUrl must be at most 2048 characters, use the https scheme (or http with the host localhost, 127.0.0.1 or [::1]) written in lowercase, name a public domain or one of those hosts rather than an IP address, and have no user info or fragment" — See the `returnUrl` rules in [Choose where the user returns](registry-skill-sync-github.md#registry-skill-sync-github-return-url).
+ "forceAuthentication is only supported when triggerSynchronization is true" — Set `triggerSynchronization` to `true` in the same request.
+ "forceAuthentication is only supported for a GitHub source whose credential provider has grantType AUTHORIZATION\_CODE" — Use `forceAuthentication` only on a record with a GitHub source.
+ "Setting, synchronizing or re-authorizing (forceAuthentication) a GitHub source whose credential provider uses grantType AUTHORIZATION\_CODE is only supported for a request from the registry owner’s account. Make the request with credentials from the account that owns the registry."
+ "Setting, synchronizing or re-authorizing (forceAuthentication) a GitHub source whose credential provider uses grantType AUTHORIZATION\_CODE is only supported for a request signed by an IAM role or IAM user. Make the request with the credentials of an IAM role or IAM user."
+ "The caller is not authorized to perform <action>, which grantType AUTHORIZATION\_CODE requires: <reason>" — Add the missing permission. See [Permissions for a GitHub source](registry-iam-permissions.md#registry-iam-skills-github).

The record’s `statusReason` reports these errors:

 **Not found or unreadable** 
+ "The repository, branch or tag, or path was not found, or the GitHub credentials can’t read it." — GitHub reports a private repository that the authorizing GitHub user can’t read as not found. Check the URL, and check that the user can read the repository. To read a private repository, the authorization must include the `repo` scope.
+ "Unable to read the GitHub source: no SKILL.md was found in the skill folder at the resolved branch or tag. Check the path in the source URL." — When you synchronize only `SKILL.md` from GitHub, the file must be named exactly `SKILL.md`.
+ "Unable to synchronize the skill package from GitHub: the path in the source URL is not a folder with files in it at the resolved branch or tag."
+ "Unable to synchronize the skill package from GitHub: the skill folder has no SKILL.md at its top level."
+ "Unable to read the GitHub source: the repository has moved, for example after it was renamed or transferred. Update the source URL to the repository’s new location."
+ "Unable to read the GitHub source: the repository is empty. Push a commit to the branch or tag, then synchronize again."
+ "The source host was not found; check the URL."
+ "Unable to read the GitHub source: GitHub denied access because the repository’s organization enforces SAML single sign-on. The authorized GitHub user must authorize the OAuth App’s access to the organization through single sign-on."
+ "Unable to read the GitHub source: GitHub denied access because the repository’s organization restricts OAuth App access and has not approved the OAuth App. An organization owner must approve it."

 **Ambiguous branch or tag** 
+ "The source URL matches more than one branch or tag; rename one of them or use an unambiguous URL." — Branch and tag names can contain slashes, so a URL can match more than one branch or tag, or a branch and a tag can have the same name. To name the ref without ambiguity, start it with `refs/heads/` for a branch or `refs/tags/` for a tag, for example `https://github.com/octo-org/skills/tree/refs/heads/release/2026.10/my-skill`.

 **Authorization pending or expired** 

A record whose status is `CREATE_PENDING_AUTH` or `UPDATE_PENDING_AUTH` is waiting for a GitHub user to authorize access. Open the `authorizationUrl` that the `CreateRegistryRecord` or `UpdateRegistryRecord` response returned in `authorizationData`, or choose **Authorize on GitHub** in the console, before the link expires. The link works once and expires 10 minutes after the approval starts. If the approval is still in progress when the link expires, the record fails. If another request restarts the same approval, the record follows the new link, for at most 30 minutes in total. For the complete flow, see [Synchronize a skill from GitHub](registry-skill-sync-github.md).

While the record waits, `UpdateRegistryRecord` fails with a `ConflictException`, for example: "Registry record cannot be modified while in <status> state: it is waiting for the user to authorize its synchronization. Update the record with triggerSynchronization set to true to get a new authorization URL, or retry after the authorization completes or expires."

The record’s `statusReason` reports these errors:
+ "Unable to synchronize: the authorization expired before it was completed. Update the registry record with triggerSynchronization to get a new authorization URL."
+ "Unable to synchronize: the authorization did not complete, for example because access was denied. Update the registry record with triggerSynchronization to get a new authorization URL."
+ "Unable to synchronize: the authorization was not completed in time. Update the registry record with triggerSynchronization to get a new authorization URL."
+ "Unable to synchronize from GitHub: the GitHub user hasn’t authorized the credential provider, or the authorization has expired. Update the registry record with triggerSynchronization to get an authorization URL, then authorize the credential provider with it."
+ "Unable to read the GitHub source: GitHub rejected the OAuth access token, which may have been revoked or have expired. Update the registry record with triggerSynchronization to authorize the credential provider again. If the synchronization fails with this error again, also set forceAuthentication."
+ "Unable to read the GitHub source: the caller credentials of the create or update request have expired. Update the registry record to synchronize it again."

GitHub also revokes a token without notice when the same GitHub user approves access more than 10 times for the same OAuth App and scopes. For more information, see [Authorize GitHub access](registry-skill-sync-github.md#registry-skill-sync-github-authorization).

If the console can’t complete the authorization because the link is no longer current, failed, or expired, start a new authorization. Update the record with `triggerSynchronization` and `forceAuthentication` set to `true`.

 **Repository or folder too large** 
+ "Unable to synchronize the skill package from GitHub: the repository is too large. Its files must total at most 50 MiB, and GitHub must list all of them in one response."
+ "Unable to synchronize from GitHub: the repository is too large. Its file listing is larger than 40 MiB."
+ "Unable to synchronize the skill package from GitHub: the skill folder has more than 1000 files."
+ "Unable to synchronize the skill package from GitHub: a file in the skill folder exceeds the maximum file size of 10 MiB."
+ "Unable to synchronize the skill package from GitHub: the skill folder’s files exceed the maximum total size of 50 MiB."
+ "Unable to synchronize the skill package from GitHub: a file in the skill folder is nested more than 8 levels deep."
+ "Unable to synchronize the skill package from GitHub: the zipped skill folder exceeds the maximum package size of 5 MiB."
+ "The SKILL.md file in the GitHub source exceeds the maximum size of 100 KiB."

To synchronize a skill from a large repository, move the skill to a smaller repository, or synchronize it from Amazon S3 instead. See [Skill package limits](bedrock-agentcore-limits.md#registry-skill-package-limits).

 **Unsupported folder content** 
+ "Unable to synchronize the skill package from GitHub: Git LFS files aren’t supported. Commit the skill’s files to the repository without Git LFS."
+ "Unable to synchronize the skill package from GitHub: the skill folder contains a symbolic link, a hard link or another entry that isn’t a file or a folder."
+ "Unable to synchronize the skill package from GitHub: the skill folder contains a Git submodule, which isn’t supported."
+ "Unable to synchronize the skill package from GitHub: a file name in the skill folder contains a backslash."
+ "The SKILL.md in the source folder is a symbolic link; replace it with the file itself."

 **Rate limits and temporary errors** 
+ "Unable to read the GitHub source: GitHub is rate limiting requests for the authorized GitHub user. Synchronize again after <time>." — Wait until the time shown, in UTC, and then synchronize again.
+ "Unable to synchronize the skill package from GitHub: GitHub is temporarily throttling archive downloads. Synchronize again later."
+ "Unable to read the GitHub source: GitHub returned a server error. Synchronize again later."
+ "Unable to read the GitHub source: GitHub didn’t respond in time. Synchronize again later."
+ "Unable to synchronize the skill package from GitHub: the repository’s archive couldn’t be downloaded from GitHub. This is usually temporary. Synchronize again later."

 **GitHub Enterprise Server** 

A GitHub Enterprise Server must be reachable from the internet over HTTPS on port 443, under the host name that it’s configured with, with a certificate from a public certificate authority.
+ "Unable to read the GitHub source: the GitHub Enterprise Server’s TLS certificate isn’t trusted. It must be issued by a public certificate authority for the server’s host name."
+ "Unable to read the GitHub source: the GitHub Enterprise Server’s host name resolves to an address that isn’t public. The server must be reachable from the internet."
+ "Unable to read the GitHub source: the GitHub Enterprise Server, or a proxy in front of it, returned an invalid response, such as a sign-in page or a redirect. The source URL must reach the server’s API directly, with no proxy or sign-in page answering in its place."
+ "Unable to synchronize the skill package from GitHub: the GitHub Enterprise Server redirected the archive download to a location other than its own archive host. Use the host name the server is configured with in the source URL."

### Customer managed key errors
<a name="registry-troubleshooting-skills-kms"></a>

For a registry encrypted with a customer managed key, requests that upload a package, synchronize a skill package, or return a download URL can fail with the following errors. A message can be followed by the AWS KMS error code and, for some errors, the request ID.
+ "Caller lacks access to the KMS key." — The caller needs `kms:GenerateDataKey` to upload or synchronize a package, and `kms:Decrypt` to read a record. See [Permissions for registries encrypted with a customer managed key](registry-iam-permissions.md#registry-iam-skills-kms).
+ "The KMS key is disabled. Enable the key to continue using encryption."
+ "The KMS key is in an invalid state (e.g., pending deletion or pending import)." — If the key is pending deletion, cancel the deletion and enable the key.
+ "The KMS key was not found. Verify the key ARN is correct and the key exists."

Requests that upload a package or return a download URL can also fail with this error:
+ "The KMS key’s policy or grants do not allow Agent Registry to use the key for this registry. Check the key policy, resource control policies and the registry’s grant." — AWS Agent Registry can no longer use the key for the registry.

A failed synchronization reports the key problem in `statusReason`, for example:
+ "Unable to process the registry record because the KMS key associated with the registry is disabled."
+ "Unable to process the registry record because the KMS key associated with the registry could not be accessed."
+ "Unable to process the registry record because the KMS key associated with the registry is in an invalid state (for example, pending deletion or pending import)."
+ "Unable to process the registry record because the KMS key associated with the registry could not be found. It may have been deleted or is not available in this Region."

See [Behavior when a key becomes unavailable](registry-data-encryption.md#registry-encryption-key-unavailable).

## Auto-detection errors
<a name="registry-troubleshooting-auto-detection"></a>

### "Creating an organization-scoped registry requires the caller to be part of an AWS Organization."
<a name="registry-troubleshooting-auto-detection-not-in-org"></a>

The account creating the registry isn’t a member of an AWS Organization (for example, it’s a standalone account). Create the registry from an account that belongs to your organization.

### "Auto-detection preconditions are not satisfied for this organization."
<a name="registry-troubleshooting-auto-detection-preconditions"></a>

The organization doesn’t yet meet the auto-detection preconditions, or they haven’t finished propagating. Confirm that trusted access is enabled for auto-detection and that you’re creating the registry from the management account or a registered delegated administrator, then retry after a short wait. See [Enabling auto-detection across your organization](registry-organizations.md#registry-organizations-enabling).

### "An organization-scoped registry already exists for this account."
<a name="registry-troubleshooting-auto-detection-already-exists-account"></a>

This account already owns an organization-scoped registry, and an account can have only one. Use the existing registry, or delete it before creating another. If you can’t find the registry in this account, see [Locating an existing organization-scoped registry](#registry-troubleshooting-auto-detection-find-existing).

### "Another organization-scoped registry with active auto-detection already exists for this organization."
<a name="registry-troubleshooting-auto-detection-already-exists-org"></a>

Another account in your organization already owns an organization-scoped registry with active auto-detection, and an organization can have only one at a time. For security reasons, the error message does not name the account that owns the existing registry. To find it and choose how to resolve the conflict, see [Locating an existing organization-scoped registry](#registry-troubleshooting-auto-detection-find-existing).

### Locating an existing organization-scoped registry
<a name="registry-troubleshooting-auto-detection-find-existing"></a>

When `CreateRegistry` reports that an organization-scoped registry already exists — either in your account or somewhere else in your organization — the error does not name the specific registry or the account that owns it. Find the existing registry first, then decide how to resolve the conflict.

An organization-scoped registry is normally owned by one of these accounts:
+ The organization’s **management account**.
+ The account currently registered as the **delegated administrator** for AWS Agent Registry.

Ask an administrator with access to those accounts to list registries in the same Region as the failing call, and look for one whose `autoDetectionConfiguration.scope` is `ORGANIZATION`:

```bash
aws agent-registry-control list-registries --region us-east-1
```

From the management account, confirm which account is currently the delegated administrator:

```bash
aws organizations list-delegated-administrators \
  --service-principal agent-registry.amazonaws.com
```

The conflict only applies within the same Region — a registry in `us-east-1` does not prevent creating one in `us-west-2`.

Once you locate the existing registry, choose one of the following paths:
+  **Share and reuse it.** Have the owning account grant your account access using AWS RAM, and manage records in the shared registry instead of creating a new one. See [Sharing a registry across accounts with AWS RAM](registry-cross-account-sharing.md).
+  **Free the slot without deleting.** The owning account sets `autoDetectionConfiguration.enabled` to `false` on the existing registry; after the update takes effect, retry `CreateRegistry`. See [Disable auto-detection on the registry](registry-organizations.md#registry-organizations-disable).
+  **Delete the existing registry.** If it’s no longer needed, the owning account deletes it. See [Turning off auto-detection](registry-organizations.md#registry-organizations-turning-off) for the teardown order.

### `CreateRegistry` fails even though trusted access is enabled and the delegated administrator is registered
<a name="registry-troubleshooting-auto-detection-slr-missing"></a>

Confirm the management account has the AWS Agent Registry service-linked role (`AWSServiceRoleForAgentRegistry`). It must exist in the management account before an organization-scoped registry can be created, even when the delegated administrator is the one creating it. See [Step 1: Enable trusted access and create the service-linked role](registry-organizations.md#registry-organizations-step1).

### The registry is `READY` but records aren’t appearing
<a name="registry-troubleshooting-auto-detection-no-records"></a>

Confirm the registry’s auto-detection status is `ACTIVE` (with `get-registry`) and that the member accounts contain supported resource types (AgentCore Runtimes or Gateways). Allow time for discovery to complete — on first setup, the initial discovery of preexisting resources can take up to 20 minutes.

### Auto-detection status still shows "The registry’s delegated administrator account was deregistered" after a delegated administrator is re-registered
<a name="registry-troubleshooting-auto-detection-da-deregistered-status"></a>

When the management account deregisters the delegated administrator that owns an organization-scoped registry, AWS Agent Registry turns auto-detection off on that registry and records the status reason `The registry’s delegated administrator account was deregistered.` This status reason describes *why* auto-detection was originally disabled — it is a historical record and is not refreshed when the organization state later changes.

If a delegated administrator is registered again, the registry’s auto-detection does not resume automatically and the status reason continues to display the deregistration message. This is expected in each of the following situations:
+ The same account is re-registered as the delegated administrator.
+ A different account is registered as the delegated administrator — including when that account already owns its own organization-scoped registry with auto-detection previously disabled.
+ No new delegated administrator is registered, and the management account owns an organization-scoped registry directly.

To resume auto-detection, the account that owns the affected registry must explicitly set `enabled` back to `true`. Only one organization-scoped registry per Region can have `autoDetection.status` set to `ACTIVE` in an organization, so if multiple registries are eligible, re-enable auto-detection only on the one you want to keep active.

```bash
aws agent-registry-control update-registry \
  --registry-id <registry-id-or-arn> \
  --auto-detection-configuration '{"optionalValue":{"scope":"ORGANIZATION","enabled":true}}' \
  --region us-east-1
```

For the full lifecycle, see [Turning off auto-detection](registry-organizations.md#registry-organizations-turning-off).

### "Registry cannot be deleted while auto-detection is enabled. Disable auto-detection first."
<a name="registry-troubleshooting-auto-detection-delete-blocked"></a>

You must disable auto-detection before you can delete an organization-scoped registry. To delete the registry, complete these steps in order:

1. Disable auto-detection on the registry (set `autoDetectionConfiguration.enabled` to `false`).

1. Delete all registry records.

1. Delete the registry.

For more information, see [Disable auto-detection on the registry](registry-organizations.md#registry-organizations-disable).