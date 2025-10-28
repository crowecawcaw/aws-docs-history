# Custom tag propagation

Amazon SageMaker AI supports the ability to propagate custom tags set at the domain, user profile, and
space level to all of the SageMaker AI resources created in the context of Amazon SageMaker Studio,
JupyterLab, Code Editor, based on Code-OSS, Visual Studio Code - Open Source, and Amazon SageMaker Canvas. With custom tag propagation, users can propagate their
own custom tags to resources to improve cost tracking and tie resources to specific projects and
teams.

To activate this feature, use the `TagPropagation` attribute in the [CreateDomain](../APIReference/API_CreateDomain.md "../APIReference/API_CreateDomain.md") and [UpdateDomain](../APIReference/API_UpdateDomain.md "../APIReference/API_UpdateDomain.md") APIs. Custom
tag propagation can only be set at the domain level, which means that all users and spaces in a
domain use the feature when it is activated. It is not possible to modify custom tag propagation
settings at the user profile or space level. For more information about using custom tag
propagation, see [Add custom tags to resources](custom-tags-add.md "custom-tags-add.md").

###### Note

System tags added by AWS services on a domain, user profile, and space are not propagated.

## Example use cases

Custom tag propagation is particularly useful for the following use cases.

- Track cost across all of the SageMaker AI resources created in Amazon SageMaker Studio.
- Track cost for SageMaker AI resources that are created in Amazon SageMaker Canvas. This includes models
  deployed on a SageMaker AI endpoint.
- Track cost incurred for an Amazon DataZone project by propagating the Amazon DataZone
  project ID to all the resources created by Amazon SageMaker Studio.

## Tag merging

With custom tag propagation activated, resources created at the user profile and space level
take on the tags specified at the domain level, as well as those specified during user profile
or space creation.

SageMaker AI resources have a 50 tag limit. If the number of tags added to a resource exceeds 50,
SageMaker AI returns an error during resource creation. We recommend limiting the number of tags to
avoid this. For example, assume a user has 25 tags for their domain and 30 tags for their user
profile. When the user creates a resource, a total of 55 tags propagate to the resource.
Because the aggregate tag total exceeds 50, resource creation fails until the user removes at
least 5 tags.

###### Note

By default, SageMaker AI automatically adds the `sagemaker:user-profile-arn`,
`sagemaker:domain-arn`, or `sagemaker:space-arn` tag to SageMaker AI
resources. SageMaker AI adds the ARN tag regardless of whether or not the domain is using custom tag
propagation. These ARN tags also contribute toward the 50 tag limit.
