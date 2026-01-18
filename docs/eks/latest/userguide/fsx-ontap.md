**Help improve this page**

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Use high-performance app storage with FSx for NetApp ONTAP

The NetApp Trident provides dynamic storage orchestration using a Container Storage Interface (CSI) compliant driver. This allows Amazon EKS clusters to manage the lifecycle of persistent volumes (PVs) backed by Amazon FSx for NetApp ONTAP file systems. Note that the Amazon FSx for NetApp ONTAP CSI driver is not compatible with Amazon EKS Hybrid Nodes. To get started, see [Use Trident with Amazon FSx for NetApp ONTAP](https://docs.netapp.com/us-en/trident/trident-use/trident-fsx.html "https://docs.netapp.com/us-en/trident/trident-use/trident-fsx.html") in the NetApp Trident documentation.

Amazon FSx for NetApp ONTAP is a storage service that allows you to launch and run fully managed ONTAP file systems in the cloud. ONTAP is NetApp’s file system technology that provides a widely adopted set of data access and data management capabilities. FSx for ONTAP provides the features, performance, and APIs of on-premises NetApp file systems with the agility, scalability, and simplicity of a fully managed AWS service. For more information, see the [FSx for ONTAP User Guide](../../../fsx/latest/ONTAPGuide/what-is-fsx-ontap.md "../../../fsx/latest/ONTAPGuide/what-is-fsx-ontap.md").

###### Important

If you are using Amazon FSx for NetApp ONTAP alongside the Amazon EBS CSI driver to provision EBS volumes, you must specify to not use EBS devices in the `multipath.conf` file. For supported methods, see [Configuration File Blacklist](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/7/html/dm_multipath/config_file_blacklist#config_file_blacklist "https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/7/html/dm_multipath/config_file_blacklist#config_file_blacklist"). Here is an example.

```
  defaults {
        user_friendly_names yes
        find_multipaths no
      }
      blacklist {
        device {
          vendor "NVME"
          product "Amazon Elastic Block Store"
        }
      }
```
