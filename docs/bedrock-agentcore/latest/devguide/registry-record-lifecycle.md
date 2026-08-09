# Record lifecycle

###### Migration Now Open

AWS Agent Registry has launched under the new `agent-registry` namespace. Support for the public preview `bedrock-agentcore` namespace will be discontinued on September 17, 2026. For migration instructions, see [Comprehensive registry migration guide](registry-faq.md "registry-faq.md").

## Status transitions

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

- **Create** → DRAFT. Edit freely before submitting.
- **Submit** → PENDING\_APPROVAL. Auto-approval skips to APPROVED. Amazon EventBridge notification sent.
- **Approve/Reject** → Curator uses UpdateRegistryRecordStatus. Can directly approve a REJECTED record.
- **Deprecate** → Terminal from any status. Cannot be undone.

## How edits affect status

| Current status    | Effect of edit                                                                                                       |
| ----------------- | -------------------------------------------------------------------------------------------------------------------- |
| DRAFT             | Updated in place. Stays DRAFT.                                                                                       |
| PENDING\_APPROVAL | New DRAFT revision. Pending revision discarded. Not visible via the discovery APIs or MCP endpoint (never approved). |
| APPROVED          | New DRAFT revision. Approved revision stays discoverable until the new revision is approved.                         |
| REJECTED          | New DRAFT revision. Must go through normal submit-and-approve flow again.                                            |
| DEPRECATED        | Deprecated Records cannot be edited; Deprecated is a Terminal state                                                  |

###### Note

To temporarily hide an approved record from discovery without deprecating it, reject the record. Rejected records are not returned by the discovery APIs or the MCP endpoint. When you want to make the record discoverable again, edit and re-approve it to create a new approved revision.

## Dual-revision behavior

Editing an APPROVED record creates a new DRAFT revision while the approved revision remains active:

- **Discovery APIs (`SearchDiscoverableRegistryRecords`, `ListDiscoverableRegistryRecords`, `BatchGetDiscoverableRegistryRecord`) and the MCP endpoint (`InvokeRegistryMcp`)** — Return the approved revision.
- **Management APIs (`GetRegistryRecord`, `ListRegistryRecords`)** — Return the latest revision (which may be DRAFT).

Once a curator reviews and approves the edited revision, the discovery APIs and MCP endpoint start showing the new (approved) revision.

## Visibility rules

| API                                | Returns                      |
| ---------------------------------- | ---------------------------- |
| SearchDiscoverableRegistryRecords  | Only approved revisions      |
| ListDiscoverableRegistryRecords    | Only approved revisions      |
| GetDiscoverableRegistryRecord      | Only approved revisions      |
| BatchGetDiscoverableRegistryRecord | Only approved revisions      |
| InvokeRegistryMcp                  | Only approved revisions      |
| GetRegistryRecord                  | Latest revision (any status) |
| ListRegistryRecords                | Latest revision (any status) |

###### Note

`SearchDiscoverableRegistryRecords` was named `SearchRegistryRecords` in the `bedrock-agentcore` namespace. The `ListDiscoverableRegistryRecords` and `BatchGetDiscoverableRegistryRecord` APIs are only available in the `agent-registry` namespace.
