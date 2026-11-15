

# Step 2: Validate and confirm inventory
<a name="transform-vmware-ms-validate-inventory"></a>

Before loading your server data into MGN, AWS Transform prepares the migration inventory file for your review. You must confirm the migration inventory file data and content as this sets the migration configuration. You can review the data in the file and update it using either of these methods:
+ **Edit the migration inventory file directly** – Download the file in CSV or XLSX format and modify it locally in your preferred spreadsheet application. You can adjust any of the fields in the file, except for the read-only ones.
+ **Use the chat interface** – Make targeted changes for specific columns on individual source servers without downloading the entire file.

The migration inventory file includes details such as server names, operating systems, Amazon EC2 instance type recommendations, target subnets, security groups, IP assignments, and licensing options. Required fields include:
+ **Server information** – Server name, VMID, and source specifications.
+ **Wave assignment** – Migration wave grouping.
+ **Application grouping** – Logical application associations.
+ **Target configuration** – Target account, Region, and Amazon EC2 instance type. You can control the operating system licensing options (BYOL or License Included) and tenancy by specifying the configuration in the inventory file columns `mgn:launch:placement:operating-system-licensing` and `mgn:launch:placement:tenancy`.
+ **Network configuration** – Target subnet and security groups.

For more information about the fields, see [Import parameters](https://docs.aws.amazon.com/mgn/latest/ug/import-parameters.html) in the *MGN User Guide*.

After you review the migration inventory file, you can either accept it as shown or upload a modified version. AWS Transform then loads the data into MGN, which creates source server records for each server in the wave.

**Note**  
Do not remove columns or change column headers in the inventory file. AWS Transform requires the original file structure to process the data correctly.

**Note**  
AWS Transform allows one import to a given target AWS account and target AWS Region at a time. If you work on more than one wave simultaneously, or if there is more than one migration job running with the same target account, you must wait for an import to finish before you can perform another import in a different wave or job.