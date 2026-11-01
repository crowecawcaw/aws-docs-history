

# Essential notes for version 2.23 and 3.23
<a name="rn-2-23-essential"></a>

Read these essential notes before you upgrade to version 2.23 (3.23 for Conductor Live).

## Conductor Live user guide revision
<a name="rn-2-23-essential-cl3-ug-revision"></a>

The Conductor Live user guide has been revised and brought more up to date. More improvements will be published in the upcoming months.

Find the guide on the landing page for the AWS Elemental Live suite of products.

The user guide includes information about three recent new features in Statmux that enhance the capabilities of an MPTS:
+ Program passthrough
+ Passthrough of a custom stream
+ Passthrough of a custom stream that is an SI/PSI table

## Changes to usage of the Mellanox card
<a name="rn-2-23-essential-mellanox"></a>

Read this information if, before upgrading to version 2.23.3, you were already running events with SMPTE 2110 inputs or outputs, or with SMPTE 2022-6 inputs.

For these workflows, you must use an Elemental Live node or VM or qualified hardware unit that includes a Mellanox card. Version 2.23.3 of Elemental Live includes changes to the way that Elemental Live works with the card. The changes are as follows:
+ Version 2.23.3 introduces performance optimizations for SMPTE 2110 inputs and SMPTE 2022-6 inputs. These optimizations don't apply to SMPTE 2110 outputs. For more information about these optimizations, see [Performance optimizations for SMPTE 2110 inputs](rn-2-23-features.md#rn-2-23-perf-2110).
+ In earlier versions, you needed to reserve cores for SMPTE 2110 inputs and outputs, and for SMPTE 2022-6 inputs. Starting with version 2.23.3, you no longer reserve cores for SMPTE 2110 outputs.

You might need to make changes to the Elemental Live configuration.

**Scenario 1**

You might previously have been running events with SMPTE 2110 inputs or SMPTE 2022-6 inputs, and possibly SMPTE 2110 outputs. If so, you must reboot the Elemental Live hardware unit to apply the performance optimizations. Follow these steps:

1. Upgrade to version 2.23.3, as described in the [AWS Elemental Live Upgrade Guide](https://docs.aws.amazon.com/elemental-live/latest/upgradeguide/).

1. On the node, run the following command:

   **sudo shutdown -r now**

**Scenario 2**

You might previously have been running events with SMPTE 2110 outputs, but not with SMPTE 2110 inputs or SMPTE 2022-6 inputs. If so, you followed instructions to reserve cores for these outputs. Starting with version 2.23.3, you don't need to reserve cores. Therefore, you should release the cores, so that all processes can access them. Follow these steps:

1. Upgrade to version 2.23.3, as described in the [AWS Elemental Live Upgrade Guide](https://docs.aws.amazon.com/elemental-live/latest/upgradeguide/).

1. Release the reserved cores. For information, in the [AWS Elemental Live User Guide](https://docs.aws.amazon.com/elemental-live/latest/ug/), in the navigation bar, choose **Features**, then **SMPTE 2110 inputs and outputs**, then **Setup: Reserving processing cores**. Follow the procedure to release cores. Remember to reboot.

## Log4j has no impact on the Live suite
<a name="rn-2-23-essential-log4js"></a>

AWS Elemental Conductor Live 3 uses logstash, but not in a configuration that was susceptible to the widely reported Log4j issue. Out of an abundance of caution, and to allay any concerns from customers, we are upgrading logstash in Conductor Live to the latest patched version.

**Note**  
Neither AWS Elemental Live nor AWS Elemental Statmux use logstash.

## Release types
<a name="rn-2-23-essential-release-types"></a>

Starting with the 2.22.x series, all Elemental Live General Availability (GA) releases include both features and fixes. Releases within a major version are numbered starting with 0. For example, a major series might have versions from 2.22.0 to 2.22.5. Each release in the series always includes fixes and usually includes features.

## Required reading
<a name="rn-2-23-essential-required-reading"></a>

If you have not upgraded your Elemental Live software for several versions, you must read the release notes for the versions you missed.

Specifically, read the essential notes for each major version that you skipped. Each major version in these release notes has its own essential notes.