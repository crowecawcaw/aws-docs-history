

# Rebooting compute nodes with Slurm in AWS PCS
<a name="slurm-reboot"></a>

AWS PCS supports Slurm's native `scontrol reboot` command. Use this command to reboot compute nodes without EC2 instance replacement. Other reboot methods (Amazon EC2 console, AWS CLI, automated patches, or system maintenance) cause AWS PCS to consider the EC2 instance unhealthy and replace it.

## Benefits of Slurm reboot
<a name="slurm-reboot-benefits"></a>

Slurm reboot provides several advantages for cluster maintenance:
+ **Preserve capacity** – Avoid losing capacity-constrained EC2 instances to other customers.
+ **Reduce costs** – Eliminate unnecessary instance replacement cycles and continued billing for idle nodes.
+ **Faster recovery** – No provisioning delays compared to instance replacement.
+ **Operational flexibility** – Clear memory leaks, remove temporary files, and recover nodes from degraded states.

## When to use Slurm reboot
<a name="slurm-reboot-use-cases"></a>

Use Slurm reboot for common operational maintenance scenarios:
+ **Troubleshooting** – Resolve performance issues or unresponsive processes, especially for GPU nodes.
+ **Resource cleanup** – Clear memory leaks, temporary files in `/tmp`, or stuck processes that affect job performance.
+ **Recovery** – Recover nodes from hung or degraded states before requiring full node replacement.

## Limitations
<a name="slurm-reboot-limitations"></a>
+ Only Slurm Admin users (root users) can execute reboot commands.
+ Reboot support is limited to `scontrol reboot` only.
+ RebootProgram configuration isn't supported.
+ No console interface – command-line only.

**Topics**
+ [Benefits of Slurm reboot](#slurm-reboot-benefits)
+ [When to use Slurm reboot](#slurm-reboot-use-cases)
+ [Limitations](#slurm-reboot-limitations)
+ [Reboot a compute node using Slurm in AWS PCS](slurm-reboot-procedure.md)
+ [Cancel a pending reboot in AWS PCS](slurm-reboot-cancel.md)
+ [Slurm reboot frequently asked questions in AWS PCS](slurm-reboot-faq.md)
+ [Troubleshooting Slurm reboot issues in AWS PCS](slurm-reboot-troubleshooting.md)