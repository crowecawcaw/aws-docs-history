# Storage Services

The SAP BOBI Platform uses the following AWS storage services:

- [Amazon Elastic Block Store (Amazon EBS)](https://aws.amazon.com/ebs/ "https://aws.amazon.com/ebs/") is used for block storage requirements of SAP BOBI Platform application servers and databases (when the database is installed on EC2).

Figure 2 shows an example use of EBS volumes for application and database. In this example, EBS volumes are used for root volumes, SAP BOBI Platform installation directory, operating system swap volume, and database data and log volumes. The CMS database is typically a small database that stores information like users, SAP BOBI Platform servers, folders, and other configurations. Therefore, it does not have the same storage performance requirements as other enterprise OLTP/OLAP databases. Follow the best practices of the database vendor for designing storage for the SAP BOBI Platform database.

- [Amazon FSx for Windows File Server](https://aws.amazon.com/fsx/windows/ "https://aws.amazon.com/fsx/windows/") is used for shared file system requirements of SAP BOBI Platform application servers installed on Windows EC2 instances. The usage is the same as for FileStore as described above.
- [Amazon Simple Storage Service (Amazon S3)](https://aws.amazon.com/s3/ "https://aws.amazon.com/s3/") is used for storing the backups of SAP BOBI Platform application servers.
  Figure 2 shows an example use of AWS storage services by an SAP BOBI Platform installation. In this example, two SAP applications servers and a database are installed on three separate EC2 instances with Windows operating systems. EBS volumes are used for local file systems like root, install, swap, data, and log volumes. [Amazon FSx for Windows File Server](https://aws.amazon.com/fsx/windows/ "https://aws.amazon.com/fsx/windows/") is used for shared file system FileStore.

**Figure 2: AWS storage system use on SAP BOBI Platform installation**

![Storage system use on SAP BOBI Platform installation](images/bobi_windows_storage.png)
