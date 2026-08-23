# Adding and ordering steps

Steps are numbered from 1 and run in ascending order. A plan can contain up to 20
steps and up to 100 source servers in total across all of its steps.

The following rules apply to steps:

- A source server can appear in only one step within a single plan. The same
  source server can appear in more than one plan.
- A wait step cannot be the first step in a plan, because there is nothing to
  wait for.
- A wait step must be between 1 and 120 minutes.
- You cannot change a step's type after you create it. To change a server step
  into a wait step, delete it and create a new one.
  To add a server step with the AWS CLI, use the
  `create-recovery-plan-step` command with a
  `serverStepConfiguration`. Servers that you do not give an
  `impactLevel` default to `CRITICAL`.

```
aws drs create-recovery-plan-step \
    --recovery-plan-arn `PLAN_ARN` \
    --step-name "Database tier" \
    --configuration '{
        "serverStepConfiguration": {
            "servers": [
                {"serverArn": "`SERVER_ARN_1`", "impactLevel": "CRITICAL"},
                {"serverArn": "`SERVER_ARN_2`", "impactLevel": "OPTIONAL"}
            ]
        }
    }'
```

To add a wait step, use a `waitStepConfiguration` instead.

```
aws drs create-recovery-plan-step \
    --recovery-plan-arn `PLAN_ARN` \
    --step-name "Wait for database startup" \
    --configuration '{"waitStepConfiguration": {"waitDurationMinutes": 10}}'
```

By default, a new step is added to the end of the plan. To insert a step at a specific
position, include `--step-order`; the steps at and after that position move
down by one. To reorder the steps that a plan already has, use
`reorder-recovery-plan-steps` and pass the complete list of step ARNs in
the order that you want.

```
aws drs reorder-recovery-plan-steps \
    --recovery-plan-arn `PLAN_ARN` \
    --ordered-step-arns `STEP_ARN_2` `STEP_ARN_1` `STEP_ARN_3`
```

To change the servers in a server step, use
`update-recovery-plan-step`. The server list is replaced in full, so
include every server that you want the step to keep.

## Finding a source server ARN

The step APIs identify a source server by its ARN, in the
`serverArn` field. A source server ARN has the following
format.

```
arn:`partition`:drs:`region`:`account-id`:source-server/s-`EXAMPLE1`
```

To find the ARNs of your source servers, use
`describe-source-servers` and read the `arn` field of each
entry in the response.

```
aws drs describe-source-servers \
    --query 'items[].{arn:arn,hostname:sourceProperties.identificationHints.hostname}'
```

###### Note

The step APIs take a full ARN in `serverArn`, but
`start-recovery-plan-execution` takes the short source server ID
in `sourceServerID` instead, for example
`s-`EXAMPLE1``. The short ID is the last
part of the ARN, after `source-server/`.
