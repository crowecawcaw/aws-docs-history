

# Getting started on Linux

On Linux, you install AWS Emulator as a native package and run it as a local process. The package installs the emulator in `/opt/aws-emulator/` and adds the `aws-emulator` command to `/usr/bin/`, so the command is on your `PATH`.

First, check what you need in [Setting up AWS Emulator](setting-up.md).

## To install AWS Emulator
<a name="getting-started-linux-install"></a>

1. Download and install the package for your system. The commands differ by package type and processor.

    **RPM package (x86\_64)** 

   ```bash
   sudo dnf install -y https://downloads.aws.com/aws-emulator/packages/aws-emulator/LTS/latest/aws-emulator-x86_64.rpm
   ```

    **RPM package (aarch64)** 

   ```bash
   sudo dnf install -y https://downloads.aws.com/aws-emulator/packages/aws-emulator/LTS/latest/aws-emulator-aarch64.rpm
   ```

    **Debian package (amd64)** 

   ```bash
   curl -fsSLo aws-emulator.deb https://downloads.aws.com/aws-emulator/packages/aws-emulator/LTS/latest/aws-emulator_amd64.deb
   sudo apt-get install -y ./aws-emulator.deb
   ```

    **Debian package (arm64)** 

   ```bash
   curl -fsSLo aws-emulator.deb https://downloads.aws.com/aws-emulator/packages/aws-emulator/LTS/latest/aws-emulator_arm64.deb
   sudo apt-get install -y ./aws-emulator.deb
   ```

   On Amazon Linux 2, use `yum` for the RPM commands on this page.

   The package also installs the license and notice files for AWS Emulator.

   These commands install the latest release. To install a specific version, see [Finding and installing a specific version](versioning.md#versioning-list). To check the package before you install it, see [To verify the package before you install it (optional)](#getting-started-linux-verify).

1. Confirm the installation. The command prints the version. For what it shows, see [Version numbers](versioning.md#versioning-numbers).

   ```bash
   aws-emulator -v
   ```

## To verify the package before you install it (optional)
<a name="getting-started-linux-verify"></a>

 AWS signs each package. The signature is in a file next to the package, with the same name plus `.sig`. To check that a package comes from AWS and wasn’t changed, verify it before you install it. You need GnuPG (`gpg`), which most Linux distributions include.

1. Download the package and its signature file. The following example uses the RPM package for x86\_64. For another package, change the file name in `PACKAGE_FILE`.

   ```bash
   PACKAGE_FILE=aws-emulator-x86_64.rpm
   curl -fsSLO https://downloads.aws.com/aws-emulator/packages/aws-emulator/LTS/latest/$PACKAGE_FILE
   curl -fsSLO https://downloads.aws.com/aws-emulator/packages/aws-emulator/LTS/latest/$PACKAGE_FILE.sig
   ```

1. Import the public key.

   ```bash
   curl -fsSLo aws-publishing.asc https://downloads.aws.com/keys/gpg/current.asc
   gpg --import aws-publishing.asc
   ```

1. Check the fingerprint of the key.

   ```bash
   gpg --fingerprint ssm-publishing@amazon.com
   ```

   The fingerprint must be `98BC F336 A3BE 53B7 34E9 67C5 2E5B F49B D940 F624`. If it’s different, don’t install the package.

1. Verify the signature.

   ```bash
   gpg --verify $PACKAGE_FILE.sig $PACKAGE_FILE
   ```

   The output includes `Good signature from "SSM Publishing <[ssm-publishing@amazon.com](mailto:ssm-publishing@amazon.com)>"`. It also warns that the key isn’t certified with a trusted signature. You can ignore this warning, because you checked the fingerprint. If the output says `BAD signature`, delete both files, and don’t install the package.

1. Install the file that you verified.

    **RPM package** 

   ```bash
   sudo dnf install -y ./$PACKAGE_FILE
   ```

    **Debian package** 

   ```bash
   sudo apt-get install -y ./$PACKAGE_FILE
   ```

## To start and stop AWS Emulator
<a name="getting-started-linux-run"></a>

1. Start the emulator.

   ```bash
   aws-emulator
   ```

   The emulator keeps running in that terminal. The startup line of its log gives the address and port that it serves on, and you can rely on it in scripts. For what the log contains, see [Output](cli-reference.md#cli-reference-output).

   By default, the emulator serves HTTPS on `127.0.0.1:9297`, so only your own machine can reach it. For all options, see [AWS Emulator command reference](cli-reference.md).

1. In another terminal, set the environment variables for your SDK, and then run your code. For example, set `AWS_CONFIG_FILE` to `~/.aws/emulator/9297/config` and `AWS_SHARED_CREDENTIALS_FILE` to `~/.aws/emulator/9297/emulator_credentials`. For the full list, see [To point your SDK at a local emulator](point-sdk-to-emulator.md#point-sdk-env). For Java, also see [To trust the emulator certificate in Java](point-sdk-to-emulator.md#point-sdk-ca-java).

1. To stop the emulator, press **Ctrl\+C** in its terminal, or send the process a `SIGTERM` signal. The emulator stops cleanly and deletes the files that it created in `~/.aws/emulator/<port>/`. It also deletes all emulated resources, because it keeps them only in memory.

## To use a different port
<a name="getting-started-linux-port"></a>

If another program already uses port 9297, the emulator can’t start. For the error that it prints, see [When the port is in use](cli-reference.md#cli-reference-port-in-use). To fix this, choose another port when you start the emulator.
+ To use a specific port, run `aws-emulator -p <port>`. For example, run `aws-emulator -p 9300`.
+ To let the operating system choose a free port, run `aws-emulator -p 0`. Then read the port from the `endpoint_url` field of the startup line in the log.

You can run several emulators side by side. Give each one a different port with `-p`, or use `-p 0` for each one. Each emulator keeps its own files in `~/.aws/emulator/<port>/`, and its own resources. When you set the environment variables for an emulator, use that emulator’s port in each one.

## To limit the memory of the emulator on Linux
<a name="getting-started-linux-memory"></a>

The emulator keeps emulated resources in memory. It uses about 160 MiB when idle and grows as your tests create resources. You can cap its memory with a systemd scope. This needs a systemd user session on cgroup v2. Amazon Linux 2 and many containers don’t have one. On those systems, use Docker instead, as described in [To run AWS Emulator in a container](getting-started-docker.md#getting-started-docker-run).

1. Start the emulator with the following `systemd-run` command. It sets a limit of 2 GiB, and `MemorySwapMax=0` keeps the emulator out of swap.

   ```bash
   systemd-run --user --scope -p MemoryMax=2G -p MemorySwapMax=0 aws-emulator
   ```

   The emulator runs in the foreground, as it does without the limit.

1. If the emulator goes over the limit, the kernel stops it with exit code 137. You lose the emulated resources. To start again with empty state, run the command again.

## To uninstall AWS Emulator
<a name="getting-started-linux-uninstall"></a>

1. Stop any running emulator.

1. Remove the package.

    **RPM systems** 

   ```bash
   sudo dnf remove -y aws-emulator
   ```

    **Debian systems** 

   ```bash
   sudo apt-get remove -y aws-emulator
   ```

1. (Optional) Delete the files the emulator keeps in your home directory.
**Important**  
This command deletes all the files that the emulator keeps in your home directory. Do this only when you’re done with the emulator.

   ```bash
   rm -rf ~/.aws/emulator
   ```