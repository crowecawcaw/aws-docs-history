

# Essential notes for version 2.27 and 3.27
<a name="rn-2-27-essential"></a>

## Support for the migration lifeboat script
<a name="rn-2-27-essential-lifeboat"></a>

If you haven't yet migrated to RHEL 9, note the following. When you migrate your AWS Elemental software to a version that runs on RHEL 9, you must use the AWS Elemental lifeboat script to create a backup of the data on the node. For information about the script, see the [AWS Elemental Live Migration Guide](https://docs.aws.amazon.com/elemental-live/latest/migrationguide/) and the [AWS Elemental Conductor Live Migration Guide](https://docs.aws.amazon.com/elemental-cl3/latest/migrationguide/).

**Important**  
Version 2.27.0 (3.27.0) and later don't support the lifeboat script. If you use them to migrate, you can't keep your existing data. To use the lifeboat script and keep your existing data, first migrate to a 2.26 (3.26) version. You can then upgrade to a 2.27 (3.27) version.

## Changes to 2110 receiver group inputs
<a name="rn-2-27-essential-2110-inputs"></a>
+ Stream patching – Starting with Elemental Live 2.27.0, the default mode for stream patching is make-before-break. Previously, the only supported mode was break-before-make. If you have events that use 2110 receiver group inputs that you created before version 2.27.0, you must configure each event for the mode that you want. For more information, see [NMOS next generation – receiver patching with two modes (GLV-4965)](rn-2-27-features.md#rn-2-27-0-patching-modes).
+ Shadow inputs – Starting with Elemental Live 2.27.0, shadow inputs are required with 2110 receiver group inputs. If you have events that use 2110 receiver group inputs that you created before version 2.27.0, you must modify those inputs to enable shadow inputs. For more information, see [Shadow inputs are required for 2110 receiver group inputs (GLV-4730)](rn-2-27-features.md#rn-2-27-0-shadow-inputs).