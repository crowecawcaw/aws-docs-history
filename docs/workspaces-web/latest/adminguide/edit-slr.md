

# Editing a service-linked role for WorkSpaces Secure Browser
<a name="edit-slr"></a>

WorkSpaces Secure Browser doesn't allow you to edit the `AWSServiceRoleForAmazonWorkSpacesWeb` service-linked role. After you create a service-linked role, you can't change the name of the role because various entities might reference the role. However, you can edit the description of the role using IAM. For more information, see [Editing a Service-Linked Role](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html#edit-service-linked-role) in the *IAM User Guide*.