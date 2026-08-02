# Connecting Dynatrace

## Built-in, 2-way integration

Currently, AWS DevOps Agent supports Dynatrace users with a built-in, 2-way integration enabling the following:

- **Topology resource mapping** - AWS DevOps Agent will augment your DevOps Agent Space Topology with entities and relationships available to it from your Dynatrace environment.
- **Automated Investigation triggering** - Dynatrace Workflows can be configured to trigger incident resolution Investigations from Dynatrace Problems.
- **Telemetry introspection** - AWS DevOps Agent can introspect Dynatrace telemetry as it investigates an issue via the AWS DevOps Agent-hosted Dynatrace MCP server.
- **Status updates** - AWS DevOps Agent will publish key investigation findings, root cause analyses, and generated mitigation plans to the Dynatrace user interface.

## Prerequisites

The AWS DevOps Agent integration with Dynatrace requires **Dynatrace SaaS**. The integration depends on Dynatrace platform features (Workflows, AppEngine apps including the SRE Agents app, and OAuth clients) that are only available in Dynatrace SaaS environments.

**Dynatrace Managed (on-premises) is not supported**, and Dynatrace has no plans to bring these platform features to Managed. If you are running Dynatrace Managed, you will need to upgrade to Dynatrace SaaS before connecting it to AWS DevOps Agent. See [Upgrading from Dynatrace Managed to SaaS](https://www.dynatrace.com/platform/saas-upgrade/ "https://www.dynatrace.com/platform/saas-upgrade/").

## Onboarding

### Onboarding Process

Onboarding your Dynatrace observability system involves three stages:

1. **Connect** - Establish connection to Dynatrace by configuring account access credentials, with all the environments you may need
2. **Enable** - Activate Dynatrace in specific Agent spaces with specific Dynatrace environments
3. **Configure your Dynatrace environment** - use the Dynatrace SRE Agents app to complete the connection in 2 clicks

### Step 1: Connect

Establish connection to your Dynatrace environment

#### Configuration

1. Go to the **Capability Providers** page (accessible from the side navigation)
2. Find **Dynatrace** in the **Available** providers section under **Telemetry** and choose **Register**
3. **Create OAuth client in Dynatrace, with the detailed permissions.**

   1. See [Dynatrace documentation](https://docs.dynatrace.com/docs/manage/identity-access-management/access-tokens-and-oauth-clients/oauth-clients#create-an-oauth2-client "https://docs.dynatrace.com/docs/manage/identity-access-management/access-tokens-and-oauth-clients/oauth-clients#create-an-oauth2-client")
   2. When ready press next
   3. You can connect multiple Dynatrace environments and later scope to specific ones for each DevOps Agent Space you may have.

4. Enter your Dynatrace details from the OAuth client setup:

   - **Client Name**
   - **Client ID**
   - **Client Secret**
   - **Account URN**

5. Choose Next
6. Review and add

Each registration connects to one Dynatrace OAuth client. To connect additional Dynatrace accounts, repeat this process for each one.

### Step 2: Enable

Activate Dynatrace in a specific Agent space and configure appropriate scoping

#### Configuration

1. From the agent spaces page, select an agent space and press view details
2. Select the Capabilities tab
3. Locate the Telemetry section, Press Add
4. Dynatrace appears with a Registered status. Choose **Add** to add the registration you want to your Agent Space.
5. Dynatrace Environment ID - Provide the Dynatrace environment ID you would like to associate with this DevOps agent space.
6. Enter one or more Dynatrace Entity IDs - these help DevOps agent discover your most important resources, examples might be services or applications. **If you are unsure you can press remove.**
7. Review and press Save
8. Copy the Webhook URL and Webhook Secret. You will use these in the Dynatrace **SRE Agents** app to complete the connection. See the [Getting Started section](https://www.dynatrace.com/hub/detail/community-cloudsreagents/ "https://www.dynatrace.com/hub/detail/community-cloudsreagents/") for details.

A single Agent Space can use more than one Dynatrace registration, and more than one environment from each. To add another registration or environment, repeat these steps.

### Step 3: Configure your Dynatrace environment

To complete your Dynatrace setup, use the Dynatrace **SRE Agents** app to configure the Dynatrace side of the integration in 2 clicks — no manual workflow setup is needed. For details, see the [Getting Started section](https://www.dynatrace.com/hub/detail/community-cloudsreagents/ "https://www.dynatrace.com/hub/detail/community-cloudsreagents/").

#### Supported Event Schemas

AWS DevOps Agent supports two types of events from Dynatrace using webhooks. The supported event schemas are documented below:

##### Incident Event

Incident events are used to trigger an investigation. The event schema is:

```
{
    "event.id": string;
    "event.status": "ACTIVE" | "CLOSED";
    "event.status_transition": string;
    "event.description": string;
    "event.name": string;
    "event.category": "AVAILABILITY" | "ERROR" | "SLOWDOWN" | "RESOURCE_CONTENTION" | "CUSTOM_ALERT" | "MONITORING_UNAVAILABLE" | "INFO";
    "event.start"?: string;
    "affected_entity_ids"?: string[];
}
```

##### Mitigation Event

Mitigation events are used to trigger generating a mitigation report for the investigation on next steps. The event schema is:

```
{
    "task_id": string;
    "task_version": number;
    "event.type": "mitigation_request";
}
```

## Removal

The telemetry source is connected at two levels at the agent space level and at account level. To completely remove it you must first remove from all agent spaces where it is used and then it can be unregistered.

### Step 1: Remove from agent space

1. From the agent spaces page, select an agent space and press view details
2. Select the Capabilities tab
3. Scroll down to the Telemetry section
4. Select Dynatrace
5. Press remove

### Step 2: Deregister from account

1. Go to the **Capability Providers** page (accessible from the side navigation)
2. Scroll to the **Currently registered** section.
3. Check the agent space count is zero (if not repeat Step 1 above in your other agent spaces)
4. Select Dynatrace, then choose **Deregister** from the **Actions** menu.
