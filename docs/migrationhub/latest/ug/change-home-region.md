AWS Migration Hub will no longer be open to new customers starting November 7, 2025. To continue using the service, sign up prior to November 7, 2025. For capabilities similar to AWS Migration Hub, explore [AWS Transform](https://aws.amazon.com/transform "https://aws.amazon.com/transform").

# Changing your AWS Migration Hub home Region

###### To use the AWS Management Console to change your home Region

1. Sign in to the AWS Management Console and open
   the Migration Hub console at
   [https://console.aws.amazon.com/migrationhub/](https://console.aws.amazon.com/migrationhub/ "https://console.aws.amazon.com/migrationhub/").
2. In the left navigation pane, scroll to the bottom, and choose
   **Settings**.
3. Choose **Remove**.
4. Enter `confirm`, and then choose
   **Confirm**.
5. Choose **Choose a home Region**, and then choose your new
   home Region from the list.
6. Choose **Confirm home Region**.

###### To use the API or the AWS CLI to change your home Region

1. Use either the [DescribeHomeRegionControls](../../../migrationhub-home-region/latest/APIReference/API_DescribeHomeRegionControls.md "../../../migrationhub-home-region/latest/APIReference/API_DescribeHomeRegionControls.md") API or the [describe-home-region-controls](../../../cli/latest/reference/migrationhub-config/describe-home-region-controls.md "../../../cli/latest/reference/migrationhub-config/describe-home-region-controls.md") AWS CLI command to get the control ID
   of the current Region.
2. Invoke either the [DeleteHomeRegionControl](../../../migrationhub-home-region/latest/APIReference/API_DeleteHomeRegionControl.md "../../../migrationhub-home-region/latest/APIReference/API_DeleteHomeRegionControl.md") API or the [delete-home-region-control](../../../cli/latest/reference/migrationhub-config/delete-home-region-control.md "../../../cli/latest/reference/migrationhub-config/delete-home-region-control.md") AWS CLI command with the control ID that
   you obtained in the previous step.
3. Use the [CreateHomeRegionControl](../../../migrationhub-home-region/latest/APIReference/API_CreateHomeRegionControl.md "../../../migrationhub-home-region/latest/APIReference/API_CreateHomeRegionControl.md") API or the [create-home-region-control](../../../cli/latest/reference/migrationhub-config/create-home-region-control.md "../../../cli/latest/reference/migrationhub-config/create-home-region-control.md") AWS CLI command to set the new home
   Region.
   Your home Region can only be changed to another AWS Region that is supported by
   AWS Migration Hub. For a list of the supported Regions, see [AWS Migration Hub Service endpoints](../../../general/latest/gr/migrationhubn.md "../../../general/latest/gr/migrationhubn.md") in
   the _AWS General Reference_.

If you change the Migration Hub home Region, you'll need to recollect the data in the new home
Region. Data collected in the old home Region doesn't migrate to the new home Region.
