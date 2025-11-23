# Updating the stream poller

The following information outlines the steps needed to update the stream poller with the latest Lambda artifacts using
the AWS management console.

## To update the stream poller with the latest Lambda artifacts

You can update the stream poller with the latest Lambda code artifacts as follows:

1. In the AWS Management Console, navigate to CloudFormation and select the main parent CloudFormation stack.
2. Select the **Update** option for the stack.
3. Select **Replace current template**.
4. For the template source, choose **Amazon S3 URL** and enter
   the following S3 URL:

```
https://aws-neptune-customer-samples.s3.amazonaws.com/neptune-stream/neptune_to_elastic_search.json
```

5. Select **Next** without changing any CloudFormation parameters.
6. Choose **Update Stack**.

The stack will now update the Lambda artifacts with the most recent ones.

## Extending the stream poller to support custom fields

The current stream poller can easily be extended to write custom code for handling
custom fields, as is explained in detail in this blog post: [Capture
graph changes using Neptune Streams](https://aws.amazon.com/blogs/database/capture-graph-changes-using-neptune-streams/ "https://aws.amazon.com/blogs/database/capture-graph-changes-using-neptune-streams/").

###### Note

When adding a custom field in OpenSearch, make sure to add the new field
as an inner object of a predicate (see [Neptune Full-text search data model](full-text-search-model.md "full-text-search-model.md")).
