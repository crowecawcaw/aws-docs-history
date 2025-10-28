# Slurm reboot frequently asked questions in AWS PCS

Find answers to common questions about using Slurm reboot in AWS PCS.

**What is Slurm reboot support?**

Support for the native Slurm `scontrol reboot` command. Use this command to
reboot compute nodes without automatic instance replacement, which preserves EC2 instance
capacity and reduces operational costs.

**Who can use Slurm reboot commands?**

Only Slurm Admin users (root users) can execute reboot commands. Regular users
attempting to use `scontrol reboot` will receive a permission denied error from
Slurm without affecting the node.

**What happens to running jobs during a reboot?**

By default, jobs complete normally before reboot occurs. With the ASAP option, the
node is drained to prevent new jobs, and reboot happens after current jobs finish. Jobs
can be cancelled or requeued for immediate reboots.

**How is this different from EC2 console reboot?**

Slurm reboot preserves the EC2 instance and avoids replacement, while EC2 console
reboots trigger NodeGroupManager to replace the instance due to failed health checks
during the reboot process.

**Can I configure custom reboot scripts?**

No, RebootProgram configuration is not supported in the initial release. The feature
uses standard Slurm reboot behavior without custom script support.

**How long does a Slurm reboot take?**

Reboot time varies based on instance type, customer boot processes, AMI configuration,
and whether jobs need to complete first. The process includes waiting for jobs to
complete, physical reboot, health checks, and slurmd daemon registration.

**Can I see a history of reboots?**

Reboot events are recorded in Slurm logs (slurmctld and slurmd) which can be monitored
through CloudWatch. The reason field in node status shows the reboot reason during the
process.

**What if a node gets stuck during reboot?**

If a node doesn't complete the reboot process within ResumeTimeout, it will be marked
as DOWN. Check CloudWatch logs for errors, verify network connectivity, and examine slurmd
logs. Contact AWS Support if issues persist.

**Can I reboot multiple nodes at once?**

Yes, you can specify multiple nodes in the reboot command:

```
scontrol reboot ASAP node1,node2,node3
```

**How can I reboot a node without waiting for jobs to complete?**

For immediate node reboots when facing issues like problematic nodes affecting
multi-node jobs, significant performance degradation, or unstable GPU behavior, you have
two options:

- Cancel and Reboot – First, cancel affected
  jobs using `scancel <job_id>`, then initiate an immediate reboot
  using `scontrol reboot ASAP <nodename>`. Running jobs will be
  terminated and need to be resubmitted after the node recovers.
- Drain and Requeue (less impactful) – Start
  by initiating a drain and reboot with `scontrol reboot ASAP
<nodename>`, then requeue affected jobs using `scontrol requeue
<job_id>`. This puts jobs back into pending state instead of cancelling
  them.

**What happens if I specify nextstate=DOWN?**

If you specify `nextstate=DOWN`, the node will be marked as unhealthy after
reboot and trigger instance replacement. To avoid instance replacement, don't specify
nextstate or use `nextstate=RESUME`.

## Additional resources

- For basic reboot procedures, see [Reboot a compute node using Slurm in AWS PCS](slurm-reboot-procedure.md "slurm-reboot-procedure.md").
- For troubleshooting reboot issues, see [Troubleshooting Slurm reboot issues in
  AWS PCS](slurm-reboot-troubleshooting.md "slurm-reboot-troubleshooting.md").
- For Slurm reboot documentation, see [Slurm scontrol
  documentation](https://slurm.schedmd.com/scontrol.html#OPT_reboot "https://slurm.schedmd.com/scontrol.html#OPT_reboot").
