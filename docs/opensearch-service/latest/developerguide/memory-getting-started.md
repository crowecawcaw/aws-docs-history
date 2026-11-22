

# Getting started with Amazon OpenSearch Memory

This tutorial shows the basic Amazon OpenSearch Memory workflow with the AWS Command Line Interface (AWS CLI). You create a space, send a short conversation to it as an event, search the memories that OpenSearch Memory extracts, and then delete the space.

**Important**  
This tutorial creates resources that incur charges to your AWS account. You're charged for the space, the stored event and memories, and the model calls that extract the memories. The charges stop when you delete the space in [Step 5: Clean up](#memory-getting-started-cleanup). For more information, see [Amazon OpenSearch Service pricing](https://aws.amazon.com/opensearch-service/pricing/).

**Topics**
+ [Prerequisites](#memory-getting-started-prereqs)
+ [Step 1: Create a space](#memory-getting-started-create)
+ [Step 2: Wait for the space to become active](#memory-getting-started-wait)
+ [Step 3: Send an event](#memory-getting-started-event)
+ [Step 4: Search memories](#memory-getting-started-search)
+ [Step 5: Clean up](#memory-getting-started-cleanup)
+ [Next steps](#memory-getting-started-next-steps)

## Prerequisites
<a name="memory-getting-started-prereqs"></a>

Before you begin, make sure that you have the following:
+ An AWS account.
+ The AWS CLI installed and configured with credentials for an IAM identity. For more information, see [Installing the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) in the *AWS Command Line Interface User Guide*.
+ Permission to perform the following actions: `osm:CreateSpace`, `osm:GetSpace`, `osm:DeleteSpace`, `osm:CreateEvent`, and `osm:SearchMemories`. For an example policy that grants exactly these permissions, see [Running the getting started tutorial](security-iam-memory.md#security-iam-memory-policy-example-tutorial).

The examples use the Region `us-east-1`. To use another Region, change the `--region` value in each command.

## Step 1: Create a space
<a name="memory-getting-started-create"></a>

A space stores your events and memories and defines the memory strategies that extract the memories. In this step, you create a space with two strategies: a `SEMANTIC` strategy named `user-facts` that extracts facts, and a `SUMMARY` strategy that summarizes each conversation.

Run the following command.

```bash
aws opensearchmemory create-space \
    --region us-east-1 \
    --name getting-started-space \
    --memory-strategies '[{"type":"SEMANTIC","name":"user-facts"},{"type":"SUMMARY"}]'
```

The response includes the ID of the new space and its status.

```json
{
    "spaceId": "sp-02864597b164",
    "arn": "arn:aws:osm:us-east-1:111122223333:space/sp-02864597b164",
    "name": "getting-started-space",
    "status": "CREATING",
    "createdAt": "2026-11-14T00:30:12Z"
}
```

Make a note of the `spaceId` value. You use it in every remaining step.

The `SUMMARY` strategy has no name, so OpenSearch Memory generates one for it. You can see the generated name in the [GetSpace](https://docs.aws.amazon.com/opensearch-service/latest/MemoryAPIReference/API_GetSpace.html) response in the next step.

**Note**  
To create a space from the console instead, open the Amazon OpenSearch Service console, choose **Memory** and then **Spaces** in the navigation pane, choose **Create Space**, keep the **Easy create** method, enter a name, and choose **Create Space**. Easy create gives the space the same two strategies that this step creates.

## Step 2: Wait for the space to become active
<a name="memory-getting-started-wait"></a>

[CreateSpace](https://docs.aws.amazon.com/opensearch-service/latest/MemoryAPIReference/API_CreateSpace.html) returns while OpenSearch Memory is still setting up the space. You can't send events to the space until its status is `ACTIVE`. Run the following command to wait.

```bash
aws opensearchmemory wait space-active \
    --region us-east-1 \
    --space-id sp-02864597b164
```

The command returns when the space is active, which usually takes a few minutes. Then view the space.

```bash
aws opensearchmemory get-space \
    --region us-east-1 \
    --space-id sp-02864597b164
```

The response shows the status `ACTIVE` and the two strategies, including the name that OpenSearch Memory generated for the `SUMMARY` strategy.

```json
{
    "spaceId": "sp-02864597b164",
    "arn": "arn:aws:osm:us-east-1:111122223333:space/sp-02864597b164",
    "name": "getting-started-space",
    "status": "ACTIVE",
    "createdAt": "2026-11-14T00:30:12Z",
    "memoryStrategies": [
        { "type": "SEMANTIC", "name": "user-facts" },
        { "type": "SUMMARY", "name": "summary_1" }
    ]
}
```

If the status is `FAILED`, the `statusReason` field explains why. For more information, see [Space status](memory-spaces.md#memory-spaces-status).

## Step 3: Send an event
<a name="memory-getting-started-event"></a>

An event carries content for one actor in one session. In this step, you send a two-turn conversation for the actor `user-123` in the session `session-001`.

Save the following request in a file named `event.json`. Replace the `spaceId` value with your space ID.

```json
{
    "spaceId": "sp-02864597b164",
    "actorId": "user-123",
    "sessionId": "session-001",
    "payload": {
        "conversational": {
            "unified": {
                "source": {
                    "object": {
                        "messages": [
                            {
                                "role": "USER",
                                "content": { "text": "I'm vegetarian, so please suggest meat-free recipes." }
                            },
                            {
                                "role": "ASSISTANT",
                                "content": { "text": "Here are three meat-free recipes for this week." }
                            }
                        ]
                    }
                }
            }
        }
    }
}
```

Then run the following command.

```bash
aws opensearchmemory create-event \
    --region us-east-1 \
    --cli-input-json file://event.json
```

The response confirms that the event is stored.

```json
{
    "event": {
        "eventId": "ev-8f3a2c1d9b7e",
        "spaceId": "sp-02864597b164",
        "actorId": "user-123",
        "sessionId": "session-001",
        "eventTimestamp": "2026-11-14T00:35:41Z"
    }
}
```

Note the following about the request:
+ `actorId` identifies who the conversation is about. Every search is scoped to one actor.
+ `sessionId` groups the turns of one conversation. Send every event of the same conversation with the same session ID.
+ `messages` lists the turns in order. Each turn has a `role` and its text in `content.text`. For the roles, see [Conversational](memory-events.md#memory-events-payloads-conversational).
+ The AWS CLI adds a `clientToken` to the request for you, so a retried request doesn't create a second event.

## Step 4: Search memories
<a name="memory-getting-started-search"></a>

OpenSearch Memory extracts memories after the event is stored, when one of the strategy's extraction triggers fires. The conversation in Step 3 has two messages, which is fewer than the default of 12, so extraction starts when the session has been idle for 60 seconds, the default idle timeout. To configure extraction triggers, see [Extraction triggers](memory-strategies.md#memory-strategies-triggers).

After a brief time, run the following command.

```bash
aws opensearchmemory search-memories \
    --region us-east-1 \
    --space-id sp-02864597b164 \
    --actor-id user-123 \
    --query '{"match": {"memory_text": "vegetarian"}}'
```

The response lists the matching memories, most relevant first. The exact text depends on the extraction model and may differ from this example.

```json
{
    "memories": [
        {
            "memoryId": "mem-3b9f1c2e-7d4a-4e8b-9c1f-2a6d8e0b4f17",
            "memoryType": "SEMANTIC",
            "strategyName": "user-facts",
            "content": "The user is vegetarian.",
            "score": 1.38,
            "systemMetadata": {
                "actorId": "user-123",
                "sessionId": "session-001",
                "createdAt": "2026-11-14T00:36:52Z",
                "updatedAt": "2026-11-14T00:36:52Z"
            },
            "sourceEventIds": [ "ev-8f3a2c1d9b7e" ]
        }
    ]
}
```

If the response is empty, wait a little longer and run the command again. For more information about how long extraction takes, see [What you see, and when](memory-how-it-works.md#memory-how-it-works-consistency).

Note the following about the result:
+ The query searched the `memory_text` field. The response returns that text in `content`.
+ `score` is a relevance score.
+ `sourceEventIds` lists the events that the memory came from. You can pass these IDs to [GetEvent](https://docs.aws.amazon.com/opensearch-service/latest/MemoryAPIReference/API_GetEvent.html) to show the evidence behind a memory.

To search with a natural-language question instead of keywords, use a `neural` query. For more information, see [Searching memories and events in Amazon OpenSearch Memory](memory-search.md).

## Step 5: Clean up
<a name="memory-getting-started-cleanup"></a>

**Warning**  
Deleting a space permanently deletes its memories. You can't undo the deletion.

When you finish the tutorial, delete the space so that you stop incurring charges.

```bash
aws opensearchmemory delete-space \
    --region us-east-1 \
    --space-id sp-02864597b164
```

The response shows the status `DELETING`. Deletion continues after the call returns. To wait for it to finish, run the following command.

```bash
aws opensearchmemory wait space-deleted \
    --region us-east-1 \
    --space-id sp-02864597b164
```

## Next steps
<a name="memory-getting-started-next-steps"></a>

Now that you have completed the basic workflow, learn more about the following topics:
+ [How Amazon OpenSearch Memory works](memory-how-it-works.md) – How events become memories, and when each operation reflects a change.
+ [Memory strategies in Amazon OpenSearch Memory](memory-strategies.md) – How to choose strategy types, control when extraction runs, and write a `CUSTOM` extraction prompt.
+ [Working with events in Amazon OpenSearch Memory](memory-events.md) and [Working with memories in Amazon OpenSearch Memory](memory-memories.md) – The event and memory operations in detail.
+ [Searching memories and events in Amazon OpenSearch Memory](memory-search.md) – The query language.
+ [Security in Amazon OpenSearch Memory](memory-security.md) – Controlling access with IAM and encrypting a space with your own key.