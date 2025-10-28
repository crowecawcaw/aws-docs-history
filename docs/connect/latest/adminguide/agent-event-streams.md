# Amazon Connect agent event streams

Amazon Connect agent event streams are Amazon Kinesis data streams that provide you with near real-time
reporting of agent activity within your Amazon Connect instance. The events published to the stream
include these CCP events:

- Agent login
- Agent logout
- Agent connects with a contact
- Agent status change, such as to Available to handle contacts, or on Break or at
  Training.
  You can use the agent event streams to create dashboards that display agent information
  and events, integrate streams into workforce management (WFM) solutions, and configure
  alerting tools to trigger custom notifications of specific agent activity. Agent event
  streams help you manage agent staffing and efficiency.

###### Contents

- [Enable agent event streams to report agent
  activity in Amazon Connect](agent-event-streams-enable.md "agent-event-streams-enable.md")
- [Sample agent event stream in Amazon Connect](sample-agent-event-stream.md "sample-agent-event-stream.md")
- [Determine the contact center agent's ACW (After
  Contact Work) time](determine-acw-time.md "determine-acw-time.md")
- [Agent event streams data model in
  Amazon Connect](agent-event-stream-model.md "agent-event-stream-model.md")
