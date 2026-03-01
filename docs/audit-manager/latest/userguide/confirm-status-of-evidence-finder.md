# Confirming the status of evidence finder

After you submit your request to enable evidence finder, it takes up to 10 minutes to
enable the feature and create an event data store. As soon as the event data store is
created, all new evidence is ingested into the event data store moving forward.

When evidence finder is enabled and the event data store is created, we backfill the
newly created event data store with up to two years’ worth of your past evidence. This
process happens automatically and takes up to seven days to complete.

Follow the steps on this page to check and understand the status of your request to
enable evidence finder.

## Prerequisites

Make sure that you followed the steps to enable evidence finder. For instructions,
see [Enabling evidence finder](evidence-finder-settings-enable.md "evidence-finder-settings-enable.md").

## Procedure

You can check the current status of evidence finder using the Audit Manager console, the
AWS CLI, or the Audit Manager API.

Audit Manager console

###### To see the current status of evidence finder on the Audit Manager console

1. Open the AWS Audit Manager console at [https://console.aws.amazon.com/auditmanager/home](https://console.aws.amazon.com/auditmanager/home "https://console.aws.amazon.com/auditmanager/home").
2. In the left navigation pane, choose
   **Settings**.
3. Under **Enable evidence finder –
   optional**, review the current status.

Each status is defined as follows:

| Status                                               | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| ---------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Evidence finder isn't<br>enabled**                 | You haven't successfully enabled evidence<br>finder yet.                                                                                                                                                                                                                                                                                                                                                                                                      |
| **You have requested to enable<br>evidence finder**  | Your request is pending the event data store<br>being created.                                                                                                                                                                                                                                                                                                                                                                                                |
| **Evidence finder is<br>enabled**                    | The event data store was created. You can<br>now use evidence finder.<br>Depending how much evidence you have, it<br>takes up to seven days to backfill the new event<br>data store with your past evidence data. A blue<br>information panel indicates that the data backfill<br>is in progress. Feel free to start exploring<br>evidence finder in the meantime. However, keep in<br>mind that not all data is available until the<br>backfill is complete. |
| **You have requested to disable<br>evidence finder** | Your request is pending the event data store<br>being deleted.                                                                                                                                                                                                                                                                                                                                                                                                |
| **Evidence finder has been<br>disabled**             | Evidence finder has been permanently<br>disabled and the event data store is deleted.                                                                                                                                                                                                                                                                                                                                                                         |

AWS CLI

###### To see the current status of evidence finder in the AWS CLI

Run the [get-settings](../../../cli/latest/reference/auditmanager/get-settings.md "../../../cli/latest/reference/auditmanager/get-settings.md") command with the `--attribute`
parameter set to `EVIDENCE_FINDER_ENABLEMENT`.

```
aws auditmanager get-settings --attribute EVIDENCE_FINDER_ENABLEMENT
```

This returns the following information:

###### enablementStatus

This attribute shows the current status of evidence finder.

- `ENABLE_IN_PROGRESS` – You requested to
  enable evidence finder. An event data store is currently being
  created to support evidence finder queries.
- `ENABLED` – An event data store was created
  and evidence finder is enabled. We recommend waiting seven days
  until the event data store is backfilled with your past evidence
  data. You can use evidence finder in the meantime, but not all
  data is available until the backfill is complete.
- `DISABLE_IN_PROGRESS` – You requested to
  disable evidence finder, and your request is pending the event
  data store being deleted.
- `DISABLED` – You permanently disabled
  evidence finder and the event data store is deleted. You can't
  re-enable evidence finder after this point.

###### backfillStatus

This attribute shows the current status of the evidence data
backfill.

- `NOT_STARTED` – The backfill hasn’t started
  yet.
- `IN_PROGRESS` – The backfill is in progress.
  This takes up to seven days to complete, depending on the amount
  of evidence data.
- `COMPLETED` – The backfill is complete. All
  of your past evidence is now queryable.

Audit Manager API

###### To see the current status of evidence finder using the API

Call the [GetSettings](../APIReference/API_GetSettings.md "../APIReference/API_GetSettings.md") operation with the `attribute`
parameter set to `EVIDENCE_FINDER_ENABLEMENT`. This
returns the following information:

###### enablementStatus

This attribute shows the current status of evidence finder.

- `ENABLE_IN_PROGRESS` - You requested to enable
  evidence finder. An event data store is currently being created
  to support evidence finder queries.
- `ENABLED` - An event data store was created and
  evidence finder is enabled. We recommend waiting seven days
  until the event data store is backfilled with your past evidence
  data. You can use evidence finder in the meantime, but not all
  data is available until the backfill is complete.
- `DISABLE_IN_PROGRESS` - You requested to disable
  evidence finder, and your request is pending the deletion of the
  event data store.
- `DISABLED` - You permanently disabled evidence
  finder and the event data store is deleted. You can't re-enable
  evidence finder after this point.

###### backfillStatus

This attribute shows the current status of the evidence data
backfill.

- `NOT_STARTED` means that the backfill hasn’t
  started yet.
- `IN_PROGRESS` means that the backfill is in
  progress. This takes up to seven days to complete, depending on
  the amount of evidence data.
- `COMPLETED` means that the backfill is complete.
  All of your past evidence is now queryable.

For more information, see [evidenceFinderEnablement](../APIReference/API_EvidenceFinderEnablement.md "../APIReference/API_EvidenceFinderEnablement.md") in the _Audit Manager API Reference_.

## Next steps

After evidence finder is successfully enabled, you can start using the feature. We
recommend waiting seven days until the event data store is backfilled with your past
evidence data. You can use evidence finder in the meantime, but not all data might
be available until the backfill is complete.

To get started with evidence finder, see [Searching for evidence in evidence finder](search-for-evidence-in-evidence-finder.md "search-for-evidence-in-evidence-finder.md").

## Additional resources

- [Troubleshooting evidence finder issues](evidence-finder-issues.md "evidence-finder-issues.md")
