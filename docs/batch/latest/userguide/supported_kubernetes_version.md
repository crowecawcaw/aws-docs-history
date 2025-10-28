# Supported Kubernetes versions

AWS Batch on Amazon EKS currently supports the following Kubernetes versions:

- `1.33`
- `1.32`
- `1.31`
- `1.30`
- `1.29`
- `1.28`
- `1.27`
- `1.26`
- `1.25`
  You might see an error message that resembles the following when you use the
  `CreateComputeEnvironment` API operation or
  `UpdateComputeEnvironment`API operation to create or update a compute environment.
  This issue occurs if you specify an unsupported Kubernetes version in
  `EC2Configuration`.

```
At least one imageKubernetesVersion in EC2Configuration is not supported.
```

To resolve this issue, delete the compute environment and then re-create it with a
supported Kubernetes version.

You can perform a minor version upgrade on your Amazon EKS cluster. For example, you can
upgrade the cluster from `1.xx` to `1.yy` even if the minor version
isn't supported.

However, the compute environment status might change to `INVALID` after a major
version update. For example, if you perform a major version upgrade from `1.xx` to
`2.yy`. If the major version isn't supported by AWS Batch, you see an error message
that resembles the following.

```
reason=CLIENT_ERROR - ... `EKS` Cluster version [`2.yy`] is unsupported
```
