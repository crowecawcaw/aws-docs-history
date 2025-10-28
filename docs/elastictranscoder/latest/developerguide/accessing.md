End of support notice: On November 13, 2025, AWS will discontinue support for Amazon Elastic Transcoder. After November 13, 2025, you will no longer be able to access the Elastic Transcoder console or Elastic Transcoder resources.

For more information about transitioning to AWS Elemental MediaConvert, visit this [blog post](https://aws.amazon.com/blogs/media/how-to-migrate-workflows-from-amazon-elastic-transcoder-to-aws-elemental-mediaconvert/ "https://aws.amazon.com/blogs/media/how-to-migrate-workflows-from-amazon-elastic-transcoder-to-aws-elemental-mediaconvert/").

# Accessing Elastic Transcoder

Elastic Transcoder is a RESTful web service that uses HTTPS as the protocol and JavaScript Object Notation (JSON)
as the message format. Your application code can make requests directly to the Elastic Transcoder API.
When using the REST API directly, you must write the necessary code to sign and authenticate your requests.
For more information about the API and about signing requests, see [API Reference](api-reference.md "api-reference.md").

Elastic Transcoder also provides a management console. You can use the console to perform all of the same operations that you can
perform using the Elastic Transcoder API. For information about using the console to create and manage pipelines, presets, and jobs,
see the applicable topic:

- [Working with Jobs](working-with-jobs.md "working-with-jobs.md")
- [Working with Pipelines](working-with-pipelines.md "working-with-pipelines.md")
- [Working with Presets](working-with-presets.md "working-with-presets.md")

## Regions and Endpoints

You create pipelines in a specific AWS region. You always send your Elastic Transcoder requests to a region-specific endpoint.
For a list of supported AWS regions, go to the [Regions and Endpoints](../../../general/latest/gr/rande.md#elastictranscoder_region "../../../general/latest/gr/rande.md#elastictranscoder_region")
section in the _Amazon Web Services General Reference_.
