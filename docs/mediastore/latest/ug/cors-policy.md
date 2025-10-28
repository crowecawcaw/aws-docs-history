End of support notice: On November 13, 2025, AWS will discontinue support
for AWS Elemental MediaStore. After November 13, 2025, you will no longer be able to access the MediaStore console
or MediaStore resources. For more information, visit this
[blog post](https://aws.amazon.com/blogs/media/support-for-aws-elemental-mediastore-ending-soon/ "https://aws.amazon.com/blogs/media/support-for-aws-elemental-mediastore-ending-soon/").

# Cross-origin resource sharing (CORS) policies in AWS Elemental MediaStore

Cross-origin resource sharing (CORS) defines a way for client web applications that are loaded in one domain to interact with resources in a different
domain. With CORS support in AWS Elemental MediaStore, you can build rich client-side web applications with MediaStore and selectively allow cross-origin
access to your MediaStore resources.

###### Note

If you are using Amazon CloudFront to distribute content from a container that has a CORS policy, be sure to [configure the distribution for AWS Elemental MediaStore](../../../AmazonCloudFront/latest/DeveloperGuide/live-streaming.md#video-streaming-mediastore "../../../AmazonCloudFront/latest/DeveloperGuide/live-streaming.md#video-streaming-mediastore") (including the step to
edit the cache behavior to set up CORS).

This section provides an overview of CORS. The subtopics describe how you can enable CORS using the AWS Elemental MediaStore console, or programmatically
using the MediaStore REST API and the AWS SDKs.

###### Topics

- [CORS use-case scenarios](cors-policy-use-case-scenarios.md "cors-policy-use-case-scenarios.md")
- [Adding a CORS policy to a container](cors-policy-adding.md "cors-policy-adding.md")
- [Viewing a CORS policy](cors-policy-viewing.md "cors-policy-viewing.md")
- [Editing a CORS policy](cors-policy-editing.md "cors-policy-editing.md")
- [Deleting a CORS policy](cors-policy-deleting.md "cors-policy-deleting.md")
- [Troubleshooting CORS issues](cors-policy-troubleshooting.md "cors-policy-troubleshooting.md")
- [Example CORS policies](cors-policies-examples.md "cors-policies-examples.md")
