# Flexible Instance Types

AWS Elastic Disaster Recovery (AWS DRS) uses EC2 Launch Templates to define how each source server will be launched as
an EC2 instance. For each source server, you can define an EC2 instance type that will be used to launch, if
**Instance-type right-sizing** is not activated. However,
you might want to be flexible with the instance type definitions as this can help in certain situations, such as
reducing the risk of not finding enough resources to support recovery which results in an
**Insufficient Capacity Error (ICE)**.

## How it works

Using attribute based instance type selection allows you to specify attributes to define a set of instance
types that can be used to launch an EC2 instance for the source server. These instance types will only
include those that are offered in the AWS Region and Availability Zone specified by the subnet in your
launch template. To learn more about attribute based instance type selection, visit:
[How attribute-based instance type selection works](../../../AWSEC2/latest/UserGuide/ec2-fleet-attribute-based-instance-type-selection.md#ec2fleet-abs-how-it-works "../../../AWSEC2/latest/UserGuide/ec2-fleet-attribute-based-instance-type-selection.md#ec2fleet-abs-how-it-works").

DRS will use EC2 fleets to launch instances using the attribute settings defined in the EC2 launch template. This will apply price
protection to ensure the fleet picks the most cost effective instance types for you. We use the default protection
settings, so we will protect against selecting instance types that are 20% more expensive than the lowest
cost instance type. To learn more about price protection using fleets, visit:
[Price protection](../../../AWSEC2/latest/UserGuide/ec2-fleet-attribute-based-instance-type-selection.md#ec2fleet-abs-price-protection "../../../AWSEC2/latest/UserGuide/ec2-fleet-attribute-based-instance-type-selection.md#ec2fleet-abs-price-protection").

When launching an instance, EC2 fleets will attempt to launch an instance type listed in **Preview matching instance
types**. It will start from the lowest cost instance type. If an instance type has run out of capacity in
the current AWS Region and Availability Zone, EC2 fleets will attempt to launch with another instance type from the list.
It is expected each attempt will take up to a few minutes, so if most of the instance types are not available, it could have an impact on your
[Recovery Time Objective (RTO)](What-is-RTO.md "What-is-RTO.md").

A large and diverse list of possible instance types listed in _Preview matching instance
types_ increases the chances of finding an available instance type.

## How to use

To use this setting, you can modify the **Default launch settings** (editing the **Default EC2 launch template**) or the **Launch settings** of one or more source servers, and edit the **EC2 launch template**.

Modifying the default launch template settings will only apply to servers added after the change. Modifying the settings of existing source servers will apply to the next launch of those servers.

In the **Instance type** section of the page, select **Specify instance type attributes**.

## Attribute selection

These are the attributes that you can set:

- **Number of vCPUs:** Enter the minimum and maximum number of vCPUs for your compute requirements. To indicate no limits, mark the no minimum or no maximum checkboxes.
- **Amount of memory (MiB):** Enter the minimum and maximum amount of memory, in MiB, for your compute requirements. To indicate no limits, mark the no minimum or no maximum checkboxes.
- Expand **Additional instance type attributes** and choose
  **Add attribute** to express your compute requirements
  in more detail. For information about each attribute, see
  [InstanceRequirementsRequest](../../../AWSEC2/latest/APIReference/API_InstanceRequirementsRequest.md "../../../AWSEC2/latest/APIReference/API_InstanceRequirementsRequest.md")
  in the Amazon EC2 API Reference.
  For example, you can set **Allowed instance types** to include additional specific instance types, or alternatively,
  you can use **Excluded instance types** to exclude specific instance types out of the resulting instance
  types. Note that allowed and excluded instance types cannot be specified together. You can also exclude
  instance types by selecting instance types from the **Preview matching instance types** and clicking the
  **Exclude selected instance types**.
- **Preview matching instance types:** You can preview the instance types
  that match the specified attributes. To exclude instance types, you can select the instance types
  you want to exclude from the previewed list of instance types, but only if you did not allow
  instance types, as you can either exclude or allow instance types but not both. You can exclude
  instance types by selecting instance types from the **Preview matching instance
  types** and clicking the **Exclude selected instance types**. If this
  list is empty, try to expand the attribute values to allow more options.

You can use **Allowed instance types** to add most of the supported instance
types to the **Preview matching instance types** list. This way you can create
a limited set of instance types, which may be useful in situations where you are constrained by the instance
type options you can use, and can only use a small list of those.

###### Note

Adding burstable instance types, such as t2 or t3, to the allow attribute will not affect the list in
**Preview matching instance types**. However, if you select a burstable
instance type and update the **EC2 launch template** on the EC2 console by selecting
_Burstable performance support_
from the **Attribute** dropdown, setting the **Attribute value**
to _Include_ (or _Required_), and set the new template version as a default, these
instance types will affect the preview list.

###### Note

You can define attributes directly on the EC2 launch template. If you have defined an attribute
that is not supported on the DRS console, that attribute will still affect the list of instance types
in **Preview matching instance types**, even if the DRS console will not display it.

###### Note

Note: Flexible instance types cannot be used if
**instance type right-right sizing** is active, or if
the subnet selected for launch is on an AWS Outpost rack.
