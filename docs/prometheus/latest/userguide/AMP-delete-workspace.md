# Delete an Amazon Managed Service for Prometheus workspace

Deleting a workspace deletes the data that has been ingested into it.

###### Note

Deleting an Amazon Managed Service for Prometheus workspace does not automatically delete any AWS managed
collectors that are scraping metrics and sending them to the workspace. For more
information, see [Find and delete scrapers](AMP-collector-how-to.md#AMP-collector-list-delete "AMP-collector-how-to.md#AMP-collector-list-delete").

**To delete a workspace using the AWS CLI**

Use the following command:

```
aws amp delete-workspace --workspace-id `my-workspace-id`
```

###### To delete a workspace using the Amazon Managed Service for Prometheus console

1. Open the Amazon Managed Service for Prometheus console at [https://console.aws.amazon.com/prometheus/](https://console.aws.amazon.com/prometheus/home "https://console.aws.amazon.com/prometheus/home").
2. In the upper left corner of the page, choose the menu icon and then choose
   **All workspaces**.
3. Choose the workspace ID of the workspace that you want to delete, and then
   choose **Delete**.
4. Enter `delete` in the confirmation box, and choose
   **Delete**.
