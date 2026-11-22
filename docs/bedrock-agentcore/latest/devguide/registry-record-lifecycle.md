

# Record lifecycle

**Migration Now Open**  
 AWS Agent Registry has launched under the new `agent-registry` namespace. Support for the public preview `bedrock-agentcore` namespace will be discontinued on October 30, 2026. For migration instructions, see [Comprehensive registry migration guide](registry-faq.md).

## Status transitions
<a name="registry-status-transitions"></a>

```
Create → DRAFT → Submit → PENDING_APPROVAL → Approve → APPROVED
                               │                          │
                               │ Reject                   │ Edit (new DRAFT
                               ▼                          │  revision; approved
                          REJECTED ── Approve (direct) ───┘  stays discoverable)
                               │
                               └── Edit → DRAFT

         Any status → DEPRECATED (terminal)
```

## Transition details
<a name="registry-transition-details"></a>
+  **Create** → DRAFT. Edit freely before submitting.
+  **Submit** → PENDING\_APPROVAL. Auto-approval skips to APPROVED. Amazon EventBridge notification sent.
+  **Approve/Reject** → Curator uses UpdateRegistryRecordStatus. Can directly approve a REJECTED record.
+  **Deprecate** → Terminal from any status. Cannot be undone.
+  **Wait for GitHub authorization** → A skill record that synchronizes from GitHub can wait in CREATE\_PENDING\_AUTH or UPDATE\_PENDING\_AUTH until a user approves access. See [Pending authorization statuses](#registry-pending-authorization).

## How edits affect status
<a name="registry-edits-affect-status"></a>


| Current status | Effect of edit | 
| --- | --- | 
| DRAFT | Updated in place. Stays DRAFT. | 
| PENDING\_APPROVAL | New DRAFT revision. Pending revision discarded. Not visible via the discovery APIs or MCP endpoint (never approved). | 
| APPROVED | New DRAFT revision. Approved revision stays discoverable until the new revision is approved. | 
| REJECTED | New DRAFT revision. Must go through normal submit-and-approve flow again. | 
| DEPRECATED | Deprecated Records cannot be edited; Deprecated is a Terminal state | 
| CREATE\_PENDING\_AUTH, UPDATE\_PENDING\_AUTH | Refused with a `ConflictException`, unless the update synchronizes a GitHub source: `triggerSynchronization`, or a new or changed GitHub source. See [Pending authorization statuses](#registry-pending-authorization). | 

**Note**  
To temporarily hide an approved record from discovery without deprecating it, reject the record. Rejected records are not returned by the discovery APIs or the MCP endpoint. When you want to make the record discoverable again, edit and re-approve it to create a new approved revision.

## Dual-revision behavior
<a name="registry-dual-revision"></a>

Editing an APPROVED record creates a new DRAFT revision while the approved revision remains active:
+  **Discovery APIs (`SearchDiscoverableRegistryRecords`, `ListDiscoverableRegistryRecords`, `BatchGetDiscoverableRegistryRecord`) and the MCP endpoint (`InvokeRegistryMcp`)** — Return the approved revision.
+  **Management APIs (`GetRegistryRecord`, `ListRegistryRecords`)** — Return the latest revision (which may be DRAFT).

Once a curator reviews and approves the edited revision, the discovery APIs and MCP endpoint start showing the new (approved) revision.

## Skill packages and synchronization
<a name="registry-skill-package-revisions"></a>

Skill packages and skill sources follow the same dual-revision behavior. For information about how to publish them, see [Publish skill packages](registry-skill-packages.md).
+  **Asynchronous processing** — When a request uploads a package or starts a synchronization, the record moves to CREATING or UPDATING while the registry reads and validates the content. It then moves to DRAFT, or to CREATE\_FAILED or UPDATE\_FAILED, with the reason in `statusReason`. A synchronization that reads the same SKILL.md and package, in a request that changes nothing else, returns the record to its previous status instead, so an APPROVED record stays APPROVED.
+  **New revision** — Uploading a package, replacing it, or removing an uploaded package is a content change, even when the new package has the same bytes. A synchronization that changes the package or SKILL.md is a content change too. A content change to an APPROVED record creates a new DRAFT revision, which you must submit for approval again.
+  **Package served during review** — Until the new revision is approved, `BatchGetDiscoverableRegistryRecord` and the MCP endpoint keep returning the approved revision and its package. `GetRegistryRecord` returns the latest revision and its package, including a DRAFT revision.
+  **Failed update** — If a package upload or a synchronization fails, `GetRegistryRecord` keeps returning the previous package, unless the update switched between an uploaded package and a synchronized package. Then it returns no package until an update succeeds.
+  **Synchronized source** — If a synchronization fails, `synchronizedSource` still describes the last synchronization that the registry accepted. An upload, new `skillMd.data`, or removing a synchronized package removes `synchronizedSource`.

## Pending authorization statuses
<a name="registry-pending-authorization"></a>

A skill record that synchronizes from GitHub reads the repository with the access that a GitHub user approves. When a create or update request needs that approval, the record enters one of these statuses:
+  `CREATE_PENDING_AUTH` — The new record waits for a user to approve GitHub access before its first synchronization. The record has no package yet.
+  `UPDATE_PENDING_AUTH` — An update waits for a user to approve GitHub access before it synchronizes. `GetRegistryRecord` keeps returning a download URL for the record’s previous package, unless the update replaces an uploaded package with a synchronized one. If the record was approved, the approved revision stays discoverable.

The `CreateRegistryRecord` or `UpdateRegistryRecord` response returns `authorizationData`, which contains the authorization URL for the user to open. A pending status ends in one of these ways:
+  **The user approves access and the authorization completes** — The record moves to CREATING or UPDATING, synchronizes, and then moves to DRAFT, or to CREATE\_FAILED or UPDATE\_FAILED.
+  **The authorization isn’t completed in time** — Each authorization URL expires 10 minutes after the approval starts. If the approval is still in progress then, the record fails. If another request restarts the same approval, waiting records follow the new URL, for at most 30 minutes in total. If the authorization expires, fails, or times out, the record moves to CREATE\_FAILED or UPDATE\_FAILED, and `statusReason` explains why.
+  **You deprecate or delete the record.** 

While a record is in a pending authorization status:
+ An update fails with a `ConflictException`, unless it synchronizes a GitHub source: it sets `triggerSynchronization` to `true` (optionally with `forceAuthentication`), or sets a new or changed GitHub source. Use `triggerSynchronization` to get a new authorization URL.
+ You can read, deprecate, or delete the record. You can’t submit it for approval, approve it, or reject it.

For more information about the authorization flow, see [Synchronize a skill from GitHub](registry-skill-sync-github.md).

## Visibility rules
<a name="registry-visibility-rules"></a>


| API | Returns | 
| --- | --- | 
| SearchDiscoverableRegistryRecords | Only approved revisions | 
| ListDiscoverableRegistryRecords | Only approved revisions | 
| GetDiscoverableRegistryRecord | Only approved revisions | 
| BatchGetDiscoverableRegistryRecord | Only approved revisions | 
| InvokeRegistryMcp | Only approved revisions | 
| GetRegistryRecord | Latest revision (any status) | 
| ListRegistryRecords | Latest revision (any status) | 

**Note**  
 `SearchDiscoverableRegistryRecords` was named `SearchRegistryRecords` in the `bedrock-agentcore` namespace. The `ListDiscoverableRegistryRecords` and `BatchGetDiscoverableRegistryRecord` APIs are only available in the `agent-registry` namespace.