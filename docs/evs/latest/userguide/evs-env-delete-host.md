

# Delete an Amazon EVS host
<a name="evs-env-delete-host"></a>

You can delete an Amazon EVS host from your environment when the host is no longer needed. Before deleting a host, ensure that your environment retains enough hosts to satisfy your VCF deployment topology requirements. For minimum host counts, see the [VMware Cloud Foundation documentation](https://techdocs.broadcom.com/us/en/vmware-cis/vcf.html).

**Warning**  
Deleting a host without decommissioning will leave stale data in your vCenter and SDDC Manager that may require additional efforts to clean up. Ensure that your hosts are decommissioned before deleting hosts in the Amazon EVS console or API.

**Warning**  
Always use the Amazon EVS console or API to remove your Amazon EVS hosts. Deleting hosts from the EC2 console may leave your environment in an inconsistent state.

 **To delete an Amazon EVS host** 

Follow these steps to delete an Amazon EVS host.

**Example**  

1. Go to SDDC Manager.

1. Remove the cluster from SDDC Manager.

1. Decommission the host in SDDC Manager. For more information, see [Decommission Hosts](https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-5-2-and-earlier/5-2/map-for-administering-vcf-5-2/host-management-admin/decommission-hosts-admin.html) in the VMware Cloud Foundation documentation.

1. Go to the [Amazon EVS console](https://console.aws.amazon.com/evs).

1. In the navigation pane, choose **Environment**.

1. Select the environment that contains the host to delete.

1. Select the **Hosts** tab.

1. Choose **Delete host**.

1. Select the host and choose **Delete** within the **Hosts** tab. Repeat this step for each host that you want to delete.

1. Go to SDDC Manager.

1. Remove the cluster from SDDC Manager.

1. Decommission the host in SDDC Manager. For more information, see [Decommission Hosts](https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-5-2-and-earlier/5-2/map-for-administering-vcf-5-2/host-management-admin/decommission-hosts-admin.html) in the VMware Cloud Foundation documentation.

1. Open a new terminal session.

1. Delete the host. See example command below for reference.

   ```
   aws evs delete-environment-host \
   --environment-id env-abcdefghij \
   --host-name my-evs-host.example.com
   ```