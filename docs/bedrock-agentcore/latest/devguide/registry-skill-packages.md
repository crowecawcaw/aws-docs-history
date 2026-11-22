

# Publish skill packages

A *skill* is a set of instructions that an agent follows to perform a task. A skill is a folder that contains a SKILL.md file. The folder can also contain scripts, reference documents, and assets such as templates that the agent uses with the instructions. SKILL.md starts with YAML frontmatter that names and describes the skill, followed by the instructions in Markdown. For the format of a skill, see the [Agent Skills specification](https://agentskills.io/specification) on the Agent Skills website.

In AWS Agent Registry, you publish a skill as a skill record, a record with the record type `SKILL`. A skill record can hold just the skill’s SKILL.md file, or it can hold the complete skill as a *skill package*, a .zip file of the skill folder. The registry supports only the ZIP format for packages. When a record has a package, you can download the package if you can read the record. You can then install the complete skill, not only read its instructions.

## Ways to provide skill content
<a name="registry-skill-packages-content-sources"></a>

You can provide the content of a skill record in three ways. In the console, you choose the way in **Skill content source**, in the **Skill content** section of the create and edit forms. The create form offers **Author inline** and **Upload a package**; **Synchronize from source** appears when you edit a record. To create a record that synchronizes, choose **Synchronize from source** in the **Record source** section of the **Create record** page instead.

Write SKILL.md (**Author inline**)  
You enter the text of SKILL.md in the console, or send it in the request that creates or updates the record. The record has no package. Use this way for a skill that consists only of instructions. For more information, see [Create and manage records](registry-create-manage-records.md).

Upload a package (**Upload a package**)  
You build the ZIP file yourself, for example in a CI/CD pipeline, and send it with the record. The registry validates the package and stores it. For more information, see [Upload a skill package](registry-skill-package-upload.md).

Synchronize from a source (**Synchronize from source**)  
You point the record at a skill in Amazon S3 or GitHub, and the registry reads the skill from there. You choose whether the registry reads only SKILL.md or the full package. Use this way when your build already publishes the skill to Amazon S3, or when the skill’s source of truth is a GitHub repository. For more information, see [Synchronize a skill from Amazon S3](registry-skill-sync-s3.md) and [Synchronize a skill from GitHub](registry-skill-sync-github.md).

**Synchronization isn’t automatic**  
The registry reads the source only when you create the record, when you change the source, or when you request a synchronization. It doesn’t detect changes in the source. After you change the skill in Amazon S3 or GitHub, request a synchronization. Until you do, the record keeps its earlier content.  
To request a synchronization in the console, choose **Manage**, choose **Synchronization**, and then choose **Sync**. In the API, call `UpdateRegistryRecord` with `triggerSynchronization` set to `true`.

For any skill record, the following rules apply:
+ A record gets its content in one way at a time. When you switch to a different way, the new content replaces the old. For more information, see [Change how a record gets its content](registry-skill-package-upload.md#registry-skill-package-upload-switch).
+ When you upload a package or synchronize from a source, the registry takes the record’s SKILL.md from the package or the source. Search and discovery then show that SKILL.md. In the same `CreateRegistryRecord` or `UpdateRegistryRecord` request, don’t also send your own SKILL.md text, and don’t both upload a package and synchronize from a source. A request that does either fails with a `ValidationException`.

For every member of the `agentSkillsDefinition` descriptor, see [AgentSkills descriptors](registry-supported-record-types.md#registry-agentskills-descriptors). To troubleshoot errors, see [Skill package and skill synchronization errors](registry-troubleshooting.md#registry-troubleshooting-skills).

## Synchronize SKILL.md only or the full package
<a name="registry-skill-packages-sync-modes"></a>

When you synchronize from Amazon S3 or GitHub, you choose whether the registry reads only SKILL.md or the whole skill. In the console, for **Content type**, choose **Skill markdown** or **Skill package**. In the API, set the source in `skillMd.source` or in `skillPackage.source`. Both members are in `descriptors.agentSkillsDefinition.additionalData`.

**Note**  
The console has two names for a skill’s SKILL.md content. It calls it **Skill markdown** where you choose what a synchronized source points to, and on the record detail page. It calls it **Skill documentation** in the **Content to include** list, where you author the content inline. Both refer to the same SKILL.md file.

SKILL.md only (`skillMd.source`)  
The registry reads only the SKILL.md file. The record gets its text and has no package. Use this mode when consumers need only the instructions.

Full package (`skillPackage.source`)  
The registry reads the whole skill: a ZIP object in Amazon S3, or every file in a GitHub folder. It validates and stores the package in the same way as an uploaded package. Consumers can download the package.

Set only one of the two members. A request that sets both, or that sets one while the record already has the other, fails with a `ValidationException`. To switch from one mode to the other, remove the other member in the same request. For the request syntax, see [Synchronize again or change the source](registry-skill-sync-s3.md#registry-skill-sync-s3-resync).

The following JSON examples show the `descriptors` value of a `CreateRegistryRecord` request. In an `UpdateRegistryRecord` request, you wrap each level of the descriptors in `optionalValue`. In the examples, replace the bucket, the object key, the GitHub URL, and the ARNs with your own values.

 **Example – Read only SKILL.md from Amazon S3** 

```json
{
  "agentSkillsDefinition": {
    "additionalData": {
      "skillMd": {
        "source": {
          "fromUrl": {
            "url": "s3://amzn-s3-demo-bucket/skills/my-skill/SKILL.md",
            "credentialProviderConfigurations": [
              {
                "credentialProviderType": "IAM",
                "credentialProvider": {
                  "iamCredentialProvider": {
                    "roleArn": "arn:aws:iam::111122223333:role/RegistrySkillSourceRead"
                  }
                }
              }
            ]
          }
        }
      }
    }
  }
}
```

 **Example – Read the full package from Amazon S3** 

```json
{
  "agentSkillsDefinition": {
    "additionalData": {
      "skillPackage": {
        "source": {
          "fromUrl": {
            "url": "s3://amzn-s3-demo-bucket/skills/my-skill.zip",
            "credentialProviderConfigurations": [
              {
                "credentialProviderType": "IAM",
                "credentialProvider": {
                  "iamCredentialProvider": {
                    "roleArn": "arn:aws:iam::111122223333:role/RegistrySkillSourceRead"
                  }
                }
              }
            ]
          }
        }
      }
    }
  }
}
```

For a GitHub source, also set `repositoryProvider` to `GITHUB`, and use an OAuth credential provider.

 **Example – Read the full package from a GitHub folder** 

```json
{
  "agentSkillsDefinition": {
    "additionalData": {
      "repositoryProvider": "GITHUB",
      "skillPackage": {
        "source": {
          "fromUrl": {
            "url": "https://github.com/octo-org/skills/tree/main/skills/my-skill",
            "credentialProviderConfigurations": [
              {
                "credentialProviderType": "OAUTH",
                "credentialProvider": {
                  "oauthCredentialProvider": {
                    "providerArn": "arn:aws:bedrock-agentcore:us-east-1:111122223333:token-vault/default/oauth2credentialprovider/my-github-provider",
                    "grantType": "AUTHORIZATION_CODE",
                    "scopes": ["repo"]
                  }
                }
              }
            ]
          }
        }
      }
    }
  }
}
```

A GitHub user might need to approve access before the registry can read the folder. To learn when you need an approval, see [Authorize GitHub access](registry-skill-sync-github.md#registry-skill-sync-github-authorization).

A synchronization replaces the record’s SKILL.md and package, and sets the record’s name and description to the `name` and `description` in the SKILL.md frontmatter. It does this on every synchronization, so a name or description that you set with `UpdateRegistryRecord` lasts only until the next one. A synchronization doesn’t change the record’s display name or record version. It fails if another record in the registry already has that name at the same record version, or if the name starts with `aws-autodetected-`. For the status reasons, see [Record name errors](registry-troubleshooting.md#registry-troubleshooting-skills-name).

**Note**  
The registry synchronizes `skillMd.source` only from an `s3://` URL, or from a GitHub URL when `repositoryProvider` is set to `GITHUB`. A request that sets a new `https://` URL without `repositoryProvider` fails with a `ValidationException`. A record that you created before skill synchronization was available might already store such a URL. The registry keeps it when you update the record’s other fields, but never reads content from it. To synchronize the record, replace the URL.

## What the registry stores and returns
<a name="registry-skill-packages-stored"></a>

When a record gets a package, by upload or by full-package synchronization, AWS Agent Registry does the following:
+ Validates the package. For the validation rules, see [Skill package format and validation](registry-skill-package-format.md). For the statuses that the record goes through, see [Status and approval](#registry-skill-packages-approval).
+ Copies the package’s SKILL.md into the record (`skillMd.data`), so that search and discovery show it in the same way as a SKILL.md that you write. If the record has a skill definition (`agentSkillsDefinition.data`), the registry doesn’t change it.
+ Encrypts the package at rest and stores it. If the registry has a customer managed key, the registry uses that key. For more information, see [Data encryption](registry-data-encryption.md).

**Validation isn’t a malware scan**  
 AWS Agent Registry checks that a skill package is a well-formed ZIP archive and that its SKILL.md follows the format rules. It doesn’t scan packages for malware or check what the scripts in a package do. Before an agent installs or runs a skill from the registry, validate it in the same way as any other content from an external source. For more information, see [Validate record metadata before you act on it](registry-data-protection.md#registry-consumer-validation).

### Which package each operation returns
<a name="registry-skill-packages-which-package"></a>

The registry doesn’t return the package itself. The following operations return an `artifact` member. It contains a `downloadUrl` for the package, which is valid for up to 5 minutes, and the package’s `sha256` checksum.


| Operation | Returns a download URL for | 
| --- | --- | 
|  `GetRegistryRecord` (control plane) | The package of the record’s latest revision. | 
|  `BatchGetDiscoverableRegistryRecord` (data plane) and the `batch_get_discoverable_registry_record` tool of the registry’s Model Context Protocol (MCP) endpoint | The package of the record’s latest approved revision. | 

 `SearchDiscoverableRegistryRecords`, `ListDiscoverableRegistryRecords`, `ListRegistryRecords`, and the responses of `CreateRegistryRecord` and `UpdateRegistryRecord` never return a download URL. For more information, see [Download a skill package](registry-skill-package-download.md).

For a synchronized record, `GetRegistryRecord` also returns `synchronizedSource`. It shows the source that the record’s current content came from, when the registry read it, and which version of the source it read.

### Packages during an update
<a name="registry-skill-packages-update-in-progress"></a>

During an update, and after an update fails, what `GetRegistryRecord` returns depends on where the new package comes from:
+  **Upload replaces upload, or synchronization replaces synchronization** — `GetRegistryRecord` keeps returning a download URL for the last package that passed validation.
+  **Upload replaces synchronization, or synchronization replaces upload** — `GetRegistryRecord` returns no download URL until an update succeeds, including after this update fails.

In both cases, if the record has an approved revision, `BatchGetDiscoverableRegistryRecord` and the MCP endpoint keep returning a download URL for that revision’s package. An update includes the time that the record waits for GitHub authorization.

### Package retention
<a name="registry-skill-packages-retention"></a>

The registry keeps a record’s earlier packages until you delete the record, so that it can return the packages described in this section. It doesn’t list or return earlier packages in any other way. When you delete the record, the registry deletes all of its packages.

## Status and approval
<a name="registry-skill-packages-approval"></a>

When you upload a package or synchronize from a source, the registry reads and validates the content after the request returns. The record moves through the following statuses:
+  **When you create a record** — `CREATING`, and then `DRAFT` if the content is valid, or `CREATE_FAILED` if it isn’t. For a GitHub source that needs a user’s authorization, the record is in `CREATE_PENDING_AUTH` first, until the user authorizes access.
+  **When you update a record** — `UPDATING`, and then `DRAFT` or `UPDATE_FAILED`. For a GitHub source that needs a user’s authorization, the record is in `UPDATE_PENDING_AUTH` first.


| Status | Meaning | 
| --- | --- | 
|  `CREATE_PENDING_AUTH`, `UPDATE_PENDING_AUTH`  | GitHub sources only. The record is waiting for a GitHub user to authorize access. For more information, see [Authorize GitHub access](registry-skill-sync-github.md#registry-skill-sync-github-authorization). | 
|  `CREATING`, `UPDATING`  | The registry is reading the source or validating the package. | 
|  `DRAFT`  | The content is valid and stored. You can submit the record for approval. | 
|  `CREATE_FAILED`, `UPDATE_FAILED`  | The package or the source failed. `statusReason` explains why. Fix the problem and update the record. | 

If a synchronization reads the same SKILL.md and package as before, and the request changes nothing else, the record returns to its previous status instead of `DRAFT`. For example, an `APPROVED` record stays `APPROVED`.

While a record is in `CREATING` or `UPDATING` status, you can’t update or delete it. A request to do so fails with a `ConflictException`.

### Change the content of an approved record
<a name="registry-skill-packages-approved-changes"></a>

Changes to the skill content of an approved record follow the record lifecycle:
+ When you upload a new package to an `APPROVED` record, or remove its uploaded package, the update creates a new `DRAFT` revision. This happens even if the new package is identical to the current one. A synchronization that changes the record’s SKILL.md or package also creates a new `DRAFT` revision. Submit the revision for approval to publish it.
+ Until the new revision is approved, `BatchGetDiscoverableRegistryRecord` and the MCP endpoint keep returning a download URL for the approved revision’s package. For more information, see [Which package each operation returns](#registry-skill-packages-which-package).

For more information about revisions and approval, see [Record lifecycle](registry-record-lifecycle.md).

## Availability
<a name="registry-skill-packages-availability"></a>

Skill packages and skill synchronization from Amazon S3 and GitHub are available in all commercial AWS Regions where AWS Agent Registry is available. They aren’t available in the AWS GovCloud (US) Regions. For the Regions where AWS Agent Registry is available, see [Supported AWS Regions](agentcore-regions.md).

Skill packages and skill synchronization are available only in the `agent-registry` namespace (`aws agent-registry-control` and `aws agent-registry` in the AWS CLI).

For package sizes and other limits, see [Skill package limits](bedrock-agentcore-limits.md#registry-skill-package-limits).

**Topics**