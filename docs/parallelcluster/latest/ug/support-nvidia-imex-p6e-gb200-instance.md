# Support NVIDIA-Imex with p6e-gb200 instance

This tutorial shows you how to get started with AWS ParallelCluster on P6e-GB200, to leverage the
highest GPU performance for AI training and inference. [p6e-gb200.36xlarge instances are only available via P6e-GB200 UltraServers](https://aws.amazon.com/ec2/instance-types/p6/ "https://aws.amazon.com/ec2/instance-types/p6/") where the
`u-p6e-gb200x72` is Ultraserver Size and `p6e-gb200.36xlarge` is the [InstanceType](Scheduling-v3.md#yaml-Scheduling-SlurmQueues-ComputeResources-InstanceType "Scheduling-v3.md#yaml-Scheduling-SlurmQueues-ComputeResources-InstanceType") which forms
the ultraserver. On purchasing an Ultraserver `u-p6e-gb200x72` it will be available
through a [EC2 Capacity Blocks for ML](https://aws.amazon.com/ec2/capacityblocks/ "https://aws.amazon.com/ec2/capacityblocks/")
which will have 18 `p6e-gb200.36xlarge` instances. To learn more, see [P6e-GB200](https://aws.amazon.com/ec2/instance-types/p6/ "https://aws.amazon.com/ec2/instance-types/p6/").

AWS ParallelCluster version 3.14.0:

- provides the complete NVIDIA software stack (drivers, CUDA, EFA, NVIDIA-IMEX) required
  by this instance type
- creates nvidia-imex configurations for P6e-GB200 ultraserver
- enables and starts the `nvidia-imex` service for P6e-GB200 ultraserver
- configures the Slurm Block topology plugin so that every P6e-GB200 Ultraserver (an EC2
  Capacity Block) is a Slurm Block with the right size (see the [Release notes and document history](document_history.md "document_history.md") entry for version 3.14.0).
  However, GPU-to-GPU communication over NVLink requires additional configurations, specifically a
  [`nodes_config.cfg`](https://docs.nvidia.com/multi-node-nvlink-systems/imex-guide/config.html#imex-service-node-configuration-file-location "https://docs.nvidia.com/multi-node-nvlink-systems/imex-guide/config.html#imex-service-node-configuration-file-location") file that contains the IP addresses of compute nodes
  in an IMEX domain that ParallelCluster does not generate automatically. To help generate this file,
  we provide a prolog script that automatically discovers compute node IPs and configures the
  [`nodes_config.cfg`](https://docs.nvidia.com/multi-node-nvlink-systems/imex-guide/config.html#imex-service-node-configuration-file-location "https://docs.nvidia.com/multi-node-nvlink-systems/imex-guide/config.html#imex-service-node-configuration-file-location") following [NVIDIA IMEX Slurm Job Scheduler Integration](https://docs.nvidia.com/multi-node-nvlink-systems/imex-guide/deployment.html#job-scheduler-integration "https://docs.nvidia.com/multi-node-nvlink-systems/imex-guide/deployment.html#job-scheduler-integration") recommendations. This tutorial walks you through
  how to create the prolog script, deploy it via a HeadNode custom action, and validate the IMEX setup.

###### Note

P6e-GB200 is supported starting with AWS ParallelCluster v3.14.0 on Amazon Linux 2023, Ubuntu 22.04,
and Ubuntu 24.04. For detailed software versions and an updated list of supported distributions, see the
[AWS ParallelCluster
changelog](https://github.com/aws/aws-parallelcluster/blob/develop/CHANGELOG.md "https://github.com/aws/aws-parallelcluster/blob/develop/CHANGELOG.md").

## Create a Prolog Script to manage

NVIDIA-Imex

**Limitation:**

- This prolog script will run on submission of an exclusive job. This is to ensure that
  an IMEX re-start does not disrupt any running jobs on p6e-Gb200 nodes that belong to an
  IMEX domain.

Below is the `91_nvidia_imex_prolog.sh` script you should configure as a prolog in Slurm.
It is used to automatically update the nvidia-imex configuration on compute nodes. The script's name has
a prefix of `91` to adhere to [SchedMD's naming convention](https://slurm.schedmd.com/prolog_epilog.html "https://slurm.schedmd.com/prolog_epilog.html"). This ensures it executes prior to any other prolog scripts in the
sequence. The script reconfigures the NVIDIA Imex node's configuration when a job is started and reloads
the necessary NVIDIA daemons.

###### Note

This script will not be executed in case multiple jobs are started concurrently on the same
nodes, therefore we suggest to use the `--exclusive` flag on submission.

```
#!/usr/bin/env bash

# This prolog script configures the NVIDIA IMEX on compute nodes involved in the job execution.
#
# In particular:
# - Checks whether the job is executed exclusively.
#   If not, it exits immediately because it requires jobs to be executed exclusively.
# - Checks if it is running on a p6e-gb200 instance type.
#   If not, it exits immediately because IMEX must be configured only on that instance type.
# - Checks if the IMEX service is enabled.
#   If not, it exits immediately because IMEX must be enabled to get configured.
# - Creates the IMEX default channel.
#   For more information about IMEX channels, see https://docs.nvidia.com/multi-node-nvlink-systems/imex-guide/imexchannels.html
# - Writes the private IP addresses of compute nodes into /etc/nvidia-imex/nodes_config.cfg.
# - Restarts the IMEX system service.
#
# REQUIREMENTS:
#  - This prolog assumes to be run only with exclusive jobs.

LOG_FILE_PATH="/var/log/parallelcluster/nvidia-imex-prolog.log"
SCONTROL_CMD="/opt/slurm/bin/scontrol"
IMEX_START_TIMEOUT=60
IMEX_STOP_TIMEOUT=15
ALLOWED_INSTANCE_TYPES="^(p6e-gb200)"
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

function error_exit() {
  error "$1" && exit 1
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

function get_compute_resource_name() {
  local _queue_name_prefix=$1
  local _slurmd_node_name=$2
  echo "${_slurmd_node_name}" | sed -E "s/${_queue_name_prefix}(.+)-[0-9]+$/\1/"
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

## Create the HeadNode

OnNodeStart Custom Action Script

Create an `install_custom_action.sh` custom action which will download the
aforementioned prolog script in a shared directory `/opt/slurm/etc/scripts/prolog.d/`
which is accessed by Compute Nodes and sets the proper permissions to be executed.

```
#!/bin/bash
set -e

echo "Executing $0"

PROLOG_NVIDIA_IMEX=/opt/slurm/etc/scripts/prolog.d/91_nvidia_imex_prolog.sh
aws s3 cp "s3://<Bucket>/91_nvidia_imex_prolog.sh" "${PROLOG_NVIDIA_IMEX}"
chmod 0755 "${PROLOG_NVIDIA_IMEX}"
```

## Create the cluster

Create a cluster including P6e-GB200 instances. Below you can find an example configuration
containing SlurmQueues for Ultraserver type `u-p6e-gb200x72`.

P6e-GB200 is currently only available in Local Zones. Some [Local Zones do not support a NAT
Gateway](../../../local-zones/latest/ug/local-zones-connectivity-nat.md "../../../local-zones/latest/ug/local-zones-connectivity-nat.md"), so please follow the [Connectivity options for Local
Zones](../../../local-zones/latest/ug/local-zones-connectivity.md "../../../local-zones/latest/ug/local-zones-connectivity.md") as ParallelCluster needs [Configuring security groups for restricted environments](security-groups-configuration.md "security-groups-configuration.md") to connect to AWS Services. Please follow
the [Launch instances with Capacity Blocks (CB)](launch-instances-capacity-blocks.md "launch-instances-capacity-blocks.md")
(AWS ParallelClusterLaunch) as Ultraservers are available only as Capacity Blocks.

```
HeadNode:
  CustomActions:
    OnNodeStart:
      Script: s3://<s3-bucket-name>/install_custom_action.sh
    S3Access:
      - BucketName: <s3-bucket-name>
  InstanceType: <HeadNode-instance-type>
  Networking:
    SubnetId: <subnet-abcd78901234567890>
  Ssh:
    KeyName: <Key-name>
Image:
  Os: ubuntu2404
Scheduling:
  Scheduler: slurm
  SlurmSettings:
    CustomSlurmSettings:
      - PrologFlags: "Alloc,NoHold"
      - MessageTimeout: 240
  SlurmQueues:
    - CapacityReservationTarget:
        CapacityReservationId: <cr-123456789012345678>
      CapacityType: CAPACITY_BLOCK
      ComputeResources: ### u-p6e-gb200x72
        - DisableSimultaneousMultithreading: true
          Efa:
            Enabled: true
          InstanceType: p6e-gb200.36xlarge
          MaxCount: 18
          MinCount: 18
          Name: cr1
      Name: q1
      Networking:
        SubnetIds:
          - <subnet-1234567890123456>
```

## Validate IMEX Setup

The `91_nvidia_imex_prolog.sh` prolog will run when you submit a Slurm
job. Below is an example job to check the status NVIDIA-imex domain.

```
#!/bin/bash
#SBATCH --job-name=nvidia-imex-status-job
#SBATCH --ntasks-per-node=1
#SBATCH --output=slurm-%j.out
#SBATCH --error=slurm-%j.err

QUEUE_NAME="q1"
COMPUTE_RES_NAME="cr1"
IMEX_CONFIG_FILE="/opt/parallelcluster/shared/nvidia-imex/config_${QUEUE_NAME}_${COMPUTE_RES_NAME}.cfg"

srun bash -c "/usr/bin/nvidia-imex-ctl -N -c ${IMEX_CONFIG_FILE} > result_\${SLURM_JOB_ID}_\$(hostname).out 2> result_\${SLURM_JOB_ID}_\$(hostname).err"
```

Check the output of the Job:

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

5/12/2025 06:08:10.580
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
