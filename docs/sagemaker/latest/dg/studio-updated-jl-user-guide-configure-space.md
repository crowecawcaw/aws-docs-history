# Configure a space

After you create a JupyterLab space, you can configure it to do the following:

- Change the instance type.
- Change the storage volume.
- (Admin set up required) Use a custom image.
- (Admin set up required) Use a lifecycle configuration.
- (Admin set up required) Attach a custom Amazon EFS.

###### Important

You must stop the JupyterLab space every time you configure it. Use the following
procedure to configure the space.

###### To configure a space

1. Within Studio,
   navigate
   to the JupyterLab application page.
2. Choose the name of the space.
3. (Optional) For **Image**, specify an image that your
   administrator provided to customize your environment.

###### Important

Custom IAM policies that allow Studio users to create spaces must also
grant permissions to list images (`sagemaker: ListImage`) to view
custom images. To add the permission, see
[Add or remove identity permissions](../../../IAM/latest/UserGuide/access_policies_manage-attach-detach.md "../../../IAM/latest/UserGuide/access_policies_manage-attach-detach.md")
in the _AWS Identity and Access Management_ User
Guide.

[AWS managed policies for Amazon SageMaker AI](security-iam-awsmanpol.md "security-iam-awsmanpol.md")
that give permissions to create SageMaker AI resources already include permissions to list
images while creating those resources. 4. (Optional) For **Space Settings**, specify the
following:

    * **Storage (GB)** – Up to 100 GB or the amount
     that your administrator configured for the space.
    * **Lifecycle Configuration** – A lifecycle
     configuration that your administrator provides.
    * **Attach custom EFS filesystem** – An Amazon EFS to
     which your administrator provides access.

5. Choose **Run space**.
   When you open the JupyterLab application, your space has the updated
   configuration.
