# `AdditionalPackages` section

**(Optional)** Used to identify additional packages to install.

```
AdditionalPackages:
  IntelSoftware:
    IntelHpcPlatform: `boolean`
```

[Update policy: If this setting is
changed, the update is not allowed.](using-pcluster-update-cluster-v3.md#update-policy-fail-v3 "using-pcluster-update-cluster-v3.md#update-policy-fail-v3")

## `IntelSoftware`

**(Optional)** Defines the configuration for Intel select
solutions.

```
IntelSoftware:
  IntelHpcPlatform: `boolean`
```

[Update policy: If this setting is
changed, the update is not allowed.](using-pcluster-update-cluster-v3.md#update-policy-fail-v3 "using-pcluster-update-cluster-v3.md#update-policy-fail-v3")

### `IntelSoftware` properties

`IntelHpcPlatform` (**Optional**, `Boolean`)

If `true`, indicates that the [End user license agreement](https://software.intel.com/en-us/articles/end-user-license-agreement "https://software.intel.com/en-us/articles/end-user-license-agreement") for Intel Parallel Studio is accepted.
This causes Intel Parallel Studio to be installed on the head node and shared
with the compute nodes. This adds several minutes to the time it takes the head
node to bootstrap.

[Update policy: If this setting is
changed, the update is not allowed.](using-pcluster-update-cluster-v3.md#update-policy-fail-v3 "using-pcluster-update-cluster-v3.md#update-policy-fail-v3")

###### Note

Starting with AWS ParallelCluster version 3.10.0 the `IntelHpcPlatform`
parameter is no longer supported.
