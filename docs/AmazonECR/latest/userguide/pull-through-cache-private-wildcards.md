# Customizing repository prefixes

for ECR to ECR pull through cache

Pull through cache rules support both the **ecr repository prefix**
and the **upstream repository prefix**. The **ecr repository
prefix** is the repository namespace prefix in Amazon ECR cache registry that's
associated with the rule. All repositories using this prefix become pull through
cache-enabled repositories for the upstream registry defined in the rule. For example, a
prefix of `prod` applies to all repositories beginning with
`prod/`. To apply a template to all repositories in your registry that
don't have an associated pull through cache rule, use `ROOT` as the
prefix.

###### Important

There is always an assumed `/` applied to the end of the prefix. If you
specify `ecr-public` as the prefix, Amazon ECR treats that as
`ecr-public/`.

The **upstream repository prefix** matches the upstream repository
name. By default, it's set to `ROOT`, which allows matching with any upstream
repository. You can set the **upstream repository prefix** only when
the Amazon ECR repository prefix has a non-`ROOT` value.

The following table shows the mapping between cache repository names and upstream
repository names based on their prefix configurations in pull through cache
rules.

| Cache namespace | Upstream namespace | Mapping relationship (cache repository → upstream<br>repository)                                   |
| --------------- | ------------------ | -------------------------------------------------------------------------------------------------- |
| ecr-public      | ROOT (default)     | `ecr-public/my-app/image1` →<br>`my-app/image1`<br>`ecr-public/my-app/image2` →<br>`my-app/image2` |
| ROOT            | ROOT               | `my-app/image1` → `my-app/image1`                                                                  |
| team-a          | team-a             | `team-a/myapp/image1` →<br>`team-a/myapp/image1`                                                   |
| my-app          | upstream-app       | `my-app/image1` →<br>`upstream-app/image1`                                                         |
