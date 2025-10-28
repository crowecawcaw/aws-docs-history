# EUCPERF05-BP04 Use instance storage when available and appropriate

An instance store provides temporary block-level storage for your instance. This
storage is located on disks that are physically attached to the host computer. Instance
store is ideal for temporary storage of information that changes frequently, such as
buffers, caches, scratch data, and other temporary content.

For AppStream 2.0, the Graphics G4, Graphics G5, and Memory Optimized
(stream.memory.z1d) instance families include NVMe instance storage volumes. For further
information related to the instance storage volumes and initializing, see [Instance store
temporary block storage for EC2 instances](../../../AWSEC2/latest/WindowsGuide/InstanceStorage.md "../../../AWSEC2/latest/WindowsGuide/InstanceStorage.md").

For WorkSpaces, the graphics.g4dn and GraphicsPro.G4dn bundles provide NVMe instance storage
volumes.

**Level of risk exposed if this best practice is not
established:** Low

## Implementation guidance

Use the local instance store on instances that support it to optimize the performance
of end user applications. When doing so, consider that the instance store is not backed up
and should only be used to satisfy temporary storage requirements. See [Local Instance Store for GPU-enabled Bundles](https://aws.amazon.com/workspaces/features/#Local_Instance_Store_for_GPU-enabled_Bundles "https://aws.amazon.com/workspaces/features/#Local_Instance_Store_for_GPU-enabled_Bundles") for more information.
