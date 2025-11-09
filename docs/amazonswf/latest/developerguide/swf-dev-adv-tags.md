# Tags in Amazon SWF

Amazon SWF supports tagging a workflow execution. This is especially useful when you have many
resources.

Amazon SWF supports tagging a workflow execution with up to five tags. Each tag is a free-form
string and may be up to 256 characters in length. If you want to use tags, you must assign them
when you start a workflow execution. You can't add tags to a workflow execution after it has
been started, nor may you edit or remove tags that have been assigned to a workflow
execution.

IAM supports controlling access to Amazon SWF domains based on tags. To control access based on
tags, provide information about your tags in the condition element of an IAM policy.

## Manage tags

Manage Amazon Simple Workflow Service tags using the AWS SDKs or by interacting directly with the Amazon SWF API. Using the API you can
add tags when registering a domain, list tags for an existing domain, and add or delete tags for an existing domain.

###### Note

There is a limit of 50 tags per resource. See [General Account Quotas for Amazon SWF](swf-dg-limits.md#swf-dg-limits-general "swf-dg-limits.md#swf-dg-limits-general")

- [`RegisterDomain`](../apireference/API_RegisterDomain.md "../apireference/API_RegisterDomain.md")
- [`ListTagsForResource`](../apireference/API_ListTagsForResource.md "../apireference/API_ListTagsForResource.md")
- [`TagResource`](../apireference/API_TagResource.md "../apireference/API_TagResource.md")
- [`UntagResource`](../apireference/API_UntagResource.md "../apireference/API_UntagResource.md")

For more information see [Working with Amazon SWF APIs](swf-dg-using-swf-api.md "swf-dg-using-swf-api.md"), and [Amazon Simple Workflow Service API Reference](../apireference.md "../apireference.md").

## Tag workflow executions

With Amazon SWF, you can associate tags with workflow executions and then query for workflow executions based
on these tags. You can filter the listi when you use the visibility operations.
By carefully selecting the tags you assign to an execution, you can use them to provide meaningful
listings.

For example, suppose you run several fulfillment centers. With tags, you could list the
processes occurring in a specific fulfillment center. Or, if a customer is converting
different types of media files, tags could indicate different processes when converting
video, audio, and image files.

You can
associate up to five tags with a workflow execution when you start the execution using the
`StartWorkflowExecution` action, `StartChildWorkflowExecution` decision, or
`ContinueAsNewWorkflowExecution` decision. When you use
visibility actions to list or count workflow executions, you can filter results based on your tags.

###### To use tagging

1. Devise a tagging strategy. Think about your business requirements and create a list of tags that are
   meaningful to you. Determine which executions will get which tags. Even though an execution can be assigned a
   maximum of five tags, your tag library can have any number of tags. Because each tag can be any string value up to
   256 characters in length, a tag can describe almost any business concept.
2. Tag an execution with up to five tags when you create it.
3. List or count the executions that are tagged with a particular tag by specifying the
   _tagFilter_ parameter with the `ListOpenWorkflowExecutions`,
   `ListClosedWorkflowExecutions`, `CountOpenWorkflowExecutions`, and
   `CountClosedWorkflowExecutions` actions. The action will filter the executions based on the tags
   specified.

When you associate a tag with a workflow execution, it is permanently associated with that execution, and can't
be removed.

You can specify only one tag in the `tagFilter` parameter with
`ListWorkflowExecutions`. Also, tag matching is case sensitive, and only exact matches return results.

Assume you have already set up two executions that are tagged as follows.

| Execution Name | Assigned Tags           |
| -------------- | ----------------------- |
| Execution-One  | Consumer, 2011-February |
| Execution-Two  | Wholesale, 2011-March   |

You can filter the list of executions returned by `ListOpenWorkflowExecutions` on the Consumer tag.
The `oldestDate` and `latestDate` values are specified as [Unix Time](https://en.wikipedia.org/wiki/Unix_time "https://en.wikipedia.org/wiki/Unix_time") values.

```
https://swf.us-east-1.amazonaws.com
  RespondDecisionTaskCompleted
  {
    "domain":"867530901",
    "startTimeFilter":{
        "oldestDate":1262332800,
        "latestDate":1325348400
    },
    "tagFilter":{
      "tag":"Consumer"
      }
  }
```

## Control access to domains with tags

You can control access to Amazon Simple Workflow Service domains by referencing tags associated with Amazon SWF
domains in IAM.

For instance, you could restrict Amazon SWF domains that include a tag with the key
`environment` and the value `production` with the following
condition:

```
"Condition": {
    "StringEquals": {"aws:ResourceTag/environment": "production"}
}
```

For more information, see:

- [Controlling Access Using IAM
  Tags](../../../IAM/latest/UserGuide/access_iam-tags.md "../../../IAM/latest/UserGuide/access_iam-tags.md")
- [Tag-based Policies](tag-based-policies.md "tag-based-policies.md")
