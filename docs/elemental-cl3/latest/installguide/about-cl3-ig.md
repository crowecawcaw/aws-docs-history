# About this guide

This guide describes how to install AWS Elemental Conductor Live software for the first time. (To perform a
kickstart and fresh install on a node that you have already deployed, see the [AWS Elemental Conductor Live Upgrade
Guide](../upgradeguide.md "../upgradeguide.md").)

**Supported versions**

This guide applies to all versions of the software that are currently available for
download from AWS Elemental.

**Phase 1 of installation**

The following table lists the reference documents for the different types of
installation.

| Type of hardware        | Description                                                                                                                                                                                                                                                                                                                                                                                   | Section in this<br>guide                                                                                            |
| ----------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| AWS Elemental appliance | You obtained<br>an<br>AWS Elemental<br>appliance.<br>This<br>hardware<br>comes with<br>the<br>software and the appropriate licenses already installed.<br>You<br>don't need to perform any installation. Instead, you need to complete<br>setup of the appliance. See [AWS Elemental Conductor Live Configuration<br>Guide](../configguide/about-cl3-cg.md "../configguide/about-cl3-cg.md"). | None                                                                                                                |
| Qualified<br>hardware   | You're installing<br>software<br>and<br>licenses<br>for each<br>qualified<br>hardware that's running AWS Elemental software.                                                                                                                                                                                                                                                                  | [Installing Conductor Live on qualified hardware](install-cl3-ig.md "install-cl3-ig.md") in this guide              |
| Virtual<br>machine (VM) | You're installing<br>software<br>and licenses for each VM guest that's running AWS Elemental<br>software.                                                                                                                                                                                                                                                                                     | [Installing Conductor Live on a virtual machine<br>(VM)](install-vm-cl3-ig.md "install-vm-cl3-ig.md") in this guide |

The procedures in this guide get you through phase 1 of the software installation process:

- The preconfigured operating system is
  installed.
- The software is installed, eth0 is configured, and licenses are installed.
  Phase 2 covers configuration of the software. See [AWS Elemental Conductor Live Configuration Guide](../configguide.md "../configguide.md").

###### Note

For
assistance with your AWS Elemental appliances and software products, see the
[AWS Elemental Support Center](https://console.aws.amazon.com/elemental-appliances-software/home?region=us-east-1#/supportcenter "https://console.aws.amazon.com/elemental-appliances-software/home?region=us-east-1#/supportcenter").
