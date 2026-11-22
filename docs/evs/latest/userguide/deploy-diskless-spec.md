

# Step 4b (diskless): Create the specification and deploy

In this step, you describe the VMware Cloud Foundation (VCF) management domain in a JSON deployment specification, validate it in the VCF Installer, and deploy VCF. Then you verify the cluster and the storage in the vSphere Client. The example is a two-host VCF 9.x management domain on r7i.metal-24xl hosts, with one NFS principal datastore on Amazon FSx for OpenZFS and no vSAN.

Before you begin, make sure that the following are true.
+ You completed [Step 4a (diskless): Prepare diskless hosts and the VCF Installer](getting-started-diskless.md).
+ Every host is in the `CREATED` state.
+ The principal datastore is mounted on the first host, and every download shows success.

## Create the deployment specification
<a name="getting-started-diskless-spec"></a>

To create the specification, do the following.

1. List the VLAN IDs that Amazon Elastic VMware Service assigned to your environment. The VLAN IDs can differ for each environment, so read them from your environment.

   Replace the example environment ID with your own value. Replace `<region-code>` with the Region where you created the environment.

   ```bash
   aws evs list-environment-vlans \
       --environment-id env-abcde12345 \
       --query 'environmentVlans[].[functionName,vlanId,cidr]' \
       --output table \
       --region <region-code>
   ```

   You need the VM management (`vmManagement`), vMotion, and host overlay (`vTep`) VLAN IDs. The output also lists a VLAN ID for `vmkManagement`. Don’t use it, because the host management network is untagged and uses VLAN ID `0`.

1. Save the following specification to a file. It’s for a two-host management domain that uses one NFS datastore and no vSAN.

   Replace the example addresses and names with your own values.

   ```json
   {
     "version": "<vcf-spec-version>",
     "vcfInstanceName": "evs-vcf",
     "sddcId": "evs-m01",
     "ceipEnabled": false,
     "skipEsxThumbprintValidation": true,
     "skipGatewayPingValidation": true,
     "workflowType": "VCF",
     "dnsSpec": {
       "subdomain": "evs.example.com",
       "nameservers": ["10.10.200.100", "10.10.200.101"]
     },
     "ntpServers": ["time.aws.com"],
     "hostSpecs": [
       {
         "hostname": "esx01.evs.example.com",
         "credentials": { "username": "root", "password": "<esx01-root-password>" }
       },
       {
         "hostname": "esx02.evs.example.com",
         "credentials": { "username": "root", "password": "<esx02-root-password>" }
       }
     ],
     "networkSpecs": [
       {
         "networkType": "MANAGEMENT",
         "ipAddressVersion": "IPv4",
         "subnet": "10.10.0.0/24",
         "gateway": "10.10.0.1",
         "vlanId": "0",
         "mtu": 1500,
         "portGroupKey": "DVPG_FOR_MANAGEMENT",
         "teamingPolicy": "failover_explicit",
         "activeUplinks": ["uplink1"],
         "standbyUplinks": ["uplink2"]
       },
       {
         "networkType": "VM_MANAGEMENT",
         "ipAddressVersion": "IPv4",
         "subnet": "10.10.1.0/24",
         "gateway": "10.10.1.1",
         "vlanId": "<vm-management-vlan-id>",
         "mtu": 1500,
         "portGroupKey": "DVPG_FOR_VM_MANAGEMENT",
         "teamingPolicy": "failover_explicit",
         "activeUplinks": ["uplink1"],
         "standbyUplinks": ["uplink2"]
       },
       {
         "networkType": "VMOTION",
         "ipAddressVersion": "IPv4",
         "subnet": "10.10.2.0/24",
         "gateway": "10.10.2.1",
         "vlanId": "<vmotion-vlan-id>",
         "mtu": 8500,
         "includeIpAddressRanges": [
           { "startIpAddress": "10.10.2.10", "endIpAddress": "10.10.2.20" }
         ],
         "portGroupKey": "DVPG_FOR_VMOTION",
         "teamingPolicy": "failover_explicit",
         "activeUplinks": ["uplink1"],
         "standbyUplinks": ["uplink2"]
       },
       {
         "networkType": "NFS",
         "ipAddressVersion": "IPv4",
         "subnet": "10.10.0.0/24",
         "gateway": "10.10.0.1",
         "vlanId": "0",
         "mtu": 1500,
         "includeIpAddressRanges": [
           { "startIpAddress": "10.10.0.20", "endIpAddress": "10.10.0.29" }
         ],
         "portGroupKey": "DVPG_FOR_NFS",
         "teamingPolicy": "failover_explicit",
         "activeUplinks": ["uplink1"],
         "standbyUplinks": ["uplink2"]
       }
     ],
     "vspClusterSpec": {
       "ipv4Pool": {
         "ipRange": { "startIpAddress": "10.10.1.100", "endIpAddress": "10.10.1.113" }
       },
       "platformFqdn": "vsp-platform.evs.example.com",
       "instanceFqdn": "vsp-instance.evs.example.com",
       "fleetFqdn": "vsp-fleet.evs.example.com",
       "systemUserPassword": "<vsp-system-password>",
       "size": "small",
       "name": "evs-m01-vmsp-01",
       "internalClusterCidrIpv4": "198.18.0.0/15"
     },
     "nsxtSpec": {
       "transportVlanId": "<vtep-vlan-id>",
       "ipAddressPoolSpec": {
         "name": "evs-m01-cl01-tep01",
         "description": "ESX host overlay TEP IP pool",
         "subnets": [
           {
             "cidr": "10.10.4.0/24",
             "gateway": "10.10.4.1",
             "ipAddressPoolRanges": [
               { "start": "10.10.4.10", "end": "10.10.4.30" }
             ]
           }
         ]
       },
       "nsxtManagerSize": "medium",
       "vipFqdn": "nsx.evs.example.com",
       "rootNsxtManagerPassword": "<nsx-root-password>",
       "nsxtAdminPassword": "<nsx-admin-password>",
       "nsxtAuditPassword": "<nsx-audit-password>",
       "useExistingDeployment": false,
       "nsxtManagers": [
         { "hostname": "nsx01.evs.example.com" }
       ]
     },
     "vcfOperationsSpec": {
       "applianceSize": "small",
       "useExistingDeployment": false,
       "adminUserPassword": "<vcf-operations-admin-password>",
       "nodes": [
         {
           "hostname": "vcfops.evs.example.com",
           "rootUserPassword": "<vcf-operations-root-password>",
           "type": "<primary-node-type>"
         }
       ]
     },
     "vcfOperationsCollectorSpec": {
       "applianceSize": "small",
       "hostname": "vcfopscol.evs.example.com",
       "rootUserPassword": "<vcf-operations-collector-root-password>",
       "useExistingDeployment": false
     },
     "licenseServerSpec": { "hostname": "vcf-license.evs.example.com" },
     "vidbSpec": { "hostname": "vcf-vidb.evs.example.com" },
     "saltSpec": {},
     "saltRaasSpec": {},
     "telemetryAcceptorSpec": {},
     "fleetLcmSpec": { "hostname": "vsp-fleet.evs.example.com" },
     "sddcLcmSpec": { "hostname": "vsp-instance.evs.example.com" },
     "fleetDepotSpec": {},
     "vcenterSpec": {
       "vcenterHostname": "vc.evs.example.com",
       "adminUserSsoPassword": "<vcenter-sso-password>",
       "rootVcenterPassword": "<vcenter-root-password>",
       "vmSize": "small",
       "ssoDomain": "vsphere.local",
       "useExistingDeployment": false
     },
     "clusterSpec": {
       "datacenterName": "EVS-Datacenter",
       "clusterName": "EVS-Mgmt-Cluster",
       "clusterEvcMode": "INTEL_SAPPHIRERAPIDS"
     },
     "datastoreSpec": {
       "nfsDatastoreSpec": {
         "datastoreName": "fsx-principal",
         "nasVolume": {
           "serverName": ["<fsx-endpoint-ip>"],
           "path": "/fsx/vcf-principal",
           "readOnly": false,
           "enableBindToVmknic": false
         }
       }
     },
     "dvsSpecs": [
       {
         "dvsName": "evs-m01-cl01-vds01",
         "networks": ["MANAGEMENT", "VM_MANAGEMENT", "VMOTION", "NFS"],
         "mtu": 8500,
         "nsxtSwitchConfig": {
           "transportZones": [
             { "name": "evs-overlay-TZ", "transportType": "OVERLAY" },
             { "name": "evs-vlan-TZ", "transportType": "VLAN" }
           ],
           "hostSwitchOperationalMode": "STANDARD"
         },
         "vmnicsToUplinks": [
           { "id": "vmnic1", "uplink": "uplink1" },
           { "id": "vmnic0", "uplink": "uplink2" }
         ],
         "nsxTeamings": [
           {
             "policy": "FAILOVER_ORDER",
             "activeUplinks": ["uplink1"],
             "standByUplinks": ["uplink2"]
           }
         ],
         "lagSpecs": null
       }
     ],
     "sddcManagerSpec": {
       "hostname": "sddcm.evs.example.com",
       "localUserPassword": "<sddc-manager-local-password>",
       "useExistingDeployment": true
     }
   }
   ```

1. Replace the placeholders as described in the following table.


<table>
<thead>
  <tr><th>Placeholder</th><th>Value</th></tr>
</thead>
<tbody>
  <tr><td> <code>&lt;vcf-spec-version&gt;</code> </td><td>A specification version that your VCF Installer supports. For more information, see <b>Version string</b> in the points that follow.</td></tr>
  <tr><td> <code>&lt;esx01-root-password&gt;</code>, <code>&lt;esx02-root-password&gt;</code> </td><td>The ESX root passwords from the Amazon EVS secrets in AWS Secrets Manager.</td></tr>
  <tr><td> <code>&lt;fsx-endpoint-ip&gt;</code> </td><td>The endpoint IP address of the file system. For more information, see <a href="config-fsx-openzfs-datastore.md#fsx-openzfs-endpoint">Get the endpoint IP address</a>.</td></tr>
  <tr><td> <code>&lt;vm-management-vlan-id&gt;</code>, <code>&lt;vmotion-vlan-id&gt;</code>, <code>&lt;vtep-vlan-id&gt;</code> </td><td>The VLAN IDs from the <code>list-environment-vlans</code> output. Keep the quotation marks around the values.</td></tr>
  <tr><td> <code>&lt;primary-node-type&gt;</code> </td><td>The value that the VCF Installer API defines for the primary VCF Operations node. For the value of <code>nodes.type</code>, see <a href="https://developer.broadcom.com/xapis/vcf-installer-api/latest/data-structures/VcfOperationsSpec">VcfOperationsSpec</a> in the VCF Installer API reference.</td></tr>
  <tr><td> <code>&lt;sddc-manager-local-password&gt;</code> </td><td>The local user password that you entered for the VCF Installer OVA.</td></tr>
  <tr><td>All other passwords</td><td>Passwords that you choose. For the rules, see <a href="vcf-installer-settings.md">VCF Installer settings for Amazon EVS</a>.</td></tr>
</tbody>
</table>


The following points apply to this specification.

Uplinks  
An r7i.metal-24xl host has the following uplinks.  


<table>
<thead>
  <tr><th>Instance type</th><th>Elastic Network Adapter uplinks</th><th>Speed</th></tr>
</thead>
<tbody>
  <tr><td> <code>r7i.metal-24xl</code> </td><td> <code>vmnic0</code>, <code>vmnic1</code> </td><td>37.5 Gbps each</td></tr>
</tbody>
</table>

 `vmnic0` is the uplink of the standard switch `vSwitch0`, and `vmnic1` is unused. Map `vmnic1` to `uplink1` and `vmnic0` to `uplink2` in `vmnicsToUplinks`, as in the example. The VCF Installer moves `vmnic0` from `vSwitch0` to the distributed switch. Use only these two uplinks.  
If you use r7i.metal-48xl, check the adapter names and speeds in the VMware Host Client before you fill in `vmnicsToUplinks`.

No vSAN  
The `datastoreSpec` contains only `nfsDatastoreSpec`, and the `networks` list of the distributed switch has no vSAN network. The specification has no `vsanSpec` and no reference to local devices.

NFS network  
You must declare a network of type `NFS` in `networkSpecs` and in the `networks` list of the distributed switch. The following rules apply to the NFS network.  
+ If the NFS network is missing, the VCF Installer rejects the specification with the errors `MISSING_NET_SPEC_ENTRY` and `MISSING_DVS_SPEC_NET_ENTRY`.
+ Declare the NFS network on the host management subnet, as in the example.
+ Give the NFS network an address range in `includeIpAddressRanges`, with at least one address for each host. The Installer assigns each host one address from this range. Without the range, the Installer reports `NOT_ENOUGH_IPS` and `MISSING_INCLUSION_RANGE`.
+ The datastore stays mounted through `vmk0`, and `enableBindToVmknic` is `false`.

Version string  
Replace `<vcf-spec-version>` with a specification version that your VCF Installer supports. The `version` field of the specification is described in [SddcSpec](https://developer.broadcom.com/xapis/vcf-installer-api/latest/data-structures/SddcSpec) in the VCF Installer API reference. Don’t enter a build number. If the version isn’t supported, the Installer rejects the specification and lists the specification versions that it supports.

Cluster EVC mode  
The example sets the Enhanced vMotion Compatibility (EVC) mode of the cluster, `clusterEvcMode`, to `INTEL_SAPPHIRERAPIDS`. The VCF Installer doesn’t apply this value, so you set the mode after deployment, as described in [Set the cluster EVC mode](#getting-started-diskless-evc).

NTP servers  
The example uses `time.aws.com`. The diskless hosts use the link-local Amazon Time Sync Service address `169.254.169.123` as their NTP source. Validation reports the NTP warnings that [Validate and deploy](#getting-started-diskless-deploy) lists, and you can acknowledge them.

Skipped validation checks  
The example sets `skipEsxThumbprintValidation` and `skipGatewayPingValidation` to `true`. For more information, see [VCF Installer settings for Amazon EVS](vcf-installer-settings.md).

Appliance sizes  
The example uses one NSX Manager node of size `medium` and the `small` size for the other appliances. The VCF Installer accepts this configuration on two hosts.

## Validate and deploy
<a name="getting-started-diskless-deploy"></a>

Validation checks the specification and deploys nothing.

In the VCF Installer, do the following:

1. Choose **Deploy Using JSON Spec**, and upload your specification file.

1. Review the summary and the JSON preview, and choose **Next**. The Installer validates the specification and shows the results.

1. Resolve any errors, and acknowledge the warnings that you accept.

1. Choose **Deploy**.

Validation of a two-host specification with an NFS principal datastore takes less than 10 minutes and runs 15 checks. Expect 13 checks to pass and two checks to show warnings, with no errors. The following warnings are expected with this configuration.


| Warning | Meaning | 
| --- | --- | 
|  `IP_REACHABLE_ESXI_HOST` for each host | The check pings `time.aws.com`, which doesn’t answer. NTP doesn’t require Internet Control Message Protocol (ICMP) traffic. You can acknowledge it. | 
|  `HOST_NTP_VALIDATION` for each host | The host reads the NTP source `169.254.169.123`, which is the Amazon EVS link-local time source, and the specification uses `time.aws.com`. You can acknowledge it. | 
|  `HOST_NTP_VALIDATION` for the VCF Installer appliance | The `/etc/ntp.conf` file of the appliance holds an Amazon EC2 DNS name that `time.aws.com` resolved to, and the check expects `time.aws.com`. You can acknowledge it. | 

The Installer shows no capacity warning when the datastore is 7,168 GiB. If you provision less capacity, the Installer can advise a larger datastore. For more information, see [Size the file system](config-fsx-openzfs-datastore.md#fsx-openzfs-sizing). If the validation shows errors, see [Troubleshoot Self-deployed deployments](troubleshoot-self-deployed.md).

Deployment of a two-host management domain takes about 4.5 hours. Don’t start a second deployment while one is running.

During deployment, the VCF Installer moves its own appliance from the staging datastore to the principal datastore. This task shows no progress in the VCF Installer for about 35 minutes. You can see it as a `RelocateVM` task in vCenter Server. Don’t treat this pause as a stall.

## Set the cluster EVC mode
<a name="getting-started-diskless-evc"></a>

The VCF Installer doesn’t apply the EVC mode from the specification, so you set it after deployment. To set the mode, do the following.

1. When the VCF Installer reports success, sign in to the vSphere Client as `administrator@vsphere.local` with the password from your specification.

1. Choose the cluster, choose **Configure**, choose **VMware EVC**, and set the mode to **Intel Sapphire Rapids**. The hosts report Intel Sapphire Rapids as their highest EVC mode.

## Verify the result
<a name="getting-started-diskless-verify"></a>

In the vSphere Client, do the following:

1. Confirm that the cluster `EVS-Mgmt-Cluster` shows all hosts as connected, and that vSphere High Availability (HA) and Distributed Resource Scheduler (DRS) are on.

1. Confirm that vSAN isn’t enabled, and that the hosts have no local datastore other than the ESX system volumes.

1. Confirm that the datastore `fsx-principal` holds the management appliances, including the VCF Installer appliance.

1. Confirm that the datastores `fsx-principal` and `fsx-staging` are mounted on all hosts. If a datastore is missing on a host, mount it as in [Prepare the first host](getting-started-diskless.md#getting-started-diskless-prep-host).

1. Create a test virtual machine on the principal datastore, and migrate it between hosts with vMotion in both directions. Because the datastore is shared, vMotion moves only the memory and the state of the virtual machine.

In SDDC Manager, confirm that NFS is the primary datastore type of the cluster.

After deployment, the hosts can show a yellow warning status in vCenter Server. The warning is a vSphere HA configuration issue that says the host couldn’t reach the isolation address. The cluster stays green, and HA and DRS stay on. VCF sets the vSphere HA options `das.ignoreInsufficientHbDatastore` and `das.ignoreRedundantNetWarning` to `true`, so one NFS datastore and one network don’t raise warnings.

You have deployed the VCF management domain on diskless hosts with external storage.

Next step: [Step 5: Configure NSX networking](self-deployed-nsx-edge.md). Then continue with [Step 6: Create connectors](self-deployed-create-connectors.md) and [Step 7: Verify the environment](self-deployed-verify.md).

When you no longer need the environment, see [Clean up a Self-deployed environment](self-deployed-cleanup.md).

**Important**  
Deleting the environment doesn’t delete your external storage. The file system and its volumes continue to incur charges until you delete them.