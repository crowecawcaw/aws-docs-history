

AWS Data Pipeline is no longer available to new customers. Existing customers of AWS Data Pipeline can continue to use the service as normal. [Learn more](https://aws.amazon.com/blogs/big-data/migrate-workloads-from-aws-data-pipeline/)

# Tagging Your Pipeline
<a name="dp-adding-tags"></a>

Tags are case-sensitive key-value pairs that consist of a key and an optional value, both defined by the user. You can apply up to ten tags to each pipeline. Tag keys must be unique for each pipeline. If you add a tag with a key that is already associated with the pipeline, it updates the value of that tag.

Applying a tag to a pipeline also propagates the tags to its underlying resources (for example, Amazon EMR clusters and Amazon EC2 instances). However, it does not apply these tags to resources in a `FINISHED` or otherwise terminated state. You can use the CLI to apply tags to these resources, if needed.

When you are finished with a tag, you can remove it from your pipeline.

**To tag your pipeline using the AWS CLI**  
To add tags to a new pipeline, add the `--tags` option to your [create-pipeline](https://docs.aws.amazon.com/cli/latest/reference/datapipeline/create-pipeline.html) command. For example, the following option creates a pipeline with two tags, an `environment` tag with a value of `production`, and an `owner` tag with a value of `sales`.

```
--tags key=environment,value=production key=owner,value=sales
```

To add tags to an existing pipeline, use the [add-tags](https://docs.aws.amazon.com/cli/latest/reference/datapipeline/add-tags.html) command as follows:

```
aws datapipeline add-tags --pipeline-id {{df-00627471SOVYZEXAMPLE}} --tags key=environment,value=production key=owner,value=sales
```

To remove tags from an existing pipeline, use the [remove-tags](https://docs.aws.amazon.com/cli/latest/reference/datapipeline/remove-tags.html) command as follows:

```
aws datapipeline remove-tags --pipeline-id {{df-00627471SOVYZEXAMPLE}} --tag-keys environment owner
```