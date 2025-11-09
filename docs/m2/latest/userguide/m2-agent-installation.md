AWS Mainframe Modernization Service (Managed Runtime Environment experience) is no longer open to new customers. For
capabilities similar to AWS Mainframe Modernization Service (Managed Runtime Environment experience) explore AWS Mainframe Modernization Service (Self-Managed
Experience). Existing customers can continue to use the service as normal. For more information, see [AWS Mainframe Modernization
availability change](mainframe-modernization-availability-change.md "mainframe-modernization-availability-change.md").

# Install a File Transfer agent

You can use this document as a step-by-step guide to install an agent on the source
mainframe.

###### Note

This guide is only for the mainframe system programmers.

###### Topics

- [Step 1: Create a zFS data set for the M2-agent](#allocate-dataset "#allocate-dataset")
- [Step 2: Format the data set as zFS](#format-dataset "#format-dataset")
- [Step 3: Mount the filesystem](#mount-filesystem "#mount-filesystem")
- [Step 4: Verify the mount](#verify-mount "#verify-mount")
- [Step 5: Enter OMVS](#enter-omvs "#enter-omvs")
- [Step 6: Set the agent installation directory environment
  variable](#agent-directory "#agent-directory")
- [Step 7: Set the work directory environment variable](#work-directory "#work-directory")
- [Step 8: Create the work directory](#create-work-directory "#create-work-directory")
- [Step 9: Copy the agent tar file and copy the work
  directory](#agent-tar-package "#agent-tar-package")
- [Step 10: Finish the agent installation](#finish-agent-installation "#finish-agent-installation")

## Step 1: Create a zFS data set for the M2-agent

Create a zFS for the M2-agent installation using the JCL (Job Control Language)
below:

```
DEFINE   EXEC   PGM=IDCAMS
SYSPRINT DD     SYSOUT=A
SYSIN    DD     *
 DEFINE CLUSTER (NAME(yourhlq.M2AGENT.ZFS) -
 VOLUMES(*) -
 LINEAR CYL(1000 200))
```

## Step 2: Format the data set as zFS

After creating the data set, format it as a zFS filesystem.

One way to do that is using the following JCL:

```
FORMAT  EXEC PGM=IOEAGFMT,
PARM=('-aggregate yourhlq.M2AGENT.ZFS -size 1200') ,
SYSPRINT DD  SYSOUT=*
```

Submit this job and check if it completed successfully.

## Step 3: Mount the filesystem

To mount the filesystem, use the `MOUNT` command. You can mount the filesystem in
command line in ISPF or in batch.

For example:

```
MOUNT FILESYSTEM('yourhlq.M2AGENT.ZFS') TYPE(ZFS) MODE(RDWR) MOUNTPOINT('/usr/lpp/aws/m2-agent')
```

You will use this mount point in step 6.

###### Note

Defining the mount path is optional and you should use an existing directory for
this.

## Step 4: Verify the mount

Verify that the filesystem is correctly mounted using `D OMVS,F` command or by
checking within Unix System Service (USS).

## Step 5: Enter OMVS

Use the following command to enter OMVS:

```
TSO OMVS
```

## Step 6: Set the agent installation directory environment

variable

Use the following command to set the agent installation directory environment:

```
export AGENT_DIR=/usr/lpp/aws/m2-agent
```

###### Note

Mount point is defined in step 3.

## Step 7: Set the work directory environment variable

Use the following command to set the work directory environment variable:

```
export WORK_DIR=$AGENT_DIR/tmp
```

## Step 8: Create the work directory

Use the following command to set the work directory environment:

```
mkdir -p $WORK_DIR
```

## Step 9: Copy the agent tar file and copy the work

directory

Download the agent tar file from AWS using the [M2 agent
link](https://drm0z31ua8gi7.cloudfront.net/filetransfer/m2-agent-v1.0.0.tar "https://drm0z31ua8gi7.cloudfront.net/filetransfer/m2-agent-v1.0.0.tar").

The transfer mechanism will depend on your environment, but make sure that the tar file is
transferred in binary mode.

## Step 10: Finish the agent installation

Follow these steps to finish the agent installation.

1. Set the m2-agent version environment variable to the version currently being installed
   using the following command:

```
export M2_AGENT_VERSION=1.0.0
```

2. Extract the agent tar package using the following command:

```
tar -xpf m2-agent-$M2_AGENT_VERSION.tar -C $AGENT_DIR
```

3. Create a `current-version` symbolic link to the current agent installation
   directory with the following command:

```
ln -s $AGENT_DIR/m2-agent-v$M2_AGENT_VERSION $AGENT_DIR/current-version
```

4. Update and submit `CPY#PDS` to create the File Transfer agent data sets.

###### Note

JCL uses the `SYS2.AWS.M2 HLQ`.

To create the File Transfer agent, update the three symbolic variables HLQ (High level qualifier),
`VOLSER`, and `AGNTPATH` to be used later in the JCL:

```
oedit $AGENT_DIR/current-version/installation/CPY#PDS

```

###### Note

This JCL is tailored for setting up certain aspects of the agent installation on the
mainframe. It allocates necessary data sets and then copies specific files from the Unix
filesystem to these data sets.
