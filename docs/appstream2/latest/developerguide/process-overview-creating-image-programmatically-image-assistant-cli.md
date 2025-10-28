# Process Overview for Programmatically Creating an Amazon AppStream 2.0 Image

You can use the Image Assistant CLI operations with your application
installation automation to create a fully programmatic AppStream 2.0 image creation workflow.
After your application installation automation completes, but before the image is
created, use the Image Assistant CLI operations to specify the following:

- The executable files that your users can launch
- The optimization manifests for your applications
- Other AppStream 2.0 image metadata
  The following high-level overview describes the process for programmatically creating an AppStream 2.0 image.

1. Use your application installation automation to install the required applications on your
   image builder. This installation may include applications that your users will launch, any dependencies, and background applications.
2. Determine the files and folders to optimize.
3. If applicable, use the Image Assistant `add-application` CLI operation to specify the application metadata and optimization manifest for the AppStream 2.0 image.
4. To specify additional applications for the AppStream 2.0 image, repeat steps 1 through 3 for each application as needed.
5. If applicable, use the Image Assistant `update-default-profile` CLI operation to overwrite the default Windows profile and create default application and Windows settings for your users.
6. Use the Image Assistant `create-image` CLI operation to create the image.
