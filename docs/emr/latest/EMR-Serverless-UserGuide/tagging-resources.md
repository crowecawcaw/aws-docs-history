# Tagging your resources

You can tag new or existing applications and job runs. If you're using the
Amazon EMR Serverless API, the AWS CLI, or an AWS SDK, you can apply tags to new resources
using the `tags` parameter on the relevant API action. You can apply tags to
existing resources using the `TagResource` API action.

You can use some resource-creating actions to specify tags for a resource when the
resource is created. In this case, if tags cannot be applied while the resource is being
created, the resource fails to be created. This mechanism ensures that resources you
intended to tag on creation are either created with specified tags or not created at
all. If you tag resources at the time of creation, you do not need to run custom tagging
scripts after creating a resource.

The following table describes the Amazon EMR Serverless resources that can be
tagged.

| Taggable resources | Resource | Supports tags                                                                                          | Supports tag propagation | Supports tagging on creation (Amazon EMR Serverless API, AWS CLI, and<br>AWS SDK) | API for creation (tags can be added during creation) |
| ------------------ | -------- | ------------------------------------------------------------------------------------------------------ | ------------------------ | --------------------------------------------------------------------------------- | ---------------------------------------------------- |
| Application        | Yes      | No. Tags associated with an application do not propagate to job runs<br>submitted to that application. | Yes                      | `CreateApplication`                                                               |
| Job run            | Yes      | No                                                                                                     | Yes                      | `StartJobRun`                                                                     |
