# Use Amazon File Cache with Amazon EC2 instances

Amazon File Cache provides a fully managed, high-speed cache on AWS that makes it easier to process
file data, regardless of where the data is stored. Amazon File Cache serves as a temporary,
high-performance storage location for data that's stored in on-premises file systems, AWS
file systems, and Amazon Simple Storage Service (Amazon S3) buckets. You can use this capability to make dispersed
datasets available to file-based applications on AWS with a unified view, and at high
speeds—sub-millisecond latencies and high throughput. For more information, see the
[Amazon
File Cache User Guide](../../../fsx/latest/FileCacheGuide/what-is.md "../../../fsx/latest/FileCacheGuide/what-is.md").

Amazon File Cache works with the most popular Linux AMIs, and is compatible with x86-based
instance types and Graviton instance types. You can access your cache from your Amazon EC2 instances
using the open-source Lustre client. You can mount your cache and then work with the files and
directories in your cache using standard Linux commands. Amazon EC2 instances can access your cache
from other Availability Zones within the same virtual private cloud (VPC), provided that your
network configuration allows access across subnets within the VPC. You can also create a cache
in a shared VPC.

To get started, see [Getting started with Amazon File Cache](../../../fsx/latest/FileCacheGuide/getting-started.md "../../../fsx/latest/FileCacheGuide/getting-started.md") in the _Amazon File Cache User Guide_.
