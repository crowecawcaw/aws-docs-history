

# Data exports using Amazon S3 subscriptions

Use a data subscription to receive one AWS Marketplace seller dataset in an Amazon Simple Storage Service (Amazon S3) bucket that you own, every day. You provide the AWS Key Management Service (AWS KMS) key that encrypts every file. You can load the files into your data warehouse, business intelligence, or analytics tools without building an export pipeline.

You create and manage data subscriptions in AWS Partner Central. Each subscription delivers one dataset to one bucket. You can create several subscriptions that deliver to the same bucket, or use a different bucket for each one. You can't change a subscription after you create it. To change its dataset, bucket, or key, cancel it and create a new one.

**Note**  
You keep control of the bucket. AWS Marketplace writes to it, but it never reads, lists, or deletes your objects, and it never rewrites a file that it has delivered.  
For more information about AWS Partner datasets, such as opportunities and leads, see [Delivering partner reporting data to your account with data subscriptions](https://docs.aws.amazon.com/partner-central/latest/getting-started/data-subscriptions.html) in the *AWS Partner Central Getting Started Guide*.

**Topics**
+ [Available datasets](data-subscriptions-datasets.md)
+ [Prerequisites](data-subscriptions-prerequisites.md)
+ [Creating a data subscription](data-subscriptions-create.md)
+ [Monitoring delivery](data-subscriptions-monitor.md)
+ [Understanding the delivered files](data-subscriptions-files.md)
+ [Cancelling a data subscription](data-subscriptions-cancel.md)
+ [Controlling access to data subscriptions](data-subscriptions-iam.md)
+ [Data subscription limits](data-subscriptions-quotas.md)