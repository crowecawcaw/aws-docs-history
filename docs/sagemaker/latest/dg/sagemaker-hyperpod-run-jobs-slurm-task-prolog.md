# Injecting environment variables with a task prolog

You can use a task prolog to automatically inject environment variables into your jobs
without changing your job scripts. A Slurm task prolog is a script that
runs before a task starts. It runs with the same environment as the task. The task
prolog writes each variable to standard output as
`export `NAME`=`value``, and
Slurm sets those variables in the task's environment.

Slurm supports only a single `TaskProlog` entry in
`slurm.conf`. HyperPod AMIs configure `TaskProlog` to point
at a dispatcher script. This keeps the single entry available for multiple features and
your own customizations.

The dispatcher runs every executable `*.sh` script in a drop-in directory.
The relevant HyperPod AMI configuration is as follows:

- `slurm.conf` sets
  `TaskProlog=/opt/slurm/etc/task_prolog.sh`.
- `/opt/slurm/etc/task_prolog.sh` is a dispatcher that runs, in
  file name order, every executable `*.sh` script it finds in
  `/opt/slurm/etc/task_prolog.d/`. If the directory is empty or missing,
  the dispatcher does nothing and exits successfully.
- `/opt/slurm/etc/task_prolog.d/` is the drop-in directory for the
  scripts that the dispatcher runs. The AMI creates this directory as the supported
  location for your environment variable injection scripts.
  Because you have root access on HyperPod cluster nodes, you can edit
  `slurm.conf` directly.

###### Changing the TaskProlog entry stops environment variable injection

If you remove or repoint the `TaskProlog=/opt/slurm/etc/task_prolog.sh`
entry, the dispatcher no longer runs. Any HyperPod feature that relies on it
to inject environment variables (for example, observability metrics collection) no
longer receives those variables. To keep these features working, add your own scripts
to `/opt/slurm/etc/task_prolog.d/` instead of changing the entry.

For containerized jobs, the task prolog runs inside the container. HyperPod
configures Enroot bind mounts under `/etc/enroot/mounts.d/` so
that the dispatcher script and the `task_prolog.d/` directory are available
inside Pyxis containers.

###### Container images must include bash

Because the task prolog dispatcher is a `bash` script that runs inside the
container, container images for your jobs must include the `bash` shell at
`/bin/bash`. Otherwise, the task prolog fails and the job exits with an
error.

If you build a custom AMI, it inherits this task prolog configuration from the
HyperPod base AMI. Preserve the `TaskProlog` entry and the
`/opt/slurm/etc/task_prolog.d/` directory in your custom AMI so that the
dispatcher stays available. For more information about custom AMIs, see [Custom Amazon Machine Images (AMIs) for SageMaker HyperPod clusters](hyperpod-custom-ami-support.md "hyperpod-custom-ami-support.md").

## Add your own task prolog script

You can add executable scripts to `/opt/slurm/etc/task_prolog.d/` to inject
environment variables into your jobs. The dispatcher runs these scripts in ascending
order by file name. HyperPod can install its own scripts in this directory. To
run your script after them, use a high numeric prefix, such as `900_`. If two
scripts export the same variable, the value from the script that runs later takes
effect.

To add your own task prolog script, follow these steps:

1. Create an executable script in `/opt/slurm/etc/task_prolog.d/` on
   each compute node. Give the file a numeric prefix to set its order, for example,
   `900_my_env.sh`. Write each environment variable to standard output in
   the form `export `NAME`=`value``,
   and send any other output to standard error.

```
`$` `sudo tee /opt/slurm/etc/task_prolog.d/900_my_env.sh > /dev/null <<'EOF'
#!/bin/bash
echo "export MY_CUSTOM_VAR=my_value"
EOF`
`$` `sudo chmod +x /opt/slurm/etc/task_prolog.d/900_my_env.sh`
```

2. Verify that your variable is injected into a job on the host.

```
`$` `srun bash -c 'env | grep MY_CUSTOM_VAR'`
`MY_CUSTOM_VAR=my_value`
```

3. If you run containerized jobs, verify that your variable is also injected
   inside a Pyxis container.

```
`$` `srun --container-image=`docker/image:tag` bash -c 'env | grep MY_CUSTOM_VAR'`
`MY_CUSTOM_VAR=my_value`
```

###### Scripts don't persist across node replacements

Scripts that you place directly in `/opt/slurm/etc/task_prolog.d/` are
local to each node, and are not preserved when a node is replaced (for example, during
auto-resume). To keep your scripts across node replacements, install them from a
lifecycle script so they are reapplied when a node is provisioned. For more information
about lifecycle scripts for Slurm, see [Customizing SageMaker HyperPod clusters using lifecycle scripts](sagemaker-hyperpod-lifecycle-best-practices-slurm.md "sagemaker-hyperpod-lifecycle-best-practices-slurm.md").
