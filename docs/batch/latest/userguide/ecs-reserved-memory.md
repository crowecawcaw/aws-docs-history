# Reserve system memory

If you occupy all of the memory on a compute resource with your jobs, it's possible that your jobs contend with
critical system processes for memory and possibly cause a system failure. The Amazon ECS container agent provides a
configuration variable that's called `ECS_RESERVED_MEMORY`. You can use this configuration variable to
remove a specified number of MiB of memory from the pool that's allocated to your jobs. This effectively reserves
that memory for critical system processes.

The default AWS Batch compute resource AMI reserves 32 MiB of memory for the Amazon ECS container
agent and other critical system processes. We recommend reserving a 5% memory buffer for Amazon ECS container
agent and other critical system processes.
