# AWS Tag Editor

You can use the AWS Resource Groups and Tag Editor to tag your migrated resources.

###### Note

The AWS Tag Editor only works for resources running in the account.

###### To get started

1. Open the AWS Management Console.
2. Go to the **Resource Groups & Tag Editor, Tagging, Tag Editor**
   page.
3. Specify the Region(s) your resources are located. **Example**: us-east-1.
4. Choose the type of resources you want to bulk tag. **Example**: EC2, Lambda, and S3.
5. Choose **Search resources** to view the resources that meet the
   conditions you have selected.
6. Select all or a few of the listed resources you want to tag.
7. Choose **Manage tags** of selected resources.
8. Enter `map-migrated` in the Tag Key field.

###### Note

The Migration Acceleration Program requires that you tag resources with the
`map-migrated` tag. This tag is automatically activated for you as a cost allocation
tag. Tags that are automatically activated don't count towards your cost allocation tag
quota. For more information, see [Quotas and
restrictions](../../../awsaccountbilling/latest/aboutv2/billing-limits.md "../../../awsaccountbilling/latest/aboutv2/billing-limits.md"). 9. Enter and replace your **MPE ID** with the tag value you
want to apply to the migrated workloads.

**Example**:

    * If your MPE ID is `12345`, use the value
     `mig12345`.
    * If your MPE ID is `ABCDE12345`, use the value
     `migABCDE12345`.

10. Choose **Review**. 11. Choose **Apply tag** changes.
Depending on your migrated resource and MPE ID, the tag value can be any of the
following:

- `mig`5-digit MPE ID``
- `sap`5-digit MPE ID``
- `oracle`5-digit MPE ID``

- `mig`10 alphanumeric MPE ID characters``
- `sap`10 alphanumeric MPE ID characters``
- `oracle`10 alphanumeric MPE ID
  characters``

###### Note

Use lowercase letters for the `mig`, `sap`, and
`oracle` prefixes and uppercase letters for the alphanumeric MPE IDs (long MPE
IDs). For more information about what tag values you should use, see [Tagging key combinations](setting-up.md "setting-up.md"). For more information about your MPE ID, see [MPE ID length](mpe-length.md "mpe-length.md").
