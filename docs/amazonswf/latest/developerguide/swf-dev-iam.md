# Basic Principles

Amazon SWF access control is based primarily on two types of permissions:

- Resource permissions: Which Amazon SWF resources a user can access.

You can express resource permissions only for domains.

- API permissions: Which Amazon SWF actions a user can call.
  The simplest approach is to grant full account access—call any Amazon SWF action in
  any domain—or deny access entirely. However, IAM supports a more granular approach
  to access control that is often more useful. For example, you could:

- Allow a user to call any Amazon SWF action without restrictions, but only in a
  specified domain. You could use such a policy to allow workflow applications that are
  under development to use any action, but only a "sandbox" domain.
- Allow a user to access any domain, but constrain how they use the API. You could
  use such a policy to allow an "auditor" application to call the API in any domain,
  but allow only read access.
- Allow a user to call only a limited set of actions in certain domains. You could
  use such a policy to allow a workflow starter to call only the
  `StartWorkflowExecution` action in a specified domain.
  Amazon SWF access control is based on the following principles:

- Access control decisions are based only on IAM policies; all policy auditing and
  manipulation is done through IAM.
- The access control model uses a deny-by-default policy; any access that isn't
  explicitly allowed is denied.
- You control access to Amazon SWF resources by attaching appropriate IAM policies to
  the workflow's actors.
- Resource permissions can be expressed only for domains.
- You can further constrain the usage of some actions by applying conditions to one
  or more parameters.
- If you grant permission to use [RespondDecisionTaskCompleted](../apireference/API_RespondDecisionTaskCompleted.md "../apireference/API_RespondDecisionTaskCompleted.md"), you can express permissions for the list of
  decisions included in that action.

Each of the decisions has one or more parameters, much like a regular API call. To
allow for policies to be as readable as possible, you can express permissions on
decisions as if they were actual API calls, including applying conditions to some
parameters. These types of permissions are called _pseudo API_
permissions.
For a summary of which regular and pseudo API parameters can be constrained by using
conditions, see [API Summary](swf-dev-iam.md "swf-dev-iam.md").
