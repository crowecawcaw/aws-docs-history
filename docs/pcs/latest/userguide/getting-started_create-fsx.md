

# Create shared storage for AWS PCS in Amazon FSx for Lustre
<a name="getting-started_create-fsx"></a>

Amazon FSx for Lustre makes it easy and cost-effective to launch and run the popular, high-performance Lustre file system. You use Lustre for workloads where speed matters, such as machine learning, high performance computing (HPC), video processing, and financial modeling. For more information, see [What is Amazon FSx for Lustre?](https://docs.aws.amazon.com/fsx/latest/LustreGuide/what-is.html) in the *Amazon FSx for Lustre User Guide*. 

 The AWS PCS demonstration cluster can use an FSx for Lustre file system to provide a high-performance shared directory between the cluster nodes. Create an FSx for Lustre file system in the same VPC as your cluster. 

**To create your FSx for Lustre file system**

1. Go to the [Amazon FSx console](https://console.aws.amazon.com/fsx).

1. Make sure the console is set to use the same AWS Region as your cluster.

1. Choose **Create file system**.
   + For **Select file system type**, choose **Amazon FSx for Lustre**, then choose **Next**.

1. On the **Specify file system details** page, set the following parameters:
   + Under **File system details**
     + For **Name**, enter `getstarted-fsx`
     + For **Deployment and storage type**, choose **Persistent, SSD**. Persistent file systems store data durably, which suits a shared directory that outlives individual compute nodes.
     + For **Throughput per unit of storage**, choose **125 MB/s/TiB**
     + For **Storage capacity**, enter 1.2 TiB
     + For **Metadata Configuration**, choose **Automatic**
     + For **Data compression type**, choose **LZ4**
   + Under **Network & security**
     + For **Virtual Private Cloud (VPC)**, choose the VPC named `hpc-networking:Large-Scale-HPC`
     + For **VPC Security Groups**, leave the security group named `default`
     + For **Subnet**, choose the subnet where the name starts with `hpc-networking:PrivateSubnetA`. Place the file system in the same subnet as your compute nodes so that they reach it over the local network.
   + Leave the other options set to their default values.
   + Choose **Next**.

1. On the **Review and create** page, choose **Create file system**. This returns you to the **File systems** page.

1.  Navigate to the details page for the FSx for Lustre file system you created. 

1. Make a note of the **DNS name** and the **Mount name**. You provide both values later when you configure the node lifecycle action that mounts this file system. The `mount-fsx-lustre` script mounts the file system by its DNS name, not its file system ID.

**Note**  
 The **Status** field shows **Creating** while the file system is being provisioned. File system creation can take several minutes. Wait until it completes before proceeding with the rest of the tutorial. 