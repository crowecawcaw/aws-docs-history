# Delete an Amazon SageMaker AI domain

This page explains how to delete a domain and the requirements needed. A
domain consists of a list of authorized users, configuration settings, and an
Amazon Elastic File System (Amazon EFS) volume. The Amazon EFS volume contains data for the users, including
notebooks, resources, and artifacts. A user can have multiple applications (apps) which
support the reading and execution experience of the user’s notebooks, terminals, and
consoles. You can delete your domain using one of the following:

- AWS console
- AWS Command Line Interface (AWS CLI)
- SageMaker SDK

## Requirements

You must satisfy the following requirements to delete a domain.

- You must have admin permission to delete a domain.
- You can only delete an app with the status `InService`
  displayed as **Ready** in the domain. To delete the
  containing domain, you don't need to delete an app whose status is
  `Failed`. In the domain, an attempt to delete an app in
  the failed state results in an error.
- To delete a domain, the domain cannot contain any user profiles or
  shared spaces. To delete a user profile or shared space, the user profile or space
  cannot contain any non-failed apps.

When you delete these resources, the following occurs:

    + App – The data (files and notebooks) in a user's home
     directory is saved. Unsaved notebook data is lost.
    + User profile – The user can no longer sign in to the
     domain. The user loses access to their home directory, but the
     data is not deleted. An admin can retrieve the data from the Amazon EFS
     volume where it is stored under the user's AWS account.

- To switch authentication modes from IAM to
  IAM Identity Center, you must delete the domain.

## EFS files

Your files are kept in an Amazon EFS volume as a backup. This backup includes the files
in the mounted directory, which is `/home/sagemaker-user` for
Amazon SageMaker Studio Classic and `/root` for kernels.

When you delete files from these mounted directories, the kernel or app may move
the deleted files into a hidden trash folder. If the trash folder is inside the
mounted directory, those files are copied into the Amazon EFS volume and will incur
charges. To avoid these Amazon EFS charges, you must identify and clean the trash folder
location. The trash folder location for default apps and kernels is
`~/.local/`. This may vary depending on the Linux distribution used
for custom apps or kernels. For more information about the Amazon EFS volume, see [Manage Your Amazon EFS Storage Volume in Amazon SageMaker Studio Classic](studio-tasks-manage-storage.md "studio-tasks-manage-storage.md").

When you use the SageMaker AI console to delete the domain, the Amazon EFS volume is
detached but not deleted. The same behavior occurs by default when you use the AWS CLI
or the SageMaker Python SDK to delete the domain. However, when you use the AWS CLI or
the SageMaker Python SDK, you can set the `RetentionPolicy` to
`HomeEfsFileSystem=Delete`. This deletes the Amazon EFS volume along with
the domain.

## Delete an Amazon SageMaker AI domain

(console)

###### Important

When a user, space, or domain is deleted, the Amazon EFS volume that contains the
corresponding data will be lost. This includes notebooks and other
artifacts.

###### To delete a domain

1. Open the [SageMaker AI
   console](https://console.aws.amazon.com/sagemaker/ "https://console.aws.amazon.com/sagemaker/").
2. On the left navigation pane, choose **Admin
   configurations** to expand the options, if not already
   expanded.
3. Under **Admin configurations**, choose
   **Domains**.
4. Select the domain name link that you want to delete.
5. Choose the **User profiles** tab.
6. Repeat the following steps for each user in the **User
   profiles** list.
   1. Choose the user name link.
   2. If not already selected, choose the **User
      Details** tab
   3. Find any apps and spaces and choose **Delete**
      under the corresponding **Action** column.
   4. Follow the delete instructions.
   5. Once all of the app and spaces have **Status** as
      **Deleted**, choose **Delete**
      at the top right of the page.
   6. Follow the delete instructions.

7. When all users are deleted, choose the **Space
   management** tab.
8. Repeat the following steps for each space in the
   **Spaces** list.
   1. Select the bubble corresponding to the space.
   2. Choose **Delete**.
   3. Follow the delete instructions.

9. When all users and spaces are deleted, choose the **Domain
   settings** tab.
10. Find the **Delete domain** section.
11. Choose **Delete domain**. If this button is not
    available, you must repeat the previous steps to delete all spaces and
    users.
12. Follow the delete instructions.

## Delete an Amazon SageMaker AI domain

(AWS CLI)

###### To delete a domain

1. Retrieve the list of domains in your account.

```
aws --region `Region` sagemaker list-domains
```

2. Retrieve the list of applications for the domain to be deleted.

```
aws --region `Region` sagemaker list-apps \
    --domain-id-equals `DomainId`
```

3. Delete each application in the list.

```
aws --region `Region` sagemaker delete-app \
    --domain-id `DomainId` \
    --app-name `AppName` \
    --app-type `AppType` \
    --user-profile-name `UserProfileName`
```

4. Retrieve the list of user profiles in the domain.

```
aws --region `Region` sagemaker list-user-profiles \
    --domain-id-equals `DomainId`
```

5. Delete each user profile in the list.

```
aws --region `Region` sagemaker delete-user-profile \
    --domain-id `DomainId` \
    --user-profile-name `UserProfileName`
```

6. Retrieve the list of shared spaces in the domain.

```
aws --region `Region` sagemaker list-spaces \
    --domain-id `DomainId`
```

7. Delete each shared space in the list.

```
aws --region `Region` sagemaker delete-space \
    --domain-id `DomainId` \
    --space-name `SpaceName`
```

8. Delete the domain. To also delete the Amazon EFS volume, specify
   `HomeEfsFileSystem=Delete`.

```
aws --region `Region` sagemaker delete-domain \
    --domain-id `DomainId` \
    --retention-policy HomeEfsFileSystem=`Retain`
```
