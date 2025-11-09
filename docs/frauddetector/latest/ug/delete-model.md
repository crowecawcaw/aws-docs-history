Amazon Fraud Detector is no longer open to new customers as of November 7, 2025. For capabilities similar to Amazon Fraud Detector, explore Amazon SageMaker, AutoGluon, and AWS WAF.

# Delete a model or model version

You can delete models and model versions in Amazon Fraud Detector, provided that they are not associated
with a detector version. When you delete a model, Amazon Fraud Detector permanently deletes that model and the data is no longer stored in Amazon Fraud Detector.

You can also remove Amazon SageMaker AI models if they are not associated with
a detector version. Removing a SageMaker AI model disconnects it from Amazon Fraud Detector, but the model remains
available in SageMaker AI.

###### To delete a model version

You can only delete model versions that are in the `Ready to deploy` status. To change a model version from `ACTIVE` to
`Ready to deploy` status, undeploy the model version.

1. Sign in to the AWS Management Console and open the Amazon Fraud Detector console at [https://console.aws.amazon.com/frauddetector](https://console.aws.amazon.com/frauddetector "https://console.aws.amazon.com/frauddetector").
2. In the left navigation pane of the Amazon Fraud Detector console, choose
   **Models**.
3. Choose the model that contains the model version you want to delete.
4. Choose the model version that you want to delete.
5. Choose **Actions**, and then choose
   **Delete**.
6. Enter the model version name, and then choose **Delete model
   version**.

###### To undeploy a model version

You can't undeploy a model version that is in use by any detector version
(`ACTIVE`, `INACTIVE`, `DRAFT`). Therefore, to
undeploy a model version that is in use by a detector version, first remove the model
version from the detector version.

1. In the left navigation pane of the Amazon Fraud Detector console, choose
   **Models**.
2. Choose the model that contains the model version you want to undeploy.
3. Choose the model version that you want to delete.
4. Choose **Actions**, and then choose **Undeploy model
   version**.

###### To delete a model

Before deleting a model, you must first delete all model versions and are associated
with the model.

1. In the left navigation pane of the Amazon Fraud Detector console, choose
   **Models**.
2. Choose the model that you want to delete.
3. Choose **Actions**, and then choose
   **Delete**.
4. Enter the model name, and then choose **Delete model**.

###### To remove an Amazon SageMaker AI model

1. In the left navigation pane of the Amazon Fraud Detector console, choose
   **Models**.
2. Choose the SageMaker AI model that you want to remove.
3. Choose **Actions**, and then choose **Remove
   model**.
4. Enter the model name and then choose **Remove SageMaker AI
   model**.
