# AWS Transform environment

AWS Transform is an agentic service that uses natural language processing to help you plan and execute your workload
transformations. You interact with AWS Transform primarily through a conversational interface, where the service adapts and
responds based on the context of your discussion. For example, you can start by describing your current architecture and
transformation goals using everyday language, such as "I need to migrate my on-premises VMs to EC2."

As you converse with AWS Transform, the service builds a customized job plan that aligns with your specific requirements.
The conversation flow is dynamic and driven by you, allowing you to refine your transformation plan iteratively.
You can modify the job plan during the conversation by making requests like "add a testing phase before production cutover" or
"remove the backup step since we already have a solution." You can also go back to a previous task and perform it again. AWS Transform continuously updates the plan based on your input,
ensuring the final transformation strategy meets your technical and business needs.

Here's what you see when you open AWS Transform.

- View control pane: This is the narrow pane on the left of AWS Transform. You can
  choose one of the icons to choose what view is shown to the right of the
  view control pane. Hover over each icon for a tool tip explaining the view. The give standard views, from top to bottom, are:

      + **Job Plan**
      + **Dashboard**
      + **Approvals**
      + **Artifacts**
      + **Worklog**

  Some workflows provide additional views.

When you are working in a job plan, the views are:

    + **Chat**
    + **Approvals**
    + **Artifact store**
    + **Worklog**

When you are in a workspace, the views are at the top:

    + **Jobs**
    + **Artifacts**
    + **Collaborators (Users)**
    + **Connectors**
    + **Settings**

- The **View** pane is next to the view controls.
- The **Chat** pane is in the center. This is where you conduct your conversation with AWS Transform.

###### Note

Users with read-only permissions are unable to send messages in the chat.

- To the right is the **Collaboration** pane. This appears when _human in the loop_ (HITL) activities are performed, such as:
  - Uploading data files
  - Reviewing information and plans provided by AWS Transform

## Start your project

AWS Transform guides you through your modernization and migration projects. To get started:

1. Create a workspace to host your project. On the **Workspaces** page, choose **Create workspace**. Follow the instructions and then open the workspace.
2. In the **Chat** pane, type "create a job"
3. Choose a job, and follow the instructions provide by AWS Transform. If your input is required, the **Collaboration** pane appears and explains what is required.

### Workflow flexibility

The AWS Transform workflow environment provides flexibility in the progression of your modernization projects. Using natural language in the chat pane you can:

- Retry a task that AWS Transform has already completed, providing different human-in-the-loop input along the way.
- Rerun a job, for example, if there have been changes in your modernization sources.

## Chatting with AWS Transform

AWS Transform chat is available at every stage of your project. To open the chat click the purple hexagonal icon in the lower right corner of the web console.

The chat is there for you to ask anything. For example, you can ask the chat to explain concepts, guide you through a process, explain a AWS Transform request or response, or explain a AWS Transform report.

###### Note

Users with read-only permissions are unable to send messages in the chat.

### AWS Transform chat integrations

AWS Transform chat is integrated with:

#### Experience-Based Acceleration

[Experience-Based
Acceleration (EBA)](https://aws.amazon.com/experience-based-acceleration/ "https://aws.amazon.com/experience-based-acceleration/") is offered through AWS Transform chat. It enables you to perform EBA
assessment for Windows workloads and generate a plan. You can start by importing
assessment results from CAST. It helps you discover your application portfolio, after
which you can use AWS Transform chat to select applications that meet your business needs
(for example, filtering applications based on complexity or lines of code). You can then perform
deeper assessment of the selected application and generate a modernization
plan.

#### AWS Countdown Premium

[AWS Countdown Premium](https://aws.amazon.com/premiumsupport/aws-countdown/ "https://aws.amazon.com/premiumsupport/aws-countdown/") (CDP) integrated into AWS Transform provides sustained,
expert guidance with designated AWS engineering support. Your designated CDP Engineer dives deep into your tech stack, providing personalized, context-aware support when issues arise.
Users can leverage AWS Transform to log a support ticket directly from its chat interface.
The support ticket embeds worklog and job plan details to help support understand the customer's context.
If a customer or partner is part of the CDP Program, the support ticket automatically gets routed to the designated
CDP Engineer who can help debug issues, interpret transformation outputs, and drive progress for expedited issue resolution. For example:

- For .NET workloads, CDP can assist with repository connector issues, dependency resolution, and post-transformation deployment.
- In mainframe scenarios, CDP can help troubleshoot refactored Java code, configure database migration tools, and build CI/CD pipelines.
- In VMware migrations, CDP can accelerate network configuration, Application Migration Service setup, and agent installation.

#### AWS Skill Builder

[AWS Skill Builder](https://skillbuilder.aws/ "https://skillbuilder.aws/") provides relevant
learning modules through the chat. You can ask AWS Transform chat about your learning needs, and it presents you relevant course catalog.
Skill Builder delivers contextual micro-learning experiences as you work through transformation stages.
