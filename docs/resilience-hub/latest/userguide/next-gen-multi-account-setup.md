# Multi-account setup (without AWS Organizations)

If your service's resources span multiple AWS accounts and you are not using AWS
Organizations, you need cross-account roles in addition to the invoker role.

**Step 1: Create cross-account roles**

In each account that contains resources for your service, create a role with:

- `ReadOnlyAccess` policy attached.
- A trust policy that allows the invoker role to assume it, using an
  `ExternalId` to prevent confused deputy attacks. Use a unique
  `ExternalId` value per service and account combination:

```
{
  "Version": "2012-10-17",
  "Statement": [{
    "Effect": "Allow",
    "Principal": {
      "Service": "resiliencehub.amazonaws.com"
    },
    "Action": "sts:AssumeRole"
  },
  {
    "Effect": "Allow",
    "Principal": {
      "AWS": "arn:aws:iam::123456789012:role/AWSResilienceHubAssessmentRole"
    },
    "Action": "sts:AssumeRole",
    "Condition": {
      "StringEquals": {
        "sts:ExternalId": "ngrh-my-service-111122223333"
      }
    }
  }]
}
```

**Step 2: Grant the invoker role permission to assume cross-account
roles**

Add an inline policy to your invoker role that allows it to assume the cross-account
roles:

```
{
  "Effect": "Allow",
  "Action": "sts:AssumeRole",
  "Resource": [
    "arn:aws:iam::111122223333:role/NGRHResourceRole",
    "arn:aws:iam::444455556666:role/NGRHResourceRole"
  ]
}
```

**Step 3: Configure cross-account roles on your service**

Specify the cross-account role ARNs and external IDs when creating the service:

```
aws resiliencehubv2 create-service \
  --name "my-service" \
  --regions '["us-east-1"]' \
  --permission-model '{
    "invokerRoleName": "AWSResilienceHubAssessmentRole",
    "crossAccountRoles": [
      {
        "crossAccountRoleArn": "arn:aws:iam::111122223333:role/NGRHResourceRole",
        "externalId": "ngrh-my-service-111122223333"
      },
      {
        "crossAccountRoleArn": "arn:aws:iam::444455556666:role/NGRHResourceRole",
        "externalId": "ngrh-my-service-444455556666"
      }
    ]
  }'
```

You can configure up to 5 cross-account role ARNs per service.
