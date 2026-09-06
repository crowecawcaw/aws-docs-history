

# Actions, resources, and condition keys for AWS BugBust
<a name="list_bugbust"></a>

AWS BugBust (service prefix: `bugbust`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/codeguru/latest/bugbust-ug/).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/codeguru/latest/bugbust-ug/auth-and-access-control-permissions-reference.html).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/codeguru/latest/bugbust-ug/security-iam.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/bugbust/bugbust.json) for this service.

**Topics**
+ [Actions defined by AWS BugBust](#list_bugbust-actions-as-permissions)
+ [Permission-only actions for AWS BugBust](#list_bugbust-permission-only-actions)
+ [Resource types defined by AWS BugBust](#list_bugbust-resources-for-iam-policies)
+ [Condition keys for AWS BugBust](#list_bugbust-policy-keys)

## Actions defined by AWS BugBust
<a name="list_bugbust-actions-as-permissions"></a>

AWS BugBust has no API operations that can be used in the `Actions` element of an IAM policy statement.

## Permission-only actions for AWS BugBust
<a name="list_bugbust-permission-only-actions"></a>

The following actions are defined by AWS BugBust but are not directly invocable through any API operation. They can only be used in IAM policy statements to grant or deny permissions.




- **   [CreateEvent](https://docs.aws.amazon.com/codeguru/latest/bugbust-ug/auth-and-access-control-permissions-reference.html)  **
  - **Description:** Grants permission to create a BugBust event
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_bugbust-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_bugbust-aws_TagKeys)
  - **Access level:** Write

- **   [EvaluateProfilingGroups](https://docs.aws.amazon.com/codeguru/latest/bugbust-ug/auth-and-access-control-permissions-reference.html)  **
  - **Description:** Grants permission to evaluate checked-in profiling groups
  - **Resource types (\*required):** [Event\*](#list_bugbust-resource-Event)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bugbust-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [GetEvent](https://docs.aws.amazon.com/codeguru/latest/bugbust-ug/auth-and-access-control-permissions-reference.html)  **
  - **Description:** Grants permission to view customer details about an event
  - **Resource types (\*required):** [Event\*](#list_bugbust-resource-Event)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bugbust-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetJoinEventStatus](https://docs.aws.amazon.com/codeguru/latest/bugbust-ug/auth-and-access-control-permissions-reference.html)  **
  - **Description:** Grants permission to view the status of a BugBust player's attempt to join a BugBust event
  - **Resource types (\*required):** [Event\*](#list_bugbust-resource-Event)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bugbust-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [JoinEvent](https://docs.aws.amazon.com/codeguru/latest/bugbust-ug/auth-and-access-control-permissions-reference.html)  **
  - **Description:** Grants permission to join an event
  - **Resource types (\*required):** [Event\*](#list_bugbust-resource-Event)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bugbust-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [ListBugs](https://docs.aws.amazon.com/codeguru/latest/bugbust-ug/auth-and-access-control-permissions-reference.html)  **
  - **Description:** Grants permission to view the bugs that were imported into an event for players to work on
  - **Resource types (\*required):** [Event\*](#list_bugbust-resource-Event)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bugbust-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListEventParticipants](https://docs.aws.amazon.com/codeguru/latest/bugbust-ug/auth-and-access-control-permissions-reference.html)  **
  - **Description:** Grants permission to view the participants of an event
  - **Resource types (\*required):** [Event\*](#list_bugbust-resource-Event)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bugbust-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListEventScores](https://docs.aws.amazon.com/codeguru/latest/bugbust-ug/auth-and-access-control-permissions-reference.html)  **
  - **Description:** Grants permission to view the scores of an event's players
  - **Resource types (\*required):** [Event\*](#list_bugbust-resource-Event)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bugbust-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListEvents](https://docs.aws.amazon.com/codeguru/latest/bugbust-ug/auth-and-access-control-permissions-reference.html)  **
  - **Description:** Grants permission to List BugBust events
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bugbust-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListProfilingGroups](https://docs.aws.amazon.com/codeguru/latest/bugbust-ug/auth-and-access-control-permissions-reference.html)  **
  - **Description:** Grants permission to view the profiling groups that were imported into an event for players to work on
  - **Resource types (\*required):** [Event\*](#list_bugbust-resource-Event)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bugbust-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListPullRequests](https://docs.aws.amazon.com/codeguru/latest/bugbust-ug/auth-and-access-control-permissions-reference.html)  **
  - **Description:** Grants permission to view the pull requests used by players to submit fixes to their claimed bugs in an event
  - **Resource types (\*required):** [Event\*](#list_bugbust-resource-Event)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bugbust-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListTagsForResource](https://docs.aws.amazon.com/codeguru/latest/bugbust-ug/auth-and-access-control-permissions-reference.html)  **
  - **Description:** Grants permission to lists tag for a Bugbust resource
  - **Resource types (\*required):** [Event\*](#list_bugbust-resource-Event)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bugbust-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [TagResource](https://docs.aws.amazon.com/codeguru/latest/bugbust-ug/auth-and-access-control-permissions-reference.html)  **
  - **Description:** Grants permission to tag a Bugbust resource
  - **Resource types (\*required):** [Event\*](#list_bugbust-resource-Event)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_bugbust-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_bugbust-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_bugbust-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/codeguru/latest/bugbust-ug/auth-and-access-control-permissions-reference.html)  **
  - **Description:** Grants permission to untag a Bugbust resource
  - **Resource types (\*required):** [Event\*](#list_bugbust-resource-Event)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_bugbust-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_bugbust-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_bugbust-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdateEvent](https://docs.aws.amazon.com/codeguru/latest/bugbust-ug/auth-and-access-control-permissions-reference.html)  **
  - **Description:** Grants permission to update a BugBust event
  - **Resource types (\*required):** [Event\*](#list_bugbust-resource-Event)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bugbust-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateWorkItem](https://docs.aws.amazon.com/codeguru/latest/bugbust-ug/auth-and-access-control-permissions-reference.html)  **
  - **Description:** Grants permission to update a work item as claimed or unclaimed (bug or profiling group)
  - **Resource types (\*required):** [Event\*](#list_bugbust-resource-Event)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bugbust-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateWorkItemAdmin](https://docs.aws.amazon.com/codeguru/latest/bugbust-ug/auth-and-access-control-permissions-reference.html)  **
  - **Description:** Grants permission to update an event's work item (bug or profiling group)
  - **Resource types (\*required):** [Event\*](#list_bugbust-resource-Event)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bugbust-aws_ResourceTag___TagKey_)
  - **Access level:** Write



## Resource types defined by AWS BugBust
<a name="list_bugbust-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [Event](https://docs.aws.amazon.com/codeguru/latest/bugbust-ug/event-managing.html)  | arn:${Partition}:bugbust:${Region}:${Account}:events/${EventId} | [aws:ResourceTag/${TagKey}](#list_bugbust-aws_ResourceTag___TagKey_) | 

## Condition keys for AWS BugBust
<a name="list_bugbust-policy-keys"></a>

AWS BugBust defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access based on the tags that are passed in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access based on the tags associated with the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access based on the tag keys that are passed in the request | ArrayOfString | 