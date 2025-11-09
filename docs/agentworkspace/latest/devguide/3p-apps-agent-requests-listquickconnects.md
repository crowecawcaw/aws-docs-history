# Get the list of Quick

Connect endpoints associated with a given queue in Amazon Connect Agent Workspace

Get the list of Quick Connect endpoints associated with the given queue(s).
Optionally you can pass in a parameter to override the default max-results value of 500.

**Signature**

```
listQuickConnects(
    queueARNs: QueueARN | QueueARN[],
    options?: ListQuickConnectsOptions,
  ): Promise<ListQuickConnectsResult>

```

**Usage**

```
const routingProfile: AgentRoutingProfile = await agentClient.getRoutingProfile();
const quickConnects: ListQuickConnectsResult = await agentClient.listQuickConnects(routingProfile.queues[0].queueARN);

```

**Input**

| **Parameter**        | **Type** | **Description**                                                                                                                                       |
| -------------------- | -------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| queueARNs _Required_ | string   | string[]                                                                                                                                              | One or more Queue ARNs for which the Queue Connects need to be<br>retrieved |
| options.maxResults   | number   | The maximum number of results to return per page. The default<br>value is 500                                                                         |
| options.nextToken    | string   | The token for the next set of results. Use the value returned in<br>the previous response in the next request to retrieve the next set<br>of results. |

**Output - ListQuickConnectsResult**

| **Parameter** | **Type**       | **Description**                                                                                                                                                                   |
| ------------- | -------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| quickConnects | QuickConnect[] | Its either AgentQuickConnect or QueueQuickConnect or<br>PhoneNumberQuickConnect which contains endpointARN and name.<br>Additionally PhoneNumberQuickConnect contains phoneNumber |
| nextToken     | string         | If there are additional results, this is the token for the next<br>set of results.                                                                                                |

**Permissions required:**

```
User.Configuration.View

```
