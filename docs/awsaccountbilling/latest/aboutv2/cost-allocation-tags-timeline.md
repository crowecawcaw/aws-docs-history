# Understanding dates for cost allocation

tags

###### Prerequisites

To view these dates in the **Cost allocation tags** page of the
AWS Billing and Cost Management console, you must have the `ce:ListCostAllocationTags`
permission.

For more information about updating your AWS Identity and Access Management (IAM) policies, see [Managing access permissions](migrate-granularaccess-whatis.md#migrate-control-access-billing "migrate-granularaccess-whatis.md#migrate-control-access-billing").

When you use cost allocation tags, you can determine when the tags were last used or
last updated with the following metadata fields:

- **Last updated date** – The last date that the tag key
  was either activated or deactivated for cost allocation.

For example, suppose that your tag key `lambda:createdby` changed
from inactive to active on July 1, 2023. This means that the **Last
updated date** column will show July 1, 2023.

- **Last used month** – The last month that the tag key
  was used on an AWS resource.

For example, suppose that your tag key `lambda:createdby` was last
used on April 2023. The **Last used month** column will show
April 2023. This means that the tag key hasn't been associated with any resource
since that date.

###### Notes

    + The **Last updated date** column appears empty
     for newly created tag keys that haven't been activated.
    + The **Last used month** column shows
     **-** for tag keys that aren't currently associated with any
     resource.
