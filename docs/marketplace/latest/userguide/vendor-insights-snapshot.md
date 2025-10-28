# Managing snapshots in AWS Marketplace Vendor Insights

A _snapshot_ is a point-in-time posture of a security
profile. In AWS Marketplace Vendor Insights, you can use snapshots to assess a seller's product at any given time. As
the seller, you can compare the security postures of your profile at different times or the
latest snapshots of different security profiles to support your decision making. Snapshots
provide necessary security information in addition to providing transparency about freshness and
source of the data.

In the AWS Marketplace console, in the AWS Marketplace Vendor Insights **Snapshot summary** section, you can
view the following snapshot details for the creation and release schedule:

- **Last created snapshot** – Snapshot last created for this
  profile.
- **Next scheduled creation** – Snapshot scheduled to be created
  next.
- **Creation frequency** – Length of time between snapshot
  creations or the frequency of creating snapshots.
- **Next scheduled release** – Snapshot scheduled to be released
  next.
- **Staging time** – Snapshot is staged for at least this length
  of time and then eligible to be released during a snapshot release event.
- **Release frequency** – Length of time between release
  events.
  In the **Snapshot list** section, the snapshot statuses are as
  follows:

- **Released** – Snapshot is public and available to view for
  users with permission to this product.
- **Pending release** – Snapshot completed or is in the mandatory
  minimum staging period and scheduled for the next release.
- **Private** – Snapshot created before security profile
  activation or had validation errors and isn't visible to the public. Private snapshots
  remain only in seller visibility.

###### Topics

- [Create a snapshot](#create-snapshot "#create-snapshot")
- [View a snapshot](#view-snapshot "#view-snapshot")
- [Export a snapshot](#export-snapshot "#export-snapshot")
- [View latest released snapshot](#latest-released-snapshot "#latest-released-snapshot")
- [Postpone a snapshot release](#postpone-snapshot "#postpone-snapshot")
- [Change preferences for the snapshot list](#update-preferences-snapshot "#update-preferences-snapshot")

## Create a snapshot

To create a snapshot for your profile, follow these steps. You can create a maximum of 20
snapshots per day.

1. Sign in to the AWS Management Console and open the [AWS Marketplace
   console](https://console.aws.amazon.com/marketplace/ "https://console.aws.amazon.com/marketplace/").
2. Choose **Vendor Insights**.
3. From **Vendor Insights**, choose a product.
4. On the product profile page, go to the **Snapshot list**, and choose
   **Create new snapshot**.
5. A message notifies you that the snapshot schedule will change. Choose
   **Create**.

###### Note

The snapshot schedule changes when a new snapshot is created. New snapshots are
scheduled for the same time as your manually created snapshot. This message includes the
new schedule.

The new snapshot is created within 30 minutes and added to the snapshot list. New
snapshots are created with a **Pending release** status. No one can view new
snapshots until the status changes to **Released**.

## View a snapshot

To view a snapshot for your profile, follow these steps.

1. Sign in to the AWS Management Console and open the [AWS Marketplace
   console](https://console.aws.amazon.com/marketplace/ "https://console.aws.amazon.com/marketplace/").
2. Choose **Vendor Insights**.
3. From **Vendor Insights**, choose a product.
4. On the product profile page, go to the **Snapshot list**, and choose
   the **Snapshot ID** of the snapshot that you want to view.
5. When you're finished, choose **Back** to exit the snapshot
   view.

## Export a snapshot

You can export to JSON or CSV formats. To export a snapshot, follow these steps.

1. Sign in to the AWS Management Console and open the [AWS Marketplace
   console](https://console.aws.amazon.com/marketplace/ "https://console.aws.amazon.com/marketplace/").
2. Choose **Vendor Insights**.
3. From **Vendor Insights**, choose a product.
4. On the product profile page, go to the **Snapshot list**, and choose
   the **Snapshot ID** of the snapshot that you want to export.
5. Choose **Export**.
6. From the dropdown list, choose **Download (JSON)** or
   **Download (CSV)**.

## View latest released snapshot

The latest released snapshot is what users use to view and assess your product's health.
It's important to know what is in your latest released snapshot to ensure that you're
portraying your product with accurate information. To view the latest snapshot for your
profile, follow these steps.

1. Sign in to the AWS Management Console and open the [AWS Marketplace
   console](https://console.aws.amazon.com/marketplace/ "https://console.aws.amazon.com/marketplace/").
2. Choose **Vendor Insights**.
3. From **Vendor Insights**, choose a product.
4. On the product profile page, go to the **Snapshot list**, and choose
   the **Snapshot ID** of the snapshot that you want to view.
5. Choose **View latest released snapshot**.
6. When you're finished, choose **Back** to exit the snapshot
   view.

## Postpone a snapshot release

To delay the release of a snapshot to your profile, you can postpone a snapshot release
for a specific **Snapshot ID**.

1. Sign in to the AWS Management Console and open the [AWS Marketplace
   console](https://console.aws.amazon.com/marketplace/ "https://console.aws.amazon.com/marketplace/").
2. Choose **Vendor Insights**.
3. From **Vendor Insights**, choose a product.
4. On the product profile page, go to the **Snapshot list**, and choose
   the **Snapshot ID** of the snapshot for which you want to postpone the
   release.
5. From the **Snapshot summary**, choose **Postpone snapshot
   release**.
6. A message notifes you that the snapshot schedule will change. Choose
   **Postpone**.

A success message appears, indicating that you have successfully postponed the snapshot
release for this product.

## Change preferences for the snapshot list

After creating a snapshot, you can change the preferences of how a snapshot is viewed in
the **Snapshot list**.

1. Sign in to the AWS Management Console and open the [AWS Marketplace
   console](https://console.aws.amazon.com/marketplace/ "https://console.aws.amazon.com/marketplace/").
2. Choose **Vendor Insights**.
3. From **Vendor Insights**, choose a product.
4. On the product profile page, go to the **Snapshot list**, and choose
   the **Snapshot ID** of the snapshot that you want to change.
5. Choose the preferences icon. You can customize the following preferences for your
   snapshot:
   - **Page size** – Select how many snapshots you want listed
     on each page: **10 resources**, **20 resources**, or
     **50 resources** per page.
   - **Wrap lines** – Select an option to wrap lines to view
     the entire record.
   - **Time format** – Select whether you want
     **Absolute**, **Relative**, or
     **ISO**.
   - **Visible columns** – Select options that you want visible
     for the snapshot details: **Snapshot ID**,
     **Status**, and **Date created** .
