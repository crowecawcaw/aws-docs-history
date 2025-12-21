# Connecting Dynatrace

## Built-in, 2-way integration

Currently, AWS DevOps Agent supports Dynatrace users with a built-in, 2-way integration enabling the following:

- **Topology resource mapping** - AWS DevOps Agent will augment your DevOps Agent Space Topology with entities and relationships available to it from your Dynatrace environment.
- **Automated Investigation triggering** - Dynatrace Workflows can be configured to trigger incident resolution Investigations from Dynatrace Problems.
- **Telemetry introspection** - AWS DevOps Agent can introspect Dynatrace telemetry as it investigates an issue via the AWS DevOps Agent-hosted Dynatrace MCP server.
- **Status updates** - AWS DevOps Agent will publish key investigation findings, root cause analyses, and generated mitigation plans to the Dynatrace user interface.

## Onboarding

### Onboarding Process

Onboarding your Dynatrace observability system involves three stages:

1. **Connect** - Establish connection to Dynatrace by configuring account access credentials, with all the environments you may need
2. **Enable** - Activate Dynatrace in specific Agent spaces with specific Dynatrace environments
3. **Configure your Dynatrace environment -** download the workflows and dashboard and import into Dynatrace, making a note of the webhooks details to trigger investigations in designated Agent spaces

### Step 1: Connect

Establish connection to your Dynatrace environment

#### Configuration

1. Open the hamburger menu and select Settings
2. Scroll to the Available - Telemetry section. Press Register next to Dynatrace
3. **Create OAuth client in Dynatrace, with the detailed permissions.**
   1. See [Dynatrace documentation](https://docs.dynatrace.com/docs/shortlink/aws-devops-agent "https://docs.dynatrace.com/docs/shortlink/aws-devops-agent")
   2. When ready press next
   3. You can connect multiple dynatrace environments and later scope to specific ones for each DevOps Agent Space you may have.

4. Enter your Dynatrace details from the OAuth client setup:
   1. **Client Name**
   2. **Client ID**
   3. **Client Secret**
   4. **Account URN**

5. Click Next
6. Review and add

### Step 2: Enable

Activate Dynatrace in a specific Agent space and configure appropriate scoping

#### Configuration

1. From the agent spaces page, select an agent space and press view details
2. Select the Capabilities tab
3. Locate the Telemetry section, Press Add
4. You will notice Dynatrace with ‘Registered’ status. Click on add to add this to your agent space
5. Dynatrace Environment ID - Provide the Dynatrace environment ID you would like to associate with this DevOps agent space.
6. Enter one or more Dynatrace Entity IDs - these help DevOps agent discover your most important resources, examples might be services or applications. **If you are unsure you can press remove.**
7. Review and press Save
8. Copy the Webhook URL and Webhook Secret and follow the instructions [[https://docs.dynatrace.com/docs/shortlink/aws-devops-agent](https://docs.dynatrace.com/docs/shortlink/aws-devops-agent "https://docs.dynatrace.com/docs/shortlink/aws-devops-agent")] to add this credentials to Dynatrace.

### Step 3: Configure your Dynatrace environment

To complete your Dynatrace set up you will need to perform certain setup steps in your Dynatrace environment. Follow the instructions here: [https://docs.dynatrace.com/docs/shortlink/aws-devops-agent](https://docs.dynatrace.com/docs/shortlink/aws-devops-agent "https://docs.dynatrace.com/docs/shortlink/aws-devops-agent")

## Removal

The telemetry source is connected at two levels at the agent space level and at account level. To completely remove it you must first remove from all agentspaces where it is used and then it can be unregistered.

### Step 1: Remove from agent space

1. From the agent spaces page, select an agent space and press view details
2. Select the Capabilities tab
3. Scroll down to the Telemetry section
4. Select Dynatrace
5. Press remove

### Step 2: Remove from agent space

1. Open the hamburger menu and select Settings
2. Scroll to the **Currently registered** section.
3. Check the agent space count is zero (if not repeat Step 1 above in your other agent spaces)
4. Press Deregister next to Dynatrace
