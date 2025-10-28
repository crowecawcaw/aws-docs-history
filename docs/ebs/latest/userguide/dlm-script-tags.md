# Identify snapshots created with Data Lifecycle Manager pre and post scripts

Amazon Data Lifecycle Manager automatically assigns the following system tags to snapshots created with
pre and post scripts.

- Key: `aws:dlm:pre-script`; Value: `SUCCESS`|`FAILED`

A tag value of `SUCCESS` indicates that the pre script executed successfully.
A tag value of `FAILED` indicates that the pre script did not execute successfully.

- Key: `aws:dlm:post-script`; Value: `SUCCESS`|`FAILED`

A tag value of `SUCCESS` indicates that the post script executed successfully.
A tag value of `FAILED` indicates that the post script did not execute successfully.
For custom SSM documents and SAP HANA backups, you can infer successful
application-consistent snapshot creation if the snapshot is tagged with both
`aws:dlm:pre-script:SUCCESS` and
`aws:dlm:post-script:SUCCESS`.

Additionally, application-consistent snapshots created using VSS backup are automatically tagged with:

- Key: `AppConsistent tag`; Value: `true`|`false`

A tag value of `true` indicates that the VSS backup succeeded and that the snapshots
are application-consistent. A tag value of `false` indicates that the VSS backup did
not succeed and that the snapshots are not application-consistent.
