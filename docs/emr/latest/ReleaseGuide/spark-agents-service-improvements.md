# Service Improvements for Apache Spark Agents

The Apache Spark agent for Amazon EMR may use content, for example, to help the Agent provide better responses to common questions, fix operational issues, or for debugging.

## Content That AWS May Use for Service Improvement

- Your natural language prompts and generated responses from the Apache Spark agents for Amazon EMR, AWS Glue and Amazon SageMaker Notebooks

## Content That AWS Does Not Use for Service Improvement

- Code that you write yourself for the Spark applications
- SageMaker Notebook context and metadata
- Data from your AWS Glue Data Catalog or other data sources

Only Amazon employees will have access to the data. Your trust, privacy, and the security of your Customer Content are our highest priority and ensure that our use complies with our commitments to you. For more information, see Data Privacy FAQ.

## How to Opt Out

To opt out of data collection for the Apache Spark Agents configure an AI services opt-out policy in AWS Organizations for Amazon SageMaker Unified Studio MCP Service. For more information, see [AI services opt-out policies](../../../organizations/latest/userguide/orgs_manage_policies_ai-opt-out.md "../../../organizations/latest/userguide/orgs_manage_policies_ai-opt-out.md") in the _AWS Organizations User Guide_.

When you configure an AI services opt-out policy, it has the following effects:

- AWS will delete the data that it collected and stored for service improvement prior to your opt out (if any).
- After you opt out, AWS will no longer collect or store this data.
- AWS will no longer use your content for service improvement.
