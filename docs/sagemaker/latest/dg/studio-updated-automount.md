

# Amazon EFS creation and auto-mounting in Studio
<a name="studio-updated-automount"></a>

Amazon SageMaker AI supports creating an Amazon EFS volume for a domain and automatically mounting a home directory folder for each user. Using this folder, users can share data between their own private spaces. However, users cannot share data with other users in the domain. Users only have access to their own folder.

**Important**  
For domains created after June 1, 2026, EFS is not created by default during domain creation (for quick setup). You must enable EFS creation before auto-mounting can be enabled.

 **EFS creation and auto-mount settings** 

EFS in Amazon SageMaker Studio involves two settings that work together:
+ `HomeEFSCreation` – Controls whether an EFS file system is created and managed by SageMaker AI for the domain.

  Default for new domains created through quick setup: **Disabled**

  When enabled: Creates a new EFS file system managed by SageMaker AI for this domain.
+ `AutoMountHomeEFS` – Controls whether EFS storage is automatically mounted for users.

  Default: **Enabled** (when `HomeEFSCreation` is enabled)

  Description: Auto-mounts a home directory for each user to share notebooks, data, and code across their private spaces.

  This setting is only editable when `HomeEFSCreation` is enabled.

  At the user profile level, this value defaults to **DefaultAsDomain** (inherits the domain-level setting).

Key behaviors:
+ If no value is set for `AutoMountHomeEFS`, auto-mount EFS is enabled by default.
+ If you have an existing space, restart the space to mount EFS.
+ Auto-mount EFS is available for private spaces only.

 **Enable EFS creation and auto-mount** 

After domain creation (quick setup):

1. Open the SageMaker AI console.

1. On the left navigation pane, under **Admin configurations**, choose **Domains**.

1. Select your domain, then choose the **Domain settings** tab.

1. In the **Storage configurations** section, choose **Edit**.

1. Under **EFS storage and encryption**, toggle `HomeEFSCreation` to ON. This creates a new EFS file system managed by SageMaker AI for this domain.

1. Ensure `AutoMountHomeEFS` is toggled ON (enabled by default when `HomeEFSCreation` is on). This auto-mounts a home directory for each user to share notebooks, data, and code across their private spaces.

1. Choose **Submit**.

1. If you have existing spaces, restart them to access EFS data.

For custom setup, EFS creation and auto-mounting are enabled by default.

 The user’s folder can be accessed through a folder named `user-default-efs` . This folder is present in the `$HOME` directory of the Studio application.

 For information about opting out of Amazon EFS auto-mounting, see [Opt out of Amazon EFS auto-mounting](studio-updated-automount-optout.md). 

 Amazon EFS auto-mounting also facilitates the migration of data from Studio Classic to Studio. For more information, see [(Optional) Migrate data from Studio Classic to Studio](studio-updated-migrate-data.md). 

 **Access point information** 

 When auto-mounting is activated, SageMaker AI uses an Amazon EFS access point to facilitate access to the data in the Amazon EFS volume. For more information about access points, see [Working with Amazon EFS access points](https://docs.aws.amazon.com/efs/latest/ug/efs-access-points.html) SageMaker AI creates a unique access point for each user profile in the domain during user profile creation or during application creation for an existing user profile. The POSIX user value of the access point matches the `HomeEfsFileSystemUid` value of the user profile that SageMaker AI creates the access point for. To get the value of the user, see [DescribeUserProfile](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeUserProfile.html#sagemaker-DescribeUserProfile-response-HomeEfsFileSystemUid). The root directory path is also set to the same value as the POSIX user value.  

 SageMaker AI sets the permissions of the new directory to the following values: 

 
+  Owner user ID: `{{POSIX user value}}` 
+  Owner group ID: `0` 
+  Permissions `700` 

 The access point is required to access the Amazon EFS volume. As a result, you cannot delete or update the access point without losing access to the Amazon EFS volume. 

 **Error resolution** 

 If SageMaker AI encounters an issue when auto-mounting the Amazon EFS user folder during application creation, the application is still created. However, in this case, SageMaker AI creates a file named `error.txt` instead of mounting the Amazon EFS folder. This file describes the error encountered, as well as steps to resolve it. SageMaker AI creates the `error.txt` file in the `user-default-efs` folder located in the `$HOME` directory of the application. 