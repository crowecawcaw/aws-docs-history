

AWS Migration Hub is no longer open to new customers as of November 7, 2025. For capabilities similar to AWS Migration Hub, explore [AWS Transform](https://aws.amazon.com/transform).

# Changing your AWS Migration Hub home Region
<a name="change-home-region"></a>

**To use the AWS Management Console to change your home Region**

1. Sign in to the AWS Management Console and open the Migration Hub console at [https://console.aws.amazon.com/migrationhub/](https://console.aws.amazon.com/migrationhub/). 

1. In the left navigation pane, scroll to the bottom, and choose **Settings**.

1. Choose **Remove**.

1. Enter **confirm**, and then choose **Confirm**.

1. Choose **Choose a home Region**, and then choose your new home Region from the list.

1. Choose **Confirm home Region**.

**To use the API or the AWS CLI to change your home Region**

1. Use either the [DescribeHomeRegionControls](https://docs.aws.amazon.com/migrationhub-home-region/latest/APIReference/API_DescribeHomeRegionControls.html) API or the [describe-home-region-controls](https://docs.aws.amazon.com/cli/latest/reference/migrationhub-config/describe-home-region-controls.html) AWS CLI command to get the control ID of the current Region.

1. Invoke either the [DeleteHomeRegionControl](https://docs.aws.amazon.com/migrationhub-home-region/latest/APIReference/API_DeleteHomeRegionControl.html) API or the [delete-home-region-control](https://docs.aws.amazon.com/cli/latest/reference/migrationhub-config/delete-home-region-control.html) AWS CLI command with the control ID that you obtained in the previous step.

1. Use the [CreateHomeRegionControl](https://docs.aws.amazon.com/migrationhub-home-region/latest/APIReference/API_CreateHomeRegionControl.html) API or the [create-home-region-control](https://docs.aws.amazon.com/cli/latest/reference/migrationhub-config/create-home-region-control.html) AWS CLI command to set the new home Region.

Your home Region can only be changed to another AWS Region that is supported by AWS Migration Hub. For a list of the supported Regions, see [AWS Migration Hub Service endpoints](https://docs.aws.amazon.com/general/latest/gr/migrationhubn.html) in the *AWS General Reference*.

If you change the Migration Hub home Region, you'll need to recollect the data in the new home Region. Data collected in the old home Region doesn't migrate to the new home Region. 