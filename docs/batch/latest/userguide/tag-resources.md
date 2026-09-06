

# Tag your resources
<a name="tag-resources"></a>

You can tag new or existing AWS Batch compute environments, jobs, job definitions, job queues, and scheduling policies.

If you're using the AWS Batch console, you can apply tags to new resources when they are created or to existing resources at any time using the **Tags** tab on the relevant resource page.

If you're using the AWS Batch API, the AWS CLI, or an AWS SDK, you can apply tags to new resources using the `tags` parameter on the relevant API action or to existing resources using the `TagResource` API action. For more information, see [TagResource](https://docs.aws.amazon.com/batch/latest/APIReference/API_TagResource.html).

Some resource-creating actions enable you to specify tags for a resource when the resource is created. If tags cannot be applied during resource creation, the resource creation process fails. This ensures that resources you intended to tag on creation are either created with specified tags or not created at all. If you tag resources at the time of creation, you don't need to run custom tagging scripts after resource creation.

The following table describes the AWS Batch resources that can be tagged, and the resources that can be tagged on creation.


**Tag support for AWS Batch resources**  

| Resource | Supports tags | Supports tag propagation | Supports tagging on creation (AWS Batch API, AWS CLI, AWS SDK) | 
| --- | --- | --- | --- | 
| AWS Batch compute environments | Yes | No. Compute environment tags do not propagate to any other resources. Tags for the resources are specified in the tags member of the computeResources object passed in the [CreateComputeEnvironment](https://docs.aws.amazon.com/batch/latest/APIReference/API_CreateComputeEnvironment.html) API operation. | Yes | 
| AWS Batch jobs | Yes | Yes | Yes | 
| AWS Batch job definitions | Yes | Yes. Set `propagateTags` on [RegisterJobDefinition](https://docs.aws.amazon.com/batch/latest/APIReference/API_RegisterJobDefinition.html) to propagate job definition tags to the corresponding Amazon ECS task. `propagateTags` is not supported for jobs that run on Amazon EKS resources. If both a job and its job definition specify the same tag, then the job's tag takes priority. | Yes | 
| AWS Batch job queues | Yes | No | Yes | 
| AWS Batch scheduling policies | Yes | No | Yes | 
| AWS Batch service environments | Yes | No | Yes | 
| AWS Batch consumable resources | Yes | No | Yes | 
| AWS Batch quota shares | Yes | No | Yes | 