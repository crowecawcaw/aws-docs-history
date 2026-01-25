# Configure storage (Amazon EFS)

###### Note

If you plan to use FSx for ONTAP storage for your deployment, refer to SAP HANA on AWS with Amazon FSx for NetApp ONTAP guide, and skip the Amazon EFS configuration steps detailed further here.

Amazon EFS provides easy-to-set-up, scalable, and highly available shared file systems that can be mounted with the NFSv4 client. For scale-out workloads, we recommend using Amazon EFS for SAP HANA shared and backup volumes. You can choose between different performance options for your file systems depending on your requirements. We recommend starting with the General Purpose and Provisioned Throughput options, with approximately 100 MiB/s to 200 MiB/s throughput. To set up your file systems, do the following:

1. Install the `nfs-utils` package in all the nodes in your scale-out cluster.
   - For RHEL, use `yum install nfs-utils`.
   - For SLES, use `zypper install nfs-utils`.

2. Create two Amazon EFS file systems and target mounts for SAP HANA shared and backup in your target VPC and subnet. For detailed steps, follow the instructions specified in the [AWS documentation](../../../AWSEC2/latest/UserGuide/AmazonEFS.md "../../../AWSEC2/latest/UserGuide/AmazonEFS.md").
3. After the file systems are created, mount the newly created file systems in all the nodes by using the following commands:

```
   mount -t nfs -o nfsvers=4.1,rsize=1048576,wsize=1048576,hard,timeo=600,retrans=2 <EFS DNS Name>:/ /hana/shared

   mount -t nfs -o nfsvers=4.1,rsize=1048576,wsize=1048576,hard,timeo=600,retrans=2 <EFS DNS Name>:/ /backup
```

###### Note

If you have trouble mounting the NFS file systems, you might need to adjust your security groups to allow access to port 2049. For details, see [Security Groups for Amazon EC2 Instances and Mount Targets](../../../efs/latest/ug/security-considerations.md#network-access "../../../efs/latest/ug/security-considerations.md#network-access") in the AWS documentation. 4. Add NFS mount entries to the `/etc/fstab` file in all the nodes to automatically mount these file systems during system restart; for example:

```
   echo “nfsvers=4.1,rsize=1048576,wsize=1048576,hard,timeo=600,retrans=2 <EFS DNS Name>:/ /hana/shared” >> /etc/fstab
   echo “nfsvers=4.1,rsize=1048576,wsize=1048576,hard,timeo=600,retrans=2 <EFS DNS Name>:/ /backup” >> /etc/fstab
```

5. Set appropriate permissions and ownership for your target mount points.
