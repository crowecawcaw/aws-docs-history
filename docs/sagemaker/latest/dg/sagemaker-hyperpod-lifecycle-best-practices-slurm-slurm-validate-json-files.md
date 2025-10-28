# Validating the JSON configuration files before creating a Slurm cluster on

HyperPod

To validate the JSON configuration files before submitting a cluster creation request,
use the configuration validation script [`validate-config.py`](https://github.com/aws-samples/awsome-distributed-training/blob/main/1.architectures/5.sagemaker-hyperpod/validate-config.py "https://github.com/aws-samples/awsome-distributed-training/blob/main/1.architectures/5.sagemaker-hyperpod/validate-config.py"). This script parses and compares your
HyperPod cluster configuration JSON file and Slurm configuration JSON file, and
identifies if there's any resource misconfiguration between the two files and also
across Amazon EC2, Amazon VPC, and Amazon FSx resources. For example, to validate the
`create_cluster.json` and `provisioning_parameters.json` files
from the [Base lifecycle scripts provided by HyperPod](sagemaker-hyperpod-lifecycle-best-practices-slurm-slurm-base-config.md "sagemaker-hyperpod-lifecycle-best-practices-slurm-slurm-base-config.md")
section, run the validation script as follows.

```
python3 validate-config.py --cluster-config `create_cluster.json` --provisioning-parameters `provisioning_parameters.json`
```

The following is an example output of a successful validation.

```
✔️  Validated instance group name worker-group-1 is correct ...

✔️  Validated subnet subnet-012345abcdef67890 ...
✔️  Validated security group sg-012345abcdef67890 ingress rules ...
✔️  Validated security group sg-012345abcdef67890 egress rules ...
✔️  Validated FSx Lustre DNS name fs-012345abcdef67890.fsx.us-east-1.amazonaws.com
✔️  Validated FSx Lustre mount name abcdefgh
✅ Cluster Validation succeeded
```
