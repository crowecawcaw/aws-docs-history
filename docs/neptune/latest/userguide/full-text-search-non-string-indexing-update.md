# Updating an existing Neptune full-text search stack to support non-string indexing

If you are already using Neptune full-text search, here are the steps you
need to take to support non-string indexing:

1. **Stop the stream poller Lambda function.**
   This ensures that no new updates are copied during export. Do this by disabling
   the cloud event rule that invokes the Lambda function:
   - In the AWS Management Console, navigate to CloudWatch.
   - Select **Rules**.
   - Choose the rule with the Lambda stream poller name.
   - Select **disable** to temporarily disable the rule.

2. **Delete the current Neptune index in OpenSearch.**
   Use the following `curl` query to delete the `amazon_neptune` index
   from your OpenSearch cluster:

```
curl -X DELETE "`your OpenSearch endpoint`/amazon_neptune"
```

3. **Start a one-time export from Neptune to OpenSearch.**
   It is best to set up a new OpenSearch stack at this point, so that new artifacts
   are picked up for the poller that performs the export.

Follow the steps listed [here
in GitHub](https://github.com/awslabs/amazon-neptune-tools/blob/master/export-neptune-to-elasticsearch/readme.md " https://github.com/awslabs/amazon-neptune-tools/blob/master/export-neptune-to-elasticsearch/readme.md") to start the one-time export of your Neptune data into OpenSearch. 4. **Update the Lambda artifacts for the existing stream poller.**
After the export of Neptune data to OpenSearch has completed successfully,
take the following steps:

    * In the AWS Management Console, navigate to CloudFormation.
    * Choose the main parent CloudFormation stack.
    * Select the **Update** option for that stack.
    * Select **Replace current template from options**.
    * For the template source, select **Amazon S3 URL**.
    * For the Amazon S3 URL, enter:



    ```
    https://aws-neptune-customer-samples.s3.amazonaws.com/neptune-stream/neptune_to_elastic_search.json
    ```
    * Choose **Next** without changing any of the CloudFormation parameters.
    * Select **Update stack**. CloudFormation will replace the Lambda
     code artifacts for the stream poller with the latest artifacts.

5. **Start the stream poller again.**
   Do this by enabling the appropriate CloudWatch rule:
   - In the AWS Management Console, navigate to CloudWatch.
   - Select **Rules**.
   - Choose the rule with the Lambda stream poller name.
   - Select **enable**.
