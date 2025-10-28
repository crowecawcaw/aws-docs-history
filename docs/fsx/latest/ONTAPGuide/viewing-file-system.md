# Monitoring file system details

You can view detailed configuration information for your FSx for ONTAP file system using the Amazon FSx console,
the AWS CLI, and the API and supported AWS SDKs.

###### To view detailed file system information:

- **Using the console** – Choose a file
  system to view the **File systems** detail page. The
  **Summary** panel shows the file system's ID, life
  cycle status, deployment type, SSD storage capacity, throughput capacity,
  provisioned IOPS, Availability Zones, and creation time.

The following tabs provide detailed configuration information and editing for properties that can be modified:

    + Network & security – Displays the following file system administration information:




    	- Default Amazon VPC
    	- Amazon VPC route tables associated with a Multi-AZ file system
    	- File system's network type (IPv4-only or dual-stack)
    	- Endpoint IPv4 or IPv6 address range
    	- The AWS Key Management Service (AWS KMS) key ID
    + Monitoring & performance – Displays CloudWatch alarms you've created, and metrics and warnings for the following categories:




    	- Summary – high level summary of file system activity metrics
    	- File system storage capacity
    	- File server and disk performance
    For more information, see [Monitoring with Amazon CloudWatch](monitoring-cloudwatch.md "monitoring-cloudwatch.md").
    + Administration – Displays the following file system administration information:




    	- The DNS names and IP addresses of the file system's management and
    	 inter-cluster endpoints.
    	- The ONTAP administrator username.
    	- The option to update the ONTAP administrator password.
    + List of the file system's SVMs
    + List of the file system's volumes
    + Backup settings – change the file system's automatic daily backup setting.
    + Updates – shows the status of user initiated updates made to the file system's configuration.
    + Tags – view, edit, add, remove tag Key:Value pairs.

- **Using the CLI or API** – Use the
  [describe-file-systems](../../../cli/latest/reference/fsx/describe-file-systems.md "../../../cli/latest/reference/fsx/describe-file-systems.md") CLI command or the [DescribeFileSystems](../APIReference/API_DescribeFileSystems.md "../APIReference/API_DescribeFileSystems.md") API operation.

## FSx for ONTAP file system status

You can view the status of an Amazon FSx file system by using the Amazon FSx console, the AWS CLI
command [describe-file-systems](../../../cli/latest/reference/fsx/describe-file-systems.md "../../../cli/latest/reference/fsx/describe-file-systems.md"), or the API operation [DescribeFileSystems](../APIReference/API_DescribeFileSystems.md "../APIReference/API_DescribeFileSystems.md").

| File system status | Description                                                                                                                                         |
| ------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| AVAILABLE          | The file system has been successfully created and is available for use.                                                                             |
| CREATING           | Amazon FSx is creating a new file system.                                                                                                           |
| DELETING           | Amazon FSx is deleting an existing file system.                                                                                                     |
| MISCONFIGURED      | The file system is in a misconfigured but recoverable state.                                                                                        |
| FAILED             | 1. The file system has failed and Amazon FSx can't recover it. 2. When creating new file system, Amazon FSx was unable to create a new file system. |
