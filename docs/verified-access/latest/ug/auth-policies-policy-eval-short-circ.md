# Verified Access policy logic short-circuiting

You might want to write an AWS Verified Access policy that evaluates data that may or may not be
present in a given context. If you reference data in a context that does not exist, Cedar will
produce an error and evaluate the policy to deny access, regardless of your intent. For
example, this would result in a deny, as `fake_provider` and `bogus_key`
do not exist in this context.

```
permit(principal, action, resource) when {
  context.fake_provider.bogus_key > 42
};
```

To avoid this situation, you can check to see if a key is present by using the
`has` operator. If the `has` operator returns false, further
evaluation of the chained statement halts, and Cedar does not produce an error attempting to
reference an item that does not exist.

```
permit(principal, action, resource) when {
  context.identity.user has "some_key" && context.identity.user.some_key > 42
};
```

This is most useful when specifying a policy that references two different trust
providers.

```
permit(principal, action, resource) when {
  // user is in an allowed group
  context.aws_idc.groups has "c242c5b0-6081-1845-6fa8-6e0d9513c107"
  &&(
    (
      // if CrowdStrike data is present,
      // permit if CrowdStrike's overall assessment is over 50
      context has "crowdstrike" && context.crowdstrike.assessment.overall > 50
    )
    ||
    (
      // if Jamf data is present,
      // permit if Jamf's risk score is acceptable
      context has "jamf" && ["LOW", "NOT_APPLICABLE", "MEDIUM", "SECURE"].contains(context.jamf.risk)
    )
  )
};
```
