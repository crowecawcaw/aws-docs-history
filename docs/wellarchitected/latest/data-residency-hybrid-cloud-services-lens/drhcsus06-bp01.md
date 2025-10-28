# DRHCSUS06-BP01 Monitor Local Zone hardware introductions, and choose the latest EC2 Instances to take advantage of energy efficiency improvements

As new more powerful and efficient Amazon EC2 instance families
are introduced into AWS Local Zones they should be adopted to
reduce the number of EC2 instances used and overall energy
consumption.

**Desired outcome:** You use most
energy efficient and performant Amazon EC2 offerings to deploy
workloads.

**Benefits of establishing this best
practice:** By adopting the latest Amazon EC2 families,
it may be possible to reduce the number of Amazon EC2 instances
needed to support your data-residency workloads.

**Level of risk exposed if this best
practice is not established:** Medium

## Implementation guidance

Monitor
[AWS Local Zones features](https://aws.amazon.com/about-aws/global-infrastructure/localzones/features "https://aws.amazon.com/about-aws/global-infrastructure/localzones/features") to discover the latest generation of
Amazon EC2 instances, and use these whenever possible. New
Amazon EC2 instance types often incorporate energy efficiency
improvements using the latest Intel processor families or
AWS-optimized processor architectures such as
[AWS Graviton](https://aws.amazon.com/ec2/graviton/ "https://aws.amazon.com/ec2/graviton/"). Some of the latest instance types integrate
specialized hardware accelerators such as GPUs or FPGAs to
offload compute-intensive tasks from the CPU, resulting in
overall improved performance per watt. This improved performance
per watt in turn reduces energy consumption to help meet your
sustainability goals and improve performance for data residency
workloads.
