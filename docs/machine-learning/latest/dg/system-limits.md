We are no longer updating the Amazon Machine Learning service or accepting
new users for it. This documentation is available for existing users, but we are
no longer updating it. For more information, see [What is Amazon Machine Learning](what-is-amazon-machine-learning.md "what-is-amazon-machine-learning.md").

# System Limits

In order to provide a robust, reliable service, Amazon ML imposes
certain limits on the requests you make to the system. Most ML
problems fit easily within these constraints. However, if you do
find that your use of Amazon ML is being restricted by these
limits, you can contact
[AWS customer
service](https://aws.amazon.com/contact-us/ "https://aws.amazon.com/contact-us/") and request to have a limit raised. For example,
you might have a limit of five for the number of jobs that you can
run simultaneously. If you find that you often have jobs queued
that are waiting for resources because of this limit, then it
probably makes sense to raise that limit for your account.

The following table shows default per-account limits in Amazon ML.
Not all of these limits can be raised by AWS customer service.

| **Limit Type**                                           | **System Limit**                 |
| -------------------------------------------------------- | -------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Size of each observations                                | 100 KB                           |
| Size of training data \*                                 | 100 GB                           |
| Size of batch prediction input                           | 1 TB                             |
| Size of batch prediction input (number of records)       | 100 million                      |
| Number of variables in a data file (schema)              | 1,000                            |
| Recipe complexity (number of processed output variables) | 10,000                           |
| TPS for each real-time prediction endpoint               | 200                              |
| Total TPS for all real-time prediction endpoints         | 10,000                           |
| Total RAM for all real-time prediction endpoints         | 10 GB                            |
| Number of simultaneous jobs                              | 25                               |
| Longest run time for any job                             | 7 days                           |
| Number of classes for multiclass ML models               | 100                              |
| ML model size                                            | Minimum of 1 MB, maximum of 2 GB |
| Number of tags per object                                | 50                               | <br>• The size of your data files is limited to ensure that jobs finish in a timely manner. Jobs that have been running for more than seven days will be automatically terminated, resulting in a FAILED status. |
