# Tools to diagnose application integrations

The tools used to diagnose application integrations in the AWS Diagnostic Tools service cover
Amazon Pinpoint, Amazon Polly, and Amazon Simple Workflow Service. With Diagnostic Tools, AWS Partners can monitor, troubleshoot,
and optimize their customer's AWS applications.

## Amazon Pinpoint tools

Amazon Pinpoint diagnostic tools are employed to monitor user engagement and interactions within
applications. This encompasses tracking user behavior, sending targeted messages, and
evaluating the effectiveness of campaigns.

These tools aid in troubleshooting issues related to user engagement and message delivery,
including:

- Diagnosing message delivery problems such as bounces or complaints.
- Investigating low user engagement by analyzing user interaction data.
- Optimizing message campaigns based on open rates, click-through rates, and conversion
  rates.

**Amazon Pinpoint tools**

- Amazon Pinpoint Campaign Details
- Amazon Pinpoint Segment Details
- Amazon Pinpoint Journey Details
- Amazon Pinpoint Journey Run Details
- Amazon Pinpoint Dashboard

## Amazon Polly tools

The Amazon Polly tool helps partners convert text into speech and customize the speech
output.

This tool helps partners troubleshoot text-to-speech conversion issues that may originate
from Amazon Polly including:

- Identifying errors or mispronunciations in the generated speech.
- Analyzing usage patterns to ensure efficient utilization of Polly resources.
- Optimizing voice selection and speech markup to enhance speech quality.

**Amazon Polly tools**

- Amazon Polly

## Amazon EventBridge tools

Amazon EventBridge Bridge is a serverless event bus service that enables software applications to communicate with each other using events. Offered by AWS, this service is designed to simplify the architecture of event-driven applications by providing a robust and scalable infrastructure for routing events between software components. Amazon EventBridge tools help troubleshoot EventBridge Rules:

- Quickly identify and list EventBridge Rules to confirm the presence and proper configuration of the correct rules for your events. This proves particularly valuable in complex systems with many Rules.
- Inspect event patterns within EventBridge Rules to pinpoint precisely which events a rule is monitoring. This helps diagnose issues, especially if a service isn't reacting as expected, potentially due to a mismatch in the event pattern and emitted events.
- Verify the targets of EventBridge Rules to confirm that events are correctly directed to the intended AWS service or resource. This step is crucial as misconfigured targets often disrupt event-driven architectures.
- Understand the details of event data transformation within EventBridge Rules for effective debugging. Missteps in transformation logic are a common source of unexpected application behavior.
- Ensure the proper permissions are associated with EventBridge Rules. Correct permissions are essential for the rule's operation; lacking them can result in untriggered rules or non-responsive targets.

**Amazon EventBridge tools**

- EventBridge Rule Details
- EventBridge Lookup

## Amazon Simple Workflow Service tools

Amazon Simple Workflow Service tools help diagnose issues related to workflow orchestration and task
execution, including:

- Detecting and resolving workflow execution failures or timeouts.
- Monitoring the progress of workflow executions and identifying bottlenecks.
- Debugging task failures by examining task history and input/output data.

**Amazon Simple Workflow Service (Amazon SWF) tools**

- Amazon Simple Workflow Service Activities
- Amazon Simple Workflow Service Dashboard
- Amazon Simple Workflow Service Domains
- Amazon Simple Workflow Service Execution Details
- Amazon Simple Workflow Service Execution History
- Amazon Simple Workflow Service List Executions
- Amazon Simple Workflow Service Types Lookup

## Benefits for AWS Partners

By using AWS Diagnostic Tools your partners can handle common application integration related
troubleshooting scenarios that may include:

- _Message delivery issues:_ Troubleshooting message delivery problems
  in Amazon Pinpoint, investigating delivery logs, and ensuring message accuracy.
- _User engagement optimization:_ Analyzing user engagement metrics in
  Amazon Pinpoint to improve user interactions and campaign effectiveness.
- _Voice quality and pronunciation:_ Diagnosing voice quality issues and
  mispronunciations in Amazon Polly.
- _Resource utilization:_ Monitoring resource utilization in Amazon Polly and
  Amazon SWF to optimize resource allocation.
- _Workflow execution failures:_ Resolving workflow execution failures
  and timeouts in Amazon SWF.
- _Performance optimization:_ Analyzing Amazon SWF workflows for performance
  bottlenecks and delays.
- _Task retries:_ Handling task retries in Amazon SWF to ensure smooth
  workflow execution.
