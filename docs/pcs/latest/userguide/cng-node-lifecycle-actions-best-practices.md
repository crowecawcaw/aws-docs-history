# Best practices for node lifecycle actions in AWS PCS

Follow these best practices when you use node lifecycle actions.

- **Test crawl-walk-run.** Verify scripts on a standalone Amazon EC2
  instance, then as a lifecycle action on a compute node group with a single static instance
  (`minInstanceCount` = `maxInstanceCount` = 1), then with dynamic
  scaling.
- **Choose the right `executionPolicy`.** Leave
  one-time setup at the default `FIRST_BOOT_ONLY`; use `EVERY_BOOT` only for
  configuration that must be reapplied after a reboot.
- **Make `EVERY_BOOT` scripts idempotent.**
  Re-running them should be safe. `FIRST_BOOT_ONLY` scripts run once, so they don't need
  this.
- **Use descriptive names.** Names appear in log paths and the
  console — for example, `Mount EFS home directory`, not
  `script1`.
- **Bake heavy installs into the AMI.** The node has
  approximately 30 minutes to join Slurm. If an install takes more than 5 minutes, put it in a
  custom AMI or on a shared file system.
- **Use checksums in production**, especially for scripts from
  shared repositories.
- **Forward logs to Amazon CloudWatch** with a node bootstrapped script
  so you can debug terminated instances. The AWS-maintained `configure-cloudwatch-logs.sh`
  script does this. For more information, see [Use AWS-maintained scripts for node lifecycle actions in AWS PCS](cng-node-lifecycle-actions-vetted-scripts.md "cng-node-lifecycle-actions-vetted-scripts.md").
- **Keep dependencies minimal**, and avoid forking background
  processes that outlive the script.
- **Do not modify AWS PCS agent files** under
  `/etc/amazon/pcs/` or `/var/log/amazon/pcs/`, or systemd units whose names
  begin with `pcs-`. These manage cluster connectivity.
- **Do not reboot the instance during a lifecycle action
  script.** A reboot interrupts the AWS PCS bootstrap sequence, preventing
  `slurmd` from starting or causing AWS PCS to terminate the node.
- **Store secrets in AWS Secrets Manager or Systems Manager Parameter
  Store.** Do not pass secrets as script arguments. Arguments are visible in API responses
  and the console.
- **Use S3 with a gateway VPC endpoint** for nodes in private subnets.
  The endpoint provides script access with no internet egress required.
