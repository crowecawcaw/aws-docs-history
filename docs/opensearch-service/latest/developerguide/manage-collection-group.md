# Manage Amazon OpenSearch Serverless collection groups

After creating Amazon OpenSearch Serverless collection groups, you can modify their settings as your
needs change. Use these management operations to update capacity limits and view
collection group details. These changes help you optimize resource allocation and
maintain efficient organization of your collections.

## View collection groups

Display your OpenSearch Serverless collection groups to review their configurations, associated
collections, and current status.

Console

1. Open the Amazon OpenSearch Service console at
   [https://console.aws.amazon.com/aos/](https://console.aws.amazon.com/aos/ "https://console.aws.amazon.com/aos/").
2. In the left navigation pane, choose
   **Serverless**, then choose
   **Collections**
3. Choose the **Collection groups tab**. Your
   account's collection groups are displayed.
4. Choose the **Name** of a collection group to
   display its details.

AWS CLI

- Use the [list-collection-groups](../../../cli/latest/reference/opensearchserverless/list-collection-groups.md "../../../cli/latest/reference/opensearchserverless/list-collection-groups.md") command to list all
  collection groups in your account. Use the [batch-get-collection-group](../../../cli/latest/reference/opensearchserverless/batch-get-collection-group.md "../../../cli/latest/reference/opensearchserverless/batch-get-collection-group.md") command to view details
  about specific collection groups. In the following commands,
  replace the `example` content with your
  own specific information.

To list all collection groups:

```

aws opensearchserverless list-collection-groups

```

To get details about specific collection groups:

```

aws opensearchserverless batch-get-collection-group \
    --names `my-collection-group` `another-group`

```

## Update collection group settings

Update your OpenSearch Serverless collection group settings to modify configurations such as
capacity limits and description.

Console

1. Open the Amazon OpenSearch Service console at
   [https://console.aws.amazon.com/aos/](https://console.aws.amazon.com/aos/ "https://console.aws.amazon.com/aos/").
2. In the left navigation pane, choose
   **Serverless**, then choose
   **Collections**
3. Choose the **Collection groups tab**. Your
   account's collection groups are displayed.
4. Choose the **Name** of a collection group to
   display its details.
5. In **Collection group details**, choose
   **Edit**.
6. Make any changes, then choose
   **Save**.

AWS CLI

- Use the [update-collection-group](../../../cli/latest/reference/opensearchserverless/update-collection-group.md "../../../cli/latest/reference/opensearchserverless/update-collection-group.md") command to update the
  description and capacity limits of an existing collection group.
  In the following command, replace the
  `example` content with you own
  information.

```

aws opensearchserverless update-collection-group \
    --id `abcdef123456` \
    --description "`Updated description for production workloads`" \
    --capacity-limits maxIndexingCapacityInOCU=`30`,maxSearchCapacityInOCU=`30`,minIndexingCapacityInOCU=`4`,minSearchCapacityInOCU=`4`

```

Changes to capacity limits take effect immediately and might impact the scaling
behavior of collections in the group.

## Delete collection groups

Before you can delete a collection group, you must first remove all collections
from the group. You cannot delete a collection group that contains
collections.

Console

1. Open the Amazon OpenSearch Service console at
   [https://console.aws.amazon.com/aos/](https://console.aws.amazon.com/aos/ "https://console.aws.amazon.com/aos/").
2. In the left navigation pane, choose
   **Serverless**, then choose
   **Collections**
3. Choose the **Collection groups tab**. Your
   account's collection groups are displayed.
4. Choose the **Name** of the collection group
   you want to delete.

###### Important

Remove all collections from the collection group by
updating each collection to remove the collection group
association or by moving them to other collection
groups. 5. At the top of the page, choose
**Delete**. 6. Confirm deletion, then choose
**Delete**.

AWS CLI

- Use the [delete-collection-group](../../../cli/latest/reference/opensearchserverless/delete-collection-group.md "../../../cli/latest/reference/opensearchserverless/delete-collection-group.md") command to delete a
  collection group.

###### Important

Remove all collections from the collection group by
updating each collection to remove the collection group
association or by moving them to other collection
groups.

In the following command, replace the
`example` content with you own
information.

Delete the empty collection group:

```

aws opensearchserverless delete-collection-group \
    --id `abcdef123456`

```
