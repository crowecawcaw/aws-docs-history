# Quick Research steps in Amazon Quick Flows

Amazon Quick Research is available as a step within Amazon Quick Flows, allowing you to generate comprehensive research reports as part of automated, multi-step workflows. This integration transforms how teams approach research by embedding it directly into their everyday processes, eliminating the need to switch between tools or conduct analysis separately.

## What you can do

Quick Research steps in Flows enable the automation and standardization of research processes across common business scenarios, including sales teams creating account plans, legal and compliance teams conducting detailed analysis and policy reviews, intellectual property specialists researching patent prior art, and business users generating in-depth industry reports for strategic planning. By incorporating Research steps within multi-step workflows, these processes can be scheduled to execute automatically, ensuring timely delivery of insights without interruption.

## Adding a research step to your flow

To add a research step to your flow, follow these steps:

1. In the flow Editor mode, select the **+ Add step** button.
2. From the step menu, choose **Research**.
3. Configure your research agent as follows:
   1. For **Title**, enter a clear, descriptive name for your research.
   2. For **Research Objective**, enter a detailed description of what you want accomplished. Use `@` to reference inputs from previous flow steps. Use this both to have research informed by prior steps in your flow and take dynamic user inputs to incorporate in the research objective.
   3. For **Research Materials**, select data sources—web search, file uploads, or Quick assets.

###### Tip

Use an @reference in your objective to get dynamic inputs from user or utilize outputs of previous steps in the workflow. You can also reference your Research step in later steps to utilize the generated report like to send a summary over email to your team.
