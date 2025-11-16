# Frequently asked questions about Slurm CLI Filter

Plugins in AWS PCS

Review these frequently asked questions about CLI Filter Plugins.

**What is the difference between CLI Filter Plugin and Job Submit Plugin?**

CLI Filter Plugin runs client-side on login and compute nodes before job submission
reaches the controller, while Job Submit Plugin runs server-side on the controller after job
submission. CLI Filter Plugin can be bypassed by users but doesn't hold controller locks, while Job
Submit is secure but can impact cluster performance during execution.

**Does AWS PCS support Slurm Job Submit Plugin?**

No, Job Submit Plugin is not supported in AWS PCS. Use CLI Filter Plugin instead for job submission validation and modification.

**Can I use CLI Filter Plugin for security enforcement?**

No, CLI Filter Plugin can be bypassed by determined users and should not be relied upon
for security enforcement. Use it for user experience improvements, default parameter setting,
and policy guidance rather than security-critical policies.

**Why must the script be on all compute nodes, not just login nodes?**

Slurm commands like `srun` can be executed within job scripts on compute nodes,
which also triggers CLI Filter Plugin execution. The script must be available wherever Slurm commands
are executed.

**Can I modify the CLI Filter Plugin script on a live cluster?**

Yes, if you use the S3 or file system deployment approach. New instances will get the
updated script, but existing instances need the script updated manually or through your chosen
deployment method.

**Can I use different CLI Filter Plugin scripts on different compute node groups?**

Yes, but this is not recommended. You can provide scripts with different logic to
different compute node groups, but you are responsible for managing interdependencies and
preventing overlapping logic. Most customers provide one set of logic across an entire
cluster.

**Can I use CLI Filter Plugin with C implementation instead of Lua?**

C implementation is not supported. Only Lua script implementation is supported in AWS PCS.
SchedMD recommends customers use Lua over C for ease of use when implementing CLI
Filter Plugins.

**Can I turn CLI Filter Plugin on or off on an existing cluster?**

Yes, you can enable or disable CLI Filter Plugin on existing clusters using the Update API without recreating the cluster.
