# Upload Files to Amazon SageMaker Studio Classic

###### Important

As of November 30, 2023, the previous Amazon SageMaker Studio experience is now named
Amazon SageMaker Studio Classic. The following section is specific to using the Studio Classic application. For
information about using the updated Studio experience, see [Amazon SageMaker Studio](studio-updated.md "studio-updated.md").

Studio Classic is still maintained for existing
workloads but is no longer available for onboarding. You can only stop or delete existing Studio Classic
applications and cannot create new ones. We recommend that you [migrate your workload to the new Studio experience](studio-updated-migrate.md "studio-updated-migrate.md").

When you onboard to Amazon SageMaker Studio Classic, a home directory is created for you in the
Amazon Elastic File System (Amazon EFS) volume that was created for your team. Studio Classic can only open files that
have been uploaded to your directory. The Studio Classic file browser maps to your home
directory.

###### Note

Studio Classic does not support uploading folders. While you can only upload individual
files, you can upload multiple files at the same time.

###### To upload files to your home directory

1. In the left sidebar, choose the **File Browser** icon (
   ![Black square icon representing a placeholder or empty image.](images/studio/icons/folder.png)
   ).
2. In the file browser, choose the **Upload Files** icon (
   ![Black square icon representing a placeholder or empty image.](images/icons/File_upload_squid.png)
   ).
3. Select the files you want to upload and then choose **Open**.
4. Double-click a file to open the file in a new tab in Studio Classic.
