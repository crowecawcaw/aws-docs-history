

# Configure UltraServer instances
<a name="capacity-blocks-nvidia-imex"></a>

NVIDIA UltraServer instances (`p6e-gb200.36xlarge`, `p6e-gb200.72xlarge`, `p6e-gb300.36xlarge`, `p6e-gb300.72xlarge`) connect multiple GPUs across instances using NVLink. GPU-to-GPU communication over NVLink requires the [NVIDIA IMEX](https://docs.nvidia.com/multi-node-nvlink-systems/imex-guide/index.html) service to be configured with the IP addresses of all compute nodes in the job. This page shows you how to create a Slurm prolog script that automatically configures IMEX for each job, and how to deploy it in your AWS PCS cluster.

**Note**  
This prolog script supports `p6e-gb200` and `p6e-gb300` instance types.

## Prerequisites
<a name="capacity-blocks-nvidia-imex-prerequisites"></a>
+ A AWS PCS cluster with Slurm 25.05 or later.
+ A compute node group using UltraServer instances with a Capacity Block. For more information, see [Configure an AWS PCS compute node group to use a Capacity Block](capacity-blocks-configure-cng.md).
+ An AMI with the NVIDIA driver, CUDA, and IMEX packages installed. The IMEX service (`nvidia-imex`) must be enabled on the AMI.
+ The prolog script must be available on all compute nodes at the path configured in the cluster's Slurm `Prolog` setting. You can use a shared file system or include the script in your custom AMI.

## Automatic topology selection
<a name="capacity-blocks-nvidia-imex-topology"></a>

When you create a AWS PCS cluster with UltraServer compute node groups, the system inspects the Capacity Block, identifies the UltraServer type, and configures Slurm with the appropriate topology plugin. This process runs automatically and does not require any configuration.

AWS PCS manages topology through a dynamically generated `topology.yaml` file. As the cluster evolves through compute node group additions or removals, AWS PCS continuously reconciles the topology configuration to reflect the current cluster state.

Block topology models uniform, high-bandwidth communication domains where all GPUs participate in a single high-speed NVLink domain with near-uniform latency. The `topology/block` plugin allocates nodes based on the defined network topology, ensuring that jobs are placed within the same UltraServer and GPU-to-GPU communication uses NVLink instead of falling back to EFA networking.

## Using the topology/block plugin
<a name="capacity-blocks-nvidia-imex-job-submission"></a>

Jobs submitted to UltraServer queues are automatically placed within the same block (UltraServer) by the Slurm scheduler. All nodes in a block are allocated to a job before the next block is used. Jobs must use the `--exclusive` flag because IMEX requires a dedicated IMEX domain per job, and restarting the IMEX service would disrupt any other running jobs on the same nodes. For more information about the topology/block plugin, see the [Topology guide](https://slurm.schedmd.com/topology.html) and [topology.yaml reference](https://slurm.schedmd.com/topology.yaml.html) in the Slurm documentation.

When submitting jobs, you can use the `--segment=N` argument with `sbatch` and `srun` commands to specify the number of nodes to group together within the same block. The size of the segment must be less than or equal to the planning block size. Using `--segment` does not guarantee that segments will be placed on different blocks.

The following are sample scenarios for allocating blocks on a queue with 18-node UltraServers (for example, a `u-p6e-gb200x72` which has 18 `p6e-gb200.36xlarge` instances):

```
# Allocate a whole block (single UltraServer)
sbatch -N18 --exclusive --partition=ultra job.sh

# Allocate two full blocks (two UltraServers)
sbatch -N36 --exclusive --partition=ultra job.sh

# Allocate 24 nodes: full block is filled before 2nd block is used
sbatch -N24 --exclusive --partition=ultra job.sh

# Allocate 24 nodes as segments of 12, segments can fit on blocks with available space
sbatch -N24 --segment=12 --exclusive --partition=ultra job.sh
```

## Best practices for UltraServer topology
<a name="capacity-blocks-nvidia-imex-best-practices"></a>

For optimal performance with UltraServer architecture in AWS PCS:
+ **Use segments for better availability**: Use the `--segment` option with a value smaller than the full block size to allow jobs to be scheduled on blocks that have some drained or unavailable nodes. This trades absolute NVLink locality for quicker job scheduling times. For more information, see [Gaining more control over node scheduling with the Topology/Block Plugin](https://slurm.schedmd.com/SLUG24/NVIDIA-Craig_Tierney.pdf).
+ **Consider job size and block size**: If `BlockSizes=18`, jobs with up to 18 instances always run on a single UltraServer. Jobs requesting more than 18 nodes span multiple UltraServers, with NVLink connectivity within each block and EFA networking between blocks.
+ **Segment trade-offs**: Using `--segment` disables higher-order block size scheduling. Without `--segment`, a full block is filled before the next block is used. With `--segment`, segments can be placed on any block with sufficient available nodes.

## Limitations
<a name="capacity-blocks-nvidia-imex-limitations"></a>
+ AWS PCS requires that UltraServer compute node groups are placed in dedicated queues, separate from non-UltraServer compute node groups.
+ Each compute node group can be associated with only one UltraServer Capacity Block.
+ When a queue contains multiple UltraServer compute node groups, the instance count of each compute node group must have power-of-2 ratios between them (for example, 9 and 18, or 2 and 8).
+ Jobs on UltraServer queues must use the `--exclusive` flag to ensure a dedicated IMEX domain per job.
+ The IMEX domain created by the prolog script includes only the nodes allocated to the job. Since AWS PCS dynamically allocates nodes to jobs, the IMEX domain cannot be pre-created and must be configured at job start time. Jobs that span multiple UltraServers will not have NVLink connectivity between nodes in different UltraServers because the IMEX domain is based on IP addresses and cannot bridge across separate NVLink fabrics.
+ The IMEX `nodes_config.cfg` cannot be modified while the service is running. If the configuration is changed, IMEX permanently blocks communication to mismatched nodes. The only recovery is to stop IMEX on all nodes and restart with a consistent configuration.

## Create the IMEX prolog script
<a name="capacity-blocks-nvidia-imex-prolog"></a>

The following `91_nvidia_imex_prolog.sh` script configures NVIDIA IMEX on compute nodes when a Slurm job starts. The script name uses a `91` prefix following [SchedMD's naming convention](https://slurm.schedmd.com/prolog_epilog.html) for prolog execution ordering.

The script performs the following actions:

1. Checks whether the job is exclusive. IMEX configuration requires exclusive jobs to prevent disrupting other running jobs on the same nodes.

1. Checks whether the instance type is a supported UltraServer type (`p6e-gb200` or `p6e-gb300`).

1. Checks whether the IMEX service is enabled.

1. Creates the IMEX default channel device if it does not exist.

1. Writes the private IP addresses of all job nodes into `/etc/nvidia-imex/nodes_config.cfg`.

1. Restarts the IMEX service.

**Important**  
This prolog script requires jobs to be submitted with the `--exclusive` flag. Restarting IMEX while other jobs are running on the same nodes will disrupt those jobs.

Save the following script as `91_nvidia_imex_prolog.sh`:

```
#!/usr/bin/env bash

# This prolog script configures NVIDIA IMEX on compute nodes involved in the job execution.
#
# In particular:
# - Checks whether the job is executed exclusively.
#   If not, it exits immediately because it requires jobs to be executed exclusively.
# - Checks if it is running on a supported UltraServer instance type.
#   If not, it exits immediately because IMEX must be configured only on those instance types.
# - Checks if the IMEX service is enabled.
#   If not, it exits immediately because IMEX must be enabled to get configured.
# - Creates the IMEX default channel.
#   For more information about IMEX channels, see
#   https://docs.nvidia.com/multi-node-nvlink-systems/imex-guide/imexchannels.html
# - Writes the private IP addresses of compute nodes into /etc/nvidia-imex/nodes_config.cfg.
# - Restarts the IMEX system service.
#
# REQUIREMENTS:
#  - This prolog assumes to be run only with exclusive jobs.

LOG_FILE_PATH="/var/log/nvidia-imex-prolog.log"
SCONTROL_CMD="scontrol"
IMEX_START_TIMEOUT=60
IMEX_STOP_TIMEOUT=15
ALLOWED_INSTANCE_TYPES="^(p6e-gb200|p6e-gb300)"
IMEX_SERVICE="nvidia-imex"
IMEX_NODES_CONFIG="/etc/nvidia-imex/nodes_config.cfg"

function info() {
  echo "$(date "+%Y-%m-%dT%H:%M:%S.%3N") [INFO] [PID:$$] [JOB:${SLURM_JOB_ID}] $1"
}

function warn() {
  echo "$(date "+%Y-%m-%dT%H:%M:%S.%3N") [WARN] [PID:$$] [JOB:${SLURM_JOB_ID}] $1"
}

function error() {
  echo "$(date "+%Y-%m-%dT%H:%M:%S.%3N") [ERROR] [PID:$$] [JOB:${SLURM_JOB_ID}] $1"
}

function prolog_end() {
    info "PROLOG End JobId=${SLURM_JOB_ID}: $0"
    info "----------------"
    exit 0
}

function get_instance_type() {
  local token=$(curl -X PUT -s "http://169.254.169.254/latest/api/token" -H "X-aws-ec2-metadata-token-ttl-seconds: 21600")
  curl -s -H "X-aws-ec2-metadata-token: ${token}" http://169.254.169.254/latest/meta-data/instance-type
}

function return_if_unsupported_instance_type() {
  local instance_type=$(get_instance_type)

  if [[ ! ${instance_type} =~ ${ALLOWED_INSTANCE_TYPES} ]]; then
    info "Skipping IMEX configuration because instance type ${instance_type} does not support it"
    prolog_end
  fi
}

function return_if_imex_disabled() {
  if ! systemctl is-enabled "${IMEX_SERVICE}" &>/dev/null; then
    warn "Skipping IMEX configuration because system service ${IMEX_SERVICE} is not enabled"
    prolog_end
  fi
}

function return_if_job_is_not_exclusive() {
  if [[ "${SLURM_JOB_OVERSUBSCRIBE}" =~ ^(NO|TOPO)$  ]]; then
    info "Job is exclusive, proceeding with IMEX configuration"
  else
    info "Skipping IMEX configuration because the job is not exclusive"
    prolog_end
  fi
}

function get_ips_from_node_names() {
  local _nodes=$1
  ${SCONTROL_CMD} -ao show node "${_nodes}" | sed 's/^.* NodeAddr=\([^ ]*\).*/\1/'
}

function reload_imex() {
  info "Stopping IMEX"
  timeout ${IMEX_STOP_TIMEOUT} systemctl stop ${IMEX_SERVICE}
  pkill -9 ${IMEX_SERVICE}

  info "Restarting IMEX"
  timeout ${IMEX_START_TIMEOUT} systemctl start ${IMEX_SERVICE}
}

function create_default_imex_channel() {
  info "Creating IMEX default channel"
  MAJOR_NUMBER=$(cat /proc/devices | grep nvidia-caps-imex-channels | cut -d' ' -f1)
  if [ ! -d "/dev/nvidia-caps-imex-channels" ]; then
    sudo mkdir /dev/nvidia-caps-imex-channels
  fi

  # Then check and create device node
  if [ ! -e "/dev/nvidia-caps-imex-channels/channel0" ]; then
    sudo mknod /dev/nvidia-caps-imex-channels/channel0 c $MAJOR_NUMBER 0
    info "IMEX default channel created"
  else
    info "IMEX default channel already exists"
  fi
}

{
  info "PROLOG Start JobId=${SLURM_JOB_ID}: $0"

  return_if_job_is_not_exclusive
  return_if_unsupported_instance_type
  return_if_imex_disabled

  create_default_imex_channel

  IPS_FROM_CR=$(get_ips_from_node_names "${SLURM_NODELIST}")

  info "Node Names: ${SLURM_NODELIST}"
  info "Node IPs: ${IPS_FROM_CR}"
  info "IMEX Nodes Config: ${IMEX_NODES_CONFIG}"

  info "Updating IMEX nodes config ${IMEX_NODES_CONFIG}"
  echo "${IPS_FROM_CR}" > "${IMEX_NODES_CONFIG}"
  reload_imex

  prolog_end

} 2>&1 | tee -a "${LOG_FILE_PATH}" | logger -t "91_nvidia_imex_prolog"
```

## Deploy the prolog script
<a name="capacity-blocks-nvidia-imex-deploy"></a>

To deploy the prolog script, configure the Slurm `Prolog` and `PrologFlags` custom settings on your cluster. You can set these when you create a cluster or update an existing cluster.

For more information about configuring custom Slurm settings, see [Custom Slurm settings for AWS PCS clusters](slurm-custom-settings-cluster.md). For the procedure to update a cluster, see [Update an AWS PCS cluster](working-with_clusters_update_procedure.md).

Set the following custom Slurm settings on the cluster:
+ `Prolog` - Set to the path where the prolog script is available on compute nodes, for example `/shared/scripts/prolog.d/91_nvidia_imex_prolog.sh`.
+ `PrologFlags` - Set to `Alloc,NoHold`. The `Alloc` flag runs the prolog on each node when it is first allocated to a job. The `NoHold` flag prevents the job from being held if the prolog fails.

**Example Update cluster with prolog settings using the AWS CLI**  

```
aws pcs update-cluster \
  --cluster-identifier <cluster-id> \
  --slurm-configuration '{
    "slurmCustomSettings": [
      {"parameterName": "Prolog", "parameterValue": "/shared/scripts/prolog.d/91_nvidia_imex_prolog.sh"},
      {"parameterName": "PrologFlags", "parameterValue": "Alloc,NoHold"}
    ]
  }'
```

## Validate the IMEX setup
<a name="capacity-blocks-nvidia-imex-validate"></a>

The prolog script runs automatically when you submit a Slurm job. Submit a test job to verify that IMEX is configured correctly on all nodes.

Create a job script named `check-imex.sh`:

```
#!/bin/bash
#SBATCH --job-name=nvidia-imex-status
#SBATCH --ntasks-per-node=1
#SBATCH --exclusive
#SBATCH --output=imex-status-%j.out
#SBATCH --error=imex-status-%j.err

srun bash -c "/usr/bin/nvidia-imex-ctl -N > imex_result_\${SLURM_JOB_ID}_\$(hostname).out 2>&1"
```

Submit the job to your UltraServer queue:

```
sbatch -p {{queue-name}} -N {{node-count}} check-imex.sh
```

Check the output files. A successful IMEX configuration shows all nodes in `READY` state with `C` (Connected) in the connectivity table and `Domain State: UP`:

```
Connectivity Table Legend:
I - Invalid - Node wasn't reachable, no connection status available
N - Never Connected
R - Recovering - Connection was lost, but clean up has not yet been triggered.
D - Disconnected - Connection was lost, and clean up has been triggreed.
A - Authenticating - If GSSAPI enabled, client has initiated mutual authentication.
!V! - Version mismatch, communication disabled.
!M! - Node map mismatch, communication disabled.
C - Connected - Ready for operation

5/4/2026 06:08:10.580
Nodes:
Node #0   - 172.31.48.81    - READY                - Version: 570.172
Node #1   - 172.31.48.98    - READY                - Version: 570.172
Node #2   - 172.31.48.221   - READY                - Version: 570.172
Node #3   - 172.31.49.228   - READY                - Version: 570.172
Node #4   - 172.31.50.39    - READY                - Version: 570.172
Node #5   - 172.31.50.44    - READY                - Version: 570.172
Node #6   - 172.31.51.66    - READY                - Version: 570.172
Node #7   - 172.31.51.157   - READY                - Version: 570.172
Node #8   - 172.31.52.239   - READY                - Version: 570.172
Node #9   - 172.31.53.80    - READY                - Version: 570.172
Node #10  - 172.31.54.95    - READY                - Version: 570.172
Node #11  - 172.31.54.183   - READY                - Version: 570.172
Node #12  - 172.31.54.203   - READY                - Version: 570.172
Node #13  - 172.31.54.241   - READY                - Version: 570.172
Node #14  - 172.31.55.59    - READY                - Version: 570.172
Node #15  - 172.31.55.187   - READY                - Version: 570.172
Node #16  - 172.31.55.197   - READY                - Version: 570.172
Node #17  - 172.31.56.47    - READY                - Version: 570.172

 Nodes From\To  0   1   2   3   4   5   6   7   8   9   10  11  12  13  14  15  16  17
       0        C   C   C   C   C   C   C   C   C   C   C   C   C   C   C   C   C   C
       1        C   C   C   C   C   C   C   C   C   C   C   C   C   C   C   C   C   C
       2        C   C   C   C   C   C   C   C   C   C   C   C   C   C   C   C   C   C
       3        C   C   C   C   C   C   C   C   C   C   C   C   C   C   C   C   C   C
       4        C   C   C   C   C   C   C   C   C   C   C   C   C   C   C   C   C   C
       5        C   C   C   C   C   C   C   C   C   C   C   C   C   C   C   C   C   C
       6        C   C   C   C   C   C   C   C   C   C   C   C   C   C   C   C   C   C
       7        C   C   C   C   C   C   C   C   C   C   C   C   C   C   C   C   C   C
       8        C   C   C   C   C   C   C   C   C   C   C   C   C   C   C   C   C   C
       9        C   C   C   C   C   C   C   C   C   C   C   C   C   C   C   C   C   C
      10        C   C   C   C   C   C   C   C   C   C   C   C   C   C   C   C   C   C
      11        C   C   C   C   C   C   C   C   C   C   C   C   C   C   C   C   C   C
      12        C   C   C   C   C   C   C   C   C   C   C   C   C   C   C   C   C   C
      13        C   C   C   C   C   C   C   C   C   C   C   C   C   C   C   C   C   C
      14        C   C   C   C   C   C   C   C   C   C   C   C   C   C   C   C   C   C
      15        C   C   C   C   C   C   C   C   C   C   C   C   C   C   C   C   C   C
      16        C   C   C   C   C   C   C   C   C   C   C   C   C   C   C   C   C   C
      17        C   C   C   C   C   C   C   C   C   C   C   C   C   C   C   C   C   C

Domain State: UP
```

## Troubleshooting
<a name="capacity-blocks-nvidia-imex-troubleshooting"></a>

Node configuration mapping mismatch  
If you see `!M!` in the connectivity table or `Node configuration mapping mismatch` in the IMEX logs, the `nodes_config.cfg` file is not consistent across all nodes. IMEX permanently blocks communication to mismatched nodes. Verify that the prolog script ran on all nodes and restart the job.

IMEX channel device not found  
If the prolog script fails to create the IMEX channel device, verify that the NVIDIA driver is installed and that `/proc/devices` contains `nvidia-caps-imex-channels`.

Prolog script not running  
Verify that the `Prolog` and `PrologFlags` settings are configured on the cluster. Check that the script file exists on the compute nodes and has execute permissions (`chmod 0755`).