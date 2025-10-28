# Troubleshoot call disconnects by using

DisconnectDetails in the contact record

This topic explains how to leverage the Amazon Connect [DisconnectDetails](ctr-data-model.md#ctr-disconnectdetails "ctr-data-model.md#ctr-disconnectdetails") in the contact record to troubleshoot call disconnect
issues.

## Step 1: Observe the issue

- No audio from agent:
  - Observation: If the customer cannot hear the agent, generally,
    leading to the customer disconnecting the call.
  - Potential causes: This can be caused by a combination of
    network/hardware configurations.

- No audio from agent and customer:
  - Observation: If the customer cannot hear the agent, and the agent
    cannot hear the customer.
  - Potential causes: This can be caused by network connectivity
    issues.

## Step 2: Analyze the impact

Use the [DisconnectDetails](ctr-data-model.md#ctr-disconnectdetails "ctr-data-model.md#ctr-disconnectdetails") data
together with other fields on the contact record such as [agent hierarchies](ctr-data-model.md#ctr-AgentHierarchyGroups "ctr-data-model.md#ctr-AgentHierarchyGroups") and [device info](ctr-data-model.md#ctr-deviceinfo "ctr-data-model.md#ctr-deviceinfo") to identify which users are affected
and to spot any trends. Using this information, answer the following questions to
understand overall impact: 

- What percentage of agents are impacted?
  - Scenario 1:  If only a single agent seems to be facing the
    problem, it could be related to agent
    workstation/hardware/system/network configuration of the agent.
  - Scenario 2: If multiple agents in the same hierarchy <(ex:
    same geographical location, or office) audio quality issues, this
    could be a result of a local network issue (modem/ISP/Router/LAN
    connections) or recent software upgrades to these
    agent workstations.
  - Scenario 3: Multiple agents (working remote and/or at office
    location) may be facing the issue. Check the browser/system
    configurations for any updates along with any network changes that
    may have occurred at the organizational level.

- What percentage of calls are affected in a given day and out of how many
  calls?
- Is the issue observed on incoming calls, outgoing calls or both?
- Is there any call forwarding entity from which the calls are being
  forwarded to Amazon Connect? If so, does the call disconnect issue occur in case of
  direct dials to Amazon Connect?

## Step 3: Gather information

To troubleshoot call disconnect issues, start by collecting the following
information:

- The Amazon Connect instance ARN: For instructions, see [Find your Amazon Connect instance ID or ARN](find-instance-arn.md "find-instance-arn.md").
- Contact ID of the affected call you're going to investigate.
- View the contact records for the contact ID. For instructions, see [View a contact record in the Amazon Connect admin website](sample-ctr.md "sample-ctr.md").
- The following additional resources will also help you identify the source
  of the issue:
  - Call recordings: Amazon Connect call recordings are helpful in
    understanding deeper insights regarding call quality.
    - The agent audio is stored in the right channel.
    - All incoming audio, including the customer and anyone
      conferenced in, is stored in the left channel.

  - [Download and review Amazon Connect Contact Control Panel
    (CCP) logs](download-ccp-logs.md "download-ccp-logs.md"): The logs help provide
    insights for a given call handled by an agent.
  - [Endpoint Test Utility](check-connectivity-tool.md "check-connectivity-tool.md") results: This browser based tool helps you validate agent
    workstation settings in a JSON format.

## Step 4: Use

`DisconnectDetails`

When you're viewing the contact record for the affected contact, go to the [DisconnectDetails](ctr-data-model.md#ctr-disconnectdetails "ctr-data-model.md#ctr-disconnectdetails") section. It provides
insights into a call getting disconnected ungracefully due to potential media
connection or device issues.

For calls with `PotentialDisconnectIssue`, the field will be populated
with the detected reason of `AGENT_CONNECTIVITY_ISSUE` or
`AGENT_DEVICE_ISSUE`.

- `AGENT_CONNECTIVITY_ISSUE`: This suggests that there is an issue
  with the network connectivity between agent workstation and Amazon Connect. It is
  causing the call to disconnect.  For additional troubleshooting steps, see
  [Troubleshoot your network](network-ts.md "network-ts.md").
- `AGENT_DEVICE_ISSUE`: This suggests that there is an issue with
  the agent's workstation or headset hampering two-way communication resulting
  in one of the parties to hang up. For additional troubleshooting steps, see
  [Troubleshoot an agent's workstation](agent-ts.md "agent-ts.md").
