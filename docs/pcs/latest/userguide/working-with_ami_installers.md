# Software installers to build custom AMIs for

AWS PCS

AWS provides a downloadable file that can install the AWS PCS software on an instance.
AWS also provides software that can download, compile, and install relevant versions of Slurm
and its dependencies. You can use these instructions to build custom AMIs for use with AWS PCS
or you can use your own methods.

###### Contents

- [AWS PCS agent software installer](working-with_ami_installers.md#working-with_ami_installers_service "working-with_ami_installers.md#working-with_ami_installers_service")
- [Slurm installer](working-with_ami_installers.md#working-with_ami_installers_slurm "working-with_ami_installers.md#working-with_ami_installers_slurm")
- [Supported operating systems](working-with_ami_installers.md#working-with_ami_installers_os "working-with_ami_installers.md#working-with_ami_installers_os")
- [Supported instance types](working-with_ami_installers.md#working-wth_ami_installers_instance-types "working-with_ami_installers.md#working-wth_ami_installers_instance-types")
- [Supported Slurm versions](working-with_ami_installers.md#working-with_ami_installers_slurm-versions "working-with_ami_installers.md#working-with_ami_installers_slurm-versions")
- [Verify installers using a checksum](working-with_ami_installers.md#working-with_ami_installers_verify "working-with_ami_installers.md#working-with_ami_installers_verify")

## AWS PCS agent software installer

The AWS PCS agent software installer configures an instance to work with AWS PCS during
the instance bootstrap process. You must use AWS-provided installers to install the AWS PCS
agent on your custom AMI.

For more information about the AWS PCS agent software, see [AWS PCS agent versions](pcs-agent-versions.md "pcs-agent-versions.md").

## Slurm installer

The Slurm installer downloads, compiles, and installs relevant versions of Slurm and its
dependencies. You can use the Slurm installer to build custom AMIs for AWS PCS. You can also
use your own mechanisms if they are consistent with the software configuration that the Slurm
installer provides. For more information about AWS PCS support for Slurm, see [Slurm versions in AWS PCS](slurm-versions.md "slurm-versions.md").

The AWS-provided software installs the following:

- [Slurm](https://slurm.schedmd.com/ "https://slurm.schedmd.com/") at the requested major and maintenance
  version (currently version 25.05.x) - [License GPL 2](https://github.com/SchedMD/slurm?tab=License-1-ov-file "https://github.com/SchedMD/slurm?tab=License-1-ov-file")
  - Slurm is built with `--sysconfdir` set to `/etc/slurm`
  - Slurm is built with the option `--enable-pam` and
    `--without-munge`
  - Slurm is built with the option `--sharedstatedir=/run/slurm/`
  - Slurm is built with PMIX and JWT support
  - Slurm is installed at `/opt/aws/pcs/schedulers/slurm-25.05`

- [OpenPMIX](https://openpmix.github.io/ "https://openpmix.github.io/") (version 4.2.6) – [License](https://github.com/openpmix/openpmix?tab=License-1-ov-file "https://github.com/openpmix/openpmix?tab=License-1-ov-file")
  - OpenPMIX is installed as a subdirectory of `/opt/aws/pcs/scheduler/`

- [libjwt](https://benmcollins.github.io/libjwt/ "https://benmcollins.github.io/libjwt/") (version 1.17.0) –
  [License
  MPL-2.0](https://github.com/benmcollins/libjwt?tab=MPL-2.0-1-ov-file#readme "https://github.com/benmcollins/libjwt?tab=MPL-2.0-1-ov-file#readme")
  - libjwt is installed as a subdirectory of `/opt/aws/pcs/scheduler/`

The AWS-provided software changes the system configuration as follows:

- The Slurm `systemd` file created by the build is copied to
  `/etc/systemd/system/` with file name `slurmd-25.05.service`.
- If they don't exist, a Slurm user and group (`slurm:slurm`) are created with
  UID/GID of `401`.
- The folder `/etc/aws/pcs/scheduler/slurm-25.05/plugstack.conf.d/` is created, to store your [Extend Slurm functionality on AWS PCS with SPANK plugins](spank.md "spank.md") configuration.
- On Amazon Linux 2 and Rocky Linux 9 the installation adds the EPEL repository to install
  the required software to build Slurm or its dependencies.
- On RHEL9 the installation will enable `codeready-builder-for-rhel-9-rhui-rpms`
  and `epel-release-latest-9` from `fedoraproject` to install the required
  software to build Slurm or its dependencies.

## Supported operating systems

See [Supported operating systems in AWS PCS](operating-systems.md "operating-systems.md").

###### Note

AWS Deep Learning AMIs (DLAMI) versions based on Amazon Linux 2 and Ubuntu 22.04 should be compatible
with the AWS PCS software and Slurm installers. For more information, see [Choosing Your DLAMI](../../../dlami/latest/devguide/options.md "../../../dlami/latest/devguide/options.md") in
the _AWS Deep Learning AMIs Developer Guide_.

## Supported instance types

AWS PCS software and Slurm installers support any x86_64 or arm64 instance type than
can run one of the supported operating systems.

## Supported Slurm versions

See [Slurm versions in AWS PCS](slurm-versions.md "slurm-versions.md").

## Verify installers using a checksum

You can use SHA256 checksums to verify the installer tarball (.tar.gz) files. We recommend
that you do this to verify the identity of the software publisher and to check that the
application has not been altered or corrupted since it was published.

###### To verify a tarball

Use the **sha256sum** utility for the SHA256 checksum and
specify the tarball filename. You must run the command from the directory where you saved the
tarball file.

- SHA256

```
`$` sha256sum `tarball_filename.tar.gz`
```

The command should return a checksum value in the following format.

```
`checksum_value` `tarball_filename.tar.gz`
```

Compare the checksum value returned by the command with the checksum value provided in the
following table. If the checksums match, then it's safe to run the installation script.

###### Important

If the checksums don't match, don't run the installation script. Contact [Support](https://console.aws.amazon.com/support "https://console.aws.amazon.com/support").

For example, the following command generates the SHA256 checksum for the Slurm 25.05.3-1
tarball.

```
`$` sha256sum aws-pcs-slurm-25.05-installer-25.05.3-1.tar.gz
```

Example output:

```
851bb5815b6700ceb30cc4a3fda204ca8ce362c14528c339908983255a936cf0 aws-pcs-slurm-25.05-installer-25.05.3-1.tar.gz
```

The following tables list the checksums for recent versions of the installers. Replace
`us-east-1` with the AWS Region where you use AWS PCS.

| AWS PCS agent                 | Installer                                                                                                                       | Download URL                                                       | SHA256 checksum |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------ | --------------- | --------- | ------------ | --------------- |
| AWS PCS agent 1.2.2-1         | ``https://aws-pcs-repo-`us-east-1`.s3.`us-east-1`.amazonaws.com/aws-pcs-agent/aws-pcs-agent-v1.2.2-1.tar.gz``                   | `fd7b6ea5442db75d723fc4971781ce6ae511baa21b87c4286fc1df8127b282b8` |
| AWS PCS agent 1.2.1-1         | ``https://aws-pcs-repo-`us-east-1`.s3.`us-east-1`.amazonaws.com/aws-pcs-agent/aws-pcs-agent-v1.2.1-1.tar.gz``                   | `2b784643ca01ccca1baa64fbfb34bb41efe8bdca69470998b74ce3962bc271d4` |
| AWS PCS agent 1.2.0-1         | ``https://aws-pcs-repo-`us-east-1`.s3.`us-east-1`.amazonaws.com/aws-pcs-agent/aws-pcs-agent-v1.2.0-1.tar.gz``                   | `470db8c4fc9e50277b6317f98584b6b547e73523043e34f018eecae767846805` |
| AWS PCS agent 1.1.1-1         | ``https://aws-pcs-repo-`us-east-1`.s3.`us-east-1`.amazonaws.com/aws-pcs-agent/aws-pcs-agent-v1.1.1-1.tar.gz``                   | `bef078bf60a6d8ecde2e6c49cd34d088703f02550279e3bf483d57a235334dc6` |
| AWS PCS agent 1.1.0-1         | ``https://aws-pcs-repo-`us-east-1`.s3.`us-east-1`.amazonaws.com/aws-pcs-agent/aws-pcs-agent-v1.1.0-1.tar.gz``                   | `594c32194c71bccc5d66e5213213ae38dd2c6d2f9a950bb01accea0bbab0873a` |
| AWS PCS agent 1.0.1-1         | ``https://aws-pcs-repo-`us-east-1`.s3.`us-east-1`.amazonaws.com/aws-pcs-agent/aws-pcs-agent-v1.0.1-1.tar.gz``                   | `04e22264019837e3f42d8346daf5886eaacecd21571742eb505ea8911786bcb2` |
| AWS PCS agent 1.0.0-1         | ``https://aws-pcs-repo-`us-east-1`.s3.`us-east-1`.amazonaws.com/aws-pcs-agent/aws-pcs-agent-v1.0.0-1.tar.gz``                   | `d2d3d68d00c685435c38af471d7e2492dde5ce9eb222d7b6ef0042144b134ce0` | Slurm installer | Installer | Download URL | SHA256 checksum |
| ---                           | ---                                                                                                                             | ---                                                                |
| Slurm 25.05.3-1               | ``https://aws-pcs-repo-`us-east-1`.s3.`us-east-1`.amazonaws.com/aws-pcs-slurm/aws-pcs-slurm-25.05-installer-25.05.3-1.tar.gz``  | `851bb5815b6700ceb30cc4a3fda204ca8ce362c14528c339908983255a936cf0` |
| Slurm 24.11.6-1               | ``https://aws-pcs-repo-`us-east-1`.s3.`us-east-1`.amazonaws.com/aws-pcs-slurm/aws-pcs-slurm-24.11-installer-24.11.6-1.tar.gz``  | `225de9fc18206f5f65f412effe1fd457614ac97ee9822b3ff804a452b0fae522` |
| Slurm 24.11.5-1               | ``https://aws-pcs-repo-`us-east-1`.s3.`us-east-1`.amazonaws.com/aws-pcs-slurm/aws-pcs-slurm-24.11-installer-24.11.5-1.tar.gz``  | `593efe4d66bef2f3e46d5a382fb5a32f7a3ca2510bcf1b3c85739f4f951810d5` |
| Slurm 24.05.8-1               | ``https://aws-pcs-repo-`us-east-1`.s3.`us-east-1`.amazonaws.com/aws-pcs-slurm/aws-pcs-slurm-24.05-installer-24.05.8-1.tar.gz``  | `210a43b376af082bbad640b2032655885790c5dab0e6489cc327c7310a375849` |
| Slurm 24.05.7-1               | ``https://aws-pcs-repo-`us-east-1`.s3.`us-east-1`.amazonaws.com/aws-pcs-slurm/aws-pcs-slurm-24.05-installer-24.05.7-1.tar.gz``  | `0b5ed7c81195de2628c78f37c79e63fc4ae99132ca6b019b53a0d68792ee82c5` |
| Slurm 24.05.5-2               | ``https://aws-pcs-repo-`us-east-1`.s3.`us-east-1`.amazonaws.com/aws-pcs-slurm/aws-pcs-slurm-24.05-installer-24.05.5-2.tar.gz``  | `7cc8d8294f2fbff95fe0602cf9e21e02003b5d96c0730e0a18c6aa04c7a4967b` |
| Slurm 23.11.10-3 (deprecated) | ``https://aws-pcs-repo-`us-east-1`.s3.`us-east-1`.amazonaws.com/aws-pcs-slurm/aws-pcs-slurm-23.11-installer-23.11.10-3.tar.gz`` | `488a10ee0fbd57ec0e0ff7ea708a9e3038fafdc025c6bb391c75c2e2a7852a00` |
| Slurm 23.11.10-2 (deprecated) | ``https://aws-pcs-repo-`us-east-1`.s3.`us-east-1`.amazonaws.com/aws-pcs-slurm/aws-pcs-slurm-23.11-installer-23.11.10-2.tar.gz`` | `0bbe85423305c05987931168caf98da08a34c25f9eec0690e8e74de0b7bc8752` |
| Slurm 23.11.10-1 (deprecated) | ``https://aws-pcs-repo-`us-east-1`.s3.`us-east-1`.amazonaws.com/aws-pcs-slurm/aws-pcs-slurm-23.11-installer-23.11.10-1.tar.gz`` | `27e8faa9980e92cdfd8cfdc71f937777f0934552ce61e33dac4ecf5a20321e44` |
| Slurm 23.11.9-1 (deprecated)  | ``https://aws-pcs-repo-`us-east-1`.s3.`us-east-1`.amazonaws.com/aws-pcs-slurm/aws-pcs-slurm-23.11-installer-23.11.9-1.tar.gz``  | `1de7d919c8632fe8e2806611bed4fde1005a4fadc795412456e935c7bba2a9b8` |
