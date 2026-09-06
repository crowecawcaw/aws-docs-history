

# Troubleshoot call disconnects by using DisconnectDetails in the contact record
<a name="troubleshoot-call-disconnects"></a>

## Step 1: Observe the issue
<a name="observations-disconnect"></a>
+ No audio from agent:
  + Observation: If the customer cannot hear the agent, the customer generally disconnects the call.
  + Potential causes: A combination of network and hardware configurations can cause this issue.
+ No audio from agent and customer:
  + Observation: If the customer cannot hear the agent, and the agent cannot hear the customer.
  + Potential causes: Network connectivity issues.

## Step 2: Analyze the impact
<a name="analyze-impact"></a>

Use the [DisconnectDetails](ctr-data-model.md#ctr-disconnectdetails) data together with other contact record fields, such as [agent hierarchies](ctr-data-model.md#ctr-AgentHierarchyGroups) and [device info](ctr-data-model.md#ctr-deviceinfo). This helps you identify which users are affected and spot trends. To understand the overall impact, answer the following questions:
+ What percentage of agents are impacted?
  + Scenario 1:  If only a single agent seems to be facing the problem, it might be related to agent workstation, hardware, system, or network configuration of the agent.  
  + Scenario 2: If multiple agents in the same hierarchy (for example, same geographical location, or office) experience audio quality issues, this might be the result of a local network issue (modem, internet service provider (ISP), router, or local area network (LAN) connections) or recent software upgrades to these agent workstations.
  + Scenario 3: Multiple agents (working remotely or at office location) might experience this issue. Check the browser or system configurations for any updates along with any network changes that might have occurred at the organizational level.
+ What percentage of calls are affected in a given day and out of how many calls?
+ Is the issue observed on incoming calls, outgoing calls or both?
+ Is there any call forwarding entity from which the calls are being forwarded to Connect Customer? If so, does the call disconnect issue occur in case of direct dials to Connect Customer?

## Step 3: Gather information
<a name="gatherinfo-disconnect"></a>

To troubleshoot call disconnect issues, start by collecting the following information:
+ The Connect Customer instance ARN: For instructions, see [Find your Connect Customer instance ID or ARN](find-instance-arn.md).
+ Contact ID of the affected call you're going to investigate.
+ View the contact records for the contact ID. For instructions, see [View a contact record in the Connect Customer admin website](sample-ctr.md).
+ The following additional resources can also help you identify the source of the issue:
  + Call recordings: Connect Customer call recordings are helpful in understanding deeper insights regarding call quality.
    + The agent audio is stored in the right channel.
    + All incoming audio, including the customer and anyone conferenced in, is stored in the left channel.
  + [Download and review Connect Customer Contact Control Panel (CCP) logs](download-ccp-logs.md): The logs help provide insights for a given call handled by an agent.
  + [Endpoint Test Utility ](check-connectivity-tool.md) results: This browser-based tool helps you validate agent workstation settings in a JSON format.

## Step 4: Use `DisconnectDetails`
<a name="use-disconnectdetails"></a>

When you're viewing the contact record for the affected contact, go to the [DisconnectDetails](ctr-data-model.md#ctr-disconnectdetails) section. It provides insights into calls that disconnect unexpectedly because of potential media connection or device issues.

For calls with `PotentialDisconnectIssue`, Connect Customer populates the field with the detected reason of `AGENT_CONNECTIVITY_ISSUE` or `AGENT_DEVICE_ISSUE`.
+  `AGENT_CONNECTIVITY_ISSUE`: A network connectivity issue between the agent workstation and Connect Customer is causing the call to disconnect. For additional troubleshooting steps, see [Troubleshoot your network](network-ts.md).
+  `AGENT_DEVICE_ISSUE`: A workstation or headset issue is preventing two-way audio, causing one party to disconnect. For additional troubleshooting steps, see [Troubleshoot an agent's workstation](agent-ts.md).