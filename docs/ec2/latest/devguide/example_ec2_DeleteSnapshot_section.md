

# Use `DeleteSnapshot` with an AWS SDK or CLI
<a name="example_ec2_DeleteSnapshot_section"></a>

The following code examples show how to use `DeleteSnapshot`.

Action examples are code excerpts from larger programs and must be run in context. You can see this action in context in the following code example: 
+  [Working with block storage encryption, snapshots, and volume initialization](example_ec2_GettingStarted_022_section.md) 

------
#### [ CLI ]

**AWS CLI**  
**To delete a snapshot**  
This example command deletes a snapshot with the snapshot ID of `snap-1234567890abcdef0`. If the command succeeds, no output is returned.  
Command:  

```
aws ec2 delete-snapshot --snapshot-id {{snap-1234567890abcdef0}}
```
+  For API details, see [DeleteSnapshot](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/delete-snapshot.html) in *AWS CLI Command Reference*. 

------
#### [ PowerShell ]

**Tools for PowerShell V4**  
**Example 1: This example deletes the specified snapshot. You are prompted for confirmation before the operation proceeds, unless you also specify the Force parameter.**  

```
Remove-EC2Snapshot -SnapshotId snap-12345678
```
**Output:**  

```
Confirm
Are you sure you want to perform this action?
Performing the operation "Remove-EC2Snapshot (DeleteSnapshot)" on target "snap-12345678".
[Y] Yes  [A] Yes to All  [N] No  [L] No to All  [S] Suspend  [?] Help (default is "Y"):
```
+  For API details, see [DeleteSnapshot](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*. 

**Tools for PowerShell V5**  
**Example 1: This example deletes the specified snapshot. You are prompted for confirmation before the operation proceeds, unless you also specify the Force parameter.**  

```
Remove-EC2Snapshot -SnapshotId snap-12345678
```
**Output:**  

```
Confirm
Are you sure you want to perform this action?
Performing the operation "Remove-EC2Snapshot (DeleteSnapshot)" on target "snap-12345678".
[Y] Yes  [A] Yes to All  [N] No  [L] No to All  [S] Suspend  [?] Help (default is "Y"):
```
+  For API details, see [DeleteSnapshot](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*. 

------
#### [ Rust ]

**SDK for Rust**  
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/rustv1/examples/ebs#code-examples). 

```
async fn delete_snapshot(client: &Client, id: &str) -> Result<(), Error> {
    client.delete_snapshot().snapshot_id(id).send().await?;

    println!("Deleted");

    Ok(())
}
```
+  For API details, see [DeleteSnapshot](https://docs.rs/aws-sdk-ec2/latest/aws_sdk_ec2/client/struct.Client.html#method.delete_snapshot) in *AWS SDK for Rust API reference*. 

------

For a complete list of AWS SDK developer guides and code examples, see [Create Amazon EC2 resources using an AWS SDK](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.