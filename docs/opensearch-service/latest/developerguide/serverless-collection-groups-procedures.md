# Create collection

groups

This topic describes how to create, configure, and manage collection groups in
Amazon OpenSearch Serverless. Use collection groups to organize collections and share compute resources to
optimize costs. Set minimum and maximum OCU limits at the collection group level to
control performance and spending.

## Create a collection group

Use the following procedures to create a new collection group and configure its
settings. Create a collection group using the OpenSearch Serverless console, AWS CLI, or the AWS
SDKs . When you create a collection group, you specify capacity limits and other
configuration options.

Console

1. Open the Amazon OpenSearch Service console at
   [https://console.aws.amazon.com/aos/](https://console.aws.amazon.com/aos/ "https://console.aws.amazon.com/aos/").
2. In the left navigation pane, choose
   **Serverless**, then choose
   **Collection groups**
3. Choose **Create collection group**.
4. For **Collection group name**, enter a name
   for your collection group. The name must be 3-32 characters
   long, start with a lowercase letter, and contain only lowercase
   letters, numbers, and hyphens.
5. (Optional) For **Description**, enter a
   description for your collection group.
6. In the **Capacity management** section,
   configure the OCU limits:
   - **Maximum indexing capacity** – The
     maximum number of indexing OCUs that collections in this
     group can scale up to.
   - **Maximum search capacity** – The
     maximum number of search OCUs that collections in this
     group can scale up to.
   - **Minimum indexing capacity** – The
     minimum number of indexing OCUs to maintain for
     consistent performance.
   - **Minimum search capacity** – The
     minimum number of search OCUs to maintain for consistent
     performance.

7. (Optional) In the **Tags** section, add tags
   to help organize and identify your collection group.
8. Choose **Create collection group**.

AWS CLI

- Use the [create-collection-group](../../../cli/latest/reference/opensearchserverless/create-collection-group.md "../../../cli/latest/reference/opensearchserverless/create-collection-group.md") command to create a new
  collection group. In the command, replace the
  `example` content with your own
  specific information.

```

aws opensearchserverless create-collection-group \
    --name `my-collection-group` \
    --description "`Collection group for production workloads`" \
    --capacity-limits maxIndexingCapacityInOCU=`20`,maxSearchCapacityInOCU=`20`,minIndexingCapacityInOCU=`2`,minSearchCapacityInOCU=`2` \
    --tags key=`Environment`,value=`Production` key=`Team`,value=`DataEngineering`

```

The command returns details about the created collection
group, including its unique ID and ARN.

## Add a new collection to a collection

group

When creating a new collection, specify an existing collection group name to
associate the collection with. Use the following procedures to add a new collection
to a collection group.

Console

1. Open the Amazon OpenSearch Service console at
   [https://console.aws.amazon.com/aos/](https://console.aws.amazon.com/aos/ "https://console.aws.amazon.com/aos/").
2. In the left navigation pane, choose
   **Serverless**, then choose
   **Collections**
3. Choose **Create collection**.
4. For **Collection name**, enter a name for
   your collection. The name must be 3-28 characters long, start
   with a lowercase letter, and contain only lowercase letters,
   numbers, and hyphens.
5. (Optional) For **Description**, enter a
   description for your collection.
6. In the **Collection group** section, select
   the collection group you want the collection to be assigned to.
   A collection can only belong to one collection group at a
   time.

(Optional) You can also choose to **Create a new
group**. This will navigate you to the
**Create collection group** workflow. After
you finish creating the collection group, return to the step 1
of this procedure to begin creating your new collection. 7. Continue through the workflow to create the collection.

###### Important

Do not navigate away from the **Create
collection** workflow. Doing so will stop the
collection setup. The **Collection
details** page appears after setup
completes.

AWS CLI

- Use the [create-collection](../../../cli/latest/reference/opensearchserverless/create-collection.md "../../../cli/latest/reference/opensearchserverless/create-collection.md") command to create a new
  collection and add it to an existing collection group. In the
  command, replace the `example` content
  with your own specific information.

```

aws opensearchserverless create-collection \
    --name `my-collection` \
    --type SEARCH \
    --collection-group-name `my-collection-group` \
    --description "`Collection for search workloads`"

```
