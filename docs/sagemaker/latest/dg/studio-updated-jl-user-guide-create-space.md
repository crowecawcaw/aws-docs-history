# Create a space

To get started using JupyterLab, create a space or choose the space that your
administrator created for you and open JupyterLab.

Use the following procedure to create a space and open JupyterLab.

###### To create a space and open JupyterLab

1. Open Studio. For information about opening Studio, see [Launch Amazon SageMaker Studio](studio-updated-launch.md "studio-updated-launch.md").
2. Choose **JupyterLab**.
3. Choose **Create JupyterLab space**.
4. For **Name**, specify the name of the space.
5. (Optional) Select **Share with my domain** to create a shared space.
6. Choose **Create space**.
7. (Optional) For **Instance**, specify the Amazon EC2 instance that runs
   the space.
8. (Optional) For **Image**, specify an image that your
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
images while creating those resources. 9. (Optional) For **Space Settings**, specify the following:

    * **Storage (GB)** – Up to 100 GB or the amount that
     your administrator specifies.
    * **Lifecycle Configuration** – A lifecycle
     configuration that your administrator specifies.
    * **Attach custom EFS filesystem** – An Amazon EFS to
     which your administrator provides access.

10. Choose **Run space**.
11. Choose **Open JupyterLab**.
