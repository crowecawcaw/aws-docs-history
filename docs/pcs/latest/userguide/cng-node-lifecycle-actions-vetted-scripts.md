# Use AWS-maintained scripts for node lifecycle actions in AWS PCS

AWS publishes maintained scripts for common lifecycle actions. You reference a maintained
script directly from your compute node group configuration. The scripts are idempotent and safe to
run on every boot.

AWS distributes the scripts from a public, AWS-managed Amazon S3 bucket in each
AWS Region. You reference a script by its Amazon S3 URI. You reference a maintained script the
same way you reference your own script. You can reference the scripts directly from the
AWS-managed bucket.

## Available scripts

| **Script**                     | **Description**                                                                                                                                    | **Prerequisite packages**                                                                          |
| ------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `mount-efs.sh`                 | Mounts an Amazon EFS file system at a specified path and persists it across<br>reboots.                                                            | `amazon-efs-utils`, `nfs-utils`                                                                    |
| `mount-fsx-lustre.sh`          | Mounts an Amazon FSx for Lustre file system at a specified path and persists it<br>across reboots.                                                 | `lustre-client`                                                                                    |
| `configure-efs-homes.sh`       | Mounts an Amazon EFS file system as the home-directory base and configures PAM so<br>each user's home directory is created on first login.         | `amazon-efs-utils`, `nfs-utils`, and PAM<br>`mkhomedir` packages (see the per-script requirements) |
| `configure-ldaps.sh`           | Configures SSSD for LDAP or LDAPS authentication, with support for authenticated<br>bind (credentials from AWS Secrets Manager) or anonymous bind. | `sssd`, `sssd-ldap`, `sssd-tools`, and related<br>packages (see the per-script requirements)       |
| `configure-cloudwatch-logs.sh` | Configures the Amazon CloudWatch agent to forward the node's lifecycle action<br>logs to Amazon CloudWatch Logs.                                   | `amazon-cloudwatch-agent`                                                                          |

###### Important

These scripts do not install their prerequisite packages. Install the required packages in
your AMI before you use a script. A script fails if a prerequisite is missing. Some scripts
require the node's instance role to have specific permissions. See the requirements for each
script.

## Reference a script

Reference a script by its Amazon S3 URI in the `scriptLocation` field of a
lifecycle action. The scripts are stored under the `aws-pcs-node-lifecycle-scripts`
prefix of the AWS-managed `aws-pcs-repo-`region`` bucket in
each AWS Region. Use the bucket in the same AWS Region as your cluster.

```
s3://aws-pcs-repo-`region`/aws-pcs-node-lifecycle-scripts/`script`-v`version`.sh
```

Each script is versioned with [semantic versioning](https://semver.org/ "https://semver.org/").
You can pin a specific version or track the latest release within a major version:

- **Pin a specific version** — Use the full semantic
  version, such as `mount-efs-v1.0.0.sh`. The content at a specific version is
  immutable. Use a pinned version for production.
- **Track the latest version** — Use the major-version
  alias, such as `mount-efs-v1-latest.sh`. The alias points to the newest release
  within that major version. Pair it with `scriptCachingPolicy`
  `REFRESH_ON_REBOOT` to pick up updates on reboot.

Every script has a companion SHA-256 checksum file at the same location with a
`.sha256` suffix (for example,
`mount-efs-v1.0.0.sh.sha256`). Read the `.sha256` value and set it as the
script's `checksum`. The agent then verifies the script's integrity on download. For
more information, see [Script integrity (checksums)](cng-node-lifecycle-actions-configure.md#cng-node-lifecycle-actions-configure-checksums "cng-node-lifecycle-actions-configure.md#cng-node-lifecycle-actions-configure-checksums").

## Available script versions

AWS versions each script independently. The following tables list the available versions of
each script. Use a version in the script's Amazon S3 URI, as described in [Reference a script](#cng-node-lifecycle-actions-vetted-scripts-reference "#cng-node-lifecycle-actions-vetted-scripts-reference").

### `mount-efs.sh`

| **Version** | **Release date** | **Release notes** |
| ----------- | ---------------- | ----------------- |
| 1.0.0       | July 23, 2026    | Initial release.  |

### `mount-fsx-lustre.sh`

| **Version** | **Release date** | **Release notes** |
| ----------- | ---------------- | ----------------- |
| 1.0.0       | July 23, 2026    | Initial release.  |

### `configure-efs-homes.sh`

| **Version** | **Release date** | **Release notes** |
| ----------- | ---------------- | ----------------- |
| 1.0.0       | July 23, 2026    | Initial release.  |

### `configure-ldaps.sh`

| **Version** | **Release date** | **Release notes** |
| ----------- | ---------------- | ----------------- |
| 1.0.0       | July 23, 2026    | Initial release.  |

### `configure-cloudwatch-logs.sh`

| **Version** | **Release date** | **Release notes** |
| ----------- | ---------------- | ----------------- |
| 1.0.0       | July 23, 2026    | Initial release.  |

## Example: Mount an EFS file system with a maintained script

The following example references the maintained `mount-efs.sh` script in the
`us-west-2` AWS Region. You pass arguments as named flags. For the script's arguments,
see [Script arguments](#cng-node-lifecycle-actions-vetted-scripts-args "#cng-node-lifecycle-actions-vetted-scripts-args").

```
aws pcs update-compute-node-group \
  --cluster-identifier `my-cluster` \
  --compute-node-group-identifier `my-cng` \
  --node-lifecycle-actions '{
    "stages": {
      "nodeBootstrapped": [
        {
          "name": "Mount EFS home directory",
          "scriptSource": {
            "scriptLocation": "s3://aws-pcs-repo-us-west-2/aws-pcs-node-lifecycle-scripts/mount-efs-v1.0.0.sh"
          },
          "arguments": ["--file-system-id", "fs-`12345678`", "--mount-point", "/shared"],
          "onError": "TERMINATE",
          "executionPolicy": "EVERY_BOOT"
        }
      ]
    }
  }'
```

The node's instance role must have `s3:GetObject` permission for the script
object. Nodes in a private subnet can reach the bucket through an S3 gateway VPC endpoint. For
more information, see [Script storage locations](cng-node-lifecycle-actions-configure.md#cng-node-lifecycle-actions-configure-storage "cng-node-lifecycle-actions-configure.md#cng-node-lifecycle-actions-configure-storage").

## Script arguments

Each script takes named-flag arguments. Pass each flag and its value as separate elements of
the `arguments` array (for example, `["--file-system-id", "fs-12345678"]`).
All scripts run as `root` and support the AL2, AL2023, RHEL, Ubuntu, and Rocky Linux
operating systems.

### `mount-efs.sh`

| **Flag**           | **Required** | **Default** | **Description**                                                                                     |
| ------------------ | ------------ | ----------- | --------------------------------------------------------------------------------------------------- |
| `--file-system-id` | Yes          | —           | EFS file system ID, such as `fs-0123456789abcdef0`.                                                 |
| `--mount-point`    | Yes          | —           | Absolute path to mount at, such as `/mnt/efs`.                                                      |
| `--options`        | No           | `tls,iam`   | Comma-separated mount options. The default enables encryption in transit and IAM<br>authentication. |

With the default `iam` option, the node's instance role must allow
`elasticfilesystem:ClientMount` and `elasticfilesystem:ClientWrite`. The
node's subnet must have an EFS mount target whose security group allows inbound NFS (TCP 2049)
from the node.

### `mount-fsx-lustre.sh`

| **Flag**         | **Required** | **Default**     | **Description**                                                                          |
| ---------------- | ------------ | --------------- | ---------------------------------------------------------------------------------------- |
| `--fsx-dns-name` | Yes          | —               | FSx for Lustre file system DNS name.                                                     |
| `--mount-name`   | Yes          | —               | The file system's Lustre mount name (the `MountName` value from the<br>FSx console).     |
| `--mount-point`  | Yes          | —               | Absolute path to mount at, such as `/fsx`.                                               |
| `--options`      | No           | `noatime,flock` | Comma-separated mount options. The default follows the FSx for Lustre<br>recommendation. |

The node's subnet must reach the file system, and the file system's security group must
allow inbound Lustre traffic (TCP 988, and 1018–1023 for clients that use reserved source
ports) from the node.

### `configure-efs-homes.sh`

| **Flag**      | **Required** | **Default** | **Description**                                                                                     |
| ------------- | ------------ | ----------- | --------------------------------------------------------------------------------------------------- |
| `--efs-id`    | Yes          | —           | EFS file system ID, such as `fs-0123456789abcdef0`.                                                 |
| `--home-base` | No           | `/home`     | Absolute path to mount the EFS file system at and create home directories<br>under.                 |
| `--options`   | No           | `tls,iam`   | Comma-separated mount options. The default enables encryption in transit and IAM<br>authentication. |

This script requires `amazon-efs-utils`, `nfs-utils`, and PAM
`mkhomedir` support. On RHEL-family nodes, install `oddjob`,
`oddjob-mkhomedir`, and `authselect`. On AL2023, install
`authselect` explicitly. On Ubuntu, install `libpam-modules`. IAM and
network requirements match `mount-efs.sh`.

### `configure-ldaps.sh`

| **Flag**        | **Required** | **Description**                                                                                                                                      |
| --------------- | ------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| `--ldap-uri`    | Yes          | LDAP server URI. Must start with `ldap://` or<br>`ldaps://`.                                                                                         |
| `--search-base` | Yes          | LDAP search base, such as `dc=example,dc=com`.                                                                                                       |
| `--secret-arn`  | No           | AWS Secrets Manager ARN of the secret that holds the bind credentials. When<br>you omit this flag, the script configures SSSD for an anonymous bind. |
| `--tls-cacert`  | No           | Absolute path to a CA bundle for TLS verification. Defaults to the operating<br>system's CA bundle.                                                  |

This script requires `sssd`, `sssd-ldap`, and `sssd-tools`.
On RHEL-family nodes, it also requires `authselect` or `authconfig` and
`oddjob-mkhomedir`. On Ubuntu, it requires `libpam-modules`.

With `--secret-arn`, the node's instance role must allow
`secretsmanager:GetSecretValue` for the secret, and the node needs the
`awscli` and `python3` packages. The secret's value must be JSON of the
form `{"username": "<bind-dn>", "password": "<bind-password>"}`. Anonymous
bind makes no AWS API calls and needs no IAM permissions.

### `configure-cloudwatch-logs.sh`

| **Flag**           | **Required** | **Default**                            | **Description**                                                                                                                                                |
| ------------------ | ------------ | -------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `--log-group-name` | No           | `/aws/pcs/${PCS_CLUSTER_ID}/lifecycle` | The CloudWatch Logs log group to forward to. When omitted, the script derives<br>the name from the `PCS_CLUSTER_ID` environment variable that AWS PCS<br>sets. |

The script forwards the lifecycle action log directory
(`/var/log/amazon/pcs/lifecycle/actions`). The node's instance role must allow
`logs:CreateLogGroup`, `logs:CreateLogStream`, and
`logs:PutLogEvents` on the target log group. Use this script to forward logs
off-instance for post-mortem debugging.

###### Note

The Amazon CloudWatch agent must run as `root` to forward these logs. Only the
`root` user can read `/var/log/amazon/pcs/lifecycle/actions`.
