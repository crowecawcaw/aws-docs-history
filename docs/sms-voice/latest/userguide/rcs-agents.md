

# Managing RCS agents
<a name="rcs-agents"></a>

An AWS RCS Agent is the top-level resource in AWS End User Messaging that represents your brand for RCS messaging. It serves as the unified resource that binds together your testing agent and country launch agents (RCS for Business IDs). Keywords and two-way messaging configuration are defined on the AWS RCS Agent. Brand assets are defined on each registration (testing agent or country launch agent). For an overview of how the AWS RCS Agent relates to RCS for Business IDs, see [What is RCS?](rcs-overview.md).

The AWS RCS Agent follows this lifecycle:

1. **Create** the AWS RCS Agent.

1. **Add a testing agent** (included in the console create flow; optional via CLI).

1. **Test** your RCS messaging with registered test devices. No carrier approval is required for testing.

1. **Submit a country launch** registration for each country where you want to send production RCS messages.

1. **Partially approved**: at least one carrier has approved your agent. You can start sending to recipients on approved carriers.

1. **Fully approved**: all carriers in the country have approved your agent. Full reach in that country.

One AWS RCS Agent maps to one testing agent (an RCS for Business ID) plus multiple country launch agents (one RCS for Business ID per country). When you create an AWS RCS Agent in the console, the workflow immediately guides you to create a testing agent. The testing agent's brand configuration is then used to pre-populate country launch registration forms, reducing duplicative data entry.

**Topics**
+ [Understanding the AWS RCS Agent](#rcs-agents-concept)
+ [Understanding the two-level identity model](#rcs-agents-identity-model)
+ [Creating an AWS RCS Agent](#rcs-agents-create)
+ [Updating an AWS RCS Agent](#rcs-agents-update)
+ [Viewing AWS RCS Agents](#rcs-agents-view)
+ [Reviewing your testing agent](#rcs-agents-review-test-agent)
+ [Viewing country launch status](#rcs-agents-country-launch-status)
+ [Deleting an AWS RCS Agent](#rcs-agents-delete)

## Understanding the AWS RCS Agent
<a name="rcs-agents-concept"></a>

The AWS RCS Agent is distinct from the RCS for Business IDs that it manages. The following table summarizes the differences:


**AWS RCS Agent compared to RCS for Business ID**  

| Attribute | AWS RCS Agent | RCS for Business ID | 
| --- | --- | --- | 
| Managed by | You, through AWS End User Messaging console or API | AWS End User Messaging, during the registration process | 
| Scope | One per brand or per use case | One per country launch, plus one testing agent | 
| Configuration | Friendly name, deletion protection, opt-out list, tags, keywords, two-way messaging destination | Brand assets and other settings defined during registration | 
| Identifier | rcs-a1b2c3d4 format | Managed internally by the RCS infrastructure provider | 

### Agent ID and ARN
<a name="rcs-agents-id-format"></a>

Each AWS RCS Agent has a unique identifier in the format `rcs-a1b2c3d4` (the prefix `rcs-` followed by a hexadecimal string). You use this ID when calling API operations such as `UpdateRcsAgent` and `DeleteRcsAgent`.

Each AWS RCS Agent also has an AWS resource ARN in the following format:

```
arn:aws:sms-voice:{{region}}:{{account-id}}:rcs-agent/{{rcs-agent-id}}
```

You can use the ARN when specifying the AWS RCS Agent as an origination identity in the `SendTextMessage` API or when adding the agent to a phone pool.

### Lifecycle states
<a name="rcs-agents-lifecycle"></a>

An AWS RCS Agent transitions through the following lifecycle states:

**CREATED**  
The AWS RCS Agent resource has been created in AWS End User Messaging, but no registration has been submitted yet. You can update brand assets and configuration in this state.

**PENDING**  
A registration has been submitted and is awaiting processing. The agent is not yet available for sending messages.

**TESTING**  
The testing registration has been approved. The agent has a testing agent (RCS for Business ID) and can send messages to registered test devices. No country launch registrations have been completed.

**PARTIAL**  
At least one country launch registration has been completed, but not all submitted country launches are active. The agent can send messages in countries where it has been approved, but only to recipients on the specific carrier(s) that have approved the agent. The `CountryStatus` for a country moves to PARTIAL as soon as at least one carrier in that country is active.

**ACTIVE**  
All submitted country launch registrations are complete and active. The agent is fully operational in all registered countries. Note that an ACTIVE agent can return to PARTIAL status when a new country launch registration is submitted, because the new country is not yet approved.

**DELETED**  
The AWS RCS Agent has been deleted. All associated RCS for Business IDs (testing and country launch agents) are deactivated. This action cannot be undone.

## Understanding the two-level identity model
<a name="rcs-agents-identity-model"></a>

RCS in AWS End User Messaging uses a two-level identity model: the **AWS RCS Agent** and one or more **RCS for Business IDs**.

**AWS RCS Agent**  
The AWS RCS Agent is the top-level resource that you create and manage in AWS End User Messaging. It serves as the unified resource that binds together your testing agent and country launch agents. Keywords and two-way messaging configuration are defined on the AWS RCS Agent. Brand assets are defined on each registration. Each AWS RCS Agent has a unique identifier in the format `rcs-a1b2c3d4` and an AWS resource ARN. Think of the AWS RCS Agent as the unified identity for your brand across all countries where you launch RCS.

**RCS for Business ID**  
An RCS for Business ID is the per-country agent identity that is created with the RCS infrastructure provider during the registration process. Each country launch creates a separate RCS for Business ID under your AWS RCS Agent. You don't manage RCS for Business IDs directly. AWS End User Messaging handles the creation and lifecycle as part of the registration process.

One AWS RCS Agent can have the following RCS for Business IDs:
+ **One testing agent** — An RCS for Business ID created during the testing registration phase. The testing agent works with registered test devices and allows you to validate your RCS integration before launching in production. Testing messages are charged at standard rates.
+ **Multiple country launch agents** — Each country where you launch RCS creates a separate RCS for Business ID. For example, if you launch in multiple countries, your AWS RCS Agent has one country launch agent per country in addition to the testing agent.

The following diagram shows the relationship between these identities:

```
AWS RCS Agent (rcs-a1b2c3d4)
├── Testing agent (RCS for Business ID)
├── US country launch agent (RCS for Business ID)
├── ...additional country launch agents
└── [Country N] country launch agent (RCS for Business ID)
```

Keywords and two-way messaging destinations are configured on the AWS RCS Agent and apply to all associated RCS for Business IDs. Brand assets are specific to each registration (testing agent or country launch agent). The AWS RCS Agent also holds account-level settings such as the friendly name, deletion protection, and opt-out list.

## Creating an AWS RCS Agent
<a name="rcs-agents-create"></a>

You can create an AWS RCS Agent using the AWS End User Messaging console or the `CreateRcsAgent` API. When you create an agent, you provide a friendly name in the console (a console-only label stored as a tag, not visible through the API or displayed on recipients' phones) and configure optional settings such as deletion protection and opt-out list association. Brand assets are defined on the registration, not on the AWS RCS Agent itself.

### Brand asset requirements
<a name="rcs-agents-create-brand-assets"></a>

Your brand assets are displayed to recipients alongside your RCS messages. Brand assets are submitted as part of the testing registration, which the console presents as a continuation of the agent creation workflow. The following assets are required when creating an AWS RCS Agent:

**Logo**  
A square image that represents your brand. The logo appears in the messaging app alongside your messages.  
+ Dimensions: 224 × 224 pixels
+ Format: PNG with transparency
+ Maximum file size: 50 KB

**Banner image**  
A wide image that appears at the top of your agent's profile in the messaging app. The banner image is only displayed on Android devices.  
+ Dimensions: 1440 × 448 pixels
+ Format: PNG or JPEG
+ Maximum file size: 200 KB

**Brand color**  
A hex color code (for example, `#1A73E8`) used as an accent color in the messaging app. The color must have a minimum contrast ratio of 4.5:1 against a white background to meet accessibility requirements. If the contrast ratio is not set properly, your agent may not be approved.

**Important**  
Brand assets have limitations on changes after the agent is created. Some brand assets cannot be modified once the agent has been submitted for registration. Prepare your final brand assets before creating your AWS RCS Agent.

------
#### [ Console ]

The AWS End User Messaging console presents AWS RCS Agent creation and testing registration as a single guided workflow. For step-by-step console instructions, see [Step 1: Create your AWS RCS Agent and submit a testing registration](rcs-getting-started.md#rcs-getting-started-create-agent).

------
#### [ AWS CLI ]

Use the `create-rcs-agent` command to create an AWS RCS Agent. Brand assets (display name, description, logo, banner, and brand color) are not parameters of this command. They are submitted as registration fields when you create a testing registration.

```
aws pinpoint-sms-voice-v2 create-rcs-agent \
    --deletion-protection-enabled
```

The following optional parameters are available:
+ `--deletion-protection-enabled` — Prevents the agent from being deleted until deletion protection is disabled.
+ `--opt-out-list-name` — Associates an existing opt-out list with the agent.
+ `--tags` — Key-value pairs to organize and identify your AWS RCS Agent.

------

## Updating an AWS RCS Agent
<a name="rcs-agents-update"></a>

Use the `UpdateRcsAgent` API to modify the settings of an existing AWS RCS Agent. You can update the following settings:
+ **Deletion protection** — Enable or disable deletion protection for the agent.
+ **Opt-out list** — Associate or disassociate an opt-out list with the agent.
+ **Two-way messaging destination** — Configure the Amazon SNS topic and IAM role where inbound messages are delivered. Two-way messaging is always enabled for RCS. Customers are charged for all inbound RCS messages at standard rates. This setting controls where inbound messages are delivered, not whether they are received.

**Note**  
Changes to your AWS RCS Agent settings through the API are available immediately. However, updates to brand assets (registration fields such as logo, banner, and display name) are reviewed by the RCS infrastructure provider and may take time to appear on recipients' devices. To verify that your API changes have been applied, use the `DescribeRcsAgents` API to confirm the current agent configuration in AWS End User Messaging.

## Viewing AWS RCS Agents
<a name="rcs-agents-view"></a>

You can view your AWS RCS Agents using the AWS End User Messaging console or the `DescribeRcsAgents` API.

------
#### [ Console ]

To view your AWS RCS Agents in the console, navigate to the **RCS agents** page under **Configurations** in the navigation pane. The list page displays all AWS RCS Agents in your account, including their current lifecycle state, agent ID, and display name.

Choose an agent to view its details, including brand assets, configuration settings, and associated registrations.

------
#### [ AWS CLI ]

Use the `describe-rcs-agents` command to list all AWS RCS Agents in your account:

```
aws pinpoint-sms-voice-v2 describe-rcs-agents
```

To retrieve details for a specific agent, use the `--rcs-agent-ids` parameter:

```
aws pinpoint-sms-voice-v2 describe-rcs-agents \
    --rcs-agent-ids rcs-a1b2c3d4
```

------

## Reviewing your testing agent
<a name="rcs-agents-review-test-agent"></a>

Before submitting a country launch registration, review your testing agent configuration to ensure your brand assets, keywords, and messaging settings are correct. The testing agent serves as the template for country launch registrations, so any issues should be resolved before proceeding.

To review your testing agent, navigate to your AWS RCS Agent in the AWS End User Messaging console and choose the **Registrations** tab. The testing registration shows your current brand configuration, including the logo, banner image, brand color, and display name as they appear on recipients' devices.

You can also use the `DescribeRegistrationFieldValues` API to retrieve the current field values for your testing registration programmatically.

## Viewing country launch status
<a name="rcs-agents-country-launch-status"></a>

After you submit a country launch registration for your AWS RCS Agent, you can track the approval status for each carrier in that country.

------
#### [ Console ]

To view the country launch status in the console, navigate to the details page for your AWS RCS Agent and choose the **Country launch status** tab. This tab displays the approval status for each carrier in each country where you have submitted a launch registration.

------
#### [ AWS CLI ]

Use the `describe-rcs-agent-country-launch-status` command to retrieve the per-carrier launch status:

```
aws pinpoint-sms-voice-v2 describe-rcs-agent-country-launch-status \
    --rcs-agent-id rcs-a1b2c3d4
```

The response includes the approval status for each carrier in each country where you have submitted a launch registration.

------

Each carrier independently reviews and approves your agent. Your AWS RCS Agent can send messages in a country as soon as at least one carrier in that country has approved the agent. You do not need to wait for all carriers to approve before you can start sending RCS messages. As additional carriers approve your agent, your reach in that country increases.

**Note**  
You can request additional country launches from the country launch status screen. Each new country launch creates a separate registration and goes through its own carrier approval process.

## Deleting an AWS RCS Agent
<a name="rcs-agents-delete"></a>

Use the `DeleteRcsAgent` API to permanently delete an AWS RCS Agent. When you delete an agent, all associated RCS for Business IDs (including the testing agent and all country launch agents) are deactivated.

**Warning**  
Deleting an AWS RCS Agent is permanent and cannot be undone. All registrations, country launches, and testing configurations associated with the agent are lost.

Before you can delete an AWS RCS Agent, you must first delete all associated registrations (both testing and country launch registrations), and then disable deletion protection. If deletion protection is enabled, the `DeleteRcsAgent` API returns an error. To disable deletion protection, use the `UpdateRcsAgent` API with deletion protection set to `false`.

**To delete an AWS RCS Agent**

1. If deletion protection is enabled, disable it by calling the `UpdateRcsAgent` API with deletion protection set to `false`.

1. Call the `DeleteRcsAgent` API with the agent ID or ARN of the AWS RCS Agent that you want to delete.

1. Verify that the agent has been deleted by calling the `DescribeRcsAgents` API. The agent should no longer appear in the results, or its status should be DELETED.