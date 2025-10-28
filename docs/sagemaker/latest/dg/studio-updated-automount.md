# Amazon EFS auto-mounting in Studio

Amazon SageMaker AI supports automatically mounting a folder in an Amazon EFS volume for each user in a
domain. Using this folder, users can share data between their own private spaces. However, users
cannot share data with other users in the domain. Users only have access to their own folder.

The user’s folder can be accessed through a folder named `user-default-efs` .
This folder is present in the `$HOME` directory of the Studio
application.

For information about opting out of Amazon EFS auto-mounting, see [Opt out of Amazon EFS auto-mounting](studio-updated-automount-optout.md "studio-updated-automount-optout.md").

Amazon EFS auto-mounting also facilitates the migration of data from Studio Classic to Studio.
For more information, see [(Optional) Migrate data from
Studio Classic to Studio](studio-updated-migrate-data.md "studio-updated-migrate-data.md").

**Access point information**

When auto-mounting is activated, SageMaker AI uses an Amazon EFS access point to facilitate access to
the data in the Amazon EFS volume. For more information about access points, see [Working with Amazon EFS access points](../../../efs/latest/ug/efs-access-points.md "../../../efs/latest/ug/efs-access-points.md") SageMaker AI creates a unique access point for each user profile in
the domain during user profile creation or during application creation for an existing user
profile. The POSIX user value of the access point matches the `HomeEfsFileSystemUid`
value of the user profile that SageMaker AI creates the access point for. To get the value of the user,
see [DescribeUserProfile](../APIReference/API_DescribeUserProfile.md#sagemaker-DescribeUserProfile-response-HomeEfsFileSystemUid "../APIReference/API_DescribeUserProfile.md#sagemaker-DescribeUserProfile-response-HomeEfsFileSystemUid"). The root directory path is also set to the same value as
the POSIX user value. 

SageMaker AI sets the permissions of the new directory to the following values:

- Owner user ID: `POSIX user value`
- Owner group ID: `0`
- Permissions `700`
  The access point is required to access the Amazon EFS volume. As a result, you cannot delete or
  update the access point without losing access to the Amazon EFS volume.

**Error resolution**

If SageMaker AI encounters an issue when auto-mounting the Amazon EFS user folder during application
creation, the application is still created. However, in this case, SageMaker AI creates a file
named `error.txt` instead of mounting the Amazon EFS folder. This file describes the
error encountered, as well as steps to resolve it. SageMaker AI creates the `error.txt` file
in the `user-default-efs` folder located in the `$HOME` directory of the
application.
