# Methods to create an investigation

You can create investigations in the following ways:

- From within many AWS consoles. For example, you can start an investigation
  when viewing a CloudWatch metric or alarm in the CloudWatch console, or from a Lambda
  function's **Monitor** tab on its properties page.
- By following a prompt in chat with CloudWatch investigations. You can start by asking questions
  like "Why is my Lambda function slow today?" or "What's wrong with my
  database?"
- By configuring a CloudWatch alarm action to automatically start an investigation
  when the alarm goes into ALARM state.
  After you start an investigation with any of these methods, CloudWatch investigations scans your system to
  find telemetry that might be relevant to the situation, and also generates hypotheses
  based on what it finds. CloudWatch investigations surfaces both the telemetry data and the
  hypotheses. At any time after accepting a hypothesis, you can generate a
  comprehensive incident report that automatically captures the current investigation
  findings, timeline events, and recommended actions.
