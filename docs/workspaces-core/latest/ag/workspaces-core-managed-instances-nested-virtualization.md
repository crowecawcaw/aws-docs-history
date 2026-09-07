

# Enable nested virtualization on Amazon WorkSpaces Core Managed Instances
<a name="workspaces-core-managed-instances-nested-virtualization"></a>

With nested virtualization, you can run hypervisors such as KVM and Hyper-V inside your Amazon WorkSpaces Core Managed Instance. Use these hypervisors to create and manage virtual machines within the instance. You can use nested virtualization for development tools such as Docker Desktop, Windows Subsystem for Linux 2 (WSL2), Android Studio emulators, and QEMU.

Amazon WorkSpaces Core Managed Instances support Amazon EC2 nested virtualization. For information about the Nitro hypervisor architecture, the L0/L1/L2 layers, and supported L1 hypervisors, see the [Amazon EC2 nested virtualization documentation](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/amazon-ec2-nested-virtualization.html).

**Topics**
+ [Prerequisites](#nv-prerequisites)
+ [Enable nested virtualization](#nv-enable-nested-virtualization)
+ [Considerations](#nv-considerations)
+ [Troubleshooting](#nv-troubleshooting)
+ [Related resources](#nv-related-resources)

## Prerequisites
<a name="nv-prerequisites"></a>

Before enabling nested virtualization, ensure the following:
+ **Supported instance type** – The instance type must be supported by both Amazon WorkSpaces Core Managed Instances (see [Using Amazon WorkSpaces Managed Instances](partner-admin-guides.md#workspaces-core-managed-instances)) and Amazon EC2 nested virtualization. For the full list of Amazon EC2-supported types, see [EC2 nested virtualization supported instance types](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/amazon-ec2-nested-virtualization.html).
+ **Region availability** – Nested virtualization for Amazon WorkSpaces Core Managed Instances is available only in supported commercial AWS Regions.
+ **IAM permissions** – You must have permissions to call `CreateWorkspaceInstance`.
+ **AMI compatibility** – Your AMI's guest operating system must support nested virtualization in-guest. For more information, see [No AMI/OS validation](#nv-no-ami-os-validation).

## Enable nested virtualization
<a name="nv-enable-nested-virtualization"></a>

You can enable nested virtualization only at instance creation. When you create a Amazon WorkSpaces Core Managed Instance, set `CpuOptions.NestedVirtualization` to `enabled` in the `CreateWorkspaceInstance` request. The valid values are `enabled` and `disabled`. If you omit `NestedVirtualization`, it defaults to `disabled`. For more information, see [CpuOptionsRequest](https://docs.aws.amazon.com/workspaces-instances/latest/api/API_CpuOptionsRequest.html) in the *Amazon WorkSpaces Instances API Reference*.

**Important**  
Unlike Amazon EC2, Amazon WorkSpaces Core Managed Instances do **not** support modifying CPU options after creation. You cannot enable or disable nested virtualization on an existing Amazon WorkSpaces Core Managed Instance. To change this setting, delete the instance and create a new one.

### Example request payload
<a name="nv-example-request-payload"></a>

Save the following to a file (for example, `/tmp/create-nv.json`):

```
{
  "ManagedInstance": {
    "ImageId": "ami-0abcdef1234567890",
    "InstanceType": "m7i.large",
    "SubnetId": "subnet-0example1234",
    "SecurityGroupIds": ["sg-0example5678"],
    "CpuOptions": {
      "NestedVirtualization": "enabled"
    },
    "TagSpecifications": [
      {
        "ResourceType": "instance",
        "Tags": [
          {"Key": "Name", "Value": "my-nv-workspace"}
        ]
      }
    ]
  },
  "BillingConfiguration": {
    "BillingMode": "MONTHLY"
  }
}
```

### AWS CLI
<a name="nv-enable-nested-virtualization-cli"></a>

```
aws workspaces-instances create-workspace-instance \
  --region us-west-2 \
  --cli-input-json file:///tmp/create-nv.json
```

### Verify nested virtualization is enabled
<a name="nv-verify-nested-virtualization"></a>

After the instance reaches the `ALLOCATED` state, use `GetWorkspaceInstance` to confirm:

```
aws workspaces-instances get-workspace-instance \
  --region us-west-2 \
  --workspace-instance-id wsi-0example1234
```

The response includes:

```
{
  "CpuOptions": {
    "NestedVirtualization": "enabled"
  }
}
```

## Considerations
<a name="nv-considerations"></a>

Consider the following when you use nested virtualization on Amazon WorkSpaces Core Managed Instances.

### Launch-time only
<a name="nv-launch-time-only"></a>

You can configure nested virtualization only at instance creation. There is no `ModifyWorkspaceInstance` or equivalent API to change CPU options on an existing instance.

To change the nested virtualization setting, delete the Amazon WorkSpaces Core Managed Instance and create a new one with the desired configuration.

### No AMI/OS validation
<a name="nv-no-ami-os-validation"></a>

Amazon WorkSpaces Core Managed Instances do not validate whether your AMI's guest operating system supports nested virtualization. The instance launches successfully even if the operating system lacks in-guest support for nested virtualization (for example, Windows Server 2016 or Amazon Linux 2).

If you enable nested virtualization on an unsupported operating system:
+ The Amazon EC2 instance launches successfully.
+ The Amazon WorkSpaces Core Managed Instance reaches `ALLOCATED` state.
+ Nested virtualization does not function in-guest.

Verify your operating system supports nested virtualization before enabling this option.

For the operating systems, hypervisors, and other constraints that apply at the Amazon EC2 level, see [Amazon EC2 nested virtualization](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/amazon-ec2-nested-virtualization.html).

### Supported instance types
<a name="nv-supported-instance-types"></a>

Nested virtualization requires an instance type that is supported by **both**:

1. Amazon WorkSpaces Core Managed Instances supported instance types (see [Using Amazon WorkSpaces Managed Instances](partner-admin-guides.md#workspaces-core-managed-instances)).

1. Amazon EC2 nested virtualization supported instance types.

Not all instance types that Amazon WorkSpaces Core Managed Instances support also support Amazon EC2 nested virtualization. If you specify an unsupported type (for example, `c5.large`), the instance is created but transitions to `ERROR_ALLOCATING` state. For more information, see [Troubleshooting](#nv-troubleshooting).

To list the Amazon EC2 instance types that support nested virtualization in a Region, use the following command:

```
aws ec2 describe-instance-types \
  --region us-west-2 \
  --filters Name=processor-info.supported-features,Values=nested-virtualization \
  --query 'InstanceTypes[].InstanceType' \
  --output json
```

### Windows considerations
<a name="nv-windows-considerations"></a>

When nested virtualization is enabled on a Windows instance:
+ **Virtual Secure Mode (VSM)** – Automatically disabled, including Credential Guard.
+ **CPU limit** – Not supported on Windows instances with more than 192 vCPUs.

For details, see the [EC2 nested virtualization documentation](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/amazon-ec2-nested-virtualization.html).

### Security and shared responsibility
<a name="nv-security-shared-responsibility"></a>

When you use nested virtualization on Amazon WorkSpaces Core Managed Instances, responsibility is divided as follows.

**L0** – Physical infrastructure and Nitro hypervisor  
AWS

**Managed-service layer** – Amazon WorkSpaces Core Managed Instances lifecycle, billing, and monitoring  
AWS

**L1** – Guest operating system and any hypervisor you install (KVM, Hyper-V)  
Customer

**L2** – Virtual machines running inside your instance  
Customer

Applications and data within the L1 and L2 layers  
Customer

## Troubleshooting
<a name="nv-troubleshooting"></a>

The following sections describe common issues and their resolutions.

### Instance moves to ERROR\_ALLOCATING after enabling nested virtualization
<a name="nv-troubleshooting-error-allocating"></a>

**Cause:** The specified instance type does not support nested virtualization at the Amazon EC2 level (for example, `c5.large`).

**Resolution:** Call `GetWorkspaceInstance` and check the `EC2InstanceErrors` field. The error message from Amazon EC2 (typically `InvalidParameterCombination`) indicates the instance type does not support nested virtualization. Recreate the instance with a supported instance type.

```
aws workspaces-instances get-workspace-instance \
  --region us-west-2 \
  --workspace-instance-id wsi-0example1234
```

### ValidationException: NESTED\_VIRTUALIZATION\_NOT\_SUPPORTED
<a name="nv-troubleshooting-not-supported-region"></a>

**Cause:** The requested Region does not yet support nested virtualization for Amazon WorkSpaces Core Managed Instances.

**Resolution:** Create the instance in a supported commercial Region, or wait for the feature to become available in your Region.

### ValidationException: Mutual exclusion error
<a name="nv-troubleshooting-mutual-exclusion"></a>

**Cause:** Both `AmdSevSnp` and `NestedVirtualization` are set to `enabled`.

**Resolution:** Choose one or the other. These options are mutually exclusive.

### Nested virtualization not working in-guest
<a name="nv-troubleshooting-not-working-in-guest"></a>

**Cause:** The AMI's guest operating system does not support nested virtualization (for example, Windows Server 2016 or Amazon Linux 2).

**Resolution:** Use an operating system version that supports nested virtualization in-guest. Amazon WorkSpaces Core Managed Instances do not validate operating system compatibility at launch time.

## Related resources
<a name="nv-related-resources"></a>

Use the following resources to learn more about nested virtualization concepts, supported instance types, and the relevant API operations.
+ [Amazon EC2 nested virtualization](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/amazon-ec2-nested-virtualization.html) – Background, architecture, supported hypervisors, and considerations at the Amazon EC2 level.
+ Amazon WorkSpaces Core Managed Instances supported instance types (see [Using Amazon WorkSpaces Managed Instances](partner-admin-guides.md#workspaces-core-managed-instances)).
+ [CreateWorkspaceInstance API reference](https://docs.aws.amazon.com/workspaces-instances/latest/api/API_CreateWorkspaceInstance.html).
+ [CpuOptionsRequest](https://docs.aws.amazon.com/workspaces-instances/latest/api/API_CpuOptionsRequest.html) – The CPU options data type, including the `NestedVirtualization` values.
+ [GetWorkspaceInstance API reference](https://docs.aws.amazon.com/workspaces-instances/latest/api/API_GetWorkspaceInstance.html).