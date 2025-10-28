End of support notice: On November 13, 2025, AWS will discontinue support
for AWS Elemental MediaStore. After November 13, 2025, you will no longer be able to access the MediaStore console
or MediaStore resources. For more information, visit this
[blog post](https://aws.amazon.com/blogs/media/support-for-aws-elemental-mediastore-ending-soon/ "https://aws.amazon.com/blogs/media/support-for-aws-elemental-mediastore-ending-soon/").

# Policies in AWS Elemental MediaStore

You can apply one or more of these policies to your AWS Elemental MediaStore container:

- [Container policy](policies.md "policies.md") - Sets access rights to all folders and objects within the container. MediaStore sets a default policy
  that allows users to perform all MediaStore operations on the container. This policy specifies that all operations must be performed over
  HTTPS. After you create a container, you can edit the container policy.
- [Cross-origin resource sharing (CORS) policy](cors-policy.md "cors-policy.md") - Allows client web applications from one domain to interact with resources
  in a different domain. MediaStore does not set a default CORS policy.
- [Metrics policy](policies-metric.md "policies-metric.md") - Allows MediaStore to send metrics to Amazon CloudWatch. MediaStore does not set a default metric
  policy.
- [Object lifecycle policy](policies-object-lifecycle.md "policies-object-lifecycle.md") - Controls how long objects remain in a MediaStore container. MediaStore
  does not set a default object lifecycle policy.
