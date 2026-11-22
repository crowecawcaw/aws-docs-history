

# VCF feature support on Amazon EVS

Check whether Amazon Elastic VMware Service supports a VMware Cloud Foundation (VCF) feature before you plan a design that depends on it.

Each table covers one area. For the VCF versions and EC2 instance types that Amazon EVS provides, see [Supported VCF versions and instance types](versions-provided.md).

## Status values
<a name="feat-status-values"></a>

The **Status** column uses the following values.
+  **Supported** means that the feature works on every VCF version and instance type in the row, with no Amazon EVS-specific condition beyond the row.
+  **Supported with conditions** means that the feature works only under the conditions in the **Instance types** and **Notes for Amazon EVS** cells.
+  **Not supported** means that Amazon EVS doesn’t support the feature, or that Broadcom doesn’t support it on this hardware or environment.

## Compute and storage
<a name="feat-compute-storage"></a>

The following table lists the compute and storage features and whether Amazon EVS supports each one.


| Feature | Status | VCF versions | Instance types | Notes for Amazon EVS | Broadcom documentation | Amazon EVS page | 
| --- | --- | --- | --- | --- | --- | --- | 
|  vSAN Express Storage Architecture (ESA) | Supported with conditions | All | Hosts with local NVMe | Requires local NVMe instance storage. Set failures to tolerate (FTT) to at least 1 when you run VCF bringup. Diskless hosts, which need VCF 9.x, have no local NVMe and use external principal storage instead. | None |  [Step 4a (local storage): Prepare the VCF Installer](self-deployed-install-vcf.md)  | 
|  vSAN Original Storage Architecture (OSA) | Not supported | All | All | Amazon EVS clusters use vSAN ESA. Use vSAN ESA for vSAN storage. | None | None | 

## Availability and recovery
<a name="feat-availability-recovery"></a>

The following table lists the availability and recovery features and whether Amazon EVS supports each one.


| Feature | Status | VCF versions | Instance types | Notes for Amazon EVS | Broadcom documentation | Amazon EVS page | 
| --- | --- | --- | --- | --- | --- | --- | 
|  vSphere Fault Tolerance | Not supported | All | All | Broadcom doesn’t support Fault Tolerance for VMs on NSX port groups, or for NSX Managers and Edge nodes. Workload VMs on Amazon EVS run on NSX overlay networks. |  [Broadcom knowledge base article 317806](https://knowledge.broadcom.com/external/article?articleNumber=317806)  | None | 