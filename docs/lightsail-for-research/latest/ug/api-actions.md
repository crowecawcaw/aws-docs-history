# Lightsail for Research API actions

You can use the following API actions, which are part of the Lightsail API, to manage
Amazon Lightsail for Research resources. Choose the name of the action to view more
information about that action.

###### Lightsail for Research actions

- [AddOnRequest](../../../lightsail/2016-11-28/api-reference/API_AddOnRequest.md "../../../lightsail/2016-11-28/api-reference/API_AddOnRequest.md") - Describes a request to enable, modify, or disable an
  add-on for an Amazon Lightsail or Lightsail for Research resource. Valid values are
  `AutoSnapshot | StopInstanceOnIdle`.
- [CreateGUISessionAccessDetails](../../../lightsail/2016-11-28/api-reference/API_CreateGUISessionAccessDetails.md "../../../lightsail/2016-11-28/api-reference/API_CreateGUISessionAccessDetails.md") - Creates two URLs that are used to
  access a virtual computer's graphical user interface (GUI) session.
- [GetCostEstimate](../../../lightsail/2016-11-28/api-reference/API_GetCostEstimate.md "../../../lightsail/2016-11-28/api-reference/API_GetCostEstimate.md") - Retrieves information about the cost estimate for a
  specified resource.
- [StartGUISession](../../../lightsail/2016-11-28/api-reference/API_StartGUISession.md "../../../lightsail/2016-11-28/api-reference/API_StartGUISession.md") - Initiates a Amazon DCV GUI session that's used to
  access a virtual computer's operating system or application. The session will be
  active for 1 hour. Use this action to resume the session after it expires.
- [StopGUISession](../../../lightsail/2016-11-28/api-reference/API_StopGUISession.md "../../../lightsail/2016-11-28/api-reference/API_StopGUISession.md") - Terminates a web-based Amazon DCV GUI session that's
  used to access a virtual computer's operating system or application. The session
  will close and any unsaved data will be lost.

###### Virtual computer and instance actions

- [CreateInstances](../../../lightsail/2016-11-28/api-reference/API_CreateInstances.md "../../../lightsail/2016-11-28/api-reference/API_CreateInstances.md") - Creates one or more virtual computers.
- [DeleteInstance](../../../lightsail/2016-11-28/api-reference/API_DeleteInstance.md "../../../lightsail/2016-11-28/api-reference/API_DeleteInstance.md") - Deletes a virtual computer.
- [GetBlueprints](../../../lightsail/2016-11-28/api-reference/API_GetBlueprints.md "../../../lightsail/2016-11-28/api-reference/API_GetBlueprints.md") - Returns the list of available virtual computer
  applications, or blueprints.
- [GetBundles](../../../lightsail/2016-11-28/api-reference/API_GetBundles.md "../../../lightsail/2016-11-28/api-reference/API_GetBundles.md")

* Returns the hardware bundles that you can apply to a virtual computer when you
  create it.

- [GetInstance](../../../lightsail/2016-11-28/api-reference/API_GetInstance.md "../../../lightsail/2016-11-28/api-reference/API_GetInstance.md") - Returns information about a specific virtual computer or
  instance.
- [GetInstanceMetricData](../../../lightsail/2016-11-28/api-reference/API_GetInstanceMetricData.md "../../../lightsail/2016-11-28/api-reference/API_GetInstanceMetricData.md") - Returns the data points for the specified
  virtual computer metric, given an virtual computer name.
- [GetInstances](../../../lightsail/2016-11-28/api-reference/API_GetInstances.md "../../../lightsail/2016-11-28/api-reference/API_GetInstances.md") - Returns information about all Lightsail instances and
  Lightsail for Research virtual computers in the user's account.
- [GetInstanceState](../../../lightsail/2016-11-28/api-reference/API_GetInstanceState.md "../../../lightsail/2016-11-28/api-reference/API_GetInstanceState.md") - Returns the state of a specific virtual computer or
  instance.
- [RebootInstance](../../../lightsail/2016-11-28/api-reference/API_RebootInstance.md "../../../lightsail/2016-11-28/api-reference/API_RebootInstance.md") - Restarts a specific virtual computer.
- [StartInstance](../../../lightsail/2016-11-28/api-reference/API_StartInstance.md "../../../lightsail/2016-11-28/api-reference/API_StartInstance.md") - Starts a specific virtual computer from a stopped
  state. To restart a virtual computer, use the `reboot instance`
  operation.
- [StopInstance](../../../lightsail/2016-11-28/api-reference/API_StopInstance.md "../../../lightsail/2016-11-28/api-reference/API_StopInstance.md") - Stops a specific virtual computer that is currently
  running.
- [UpdateInstanceMetadataOptions](../../../lightsail/2016-11-28/api-reference/API_UpdateInstanceMetadataOptions.md "../../../lightsail/2016-11-28/api-reference/API_UpdateInstanceMetadataOptions.md") - Modifies the virtual computer metadata
  parameters on a running or stopped virtual computer.

###### Disk actions

- [AttachDisk](../../../lightsail/2016-11-28/api-reference/API_AttachDisk.md "../../../lightsail/2016-11-28/api-reference/API_AttachDisk.md")

* Attaches a block storage disk to a running or stopped virtual computer, and
  exposes it to the virtual computer with the specified disk name.

- [CreateDisk](../../../lightsail/2016-11-28/api-reference/API_CreateDisk.md "../../../lightsail/2016-11-28/api-reference/API_CreateDisk.md")

* Creates a block storage disk that can be attached to a virtual computer in the
  same AWS Region.

- [DeleteDisk](../../../lightsail/2016-11-28/api-reference/API_DeleteDisk.md "../../../lightsail/2016-11-28/api-reference/API_DeleteDisk.md")

* Deletes the specified block storage disk.

- [DetachDisk](../../../lightsail/2016-11-28/api-reference/API_DetachDisk.md "../../../lightsail/2016-11-28/api-reference/API_DetachDisk.md")

* Detaches a stopped block storage disk from a virtual computer.

- [GetDisk](../../../lightsail/2016-11-28/api-reference/API_GetDisk.md "../../../lightsail/2016-11-28/api-reference/API_GetDisk.md") -
  Returns information about a specific block storage disk.
- [GetDisks](../../../lightsail/2016-11-28/api-reference/API_GetDisks.md "../../../lightsail/2016-11-28/api-reference/API_GetDisks.md") -
  Returns information about all block storage disks in your AWS account and region.

###### Key pair actions

- [CreateKeyPair](../../../lightsail/2016-11-28/api-reference/API_CreateKeyPair.md "../../../lightsail/2016-11-28/api-reference/API_CreateKeyPair.md") - Creates a custom SSH key pair that you can use with a
  Lightsail for Research virtual computer.
- [DeleteKeyPair](../../../lightsail/2016-11-28/api-reference/API_DeleteKeyPair.md "../../../lightsail/2016-11-28/api-reference/API_DeleteKeyPair.md") - Deletes the specified key pair by removing the public
  key from Amazon Lightsail.
- [DownloadDefaultKeyPair](../../../lightsail/2016-11-28/api-reference/API_DownloadDefaultKeyPair.md "../../../lightsail/2016-11-28/api-reference/API_DownloadDefaultKeyPair.md") - Downloads the regional Lightsail default key
  pair. This action also creates a Lightsail default key pair if a default key pair
  does not currently exist in the AWS Region.
- [GetInstanceAccessDetails](../../../lightsail/2016-11-28/api-reference/API_GetInstanceAccessDetails.md "../../../lightsail/2016-11-28/api-reference/API_GetInstanceAccessDetails.md") - Returns temporary SSH keys you can use to
  connect to a specific virtual computer.
- [GetKeyPair](../../../lightsail/2016-11-28/api-reference/API_GetKeyPair.md "../../../lightsail/2016-11-28/api-reference/API_GetKeyPair.md")

* Returns information about a specific key pair.

- [GetKeyPairs](../../../lightsail/2016-11-28/api-reference/API_GetKeyPairs.md "../../../lightsail/2016-11-28/api-reference/API_GetKeyPairs.md") - Returns information about all key pairs in the user's
  account.
- [ImportKeyPair](../../../lightsail/2016-11-28/api-reference/API_ImportKeyPair.md "../../../lightsail/2016-11-28/api-reference/API_ImportKeyPair.md") - Imports the public SSH key from a specific key
  pair.

###### Networking actions

- [GetInstancePortStates](../../../lightsail/2016-11-28/api-reference/API_GetInstancePortStates.md "../../../lightsail/2016-11-28/api-reference/API_GetInstancePortStates.md") - Returns the firewall port states for a specific
  virtual computer, the IP addresses allowed to connect to the virtual computer
  through the ports, and the protocol.
- [IsVpcPeered](../../../lightsail/2016-11-28/api-reference/API_IsVpcPeered.md "../../../lightsail/2016-11-28/api-reference/API_IsVpcPeered.md") - Returns a Boolean value indicating whether your Lightsail
  VPC is peered.
- [OpenInstancePublicPorts](../../../lightsail/2016-11-28/api-reference/API_OpenInstancePublicPorts.md "../../../lightsail/2016-11-28/api-reference/API_OpenInstancePublicPorts.md") - Opens ports for a specific virtual computer,
  and specifies the IP addresses allowed to connect to the virtual computer through
  the ports, and the protocol.
- [PutInstancePublicPorts](../../../lightsail/2016-11-28/api-reference/API_PutInstancePublicPorts.md "../../../lightsail/2016-11-28/api-reference/API_PutInstancePublicPorts.md") - Opens ports for a specific virtual computer,
  and specifies the IP addresses allowed to connect to the virtual computer through
  the ports, and the protocol.
- [PeerVpc](../../../lightsail/2016-11-28/api-reference/API_PeerVpc.md "../../../lightsail/2016-11-28/api-reference/API_PeerVpc.md") -
  Peers the Lightsail VPC with the user's default VPC.
- [SetIpAddressType](../../../lightsail/2016-11-28/api-reference/API_SetIpAddressType.md "../../../lightsail/2016-11-28/api-reference/API_SetIpAddressType.md") - Sets the IP address type for a virtual
  computer.
- [UnpeerVpc](../../../lightsail/2016-11-28/api-reference/API_UnpeerVpc.md "../../../lightsail/2016-11-28/api-reference/API_UnpeerVpc.md") -
  Unpeers the Lightsail VPC from the user's default VPC.

###### Snapshot actions

- [CopySnapshot](../../../lightsail/2016-11-28/api-reference/API_CopySnapshot.md "../../../lightsail/2016-11-28/api-reference/API_CopySnapshot.md") - Copies a manual snapshot of an virtual computer or disk
  as another manual snapshot, or copies an automatic snapshot of an virtual computer
  or disk as a manual snapshot.
- [CreateDiskFromSnapshot](../../../lightsail/2016-11-28/api-reference/API_CreateDiskFromSnapshot.md "../../../lightsail/2016-11-28/api-reference/API_CreateDiskFromSnapshot.md") - Creates a block storage disk from a manual or
  automatic snapshot of a disk.
- [CreateDiskSnapshot](../../../lightsail/2016-11-28/api-reference/API_CreateDiskSnapshot.md "../../../lightsail/2016-11-28/api-reference/API_CreateDiskSnapshot.md") - Creates a snapshot of a block storage disk.
- [CreateInstancesFromSnapshot](../../../lightsail/2016-11-28/api-reference/API_CreateInstancesFromSnapshot.md "../../../lightsail/2016-11-28/api-reference/API_CreateInstancesFromSnapshot.md") - Creates one or more new virtual computers
  from a manual or automatic snapshot of a virtual computer.
- [CreateInstanceSnapshot](../../../lightsail/2016-11-28/api-reference/API_CreateInstanceSnapshot.md "../../../lightsail/2016-11-28/api-reference/API_CreateInstanceSnapshot.md") - Creates a snapshot of a specific virtual
  computer.
- [DeleteAutoSnapshot](../../../lightsail/2016-11-28/api-reference/API_DeleteAutoSnapshot.md "../../../lightsail/2016-11-28/api-reference/API_DeleteAutoSnapshot.md") - Deletes an automatic snapshot of a virtual
  computer or disk.
- [DeleteDiskSnapshot](../../../lightsail/2016-11-28/api-reference/API_DeleteDiskSnapshot.md "../../../lightsail/2016-11-28/api-reference/API_DeleteDiskSnapshot.md") - Deletes a specific snapshot of a disk.
- [DeleteInstanceSnapshot](../../../lightsail/2016-11-28/api-reference/API_DeleteInstanceSnapshot.md "../../../lightsail/2016-11-28/api-reference/API_DeleteInstanceSnapshot.md") - Deletes a specific snapshot of a virtual
  computer.
- [ExportSnapshot](../../../lightsail/2016-11-28/api-reference/API_ExportSnapshot.md "../../../lightsail/2016-11-28/api-reference/API_ExportSnapshot.md") - Exports a virtual computer or block storage disk
  snapshot to Amazon Elastic Compute Cloud (Amazon EC2).
- [GetDiskSnapshot](../../../lightsail/2016-11-28/api-reference/API_GetDiskSnapshot.md "../../../lightsail/2016-11-28/api-reference/API_GetDiskSnapshot.md") - Returns information about a specific block storage
  disk snapshot.
- [GetDiskSnapshots](../../../lightsail/2016-11-28/api-reference/API_GetDiskSnapshots.md "../../../lightsail/2016-11-28/api-reference/API_GetDiskSnapshots.md") - Returns information about all block storage disk
  snapshots in your AWS account and region.
- [GetExportSnapshotRecords](../../../lightsail/2016-11-28/api-reference/API_GetExportSnapshotRecords.md "../../../lightsail/2016-11-28/api-reference/API_GetExportSnapshotRecords.md") - Returns all export snapshot records created
  as a result of the export snapshot operation.
- [GetInstanceSnapshot](../../../lightsail/2016-11-28/api-reference/API_GetInstanceSnapshot.md "../../../lightsail/2016-11-28/api-reference/API_GetInstanceSnapshot.md") - Returns information about a specific virtual
  computer snapshot.
- [GetInstanceSnapshots](../../../lightsail/2016-11-28/api-reference/API_GetInstanceSnapshots.md "../../../lightsail/2016-11-28/api-reference/API_GetInstanceSnapshots.md") - Returns all virtual computer snapshots for the
  user's account.

###### Tag actions

- [TagResource](../../../lightsail/2016-11-28/api-reference/API_TagResource.md "../../../lightsail/2016-11-28/api-reference/API_TagResource.md") - Adds one or more tags to the specified resource.
- [UntagResource](../../../lightsail/2016-11-28/api-reference/API_UntagResource.md "../../../lightsail/2016-11-28/api-reference/API_UntagResource.md") - Deletes the specified set of tag keys and their values
  from the specified resource.

###### Additional resource actions

- [GetActiveNames](../../../lightsail/2016-11-28/api-reference/API_GetActiveNames.md "../../../lightsail/2016-11-28/api-reference/API_GetActiveNames.md") - Returns the names of all active (not deleted)
  resources.
- [GetOperation](../../../lightsail/2016-11-28/api-reference/API_GetOperation.md "../../../lightsail/2016-11-28/api-reference/API_GetOperation.md") - Returns information about a specific operation.
  Operations include events such as when you create a virtual computer, attach a disk,
  and so on.
- [GetOperations](../../../lightsail/2016-11-28/api-reference/API_GetOperations.md "../../../lightsail/2016-11-28/api-reference/API_GetOperations.md") - Returns information about all operations. Results are
  returned from oldest to newest, up to a maximum of 200. Results can be paged by
  making each subsequent call to `GetOperations` use the maximum (last)
  `statusChangedAt` value from the previous request.
- [GetOperationsForResource](../../../lightsail/2016-11-28/api-reference/API_GetOperationsForResource.md "../../../lightsail/2016-11-28/api-reference/API_GetOperationsForResource.md") - Gets operations for a specific resource,
  such as a virtual computer or a disk.
- [GetRegions](../../../lightsail/2016-11-28/api-reference/API_GetRegions.md "../../../lightsail/2016-11-28/api-reference/API_GetRegions.md")

* Returns a list of all valid AWS Regions for Lightsail. Use the `include
availability zones` parameter to also return the Availability Zones in a
  region.
