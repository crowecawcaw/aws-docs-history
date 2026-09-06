

# Tagging Connector for AD resources
<a name="ad-tags"></a>

You can apply tags to your connectors, templates, and directory registrations. Tagging adds metadata to a resource that can assist with organization and management.

------
#### [ Console ]

 **To manage resource tagging using the console** 

Tagging of existing resources is managed on the details page for the resource. For more information, see the following procedures:
+  [View connector template details](view-template.html) 
+  [Managing directory registrations](directory-registration.html) 

------
#### [ API ]

 **To manage resource tagging using the API** 

**Tag**: [ TagResource](https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_TagResource.html) action in the AWS Private CA Connector for Active Directory API.

**List tags**: [ ListTagsForResource](https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_ListTagsForResource.html) action in the AWS Private CA Connector for Active Directory API.

**Untag**: [ UntagResource](https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_UntagResource.html) action in the AWS Private CA Connector for Active Directory API.

Important - It is acceptable to use tags to label objects containing confidential data. However, the tags themselves shouldn't contain any personally identifiable information (PII), sensitive, or confidential information.

------
#### [ CLI ]

 **To manage resource tagging using the CLI** 

**Tag**: [ tag-resource](https://docs.aws.amazon.com/cli/latest/reference/pca-connector-ad/tag-resource.html) command in the AWS Private CA Connector for Active Directory section of the AWS CLI.

**List tags**: [ list-tags-for-resource](https://docs.aws.amazon.com/cli/latest/reference/pca-connector-ad/list-tags-for-resource.html) command in the AWS Private CA Connector for Active Directory section of the AWS CLI.

**Untag**: [ untag-resource](https://docs.aws.amazon.com/cli/latest/reference/pca-connector-ad/untag-resource.html) command in the AWS Private CA Connector for Active Directory section of the AWS CLI.

------