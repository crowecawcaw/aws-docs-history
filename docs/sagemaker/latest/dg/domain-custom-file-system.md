# Adding a custom file system to a domain

When you create a domain, Amazon SageMaker AI adds a default Amazon Elastic File System
(Amazon EFS) volume to the domain. SageMaker AI creates this volume for you. You also have the option to
add a custom Amazon EFS or a custom Amazon FSx for Lustre file system that you've created. After you add
it, your file system is available to users who belong to your domain. Your users can access
the file system when they use Amazon SageMaker Studio. They can attach the file system to spaces that
they create for the following supported applications:

- JupyterLab
- Code Editor
  After running a space and starting the application, your users can access any data, code, or
  other artifacts that your file system contains.

You can enable your users to access your file system in the following ways:

- Through _shared spaces_ – A shared space can be
  created by any user who belongs to your domain. Then, it can used by any user who
  belongs to your domain.
- Through _private spaces_ – A private space can
  be created by any user who belongs to your domain. Then, it can be used by only that
  user.
- Exclusively as an individual user – If you don't want to enable all of your users
  to access the file system, you can enable only a specific user to access it. If you do that,
  the file system is available only in private spaces that the specific user creates.
  You can add a custom file system by using the Amazon SageMaker API, the AWS SDKs, or the AWS CLI.
  You can't add a custom file system by using the SageMaker AI console.

## Prerequisites

Before you can add a custom file system to a domain, you must meet the following
requirements:

- You have a domain in SageMaker AI. Before you can add a file system, you need the
  domain ID. You can look up the ID by using the SageMaker AI console. You can also run the
  [`list-domains`](../../../cli/latest/reference/sagemaker/list-domains.md "../../../cli/latest/reference/sagemaker/list-domains.md") command with the AWS CLI.
- You have an Amazon EFS or FSx for Lustre file system in your AWS account.

For Amazon EFS

    + For the steps to create an Amazon EFS, see [Create your Amazon EFS
     file system](../../../efs/latest/ug/gs-step-two-create-efs-resources.md "../../../efs/latest/ug/gs-step-two-create-efs-resources.md") in the *Amazon Elastic File System User Guide*.
    + Before Studio can access your file system, it must have a mount target
     in each of the subnets that you associate with the domain. For more
     information about assigning mount targets to subnets, see [Creating and
     managing mount targets and security groups](../../../efs/latest/ug/accessing-fs.md "../../../efs/latest/ug/accessing-fs.md") in the *Amazon Elastic File System User Guide*.
    + For each mount target, you must add the security group that Amazon SageMaker AI created
     in your AWS account when you created the domain. The security group name
     has the format
     `security-group-for-inbound-nfs-`domain-id``.
     For instructions on how to obtain your domain ID, see [View domains](domain-view.md "domain-view.md").
    + Your IAM permissions must allow you to use the
     `elasticfilesystem:DescribeMountTargets` action. For more
     information about this action, see [Actions, resources, and condition keys for Amazon Elastic File System](../../../service-authorization/latest/reference/list_amazonelasticfilesystem.md "../../../service-authorization/latest/reference/list_amazonelasticfilesystem.md") in the *Service Authorization Reference*.

For FSx for Lustre

    + For the steps to create a FSx for Lustre file system, see [Getting started with Amazon FSx for Lustre](../../../fsx/latest/LustreGuide/getting-started.md "../../../fsx/latest/LustreGuide/getting-started.md") in the *Amazon FSx for Lustre User Guide*. Ensure that the FSx for Lustre file system
     exists in:




    	- The same Amazon VPC as your domain.
    	- One of the subnets present in your domain.
    + Before Studio can access the FSx for Lustre file system, you must add your
     domain's security group to all of the elastic network interfaces (ENIs) in
     your FSx for Lustre file system. Without this step, the app creation fails with an
     error. Use the following instructions to add the domain security group to
     your FSx for Lustre file system ENIs.


    ###### Add your domain security group to FSx for Lustre file system ENIs
     (console)


    	1. Navigate to the [Amazon FSx
    	 console](https://console.aws.amazon.com/fsx "https://console.aws.amazon.com/fsx").
    	2. Choose **File systems**.
    	3. Choose your FSx for Lustre file system by using the corresponding link
    	 under **File system ID**.
    	4. If not selected already, choose the **Network &
    	 security** tab.
    	5. Under **Subnet** choose **To see all the ENIs,
    	 see the Amazon EC2 console**. This will take you to the Amazon EC2 console
    	 and shows all of the ENIs linked to your FSx for Lustre file system.
    	6. For each ENI:


    		1. Choose the ENI by choosing the corresponding link under
    		 **Network interface ID**.
    		2. Choose **Actions** at the top right of the summary
    		 page to expand a drop-down menu.
    		3. In the drop-down menu, choose **Choose security
    		 group**.
    		4. Search for your domain security group.


    		The security group name has the format
    		 `security-group-for-inbound-nfs-`domain-id``.
    		 For instructions on how to obtain your domain ID, see [View domains](domain-view.md "domain-view.md").
    		5. Choose **Add security group**.

## Adding a custom file system to a domain

with the AWS CLI

To add a custom file system to a domain or user profile with the AWS CLI, you pass a
`CustomFileSystemConfigs` definition when you use any of the following
commands:

- [`create-domain`](../../../cli/latest/reference/sagemaker/create-domain.md "../../../cli/latest/reference/sagemaker/create-domain.md")
- [`update-domain`](../../../cli/latest/reference/sagemaker/update-domain.md "../../../cli/latest/reference/sagemaker/update-domain.md")
- [`create-user-profile`](../../../cli/latest/reference/sagemaker/create-user-profile.md "../../../cli/latest/reference/sagemaker/create-user-profile.md")
- [`update-user-profile`](../../../cli/latest/reference/sagemaker/update-user-profile.md "../../../cli/latest/reference/sagemaker/update-user-profile.md")

The following examples show how to add a file system to an existing domain or user
profile.

###### To add a file system that is accessible in shared spaces

- Update the default space settings for your domain. The following example adds the
  file system settings to the default space settings:

```
aws sagemaker update-domain --domain-id `domain-id` \
--default-space-settings file://file-system-settings.json
```

This example passes the file system configuration as a JSON file, which is shown in a
later example.

###### To add a file system that is accessible in private spaces

- Update the default user settings for your domain. The following example adds the
  file system settings to the default user settings:

```
aws sagemaker update-domain --domain-id `domain-id` \
--default-user-settings file://file-system-settings.json
```

This example passes the file system configuration as a JSON file, which is shown in a
later example.

###### To add a file system that is accessible only to an individual user

- Update the user profile for the user. The following example adds the file system
  settings to a user profile:

```
aws sagemaker update-user-profile --domain-id `domain-id` \
--user-profile-name `user-profile-name` \
--user-settings file://file-system-settings.json
```

This example passes the file system configuration as a JSON file, which is shown in
the following example.

###### Example file system settings file

The file in the preceding examples, `file-system-settings.json`, has the
following settings:

For your FSx for Lustre file systems

```
{
    "CustomFileSystemConfigs":
    [
        {
            "FSxLustreFileSystemConfig":
            {
              "FileSystemId": "file-system-id",
              "FileSystemPath": "/"
            }
        }
    ]
}
```

This example configuration has the following keys:

`CustomFileSystemConfigs`

Settings for custom file systems (only Amazon EFS file systems are
supported).

`FSxLustreFileSystemConfig`

Settings for custom FSx for Lustre file systems.

`FileSystemId`

The ID of your Amazon EFS file system.

`FileSystemPath`

The path to the file system directory that is accessible to the domain
users in their spaces in Studio. Permitted users can access only this
directory and below. The default path is the file system root:
`/`.

For your Amazon EFS file systems

```
{
    "CustomFileSystemConfigs":
    [
        {
            "EFSFileSystemConfig":
            {
                "FileSystemId": "`file-system-id`",
                "FileSystemPath": "`/`"
            }
        }
    ]
}
```

This example configuration has the following keys:

`CustomFileSystemConfigs`

Settings for custom file systems (only Amazon EFS file systems are
supported).

`EFSFileSystemConfig`

Settings for custom Amazon EFS file systems.

`FileSystemId`

The ID of your Amazon EFS file system.

`FileSystemPath`

The path to the file system directory that is accessible to the domain
users in their spaces in Studio. Permitted users can access only this
directory and below. The default path is the file system root:
`/`.

When you assign a file system to the default space settings for a domain, you must
also include the execution role in the settings:

```
{
    "ExecutionRole": "`execution-role-arn`"
}
```

This example configuration has the following key:

`ExecutionRole`

The default execution role for the users of the domain.

If you want to apply POSIX permissions for your file system, you can also pass the
following settings to the `create-domain` or `create-user-profile`
commands:

```
{
    "CustomPosixUserConfig":
    {
        "Uid": `UID`,
        "Gid": `GID`
    }
}
```

This example configuration has the following keys:

`CustomPosixUserConfig`

The default POSIX identities that are used for file system operations. You can use
these settings to apply your existing POSIX permission structure to the user profiles
that access the custom file system. At a POSIX permissions level, you can control
which users can access the file system and which files or data they can access.

You can also apply `CustomPosixUserConfig` settings when you create a
user profile by using the `create-user-profile` command. The settings that
you apply to a user profile override those that you apply to the associated
domain.

###### Note

You can apply `CustomPosixUserConfig` settings when you use the
`create-domain` and `create-user-profile` commands. However,
you can't apply these settings when you do the following:

- Use the `update-domain` command for a domain that is already
  associated with any user profiles. You can apply these settings only to
  domains that have no user profiles.
- Use the `update-user-profile` command. To apply these settings to
  profile that you've already created, delete the profile, and create a new one
  that has the updated settings.

`Uid`

The POSIX user ID. The default is 200001.

`Gid`

The POSIX group ID. The default is 1001.

## Attaching a custom file system to a space with the

AWS CLI

After you add a custom file system to a domain, the domain users can attach the
file system to spaces that they create. For instance, they can attach the file system when
they use Studio or the [create-space](../../../cli/latest/reference/sagemaker/create-space.md "../../../cli/latest/reference/sagemaker/create-space.md") command with the
AWS CLI.

###### To attach a custom file system to a space

- Add the file system configuration to the space settings. The following example command
  attaches a file system to a new space.

```
aws sagemaker create-space \
--space-name `space-name` \
--domain-id `domain-id` \
--ownership-settings "OwnerUserProfileName=`user-profile-name`" \
--space-sharing-settings "SharingType=Private" \
--space-settings file://space-settings.json

```

In this example, the file `space-settings.json` has the following settings,
which include the `CustomFileSystems` configuration with the
`FileSystemId` key.

For your FSx for Lustre file systems

```
{
    "AppType": "JupyterLab",
    "JupyterLabAppSettings":
    {
        "DefaultResourceSpec":
        {
          "InstanceType": "instance-type"
        }
    },
    "CustomFileSystems":
    [
        {
            "FSxLustreFileSystem":
            {
              "FileSystemId": "file-system-id"
            }
        }
    ]
}
```

For your Amazon EFS file systems

```
{
    "AppType": "JupyterLab",
    "JupyterLabAppSettings":
    {
        "DefaultResourceSpec":
        {
            "InstanceType": "`instance-type`"
        }
    },
    "CustomFileSystems":
    [
        {
            "EFSFileSystem":
            {
                "FileSystemId": "`file-system-id`"
            }
        }
    ]
}
```

SageMaker AI creates a symbolic link at the following path:
`/home/sagemaker-user/custom-file-systems/`file-system-type`/`file-system-id``.
 With this, the domain users can navigate to the custom file system from within their
 home directory, `/home/sagemaker-user`.
