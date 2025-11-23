# Configuring the Amazon ECR re-scan duration

The Amazon ECR re-scan duration setting determines how long Amazon Inspector continuously monitors container images in repositories.
You configure the re-scan duration for the image last-in-use date, last pull date, and push date.
As a best practice, configure the re-scan duration to best suit your environment.

If you build images often, choose a shorter scan duration.
For images used over long periods of time, choose a longer scan duration.
The default scan duration for new accounts, including new accounts added to an organization, is 14 days.

Amazon Inspector will continue to monitor and rescan an image as long as it was last in use on a cluster or pushed within 14 days (by default).
If an image hasn’t been pushed or last used on a running container within the configured push and last in use dates, Amazon Inspector stops monitoring it.
There is an option to change the setting to monitor images by last pull date instead of the last in use date, if required.
When Amazon Inspector stops monitoring an image, it sets the image scan status code to inactive and reason code to expired.
Amazon Inspector then schedules all associated image findings to be closed.

If you increase the push date duration, Amazon Inspector applies the change to all actively scanned images in repositories configured for continual scanning.
However, inactive images remain inactive, even if you push them within the new duration.

When you configure the re-scan duration from a delegated administrator account, Amazon Inspector applies the setting to all member accounts in the organization.
If the delegated administrator account does not enable Amazon ECR scanning, it cannot view clusters for an API image.

For multi-architecture images, the last-in-use date tracking is not supported.
When using multi-architecture images, we recommend that you configure scanning based on image pull or push events instead of the last-in-use date to ensure proper re-scanning behavior.

###### Note

All re-scan duration settings configured prior to May 16, 2025, will remain unchanged.
You can continue using any default settings previously configured.

###### Image re-scan duration

The image re-scan duration determines how long Amazon Inspector will monitor images.
The image re-scan duration includes two modes: **Last in use date** (default) or **Last pull date**.
Choose **Last in use date** (default) if you want to use the last in use date from your Amazon ECS/Amazon EKS cluster activity.
Choose **Last pull date** if you want to use the last pull date from your Amazon ECR images to re-scan images.
The following options are available as re-scan durations:

- 14 days (default)
- 30 days
- 60 days
- 90 days
- 180 days

###### Image push date duration

The image push date duration determines how long Amazon Inspector will continuously monitor images after being pushed to repositories.
The following options are available as re-scan durations:

- 14 days (default)
- 30 days
- 60 days
- 90 days
- 180 days
- Lifetime

###### To configure the Amazon ECR re-scan duration

1. Sign in using your credentials, and then open the Amazon Inspector console at [https://console.aws.amazon.com/inspector/v2/home](https://console.aws.amazon.com/inspector/v2/home "https://console.aws.amazon.com/inspector/v2/home").
2. Select the AWS Region where you want to configure the Amazon ECR re-scan duration.
3. From the navigation pane, choose **General settings**, and then choose **ECR scanning settings**.
4. Under **ECR re-scan duration**, choose the image re-scan mode, and then choose the corresponding duration.
5. Under **Image push date**, choose the image push date.
6. Choose **Save**.

## Understanding ECR container image states

Inspector only scans `ACTIVE` images in ECR container images.
ECR container images in an `ARCHIVED` status are not scanned.
To learn more about scanning behaviors, see [Scan behaviors for Amazon ECR scanning](scanning-ecr.md#ecr-scan-behavior "scanning-ecr.md#ecr-scan-behavior").

When an ECR container image's image status in ECR transitions to `ACTIVE`, Inspector uses the `lastActivatedAt` field to monitor rescan duration.
