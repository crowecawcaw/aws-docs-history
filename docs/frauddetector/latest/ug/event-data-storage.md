Amazon Fraud Detector will no longer be open to new customers starting November 7, 2025. If you would like to use Amazon Fraud Detector,
sign up prior to that date. For capabilities similar to Amazon Fraud Detector, explore Amazon SageMaker, AutoGluon, and AWS WAF.

# Event data storage

After you've gathered your dataset, you store your dataset internally using Amazon Fraud Detector or externally with Amazon Simple Storage Service (Amazon S3). We recommend that you choose
where to store your dataset based on the model you use for generating fraud predictions. The following is a detailed breakdown of these two storage options.

- **Internal storage-** Your dataset is stored with Amazon Fraud Detector. All event data associated with an event is stored together. You can upload the event dataset that’s stored with Amazon Fraud Detector
  at any time. You can either stream events one at a time to an Amazon Fraud Detector API, or import large datasets (up to 1GB) using the batch import feature. When you train a model using the dataset stored with
  Amazon Fraud Detector, you can specify a time range to limit the size of your dataset.
- **External storage-** Your dataset is stored in an external data source other than Amazon Fraud Detector. Currently, Amazon Fraud Detector supports using Amazon Simple Storage Service(Amazon S3) for this purpose.
  If your model is on a file that’s uploaded to Amazon S3, that file can’t be more than 5GB of uncompressed data. If it’s more than that, make sure to shorten the time range of your dataset.
  The following table provides details about the model type and the data source it supports.

| Model type                 | Compatible training data source    |
| -------------------------- | ---------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Online Fraud Insights      | External storage, Internal storage |
| Transaction Fraud Insights | Internal storage                   |
| Account Takeover Insights  | Internal storage                   | For information on storing your dataset externally with Amazon Simple Storage Service, see [Store your event data externally with Amazon S3](uploading-event-data-to-an-s3-bucket.md "uploading-event-data-to-an-s3-bucket.md") . For information on storing your dataset internally with Amazon Fraud Detector see [Store your event data internally with Amazon Fraud Detector](storing-event-data-afd.md "storing-event-data-afd.md"). |
