# Updating the AWS Systems Manager agent and Amazon ECS container

agent on an external instance

Your on-premises server or VM must run both the AWS Systems Manager Agent (SSM Agent) and the Amazon ECS
container agent when running Amazon ECS workloads. AWS releases new versions of these agents
when any capabilities are added or updated. If your external instances are using an earlier
version of either agent, you can update them using the following procedures.

## Updating the SSM Agent on an external

instance

AWS Systems Manager recommends that you automate the process of updating the SSM Agent on your
instances. They provide several methods to automate updates. For more information, see
[Automating
updates to SSM Agent](../../../systems-manager/latest/userguide/ssm-agent-automatic-updates.md "../../../systems-manager/latest/userguide/ssm-agent-automatic-updates.md") in the _AWS Systems Manager User Guide_.

## Updating the Amazon ECS agent on an external

instance

On your external instances, the Amazon ECS container agent is updated by upgrading the
`ecs-init` package. Updating the Amazon ECS agent doesn't interrupt the
running tasks or services. Amazon ECS provides the `ecs-init` package and
signature file in an Amazon S3 bucket in each Region. Beginning with `ecs-init`
version `1.52.1-1`, Amazon ECS provides separate `ecs-init` packages
for use depending on the operating system and system architecture your external instance
uses.

Use the following table to determine the `ecs-init` package that you should
download based on the operating system and system architecture your external instance
uses.

###### Note

You can determine which operating system and system architecture that your
external instance uses by using the following commands.

```
cat /etc/os-release
uname -m
```

| Operating systems (architecture)                                                                                                                                                    | ecs-init package                     |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------ |
| CentOS 7 (x86_64)<br>CentOS 8 (x86_64)<br>CentOS Stream 9 (x86_64)<br>SUSE Enterprise Server 15 (x86_64)<br>RHEL 7 (x86_64)<br>RHEL 8 (x86_64)                                      | `amazon-ecs-init-latest.x86_64.rpm`  |
| CentOS 7 (aarch64)<br>CentOS 8 (aarch64)<br>CentOS Stream 9 (aarch64)<br>RHEL 7 (aarch64)                                                                                           | `amazon-ecs-init-latest.aarch64.rpm` |
| Debian 9 (x86_64)<br>Debian 10 (x86_64)<br>Debian 11 (x86_64)<br>Debian 12 (x86_64)<br>Ubuntu 18 (x86_64)<br>Ubuntu 20 (x86_64)<br>Ubuntu 22 (x86_64)<br>Ubuntu 24 (x86_64)         | `amazon-ecs-init-latest.amd64.deb`   |
| Debian 9 (aarch64)<br>Debian 10 (aarch64)<br>Debian 11 (aarch64)<br>Debian 12 (aarch64)<br>Ubuntu 18 (aarch64)<br>Ubuntu 20 (aarch64)<br>Ubuntu 22 (aarch64)<br>Ubuntu 24 (aarch64) | `amazon-ecs-init-latest.arm64.deb`   |

Follow these steps to update the Amazon ECS agent.

###### To update the Amazon ECS agent

1. Confirm the Amazon ECS agent version that you're running.

```
`curl -s 127.0.0.1:51678/v1/metadata | python3 -mjson.tool`
```

2. Download the `ecs-init` package for your operating system and
   system architecture. Amazon ECS provides the `ecs-init` package file in an
   Amazon S3 bucket in each Region. Make sure that you replace the
   `<region>` identifier in the command with the
   Region name (for example, `us-west-2`) that you're geographically
   closest to.

**amazon-ecs-init-latest.x86_64.rpm**

```
`curl -o amazon-ecs-init.rpm https://s3.`<region>`.amazonaws.com/amazon-ecs-agent-`<region>`/amazon-ecs-init-latest.x86_64.rpm`
```

**amazon-ecs-init-latest.aarch64.rpm**

```
`curl -o amazon-ecs-init.rpm https://s3.`<region>`.amazonaws.com/amazon-ecs-agent-`<region>`/amazon-ecs-init-latest.aarch64.rpm`
```

**amazon-ecs-init-latest.amd64.deb**

```
`curl -o amazon-ecs-init.deb https://s3.`<region>`.amazonaws.com/amazon-ecs-agent-`<region>`/amazon-ecs-init-latest.amd64.deb`
```

**amazon-ecs-init-latest.arm64.deb**

```
`curl -o amazon-ecs-init.deb https://s3.`<region>`.amazonaws.com/amazon-ecs-agent-`<region>`/amazon-ecs-init-latest.arm64.deb`
```

3. (Optional) Verify the validity of the `ecs-init` package file using
   the PGP signature.
   1. Download and install GnuPG. For more information about GNUpg, see the
      [GnuPG website](https://www.gnupg.org "https://www.gnupg.org"). For Linux
      systems, install `gpg` using the package manager on your
      flavor of Linux.
   2. Retrieve the Amazon ECS PGP public key.

   ```
   `gpg --keyserver hkp://keys.gnupg.net:80 --recv BCE9D9A42D51784F`
   ```

   3. Download the `ecs-init` package signature. The signature is
      an ASCII detached PGP signature that's stored in a file with the
      `.asc` extension. Amazon ECS provides the signature file in an
      Amazon S3 bucket in each Region. Make sure that you replace the
      `<region>` identifier in the command
      with the Region name (for example, `us-west-2`) that you're
      geographically closest to.

   **amazon-ecs-init-latest.x86_64.rpm**

   ```
   `curl -o amazon-ecs-init.rpm.asc https://s3.`<region>`.amazonaws.com/amazon-ecs-agent-`<region>`/amazon-ecs-init-latest.x86_64.rpm.asc`
   ```

   **amazon-ecs-init-latest.aarch64.rpm**

   ```
   `curl -o amazon-ecs-init.rpm.asc https://s3.`<region>`.amazonaws.com/amazon-ecs-agent-`<region>`/amazon-ecs-init-latest.aarch64.rpm.asc`
   ```

   **amazon-ecs-init-latest.amd64.deb**

   ```
   `curl -o amazon-ecs-init.deb.asc https://s3.`<region>`.amazonaws.com/amazon-ecs-agent-`<region>`/amazon-ecs-init-latest.amd64.deb.asc`
   ```

   **amazon-ecs-init-latest.arm64.deb**

   ```
   `curl -o amazon-ecs-init.deb.asc https://s3.`<region>`.amazonaws.com/amazon-ecs-agent-`<region>`/amazon-ecs-init-latest.arm64.deb.asc`
   ```

   4. Verify the `ecs-init` package file using the key.

   **For the `rpm`
   packages**

   ```
   `gpg --verify amazon-ecs-init.rpm.asc ./amazon-ecs-init.rpm`
   ```

   **For the `deb`
   packages**

   ```
   `gpg --verify amazon-ecs-init.deb.asc ./amazon-ecs-init.deb`
   ```

   The following is the expected output.

   ```
   gpg: Signature made Fri 14 May 2021 09:31:36 PM UTC
   gpg:                using RSA key 50DECCC4710E61AF
   gpg: Good signature from "Amazon ECS <ecs-security@amazon.com>" [unknown]
   gpg: WARNING: This key is not certified with a trusted signature!
   gpg:          There is no indication that the signature belongs to the owner.
   Primary key fingerprint: F34C 3DDA E729 26B0 79BE  AEC6 BCE9 D9A4 2D51 784F
        Subkey fingerprint: D64B B6F9 0CF3 77E9 B5FB  346F 50DE CCC4 710E 61AF
   ```

4. Install the `ecs-init` package.

**For the `rpm` package on CentOS 7, CentOS 8,
and RHEL 7**

```
`sudo yum install -y ./amazon-ecs-init.rpm`
```

**For the `rpm` package on SUSE Enterprise
Server 15**

```
`sudo zypper install -y --allow-unsigned-rpm ./amazon-ecs-init.rpm`
```

**For the `deb` package**

```
`sudo dpkg -i ./amazon-ecs-init.deb`
```

5. Restart the `ecs` service.

```
`sudo systemctl restart ecs`
```

6. Verify the Amazon ECS agent version was updated.

```
`curl -s 127.0.0.1:51678/v1/metadata | python3 -mjson.tool`
```
