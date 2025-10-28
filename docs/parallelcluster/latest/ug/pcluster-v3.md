# `pcluster`

`pcluster` is the primary AWS ParallelCluster CLI command. You use `pcluster` to launch and
manage HPC clusters in the AWS Cloud.

`pcluster` writes logs of your commands to `pcluster.log.#` files in
`/home/user/.parallelcluster/`. For more information, see [pcluster CLI logs](troubleshooting-v3-pc-cli-logs.md "troubleshooting-v3-pc-cli-logs.md").

To use `pcluster`, you must have an IAM role with the [permissions](iam-roles-in-parallelcluster-v3.md#iam-roles-in-parallelcluster-v3-example-user-policies "iam-roles-in-parallelcluster-v3.md#iam-roles-in-parallelcluster-v3-example-user-policies")
required to run it.

```
pcluster [-h]
```

## Arguments

``pcluster `command```

Possible choices: [build-image](pcluster.md "pcluster.md") |
[configure](pcluster.md "pcluster.md") |
[create-cluster](pcluster.md "pcluster.md") |
[dcv-connect](pcluster.md "pcluster.md") |
[delete-cluster](pcluster.md "pcluster.md") |
[delete-cluster-instances](pcluster.md "pcluster.md") |
[delete-image](pcluster.md "pcluster.md") |
[describe-cluster](pcluster.md "pcluster.md") |
[describe-cluster-instances](pcluster.md "pcluster.md") |
[describe-compute-fleet](pcluster.md "pcluster.md") |
[describe-image](pcluster.md "pcluster.md") |
[export-cluster-logs](pcluster.md "pcluster.md") |
[export-image-logs](pcluster.md "pcluster.md") |
[get-cluster-log-events](pcluster.md "pcluster.md") |
[get-cluster-stack-events](pcluster.md "pcluster.md") |
[get-image-log-events](pcluster.md "pcluster.md") |
[get-image-stack-events](pcluster.md "pcluster.md") |
[list-clusters](pcluster.md "pcluster.md") |
[list-cluster-log-streams](pcluster.md "pcluster.md") |
[list-images](pcluster.md "pcluster.md") |
[list-image-log-streams](pcluster.md "pcluster.md") |
[list-official-images](pcluster.md "pcluster.md") |
[ssh](pcluster.md "pcluster.md") |
[update-cluster](pcluster.md "pcluster.md") |
[update-compute-fleet](pcluster.md "pcluster.md") |
[version](pcluster.md "pcluster.md")

**Sub-commands:**

###### Topics

- [pcluster build-image](pcluster.md "pcluster.md")
- [pcluster configure](pcluster.md "pcluster.md")
- [pcluster create-cluster](pcluster.md "pcluster.md")
- [pcluster dcv-connect](pcluster.md "pcluster.md")
- [pcluster delete-cluster](pcluster.md "pcluster.md")
- [pcluster delete-cluster-instances](pcluster.md "pcluster.md")
- [pcluster delete-image](pcluster.md "pcluster.md")
- [pcluster describe-cluster](pcluster.md "pcluster.md")
- [pcluster describe-cluster-instances](pcluster.md "pcluster.md")
- [pcluster describe-compute-fleet](pcluster.md "pcluster.md")
- [pcluster describe-image](pcluster.md "pcluster.md")
- [pcluster export-cluster-logs](pcluster.md "pcluster.md")
- [pcluster export-image-logs](pcluster.md "pcluster.md")
- [pcluster get-cluster-log-events](pcluster.md "pcluster.md")
- [pcluster get-cluster-stack-events](pcluster.md "pcluster.md")
- [pcluster get-image-log-events](pcluster.md "pcluster.md")
- [pcluster get-image-stack-events](pcluster.md "pcluster.md")
- [pcluster list-clusters](pcluster.md "pcluster.md")
- [pcluster list-cluster-log-streams](pcluster.md "pcluster.md")
- [pcluster list-images](pcluster.md "pcluster.md")
- [pcluster list-image-log-streams](pcluster.md "pcluster.md")
- [pcluster list-official-images](pcluster.md "pcluster.md")
- [pcluster ssh](pcluster.md "pcluster.md")
- [pcluster update-cluster](pcluster.md "pcluster.md")
- [pcluster update-compute-fleet](pcluster.md "pcluster.md")
- [pcluster version](pcluster.md "pcluster.md")
