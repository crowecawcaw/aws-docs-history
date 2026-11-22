

# Working with spaces in Amazon OpenSearch Memory

In Amazon OpenSearch Memory, a *space* is the AWS resource that stores your events and memories. A space also defines which memory strategies extract memories, how long events and memories are kept, which model does the extraction, and which key encrypts the data. You control access to events and memories by controlling access to their space.

This topic describes how to create and manage spaces. The child topics describe memory strategies, events, memories, and search.

**Topics**
+ [Space IDs and ARNs](#memory-spaces-ids)
+ [Space settings](#memory-spaces-settings)
+ [Space status](#memory-spaces-status)
+ [Creating a space](#memory-spaces-create)
+ [Viewing spaces](#memory-spaces-view)
+ [Updating a space](#memory-spaces-update)
+ [Deleting a space](#memory-spaces-delete)
+ [Tagging a space](#memory-spaces-tagging)
+ [Memory strategies in Amazon OpenSearch Memory](memory-strategies.md)
+ [Working with events in Amazon OpenSearch Memory](memory-events.md)
+ [Working with memories in Amazon OpenSearch Memory](memory-memories.md)
+ [Searching memories and events in Amazon OpenSearch Memory](memory-search.md)

## Space IDs and ARNs
<a name="memory-spaces-ids"></a>

Each space has an ID that OpenSearch Memory assigns, for example `sp-02864597b164`. You pass the ID in every operation that acts on the space or its data.

Each space also has an Amazon Resource Name (ARN) in the following format. You use the ARN in IAM policies and in the tagging operations.

```
arn:aws:osm:{{region}}:{{account-id}}:space/{{space-id}}
```

## Space settings
<a name="memory-spaces-settings"></a>

The following table describes the settings of a space.


| Setting | Description | Changeable after creation | 
| --- | --- | --- | 
| name | A name from 1 to 128 characters that is unique among the spaces in your account and Region. It must start with a letter and can contain letters, digits, spaces, underscores, and hyphens. | No | 
| memoryStrategies | Up to 10 memory strategies. A space with no strategies stores events but doesn't extract memories. For more information, see [Memory strategies in Amazon OpenSearch Memory](memory-strategies.md). | Yes | 
| eventExpiryDays | How many days the space keeps each event, from 1 to 365. The default is 90. | Yes | 
| memoryExpiryDays | How many days the space keeps each memory, from 1 to 3,650. Specify 0 to keep memories indefinitely. If you don't set this value, memories are kept indefinitely. | Yes | 
| extractionModelId | The model that extracts and consolidates memories for every strategy in the space. For more information, see [Choosing an extraction model](#memory-spaces-model). | Yes | 
| encryptionConfiguration | The AWS KMS key that encrypts the space's data. By default, an AWS owned key. For more information, see [Choosing an encryption key](#memory-spaces-encryption). | No | 
| tags | Up to 50 key-value pairs. For more information, see [Tagging a space](#memory-spaces-tagging). | Yes | 

### Configuring retention
<a name="memory-spaces-retention"></a>

A space keeps each event for `eventExpiryDays` and each memory for `memoryExpiryDays`. OpenSearch Memory counts a memory's lifetime from the time it writes the memory. Updating a memory doesn't restart the count.

When an event or memory expires, it is removed. An expired memory is no longer returned by searches or lists, and reading, updating, or deleting it returns `ResourceNotFoundException`, the same as for a memory that never existed.

When you change a retention setting, the change applies to events and memories written after the change. Items already stored keep the lifetime they were written with. A memory that OpenSearch Memory rewrites later, such as a summary that it keeps up to date, takes the setting in effect at the rewrite.

**Note**  
[GetSpace](https://docs.aws.amazon.com/opensearch-service/latest/MemoryAPIReference/API_GetSpace.html) returns a retention setting only if you have set it. If `eventExpiryDays` or `memoryExpiryDays` is absent from the response, the space uses the default: 90 days for events, and no expiry for memories.

### Choosing an extraction model
<a name="memory-spaces-model"></a>

OpenSearch Memory uses one model to extract and consolidate memories for every strategy in a space. You can choose from the following models by specifying the model ID in `extractionModelId`:
+ `anthropic.claude-haiku-5-5` – The default. Lower cost and latency.
+ `anthropic.claude-opus-5-5` – Higher quality extraction, at higher cost.

Specify the model ID exactly as shown, without a Region or inference-profile prefix. If you omit the setting, the space uses the service default, which can change over time. To keep a space on one model, set the value explicitly. After you set a model, you can change it to the other supported model, but you can't return the space to the service default.

You don't need to request access to the model or grant any permissions for it. OpenSearch Memory calls the model on your behalf. Model calls may be processed in another AWS Region within the same geography as your space. Your spaces and the data stored in them stay in the Region where you created them. For more information, see [Data location](memory-data-protection.md#memory-data-location).

### Choosing an encryption key
<a name="memory-spaces-encryption"></a>

By default, OpenSearch Memory encrypts a space's data with an AWS owned key. To use a customer managed key in AWS Key Management Service (AWS KMS) instead, specify the key's ARN in `encryptionConfiguration.kmsKeyArn` when you create the space. You can't change the key after the space is created.

The key must be a symmetric encryption key that is enabled and in the same Region as the space. The principal that creates the space needs the `kms:CreateGrant` permission on the key, and principals that read and write the space's data need permission to use the key. For more information, see [Key management](memory-data-protection.md#memory-key-management).

## Space status
<a name="memory-spaces-status"></a>

A space's status tells you whether you can use or change it.


| Status | Meaning | 
| --- | --- | 
| CREATING | OpenSearch Memory is setting up the space. You can't send events, update, or delete the space yet. | 
| ACTIVE | The space is ready to use. | 
| UPDATING | OpenSearch Memory is applying a change from [UpdateSpace](https://docs.aws.amazon.com/opensearch-service/latest/MemoryAPIReference/API_UpdateSpace.html). GetSpace returns the previous configuration until the change is applied. You can't update or delete the space until then. | 
| DELETING | OpenSearch Memory is deleting the space and its memories. | 
| FAILED | Creating, updating, or deleting the space failed. statusReason explains why. | 

When deletion finishes, `GetSpace` returns `ResourceNotFoundException`.

The AWS SDKs and the AWS CLI provide two waiters: `SpaceActive`, which waits until a space is `ACTIVE`, and `SpaceDeleted`, which waits until a space no longer exists. Use them instead of polling `GetSpace` yourself.

## Creating a space
<a name="memory-spaces-create"></a>

To create a space, call [CreateSpace](https://docs.aws.amazon.com/opensearch-service/latest/MemoryAPIReference/API_CreateSpace.html) with a name. All other settings are optional.

The following AWS CLI example creates a space that keeps events for 30 days, keeps memories indefinitely, uses the Opus model for extraction, and encrypts its data with a customer managed key. Replace the key ARN with the ARN of your own key.

```bash
aws opensearchmemory create-space \
    --name support-agent-memory \
    --event-expiry-days 30 \
    --memory-expiry-days 0 \
    --extraction-model-id anthropic.claude-opus-5-5 \
    --encryption-configuration kmsKeyArn=arn:aws:kms:us-east-1:111122223333:key/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111 \
    --memory-strategies '[{"type":"SEMANTIC","name":"user-facts"},{"type":"SUMMARY","name":"session-summary"}]' \
    --tags '[{"key":"team","value":"support"}]'
```

The call returns with the status `CREATING`. Wait until the status is `ACTIVE` before you send events.

The AWS CLI and SDKs add a `clientToken` to the request. If a request is retried with the same token within 2 hours, OpenSearch Memory returns the space that the first request created instead of creating a second one. For more information, see [Idempotent requests](memory-errors.md#memory-errors-idempotency).

**To create a space (console)**

1. Open the [Amazon OpenSearch Service console](https://console.aws.amazon.com/aos/home).

1. In the navigation pane, under **Memory**, choose **Spaces**, and then choose **Create Space**.

1. For **Creation method**, choose one of the following:
   + **Easy create** – Creates the space with a `SEMANTIC` strategy and a `SUMMARY` strategy and the default settings. Enter a **Space name** and choose **Create Space**.
   + **Standard create** – Lets you choose strategies and configure them, set event and memory expiry, choose an encryption key, and add tags. The extraction model can be set only with the API.

1. Choose **Create Space**.

The space appears in the list with the status **Creating**. When it is ready, the status changes to **Active**.

## Viewing spaces
<a name="memory-spaces-view"></a>

To view a space's settings, status, and strategies, call `GetSpace` with the space ID.

```bash
aws opensearchmemory get-space --space-id sp-02864597b164
```

The response includes any strategy names that OpenSearch Memory generated for strategies that you created without a name.

To list the spaces in your account in the current Region, call [ListSpaces](https://docs.aws.amazon.com/opensearch-service/latest/MemoryAPIReference/API_ListSpaces.html). Each entry includes the space's ID, ARN, name, status, and creation time. Use `--max-results` to control the page size, from 1 to 100, and pass the returned `nextToken` to get the next page.

```bash
aws opensearchmemory list-spaces --max-results 20
```

## Updating a space
<a name="memory-spaces-update"></a>

To change a space's strategies, retention settings, or extraction model, call `UpdateSpace`. Supply only the settings you want to change. Settings you omit keep their current values.

The following example changes how long a space keeps events.

```bash
aws opensearchmemory update-space \
    --space-id sp-02864597b164 \
    --event-expiry-days 60
```

Note the following about updates:
+ To change the strategies, supply the complete new list in `memoryStrategies`. The list must contain at least one strategy. For more information, see [Updating and removing strategies](memory-strategies.md#memory-strategies-update).
+ A change to strategies, retention, or the extraction model moves the space to `UPDATING` while it is applied, then back to `ACTIVE`. A request that changes nothing, or changes only a strategy description, is applied immediately.
+ You can't update a space that is `CREATING`, `UPDATING`, or `DELETING`. The request fails with `ConflictException`. Wait for the space to return to `ACTIVE` and try again.
+ Once you set `memoryExpiryDays`, `extractionModelId`, or a strategy configuration value, you can change it to another value but you can't unset it. To stop memories from expiring, set `memoryExpiryDays` to 0.

On the console, choose the space name on the **Spaces** page and then choose **Edit**. You can edit the strategies and the retention settings of an **Active** space.

## Deleting a space
<a name="memory-spaces-delete"></a>

**Warning**  
Deleting a space permanently deletes its memories. You can't undo the deletion or recover the memories. You can't retrieve the space's events after you delete it, and they are removed when they reach their expiry.

When you no longer need a space, call [DeleteSpace](https://docs.aws.amazon.com/opensearch-service/latest/MemoryAPIReference/API_DeleteSpace.html) with the space ID.

```bash
aws opensearchmemory delete-space --space-id sp-02864597b164
```

The call returns with the status `DELETING`, and deletion continues after the call returns. When it finishes, `GetSpace` returns `ResourceNotFoundException`. Use the `SpaceDeleted` waiter to wait for this.

Deleting a space deletes its memories. The space's events are removed when they reach the end of their retention period. To remove events sooner, delete them with [DeleteEvent](https://docs.aws.amazon.com/opensearch-service/latest/MemoryAPIReference/API_DeleteEvent.html) before you delete the space.

You can't delete a space that is `CREATING` or `UPDATING`. Wait for the space to become `ACTIVE`, then delete it. Calling `DeleteSpace` on a space that is already `DELETING` returns `DELETING` again, so you can safely retry the call.

**To delete a space (console)**

1. Open the [Amazon OpenSearch Service console](https://console.aws.amazon.com/aos/home).

1. In the navigation pane, under **Memory**, choose **Spaces**.

1. Select the space and choose **Delete**.

1. Enter the space name to confirm, and then choose **Delete**.

## Tagging a space
<a name="memory-spaces-tagging"></a>

A tag is a key-value pair that you attach to a space to organize it, track costs, or control access. You can add tags when you create a space with the `tags` parameter, and manage tags on an existing space with [TagResource](https://docs.aws.amazon.com/opensearch-service/latest/MemoryAPIReference/API_TagResource.html), [UntagResource](https://docs.aws.amazon.com/opensearch-service/latest/MemoryAPIReference/API_UntagResource.html), and [ListTagsForResource](https://docs.aws.amazon.com/opensearch-service/latest/MemoryAPIReference/API_ListTagsForResource.html), which take the space's ARN.

```bash
aws opensearchmemory tag-resource \
    --resource-arn arn:aws:osm:us-east-1:111122223333:space/sp-02864597b164 \
    --tags '[{"key":"environment","value":"production"}]'
```

A tag key can have up to 128 characters, and a tag value up to 256 characters. A space can have up to 50 tags. On the console, manage tags on the space's **Tags** tab.

Adding tags when you create a space requires the `osm:TagResource` permission in addition to `osm:CreateSpace`. You can use the `aws:ResourceTag/{{key}}`, `aws:RequestTag/{{key}}`, and `aws:TagKeys` condition keys to control access to spaces based on their tags. For more information, see [ABAC with OpenSearch Memory](security-iam-memory.md#security_iam_memory-with-iam-tags).