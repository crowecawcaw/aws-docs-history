# Monitoring storage virtual machine (SVM) configuration

details

You can see the FSx for ONTAP storage virtual machines that are currently on your
file system using the Amazon FSx console, the AWS CLI, and the Amazon FSx API.

###### To view a storage virtual machine on your file system:

- **Using the console** – Choose a file
  system to view its **File systems** detail page. To list
  all the storage virtual machines on the file system, choose the
  **Storage virtual machines** tab, and then choose the
  storage virtual machine that you want to view.
- **Using the CLI or API** – Use the
  [describe-storage-virtual-machines](../../../cli/latest/reference/fsx/describe-storage-virtual-machines.md "../../../cli/latest/reference/fsx/describe-storage-virtual-machines.md") CLI command or the [DescribeStorageVirtualMachines](../APIReference/API_DescribeStorageVirtualMachines.md "../APIReference/API_DescribeStorageVirtualMachines.md") API operation.

The system response is a list of full descriptions of all the SVMs in your account in that AWS Region.
