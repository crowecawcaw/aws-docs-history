# Changing the metadata configuration mode

For SSD-based file systems, you can change the metadata configuration mode of an existing file system using the
AWS console and CLI, as explained in the following procedures.

When switching from Automatic mode to User-provisioned mode, you must provide a Metadata IOPS
value greater than or equal to the current file system Metadata IOPS value.

If you request to switch from User-provisioned to Automatic mode and the
current Metadata IOPS value is greater than the automated default, Amazon FSx rejects the request,
because downscaling Metadata IOPS is not supported. To unblock mode switch, you must increase
storage capacity to match your current Metadata IOPS in Automatic mode in order to enable
mode switch again.

You can change a file system's metadata configuration mode by using the Amazon FSx console,
the AWS CLI, or the Amazon FSx API.

1. Open the Amazon FSx console at [https://console.aws.amazon.com/fsx/](https://console.aws.amazon.com/fsx/ "https://console.aws.amazon.com/fsx/").
2. In the left navigation pane, choose **File systems**.
   In the **File systems** list, choose the FSx for Lustre file system that you
   want to change the metadata configuration mode for.
3. For **Actions**, choose **Update Metadata IOPS**.
   Or, in the **Summary** panel, choose **Update** next to the file
   system's **Metadata IOPS** field.

The **Update Metadata IOPS** dialog box appears. 4. Do one of the following.

    * To switch from User-provisioned mode to Automatic mode,
     choose **Automatic**.
    * To switch from Automatic mode to User-provisioned mode,
     choose **User-provisioned**. Then, for
     **Desired Metadata IOPS**, provide a Metadata IOPS
     value greater than or equal to the current file system Metadata IOPS value.

5. Choose **Update**.
   To change the metadata configuration mode for an SSD FSx for Lustre file system,
   use the AWS CLI command [update-file-system](../../../cli/latest/reference/fsx/update-file-system.md "../../../cli/latest/reference/fsx/update-file-system.md") (UpdateFileSystem is the equivalent API action). Set the following parameters:

- Set `--file-system-id` to the ID of the file system that you are updating.
- To change the metadata configuration mode on SSD-based file systems, use the `--lustre-configuration
MetadataConfiguration` property. This property has two parameters, `Mode`
  and `Iops`.
  - To switch your SSD file system from AUTOMATIC mode to USER_PROVISIONED mode, set `Mode` to
    `USER_PROVISIONED` and `Iops` to a Metadata IOPS value
    greater than or equal to the current file system Metadata IOPS value. For example:

  ```
  `aws fsx update-file-system \
   --file-system-id `fs-0123456789abcdef0` \
   --lustre-configuration 'MetadataConfiguration={Mode=`USER_PROVISIONED`,Iops=`96000`}'`
  ```

  - To switch from USER_PROVISIONED mode to AUTOMATIC mode, set `Mode` to
    `AUTOMATIC` and do not use the `Iops` parameter. For example:

  ```
  `aws fsx update-file-system \
   --file-system-id `fs-0123456789abcdef0` \
   --lustre-configuration 'MetadataConfiguration={Mode=`AUTOMATIC`}'`
  ```
