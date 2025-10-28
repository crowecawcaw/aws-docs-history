# Forecast Commits

You can view the forecast commit data requests that are published to your partners.
These data requests are triggered from AWS Supply Chain supply planning. For more
information, see [Supply Planning](supply-planning.md "supply-planning.md").

1. In the left navigation pane on the AWS Supply Chain dashboard, choose
   **N-Tier Visibility**.

The **N-Tier Visibility** page appears. 2. Choose the **Forecast Commits** tab.

The **Forecast Commit** page appears. 3. Under **Forecast commit**, you can view the details of all the forecast data requests from the generated supply plan.

You can select any forecast commit to review the forecast commit details. 4. Select the **Status**, **Partner**, or
**Site** dropdown to filter the forecast commits based on
the collaboration status, partner, or site. 5. Choose **Review** for forecast commits with a _For review_ collaboration status.

The **Forecast commit** details page appears. 6. Under **Review the Forecast Commit update**, review the committed forecast
and deviation. You can decide to accept or reject the response, or you can
decline and close the forecast commit.

You can read the reason for the update under **Latest update details from the partner**. 7. If you want to accept the forecast commit update, choose **Accept
response**.

The **Accept update** window appears. Choose **Accept update**. 8. If you want to reject the forecast commit update, choose **Reject and
send**.

The **Reject Forecast update and send feedback** window appears. Enter the rejection details and choose **Reject and send**. 9. If you want to decline and close the forecast commit request, choose **Decline and
close**.

The **Decline and close Forecast Commit** window appears. Enter the details and choose **Decline and close**.

## Viewing forecast commits when EDI is enabled

###### Note

You will only see this configuration if you selected _Yes_ to use **EDI Connection Settings** when setting up N-Tier Visibility.

You can only export forecast commits data in EDI format.

1. In the left navigation pane on the AWS Supply Chain dashboard, choose
   **N-Tier Visibility**.

The **N-Tier Visibility** page appears. 2. Choose the **Forecast Commits** tab.

The **Confirm or Update Forecast Commits** page appears. 3. From the **Actions** drop-down, choose **Export EDI data**.

The .json file with the forecast commits information is downloaded to your local computer and also downloaded to the Amazon S3 folder created as part of the outbound connection setup for Supply Planning.
