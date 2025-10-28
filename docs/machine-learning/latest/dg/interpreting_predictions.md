We are no longer updating the Amazon Machine Learning service or accepting
new users for it. This documentation is available for existing users, but we are
no longer updating it. For more information, see [What is Amazon Machine Learning](what-is-amazon-machine-learning.md "what-is-amazon-machine-learning.md").

# Generating and Interpreting Predictions

Amazon ML provides two mechanisms for generating predictions: asynchronous (batch-based) and
synchronous (one-at-a-time).

Use asynchronous predictions, or \*batch predictions**\*,** when you have a number of observations and would like to obtain
predictions for the observations all at once. The process uses a datasource as input, and
outputs predictions into a .csv file stored in an S3 bucket of your choice. You need to wait
until the batch prediction process completes before you can access the prediction results. The
maximum size of a datasource that Amazon ML can process in a batch file is 1 TB (approximately 100
million records). If your datasource is larger than 1 TB, your job will fail and Amazon ML will
return an error code. To prevent this, divide your data into multiple batches. If your records
are typically longer, you will reach the 1 TB limit before 100 million records are processed. In
this case, we recommend that you contact [AWS
support](https://aws.amazon.com/contact-us/ "https://aws.amazon.com/contact-us/") to increase the job size for your batch prediction.

Use synchronous, or \*real-time predictions**\*,** when you want to obtain predictions at low latency. The real-time prediction API
accepts a single input observation serialized as a JSON string, and synchronously returns the
prediction and associated metadata as part of the API response. You can simultaneously invoke
the API more than once to obtain synchronous predictions in parallel. For more information about
throughput limits of the real-time prediction API, see real-time prediction limits in [Amazon ML API
reference](../APIReference.md "../APIReference.md").

###### Topics

- [Creating a Batch Prediction](creating-batch-prediction-objects.md "creating-batch-prediction-objects.md")
- [Reviewing Batch Prediction Metrics](working-with-batch-predictions.md "working-with-batch-predictions.md")
- [Reading the Batch Prediction Output Files](reading-the-batchprediction-output-files.md "reading-the-batchprediction-output-files.md")
- [Requesting Real-time Predictions](requesting-real-time-predictions.md "requesting-real-time-predictions.md")
