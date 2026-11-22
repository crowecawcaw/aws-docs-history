

# Testing and integrations

The **Testing and integrations** step tells you which AWS Marketplace API integrations your product requires, gives you the instructions for each, and verifies the ones AWS Marketplace can check automatically.

Which tasks appear depends on your product type and pricing model. If your product requires no integrations, you do not see this step. Professional services products do not have it. Where the step falls in the **Complete your listing** journey also depends on your product type.

**Publishing will fail until your required integrations are complete.** AWS Marketplace also runs its own publish-time checks, which are separate from the checks on this step.

**Topics**
+ [How verification works](#how-verification-works)
+ [Opening the step](#opening-the-step)
+ [Which tasks apply to your product](#which-tasks-apply)
+ [Running a check](#running-a-check)
+ [Reading your test results](#reading-results)
+ [Tasks you confirm yourself](#self-attested)
+ [Building your integration with an AI agent](#ai-agent)
+ [Known limitations](#ti-limitations)
+ [Troubleshooting](#ti-troubleshooting)

## How verification works
<a name="how-verification-works"></a>

This is the most important thing to understand before you use this step.

**Verification does not test your integration.** It does not call your software, send test traffic, or run in a sandbox. It asks AWS Marketplace whether it already holds a record of your integration working.

That record is one of two things:
+ A usage submission AWS Marketplace received from you, for the metering checks.
+ A successful API call AWS Marketplace recorded, for the buyer onboarding and entitlement checks.

Choosing Verify before the call is recorded has three consequences:

1. **You must make the real call before you choose Verify.** Choosing Verify before your software has made the call always fails. There is nothing for AWS Marketplace to find.

1. **The call must come from the AWS account that owns the listing.** A successful call from a different account does not satisfy the check.

1. **The check looks back over a bounded window.** Metering, buyer onboarding, and entitlement checks all look back 90 days. A call older than the window cannot be found, even though it succeeded.

To exercise a paid product without being charged, use the task on this step that creates a $0 private offer targeted at your own account, then subscribe to it.

You can also create the $0 private offer with the AWS Marketplace Catalog API rather than from the task card.

## Opening the step
<a name="opening-the-step"></a>

**To open Testing and integrations**

1. Sign in to the AWS Partner Central console at `https://us-east-1.console.aws.amazon.com/partnercentral/home`.

1. In the left navigation pane, under **Build**, choose the product type you are working on. The Products and services page opens.

1. Choose your product to open **Product overview**.

1. Choose the **Testing and integrations** tab.

Each required integration appears as a card. Choose a card to open its instructions.

The step is locked until you complete the earlier steps of your listing. While it is locked you see **No integrations configured**, with the message "Complete the previous steps to unlock integrations."

If your product type and pricing model require no integrations, you do not see this step at all.

## Which tasks apply to your product
<a name="which-tasks-apply"></a>

### Checks AWS Marketplace runs for you
<a name="which-tasks-apply-checks"></a>


| Task | Applies to | API you must call | How to build it | 
| --- | --- | --- | --- | 
| Integrate with buyer onboarding | SaaS, all pricing models | `ResolveCustomer` | [ResolveCustomer API reference](https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-metering_ResolveCustomer.html) | 
| Integrate with entitlements | SaaS, contract-based or contract with consumption | `GetEntitlements` | [Checking entitlements using the AWS Marketplace Entitlement Service](checking-entitlements.md) | 
| Integrate with metering | SaaS, usage-based | `BatchMeterUsage` | [Configuring metering for usage with SaaS subscriptions](metering-for-usage.md) | 
| Integrate with metering | SaaS, contract with consumption | `BatchMeterUsage` | [Configuring metering for usage with SaaS subscriptions](metering-for-usage.md) | 
| Integrate with metering | AMI, usage-based | `MeterUsage` | [Configuring custom metering for AMI products with AWS Marketplace Metering Service](custom-metering-with-mp-metering-service.md) | 
| Integrate with hourly metering | Container, hourly | `RegisterUsage` | [Configuring hourly metering with AWS Marketplace Metering Service](container-metering-registerusage.md) | 
| Integrate with custom metering | Container, usage-based | `MeterUsage` | [Configuring custom metering for container products with AWS Marketplace Metering Service](container-metering-meterusage.md) | 

For how to build each integration, see the implementation page for your product type in the preceding table.

### Setup steps and confirmations
<a name="which-tasks-apply-setup"></a>

The step also lists tasks that are not checks. These appear in a separate **Test setup** table, described as "Complete these setup steps before running a test. These steps are not tests, so they do not pass or fail." See [Tasks you confirm yourself](#self-attested).

## Running a check
<a name="running-a-check"></a>

**To verify an integration**

1. Make sure your software has made the required call from the account that owns the listing, within the lookback window.

1. Open the task card.

1. Read **Instructions** for how to build the integration, and **Complete verification** for what this specific check looks for.

1. Choose **Verify**.

The check can take up to 2 minutes to return. If no result arrives in that time, choose **Verify again**.

After a check runs, **Verify** is relabeled **Verify again**, whether it passed or failed. You can rerun a check at any time.

### What you see
<a name="running-a-check-what-you-see"></a>


| Outcome | Message | 
| --- | --- | 
| Passed | **Verification passed.** "AWS Marketplace received the expected call. This task is complete." | 
| Failed, with detail | **Verification incomplete**, followed by what the check could not confirm. | 
| Failed, no detail | **Verification incomplete.** "AWS Marketplace could not confirm this task. Review the steps on this page, then choose Verify again." | 
| Could not start | "The verification could not be started. Try again." | 
| **Timed out** | "Something went wrong. Choose Verify again." | 
| Previous result unreadable | "The latest result for this task could not be loaded. You can still verify it." | 

A failed check shows on the progress bar as **Error**, not as incomplete.

### Container hourly metering
<a name="running-a-check-container-hourly"></a>

For `RegisterUsage`, deploy your container as an Amazon Elastic Container Service (Amazon ECS) task in US East (N. Virginia), wait about 25 minutes, and then choose **Verify**.

**Note**  
Register within the first 6 hours of container launch. The buyer is charged in 1-minute increments, rounded up, and charging continues until the container stops.

`RegisterUsage` timing on Amazon Elastic Kubernetes Service cannot be verified. Amazon ECS is a requirement for this check, not a recommendation.

If **Integrate with hourly metering** reports that the product code could not be found, the check could not match your call to a product code on this listing. Confirm that your container passes the product code from this listing to `RegisterUsage`, and that the call came from the AWS account that owns the listing. Publishing stays blocked until this task completes.

## Reading your test results
<a name="reading-results"></a>

The **Testing and integrations** tab carries a **Test results** table showing every integration configured on the step and the result of each check.


| Result | Meaning | 
| --- | --- | 
| **Not run** | The check has not been run yet. | 
| **Running** | The check is in progress. | 
| **Passed** | AWS Marketplace confirmed the call. | 
| **Failed** | AWS Marketplace could not confirm the call. | 
| **Complete** | You confirmed the task yourself. AWS Marketplace ran no check. | 
| **Not applicable** | Nothing to report for this item. | 

The distinction between **Passed** and **Complete** is worth attention. **Passed** means AWS Marketplace found evidence. **Complete** means you asserted it and AWS Marketplace verified nothing.

## Tasks you confirm yourself
<a name="self-attested"></a>

Some tasks have no automated check. For these, the action is **Mark as complete**, and the verification text reads "Mark complete if done." AWS Marketplace stores your confirmation and runs no check.

**AWS License Manager integration for contract pricing is one of these, for both AMI and container products.** There is no automated check for `CheckoutLicense`. You choose **Mark as complete** and AWS Marketplace does not confirm the integration works. Test it yourself before you publish.

Other self-confirmed tasks depend on your product type and can include configuring your SaaS as an API-based AI agent and tool, creating an AMI and service role, adding CloudFormation templates, embedding a runtime check for your product code, scanning your assets, adding a version, adding a container repository, pushing your container image, adding a delivery method, and the Amazon SageMaker AI setup tasks. The step shows you the set that applies to your product.

If a confirmation does not save, you see **Confirmation not saved**: "We could not save your confirmation, so this task is still incomplete. Choose Try again."

### Amazon SageMaker AI has no automated checks
<a name="self-attested-sagemaker"></a>

Every Amazon SageMaker AI task in this step is self-confirmed. Verify your integration yourself.

## Building your integration with an AI agent
<a name="ai-agent"></a>

Two options, and they are different.

**Ask the AI agent.** Available on every task. Opens the AWS Partner Central assistant with the task's details already in context, so you can ask questions about the integration in front of you.

**Get the skill.** Available on some tasks. Gives your own coding agent the **AWS Marketplace AI Metering Agent Skill** (`aws-marketplace-metering`), a curated package of instructions and reference material that guides the agent through building, deploying, and testing your metering integration. The agent can then carry out the steps against your codebase, generate the API calls with your dimensions filled in, and explain what to check when a call does not land. It is the same skill for every task on this step, so you add it once.

To get the skill without checking it out locally, install the [AWS MCP Server](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/mcp-server.html) in your coding agent. The agent then discovers and loads the skill at runtime. The skill source is also available on [GitHub](https://github.com/aws/agent-toolkit-for-aws/blob/main/skills/specialized-skills/aws-marketplace-skills/aws-marketplace-metering). For a walkthrough, see [Get started with the AWS Marketplace AI Metering Agent Skill](https://aws.amazon.com/blogs/awsmarketplace/build-aws-marketplace-saas-metering-with-the-metering-agent-skill/) on the AWS Marketplace blog.

The skill covers **SaaS usage-based (pay-as-you-go) metering only**. It does not cover SaaS contract pricing, contract with consumption, AMI, or container products. For those, use the instructions on the task and the implementation pages they reference.

The skill requires a one-time setup in your AWS account by an administrator, and direct deployment is limited to products in **Limited** state.

## Known limitations
<a name="ti-limitations"></a>

**High-volume products can fail a check that should pass.** For products submitting large numbers of metering records, the check can read only part of the window and may not reach your most recent records. When this happens you see a AWS Marketplace service error rather than a metering failure, and choosing **Verify again** may not clear it. If it repeats, contact AWS Marketplace Seller Operations on the [AWS Partner Central and Marketplace Support page](https://us-east-1.console.aws.amazon.com/partnercentral/support?region=us-east-1) in the AWS Partner Central console, and include the assessment ID.

**Entitlements granted outside AWS Marketplace do not clear a card.** If you grant entitlements by a method that AWS Marketplace does not record, the required card stays incomplete. The check has no record to find, so there is nothing for it to verify.

## Troubleshooting
<a name="ti-troubleshooting"></a>

**Verification fails and I know my call succeeded.**

Check, in order:

1. Did the call come from the account that owns the listing? A call from another account does not count.

1. Was the call inside the 90-day lookback window?

1. Did the call actually succeed? A call that returned `AccessDeniedException` is not a successful call, even though your application made it.

1. For metering, did the record carry both a pricing dimension and a buyer account? A record missing either is not complete evidence. From June 1, 2026, new SaaS integrations identify the agreement with `LicenseArn` and the buyer with `CustomerAWSAccountId`, in place of `ProductCode` and `CustomerIdentifier`.

1. Did every metering record from the last 24 hours use a key that matches one of the product's pricing dimensions? Keys are case sensitive, so a record carrying a key the listing does not define fails the check even though the call succeeded.

1. Did you trigger a call for **every** usage dimension on the listing? This applies to SaaS, AMI, and container products.

**I have contract with consumption pricing and no overage yet.**

Report only quantities beyond what the buyer is already entitled to. AWS Marketplace charges the buyer what you report and does not track what is and is not an overage. To satisfy verification before any overage exists, send a record with a `Quantity` of 0 for each usage dimension. It is not charged and still counts as evidence.

**A card shows no status.**

The status read timed out. Refresh the page.

**My listing will not publish.**

A banner lists the incomplete integrations with links to each. Complete those tasks, then publish. If the banner lists nothing, or publishing still fails after every task is complete, contact AWS Marketplace Seller Operations on the AWS Partner Central and Marketplace Support page in the AWS Partner Central console.