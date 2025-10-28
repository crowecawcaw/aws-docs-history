# Security with multi-container endpoints with direct

invocation

For multi-container endpoints with direct invocation, there are multiple containers
hosted in a single instance by sharing memory and a storage volume. It's your
responsibility to use secure containers, maintain the correct mapping of requests to
target containers, and provide users with the correct access to target containers. SageMaker AI
uses IAM roles to provide IAM identity-based policies that you use to specify
whether access to a resource is allowed or denied to that role, and under what
conditions. For information about IAM roles, see [IAM roles](../../../IAM/latest/UserGuide/id_roles.md "../../../IAM/latest/UserGuide/id_roles.md") in the
_AWS Identity and Access Management User Guide_. For information about identity-based
policies, see [Identity-based
policies and resource-based policies](../../../IAM/latest/UserGuide/access_policies_identity-vs-resource.md "../../../IAM/latest/UserGuide/access_policies_identity-vs-resource.md").

By default, an IAM principal with `InvokeEndpoint` permissions on a
multi-container endpoint with direct invocation can invoke any container inside the
endpoint with the endpoint name that you specify when you call
`invoke_endpoint`. If you need to restrict `invoke_endpoint`
access to a limited set of containers inside a multi-container endpoint, use the
`sagemaker:TargetContainerHostname` IAM condition key. The following
policies show how to limit calls to specific containers within an endpoint.
