# Custom patch baselines

Unlike predefined patch baselines, custom patch baselines do not have default patch approvals and compliance levels. This gives you greater control over which patches are approved or rejected for your environment and allows you to define your custom repositories. For example, you can assign specific approval rules and compliance values. It is also possible to create a custom patch baseline by copying a predefined patch baseline and specifying the compliance values that you want to assign to patches.

You can use Patch Manager to create a custom patch baseline for Linux-based managed nodes, such as Red Hat Enterprise Linux (RHEL), SUSE Linux Enterprise Server (SLES), Oracle Linux. You can also specify patch source repositories for each of these operating systems. See the sections below for additional information about patch sources for each.

For instructions on how to create a custom patch baseline for Linux and Windows, see the following documentation:

- [Creating a custom patch baseline (Linux)](../../../systems-manager/latest/userguide/create-baseline-console-linux.md "../../../systems-manager/latest/userguide/create-baseline-console-linux.md") in the _AWS Systems Manager User Guide_
- [Creating a custom patch baseline (Windows)](../../../systems-manager/latest/userguide/create-baseline-console-windows.md "../../../systems-manager/latest/userguide/create-baseline-console-windows.md") in the _AWS Systems Manager User Guide_

## Patch sources

When you use the default repositories that are configured on a managed node for patching operations, Patch Manager scans for security-related patches or installs them. This is the default behavior for Patch Manager. On Linux systems, you can also use Patch Manager to install patches that aren’t related to security or that are in a different source repository than the default repository that is configured on the managed node.

In the procedure to create a custom patch baseline, there is an option to specify alternative patch source repositories if you are not using the default repository configuration. In each custom patch baseline, you can specify patch source configurations for up to 20 versions of a supported Linux operating system. For more information about alternative patch sources, see [How to specify an alternative patch source repository (Linux)](../../../systems-manager/latest/userguide/patch-manager-how-it-works-alt-source-repository.md "../../../systems-manager/latest/userguide/patch-manager-how-it-works-alt-source-repository.md") in the _AWS Systems Manager User Guide_.

###### Note

If you specify alternative repositories, you must also specify the default repositories as part of the alternative patch source configuration if you want those updates to be applied.

The sections below contain information about how to obtain patch source details for SLES for SAP Applications, RHEL for SAP Applications, and Oracle Linux. You can use this information to specify a patch source when you create a custom patch baseline.

## Patch sources for SLES for SAP Applications

You can use one of the following patch repositories for SUSE Linux Enterprise Server (SLES) for SAP Applications:

- SUSE public cloud update infrastructure
- Private repository

For information about how to use a private patch repository, see [Private and local repositories](auto-os-patch-private-repo.md "auto-os-patch-private-repo.md") in this guide.

The public cloud update infrastructure is a global network of update servers maintained by SUSE on AWS Cloud that provides low-latency access to patches from on-demand instances. Customers that use SUSE on-demand instances in AWS automatically connect to the public cloud update infrastructure on boot. You can view the SUSE patch source server details in the `/etc/hosts` directory.

You can connect to the public cloud update infrastructure through an internet gateway in a public subnet, NAT gateway in a private subnet, or through a local data center. To see the repository list, run the command `zypper ls`.

By default, all repositories are considered for patching. If you want to only patch certain repositories or if you are using multiple patch sources for repositories, you must explicitly add patch sources based on repository configuration.

Complete the following steps to identify the patch source for the repository that you would like to use for patching:

1. Navigate to the following directory to view the repository files:

```
/etc/zypp/repos.d
```

2. Save the name and configuration for each repository file. For example, you might save the following:
   - Name – `SUSE_Linux_Enterprise_Server_for_SAP_Applications_x86_64:SLE-Product-SLES_SAPXX-SPX-Updates`
   - Configuration –

   ```
   name=SLE-Product-SLES_SAPXX-SPX-Updates
   enabled=1
   autorefresh=1
   baseurl=plugin:/susecloud?credentials=SUSE_Linux_Enterprise_Server_for_SAP_Applications_x86_64&path=/repo/SUSE/Updates/SLE-Product-SLES_SAP/XX-SPX/x86_64/update/
   service=SUSE_Linux_Enterprise_Server_for_SAP_Applications_x86_64
   ```

3. Enter this information when you create the custom patch baseline in the **Patch sources** section of **Patch Manager**. For the full list of steps, see [Creating a custom patch baseline (Linux)](../../../systems-manager/latest/userguide/create-baseline-console-linux.md "../../../systems-manager/latest/userguide/create-baseline-console-linux.md") in the _AWS Systems Manager User Guide_.
4. If you add a patch source for any repository, you must add patch sources for all the repositories that you would like to patch, including the default repositories.

###### Important

Before you deploy the patch, you must accept the license agreement in the `zypper.conf` configuration file. You can find the file in the following directory:

```
/etc/zypp/zypper.conf
```

To accept the license agreement, uncomment the license agreement property and save it as:

```
autoAgreeWithLicenses = yes
```

## Patch sources for RHEL for SAP Applications

You can use one of the following patch repositories for Red Hat Enterprise Linux (RHEL) for SAP Applications:

- Red Hat update infrastructure
- Local repository

For information about how to use a private patch repository, see [Private and local repositories](auto-os-patch-private-repo.md "auto-os-patch-private-repo.md") in this guide.

Red Hat update infrastructure is a global network of update servers maintained by Red Hat on AWS Cloud that provides low-latency access to patches from on-demand instances. Customers that use Red Hat on-demand instances in AWS automatically connect to the Red Hat update infrastructure on boot.

The RHEL repositories are stored in the following location:

```
/etc/yum.repos.d/
```

Complete the following steps to identify the patch source for the repository that you would like to use for patching:

1. Run the following command to view the default, enabled repositories:

```
cat /etc/yum.repos.d/* | grep -B 4 -A 6 "enabled=1"
```

This command returns four lines before and six lines after each repository that is enabled. For example, the command might return something like this:

```
[rhui-client-config-server-8-sap-bundle]
name=Red Hat Update Infrastructure 3 Client Configuration for SAP Bundle
mirrorlist=https://rhui3.REGION.ce.redhat.com/pulp/mirror/protected/rhui-client-
config/rhel/server/8/$basearch/sap-bundle
enabled=1
gpgcheck=1
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-redhat-release
sslverify=1
sslcacert=/etc/pki/rhui/cdn.redhat.com-chain.crt
sslclientcertexample=/etc/pki/rhui/product/rhui-client-config-server-8-sap-bundle.crt
sslclientkeyexample=/etc/pki/rhui/rhui-client-config-server-8-sap-bundle.key
```

2. Save the name and configuration for each repository file. In this example, you would save the following:
   - Name – `rhui-client-config-server-8-sap-bundle`
   - Configuration

   ```
   name=Red Hat Update Infrastructure 3 Client Configuration for SAP Bundle
   mirrorlist=https://rhui3.REGION.ce.redhat.com/pulp/mirror/protected/rhui-client-
   config/rhel/server/8/$basearch/sap-bundle
   enabled=1
   gpgcheck=1
   gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-redhat-release
   sslverify=1
   sslcacertexample=/etc/pki/rhui/cdn.redhat.com-chain.crt
   sslclientcertexample=/etc/pki/rhui/product/rhui-client-config-server-8-sap-bundle.crt
   ```

3. For each entry that was returned by the command in the previous step, create a new patch source when you create a custom patch baseline in the **Patch sources** section of **Patch Manager**. For the full list of steps, see [Creating a custom patch baseline (Linux)](../../../systems-manager/latest/userguide/create-baseline-console-linux.md "../../../systems-manager/latest/userguide/create-baseline-console-linux.md") in the _AWS Systems Manager User Guide_.
4. If you add a patch source for any repository, you must add patch sources for all the repositories that you would like to patch, including the default repositories.

## Patch sources for Oracle Linux

On Oracle Linux, the patch baseline uses preconfigured repositories on the managed node. All Oracle Linux Amazon Machine Images (AMIs) can access the public YUM repository. Only licensed Oracle Linux systems can access the Oracle ULN repository.

The Oracle Linux repositories are stored in the following location:

```
/etc/yum.repos.d/
```

Complete the following steps to identify the patch source for the repository that you would like to use for patching:

1. Run the following command to view the default, enabled repositories:

```
cat /etc/yum.repos.d/* | grep -B 4 -A 6 "enabled=1"
```

This command returns four lines before and six lines after each repository that is enabled. For example, the command might return something like this:

```
[o18-appsteream]
name=Oracle Linux 8 Application Stream ($basearch)
baseurl=https://yum$ociregion.$ocidomain/repo/OracleLinux/OL8/appstream/$basearch/
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-oracle
gpgcheck=1
```

2. Save the name and configuration for each repository file. In this example, you would save the following:
   - Name – `o18-appsteream`
   - Configuration

   ```
   name=Oracle Linux 8 Application Stream ($basearch)
   baseurl=https://yum$ociregion.$ocidomain/repo/OracleLinux/OL8/appstream/$basearch/
   gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-oracle
   gpgcheck=1
   ```

3. For each entry that was returned by the command in the previous step, create a new patch source when you create a custom patch baseline in the **Patch sources** section of **Patch Manager**. For the full list of steps, see [Creating a custom patch baseline (Linux)](../../../systems-manager/latest/userguide/create-baseline-console-linux.md "../../../systems-manager/latest/userguide/create-baseline-console-linux.md") in the _AWS Systems Manager User Guide_.
4. If you add a patch source for any repository, you must add patch sources for all the repositories that you would like to patch, including the default repositories.

Oracle Linux 7 managed nodes use YUM as the package manager, while Oracle Linux 8 managed nodes use DNF as the package manager. Both package managers have an update notice, which is a file named `updateinfo.xml`. The update notice is a collection of packages that fix specific issues. Individual packages aren’t assigned classifications or severity levels, so Patch Manager assigns the attributes of an update notice to the related packages and installs the packages based on the classification filters specified in the patch baseline.

Only patches specified in `updateinfo.xml` are applied if you are using the default patch baseline provided by AWS or if you do not select the option to include non-security update patches when you create a custom baseline. If you create a custom baseline and you do select the option to include non-security update patches, the patches in `updateinfo.xml` and the patches that are not in `updateinfo.xml` are applied. For more information, see [How patch baseline rules work on Oracle Linux](../../../systems-manager/latest/userguide/patch-manager-how-it-works-linux-rules.md#patch-manager-how-it-works-linux-rules-oracle "../../../systems-manager/latest/userguide/patch-manager-how-it-works-linux-rules.md#patch-manager-how-it-works-linux-rules-oracle") in the _AWS Systems Manager User Guide_.

Oracle Linux instances require internet access to the public YUM repository or Oracle ULN in order to download packages. If the Amazon EC2 instance is on a private subnet of an Amazon VPC, you can use a proxy server or a local YUM repository to download packages. For more information, see [Configuring a System to Use a Proxy With a Yum Server](https://docs.oracle.com/en/operating-systems/oracle-linux/software-management/sfw-mgmt-ConfigureaSystemtoUseOracleLinuxYumServer.html#config-proxy-with-yum "https://docs.oracle.com/en/operating-systems/oracle-linux/software-management/sfw-mgmt-ConfigureaSystemtoUseOracleLinuxYumServer.html#config-proxy-with-yum") in the Oracle documentation. Alternatively, Oracle Linux systems can work with Oracle Linux Manager for YUM package management. An Oracle Linux Manager system can be in a public subnet while Oracle Linux systems can be in a private subnet. For more information, see [Oracle Linux Manager](https://docs.oracle.com/en/operating-systems/oracle-linux-manager/ "https://docs.oracle.com/en/operating-systems/oracle-linux-manager/") in the Oracle documentation.

## Windows Server considerations

For additional information about security patches for Windows, see [How security patches are selected](../../../systems-manager/latest/userguide/patch-manager-how-it-works-selection.md "../../../systems-manager/latest/userguide/patch-manager-how-it-works-selection.md") and [How patches are installed](../../../systems-manager/latest/userguide/patch-manager-how-it-works-installation.md "../../../systems-manager/latest/userguide/patch-manager-how-it-works-installation.md") in the _AWS Systems Manager User Guide_.
