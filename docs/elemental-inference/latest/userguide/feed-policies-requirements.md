

# Policy requirements
<a name="feed-policies-requirements"></a>

Elemental Inference validates a feed policy when you attach it, and rejects the request with a validation error if the policy does not meet the following requirements:
+ The policy must include the `Version` and `Statement` elements.
+ Each statement must include the `Sid`, `Effect`, `Principal`, `Action`, and `Resource` elements. The `Sid` value must be unique within the policy.
+ The only supported action is `elemental-inference:GetMetadata`.
+ The `Principal` element cannot be a wildcard (`*`).
+ The policy cannot use the `NotAction`, `NotPrincipal`, or `NotResource` elements, and cannot specify a principal group.
+ The policy document can be at most 2,048 characters.

The `Condition` element is optional. For guidance on the conditions to include, see [Security considerations](feed-policies-security.md).