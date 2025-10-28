# AOSOPS02-BP02 Automate the process of taking snapshots

Schedule automatic snapshots to maintain consistent backups and data
recoverability.

**Level of risk exposed if this best practice
is not established**: Medium

**Desired outcome:** Snapshots are
automatically created.

**Benefits of establishing this best
practice**: To streamline snapshot management, use these
features to schedule automatic snapshots at regular intervals, which
allows for consistent data backups and recoverability in case of
issues. By automating this process, you can reduce the risk of human
error and minimize the impact of any unexpected events on your
OpenSearch Service domains.

## Implementation guidance

Amazon OpenSearch Service automatically creates hourly snapshots
of your indices within the same domain. However, these automatic
snapshots are not restorable across different domains.

If you rely solely on the automatic hourly snapshot, there's no
need to follow this recommendation. However, if you prefer to take
control of your snapshot schedule and have the flexibility to
restore them in other OpenSearch Service domains, then continue following
this best practice.

### Implementation steps

Create a Snapshot Management (SM) policy:

- Create a custom snapshot repository. For step-by-step
  instructions, see [AOSOPS02-BP01](aosops02-bp01.md "aosops02-bp01.md").
- Navigate to your OpenSearch Service domain dashboard.
- In your OpenSearch Service dashboard, select **Snapshot Management**
  from the left-hand menu.
- Create a new **Snapshot Policy** by choosing **Create policy**.
- Configure policy details:
  - **Name**: Give your
    policy a unique name, for example
    `daily-snapshot-policy`.
  - Under Source and Destination boxes, select the indices
    that you want to snapshot, and choose the snapshot
    repository you registered (for example,
    `your-repository-name`).

- In the Snapshot schedule box:
  - **Snapshot frequency:**
    Enter how often you want snapshots taken. For example,
    choose daily if you want to back up every day.
  - **Start time and Time
    zone:** Enter the time of day and the time zone
    to take the snapshots.

- (Optional) Define a retention policy to automatically delete
  older snapshots after a specific time period (for example,
  keep the last seven days).
- Review the settings, then choose
  **Create policy** to save.

Once the policy is active, OpenSearch Service will automatically
take snapshots based on your specified schedule, and they'll be
saved in the designated Amazon S3 bucket.

## Resources

- [Automating
  snapshots with Snapshot Management](../../../opensearch-service/latest/developerguide/managedomains-snapshots.md#managedomains-snapshot-mgmt "../../../opensearch-service/latest/developerguide/managedomains-snapshots.md#managedomains-snapshot-mgmt")
- [Unleash
  the power of Snapshot Management to take automated snapshots
  using Amazon OpenSearch Service](https://aws.amazon.com/blogs/big-data/unleash-the-power-of-snapshot-management-to-take-automated-snapshots-using-amazon-opensearch-service/ "https://aws.amazon.com/blogs/big-data/unleash-the-power-of-snapshot-management-to-take-automated-snapshots-using-amazon-opensearch-service/")
- [Take
  manual snapshots and restore in a different domain spanning
  across various regions and accounts in Amazon OpenSearch Service](https://aws.amazon.com/blogs/big-data/take-manual-snapshots-and-restore-in-a-different-domain-spanning-across-various-regions-and-accounts-in-amazon-opensearch-service/ "https://aws.amazon.com/blogs/big-data/take-manual-snapshots-and-restore-in-a-different-domain-spanning-across-various-regions-and-accounts-in-amazon-opensearch-service/")
