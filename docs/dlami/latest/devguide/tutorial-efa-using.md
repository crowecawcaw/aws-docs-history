# Using EFA on the DLAMI

The following section describes how to use EFA to run multi-node applications on the
AWS Deep Learning AMIs.

## Running Multi-Node Applications with EFA

To run an application across a cluster of nodes the following configuration is required

###### Topics

- [Enable Passwordless SSH](#tutorial-efa-using-multi-node-ssh "#tutorial-efa-using-multi-node-ssh")
- [Create Hosts File](#tutorial-efa-using-multi-node-hosts "#tutorial-efa-using-multi-node-hosts")
- [NCCL Tests](#tutorial-efa-using-2node "#tutorial-efa-using-2node")

### Enable Passwordless SSH

Select one node in your cluster as the leader node. The remaining nodes are referred to
as the member nodes.

1. On the leader node, generate the RSA keypair.

```
ssh-keygen -t rsa -N "" -f ~/.ssh/id_rsa
```

2. Change the permissions of the private key on the leader node.

```
chmod 600 ~/.ssh/id_rsa
```

3. Copy the public key `~/.ssh/id_rsa.pub` to and append it
   to `~/.ssh/authorized_keys` of the member nodes in the cluster.
4. You should now be able to directly login to the member nodes from
   the leader node using the private ip.

```
ssh <member private ip>
```

5. Disable strictHostKeyChecking and enable agent forwarding on the
   leader node by adding the following to the ~/.ssh/config file on the leader node:

```
Host *
    ForwardAgent yes
Host *
    StrictHostKeyChecking no
```

6. On Amazon Linux 2 instances, run the following command on the leader node to provide correct
   permissions to the config file:

```
chmod 600 ~/.ssh/config
```

### Create Hosts File

On the leader node, create a hosts file to identify the nodes in the cluster. The hosts
file must have an entry for each node in the cluster. Create a file ~/hosts and add each
node using the private ip as follows:

```
localhost slots=8
<private ip of node 1> slots=8
<private ip of node 2> slots=8
```

### NCCL Tests

###### Note

These tests have been run using EFA version 1.38.0 and OFI NCCL Plugin 1.13.2.

Listed below are a subset of NCCL Tests provided by Nvidia to test both functionality and performance over multiple compute nodes

**Supported Instances: P3dn, P4, P5, P5e, P5en**

##### Multi-node NCCL Performance

Test on P4d.24xlarge

To check NCCL Performance with EFA, run the standard NCCL Performance test that is
available on the official [NCCL-Tests Repo](https://github.com/NVIDIA/nccl-tests.git "https://github.com/NVIDIA/nccl-tests.git"). The DLAMI comes with this test already built for CUDA
XX.X. You can similarly run your own script with EFA.

When constructing your own script, refer to the following guidance:

- Use the complete path to mpirun as shown in the example while running NCCL applications with EFA.
- Change the params np and N based on the number of instances and GPUs in your cluster.
- Add the NCCL_DEBUG=INFO flag and make sure that the logs indicate EFA usage as
  "Selected Provider is EFA".
- Set the Training Log Location to parse for validation

```
TRAINING_LOG="testEFA_$(date +"%N").log"
```

Use the command `watch nvidia-smi` on any of the member nodes to monitor
GPU usage. The following `watch nvidia-smi` commands are for a generic CUDA xx.x version and
depend on the Operating System of your instance.
You can run the commands for any available CUDA version in your Amazon EC2 instance by replacing the CUDA version in the script.

- Amazon Linux 2, Amazon Linux 2023:

```
 $ /opt/amazon/openmpi/bin/mpirun -n 16 -N 8 \
-x NCCL_DEBUG=INFO --mca pml ^cm \
-x LD_LIBRARY_PATH=/usr/local/`cuda-xx.x`/efa/lib:/usr/local/`cuda-xx.x`/lib:/usr/local/`cuda-xx.x`/lib64:/usr/local/`cuda-xx.x`:/opt/amazon/efa/lib64:/opt/amazon/openmpi/lib64:$LD_LIBRARY_PATH \
--hostfile hosts --mca btl tcp,self --mca btl_tcp_if_exclude lo,docker0 --bind-to none \
/usr/local/`cuda-xx.x`/efa/test-`cuda-xx.x`/all_reduce_perf -b 8 -e 1G -f 2 -g 1 -c 1 -n 100 | tee ${TRAINING_LOG}
```

- Ubuntu 20.04, Ubuntu 20.04:

```
$ /opt/amazon/openmpi/bin/mpirun -n 16 -N 8 \
-x NCCL_DEBUG=INFO --mca pml ^cm \
-x LD_LIBRARY_PATH=/usr/local/`cuda-xx.x`/efa/lib:/usr/local/`cuda-xx.x`/lib:/usr/local/`cuda-xx.x`/lib64:/usr/local/`cuda-xx.x`:/opt/amazon/efa/lib:/opt/amazon/openmpi/lib:$LD_LIBRARY_PATH \
--hostfile hosts --mca btl tcp,self --mca btl_tcp_if_exclude lo,docker0 --bind-to none \
/usr/local/`cuda-xx.x`/efa/test-`cuda-xx.x`/all_reduce_perf -b 8 -e 1G -f 2 -g 1 -c 1 -n 100 | tee ${TRAINING_LOG}
```

Your output should look like the following:

```
# nThread 1 nGpus 1 minBytes 8 maxBytes 1073741824 step: 2(factor) warmup iters: 5 iters: 100 agg iters: 1 validation: 1 graph: 0
#
# Using devices
#  Rank  0 Group  0 Pid  33378 on ip-172-31-42-25 device  0 [0x10] NVIDIA A100-SXM4-40GB
#  Rank  1 Group  0 Pid  33379 on ip-172-31-42-25 device  1 [0x10] NVIDIA A100-SXM4-40GB
#  Rank  2 Group  0 Pid  33380 on ip-172-31-42-25 device  2 [0x20] NVIDIA A100-SXM4-40GB
#  Rank  3 Group  0 Pid  33381 on ip-172-31-42-25 device  3 [0x20] NVIDIA A100-SXM4-40GB
#  Rank  4 Group  0 Pid  33382 on ip-172-31-42-25 device  4 [0x90] NVIDIA A100-SXM4-40GB
#  Rank  5 Group  0 Pid  33383 on ip-172-31-42-25 device  5 [0x90] NVIDIA A100-SXM4-40GB
#  Rank  6 Group  0 Pid  33384 on ip-172-31-42-25 device  6 [0xa0] NVIDIA A100-SXM4-40GB
#  Rank  7 Group  0 Pid  33385 on ip-172-31-42-25 device  7 [0xa0] NVIDIA A100-SXM4-40GB
#  Rank  8 Group  0 Pid  30378 on ip-172-31-43-8 device  0 [0x10] NVIDIA A100-SXM4-40GB
#  Rank  9 Group  0 Pid  30379 on ip-172-31-43-8 device  1 [0x10] NVIDIA A100-SXM4-40GB
#  Rank 10 Group  0 Pid  30380 on ip-172-31-43-8 device  2 [0x20] NVIDIA A100-SXM4-40GB
#  Rank 11 Group  0 Pid  30381 on ip-172-31-43-8 device  3 [0x20] NVIDIA A100-SXM4-40GB
#  Rank 12 Group  0 Pid  30382 on ip-172-31-43-8 device  4 [0x90] NVIDIA A100-SXM4-40GB
#  Rank 13 Group  0 Pid  30383 on ip-172-31-43-8 device  5 [0x90] NVIDIA A100-SXM4-40GB
#  Rank 14 Group  0 Pid  30384 on ip-172-31-43-8 device  6 [0xa0] NVIDIA A100-SXM4-40GB
#  Rank 15 Group  0 Pid  30385 on ip-172-31-43-8 device  7 [0xa0] NVIDIA A100-SXM4-40GB
ip-172-31-42-25:33385:33385 [7] NCCL INFO cudaDriverVersion 12060
ip-172-31-43-8:30383:30383 [5] NCCL INFO Bootstrap : Using ens32:172.31.43.8
ip-172-31-43-8:30383:30383 [5] NCCL INFO NCCL version 2.23.4+cuda12.5
...
ip-172-31-42-25:33384:33451 [6] NCCL INFO NET/OFI Initializing aws-ofi-nccl 1.13.2-aws
ip-172-31-42-25:33384:33451 [6] NCCL INFO NET/OFI Using Libfabric version 1.22
ip-172-31-42-25:33384:33451 [6] NCCL INFO NET/OFI Using CUDA driver version 12060 with runtime 12050
ip-172-31-42-25:33384:33451 [6] NCCL INFO NET/OFI Configuring AWS-specific options
ip-172-31-42-25:33384:33451 [6] NCCL INFO NET/OFI Setting provider_filter to efa
ip-172-31-42-25:33384:33451 [6] NCCL INFO NET/OFI Setting FI_EFA_FORK_SAFE environment variable to 1
ip-172-31-42-25:33384:33451 [6] NCCL INFO NET/OFI Setting NCCL_NVLSTREE_MAX_CHUNKSIZE to 512KiB
ip-172-31-42-25:33384:33451 [6] NCCL INFO NET/OFI Setting NCCL_NVLS_CHUNKSIZE to 512KiB
ip-172-31-42-25:33384:33451 [6] NCCL INFO NET/OFI Running on p4d.24xlarge platform, Setting NCCL_TOPO_FILE environment variable to /opt/amazon/ofi-nccl/share/aws-ofi-nccl/xml/p4d-24xl-topo.xml
...
-----------------------------some output truncated-----------------------------------
#                                                              out-of-place                       in-place
#       size         count      type   redop    root     time   algbw   busbw #wrong     time   algbw   busbw #wrong
#        (B)    (elements)                               (us)  (GB/s)  (GB/s)            (us)  (GB/s)  (GB/s)
           8             2     float     sum      -1    180.3    0.00    0.00      0    179.3    0.00    0.00      0
          16             4     float     sum      -1    178.1    0.00    0.00      0    177.6    0.00    0.00      0
          32             8     float     sum      -1    178.5    0.00    0.00      0    177.9    0.00    0.00      0
          64            16     float     sum      -1    178.8    0.00    0.00      0    178.7    0.00    0.00      0
         128            32     float     sum      -1    178.2    0.00    0.00      0    177.8    0.00    0.00      0
         256            64     float     sum      -1    178.6    0.00    0.00      0    178.8    0.00    0.00      0
         512           128     float     sum      -1    177.2    0.00    0.01      0    177.1    0.00    0.01      0
        1024           256     float     sum      -1    179.2    0.01    0.01      0    179.3    0.01    0.01      0
        2048           512     float     sum      -1    181.3    0.01    0.02      0    181.2    0.01    0.02      0
        4096          1024     float     sum      -1    184.2    0.02    0.04      0    183.9    0.02    0.04      0
        8192          2048     float     sum      -1    191.2    0.04    0.08      0    190.6    0.04    0.08      0
       16384          4096     float     sum      -1    202.5    0.08    0.15      0    202.3    0.08    0.15      0
       32768          8192     float     sum      -1    233.0    0.14    0.26      0    232.1    0.14    0.26      0
       65536         16384     float     sum      -1    238.6    0.27    0.51      0    235.1    0.28    0.52      0
      131072         32768     float     sum      -1    237.2    0.55    1.04      0    236.8    0.55    1.04      0
      262144         65536     float     sum      -1    248.3    1.06    1.98      0    247.0    1.06    1.99      0
      524288        131072     float     sum      -1    309.2    1.70    3.18      0    307.7    1.70    3.20      0
     1048576        262144     float     sum      -1    408.7    2.57    4.81      0    404.3    2.59    4.86      0
     2097152        524288     float     sum      -1    613.5    3.42    6.41      0    607.9    3.45    6.47      0
     4194304       1048576     float     sum      -1    924.5    4.54    8.51      0    914.8    4.58    8.60      0
     8388608       2097152     float     sum      -1   1059.5    7.92   14.85      0   1054.3    7.96   14.92      0
    16777216       4194304     float     sum      -1   1269.9   13.21   24.77      0   1272.0   13.19   24.73      0
    33554432       8388608     float     sum      -1   1642.7   20.43   38.30      0   1636.7   20.50   38.44      0
    67108864      16777216     float     sum      -1   2446.7   27.43   51.43      0   2445.8   27.44   51.45      0
   134217728      33554432     float     sum      -1   4143.6   32.39   60.73      0   4142.4   32.40   60.75      0
   268435456      67108864     float     sum      -1   7351.9   36.51   68.46      0   7346.7   36.54   68.51      0
   536870912     134217728     float     sum      -1    13717   39.14   73.39      0    13703   39.18   73.46      0
  1073741824     268435456     float     sum      -1    26416   40.65   76.21      0    26420   40.64   76.20      0
...
# Out of bounds values : 0 OK
# Avg bus bandwidth    : 15.5514
```

To Validate that the EFA tests returned a valid result, please use the following tests to confirm:

- Get the instance type using EC2 Instance Metadata:

```
TOKEN=$(curl -X PUT "http://169.254.169.254/latest/api/token" -H "X-aws-ec2-metadata-token-ttl-seconds: 21600")
INSTANCE_TYPE=$(curl -H "X-aws-ec2-metadata-token: $TOKEN" -v http://169.254.169.254/latest/meta-data/instance-type)
```

- Run the [Performance Tests](#tutorial-efa-using-multinode "#tutorial-efa-using-multinode")
- Set the Following Parameters

```
CUDA_VERSION
CUDA_RUNTIME_VERSION
NCCL_VERSION
```

- Validate the Results as shown:

```
RETURN_VAL=`echo $?`
if [ ${RETURN_VAL} -eq 0 ]; then

    # [0] NCCL INFO NET/OFI Initializing aws-ofi-nccl 1.13.2-aws
    # [0] NCCL INFO NET/OFI Using CUDA driver version 12060 with runtime 12010

    # cudaDriverVersion 12060  --> This is max supported cuda version by nvidia driver
    # NCCL version 2.23.4+cuda12.5 --> This is NCCL version compiled with cuda version

    # Validation of logs
    grep "NET/OFI Configuring AWS-specific options" ${TRAINING_LOG} || { echo "AWS-specific options text not found"; exit 1; }
    grep "busbw" ${TRAINING_LOG} || { echo "busbw text not found"; exit 1; }
    grep "Avg bus bandwidth " ${TRAINING_LOG} || { echo "Avg bus bandwidth text not found"; exit 1; }
    grep "NCCL version $NCCL_VERSION" ${TRAINING_LOG} || { echo "Text not found: NCCL version $NCCL_VERSION"; exit 1; }
    if [[ ${INSTANCE_TYPE} == "p4d.24xlarge" ]]; then
        grep "NET/Libfabric/0/GDRDMA" ${TRAINING_LOG} || { echo "Text not found: NET/Libfabric/0/GDRDMA"; exit 1; }
        grep "NET/OFI Selected Provider is efa (found 4 nics)" ${TRAINING_LOG} || { echo "Selected Provider is efa text not found"; exit 1; }
    elif [[ ${INSTANCE_TYPE} == "p4de.24xlarge" ]]; then
        grep "NET/Libfabric/0/GDRDMA" ${TRAINING_LOG} || { echo "Avg bus bandwidth text not found"; exit 1; }
        grep "NET/OFI Selected Provider is efa (found 4 nics)" ${TRAINING_LOG} || { echo "Avg bus bandwidth text not found"; exit 1; }
    elif [[ ${INSTANCE_TYPE} == "p5.48xlarge" ]]; then
        grep "NET/Libfabric/0/GDRDMA" ${TRAINING_LOG} || { echo "Avg bus bandwidth text not found"; exit 1; }
        grep "NET/OFI Selected Provider is efa (found 32 nics)" ${TRAINING_LOG} || { echo "Avg bus bandwidth text not found"; exit 1; }
    elif [[ ${INSTANCE_TYPE} == "p5e.48xlarge" ]]; then
        grep "NET/Libfabric/0/GDRDMA" ${TRAINING_LOG} || { echo "Avg bus bandwidth text not found"; exit 1; }
        grep "NET/OFI Selected Provider is efa (found 32 nics)" ${TRAINING_LOG} || { echo "Avg bus bandwidth text not found"; exit 1; }
    elif [[ ${INSTANCE_TYPE} == "p5en.48xlarge" ]]; then
        grep "NET/Libfabric/0/GDRDMA" ${TRAINING_LOG} || { echo "Avg bus bandwidth text not found"; exit 1; }
        grep "NET/OFI Selected Provider is efa (found 16 nics)" ${TRAINING_LOG} || { echo "Avg bus bandwidth text not found"; exit 1; }
    elif [[ ${INSTANCE_TYPE} == "p3dn.24xlarge" ]]; then
        grep "NET/OFI Selected Provider is efa (found 4 nics)" ${TRAINING_LOG} || { echo "Selected Provider is efa text not found"; exit 1; }
    fi
    echo "***************************** check_efa_nccl_all_reduce passed for cuda version ${CUDA_VERSION} *****************************"
else
    echo "***************************** check_efa_nccl_all_reduce failed for cuda version ${CUDA_VERSION} *****************************"
fi

```

- To access the benchmark data, we can parse the final row of table output from the Multi Node all_reduce test:

```
benchmark=$(sudo cat ${TRAINING_LOG} | grep '1073741824' | tail -n1 | awk -F " " '{{print $12}}' | sed 's/ //' | sed  's/  5e-07//')
if [[ -z "${benchmark}" ]]; then
  echo "benchmark variable is empty"
  exit 1
fi

echo "Benchmark throughput: ${benchmark}"
```
