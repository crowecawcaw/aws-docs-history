# Delete an Amazon EVS host

You can delete an Amazon EVS host from your environment when the host is no longer needed.
Amazon EVS requires that your environment have a minimum of four hosts.
Amazon EVS does not support environments with fewer than four hosts.

###### Warning

Deleting a host without decommissioning will leave stale data in your vCenter and SDDC Manager that may require additional efforts to clean up.
Ensure that your hosts are decommissioned before deleting hosts in the Amazon EVS console or API.

###### Warning

Always use the Amazon EVS console or API to remove your Amazon EVS hosts.
Deleting hosts from the EC2 console may leave your environment in an inconsistent state.

**To delete an Amazon EVS host**

Follow these steps to delete an Amazon EVS host.

###### Example

SDDC Managuer UI and Amazon EVS console

1. Go to SDDC Manager.
2. Remove the cluster from SDDC Manager.
3. Decommission the host in SDDC Manager.
   For more information, see [Decommission Hosts](https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-5-2-and-earlier/5-2/map-for-administering-vcf-5-2/host-management-admin/decommission-hosts-admin.html "https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-5-2-and-earlier/5-2/map-for-administering-vcf-5-2/host-management-admin/decommission-hosts-admin.html") in the VMware Cloud Foundation documentation.
4. Go to the [Amazon EVS console](https://console.aws.amazon.com/evs "https://console.aws.amazon.com/evs").
5. In the navigation pane, choose **Environment**.
6. Select the environment that contains the host to delete.
7. Select the **Hosts** tab.
8. Choose **Delete host**.
9. Select the host and choose **Delete** within the **Hosts** tab.
   Repeat this step for each host that you want to delete.

SDDC Manager UI and AWS CLI

1. Go to SDDC Manager.
2. Remove the cluster from SDDC Manager.
3. Decommission the host in SDDC Manager.
   For more information, see [Decommission Hosts](https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-5-2-and-earlier/5-2/map-for-administering-vcf-5-2/host-management-admin/decommission-hosts-admin.html "https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-5-2-and-earlier/5-2/map-for-administering-vcf-5-2/host-management-admin/decommission-hosts-admin.html") in the VMware Cloud Foundation documentation.
4. Open a new terminal session.
5. Delete the host.
   See example command below for reference.

```
aws evs delete-environment-host \
--environment-id env-abcdefghij \
--host-name my-evs-host.example.com
```
