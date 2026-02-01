# Amazon SWF IAM Policies

An IAM policy contains one or more `Statement` elements, each of which
contains a set of elements that define the policy. For a complete list of elements and a
general discussion of how to construct policies, see [The Access Policy Language](../../../IAM/latest/UserGuide/AccessPolicyLanguage.md "../../../IAM/latest/UserGuide/AccessPolicyLanguage.md"). Amazon SWF
access control is based on the following elements:

Effect

(Required) The effect of the statement: `deny` or
`allow`.

###### Note

You must explicitly allow access; IAM denies access by default.

Resource

(Required) The resource—an entity in an AWS service that a user can
interact with—that the statement applies to.

You can express resource permissions only for domains. For example, a policy
can allow access to only certain domains in your account. To express permissions
for a domain, set `Resource` to the domain's Amazon Resource Name
(ARN), which has the format
"arn:aws:swf:`Region`:`AccountID`:/domain/`DomainName`".
`Region` is the AWS region,
`AccountID` is the account ID with no dashes, and
`DomainName` is the domain name.

Action

(Required) The action that the statement applies to, which you refer to by
using the following format:
`serviceId`:`action`. For
Amazon SWF, set `serviceID` to `swf`. For example,
`swf:StartWorkflowExecution` refers to the [StartWorkflowExecution](../apireference/API_StartWorkflowExecution.md "../apireference/API_StartWorkflowExecution.md") action, and is used to control which users are
allowed to start workflows.

If you grant permission to use [RespondDecisionTaskCompleted](../apireference/API_RespondDecisionTaskCompleted.md "../apireference/API_RespondDecisionTaskCompleted.md"), you can also control access to the
included list of decisions by using `Action` to express permissions for
the pseudo API. Because IAM denies access by default, a decider's decision must
be explicitly allowed or it will not be accepted. You can use a `*`
value to allow all decisions.

Condition

(Optional) Expresses a constraint on one or more of an action's parameters,
which restricts the allowed values.

Amazon SWF actions often have a wide scope, which you can reduce by using IAM
conditions. For example, to limit which task lists the [PollForActivityTask](../apireference/API_PollForActivityTask.md "../apireference/API_PollForActivityTask.md")
action is allowed to access, you include a `Condition` and use the
`swf:taskList.name` key to specify the allowable lists.

You can express constraints for the following entities.

- The workflow type. The name and version have separate keys.
- The activity type. The name and version have separate keys.
- Task lists.
- Tags. You can specify multiple tags for some actions. In that case, each
  tag has a separate key.

###### Note

For Amazon SWF, the values are all strings so you constrain a parameter by using
a string operator such as `StringEquals`, which restricts the
parameter to a specified string. However, the regular string comparison
operators such as `StringEquals` require all requests to include the
parameter. If you don't include the parameter explicitly, and there is no
default value such as the default task list provided during type registration,
access will be denied.

It is often useful to treat conditions as optional, so that you can call an
action without necessarily including the associated parameter. For example, you
might want to allow a decider to specify a set of [RespondDecisionTaskCompleted](../apireference/API_RespondDecisionTaskCompleted.md "../apireference/API_RespondDecisionTaskCompleted.md") decisions, but also allow it to
specify only one of them for any particular call. In that case, you constrain
the appropriate parameters by using a `StringEqualsIfExists`
operator, which allows access if the parameter satisfies the condition, but
doesn't deny access if the parameter is absent.

For a complete list of constrainable parameters and the associated keys, see
[API Summary](swf-dev-iam.md "swf-dev-iam.md").

The following section provides examples of how to construct Amazon SWF policies. For details,
see [String Conditions](../../../IAM/latest/UserGuide/AccessPolicyLanguage_ElementDescriptions.md#AccessPolicyLanguage_ConditionType "../../../IAM/latest/UserGuide/AccessPolicyLanguage_ElementDescriptions.md#AccessPolicyLanguage_ConditionType").

## Writing policies for Amazon SWF

A workflow consists of multiple _actors_—activities, deciders, and so on. You can control access
for each actor by attaching an appropriate IAM policy.

With the following action, the actor will be granted full account access across all
regions:

- **Action** : `swf:*`
- **Resource** : `arn:aws:swf:*:123456789012:/domain/*`

You can use wildcards to have a single value represent multiple resources, actions, or
regions.

- The first wildcard (`*`) in the `Resource` value
  indicates that the resource permissions apply to all **regions**.

To restrict permissions to a single region, replace the wildcard with the
appropriate region string, such as us-east-1.

- The second wildcard (`*`) in the `Resource` value allows
  the actor to access any of the account's domains in the specified regions.
- The wildcard (`*`) in the `Action` value allows the actor
  to call any Amazon SWF action.

For details on how to use wildcards, see [Element
Descriptions](../../../IAM/latest/UserGuide/AccessPolicyLanguage_ElementDescriptions.md "../../../IAM/latest/UserGuide/AccessPolicyLanguage_ElementDescriptions.md")

### Domain Permissions

To restrict a department's workflows to a particular domain, you could grant
permission that allows an actor to call any action, but only for a specific
department.

To gran an actor access to more than one domain, express permission for each
domain as a list of Statements:

- **Action** : `swf:*`
- **Resource** :
  `arn:aws:swf:*:123456789012:/domain/department1`
- **Resource** :
  `arn:aws:swf:*:123456789012:/domain/department2`

You can allow an actor to use any Amazon SWF action in the `department1` and
`department2` domains. You can also sometimes use wildcards to
represent multiple domains.

### API Permissions and

Constraints

You control which **actions** an actor can use by
specifying the action in the `Action` element.

With the following action, an actor can only call
`StartWorkflowExecution` to start workflows. It can't use any other
actions.

- **Action** :
  `swf:StartWorkflowExecution`

###### Conditions

You can optionally constrain the action's allowable parameter values by using
a `Condition` element.

To restrict which workflows an actor can start, constrain one or more of the
`StartWorkflowExecution` parameter values, as follows:

```
"Condition" : {
   "StringEquals" : {
      "swf:workflowType.name" : "workflow1",
      "swf:workflowType.version" : "version2"
    }
}
```

An actor with the previous constraints can run only `version2` of
`workflow1` and both parameters must be included in the
request.

You can constrain a parameter without requiring it to be included in a request by
using a `StringEqualsIfExists` operator, as follows:

```
"Condition" : {
   "StringEqualsIfExists" : { "swf:taskList.name" : "task_list_name" }
}
```

An actor with the previous policy can optionally specify a task list when starting
a workflow execution.

You can constrain a list of tags for some actions. Each tag has a separate key, so
you use `swf:tagList.member.0` to constrain the first tag in the
list, `swf:tagList.member.1` to constrain the second tag in the list,
and so on, up to a maximum of 5.

You must be careful how you constrain tag lists. For instance, the following
condition is **_not_**
recommended.

The following Condition is **not** recommended
because it allows you to optionally specify either `some_ok_tag` or
`another_ok_tag`. However, the Condition constrains only the
**first element** of the tag list. The list could
have additional elements with arbitrary values that would all be allowed because
the condition doesn't apply any conditions to `swf:tagList.member.1`,
`swf:tagList.member.2`, and so on.

```
// Example to illustrate an insecure Condition
"Condition" : {
   "StringEqualsIfExists" : {
      "swf:tagList.member.0" : "some_ok_tag", "another_ok_tag"
   }
}
```

One way to address the previous issue is to disallow the use of tag lists.

The following policy ensures that only `some_ok_tag` or
`another_ok_tag` are allowed by requiring the list to have only one
element.

```
"Condition" : {
   "StringEqualsIfExists" : {
      "swf:tagList.member.0" : "some_ok_tag", "another_ok_tag"
    },
    "Null" : { "swf:tagList.member.1" : "true" }
}
```

### Pseudo API Permissions and

Constraints

To restrict the decisions available to `RespondDecisionTaskCompleted`,
you must first allow the actor to call
`RespondDecisionTaskCompleted`. You then express permissions for the
appropriate pseudo API members using the same syntax as for the regular API, as
follows:

- **Statement 1**

**Resource** :
`arn:aws:swf:*:123456789012:/domain/*`

**Action** :
`swf:RespondDecisionTaskCompleted`

- **Statement 2**

**Resource** : `*`

**Action** :
`swf:ScheduleActivityTask`

**Condition** : `"StringEquals" : {
 "swf:activityType.name" : "SomeActivityType" }`

The first `Statement` allows the actor to call
`RespondDecisionTaskCompleted`. The second statement allows the actor
to use the `ScheduleActivityTask` decision to direct Amazon SWF to
schedule an activity task. To allow all decisions, replace
"swf:ScheduleActivityTask" with "swf:\*".

You can use Condition operators to constrain parameters just as with the regular
API. The `StringEquals` operator in the previous example
`Condition` allows `RespondDecisionTaskCompleted` to
schedule an activity task for the `SomeActivityType` activity, and it
must schedule that task. If you want to allow
`RespondDecisionTaskCompleted` to use a parameter value but not
require it to do so, you can instead use the `StringEqualsIfExists`
operator.

## AWS managed policy:

SimpleWorkflowFullAccess

You can attach the `SimpleWorkflowFullAccess` policy to your IAM
identities.

This policy provides full access to the Amazon SWF configuration service.

## Service Model Limitations on IAM

Policies

You must consider service model constraints when creating IAM policies. It is
possible to create a syntactically valid IAM policy that represents an invalid Amazon SWF
request; a request that is allowed in terms of access control can still fail because it
is an invalid request.

For example, the Amazon SWF service model does **not** allow
the `typeFilter` and `tagFilter` parameters to be used in the
same `ListOpenWorkflowExecutions` request. The following condition would
allow calls that the service will reject—by throwing
`ValidationException`—as an invalid request:

```
"Condition" : {
   "StringEquals" : {
      "swf:typeFilter.name" : "workflow_name",
      "swf:typeFilter.version" : "workflow_version",
      "swf:tagFilter.tag" : "some_tag"
    }
}
```
