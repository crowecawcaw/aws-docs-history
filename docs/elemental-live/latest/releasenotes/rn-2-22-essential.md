

# Essential notes for version 2.22 and 3.22
<a name="rn-2-22-essential"></a>

Read the following essential notes before you upgrade to version 2.22 (3.22 for Conductor Live).

## Firmware upgrade
<a name="rn-2-22-essential-firmware"></a>

In Elemental Live 2.21.4, the NIC driver firmware has been upgraded to resolve issues on appliances that include the 1G Cu SFP link speed interface. These issues occur on specific appliances in the L800 series. The issues include the following:
+ After the interface disconnects, the link status of the interface doesn't update to show the new state. (SOCK-36051)
+ The link status of the interface doesn't correctly identify that it is in a bond. (SOCK-36779)
+ The interface can unexpectedly perform a link renegotiation, resulting in a link speed dropping from 1000 Mbps to 100 Mbps.

All these problems are resolved by the firmware upgrade. The firmware upgrade is automatically performed when you install Elemental Live version 2.20.0 or later.

## Change to release lines
<a name="rn-2-22-essential-release-lines"></a>

All AWS Elemental Live, Statmux, and Conductor Live releases are now General Availability (GA). Historical Limited Availability (LA) releases are now available on the AWS Appliances & Console service.

## Change to support for Statmux
<a name="rn-2-22-essential-statmux-support"></a>

AWS Elemental Live version 2.20.2 reintroduced support for MPTS and Statmux features.

For information about how to upgrade from Statmux 2.17, search the knowledge articles in the [AWS Elemental Support Center](https://console.aws.amazon.com/elemental-appliances-software/home?region=us-east-1#/supportcenter) for *Statmux 2.17 to 2.20 Cluster Upgrade Procedure*. Contact AWS Elemental Support if you have additional questions.

## Mandatory password reset
<a name="rn-2-22-essential-password-reset"></a>

There is a mandatory one-time password reset required for AWS Elemental Live and AWS Elemental Conductor Live, if your appliances have been configured with user authentication enabled. This change is to ensure that all users of the web interface and API have set strong passwords. The new password requirements are the following:
+ Minimum 8 characters.
+ At least one uppercase letter, at least one lowercase letter, at least one number, and at least one symbol.

This password change is a one-time action. Therefore, for example, if you change the password when you install version 2.20, you won't be forced to change it again when you install 2.21.

For more details, and for important information about an issue with this procedure, see the 3.20.2 LA section of the release notes for version 2.20 and 3.20, in [Release notes for earlier versions](rn-earlier.md).

## Reminder to cycle the power when upgrading or downgrading
<a name="rn-2-22-essential-power-cycle"></a>

When you upgrade or downgrade any version of AWS Elemental Live, we strongly recommend that you turn off the appliance and turn it back on. Doing so ensures that any installer and firmware updates (or downgrades) are correctly set up.

## Video quality and density
<a name="rn-2-22-essential-vq-density"></a>

AWS Elemental invests in continuous improvement of video quality (VQ) for the AWS Elemental Live appliance. In some cases, VQ improvements are achieved by trading off stream density. By upgrading to this new software version, you might experience moderate loss of density on some workflows. If density is more important than VQ, you might be able to recover lost density by adjusting VQ parameters. For example, for an H.264 or HEVC stream, you can change SvQ from 0 to 1.

## Deprecation information
<a name="rn-2-22-essential-deprecation"></a>

Civolution watermarking will be deprecated in a later version.

When you start an event with the DTS Express audio encoder feature, you will see a notice that indicates future deprecation in a later version. Disregard this notice. DTS Express is supported for all 2.20 versions.