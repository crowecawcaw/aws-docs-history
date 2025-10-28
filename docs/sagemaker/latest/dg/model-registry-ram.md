# Cross-account discoverability

By exploring and accessing model package groups registered in other accounts, data
scientists and data engineers can promote data consistency, streamline
collaboration, and reduce duplication of effort. With Amazon SageMaker Model Registry, you can share model
package groups across accounts. There are two categories of permissions associated
with the sharing of resources:

- **Discoverability**: _Discoverability_ is the ability of the resource consumer
  account to see the model package groups shared by one or more resource owner
  accounts. Discoverability is only possible if the resource owner attaches
  the necessary resource policies to the shared model package groups. The
  resource consumer can view all shared model package groups in the AWS RAM UI
  and AWS CLI.
- **Accessibility**: _Accessibility_ is the ability of the resource consumer
  account to use the shared model package groups. For example, the resource
  consumer can register or deploy a model package from a different account if
  they have the necessary permissions.

###### Topics

- [Share model group in
  Studio](model-registry-ram-studio-share.md "model-registry-ram-studio-share.md")
- [View shared model groups in
  Studio](model-registry-ram-studio-view.md "model-registry-ram-studio-view.md")
- [Accessibility](model-registry-ram-accessibility.md "model-registry-ram-accessibility.md")
- [Set up discoverability](model-registry-ram-discover.md "model-registry-ram-discover.md")
- [View shared model package
  groups](model-registry-ram-view-shared.md "model-registry-ram-view-shared.md")
- [Dissociate principals from a
  resource share and remove a resource share](model-registry-ram-dissociate.md "model-registry-ram-dissociate.md")
- [Promote the permission and resource
  share](model-registry-ram-promote.md "model-registry-ram-promote.md")
