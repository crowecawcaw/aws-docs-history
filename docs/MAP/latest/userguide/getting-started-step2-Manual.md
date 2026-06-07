# Manual tagging

You can manually tag your migrated resources using the AWS Management Console.

###### To get started

1. Go to your AWS Management Console.
2. Go to the migrated resources. **Example**: Amazon RDS.
3. Choose **Add tags**.
4. Enter `map-migrated` as the Tag key.

###### Note

The Migration Acceleration Program requires that you tag resources with the
`map-migrated` tag. This tag is automatically activated for you as a cost allocation
tag. Tags that are automatically activated don't count towards your cost allocation tag
quota. For more information, see [Quotas and
restrictions](../../../awsaccountbilling/latest/aboutv2/billing-limits.md "../../../awsaccountbilling/latest/aboutv2/billing-limits.md"). 5. Enter and replace your **MPE ID** with the tag value you
want to apply to the migrated workloads.

**Example**:

    * If your MPE ID is `12345`, use the value
     `mig12345`.
    * If your MPE ID is `ABCDE12345`, use the value
     `migABCDE12345`.

6. Choose **Save**.
   Depending on your migrated resource and MPE ID, the tag value can be any of the
   following:

- `mig`5-digit MPE ID``
- `sap`5-digit MPE ID``
- `oracle`5-digit MPE ID``

- `mig`10 alphanumeric characters MPE ID``
- `sap`10 alphanumeric characters MPE ID``
- `oracle`10 alphanumeric characters MPE
  ID``

###### Note

Use lowercase letters for the `mig`, `sap`, and
`oracle` prefixes and uppercase letters for the alphanumeric MPE IDs (long MPE
IDs). For more information about what tag values you should use, see [Tagging key combinations](setting-up.md "setting-up.md"). For more information about your MPE ID, see [MPE ID length](mpe-length.md "mpe-length.md").

Repeat the steps above for all associated resources such as Snapshots. For more information
about tagging resources, see the [Tag your Amazon EC2
resources](../../../AWSEC2/latest/UserGuide/Using_Tags.md "../../../AWSEC2/latest/UserGuide/Using_Tags.md") in the _Amazon Elastic Compute Cloud user guide for Linux
instances_.
