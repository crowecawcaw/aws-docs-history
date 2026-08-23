# Creating a recovery plan

Create an empty plan, then add the steps that define your recovery order. A plan
cannot be run until it contains at least one server step:

###### To create a recovery plan (console)

1. Open the Elastic Disaster Recovery console at [https://console.aws.amazon.com/drs/home](https://console.aws.amazon.com/drs/home "https://console.aws.amazon.com/drs/home").
2. In the navigation pane, choose **Recovery
   plans**.
3. Choose **Create recovery plan**.
4. Enter a **Name** for the plan. The name must be
   unique within your account and Region.
5. (Optional) Enter a **Description**.
6. Add your steps in the order that you want them to run. For each server step,
   select the source servers to recover in that step and set the impact level for
   each one. For each wait step, enter the number of minutes to pause.
7. Review the plan and choose **Create recovery
   plan**.
   To create a plan with the AWS CLI, use the `create-recovery-plan`
   command.

```
aws drs create-recovery-plan \
    --name "Tier1-ecommerce" \
    --description "Database, application, and web tiers for the storefront"
```

The response includes the `recoveryPlanArn` that you use to add steps and
to start an execution.

A plan name must be 1 to 256 characters long, must start with a letter or a number,
and can contain letters, numbers, spaces, underscores, and hyphens.
