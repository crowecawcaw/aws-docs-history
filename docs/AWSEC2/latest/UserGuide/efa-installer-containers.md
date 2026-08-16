# Install the EFA software in a container

This section covers how to use the EFA installer in a containerized environment.
You can install the EFA software either by adding commands to a Dockerfile or by
running them directly in the shell of a running container.

###### To install EFA software in a container using shell commands

1. Update the operating system packages. This step ensures that you have the latest
   packages.

   - For Debian-based operating systems:

   ```
   apt-get update && apt-get upgrade -y
   ```
   - For RHEL-based operating systems:

   ```
   yum update -y
   ```

2. Download the EFA installer. We recommend that you use the latest EFA installer.
   For information about the latest version, see
   [Elastic Fabric Adapter release notes](efa-changelog.md "efa-changelog.md").

```
mkdir /tmp/efa \
&& cd /tmp/efa \
&& curl -O https://efa-installer.amazonaws.com/aws-efa-installer-`version`.tar.gz
```

(Optional) Verify the signature of the EFA installer package.

```
wget https://efa-installer.amazonaws.com/aws-efa-installer.key \
&& gpg --import aws-efa-installer.key \
&& cat aws-efa-installer.key | gpg --fingerprint \
&& wget https://efa-installer.amazonaws.com/aws-efa-installer-`version`.tar.gz.sig \
&& gpg --verify ./aws-efa-installer-`version`.tar.gz.sig
```

3. Install the EFA software. The following command uses these arguments:

   - `--skip-kmod` — Skips kernel module installation.
     The container environment can't modify kernel modules.
   - `--skip-limit-conf` — Skips the limits configuration.
     You can't set `ulimit` inside a container. Configure this as
     part of the container creation instead.
   - `--no-verify` — Skips EFA device detection.
     The device detection uses `lspci`, which doesn't work in a
     containerized environment.

```
tar -xf aws-efa-installer-`version`.tar.gz \
&& cd aws-efa-installer \
&& ./efa_installer.sh -y --skip-kmod --skip-limit-conf --no-verify
```

###### Note

For NGC containers, with EFA installer version 1.49.0 or later you can
use the `--enable-ngc` flag instead of the three flags above.
This flag handles all container-specific configuration automatically:

```
./efa_installer.sh -y --enable-ngc
```

4. Clean up the temporary installation files.

```
rm -rf /tmp/efa
```
