

# Consume context from a context store

This topic is for developers of security appliances, such as firewalls, and integrations that consume context from a context store. AWS Transit Gateway adds source context identifiers to traffic. The security appliance retrieves context records from the context store to map those identifiers to AWS resources and use the resolved context when enforcing policy.

Before a firewall integration can read the context store, the customer must grant it access. For more information, see [Grant firewall access to a context store](create-context-store.md#grant-context-store-access).

Only source context is included in the traffic.

## Context concepts
<a name="context-store-concepts"></a>

When you consume context from a context store, you work with the following:

Context  
A `ContextEntry` returned by `ListContexts`. A context entry maps a context identifier to an AWS resource or lookup value. Resource entries can represent a VPC, subnet, security group, or transit gateway attachment. Lookup entries map encoded Region, Availability Zone, and attachment type identifiers to their values.

Version  
A version identifier for the context records in one context store. The version changes when the context in the store changes. A consumer tracks the last version that it fully processed.

Context changes  
The net set of context records that were added or removed between a specified version and the current version. Each `ContextChange` contains an `ADDED` or `REMOVED` change type and the affected context entry. Context changes are not an ordered log of events.

## Context fields
<a name="context-entry-fields"></a>

A context entry (`ContextEntry`) can include the following fields. The fields returned depend on the context type.


| Field | Description | 
| --- | --- | 
| ContextId | The opaque identifier that the transit gateway adds to traffic. A security service uses the context store to resolve this identifier. | 
| ContextType | The type of context entry. | 
| SegmentType | The type of network segment for a segment entry. The only segment type is SecurityGroup. | 
| PublicId | The public identifier or value represented by the context entry. | 
| Region | The AWS Region of the resource. | 
| AvailabilityZone | The Availability Zone of the resource, where applicable. | 
| AttachmentType | The transit gateway attachment type of the resource. The possible values are ClientVPN, Connect, DXGW, NetworkFunction, Peering, VPC, VPN, and VPNConcentrator. | 

The context available depends on the attachment type. Traffic from a `VPC` attachment can include attachment, VPC, subnet, and security group context. A non-VPC attachment contributes attachment context and context for its underlying resource, but no subnet or security group context.

Resource context includes up to five security groups. If a resource has more than five security groups, its source context includes no security group context identifiers.

## Consume context from a context store
<a name="context-store-consume-pattern"></a>

A security service consumes context records from a context store as follows:

1. Use the [list-contexts](https://docs.aws.amazon.com/cli/latest/reference/networkmanager/list-contexts.html) command to load the full set of context records. Retrieve all pages, store the records, and record the returned `VersionId` after the full load is complete.

1. Use the [get-context-version](https://docs.aws.amazon.com/cli/latest/reference/networkmanager/get-context-version.html) command periodically to retrieve the current `VersionId`.

1. If the current version differs from the last version that you processed, use the [list-context-changes](https://docs.aws.amazon.com/cli/latest/reference/networkmanager/list-context-changes.html) command. Specify the last processed version as `FromVersionId`, retrieve all pages, and apply the `ADDED` and `REMOVED` records.

1. After all changes are processed, record the `ToVersionId` returned by `ListContextChanges` as the last processed version.

1. Periodically repeat the full `ListContexts` load to reconcile your local copy with the context store.

**Note**  
You can retrieve individual context records only through the Network Manager API or the AWS CLI. The AWS Network Manager console shows context stores and their associations, but not individual context records.