# Amazon Elastic File System sample for AWS CodeBuild

You might want to create your AWS CodeBuild builds on Amazon Elastic File System, a scalable, shared file
service for Amazon EC2 instances. The storage capacity with Amazon EFS is elastic, so it grows or
shrinks as files are added and removed. It has a simple web services interface that you can
use to create and configure file systems. It also manages all of the file storage
infrastructure for you, so you do not need to worry about deploying, patching, or
maintaining file system configurations. For more information, see [What is Amazon Elastic File System?](../../../efs/latest/ug/whatisefs.md "../../../efs/latest/ug/whatisefs.md") in the _Amazon Elastic File System User Guide_.

This sample shows you how to configure a CodeBuild project so that it mounts and then builds
a Java application to an Amazon EFS file system. Before you begin, you must have a Java
application ready to build that is uploaded to an S3 input bucket or an AWS CodeCommit, GitHub,
GitHub Enterprise Server, or Bitbucket repository.

Data in transit for your file system is encrypted. To encrypt data in transit using a
different image, see [Encrypting data in transit](../../../efs/latest/ug/encryption-in-transit.md "../../../efs/latest/ug/encryption-in-transit.md").

###### Topics

- [Use AWS CodeBuild with Amazon Elastic File System](#sample-efs-high-level-steps "#sample-efs-high-level-steps")
- [Troubleshoot the Amazon EFS integration](sample-efs-troubleshooting.md "sample-efs-troubleshooting.md")

## Use AWS CodeBuild with Amazon Elastic File System

The sample covers the four high-level steps required to use Amazon EFS with AWS CodeBuild. They
are:

1. Create a virtual private cloud (VPC) in your AWS account.
2. Create a file system that uses this VPC.
3. Create and build a CodeBuild project that uses the VPC. The CodeBuild project uses the
   following to identify the file system:
   - A unique file system identifier. You choose the identifier when you
     specify the file system in your build project.
   - The file system ID. The ID is displayed when you view your file system
     in the Amazon EFS console.
   - A mount point. This is a directory in your Docker container that
     mounts the file system.
   - Mount options. These include details about how to mount the file
     system.

4. Review the build project to ensure that the correct project files and
   variables were generated.

###### Note

A file system created in Amazon EFS is supported on Linux platforms only.

###### Topics

- [Step 1: Create a VPC using AWS CloudFormation](#sample-efs-create-vpc "#sample-efs-create-vpc")
- [Step 2: Create an Amazon Elastic File System file system with
  your VPC](#sample-efs-create-efs "#sample-efs-create-efs")
- [Step 3: Create a CodeBuild project to use with
  Amazon EFS](#sample-efs-create-acb "#sample-efs-create-acb")
- [Step 4: Review the build project](#sample-efs-summary "#sample-efs-summary")

### Step 1: Create a VPC using AWS CloudFormation

Create your VPC with an AWS CloudFormation template.

1. Follow the instructions in [AWS CloudFormation VPC template](cloudformation-vpc-template.md "cloudformation-vpc-template.md") to use AWS CloudFormation to create a
   VPC.

###### Note

The VPC created by this AWS CloudFormation template has two private subnets and
two public subnets. You must only use private subnets when you use
AWS CodeBuild to mount the file system you created in Amazon EFS. If you use one
of the public subnets, the build fails. 2. Sign in to the AWS Management Console and open the Amazon VPC console at
[https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/"). 3. Choose the VPC you created with AWS CloudFormation. 4. On the **Description** tab, make a note of the name of
your VPC and its ID. Both are required when you create your AWS CodeBuild
project later in this sample.

### Step 2: Create an Amazon Elastic File System file system with

your VPC

Create a simple Amazon EFS file system for this sample using the VPC you created
earlier.

1. Sign in to the AWS Management Console and open the Amazon EFS console at
   [https://console.aws.amazon.com/efs/](https://console.aws.amazon.com/efs/ "https://console.aws.amazon.com/efs/").
2. Choose **Create file system**.
3. From **VPC**, choose the VPC name you noted earlier in
   this sample.
4. Leave the Availability Zones associated with your subnets selected.
5. Choose **Next Step**.
6. In **Add tags**, for the default
   **Name** key, in **Value**, enter the
   name of your Amazon EFS file system.
7. Keep **Bursting** and **General
   Purpose** selected as your default performance and throughput
   modes, and then choose **Next Step**.
8. For **Configure client access**, choose **Next
   Step**.
9. Choose **Create File System**.
10. (Optional) We recommend adding a policy to your Amazon EFS file system that
    enforces encryption of data in transit. In the Amazon EFS console, choose
    **File system policy**, choose
    **Edit**, select the box labeled **Enforce
    in-transit encryption for all clients**, and then choose
    **Save**.

### Step 3: Create a CodeBuild project to use with

Amazon EFS

Create a AWS CodeBuild project that uses the VPC you created earlier in this sample.
When the build is run, it mounts the Amazon EFS file system created earlier. Next, it
stores the .jar file created by your Java application in your file system's mount
point directory.

1. Open the AWS CodeBuild console at [https://console.aws.amazon.com/codesuite/codebuild/home](https://console.aws.amazon.com/codesuite/codebuild/home "https://console.aws.amazon.com/codesuite/codebuild/home").
2. From the navigation pane, choose **Build projects**, and
   then choose **Create build project**.
3. In **Project name**, enter a name for your project.
4. From **Source provider**, choose the repository that
   contains the Java application you want to build.
5. Enter information, such as a repository URL, that CodeBuild uses to locate
   your application. The options are different for each source provider. For
   more information, see [Choose source provider](create-project.md#create-project-source-provider "create-project.md#create-project-source-provider").
6. From **Environment image**, choose **Managed
   image**.
7. From **Operating system**, choose **Amazon Linux
   2**.
8. From **Runtime(s)**, choose
   **Standard**.
9. From **Image**, choose
   **aws/codebuild/amazonlinux-x86_64-standard:4.0**.
10. From **Environment type**, choose
    **Linux**.
11. Under **Service role**, choose **New service
    role**. In **Role name**, enter a name for the
    role CodeBuild creates for you.
12. Expand **Additional configuration**.
13. Select **Enable this flag if you want to build Docker images or
    want your builds to get elevated privileges**.

###### Note

By default, Docker daemon is enabled for non-VPC builds. If you would like to use Docker
containers for VPC builds, see [Runtime
Privilege and Linux Capabilities](https://docs.docker.com/engine/reference/run/#runtime-privilege-and-linux-capabilities "https://docs.docker.com/engine/reference/run/#runtime-privilege-and-linux-capabilities") on the Docker Docs website and enable privileged mode. Also, Windows does not support privileged mode. 14. From **VPC**, choose the VPC ID. 15. From **Subnets**, choose one or more of the private
subnets associated with your VPC. You must use private subnets in a build
that mounts an Amazon EFS file system. If you use a public subnet, the build
fails. 16. From **Security Groups**, choose the default security
group. 17. In **File systems**, enter the following
information:

    * For **Identifier**, enter a unique file system identifier. It must
     be fewer than 129 characters and contain only alphanumeric characters and underscores.
     CodeBuild uses this identifier to create an environment variable that identifies the elastic
     file system. The environment variable format is `CODEBUILD_`<file_system_identifier>`` in capital letters. For example, if you
     enter `my_efs`, the environment variable is `CODEBUILD_MY_EFS`.
    * For **ID**, choose the file system ID.
    * (Optional) Enter a directory in the file system. CodeBuild mounts this
     directory. If you leave **Directory path** blank, CodeBuild
     mounts the entire file system. The path is relative to the root of the
     file system.
    * For **Mount point**, enter the absolute path of the
     directory in your build container where the file system is mounted. If
     this directory does not exist, CodeBuild creates it during the build.
    * (Optional) Enter mount options. If you leave **Mount options** blank,
     CodeBuild uses its default mount options:



    ```
    nfsvers=4.1
    rsize=1048576
    wsize=1048576
    hard
    timeo=600
    retrans=2
    ```

    For more information, see [Recommended NFS Mount
     Options](../../../efs/latest/ug/mounting-fs-nfs-mount-settings.md "../../../efs/latest/ug/mounting-fs-nfs-mount-settings.md") in the *Amazon Elastic File System User Guide*.

18. For **Build specification**, choose **Insert
    build commands**, and then choose **Switch to
    editor**.
19. Enter the following build spec commands into the editor. Replace
    `<file_system_identifier>`
    with the identifier you entered in step 17. Use capital letters (for
    example, `CODEBUILD_MY_EFS`).

```
version: 0.2
phases:
  install:
    runtime-versions:
      java: corretto11
  build:
    commands:
      - mvn compile -Dgpg.skip=true -Dmaven.repo.local=$CODEBUILD_`<file_system_identifier>`
```

20. Use the default values for all other settings, and then choose
    **Create build project**. When your build is complete,
    the console page for your project is displayed.
21. Choose **Start build**.

### Step 4: Review the build project

After your AWS CodeBuild project is built:

- You have a .jar file created by your Java application that is built to
  your Amazon EFS file system under your mount point directory.
- An environment variable that identifies your file system is created using
  the file system identifier you entered when you created the project.

For more information, see [Mounting file
systems](../../../efs/latest/ug/mounting-fs.md "../../../efs/latest/ug/mounting-fs.md") in the _Amazon Elastic File System User Guide_.
