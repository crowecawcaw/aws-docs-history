Amazon Fraud Detector is no longer open to new customers as of November 7, 2025. For capabilities similar to Amazon Fraud Detector, explore Amazon SageMaker, AutoGluon, and AWS WAF.

# Delete a detector, detector version, or rule

version

Before deleting a detector in Amazon Fraud Detector, you must first delete all detector versions and
rule versions that are associated with the detector.

When you delete a detector, detector version, or rule version, Amazon Fraud Detector permanently deletes
that resource and the data is no longer stored in Amazon Fraud Detector.

###### To delete a detector version

You can only delete detector versions that are in `DRAFT` or
`INACTIVE` status.

1. Sign in to the AWS Management Console and open the Amazon Fraud Detector console at [https://console.aws.amazon.com/frauddetector](https://console.aws.amazon.com/frauddetector "https://console.aws.amazon.com/frauddetector").
2. In the left navigation pane of the Amazon Fraud Detector console, choose
   **Detectors**.
3. Choose the detector that contains the detector version you want to delete.
4. Choose the detector version that you want to delete.
5. Choose **Actions**, and then choose
   **Delete**.
6. Enter `delete`, and then choose **Delete
   detector**.

###### To delete a rule version

You can delete a rule version only if it is not used by any `ACTIVE` or `INACTIVE` detector versions. If necessary, before deleting a rule version, first move the `ACTIVE` detector version to `INACTIVE`, then delete the `INACTIVE` detector version.

1. In the left navigation pane of the Amazon Fraud Detector console, choose
   **Detectors**.
2. Choose the detector that contains the rule version you want to delete.
3. Choose the **Associated rules** tab, and choose the rule that you
   want to delete.
4. Choose the rule version that you want to delete.
5. Choose **Actions**, and then choose **Delete rule
   version**.
6. Enter `delete`, and then choose **Delete
   version**.

###### To delete a detector

Before deleting a detector, you must first delete all detector versions and rule
versions that are associated with the detector.

1. In the left navigation pane of the Amazon Fraud Detector console, choose
   **Detectors**.
2. Choose the detector that you want to delete.
3. Choose **Actions**, and then choose **Delete
   detector**.
4. Enter `delete`, and then choose **Delete
   detector**.
