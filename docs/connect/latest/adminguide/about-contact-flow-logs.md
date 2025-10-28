# Use flow logs to track events in Amazon Connect

flows

Amazon Connect flow logs provide you with real-time details about events in your flows
as customers interact with them. You can also use flow logs to help debug your flows as you
are creating them. If needed, you can always [roll back](flow-version-control.md#rollback "flow-version-control.md#rollback") to a
previous version of a flow.

Following is an overview of logging for flows and bot interactions.

- **Flow logs stored in an CloudWatch group**.
  Use these logs for identifying bottlenecks in flow design, debugging flow issues in
  real-time, and analyzing customer journey patterns.

Flow logs help you track customers between different flows by including the ID of
the contact in each log entry. You can query the logs for the contact ID to trace
the customer interaction through each flow.

The CloudWatch group log is created automatically when [Enable flow logging](contact-flow-logs.md#enable-contact-flow-logs "contact-flow-logs.md#enable-contact-flow-logs") is selected for
your instance on the Amazon Connect console. However, to enable logging, you also need to add
a **Set logging behavior** block to your flow. For instructions,
see [Enable Amazon Connect flow logs in an Amazon CloudWatch log
group](contact-flow-logs.md "contact-flow-logs.md").

- **Automated interaction logs**. Use these logs to
  analyze the quality of conversations between customers and bots, understand common
  customer queries, and improve bot responses.

These logs are saved in an S3 bucket that is created when you [select](monitor-automated-interaction-logs.md "monitor-automated-interaction-logs.md") the following options
for your instance on the Amazon Connect console:

    + **Enable call recording** and create or select your S3
     bucket on the **Data storage** page. The automated
     interaction log is stored in the same S3 location as that of your call
     recording.
    + **Enable Automated Interaction Logs** on the
     **Flows** page. This option enables the logging of key
     interaction points such as flows, prompts, menus, and keypad selections.
     This automated log is available in your S3 storage and in the
     **Contact details** page on the Amazon Connect admin website.
    + **Enable Bot Analytics and Transcripts** in Amazon Connect on the
     **Flows** page. This option ensures the log includes
     the Amazon Lex bot transcript.

###### Contents

- [Storage for flow
  logs](contact-flow-logs-stored-in-cloudwatch.md "contact-flow-logs-stored-in-cloudwatch.md")
- [Enable flow logs](contact-flow-logs.md "contact-flow-logs.md")
- [Search flow logs](search-contact-flow-logs.md "search-contact-flow-logs.md")
- [Data in flow logs](contact-flow-log-data.md "contact-flow-log-data.md")
- [Track customers between multiple flows
  in your contact center](contact-flow-log-multiple-flows.md "contact-flow-log-multiple-flows.md")
- [Create alerts for events in your
  flow logs](contact-flow-log-alerts.md "contact-flow-log-alerts.md")
- [Monitor automated
  interactions (IVR)](monitor-automated-interaction-logs.md "monitor-automated-interaction-logs.md")
