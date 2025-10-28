# Create an Amazon EVS host

After an Amazon EVS environment deploys, you can add hosts to increase capacity and workload resiliency.
Amazon EVS supports 4-16 hosts per environment.
This action can only be used after the Amazon EVS environment is deployed.

###### Note

You must assign and commission the host within the SDDC Manager user interface.

**To create an Amazon EVS host**

Follow these steps to create an Amazon EVS host.

###### Warning

Amazon EVS hosts use a custom vendor add-on to provide important host functionality.
When you add a host to your environment, it will have the latest available version of the Amazon EVS custom add-on.
If your environment uses hosts with an older add-on version, adding host to your vSphere cluster will cause cluster image remediation to fail.
For steps to troubleshoot this issue, see [Troubleshoot add host failure due to incompatible cluster image](evs-env-ami-maintenance.md#troubleshoot-add-host-failure-cluster-image "evs-env-ami-maintenance.md#troubleshoot-add-host-failure-cluster-image").

###### Warning

If you have updated your ESXi version after the Amazon EVS environment deployment, SDDC manager may fail during VCF host validation in the commission hosts step.
For steps to troubleshoot this issue, see [SDDC Manager fails VCF host validation during host commissioning](troubleshooting.md#troubleshoot-sddc-failure-host-commission "troubleshooting.md#troubleshoot-sddc-failure-host-commission").

###### Note

Ensure that your Amazon EVS host count per EVS environment quota is correctly set to ensure successfully host creation.
Host creation fails if this quota value is less than the number of hosts that you are attempting to provision within a single Amazon EVS environment.
To raise the quota, you can request a quota increase.
For more information, see [Amazon EVS service quotas](service-quotas-evs.md "service-quotas-evs.md").

Amazon EVS console and SDDC Managuer UI

1. Go to the [Amazon EVS console](https://console.aws.amazon.com/evs "https://console.aws.amazon.com/evs").
2. In the navigation pane, choose **Environment**.
3. Select the environment where you want to create the host.
4. Select the **Hosts** tab.
5. Choose **Create host**.
6. Specify host details and choose **Create host**.
7. To verify completion, check that the **Host state** has changed to **Created**.
8. Go to SDDC Manager.
9. Commission the new host in SDDC Manager.
   For more information, see [Commission Hosts](https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-5-2-and-earlier/5-2/map-for-administering-vcf-5-2/host-management-admin/commission-hosts-admin.html "https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-5-2-and-earlier/5-2/map-for-administering-vcf-5-2/host-management-admin/commission-hosts-admin.html") in the VMware Cloud Foundation documentation.
10. Add the new host to the cluster, using SDDC Manager.
    For more information, see [How to Add an ESXi
    Host to Your vSphere Cluster by Using the Quickstart Workflow](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/8-0/use-quickstart-to-add---host-to-a-cluster.html "https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/8-0/use-quickstart-to-add---host-to-a-cluster.html") in the vSphere documentation.

AWS CLI and SDDC Manager UI

1. Open a new terminal session.
2. Create a new host.
   See example command below for reference.

```
aws evs create-environment-host \
    --environment-id "env-abcde12345" \
    --host '{ \
        "hostName": "esxi-host-05", \
        "keyName": "your-ec2-keypair-name", \
        "instanceType": "i4i.metal" \
    }'
```

3. Go to SDDC Manager.
4. Commission the new host in SDDC Manager.
   For more information, see [Commission Hosts](https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-5-2-and-earlier/5-2/map-for-administering-vcf-5-2/host-management-admin/commission-hosts-admin.html "https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-5-2-and-earlier/5-2/map-for-administering-vcf-5-2/host-management-admin/commission-hosts-admin.html") in the VMware Cloud Foundation documentation.
5. Add the new host to the cluster, using SDDC Manager.
   For more information, see [How to Add an ESXi
   Host to Your vSphere Cluster by Using the Quickstart Workflow](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/8-0/use-quickstart-to-add---host-to-a-cluster.html "https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/8-0/use-quickstart-to-add---host-to-a-cluster.html") in the vSphere documentation.
