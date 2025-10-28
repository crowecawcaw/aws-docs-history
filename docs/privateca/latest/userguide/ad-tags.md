# Tagging Connector for AD resources

You can apply tags to your connectors, templates, and directory registrations. Tagging
adds metadata to a resource that can assist with organization and management.

Console

**To manage resource tagging using the console**

Tagging of existing resources is managed on the details page for the resource. For more
information, see the following procedures:

- [View connector template
  details](view-template.md "view-template.md")
- [Managing directory
  registrations](directory-registration.md "directory-registration.md")

API

**To manage resource tagging using the API**

**Tag**: [TagResource](../../../pca-connector-ad/latest/APIReference/API_TagResource.md "../../../pca-connector-ad/latest/APIReference/API_TagResource.md") action in the AWS Private CA Connector for Active Directory API.

**List tags**: [ListTagsForResource](../../../pca-connector-ad/latest/APIReference/API_ListTagsForResource.md "../../../pca-connector-ad/latest/APIReference/API_ListTagsForResource.md") action in the AWS Private CA Connector for Active Directory API.

**Untag**: [UntagResource](../../../pca-connector-ad/latest/APIReference/API_UntagResource.md "../../../pca-connector-ad/latest/APIReference/API_UntagResource.md") action in the AWS Private CA Connector for Active Directory API.

Important - It is acceptable to use tags to label objects containing confidential data.
However, the tags themselves shouldn't contain any personally identifiable information
(PII), sensitive, or confidential information.

CLI

**To manage resource tagging using the CLI**

**Tag**: [tag-resource](../../../cli/latest/reference/pca-connector-ad/tag-resource.md "../../../cli/latest/reference/pca-connector-ad/tag-resource.md") command in the AWS Private CA Connector for Active Directory section of the AWS CLI.

**List tags**: [list-tags-for-resource](../../../cli/latest/reference/pca-connector-ad/list-tags-for-resource.md "../../../cli/latest/reference/pca-connector-ad/list-tags-for-resource.md") command in the AWS Private CA Connector for Active Directory section of the
AWS CLI.

**Untag**: [untag-resource](../../../cli/latest/reference/pca-connector-ad/untag-resource.md "../../../cli/latest/reference/pca-connector-ad/untag-resource.md") command in the AWS Private CA Connector for Active Directory section of the AWS CLI.
