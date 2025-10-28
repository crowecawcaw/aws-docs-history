# Image Builder output image resources

After you have created image resources for AMI or container images with
Image Builder, you can manage them using the Image Builder console, through the Image Builder API, or
with **imagebuilder** commands in the AWS CLI.

###### Tip

When you have multiple resources of the same type, tagging helps you to
identify a specific resource based on the tags you've assigned to it.
For more information about tagging your resources using Image Builder commands
in the AWS CLI, see the [Tag resources](tag-resources.md "tag-resources.md")
section of this guide.

This section covers how to list, view, and create images. For information
about image workflows and how to manage them, see [Manage build and test workflows for Image Builder images](manage-image-workflows.md "manage-image-workflows.md").

###### Contents

- [List images and build versions](image-details-list.md "image-details-list.md")
- [View image resource details](view-image-details.md "view-image-details.md")
- [Create custom images with Image Builder](create-images.md "create-images.md")
- [Import and export virtual machine images with Image Builder](vm-import-export.md "vm-import-export.md")
- [Import verified Windows ISO disk images with Image Builder](import-iso-disk.md "import-iso-disk.md")
- [Manage security findings for Image Builder images](image-security-findings.md "image-security-findings.md")
- [Clean up Image Builder resources](#images-cleanup "#images-cleanup")

## Clean up Image Builder resources

To avoid unexpected charges, make sure to clean up resources
and pipelines that you created from the examples in this guide.
For more information about deleting resources in Image Builder, see
[Delete outdated or unused Image Builder resources](delete-resources.md "delete-resources.md").
