# `LoginNodes` section

###### Note

Support for `LoginNodes` is added in AWS ParallelCluster version 3.7.0.

**(Optional)** Specifies the configuration for the login nodes pool.

```
LoginNodes:
  Pools:
    - Name: `string`
      Count: `integer`
      InstanceType: `string`
      GracetimePeriod: `integer`
      Image:
        CustomAmi: `string`
      Ssh:
        KeyName: `string`
        AllowedIps: `string`
      Networking:
        SubnetIds:
          - `string`
        SecurityGroups:
          - `string`
        AdditionalSecurityGroups:
          - `string`
      Dcv:
        Enabled: `boolean`
        Port: `integer`
        AllowedIps: `string`
      CustomActions:
        OnNodeStart:
          Sequence:
            - Script: `string`
              Args:
                - `string`
          Script: `string`
          Args:
            - `string`
        OnNodeConfigured:
          Sequence:
            - Script: `string`
              Args:
                - `string`
          Script: `string`
          Args:
            - `string`
        OnNodeUpdated:
          Sequence:
            - Script: `string`
              Args:
                - `string`
          Script: `string`
          Args:
            - `string`
      Iam:
        InstanceRole: `string`
        InstanceProfile: `string`
        AdditionalIamPolicies:
          - Policy: `string`
```

[Update policy: The login
nodes in the cluster must be stopped for this setting to be changed for an update.](using-pcluster-update-cluster-v3.md#update-policy-update-login-node-cluster "using-pcluster-update-cluster-v3.md#update-policy-update-login-node-cluster")

## `LoginNodes` properties

### `Pools` properties

Defines groups of login nodes that have the same resource configuration. Starting with AWS ParallelCluster
3.11.0 up to 10 pools can be specified.

```
Pools:
  - Name: `string`
    Count: `integer`
    InstanceType: `string`
    GracetimePeriod: `integer`
    Image:
      CustomAmi: `string`
    Ssh:
      KeyName: `string`
      AllowedIps: `string`
    Networking:
      SubnetIds:
        - `string`
      SecurityGroups:
        - `string`
      AdditionalSecurityGroups:
        - `string`
    Dcv:
      Enabled: `boolean`
      Port: `integer`
      AllowedIps: `string`
    CustomActions:
      OnNodeStart:
        Sequence:
          - Script: `string`
            Args:
              - `string`
        Script: `string`
        Args:
          - `string`
      OnNodeConfigured:
        Sequence:
          - Script: `string`
            Args:
              - `string`
        Script: `string`
        Args:
          - `string`
      OnNodeUpdated:
        Sequence:
          - Script: `string`
            Args:
              - `string`
        Script: `string`
        Args:
          - `string`
    Iam:
      InstanceRole: `string`
      InstanceProfile: `string`
      AdditionalIamPolicies:
        - Policy: `string`
```

[Update policy: Login node pools can be added, but removing a pool requires all login nodes in the cluster are stopped.](using-pcluster-update-cluster-v3.md#update-policy-add-login-node-pools "using-pcluster-update-cluster-v3.md#update-policy-add-login-node-pools")

`Name` (**Required** `String`)

Specifies the name of the `LoginNodes` pool. This is used to tag the `LoginNodes` resources.

[Update policy: If this setting is
changed, the update is not allowed.](using-pcluster-update-cluster-v3.md#update-policy-fail-v3 "using-pcluster-update-cluster-v3.md#update-policy-fail-v3")

###### Note

Starting with AWS ParallelCluster version 3.11.0, the update policy is: The login nodes in the pool must be stopped for this setting to be changed for an update.

`Count` (**Required** `Integer`)

Specifies the number of login nodes to keep active.

[Update policy: This
setting can be changed during an update.](using-pcluster-update-cluster-v3.md#update-policy-setting-supported-v3 "using-pcluster-update-cluster-v3.md#update-policy-setting-supported-v3")

`InstanceType` (**Required** `String`)

Specifies the Amazon EC2 instance type that's used for the login node. The architecture of the instance type must be the same as the
architecture used for Slurm `InstanceType` setting.

[Update policy](using-pcluster-update-cluster-v3.md#update-policy-setting-supported-v3 "using-pcluster-update-cluster-v3.md#update-policy-setting-supported-v3"): This setting can be changed if the login nodes pool is stopped.

###### Note

Starting with AWS ParallelCluster version 3.11.0, the update policy is: The login nodes in the pool must be stopped for this setting to be changed for an update.

`GracetimePeriod` (**Optional** `Integer`)

Specifies the minimum amount of time in minutes that elapse between the notification to the logged in user that a login node is to be decommissioned and
the actual stop event. Valid values for `GracetimePeriod` are from 3 up to 120 minutes. The default is 10 minutes.

###### Note

The triggering event involves interactions between multiple AWS services. Sometimes, network latency and propagation of the information might
take some time so the grace time period may take longer than expected due to internal delays in AWS services.

[Update policy: This
setting can be changed during an update.](using-pcluster-update-cluster-v3.md#update-policy-setting-supported-v3 "using-pcluster-update-cluster-v3.md#update-policy-setting-supported-v3")

`Image` (**Optional**)

Defines the image configuration for the login nodes.

```
Image:
  CustomAmi: `String`
```

`CustomAmi` (**Optional** `String`)

Specifies the custom AMI used to provision the login nodes. If not specified, the value defaults to the one
specified in the [HeadNode section](HeadNode-v3.md "HeadNode-v3.md").

[Update policy: If this setting is
changed, the update is not allowed.](using-pcluster-update-cluster-v3.md#update-policy-fail-v3 "using-pcluster-update-cluster-v3.md#update-policy-fail-v3")

`Ssh` (**Optional**)

Defines the `ssh` configuration for the login nodes.

```
Ssh:
  KeyName: `string`
  AllowedIps: `string`
```

###### Note

Starting with AWS ParallelCluster version 3.11.0, the update policy is: The login nodes in the pool must be stopped for this setting to be changed for an update.

`KeyName` (**Optional** `String`)

Specifies the `ssh` key used to log in into the login nodes. If not specified, the value defaults to the one
specified in the [HeadNode section](HeadNode-v3.md "HeadNode-v3.md").

[Update policy: The login nodes in the pool must be stopped for this setting to be changed for an update.](using-pcluster-update-cluster-v3.md#update-policy-update-login-node-pools "using-pcluster-update-cluster-v3.md#update-policy-update-login-node-pools")

###### Important

Deprecated – The configuration parameter `LoginNodes/Pools/Ssh/KeyName`
has been deprecated, and it will be removed in future releases. The CLI now returns a warning
message when it is used in the cluster configuration. See [https://github.com/aws/aws-parallelcluster/issues/6811](https://github.com/aws/aws-parallelcluster/issues/6811 "https://github.com/aws/aws-parallelcluster/issues/6811") for details.

`AllowedIps` (**Optional** `String`)

Specifies the CIDR-formatted IP range or a prefix list id for SSH connections to login nodes in the pool. The default is the [AllowedIps](HeadNode-v3.md#yaml-HeadNode-Ssh-AllowedIps "HeadNode-v3.md#yaml-HeadNode-Ssh-AllowedIps") defined in the head node configuration, or `0.0.0.0/0` if not specified.[HeadNode section](HeadNode-v3.md "HeadNode-v3.md").

[Update policy: The login nodes in the pool must be stopped for this setting to be changed for an update.](using-pcluster-update-cluster-v3.md#update-policy-update-login-node-pools "using-pcluster-update-cluster-v3.md#update-policy-update-login-node-pools")

###### Note

Support for AllowedIps for login nodes is added in AWS ParallelCluster version 3.11.0.

`Networking` (**Required**)

```
Networking:
  SubnetIds:
    - `string`
  SecurityGroups:
    - `string`
  AdditionalSecurityGroups:
    - `string`
```

###### Note

Starting with AWS ParallelCluster version 3.11.0, the update policy is: The login nodes in the pool must be stopped for this setting to be changed for an update.

`SubnetIds` (**Required** `[String]`)

The ID of existing subnet that you provision the login nodes pool in. You can only define one subnet.

[Update policy: If this setting is
changed, the update is not allowed.](using-pcluster-update-cluster-v3.md#update-policy-fail-v3 "using-pcluster-update-cluster-v3.md#update-policy-fail-v3")

`SecurityGroups` (**Optional** `[String]`)

A list of security groups to use for the login nodes pool. If no security groups are specified, AWS ParallelCluster creates security groups for you.

[Update policy: If this setting is
changed, the update is not allowed.](using-pcluster-update-cluster-v3.md#update-policy-fail-v3 "using-pcluster-update-cluster-v3.md#update-policy-fail-v3")

`AdditionalSecurityGroups` (**Optional** `[String]`)

A list of additional security groups to use for the login nodes pool.

[Update policy: If this setting is
changed, the update is not allowed.](using-pcluster-update-cluster-v3.md#update-policy-fail-v3 "using-pcluster-update-cluster-v3.md#update-policy-fail-v3")

`Dcv` (**Optional**)

Defines configuration settings for the NICE DCV server that runs on the [login nodes](LoginNodes-v3.md "LoginNodes-v3.md"). For more information, see [Connect to the head and login nodes through Amazon DCV](dcv-v3.md "dcv-v3.md")

```
Dcv:
  Enabled: `boolean`
  Port: `integer`
  AllowedIps: `string`
```

###### Important

By default, the NICE DCV port setup by AWS ParallelCluster is open to all IPv4 addresses. You can connect to a NICE DCV port only if you have the URL for the NICE DCV session and connect to the NICE DCV session within 30 seconds of when the URL is returned from pcluster dcv-connect. Use the `AllowedIps` setting to further restrict access to the NICE DCV port with a CIDR-formatted IP range and use the Port setting to set a nonstandard port.

[Update policy: If this setting is
changed, the update is not allowed.](using-pcluster-update-cluster-v3.md#update-policy-fail-v3 "using-pcluster-update-cluster-v3.md#update-policy-fail-v3")

###### Note

Support for DCV on login nodes is added in AWS ParallelCluster version 3.11.0.

`Enabled` (**Required** `Boolean`)

Specifies whether NICE DCV is enabled on the login nodes in the pool. The default value is `false`.

[Update policy: If this setting is
changed, the update is not allowed.](using-pcluster-update-cluster-v3.md#update-policy-fail-v3 "using-pcluster-update-cluster-v3.md#update-policy-fail-v3")

###### Note

NICE DCV automatically generates a self-signed certificate that's used to secure traffic between the NICE DCV client and NICE DCV server that runs on the login node. To configure your own certificate, see [Amazon DCV HTTPS certificate](dcv-v3.md#dcv-v3-certificate "dcv-v3.md#dcv-v3-certificate").

`Port` (**Optional** `Integer`)

Specifies the port for NICE DCV. The default value is `8443`.

[Update policy: If this setting is
changed, the update is not allowed.](using-pcluster-update-cluster-v3.md#update-policy-fail-v3 "using-pcluster-update-cluster-v3.md#update-policy-fail-v3")

`AllowedIps` (**Optional** `String`)

Specifies the CIDR-formatted IP range for connections to NICE DCV. This setting is used only when AWS ParallelCluster creates the security group. The default value is `0.0.0.0/0`, which allows access from any Internet address.

[Update policy: If this setting is
changed, the update is not allowed.](using-pcluster-update-cluster-v3.md#update-policy-fail-v3 "using-pcluster-update-cluster-v3.md#update-policy-fail-v3")

`CustomActions` (**Optional**)

Specifies the custom scripts to run on the login nodes.

```
CustomActions:
  OnNodeStart:
    Sequence:
      - Script: `string`
        Args:
          - `string`
    Script: `string`
    Args:
      - `string`
  OnNodeConfigured:
    Sequence:
      - Script: `string`
        Args:
          - `string`
    Script: `string`
    Args:
      - `string`
  OnNodeUpdated:
    Sequence:
      - Script: `string`
        Args:
          - `string`
    Script: `string`
    Args:
      - `string`
```

###### Note

Support for custom actions on login nodes is added in AWS ParallelCluster version 3.11.0.

`OnNodeStart` (**Optional**)

Specifies single script or a sequence of scripts to run on the [login nodes](LoginNodes-v3.md "LoginNodes-v3.md") before any node deployment bootstrap action is started. For more information, see [Custom bootstrap actions](custom-bootstrap-actions-v3.md "custom-bootstrap-actions-v3.md").

`Sequence` (**Optional**)

List of scripts to run. AWS ParallelCluster runs the scripts in the same order as they are listed in the configuration file, starting with the first.

`Script` (**Required** `String`)

Specifies the file to use. The file path can start with `https://` or `s3://`.

`Args` (**Optional** `[String]`)

List of arguments to pass to the script.

[Update policy: If this setting is
changed, the update is not allowed.](using-pcluster-update-cluster-v3.md#update-policy-fail-v3 "using-pcluster-update-cluster-v3.md#update-policy-fail-v3")

`Script` (**Required** `String`)

Specifies the file to use for a single script. The file path can start with `https://` or `s3://`.

`Args` (**Optional** `[String]`)

List of arguments to pass to the single script.

`OnNodeConfigured` (**Optional**)

Specifies single script or a sequence of scripts to run on the [login nodes](LoginNodes-v3.md "LoginNodes-v3.md") after the node bootstrap processes are complete. For more information, see [Custom bootstrap actions](custom-bootstrap-actions-v3.md "custom-bootstrap-actions-v3.md").

`Sequence` (**Optional**)

List of scripts to run. AWS ParallelCluster runs the scripts in the same order as they are listed in the configuration file, starting with the first.

`Script` (**Required** `String`)

Specifies the file to use. The file path can start with `https://` or `s3://`.

`Args` (**Optional** `[String]`)

List of arguments to pass to the script.

[Update policy: If this setting is
changed, the update is not allowed.](using-pcluster-update-cluster-v3.md#update-policy-fail-v3 "using-pcluster-update-cluster-v3.md#update-policy-fail-v3")

`Script` (**Required** `String`)

Specifies the file to use for a single script. The file path can start with `https://` or `s3://`.

`Args` (**Optional** `[String]`)

List of arguments to pass to the single script.

[Update policy: If this setting is
changed, the update is not allowed.](using-pcluster-update-cluster-v3.md#update-policy-fail-v3 "using-pcluster-update-cluster-v3.md#update-policy-fail-v3")

`OnNodeUpdated` (**Optional**)

Specifies single script or a sequence of scripts to run after the head node update is completed and the scheduler and shared storage are aligned with the latest cluster configuration changes. For more information, see [Custom bootstrap actions](custom-bootstrap-actions-v3.md "custom-bootstrap-actions-v3.md").

`Sequence` (**Optional**)

List of scripts to run. AWS ParallelCluster runs the scripts in the same order as they are listed in the configuration file, starting with the first.

`Script` (**Required** `String`)

Specifies the file to use. The file path can start with `https://` or `s3://`.

`Args` (**Optional** `[String]`)

List of arguments to pass to the script.

`Script` (**Required** `String`)

Specifies the file to use for a single script. The file path can start with `https://` or `s3://`.

`Args` (**Optional** `[String]`)

List of arguments to pass to the single script.

[Update policy: If this setting is
changed, the update is not allowed.](using-pcluster-update-cluster-v3.md#update-policy-fail-v3 "using-pcluster-update-cluster-v3.md#update-policy-fail-v3")

###### Note

AWS ParallelCluster doesn't support including both a single script and `Sequence` for the same custom action.

`Iam` (**Optional**)

Specifies either an instance role or an instance profile to use on the login nodes to override the default instance role or instance profile for the cluster.

```
Iam:
  InstanceRole: `string`
  InstanceProfile: `string`
  AdditionalIamPolicies:
    - Policy: `string`
```

###### Note

Starting with AWS ParallelCluster version 3.11.0, the update policy is: The login nodes in the pool must be stopped for this setting to be changed for an update.

`InstanceProfile` (**Optional** `String`)

Specifies an instance profile to override the default login node instance profile. You can't specify
both `InstanceProfile` and `InstanceRole`. The format is `arn:Partition:iam::Account:instance-profile/`InstanceProfileName``.
 If this is specified, the `InstanceRole`and`AdditionalIamPolicies` settings can't be specified.

[Update policy: If this setting is
changed, the update is not allowed.](using-pcluster-update-cluster-v3.md#update-policy-fail-v3 "using-pcluster-update-cluster-v3.md#update-policy-fail-v3")

`InstanceRole` (**Optional** `String`)

Specifies an instance role to override the default login node instance role. You can't
specify both `InstanceProfile` and `InstanceRole`. The format is
`arn:Partition:iam::Account:role/RoleName`. If this is specified, the
`InstanceProfile` and `AdditionalIamPolicies` settings can't be
specified.

[Update policy: If this setting is
changed, the update is not allowed.](using-pcluster-update-cluster-v3.md#update-policy-fail-v3 "using-pcluster-update-cluster-v3.md#update-policy-fail-v3")

`AdditionalIamPolicies` (**Optional**)

```
AdditionalIamPolicies:
  - Policy: `string`
```

An IAM policy Amazon Resource Name (ARN).

Specifies a list of Amazon Resource Names (ARNs) of IAM policies for Amazon EC2. This list is attached to the root role used for the login node in addition to
the permissions that are required by AWS ParallelCluster.

An IAM policy name and its ARN are different. Names can't be used.

If this is specified, the `InstanceProfile` and `InstanceRole` settings can't be specified.
We recommend that you use `AdditionalIamPolicies` because `AdditionalIamPolicies` are added to
the permissions that AWS ParallelCluster requires, and the `InstanceRole` must include all required permissions.
The required permissions often change from release to release as features are added.

There's no default value.

[Update policy: If this setting is
changed, the update is not allowed.](using-pcluster-update-cluster-v3.md#update-policy-fail-v3 "using-pcluster-update-cluster-v3.md#update-policy-fail-v3")

`Policy` (**Required** `[String]`)

[Update policy: If this setting is
changed, the update is not allowed.](using-pcluster-update-cluster-v3.md#update-policy-fail-v3 "using-pcluster-update-cluster-v3.md#update-policy-fail-v3")
