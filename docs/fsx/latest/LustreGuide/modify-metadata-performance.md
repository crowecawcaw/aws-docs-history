# Increasing metadata performance

You can increase a file system's metadata performance by using the Amazon FSx console,
the AWS CLI, or the Amazon FSx API.

1. Open the Amazon FSx console at [https://console.aws.amazon.com/fsx/](https://console.aws.amazon.com/fsx/ "https://console.aws.amazon.com/fsx/").
2. In the left navigation pane, choose **File systems**.
   In the **File systems** list, choose the FSx for Lustre file system that you
   want to increase metadata performance for.
3. For **Actions**, choose **Update Metadata IOPS**.
   Or, in the **Summary** panel, choose **Update** next to the file
   system's **Metadata IOPS** field.

The **Update Metadata IOPS** dialog box appears. 4. Choose **User-provisioned**. 5. For **Desired Metadata IOPS**, choose the new
Metadata IOPS value. The value you enter must be greater
than or equal to the current Metadata IOPS value.

    * For SSD file systems, valid values are `1500`,
     `3000`, `6000`, `12000`, and
     multiples of `12000` up to a maximum of `192000`.
    * For Intelligent-Tiering file systems, valid values are `6000`
     and `12000`.

6. Choose **Update**.
   To increase the metadata performance for an FSx for Lustre file system,
   use the AWS CLI command [update-file-system](../../../cli/latest/reference/fsx/update-file-system.md "../../../cli/latest/reference/fsx/update-file-system.md") (UpdateFileSystem is the equivalent API action). Set the following parameters:

- Set `--file-system-id` to the ID of the file system that you are updating.
- To increase your metadata performance, use the `--lustre-configuration
 MetadataConfiguration` property. This property has two parameters, `Mode` and `Iops`.

      1. If your file system is in USER\_PROVISIONED mode, using `Mode` is optional (if used, set
       `Mode` to `USER_PROVISIONED`).


      If your SSD file system is in AUTOMATIC mode, set `Mode` to `USER_PROVISIONED`
       (which switches the file system mode to USER\_PROVISIONED in addition to increasing the Metadata IOPS value).
      2. For SSD file systems, set `Iops` to a value of `1500`, `3000`,
       `6000`, `12000`, or multiples of `12000` up to a maximum of `192000`.
       For Intelligent-Tiering file systems, set `Iops` to `6000` or `12000`.
       The value you enter must be greater than or equal to the current Metadata IOPS value.

  The following example updates the provisioned Metadata IOPS to 12000.

```
`aws fsx update-file-system \
 --file-system-id `fs-0123456789abcdef0` \
 --lustre-configuration 'MetadataConfiguration={Mode=`USER_PROVISIONED`,Iops=`12000`}'`
```
