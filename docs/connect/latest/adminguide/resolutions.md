

# Resolve operational work with Resolutions in Amazon Connect Customer

 Resolutions in Amazon Connect Customer is an agentic solution for high-volume operational work such as refund requests, dispute resolution, fraud investigations, insurance claims, and loan applications. Resolutions turns your standard operating procedures (SOPs) into structured Work plans. AI agents run each Work plan from intake through verified resolution. Specialists in your organization step in for approvals and exceptions. 

 Requests like these often stall while employees search several applications for information, interpret instructions, and hand work to the next team. Resolutions coordinates that work in one place. Each request becomes a Resolutions Case that follows the Steps in your Work plan. Every request follows the same policy, and every action and decision is recorded on the Resolutions Case. 

**Topics**
+ [What you can do with Resolutions](#resolutions-what-you-can-do-with-resolutions)
+ [How Resolutions works](#resolutions-how-resolutions-works)
+ [Who uses Resolutions](#resolutions-who-uses-resolutions)
+ [How Resolutions works](resolutions-how-it-works.md)
+ [Get started with Resolutions](resolutions-get-started.md)
+ [Set up your instance for Resolutions](resolutions-prerequisites.md)
+ [Grant access to Resolutions](resolutions-grant-access.md)
+ [Create and publish a Work plan](resolutions-create-work-plan.md)
+ [Start Work plans from inbound email](resolutions-start-work-plan.md)
+ [Work on Resolutions Cases in the agent workspace](resolutions-specialists.md)
+ [Manage Work plans and versions](resolutions-manage-work-plans.md)
+ [Connect business applications](resolutions-integrations.md)
+ [Troubleshoot Resolutions](resolutions-troubleshoot.md)
+ [Resolutions quotas](resolutions-quotas.md)

## What you can do with Resolutions
<a name="resolutions-what-you-can-do-with-resolutions"></a>
+  **Create a Work plan from an SOP.** Upload a process document or describe your process in plain language. The Resolutions AI assistant asks clarifying questions about exceptions, decision rules, and approval thresholds. It then generates the Phases and Steps of the Work plan for you to review. 
+  **Assign each Step to a specialist or a business application.** Steps can extract information from customer emails and attachments, call your business applications through flow modules, email customers for missing information, and route approvals to a specialist queue. 
+  **Publish and run the Work plan.** Resolutions generates the flows, Case template, Case fields, and Task templates that the Work plan needs. Each incoming request creates a new Resolutions Case or updates an existing one. The Work plan then moves the Resolutions Case toward resolution. 
+  **Track every request.** Specialists see each Phase and Step of the Resolutions Case in the agent workspace. Operations managers see the status of every Resolutions Case and open analytics for each Work plan. 

## How Resolutions works
<a name="resolutions-how-resolutions-works"></a>

 Resolutions uses Connect Customer features that you might already use. [Cases](https://docs.aws.amazon.com/connect/latest/adminguide/cases.html) hold the record of each issue. [Tasks](tasks.md) route each Step to the required application or human specialist. Work plans are made up of deterministic [flows](https://docs.aws.amazon.com/connect/latest/adminguide/connect-contact-flows.html) that represent the applicable SOP to resolve the Resolutions Case. Resolutions uses existing communication channels in Connect Customer, such as voice, chat, and email, to interact with relevant stakeholders during the process. Resolutions uses flow modules to integrate with external applications through the [External tool flow block](resolutions-integrations.md). 

1.  The administrator assigns the operations manager the new ResolutionsUser security profile to access Resolutions from their Connect Customer admin website. For more information, see [Grant access to Resolutions](resolutions-grant-access.md). 

1.  The operations manager creates a [Work plan](resolutions-create-work-plan.md) by uploading their SOP documentation or describing their process in natural language, and answering Resolutions' questions in the conversational interface. Resolutions helps identify undocumented exceptions or edge conditions, such as what to do when a customer doesn't respond to an email even after waiting for 2 days. 

1.  The operations manager reviews the Work plan that Resolutions created. Where the source documentation is out of date with current practices, the manager updates the Step sequence or eliminates unnecessary actions before publishing. 

1.  The Work plan sequences the required Steps into Phases that track the progress of the Resolutions Case toward resolution. Cases now support Phases to identify different stages of the resolution lifecycle. 

1.  The operations manager finishes the required configuration by specifying the queues, email addresses, and flow modules required to resolve the Resolutions Case end to end. 

1.  Resolutions also creates the required Case templates, Case fields, and Task templates (to capture human input such as reviews, approvals, decisions, or exception handling). If you ask, Resolutions also creates a dedicated outbound queue and outbound whisper flow for the Work plan's email. 

1.  Finally, Resolutions creates an information extraction flow that uses the prebuilt agentic data extraction capability in Connect Customer. The flow is configured with the required Case fields and extraction elements, and contains the logic to create a new Resolutions Case or update an existing one. **The operations manager or an authorized admin updates the inbound contact flow to include the information extraction flow after determining the relevant Work plan to run on the Resolutions Case.** 

**Note**  
 Resolutions doesn't automatically update existing inbound contact flows, because they might also be used for use cases outside Resolutions. 

 Resolutions creates a Resolutions Case for each request, applies the relevant Work plan, and tracks it through completion. Resolutions uses Connect Tasks behind the scenes to route and track each Step. Email, voice, and chat communications bill separately at Connect Customer rates. Resolutions uses existing Connect Customer capabilities to configure specialist experiences, show progress in real time, forecast volumes, schedule specialists, and evaluate performance. 

## Who uses Resolutions
<a name="resolutions-who-uses-resolutions"></a>


| Role | What they do | Where they work | 
| --- | --- | --- | 
| Connect Customer administrator |  Prepares the instance, grants access, and adds Work plans to inbound contact flows  | Connect Customer admin website and AWS Management Console | 
| Operations manager (Work plan author) |  Creates, reviews, configures, and publishes Work plans. Can also add Work plans to inbound contact flows if authorized.  |  Resolutions in the Connect Customer admin website  | 
| Specialist |  Completes the Steps that need human judgment, such as approvals  | Agent workspace | 
| Developer |  Builds flow modules and registers external tools for business applications  | Flow designer, Amazon Bedrock AgentCore console, AWS CLI | 