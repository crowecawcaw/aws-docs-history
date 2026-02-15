# Using the AWS PCS multi-cluster login

node configuration script

## Running the script

###### To run the configuration script

1. Save the [content of the script](multi-cluster-login-script-code.md#multi-cluster-login-script-code-content "multi-cluster-login-script-code.md#multi-cluster-login-script-code-content") in a file named:

```
pcs-multi-cluster-login-configure.sh
```

2. Make it executable:

```
chmod +x pcs-multi-cluster-login-configure.sh
```

3. Run the script:

```
./pcs-multi-cluster-login-configure.sh --cluster-identifier `cluster-name`
```

## Cluster interaction environments

After successful configuration, the script generates a cluster-specific activation script in
the current directory. The script has the name
`activate-pcs-`cluster-name``. The activation script
configures the necessary environment variables and paths to interact with the target
cluster.

###### To activate a cluster environment

- Use the `source` command to run the activation script

```
source ./activate-pcs-`cluster-name`
```

###### Example

```
# Activate cluster environment for cluster 'my-cluster'
source ./activate-pcs-my-cluster

# Now you can use Slurm commands
sinfo
squeue
sbatch my-job.sh
```

###### What the activation script does

- Sets the `SLURM_CONF` environment variable to point to the cluster's
  configuration.
- Updates the `PATH` to include the cluster's Slurm binaries.
- Configures other necessary Slurm environment variables (`MANPATH`,
  `LD_LIBRARY_PATH`).
- Sets AWS PCS cluster identification variables.
- Enables seamless interaction with the target AWS PCS cluster.

###### To deactivate a cluster environment

- Run the deactivation command.

```
deactivate-pcs-`cluster-name`
```

###### Example

```
# After activating a cluster
source ./activate-pcs-my-cluster

# Work with the cluster
sinfo

# Deactivate when done
deactivate-pcs-my-cluster
```

###### What the deactivate command does

- Restores the original `PATH` environment variable.
- Unsets cluster-specific Slurm environment variables.
- Returns the shell environment to its pre-activation state.

###### Note

The activation is session-specific and must be sourced in the shell session where you want
to interact with the cluster.
