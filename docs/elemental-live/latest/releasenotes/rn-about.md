

# About these release notes
<a name="rn-about"></a>

These release notes describe the new features, resolved issues, and newly identified issues in each release of the following AWS Elemental products:
+ AWS Elemental Live version 2.{{x}}
+ AWS Elemental Statmux version 2.{{x}}
+ AWS Elemental Conductor Live version 3.{{x}}

The three products are released together. Each Elemental Live and Statmux version 2.{{x}} release has a matching Conductor Live version 3.{{x}} release. For example, Elemental Live 2.28.0 and Conductor Live 3.28.0 are part of the same release.

The release notes are organized by major version, with the newest version first. Starting with version 2.27, each major version has one page for each point release. For versions 2.21 to 2.26, each major version has pages for essential notes, new features, resolved issues, and newly identified issues, where the release has them, and each table of issues has a column that shows the point release. Each table of issues includes a key that identifies the issue.

Some versions in these release notes are no longer supported. We provide the installers for some older versions only so that you can upgrade to a supported version. We recommend that you upgrade to the newest version of the AWS Elemental software.

## About the suite of Live products
<a name="rn-about-products"></a>

The suite of Live products includes AWS Elemental Live, AWS Elemental Statmux, and AWS Elemental Conductor Live.

### AWS Elemental Live
<a name="rn-about-products-live"></a>

AWS Elemental Live is a massively parallel video processing system that provides content distributors with video and audio encoding for live streaming to new media platforms. With high density and support for adaptive bitrate protocols, HTML5, and multiple HD streams, Elemental Live delivers the high-quality, high-efficiency performance that current and future live streaming applications need for any device. A web-based interface simplifies your workflow and provides real-time controls.

You can deploy Elemental Live in standalone mode or as part of a cluster that Conductor Live controls.

### AWS Elemental Statmux
<a name="rn-about-products-statmux"></a>

AWS Elemental Statmux is an extension of the Elemental Live product line that lets you produce MPTS outputs. Statmux functionality works only in a Conductor Live cluster. The Elemental Live nodes create the programs for the MPTS, and Conductor Live manages the MPTS itself.

Statmux requires that each Elemental Live node has a license for the Statmux rate control add-on.

### AWS Elemental Conductor Live
<a name="rn-about-products-cl3"></a>

AWS Elemental Conductor Live is a management system for controlling Elemental Live and Statmux nodes.

#### Node-based redundancy
<a name="rn-about-cl3-redundancy"></a>
+ Conductor Live provides redundancy for Elemental Live and Statmux nodes (worker nodes). You can set up the worker nodes that Conductor Live controls so that if one node fails, a backup node takes over the activity of the failed node. A backup node is a passive, licensed worker node that is held in reserve.
+ Conductor Live provides Conductor node redundancy. You can set up the cluster with one primary and one backup Conductor node. If the primary node fails, the backup node takes over management of the worker nodes. Conductor node failure and failover have no impact on work that is in progress on the worker nodes.

#### Profiles and parameters
<a name="rn-about-cl3-profiles"></a>
+ Conductor Live requires profiles to create channels.
+ Conductor Live profiles support variables, which are called *channel parameters*. This feature makes profiles flexible. Where appropriate, you can set the value of a field to a channel parameter instead of a fixed value. When an operator uses the profile to create a channel, the operator specifies the values for the channel parameters. This feature is commonly used for input source and destination values.
+ Profile fields that are highlighted in blue on the web interface support channel parameters. To save a profile, the operator must enter validation values for the channel parameters in the profile. Conductor Live doesn't use the validation values when you create a channel from the profile. Instead, the operator must specify values for the channel parameters.
+ For a complete list of profile fields that support channel parameters, see the [AWS Elemental Conductor Live User Guide](https://docs.aws.amazon.com/elemental-cl3/latest/ug/).
+ After you create a profile, you can't modify it. Instead, you can duplicate the profile, modify the duplicate, and save it with a new name.

#### Channel tasks – Bulk actions
<a name="rn-about-cl3-bulk-actions"></a>
+ Conductor Live lets you start, stop, or delete several channels at the same time, and change the profile of several channels at the same time.

#### MPTS management
<a name="rn-about-cl3-mpts"></a>
+ You can create MPTS outputs and manage channel participation on the Conductor Live web interface.
+ The MPTS that Conductor Live creates can reside on an Elemental Live node or a Statmux node.

#### Status management
<a name="rn-about-cl3-status"></a>
+ Alerts and messages that occur on worker nodes are sent to Conductor Live and appear on the web interface.
+ You can configure Conductor Live to send a notification to an email address or a web callback URL when an alert occurs.
+ Operators can add operational notes on the **Status notifications** page.

## Types of releases
<a name="rn-about-release-types"></a>

Releases within a major version are numbered starting with 0. For example, the 2.27 major version has releases from 2.27.0 to 2.27.5. Each release in a major version includes fixes, and usually includes new features.

## Downloading the software
<a name="rn-about-download"></a>

If you have an active AWS Elemental agreement, you can download releases from the [AWS Elemental Appliances and Software console](https://console.aws.amazon.com/elemental-appliances-software/home?region=us-east-1).

## Finding the installed version
<a name="rn-about-installed-version"></a>

To find the version of the software that is installed on a node, look at the bottom of the web interface, or enter the following command:

```
cat /opt/elemental_se/versions.txt
```

Some features are available only on certain models of Elemental Live. For example, HEVC encoding is available only on licensed encoders.