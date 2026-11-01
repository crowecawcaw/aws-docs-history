

# Essential notes for version 2.26 and 3.26
<a name="rn-2-26-essential"></a>

## New operating system
<a name="rn-2-26-essential-os"></a>

Read this information if you are upgrading from an earlier version of AWS Elemental software. This note applies to both Elemental Live 2.26 and Conductor Live 3.26.

Version 2.26.0 (3.26.0 for Conductor Live) runs on RHEL 9 and won't run on RHEL 7 or CentOS 7. Therefore, to use the new versions of the AWS Elemental software, you must install the new operating system as well as upgrade the software.

## Migration guides for version 3.26 and 2.26
<a name="rn-2-26-essential-migration"></a>

There are special migration guides to perform this upgrade:
+ To upgrade to AWS Elemental Live 2.26 (or later), follow the instructions in the [AWS Elemental Live Migration Guide](https://docs.aws.amazon.com/elemental-live/latest/migrationguide/).
+ To upgrade a Conductor cluster to AWS Elemental Conductor Live 3.26 (or later) and AWS Elemental Live 2.26 (or later), follow the instructions in the [AWS Elemental Conductor Live Migration Guide](https://docs.aws.amazon.com/elemental-cl3/latest/migrationguide/). This migration guide doesn't apply to clusters that include AWS Elemental Statmux. For guidance in migrating these clusters, contact AWS Elemental Customer Support.

**Important**  
Don't follow the instructions in one of the upgrade guides. Those procedures won't work.

## Required reading
<a name="rn-2-26-essential-required-reading"></a>

If you have not upgraded your AWS Elemental Live software in several versions, you must read the release notes for the versions that you missed.

Specifically, read the essential notes for each major version that you skipped. Each major version in these release notes has its own essential notes.

## Recommendation for converting from software RAID to hardware RAID
<a name="rn-2-26-essential-raid"></a>

When you migrate to RHEL 9, note that conversion from software RAID to hardware RAID is optional.

If you do want to convert to hardware RAID, we recommend that you perform the conversion before you've migrated your system to version 2.26.x of the AWS Elemental Live software. For information about the migration guides for version 3.26 and 2.26, see [Migration guides for version 3.26 and 2.26](#rn-2-26-essential-migration).

For detailed instructions about converting to hardware RAID, see the knowledge article with the title *How to reconfigure an appliance from software RAID to hardware RAID* in the [AWS Elemental Support Center](https://console.aws.amazon.com/elemental-appliances-software/home?region=us-east-1#/supportcenter).

## Changes to features in version 2.26.0
<a name="rn-2-26-essential-changes"></a>

This version includes the following changes to existing features.

### Changes to support for Python, Ruby, and scripts
<a name="rn-2-26-essential-python-ruby"></a>

Starting with AWS Elemental Live version 2.26.0, there are new versions for some libraries. The supported versions are installed with AWS Elemental Live 2.26.0. Make sure that you update scripts (including preprocessing and post-processing scripts) that you have created so that they are compliant with the new versions.
+ Python version 3
+ Ruby version 2.6.10

### Change to support for HTTPS
<a name="rn-2-26-essential-https"></a>

Starting with version 2.26.0, HTTPS is enabled by default. (Previously, HTTP was enabled by default. You could enable HTTPS using the install script or configuration script.)

You can't disable HTTPS. But you can set up with both HTTP and HTTPS enabled:
+ To enable HTTP when it is currently disabled, run the script with `--http`.
+ To disable HTTP when it is currently enabled, run the script with `--https`.
+ To retain the current protocol configuration (whatever that is), run the script without the option. (Note that this is a change in behavior. Previously, if you ran the script with no option, you disabled HTTPS.)

Take these steps:
+ Review any scripts that you have created to make sure that you are happy with the new behavior, especially with the fact that `--https` disables HTTP.
+ Make sure that users or applications use a secure connection and trusted certificates to communicate with AWS Elemental Live. You must provide the trusted certificates. If you don't provide your own trusted certificates, you will see an error in your browser when you access the web interface. The error will indicate that the site certificate is not valid.

### Changes to AWS Elemental licenses
<a name="rn-2-26-essential-licenses"></a>

Starting with AWS Elemental Live version 2.26.0, SMPTE 2110 outputs require an Elemental license. The add-on package is free of charge, but it must be installed on appliances where you want to run events that create SMPTE 2110 outputs.

To obtain the license, contact your AWS Elemental sales person. To deploy the license, see the section about [configuring licenses](https://docs.aws.amazon.com/elemental-live/latest/configguide/config-live-licenses.html) in the AWS Elemental Live Configuration Guide.

### Removed features
<a name="rn-2-26-essential-removed-features"></a>

Starting with the AWS Elemental Live 2.26.0 GA software release, the following features are no longer part of the software:
+ Civolution watermarking
+ DTS Express encoding, which means that you can no longer choose DTS as the codec for video outputs.
+ Flash motion graphics

If you obtain an appliance that already has version 2.26.0 or later installed, or if you install version 2.26.0 or later on qualified hardware (as a fresh install), these features are not part of the software.

If you migrate a node to version 2.26.0 or later, the migration procedure includes a step to remove fields related to removed features from the event XML. You don't have to manually remove these fields.

### Impact of Mellanox driver changes
<a name="rn-2-26-essential-mellanox"></a>

The following information applies if you implement SMPTE 2110 inputs or outputs.

RHEL 9 works only with versions 5.8 and higher of the Mellanox driver. As a result, the AWS Elemental Live installer for versions 2.26.0 and higher installs this new version of the Mellanox driver. This version of the Mellanox driver isn't compatible with CIFS.

If you have an appliance that includes a Mellanox NIC, and you have been using CIFS to mount remote file shares, you must decide which feature you want to use:
+ You can continue to use Mellanox. When you install, the install script detects the Mellanox NIC and automatically installs the driver. In this case, you will no longer be able to use CIFS.
+ You can postpone installation of the new Mellanox driver. This option is useful, for example, if you have an appliance with a Mellanox NIC that you aren't yet ready to use in your workflows. You can continue to use CIFS until you need to use the Mellanox NIC. When you install, include the `--skip-mellanox` option in order to skip driver detection. The installer won't install the new Mellanox driver.