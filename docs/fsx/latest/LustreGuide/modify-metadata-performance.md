

# Increasing metadata performance
<a name="modify-metadata-performance"></a>

You can increase a file system's metadata performance by using the Amazon FSx console, the AWS CLI, or the Amazon FSx API.

## To increase metadata performance for a file system (console)
<a name="modify-metadata-console-ssd"></a>

1. Open the Amazon FSx console at [https://console.aws.amazon.com/fsx/](https://console.aws.amazon.com/fsx/).

1. In the left navigation pane, choose **File systems**. In the **File systems** list, choose the FSx for Lustre file system that you want to increase metadata performance for.

1. For **Actions**, choose **Update Metadata IOPS**. Or, in the **Summary** panel, choose **Update** next to the file system's **Metadata IOPS** field.

   The **Update Metadata IOPS** dialog box appears.

1. Choose **User-provisioned**.

1. For **Desired Metadata IOPS**, choose the new Metadata IOPS value. The value you enter must be greater than or equal to the current Metadata IOPS value.
   + For SSD file systems, valid values are `1500`, `3000`, `6000`, `12000`, and multiples of `12000` up to a maximum of `192000`.
   + For Intelligent-Tiering file systems, valid values are `6000` and `12000`.

1. Choose **Update**.

## To increase metadata performance for a file system (CLI)
<a name="modify-metadata-cli-ssd"></a>

To increase the metadata performance for an FSx for Lustre file system, use the AWS CLI command [update-file-system](https://docs.aws.amazon.com/cli/latest/reference/fsx/update-file-system.html) (UpdateFileSystem is the equivalent API action). Set the following parameters:
+ Set `--file-system-id` to the ID of the file system that you are updating.
+ To increase your metadata performance, use the `--lustre-configuration MetadataConfiguration` property. This property has two parameters, `Mode` and `Iops`.

  1. If your file system is in USER\_PROVISIONED mode, using `Mode` is optional (if used, set `Mode` to `USER_PROVISIONED`).

     If your SSD file system is in AUTOMATIC mode, set `Mode` to `USER_PROVISIONED` (which switches the file system mode to USER\_PROVISIONED in addition to increasing the Metadata IOPS value).

  1. For SSD file systems, set `Iops` to a value of `1500`, `3000`, `6000`, `12000`, or multiples of `12000` up to a maximum of `192000`. For Intelligent-Tiering file systems, set `Iops` to `6000` or `12000`. The value you enter must be greater than or equal to the current Metadata IOPS value.

The following example updates the provisioned Metadata IOPS to 12000.

```
aws fsx update-file-system \
    --file-system-id {{fs-0123456789abcdef0}} \
    --lustre-configuration 'MetadataConfiguration={Mode={{USER_PROVISIONED}},Iops={{12000}}}'
```