# Key Amazon SNS access policy

concepts

The following sections describe the concepts you need to understand to use the
access policy language. They're presented in a logical order, with the first terms you need to know at
the top of the list.

## Permission

A _permission_ is the concept of allowing or disallowing some kind of
access to a particular resource. Permissions essentially follow this form: "A is/isn't
allowed to do B to C where D applies." For example, _Jane_ (A) has
permission to _publish_ (B) to _TopicA_ (C) as long as
_she uses the HTTP protocol_ (D). Whenever Jane publishes to TopicA,
the service checks to see if she has permission and if the request satisfies the conditions
set forth in the permission.

## Statement

A _statement_ is the formal description of a single permission,
written in the access policy language. You always write a statement as part of a broader container
document known as a _policy_ (see the next concept).

## Policy

A _policy_ is a document (written in the access policy language) that acts as
a container for one or more statements. For example, a policy could have two statements in
it: one that states that Jane can subscribe using the email protocol, and another that
states that Bob cannot publish to Topic A. As shown in the following figure, an equivalent
scenario would be to have two policies, one that states that Jane can subscribe using the
email protocol, and another that states that Bob cannot publish to Topic A.

![Compares two ways of organizing policy statements in Amazon SNS. On the left, a single policy (Policy A) contains two statements. On the right, the same two statements are split between two policies, with each policy containing one statement. The diagram illustrates that these two approaches are equivalent in terms of how permissions are defined and enforced.](images/AccessPolicyLanguage_Statement_and_Policy.gif)

Only ASCII characters are allowed in policy documents. You can utilize
`aws:SourceAccount` and `aws:SourceOwner` to work around the
scenario where you need to plug-in other AWS services' ARNs that contain non-ASCII
characters. See the difference between [aws:SourceAccount versus
aws:SourceOwner](sns-access-policy-use-cases.md#source-account-versus-source-owner "sns-access-policy-use-cases.md#source-account-versus-source-owner").

## Issuer

The _issuer_ is the person who writes a policy to grant permissions
for a resource. The issuer (by definition) is always the resource owner. AWS does not
permit AWS service users to create policies for resources they don't own. If John is the
resource owner, AWS authenticates John's identity when he submits the policy he's written
to grant permissions for that resource.

## Principal

The _principal_ is the person or persons who receive the permission
in the policy. The principal is A in the statement "A has permission to do B to C where D
applies." In a policy, you can set the principal to "anyone" (that is, you can specify a
wildcard to represent all people). You might do this, for example, if you don't want to
restrict access based on the actual identity of the requester, but instead on some other
identifying characteristic such as the requester's IP address.

## Action

The _action_ is the activity the principal has permission to perform.
The action is B in the statement "A has permission to do B to C where D applies." Typically,
the action is just the operation in the request to AWS. For example, Jane sends a request
to Amazon SNS with `Action``=Subscribe`. You can specify one or multiple
actions in a policy.

## Resource

The _resource_ is the object the principal is requesting access to.
The resource is C in the statement "A has permission to do B to C where D applies."

## Conditions and keys

The _conditions_ are any restrictions or details about the
permission. The condition is D in the statement "A has permission to do B to C where D
applies." The part of the policy that specifies the conditions can be the most detailed and
complex of all the parts. Typical conditions are related to:

- Date and time (for example, the request must arrive before a specific day)
- IP address (for example, the requester's IP address must be part of a particular
  CIDR range)

A _key_ is the specific characteristic that is the basis for access
restriction. For example, the date and time of request.

You use both _conditions_ and _keys_ together to
express the restriction. The easiest way to understand how you actually implement a
restriction is with an example: If you want to restrict access to before May 30, 2010, you
use the condition called `DateLessThan`. You use the key called
`aws:CurrentTime` and set it to the value `2010-05-30T00:00:00Z`.
AWS defines the conditions and keys you can use. The AWS service itself (for example,
Amazon SQS or Amazon SNS) might also define service-specific keys. For more information, see [Amazon SNS API permissions:
Actions and resources reference](sns-access-policy-language-api-permissions-reference.md "sns-access-policy-language-api-permissions-reference.md").

## Requester

The _requester_ is the person who sends a request to an AWS service
and asks for access to a particular resource. The requester sends a request to AWS that
essentially says: "Will you allow me to do B to C where D applies?"

## Evaluation

_Evaluation_ is the process the AWS service uses to determine if an
incoming request should be denied or allowed based on the applicable policies. For
information about the evaluation logic, see [Evaluation logic](sns-access-policy-language-evaluation-logic.md "sns-access-policy-language-evaluation-logic.md").

## Effect

The _effect_ is the result that you want a policy statement to return
at evaluation time. You specify this value when you write the statements in a policy, and
the possible values are _deny_ and _allow_.

For example, you could write a policy that has a statement that
_denies_ all requests that come from Antarctica (effect=deny given that
the request uses an IP address allocated to Antarctica). Alternately, you could write a
policy that has a statement that _allows_ all requests that
_don't_ come from Antarctica (effect=allow given that the request
doesn't come from Antarctica). Although the two statements sound like they do the same
thing, in the access policy language logic, they are different. For more information, see [Evaluation logic](sns-access-policy-language-evaluation-logic.md "sns-access-policy-language-evaluation-logic.md").

Although there are only two possible values you can specify for the effect (allow or
deny), there can be three different results at policy evaluation time: _default
deny_, _allow_, or _explicit deny_. For
more information, see the following concepts and [Evaluation logic](sns-access-policy-language-evaluation-logic.md "sns-access-policy-language-evaluation-logic.md").

## Default deny

A _default deny_ is the default result from a policy in the absence
of an allow or explicit deny.

## Allow

An _allow_ results from a statement that has effect=allow, assuming
any stated conditions are met. Example: Allow requests if they are received before 1:00 p.m.
on April 30, 2010. An allow overrides all default denies, but never an explicit deny.

## Explicit deny

An _explicit deny_ results from a statement that has effect=deny,
assuming any stated conditions are met. Example: Deny all requests if they are from
Antarctica. Any request that comes from Antarctica will always be denied no matter what any
other policies might allow.
