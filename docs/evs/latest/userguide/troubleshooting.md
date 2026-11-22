

# Troubleshooting

When something doesn’t work as expected in your Amazon Elastic VMware Service environment, find the symptom in the following table. Then go to the page that covers it. If a problem remains, see [Get help from AWS Support and Broadcom](get-help.md).

The procedures in [Deploy in Self-deployed mode](getting-started-self-deployed.md) deploy VCF 9.x. Pages in [Deploy in EVS-deployed mode](evs-deployed-overview.md) cover VCF 5.2.x. A page with no line and outside those sections covers both.

## Problems by area and symptom
<a name="troubleshooting-by-symptom"></a>

The following table lists common problems. The columns show the area, the symptom, the VMware Cloud Foundation (VCF) version that it applies to, and the page that covers it. For how VCF versions relate to the deployment modes, see [Differences between deployment modes](deployment-mode-differences.md).


| Area | Symptom | VCF version | Where to look | 
| --- | --- | --- | --- | 
| Deployment |  `create-environment` returns a `ValidationException`, or a host stays in `CREATING`  | 9.x |  [Environment, host, and connector symptoms](troubleshoot-self-deployed.md#troubleshoot-sd-env-host)  | 
| Deployment |  `create-environment-host` fails with an ESX version error, or `create-environment-connector` fails with a Secrets Manager access error | 9.x |  [`create-environment-host` fails with an ESX version error](troubleshoot-self-deployed.md#troubleshoot-sd-esx-version) and [`create-environment-connector` fails with a Secrets Manager access error](troubleshoot-self-deployed.md#troubleshoot-sd-connector-secret)  | 
| Deployment | The VCF Installer validation or VCF bringup fails | 9.x |  [VCF Installer and bringup symptoms](troubleshoot-self-deployed.md#troubleshoot-sd-installer)  | 
| Deployment | BGP sessions between the NSX Edge nodes and Amazon VPC Route Server don’t come up or flap | 9.x |  [NSX Edge and BGP symptoms](troubleshoot-self-deployed.md#troubleshoot-sd-nsx) and [Step 5: Configure NSX networking](self-deployed-nsx-edge.md)  | 
| Diskless hosts | The NFS datastore doesn’t mount, or the VCF Installer rejects the specification or reports low capacity | 9.x |  [Diskless host symptoms](troubleshoot-self-deployed.md#troubleshoot-diskless)  | 
| Diskless hosts | Creating an FSx for OpenZFS volume fails with a `BadRequest` error, the datastore doesn’t show the new size, or the VCF Installer shows an inventory error after the first start | 9.x |  [Creating an FSx for OpenZFS volume fails with a `BadRequest` error](troubleshoot-self-deployed.md#troubleshoot-diskless-volume-tag), [The datastore doesn’t show the new size after a file system increase](troubleshoot-self-deployed.md#troubleshoot-diskless-size-refresh), and [The VCF Installer shows an inventory error after the first start](troubleshoot-self-deployed.md#troubleshoot-diskless-installer-inventory)  | 
| Status checks | The **Environment status** shows **Failed** for reachability, host count, key re-use, or key coverage | 5.2.x |  [Troubleshoot environment status checks](troubleshoot-status-checks.md)  | 
| Connectors | A connector reachability check stays `FAILED`  | All |  [The connector is `ACTIVE`, but its reachability check stays `FAILED`](troubleshoot-self-deployed.md#troubleshoot-sd-connector-reachability) and [Troubleshoot environment status checks](troubleshoot-status-checks.md)  | 
| Hosts | Host creation fails with a vCPU limit error | All |  [Host creation fails with a vCPU limit error](troubleshoot-hosts.md#troubleshoot-vcpu-limit)  | 
| Hosts | A vSphere HA isolation address message, a vSAN upgrade precheck failure, or an incompatible cluster image | All |  [Troubleshoot hosts](troubleshoot-hosts.md)  | 
| Hosts | You receive a vSAN capacity warning in AWS Health | All |  [vSAN capacity warning received in AWS Health](troubleshoot-hosts.md#troubleshoot-vsan-capacity)  | 
| Hosts | SDDC Manager fails host validation during host commissioning | 5.2.x |  [SDDC Manager fails VCF host validation during host commissioning](troubleshoot-hosts.md#troubleshoot-sddc-failure-host-commission)  | 
| Hosts | Hosts can’t mount an FSx for ONTAP NFS datastore | All |  [Hosts can’t mount an FSx for ONTAP NFS datastore](troubleshoot-hosts.md#troubleshoot-nfs-ontap)  | 
| Hosts | You can’t reach an ESX host over the network | All |  [You can’t reach an ESX host over the network](troubleshoot-hosts.md#access-ec2-serial-console)  | 
| Networking | Amazon EVS can’t reach DNS servers or SDDC Manager | All |  [Amazon EVS can’t reach DNS servers or SDDC Manager](troubleshoot-networking.md#troubleshoot-dns-reachability)  | 
| Networking | Route server routes don’t propagate, or the deployment fails because of the route server configuration | All |  [Routes don’t propagate or BGP sessions don’t come up](troubleshoot-networking.md#troubleshoot-rs-routes) and [The deployment fails because of the VPC Route Server configuration](troubleshoot-networking.md#troubleshoot-rs-deploy-fails)  | 
| Networking | NSX connectivity fails, or on-premises systems can’t reach the environment | All |  [NSX connectivity fails after the environment is deployed](troubleshoot-networking.md#troubleshoot-rt-association) and [On-premises systems can’t reach the environment](troubleshoot-networking.md#troubleshoot-tgw-routes)  | 
| Networking | Security group rules have no effect on VLAN subnet traffic | All |  [Security group rules have no effect on VLAN subnet traffic](troubleshoot-networking.md#troubleshoot-nacl)  | 
| Networking | You can’t reach the VCF appliances after you add a distributed firewall rule | All |  [You can’t reach the VCF appliances after you add a distributed firewall rule](troubleshoot-networking.md#troubleshoot-dfw-lockout)  | 
| Windows Server entitlements | An entitlement is `CREATE_FAILED`, `AT_RISK`, or `ENTITLEMENT_REMOVED`  | All |  [Troubleshoot Windows Server entitlements](troubleshoot-entitlements.md)  | 
| Identity and access | An IAM permission error when you use Amazon EVS | All |  [Troubleshoot Amazon EVS identity and access](security-iam-troubleshoot.md)  | 

## Troubleshooting topics
<a name="troubleshooting-topics"></a>

The following pages cover troubleshooting and support.
+  [Troubleshoot Self-deployed deployments](troubleshoot-self-deployed.md) 
+  [Troubleshoot environment status checks](troubleshoot-status-checks.md) 
+  [Troubleshoot hosts](troubleshoot-hosts.md) 
+  [Troubleshoot networking](troubleshoot-networking.md) 
+  [Troubleshoot Windows Server entitlements](troubleshoot-entitlements.md) 
+  [Troubleshoot Amazon EVS identity and access](security-iam-troubleshoot.md) 
+  [Get help from AWS Support and Broadcom](get-help.md) 

**Topics**