Amazon Monitron is no longer open to new customers. Existing customers can
continue to use the service as normal. For capabilities similar to Amazon
Monitron, see our [blog post](https://aws.amazon.com/blogs/machine-learning/maintain-access-and-consider-alternatives-for-amazon-monitron "https://aws.amazon.com/blogs/machine-learning/maintain-access-and-consider-alternatives-for-amazon-monitron").

# Accessing your Amazon Monitron data

There are two ways to access your raw Amazon Monitron data outside of Amazon Monitron.

You may want access your data on an ongoing basis, so that you can use it elsewhere. In
that case, you can configure Amazon Monitron to automatically [add your data to a Kinesis
stream](monitron-kinesis-export.md "monitron-kinesis-export.md"). From there, you can port it to various destinations, including Amazon S3 and
Lambda. This process requires configuration, and that configuration requires an understanding
of Kinesis Data Streams. However, once you have all the elements arranged to your satisfaction, you can
keep your data streaming automatically.

Or you may want to access your data once in a while, just to gain a clear understanding of
what kind of data you are storing and analyzing on AWS. In that case, you can ask AWS
support to [manually copy your data to Amazon S3](data-download-monitron.md "data-download-monitron.md").
This process requires less configuration, but it cannot be automated. It only gives you the
data that Amazon Monitron has accumulated up until now, in one chunk.

###### Topics

- [Exporting your Amazon Monitron data to Amazon S3](data-download-monitron.md "data-download-monitron.md")
- [Amazon Monitron Kinesis data export v1](monitron-kinesis-export.md "monitron-kinesis-export.md")
- [Amazon Monitron Kinesis data export v2](monitron-kinesis-export-v2.md "monitron-kinesis-export-v2.md")
