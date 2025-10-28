# Troubleshoot audio quality issues by using

`QualityMetrics` in the contact record

###### Important

The topics and content in this section are for IT administrators who have experience
with investigating network and telephony issues.

You also need to be familiar with how to access data in an Amazon Connect contact
record.

## Where to find QualityMetrics

Amazon Connect provides QualityMetrics in the contact record for each connected call.

QualityMetrics is part of the contact object that you get as a response when you call
the [DescribeContact](../APIReference/API_DescribeContact.md "../APIReference/API_DescribeContact.md")
API. The following snippet from the `DescribeContact` response shows what
it looks like:

```
 "QualityMetrics": {
         "Agent": {
            "Audio": {
               "PotentialQualityIssues": [ "string" ],
               "QualityScore": number
            }
         },
         "Customer": {
            "Audio": {
               "PotentialQualityIssues": [ "string" ],
               "QualityScore": number
            }
         }
      },
```

QualityMetrics is also a sub-section of the [QualityMetrics](ctr-data-model.md#ctr-qualitymetrics "ctr-data-model.md#ctr-qualitymetrics") object that you receive through Kinesis CTR
events.

QualityMetrics is not available by using the Amazon Connect admin website to view the contact record.

QualityMetrics is not part of EventBridge events.

## Symptoms of call quality issues

Following is a list of common symptoms that indicate call quality issues on a
participant media connection. You can observe these symptoms on a Amazon Connect call recording
on the participant channel.

- Choppy/broken audio
  - Observation: The audio stream gets interrupted and sounds choppy or
    broken on the media connection as heard by the listener on the other
    end.
  - Potential causes: Potentially caused by packet loss due to poor
    network connectivity leading to a participant sounding choppy or broken
    to the other party.

- Delayed audio
  - Observation: Participant experiences a delayed audio from the other
    side. An effect of delayed audio is consistent overlapping in
    conversation between the caller and the agent.
  - Potential causes: This can be caused due to constrained network
    bandwidth/hardware/workstation congestion.

- Echo
  - Observation: Echo is when agent hears their own voice repeated back to
    them with a delay.
  - Potential causes: This is often due to audio feedback between the
    microphone and speaker.

- Background noise
  - Observation: Extraneous background noise like fans, typing, or call
    center noise can make it difficult to hear the caller clearly.

- Distorted audio
  - Observation: Distorted, garbled, or robotic-sounding audio heard by
    one party coming from the other end.
  - Potential causes: This is typically a sign of a bandwidth issue or
    faulty hardware.

## Analyze the impact on your agents and

calls

We recommend using [QualityMetrics](ctr-data-model.md#ctr-qualitymetrics "ctr-data-model.md#ctr-qualitymetrics") data together with other fields on the contact
record—such as [AgentHierarchyGroup](ctr-data-model.md#ctr-AgentHierarchyGroups "ctr-data-model.md#ctr-AgentHierarchyGroups") and [DeviceInfo](ctr-data-model.md#ctr-deviceinfo "ctr-data-model.md#ctr-deviceinfo")—to identify the impacted population and
spot any trends. Use this information to answer the following questions to understand
overall impact:

- What percentage of agents or calls are impacted?
  - Scenario 1: If only 1 agent is encountering the problem, it could be
    related to agent workstation including operating system and
    browser/network configuration of the agent.
  - Scenario 2: If multiple agents in the same hierarchy (for example, the
    same geographical location or office) experience audio quality issues,
    this could be a result of a local network issue (modem/ISP/Router/LAN
    connections) or recent software upgrades to the machines of agents.
  - Scenario 3: Multiple agents (working remote and/or at office location)
    may be experiencing the issue. Check the browser/system configurations
    for any updates along with any network changes that may have occurred at
    the organizational level.

- What percentage of calls are affected in a given day and out of how many
  calls?
- Is the issue observed on incoming calls, outgoing calls or both?
- Is an entity forwarding calls to Amazon Connect? If so, does the audio quality issue
  occur in case of direct dials to Amazon Connect without the call quality issue.

## Use `QualityMetrics`

Amazon Connect provides [QualityMetrics](ctr-data-model.md#ctr-qualitymetrics "ctr-data-model.md#ctr-qualitymetrics")
in the contact record for each connected call. Use the metrics help you to identify the
source of the issue.

`QualityMetrics` contain the following information:

- **QualityScore**: An estimate of overall audio
  quality using a numerical value.
  - Minimum value: 1.00 (indicates poor quality)
  - Maximum value: 5.00 (indicates high quality)

- **PotentialQualityIssues**: For calls with
  potential issues, `PotentialQualityIssues` is populated with a list
  of detected reasons which include `HighPacketLoss`,
  `HighRoundTripTime`, or `HighJitterBuffer`. An empty
  list suggests that no audio quality issues were detected.

The following list explains the potential values for
`PotentialQualityIssues` and suggests causes to guide your
investigation.

- `HighPacketLoss`: When this value occurs for
  `PotentialQualityIssues`, it suggests that there is packet loss
  observed on the outbound audio (egress) stream for the participant.
  - Causes:
    - This can occur in the path the packets traverse the network
      between the participant and the Amazon Connect endpoint which could be
      due to a bad/poor network, congestion in network, constrained
      network bandwidth.
    - It can also occur when there could be other applications on
      the participant's system that may be causing network bandwidth
      starvation.

- `HighJitterBuffer`: This is the time delay introduced by a buffer
  built-in the browser to correct the order of audio packets after network
  traversal. Jitter buffer plays a major role in ensuring that the packets
  received over network at a device are aligned appropriately to provide the audio
  without distortion.
  - Causes:
    - If a congestion (network and/or hardware) occurs at the
      participant's end, the `JitterBuffer` increases
      causing audio delays/distorted or choppy audio.
    - Jitter buffer is responsible for delaying the processing media
      packets just enough to smooth out delivery times but high jitter
      buffer can cause background noise or audio quality issue.
    - If jitter buffer is more than 30 ms or changing very
      frequently then it means network congestion or low network
      bandwidth of router. High jitter can also be caused due to
      hardware issues of the devices involved.

- `HighRoundTripTime`: This is the time it takes for a packet to
  travel through an IP network, from a sending endpoint to a receiving endpoint
  and back, not including the processing time at its destination. High RTT results
  in callers experiencing noticeable delays (speech overlap) on the call.
  RoundTripTime (RTT) is the estimated network round trip time between the
  participant's device and Amazon Connect endpoint.
  - Causes:
    - The most common cause of high round trip time is a
      low-bandwidth or constrained network.
    - You may also experience high round-trip time if a certain
      software program is causing a spike in round-trip time. In the
      past, some of our customers have reported VPN applications being
      cause of the issue.
    - If the agent's physical location is distant from the AWS
      Region of the Amazon Connect instance, it results in an increase to
      RoundTripTime adding latency.
    - Routing audio through a virtualized desktop (as opposed to
      redirecting the WebRTC session directly to agent workstation)
      could also introduce high round trip time.

## Next steps

After you have identified whether the issue is `HighPacketLoss`,
`HighJitterBuffer`, `HighRoundTripTime`, use the information
to troubleshoot the network or the agent's device. See the following topics:

- [Troubleshoot your network](network-ts.md "network-ts.md")
- [Troubleshoot an agent's workstation](agent-ts.md "agent-ts.md")
