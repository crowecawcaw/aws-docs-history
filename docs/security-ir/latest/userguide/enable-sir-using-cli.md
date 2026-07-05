# Enable Security Incident Response and configure your incident response team using the API/CLI

This section provides steps to enable AWS Security Incident Response, designate a delegated administrator for AWS Security Incident Response, and configure your incident response team using the API/CLI.

As a manager of the Organizations, make sure that you read the
[Considerations and
recommendations](considerations_important.md "considerations_important.md") on how a delegated Security Incident Response administrator account operates. Before
proceeding, ensure that you have [Permissions required to designate a delegated Security Incident Response administrator account](organizations_permissions.md "organizations_permissions.md").

Onboard with a delegated administrator using the API/CLI (recommended)

1. Create the `AWSServiceRoleForSecurityIncidentResponse_Triage` service-linked role in your AWS Organizations management account:

```
aws iam create-service-linked-role --aws-service-name "triage.security-ir.amazonaws.com"
```

2. (Optional) To verify that the role was created, run the following command:

```
aws iam get-role --role-name AWSServiceRoleForSecurityIncidentResponse_Triage
```

3. From your AWS Organizations management account, register the delegated administrator account for AWS Security Incident Response:

```
aws organizations register-delegated-administrator \
  --account-id `delegated-admin-account-id` \
  --service-principal security-ir.amazonaws.com
```

4. Enable AWS Security Incident Response service access for your organization:

```
aws organizations enable-aws-service-access \
  --service-principal security-ir.amazonaws.com
```

5. Sign in to the delegated administrator account to create a membership and designate your incident response team. You must list at least two incident response team members.

```
aws security-ir create-membership \
  --membership-name "`membership-name`" \
  --incident-response-team '[
    {
      "name": "`name`",
      "jobTitle": "`job-title`",
      "email": "`email@example.com`",
      "communicationPreferences": ["Case Created", "Case Closed"]
    },
    {
      "name": "`name`",
      "jobTitle": "`job-title`",
      "email": "`email@example.com`",
      "communicationPreferences": ["Case Created", "Case Closed"]
    }
  ]'
```

6. (Optional) Verify that the membership was created:

```
aws security-ir list-memberships
```

7. (Optional) Get the membership details:

```
aws security-ir get-membership \
  --membership-id `membership-id`
```

Onboard with a management account using the API/CLI

1. Enable AWS Security Incident Response service access for your organization:

```
aws organizations enable-aws-service-access \
  --service-principal security-ir.amazonaws.com
```

2. Sign in to the management account to create a membership and designate your incident response team. You must list at least two incident response team members.

```
aws security-ir create-membership \
  --membership-name "`membership-name`" \
  --incident-response-team '[
    {
      "name": "`name`",
      "jobTitle": "`job-title`",
      "email": "`email@example.com`",
      "communicationPreferences": ["Case Created", "Case Closed"]
    },
    {
      "name": "`name`",
      "jobTitle": "`job-title`",
      "email": "`email@example.com`",
      "communicationPreferences": ["Case Created", "Case Closed"]
    }
  ]'
```

3. (Optional) Verify that the membership was created:

```
aws security-ir list-memberships
```

4. (Optional) Get the membership details:

```
aws security-ir get-membership \
  --membership-id `membership-id`
```
