

# Using OCI MySQL Heatwave as a source for AWS DMS
<a name="CHAP_Source.heatwave"></a>

With AWS DMS, you can use OCI MySQL Heatwave as a source in much the same way as you do MySQL. Using OCI MySQL Heatwave as a source requires a few additional configuration changes.

For information about versions of OCI MySQL Heatwave that AWS DMS supports as a source, see [Sources for AWS DMS](CHAP_Introduction.Sources.md).

## Setting up OCI MySQL Heatwave for logical replication
<a name="CHAP_Source.heatwave.setup"></a>

To configure your OCI MySQL Heatwave instance as a source endpoint for DMS, do the following:

1. Sign in to OCI Console, and open the main hamburger menu (≡) in the top left corner.

1. Choose **Databases**, **DB Systems**.

1. Open the **Configurations** menu.

1. Choose **Create configuration**.

1. Enter a configuration name, such as **dms\_configuration**.

1. Choose the shape of your current OCI MySQL Heatwave instance. You can find the shape on the instance's **DB system configuration** properties tab under the **DB system configuration:Shape** section.

1. In the **User variables** section, choose the `binlog_row_value_options` system variable. Its default value is `PARTIAL_JSON`. Clear the value.

1. Choose the **Create** button.

1. Open your OCI MySQLHeatwave instance, and choose the **Edit** button.

1. In the **Configuration** section, choose the **Change configuration** button, and choose the shape configuration that you created in step 4.

1. Once the changes take effect, your instance is ready for logical replication.