

# Troubleshoot Self-deployed deployments

Use the following sections to fix problems in Self-deployed environments that run VMware Cloud Foundation (VCF) 9.x, from environment creation through VCF bringup and NSX Edge configuration. Some symptoms are specific to diskless hosts. For status checks, host operations, and VPC networking, see [Troubleshoot environment status checks](troubleshoot-status-checks.md), [Troubleshoot hosts](troubleshoot-hosts.md), and [Troubleshoot networking](troubleshoot-networking.md).

In Self-deployed mode, Amazon Elastic VMware Service doesn’t manage the VCF installation.

## Environment, host, and connector symptoms
<a name="troubleshoot-sd-env-host"></a>

These symptoms occur when you create an environment, add hosts, or create connectors.

### `create-environment` returns a `ValidationException` that names a parameter
<a name="troubleshoot-sd-validation-exception"></a>

The error names a parameter such as `licenseInfo`, `hosts`, `vcfHostnames`, `siteId`, or `connectivityInfo`.

 **Cause** 

These parameters aren’t supported when `vcfVersion` is `SELF_DEPLOYED`.

 **Solution** 

Remove the parameter that the error names from your request, and run the command again. For the request, see [Step 1: Create the environment](self-deployed-create-env.md).

### The environment stays in the `CREATING` state longer than expected
<a name="troubleshoot-sd-env-creating"></a>

 **Cause** 

The environment creation didn’t complete, and the cause isn’t visible in your account.

 **Solution** 

Open a support case with AWS Support, and include the environment ID.

### `create-environment-host` fails with an ESX version error
<a name="troubleshoot-sd-esx-version"></a>

 **Cause** 

The ESX version string in the request is wrong, or your account doesn’t have access to the requested version.

 **Solution** 

1. Get the version strings that are available to you with `aws evs get-versions --region <region-code>`. Replace `<region-code>` with the Region where you created the environment.

1. Run `create-environment-host` again with a version string from the output.

For more information, see [Supported VCF versions and instance types](versions-provided.md) and [Step 3: Add hosts](self-deployed-add-hosts.md).

### A host stays in the `CREATING` state or moves to `CREATE_FAILED`
<a name="troubleshoot-sd-host-stuck"></a>

A host usually reaches the `CREATED` state in about 9 minutes.

 **Cause** 

A likely cause is a missing or incorrect DNS record for the host.

 **Solution** 

1. Verify that a forward (A) record and a reverse (PTR) record exist for the host.

1. From an instance in the VPC, query each DNS server in your VPC DHCP option set for the forward and the reverse record. For example, run `nslookup <host-fqdn> <dns-server-ip>` and `nslookup <host-ip-address> <dns-server-ip>`.

1. Make sure that the IP address in the A record is inside the host management (`vmkManagement`) VLAN subnet, and that the FQDN is 62 characters or fewer.

1. If you use Route 53, make sure that the record changes are in sync.

1. Check the host state again after you fix a record. Don’t run `create-environment-host` again for the same host name while the host exists.

After you fix the records, the host reaches the `CREATED` state. If the records resolve correctly and the host stays in the same state, contact AWS Support and include the environment ID and the host name. For the DNS requirements, see [Step 2: Create DNS records](self-deployed-host-dns-records.md).

### `create-environment-connector` fails with a Secrets Manager access error
<a name="troubleshoot-sd-connector-secret"></a>

 **Cause** 

Amazon EVS can’t read the AWS Secrets Manager secret, because the secret or its AWS KMS key doesn’t carry the required tag.

 **Solution** 

Confirm that the secret and its AWS KMS encryption key are both tagged with `EvsAccess=true`, and create the connector again. For more information, see [Step 6: Create connectors](self-deployed-create-connectors.md).

### The connector is `ACTIVE`, but its reachability check stays `FAILED`
<a name="troubleshoot-sd-connector-reachability"></a>

Connector creation doesn’t validate reachability or credentials. Within 10 minutes after the connector reaches `ACTIVE`, the reachability check changes from `UNKNOWN` to `PASSED` or `FAILED`.

 **Cause** 

Amazon EVS can’t resolve the appliance FQDN, can’t reach the appliance, or can’t sign in with the stored credentials.

 **Solution** 

1. Confirm that the appliance FQDN resolves from the service access subnet through the DNS servers in your DHCP option set.

1. Confirm that the credentials in the Secrets Manager secret are current. If they changed, update the secret. For more information, see [Update a connector](evs-env-update-connector.md).

1. Confirm that your network ACL rules allow traffic between the service access subnet and the appliance.

For more information, see [Monitor environment status](evs-env-status-check.md) and [Troubleshoot networking](troubleshoot-networking.md).

## VCF Installer and bringup symptoms
<a name="troubleshoot-sd-installer"></a>

These symptoms occur when you validate the deployment specification or run VCF bringup.

### The gateway ping validation fails
<a name="troubleshoot-sd-gateway-ping"></a>

 **Cause** 

Amazon EVS VLAN subnet gateways don’t respond to ICMP ping from outside the subnet. The check fails even when routing is correct.

 **Solution** 

In a specification file, set `skipGatewayPingValidation` to `true`. In the VCF Installer wizard, acknowledge the failed gateway ping check and continue. For more information, see [VCF Installer settings for Amazon EVS](vcf-installer-settings.md).

### The ESX host thumbprint validation fails
<a name="troubleshoot-sd-thumbprint"></a>

 **Cause** 

The specification doesn’t contain the correct thumbprints for the hosts.

 **Solution** 

In a specification file, set `skipEsxThumbprintValidation` to `true`, or get the correct thumbprints for all hosts and enter them in the specification. In the wizard, thumbprint validation is mandatory. Review and accept the thumbprint at the hosts step to continue. For more information, see [VCF Installer settings for Amazon EVS](vcf-installer-settings.md).

### VCF bringup fails
<a name="troubleshoot-sd-bringup-fails"></a>

 **Cause** 

A setting in the deployment specification doesn’t match the Amazon EVS network, or a VCF component fails.

 **Solution** 

1. Compare your specification with the settings in [VCF Installer settings for Amazon EVS](vcf-installer-settings.md). When you run bringup through the VCF Installer wizard, the wizard shows validation problems more clearly than the API.

1. Compare your specification with an example that the [spec-generator tool](https://github.com/aws/solutions-for-amazon-evs/tree/main/Deploy/EVS-Deployment-Orchestrator/spec-generator) generates, in the `Deploy` folder of the [Solutions for Amazon EVS](https://github.com/aws/solutions-for-amazon-evs) repository on GitHub.

1. If bringup still fails, contact AWS Support. For VCF-specific requests, you can also contact Broadcom with your Broadcom support entitlement.

For the bringup procedure, see [Step 4b (local storage): Run VCF bringup](sd-install-bringup.md). On diskless hosts, validation reports NTP warnings that you can acknowledge. For the list, see [Validate and deploy](deploy-diskless-spec.md#getting-started-diskless-deploy).

## NSX Edge and BGP symptoms
<a name="troubleshoot-sd-nsx"></a>

To check BGP peering, see [Verify BGP peering](self-deployed-nsx-edge.md#sd-nsx-verify).

### The BGP session stays in the `Active` state
<a name="troubleshoot-sd-bgp-active"></a>

 **Cause** 

A firewall or a network ACL blocks TCP port 179.

 **Solution** 

Verify that your network ACL allows TCP 179 between the Edge uplink IP addresses and the route server endpoint IP addresses. Also verify that the security group of the route server endpoints allows inbound TCP 179. For more information, see [Step 5: Configure NSX networking](self-deployed-nsx-edge.md).

### The BGP session flaps repeatedly
<a name="troubleshoot-sd-bgp-flaps"></a>

 **Cause** 

The MTU doesn’t match along the uplink path.

 **Solution** 

Make sure that the MTU is consistent along the NSX uplink path. The NSX uplink network uses MTU 1500. The overlay (TEP) networks use MTU 8500. For more information, see [Step 5: Configure NSX networking](self-deployed-nsx-edge.md).

### NSX overlay routes don’t appear in the VPC route table
<a name="troubleshoot-sd-bgp-routes"></a>

 **Cause** 

Route server propagation isn’t turned on for the route table, or the route table has no explicit subnet association.

 **Solution** 

Turn on route server propagation for the target route table, and make sure that the route table has at least one explicit subnet association. For more information, see [Troubleshoot networking](troubleshoot-networking.md).

### Only one BGP session is up
<a name="troubleshoot-sd-bgp-one-sided"></a>

 **Cause** 

One Edge node can’t reach both route server endpoints.

 **Solution** 

Verify that both Edge nodes can reach both route server endpoints. We recommend four route server peers in a full mesh, so that routes keep propagating when one endpoint is in maintenance. For more information, see [Set up VPC Route Server and on-premises connectivity](network-route-server.md).

## Diskless host symptoms
<a name="troubleshoot-diskless"></a>

These symptoms apply to environments with diskless hosts, which use NFS principal storage. Diskless hosts are available only with VCF 9.x. For the deployment procedure, see [Step 4a (diskless): Prepare diskless hosts and the VCF Installer](getting-started-diskless.md).

### A diskless host doesn’t finish creation
<a name="troubleshoot-diskless-host-stuck"></a>

The host stays in the `CREATING` state or moves to `CREATE_FAILED`. The cause and the solution are the same as for hosts with local storage. For the steps, see [A host stays in the `CREATING` state or moves to `CREATE_FAILED`](#troubleshoot-sd-host-stuck).

### The VCF Installer rejects the deployment specification
<a name="troubleshoot-diskless-spec"></a>

The VCF Installer validation fails for an environment with NFS principal storage and no vSAN.

 **Cause** 

The specification is missing an entry that an NFS principal datastore needs, or it uses a wrong value.

 **Solution** 

Check the error against the following table. The columns show the result that the VCF Installer reports and the solution.


| Result | Solution | 
| --- | --- | 
|  `MISSING_NET_SPEC_ENTRY` or `MISSING_DVS_SPEC_NET_ENTRY`  | Add an `NFS` network to `networkSpecs`, and add `NFS` to the `networks` list of the distributed switch. Declare it on the host management subnet. | 
|  `NOT_ENOUGH_IPS` or `MISSING_INCLUSION_RANGE`  | Add an `includeIpAddressRanges` entry to the `NFS` network. | 
| Release version is not compatible with the supported versions | Use one of the version strings from the list in the error message, and not a build number. | 
| Datastore not found on the host | Mount the principal datastore on the first host before you validate, and use the same server and path as in the specification. See [The NFS datastore doesn’t mount](#troubleshoot-diskless-mount). | 
| Capacity warning for the datastore | See [The VCF Installer reports insufficient datastore capacity](#troubleshoot-diskless-capacity). | 

For the specification, see [Create the deployment specification](deploy-diskless-spec.md#getting-started-diskless-spec). For the warnings that you can acknowledge, see [Validate and deploy](deploy-diskless-spec.md#getting-started-diskless-deploy).

### The NFS datastore doesn’t mount
<a name="troubleshoot-diskless-mount"></a>

Mounting the Amazon FSx for OpenZFS datastore on an ESX host fails. For example, the Host Client or the host log reports that the mount request was denied.

 **Cause** 

A mount request that the server denies usually means that the host management subnet is missing from the NFS export list. A security group or network ACL that blocks NFS traffic also stops the mount.

 **Solution** 

1. Make sure that the NFS export list of the volume includes the CIDR block of the host management VLAN subnet, with the options `rw,crossmnt,no_root_squash`.

1. Make sure that the security group of the file system allows the NFS ports from the host management VLAN subnet.

1. If you use a network ACL for the VLAN subnets, make sure that it allows the NFS traffic in both directions.

1. Mount the datastore through the host management VMkernel adapter (`vmk0`).

1. Make sure that the NFS server is the endpoint IP address of the file system and the path is `/fsx/<volume-name>`.

For more information, see [Security group rules](config-fsx-openzfs-datastore.md#fsx-openzfs-security-group) and [article 446573](https://knowledge.broadcom.com/external/article/446573) in the Broadcom knowledge base.

### The VCF Installer reports insufficient datastore capacity
<a name="troubleshoot-diskless-capacity"></a>

Validation reports that the datastore capacity is less than the required capacity, or recommends a larger capacity to stay under 80 percent utilization.

 **Cause** 

The datastore size that the ESX host reports is the capacity of the file system, or the quota of the volume if you set one.

 **Solution** 

1. Increase the capacity of the file system, and then raise the quota of the volume if you set one.

1. If you haven’t deployed VCF yet, unmount the datastore from the host and mount it again, so that the host reads the new size.

For the steps and for the limits after VCF is deployed, see [Increase the capacity](config-fsx-openzfs-datastore.md#fsx-openzfs-grow). For sizing guidance, see [Size the file system](config-fsx-openzfs-datastore.md#fsx-openzfs-sizing).

### The datastore doesn’t show the new size after a file system increase
<a name="troubleshoot-diskless-size-refresh"></a>

The ESX host or the VCF Installer still shows the old datastore size. A storage rescan doesn’t change it.

 **Cause** 

A volume doesn’t use the new capacity of the file system until you raise its quota. Before VCF is deployed, the host also keeps the size that it read at mount time.

 **Solution** 

Use the solution for insufficient capacity. For the steps, see [The VCF Installer reports insufficient datastore capacity](#troubleshoot-diskless-capacity).

### Creating an FSx for OpenZFS volume fails with a `BadRequest` error
<a name="troubleshoot-diskless-volume-tag"></a>

The `aws fsx create-volume` command fails. The error says that a tag in the request has the same key as a tag on the parent file system but a different value.

 **Cause** 

The file system copies its tags to volumes, and the file system and the volume have `Name` tags with different values.

 **Solution** 

Turn off the option to copy tags to volumes on the file system, and run the command again. The change causes no interruption. For the command, see [Create the file system](config-fsx-openzfs-datastore.md#fsx-openzfs-create-fs).

### The VCF Installer shows an inventory error after the first start
<a name="troubleshoot-diskless-installer-inventory"></a>

You can sign in right after the VCF Installer appliance starts, but the inventory page shows an error. The list of releases is empty until you connect the Broadcom online depot.

 **Cause** 

The VCF Installer has no release information until it connects to the Broadcom online depot.

 **Solution** 

Connect the Broadcom online depot, as described in [Connect the software depot](getting-started-diskless.md#getting-started-diskless-depot). The inventory error might remain after you connect the Broadcom online depot, and it might last more than 30 minutes. The error doesn’t block the connection to the Broadcom online depot, the bundle downloads, or the validation of the specification. Continue with the next step without waiting for the page to clear.

If these steps don’t resolve the problem, see [Get help from AWS Support and Broadcom](get-help.md) for who to contact and what to include in a case.