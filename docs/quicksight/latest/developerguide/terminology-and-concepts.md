# Terminology and concepts

Following, you can find a list of terms and concepts used to describe Amazon Quick Sight development
in the _Amazon Quick Sight Developer Guide_.

**Anonymous Quick Sight user** – A temporary Quick Sight user
identity that virtually belongs to a namespace and that you can use only with embedding. You
can use tag-based rules to implement row-level security for such users.

**Caller identity** – The
identity of the IAM user making an API request. The
identity of the caller is determined by Quick Sight using the signature
attached to the request. Through the use of our provided SDK
clients, no manual steps are necessary to generate the signature or
attach it to the requests. However, you can do it manually if you
want to.

**Invoker identity** – In addition to the caller
identity, but not as a replacement for it, you can assume a caller's identity through the
IAM `AssumeRole` API operation when making calls to Quick Sight. AWS approves callers
through their invoker’s identity. This approval means that you can avoid having to
explicitly add multiple accounts belonging to the same Quick Sight subscription.

**Namespace** – A logical container that you can use to
isolate user pools so that you can organize clients, subsidiaries, teams, and so on.

**Quick Sight ARN** – Amazon Resource Name (ARN). Quick Sight
resources are identified using their name or ARN. For example, the following are ARNs for a
group named `MyGroup1`, a user named `User1`, and a dashboard with the
ID `1a1ac2b2-3fc3-4b44-5e5d-c6db6778df89`.

```
arn:aws:quicksight:us-east-1:111122223333:group/default/MyGroup1
		arn:aws:quicksight:us-east-1:111122223333:user/default/User1
		arn:aws:quicksight:us-west-2:111122223333:dashboard/1a1ac2b2-3fc3-4b44-5e5d-c6db6778df89
```

The following examples show ARNs for a template named
`MyTemplate` and a dashboard named
`MyDashboard`.

- The following is the sample ARN for a template.

```
arn:aws:quicksight:us-east-1:111122223333:template/MyTemplate
```

- The following is the sample ARN for a template, referencing a specific version of the
  template.

```
arn:aws:quicksight:us-east-1:111122223333:template/MyTemplate/version/10
```

- The following is the sample ARN for a template alias.

```
arn:aws:quicksight:us-east-1:111122223333:template/MyTemplate/alias/STAGING
```

- The following is the sample ARN for a dashboard.

```
arn:aws:quicksight:us-east-1:111122223333:dashboard/MyDashboard
```

- The following is the sample ARN for a dashboard, referencing a specific version of the
  dashboard.

```
arn:aws:quicksight:us-east-1:111122223333:dashboard/MyDashboard/version/10
```

Depending on the scenario, you might need to provide an entity's name, ID, or ARN. You can
retrieve the ARN if you have the name, using some of the Quick Sight API operations.

**Quick Sight dashboard** – An entity that identifies
Quick Sight reports, created from analyses or templates. You can share Quick Sight dashboards.
With the right permissions, you can create scheduled email reports from them. The
`CreateDashboard` and `DescribeDashboard` API operations act on
the dashboard entity.

**Quick Sight template** – An entity that encapsulates the
metadata required to create an analysis or a dashboard. It abstracts the dataset associated
with the analysis by replacing it with placeholders. You can use templates to create
dashboards by replacing dataset placeholders with datasets. These datasets need to follow
the same schema that was used to create the source analysis and template.

**Quick Sight user** – This is an Quick Sight user identity acted
on by your API call. This user isn't identical to the caller identity but might be the one
that maps to the user in Quick Sight.
