# Troubleshooting the cost and usage dashboard

###### Topics

- [Why did my cost and usage dashboard export fail
  right after I created it?](#dataexports-failed-export "#dataexports-failed-export")
- [Why can't I access the dashboard?](#dataexports-dashboard-access "#dataexports-dashboard-access")
- [Why am I being taken to the console admin
  page to unsubscribe the QuickSight account when I try to view the dashboard?](#dataexports-quicksight-unsubscribe "#dataexports-quicksight-unsubscribe")
- [Why don't I see any data in the cost and usage
  dashboard that I just created?](#dataexports-current-month-data "#dataexports-current-month-data")
- [Why can't I see historical data in the cost and
  usage dashboard?](#dataexports-historical-data "#dataexports-historical-data")
- [Why did my QuickSight dashboard link disappear
  from the Data Exports console page?](#dataexports-qs-dashboard-link "#dataexports-qs-dashboard-link")
- [How can I configure Amazon QuickSight to visualize
  resource tags in CUR 2.0?](#dataexports-qs-configure "#dataexports-qs-configure")

## Why did my cost and usage dashboard export fail

right after I created it?

Your cost and usage dashboard export may have failed due to a delay in IAM role
propagation. If you created a new service role for this export, Amazon QuickSight may not have
had permission to access your S3 bucket and create your dashboard. When you see the error
“Insufficient permission to access the manifest file” in the Export status, choose Export, and
then choose Retry in the table action menu.

If you didn’t create a new service role for your cost and usage dashboard export, you may
have specified an incorrect service role for QuickSight to use. In this case, you should delete
your export and recreate it, while also creating a new service role in the cost and usage
dashboard console workflow.

## Why can't I access the dashboard?

You may not be able to access the cost and usage dashboard in Amazon QuickSight if you
don’t have permission to view it. To troubleshoot, open your export by choosing the export name.
Check the QuickSight created by field to see who created the dashboard. Ask the user to give you
permission to view the dashboard.

## Why am I being taken to the console admin

page to unsubscribe the QuickSight account when I try to view the dashboard?

You may encounter this error if you're using the “Active directory” authentication method.
Choose the cost and usage dashboard export name to view the details of your export. Choose
**QUICKSIGHT SIGN IN** to sign in to your QuickSight account. You'll be able
to see the dashboard if you have permission to view it.

## Why don't I see any data in the cost and usage

dashboard that I just created?

Your cost and usage dashboard could be missing the data for the current month because it
can take up to 24 hours for all your data to be populated in your dashboard. Check the status of
your cost and usage dashboard export. If the export status says “Healthy”, allow 24 hours for
your dashboard to update with the current month's data. If you don’t see the current month's
data in your dashboard after 24 hours, contact AWS Support. You can check the creation time of
your cost and usage dashboard in the Exports and Dashboards table on the Data Exports console
page.

## Why can't I see historical data in the cost and

usage dashboard?

Your cost and usage dashboard might be missing the six months of historical data for any of
the following reasons:

- **No historical data exists:** If you have an account
  without six months of historical spending due to being a new account or recently changing
  membership in AWS Organizations, no historical data can populate the dashboard.
- **Historical backfill is still in progress:** Historical
  data backfill by Data Exports can take up to 24 hours to complete. You can use the SDK/CLI to check if
  any backfill executions failed with the `ListExecutions` API for this export, or if
  they are still in progress. Wait a little longer or use `ListExecutions` to ensure
  the backfill is not in progress.
- **Historical backfill failed:** Historical data backfill may
  have failed to complete due to an internal error. You can come to this conclusion if it's been
  more than 24 hours and the backfill is not complete, or you can use the
  `ListExecutions` API in the SDK/CLI and look for any failed executions for this
  export. If you believe the backfill has failed, try remaking the cost and usage dashboard in
  the console. If it fails a second time, we recommend reaching out to AWS Support.

## Why did my QuickSight dashboard link disappear

from the Data Exports console page?

The Data Exports console page reads from a file in your S3 bucket in order to identify the
QuickSight dashboard that the export is linked to. If this file is altered or deleted, the
console doesn't know that a dashboard exists for this export. While your dashboard still exists
in QuickSight, you'll need to repair this file for the link to reappear.

## How can I configure Amazon QuickSight to visualize

resource tags in CUR 2.0?

The cost and usage dashboard feature does not support visualizing resource tags. However,
you can still receive your resource tag data in the CUR 2.0 export. If you want an AWS
supported QuickSight dashboard for visualizing your cost and usage with tags, refer to the
[CUDOS Dashboard from AWS Well-Architected Labs](https://catalog.workshops.aws/awscid/en-US/dashboards/foundational/cudos-cid-kpi/#cudos-dashboard "https://catalog.workshops.aws/awscid/en-US/dashboards/foundational/cudos-cid-kpi/#cudos-dashboard"). It currently only uses data from
legacy CUR, but will support CUR 2.0 in the future.
