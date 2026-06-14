# Creating a resilience policy

You can create resilience policies from the the next generation of Resilience Hub console or AWS CLI.

**Console:**

1. Navigate to **Resilience Hub** > **Policies**.
2. Choose **Create policy**.
3. Enter a policy name and description.
4. Select the components you need:

   - Toggle **Multi-Region DR** and set RTO/RPO.
   - Toggle **Availability SLO** and set target
     percentage.
   - Toggle **Data recovery objective** and set time between
     backups.

5. Choose **Create**.
   **AWS CLI:**

```
aws resiliencehubv2 create-policy \
  --name "Critical Service Policy" \
  --multi-region '{"rtoInMinutes": 15, "rpoInMinutes": 5, "disasterRecoveryApproach": "WARM_STANDBY"}' \
  --availability-slo '{"target": 99.99}'
```
