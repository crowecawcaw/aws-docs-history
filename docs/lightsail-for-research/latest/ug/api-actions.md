

# Lightsail for Research API actions
<a name="api-actions"></a>

You can use the following API actions, which are part of the Lightsail API, to manage Amazon Lightsail for Research resources. Choose the name of the action to view more information about that action.

**Lightsail for Research actions**
+  [AddOnRequest](https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_AddOnRequest.html) - Describes a request to enable, modify, or disable an add-on for an Amazon Lightsail or Lightsail for Research resource. Valid values are `AutoSnapshot | StopInstanceOnIdle`. 
+ [CreateGUISessionAccessDetails](https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_CreateGUISessionAccessDetails.html) - Creates two URLs that are used to access a virtual computer's graphical user interface (GUI) session.
+ [GetCostEstimate](https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_GetCostEstimate.html) - Retrieves information about the cost estimate for a specified resource.
+ [StartGUISession](https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_StartGUISession.html) - Initiates a Amazon DCV GUI session that's used to access a virtual computer's operating system or application. The session will be active for 1 hour. Use this action to resume the session after it expires.
+ [StopGUISession](https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_StopGUISession.html) - Terminates a web-based Amazon DCV GUI session that's used to access a virtual computer's operating system or application. The session will close and any unsaved data will be lost.

**Virtual computer and instance actions**
+ [CreateInstances](https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_CreateInstances.html) - Creates one or more virtual computers.
+ [DeleteInstance](https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_DeleteInstance.html) - Deletes a virtual computer.
+ [GetBlueprints](https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_GetBlueprints.html) - Returns the list of available virtual computer applications, or blueprints.
+ [GetBundles](https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_GetBundles.html) - Returns the hardware bundles that you can apply to a virtual computer when you create it.
+ [GetInstance](https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_GetInstance.html) - Returns information about a specific virtual computer or instance.
+ [GetInstanceMetricData](https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_GetInstanceMetricData.html) - Returns the data points for the specified virtual computer metric, given an virtual computer name.
+ [GetInstances](https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_GetInstances.html) - Returns information about all Lightsail instances and Lightsail for Research virtual computers in the user's account.
+ [GetInstanceState](https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_GetInstanceState.html) - Returns the state of a specific virtual computer or instance.
+ [RebootInstance](https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_RebootInstance.html) - Restarts a specific virtual computer.
+ [StartInstance](https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_StartInstance.html) - Starts a specific virtual computer from a stopped state. To restart a virtual computer, use the `reboot instance` operation.
+ [StopInstance](https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_StopInstance.html) - Stops a specific virtual computer that is currently running.
+ [UpdateInstanceMetadataOptions](https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_UpdateInstanceMetadataOptions.html) - Modifies the virtual computer metadata parameters on a running or stopped virtual computer.

**Disk actions**
+ [AttachDisk](https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_AttachDisk.html) - Attaches a block storage disk to a running or stopped virtual computer, and exposes it to the virtual computer with the specified disk name.
+ [CreateDisk](https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_CreateDisk.html) - Creates a block storage disk that can be attached to a virtual computer in the same AWS Region.
+ [DeleteDisk](https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_DeleteDisk.html) - Deletes the specified block storage disk.
+ [DetachDisk](https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_DetachDisk.html) - Detaches a stopped block storage disk from a virtual computer.
+ [GetDisk](https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_GetDisk.html) - Returns information about a specific block storage disk.
+ [GetDisks](https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_GetDisks.html) - Returns information about all block storage disks in your AWS account and region. 

**Key pair actions**
+ [CreateKeyPair](https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_CreateKeyPair.html) - Creates a custom SSH key pair that you can use with a Lightsail for Research virtual computer.
+ [DeleteKeyPair](https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_DeleteKeyPair.html) - Deletes the specified key pair by removing the public key from Amazon Lightsail.
+ [DownloadDefaultKeyPair](https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_DownloadDefaultKeyPair.html) - Downloads the regional Lightsail default key pair. This action also creates a Lightsail default key pair if a default key pair does not currently exist in the AWS Region.
+ [GetInstanceAccessDetails](https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_GetInstanceAccessDetails.html) - Returns temporary SSH keys you can use to connect to a specific virtual computer.
+ [GetKeyPair](https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_GetKeyPair.html) - Returns information about a specific key pair.
+ [GetKeyPairs](https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_GetKeyPairs.html) - Returns information about all key pairs in the user's account.
+ [ImportKeyPair](https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_ImportKeyPair.html) - Imports the public SSH key from a specific key pair.

**Networking actions**
+ [GetInstancePortStates](https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_GetInstancePortStates.html) - Returns the firewall port states for a specific virtual computer, the IP addresses allowed to connect to the virtual computer through the ports, and the protocol.
+ [IsVpcPeered](https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_IsVpcPeered.html) - Returns a Boolean value indicating whether your Lightsail VPC is peered.
+ [OpenInstancePublicPorts](https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_OpenInstancePublicPorts.html) - Opens ports for a specific virtual computer, and specifies the IP addresses allowed to connect to the virtual computer through the ports, and the protocol.
+ [PutInstancePublicPorts](https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_PutInstancePublicPorts.html) - Opens ports for a specific virtual computer, and specifies the IP addresses allowed to connect to the virtual computer through the ports, and the protocol.
+ [PeerVpc](https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_PeerVpc.html) - Peers the Lightsail VPC with the user's default VPC.
+ [SetIpAddressType](https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_SetIpAddressType.html) - Sets the IP address type for a virtual computer.
+ [UnpeerVpc](https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_UnpeerVpc.html) - Unpeers the Lightsail VPC from the user's default VPC.

**Snapshot actions**
+ [CopySnapshot](https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_CopySnapshot.html) - Copies a manual snapshot of an virtual computer or disk as another manual snapshot, or copies an automatic snapshot of an virtual computer or disk as a manual snapshot.
+ [CreateDiskFromSnapshot](https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_CreateDiskFromSnapshot.html) - Creates a block storage disk from a manual or automatic snapshot of a disk.
+ [CreateDiskSnapshot](https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_CreateDiskSnapshot.html) - Creates a snapshot of a block storage disk.
+ [CreateInstancesFromSnapshot](https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_CreateInstancesFromSnapshot.html) - Creates one or more new virtual computers from a manual or automatic snapshot of a virtual computer.
+ [CreateInstanceSnapshot](https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_CreateInstanceSnapshot.html) - Creates a snapshot of a specific virtual computer.
+ [DeleteAutoSnapshot](https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_DeleteAutoSnapshot.html) - Deletes an automatic snapshot of a virtual computer or disk.
+ [DeleteDiskSnapshot](https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_DeleteDiskSnapshot.html) - Deletes a specific snapshot of a disk.
+ [DeleteInstanceSnapshot](https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_DeleteInstanceSnapshot.html) - Deletes a specific snapshot of a virtual computer.
+ [ExportSnapshot](https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_ExportSnapshot.html) - Exports a virtual computer or block storage disk snapshot to Amazon Elastic Compute Cloud (Amazon EC2).

  
+ [GetDiskSnapshot](https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_GetDiskSnapshot.html) - Returns information about a specific block storage disk snapshot. 
+ [GetDiskSnapshots](https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_GetDiskSnapshots.html) - Returns information about all block storage disk snapshots in your AWS account and region.
+ [GetExportSnapshotRecords](https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_GetExportSnapshotRecords.html) - Returns all export snapshot records created as a result of the export snapshot operation.
+ [GetInstanceSnapshot](https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_GetInstanceSnapshot.html) - Returns information about a specific virtual computer snapshot.
+ [GetInstanceSnapshots](https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_GetInstanceSnapshots.html) - Returns all virtual computer snapshots for the user's account.

**Tag actions**
+ [TagResource](https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_TagResource.html) - Adds one or more tags to the specified resource.
+ [UntagResource](https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_UntagResource.html) - Deletes the specified set of tag keys and their values from the specified resource.

**Additional resource actions**
+ [GetActiveNames](https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_GetActiveNames.html) - Returns the names of all active (not deleted) resources.
+ [GetOperation](https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_GetOperation.html) - Returns information about a specific operation. Operations include events such as when you create a virtual computer, attach a disk, and so on.
+ [GetOperations](https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_GetOperations.html) - Returns information about all operations. Results are returned from oldest to newest, up to a maximum of 200. Results can be paged by making each subsequent call to `GetOperations` use the maximum (last) `statusChangedAt` value from the previous request.
+ [GetOperationsForResource](https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_GetOperationsForResource.html) - Gets operations for a specific resource, such as a virtual computer or a disk.
+ [GetRegions](https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_GetRegions.html) - Returns a list of all valid AWS Regions for Lightsail. Use the `include availability zones` parameter to also return the Availability Zones in a region.