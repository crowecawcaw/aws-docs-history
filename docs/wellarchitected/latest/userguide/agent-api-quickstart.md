

AWS Well-Architected Agent is in preview release and is subject to change.

# API quickstart
<a name="agent-api-quickstart"></a>

You can set up AWS WA Agent entirely through the AWS CLI or SDK instead of the console. This quickstart walks through creating a profile, adding a goal, adding application context, and verifying eligibility.

**Note**  
Before using the API, create the execution role and access roles as described in [Step 3: Configure permissions and integrations](agent-getting-started.md#agent-permissions-integrations) and [Step 6: Create access roles in your workload accounts](agent-getting-started.md#agent-access-roles). The API does not create IAM roles for you.

## Step 1: Create an agent profile
<a name="agent-api-create-profile"></a>

Create a profile with your execution role, target pillars, and account configuration.

**To create an agent profile (CLI)**

1. Run the following command. Replace the placeholder values with your account IDs, role ARNs, and target Regions.
**Note**  
 You can choose a common access role name or enter an access role name per account. This is only available in the API version of onboarding, not in the console. 

   ```
   aws wellarchitected create-agent-profile \
       --name "my-production-profile" \
       --execution-role-arn "arn:aws:iam::{{111122223333}}:role/service-role/ExecutionRoleForWellArchitectedAgent" \
       --pillars COST_OPTIMIZATION SECURITY RESILIENCE PERFORMANCE \
       --aggregation-configuration '[{"accountId":"{{444455556666}}","accessRoleArn":"arn:aws:iam::{{444455556666}}:role/AccessRoleForWellArchitectedAgent","regions":["us-east-1","us-west-2"]}]'
   ```

1. In the response, note the profile ARN. You will use this value in subsequent commands.

## Step 2: Add an optimization goal
<a name="agent-api-create-goal"></a>

Add a goal to drive recommendation prioritization. Each goal is associated with one or more optimization pillars.

**To add a goal (CLI)**
+ Run the following command. Replace the profile ARN with the value from Step 1.

  ```
  aws wellarchitected create-agent-goal \
      --profile-arn "arn:aws:wellarchitected:{{us-east-1}}:{{111122223333}}:agent-profile/{{my-production-profile}}" \
      --title "Reduce EC2 spend by 20% by Q4 through rightsizing and Reserved Instance coverage" \
      --pillars COST_OPTIMIZATION
  ```

## Step 3: Add application context
<a name="agent-api-create-context"></a>

Provide application metadata so AWS WA Agent can generate more relevant, personalized recommendations.

**To add application context (CLI)**
+ Run the following command. Replace the profile ARN and content fields with your application details.

  ```
  aws wellarchitected create-agent-context \
      --profile-arn "arn:aws:wellarchitected:{{us-east-1}}:{{111122223333}}:agent-profile/{{my-production-profile}}" \
      --title "Payment processing service" \
      --context-type APPLICATION \
      --content '{"applicationOverview":"Real-time payment processing","criticality":"MISSION_CRITICAL","accountIds":["{{444455556666}}"],"regions":["us-east-1"]}'
  ```

## Step 4: Verify profile eligibility
<a name="agent-api-verify-eligibility"></a>

Check that your profile is valid and eligible for recommendation generation.

**To verify eligibility (CLI)**

1. Run the following command:

   ```
   aws wellarchitected get-agent-profile \
       --profile-arn "arn:aws:wellarchitected:{{us-east-1}}:{{111122223333}}:agent-profile/{{my-production-profile}}" \
       --query '{eligible: eligibleForScheduledGeneration, errors: fieldErrors}'
   ```

1. If `eligibleForScheduledGeneration` is `true`, your profile is properly configured. Scheduled recommendations will begin generating within 48 hours.

1. If `eligibleForScheduledGeneration` is `false`, check the `fieldErrors` map for specific issues. See [Troubleshooting AWS Well-Architected Agent](agent-troubleshooting.md) for common resolutions.

For the complete API reference, see the [AWS Well-Architected API Reference](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/Welcome.html).