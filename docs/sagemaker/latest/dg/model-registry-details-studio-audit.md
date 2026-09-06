

# Update audit (governance) information (Studio)
<a name="model-registry-details-studio-audit"></a>

**Important**  
As of November 30, 2023, the previous Amazon SageMaker Studio experience is now named Amazon SageMaker Studio Classic. The following section is specific to using the updated Studio experience. For information about using the Studio Classic application, see [Amazon SageMaker Studio Classic](studio.md).

Document important model details to help your organization establish a robust framework of model governance. You and your team members can reference these details so they use the model for the appropriate use cases, know the business domain and owners of the model, and understand model risks. You can also save details about how the model is expected to perform and reasons for performance limitations.

**To view or update details related to the model governance, complete the following steps.**

1. On the **Audit** tab, view the approval status of the model card. The status can be one the following:
   + **Draft**: The model card is still a draft.
   + **Pending approval**: The model card is waiting to be approved.
   + **Approved**: The model card is approved.

1. To update the approval status of the model card, choose the pulldown menu next to the approval status and choose the updated approval status.

1. To update and view details related to your model package risk, complete the following steps.

   1. Choose **Risk** in the left sidebar of the **Audit** tab.

   1. View the current risk rating and explanation for the risk rating.

   1. To update the rating or explanation, complete the following steps.

      1. Choose the vertical ellipsis at the top right corner of the **Audit** page, and choose **Edit**.

      1. (Optional) Choose an updated risk rating.

      1. (Optional) Update the risk rating explanation.

      1.  At the top of the model version page, choose **Save** in the **Editing Model Version...** banner.

1. To update and view details related to the usage of your model package, complete the following steps.

   1. Choose **Usage** in the left sidebar of the **Audit** tab.

   1. View text you added in the following fields:
      + **Problem type**: The category of machine learning algorithm used to build your model.
      + **Algorithm type**: The specific algorithm used to create your model.
      + **Intended uses**: The current application of the model in your business problem.
      + **Factors affecting model efficacy**: Notes about your model’s performance limitations.
      + **Recommended use**: The types of applications you can create with the model, the scenarios in which you can expect a reasonable performance, or the type of data to use with the model.
      + **Ethical considerations**: A description of how your model might discriminate based on factors such as age or gender.

   1. To update any of the previously listed fields, complete the following steps.

      1. Choose the vertical ellipsis at the top right corner of the model version page, and choose **Edit**.

      1. (Optional) Use the dropdown menus for **Problem type** and **Algorithm type** to select new values, if needed.

      1. (Optional) Update the text descriptions in the remaining fields.

      1.  At the top of the model version page, choose **Save** in the **Editing Model Version...** banner.

1. To update and view details related to the stakeholders of your model package, complete the following steps.

   1. Choose **Stakeholders** in the left sidebar of the **Audit** tab.

   1. View the current model owner and creator, if any.

   1. To update the model owner or creator, complete the following steps:

      1. Choose the vertical ellipsis at the top right corner of the model version page, and choose **Edit**.

      1. Update the model owner or model creator fields.

      1.  At the top of the model version page, choose **Save** in the **Editing Model Version...** banner.

1. To update and view details related to the business problem that your model package addresses, complete the following steps.

   1. Choose **Business** in the left sidebar of the **Audit** tab.

   1. View the current descriptions, if any, for the business problem that the model addresses, the business problem stakeholders, and the line of business.

   1. To update any of the fields in the **Business** tab, complete the following steps.

      1. Choose the vertical ellipsis at the top right corner of the model version page, and choose **Edit**.

      1. Update the descriptions in any of the fields.

      1.  At the top of the model version page, choose **Save** in the **Editing Model Version...** banner.

1. To update and view existing documentation (represented as key-value pairs) for your model, complete the following steps.

   1. Choose **Documentation** in the left sidebar of the **Audit** page.

   1. View existing key-value pairs.

   1. To add any key-value pairs, complete the following steps.

      1. Choose the vertical ellipsis at the top right corner of the model version page, and choose **Edit**.

      1. Choose **Add**.

      1. Enter a new key and associated value.

      1.  At the top of the model version page, choose **Save** in the **Editing Model Version...** banner.

   1. To remove any key-value pairs, complete the following steps.

      1. Choose the vertical ellipsis at the top right corner of the model version page, and choose **Edit**.

      1. Choose the **Trash** icon next to the key-value pair to remove.

      1.  At the top of the model version page, choose **Save** in the **Editing Model Version...** banner.