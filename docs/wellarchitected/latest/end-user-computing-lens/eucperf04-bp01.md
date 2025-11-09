# EUCPERF04-BP01 Evaluate available instance types (AppStream) and hardware bundles

(WorkSpaces)

WorkSpaces Applications groups instances into families, such as General Purpose (stream.standard).
Within each family, there are different instance sizes, such as stream.standard.medium and
stream.standard.large. Each size has a different number of vCPUs and memory. Graphics
optimized families include instances with one or more GPUs. For more information on the
Graphics G4 (stream.graphics.g4dn), Graphics G5 (stream.graphics.g5), and Memory Optimized
(stream.memory.z1d) families, see [Amazon EC2
Instance Types](https://aws.amazon.com/ec2/instance-types/ "https://aws.amazon.com/ec2/instance-types/").

**Level of risk exposed if this best practice is not
established:** Medium

## Implementation guidance

WorkSpaces bundle selection begins with determining if your workload requires a GPU. If it
does, evaluate the Graphics G4 and Graphics G5 families. If it does not require a GPU,
evaluate the General Purpose, Compute Optimized, and Memory Optimized families. In
addition to large amounts of memory, stream.memory.z1d instances offer the highest CPU
clock rates of the WorkSpaces Applications instance family.

WorkSpaces provides hardware bundles with different amounts of vCPUs and memory.
Graphics.G4dn and GraphicsPro.G4dn bundles include GPUs.

For specifications and recommended uses cases, see [Amazon WorkSpaces](https://aws.amazon.com/workspaces-family/workspaces/pricing/ "https://aws.amazon.com/workspaces-family/workspaces/pricing/").
