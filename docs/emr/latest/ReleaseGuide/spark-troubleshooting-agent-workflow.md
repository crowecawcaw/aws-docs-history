# Spark Troubleshooting Agent Workflow in Details

To initiate the troubleshooting process, you will need access to your failed Spark application identifiers running on supported platforms (EMR-EC2, EMR Serverless, AWS Glue, or Amazon SageMaker Data Notebooks). The application should have accessible logs, Spark History Server, and configuration details. Ensure you have the necessary permissions to access the platform resources and application metadata. Once these requirements are established, you can submit a prompt like the following to kick off the troubleshooting workflow:

```
Analyze my EMR step execution failure, EMR id <step-id> with cluster id <cluster-id>
```

At this point, the agent will orchestrate the troubleshooting using specialized tools. The workflow follows these steps:

1. **Feature Extraction and Context Building**: The agent automatically collects and analyzes telemetry data from your Spark application including History Server logs, configuration settings, and error traces. You'll see the tool gathering information about performance metrics, resource utilization patterns, and failure signatures.
2. **Analysis and Root Cause Identification**: The agent leverages AI models and Spark knowledge base to correlate extracted features and identify root causes of performance issues or failures. You'll receive:
   - **Analysis Insights**: Technical details about what the agent discovered and analyzed.
   - **Root Cause**: Clear explanation of what went wrong and why.
   - **Initial Assessment**: Whether the issue is code-related, configuration-related, or resource-related, some general guidance and analysis will be provided for mitigations.

3. **Code Recommendations** (if applicable): If the analysis identifies code-related issues based on the error classification, the agent can suggest leveraging the code recommendation tool to provide specific recommendations to implement the recommended code fix with exact before/after code along with suggested replacements.
   The troubleshooting process is iterative - you can continue the conversation to dive deeper into specific issues; you may also use the tools interactively in our local Spark code development to address code bugs or improve your code continuously.
