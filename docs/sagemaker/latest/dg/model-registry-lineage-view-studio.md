# View model lineage details in

Studio

You can view the lineage details of a registered model in Amazon SageMaker Studio. The
following will provide instructions on how to access the lineage view in
Studio. See [Amazon SageMaker ML Lineage Tracking](lineage-tracking.md "lineage-tracking.md")
for more information about lineage tracking in Amazon SageMaker Studio.

This feature is not available in Amazon SageMaker Studio Classic.

- If Studio is your default experience, the UI is similar to the images
  found in [Amazon SageMaker Studio UI overview](studio-updated-ui.md "studio-updated-ui.md").
- If Studio Classic is your default experience, the UI is similar to the images
  found in [Amazon SageMaker Studio Classic UI Overview](studio-ui.md "studio-ui.md").
  The lineage view is an interactive visualization of the resources associated with
  your registered models. These resources include datasets, training jobs, approvals,
  models, and endpoints. In the lineage you can also view the associated resource
  details, including the source URI, creation timestamp, and other metadata.

The following capabilities are available in `us-east-1`, `us-west-2`,
`ap-northeast-1`, and `eu-west-1` regions:

You can track the lineage of logged and registered models. Furthermore, lineage
for models resources include datasets, evaluators, training jobs, approvals, models,
inference components, and endpoints. In the lineage you can also view the associated
resource details, including the source URI, creation timestamp, and other
metadata.

The following provides instructions on how to access the lineage details for a
registered model version.

###### To access the lineage details for a registered model version

1. Open the Studioconsole by following the instructions in [Launch Amazon SageMaker Studio](studio-updated-launch.md "studio-updated-launch.md").
2. Choose **Models** from the left navigation pane.
3. Choose the **Registered models** tab, if not selected
   already.
4. Immediately below the **Registered models** tab label,
   choose **Model Groups**, if not selected already.
5. (Optional) If you have models that are shared with you, you can choose
   between **My models** or **Shared with
   me**.
6. Select a registered model.
7. Choose the **Versions** tab, if not selected
   already.
8. Choose a specific model version from the **Versions**
   list.
9. Choose the **Lineage** tab.
   In the **Lineage** tab you can navigate through the resources
   associated with the model version. You can also choose a resource to view the
   resource details.

Note that the Lineage view is for visualization purposes only. Rearranging or
moving the components in this view does not affect the actual registered model
resources.

For `us-east-1`, `us-west-2`, `ap-northeast-1`,
and `eu-west-1` regions, you can use the following instructions to access
the lineage details for logged and registered model versions:

1. Open the Studio console by following the instructions in [Launch Amazon SageMaker Studio](studio-updated-launch.md "studio-updated-launch.md").
2. Choose **Models** from the left navigation pane.
3. Choose the **My models** tab.
4. (Optional) If you have models that are shared with you, you can choose between **Created by me** or **Shared
   with me**.
5. Select a model and choose **View Latest Version**.
6. Choose the **Lineage** tab.
