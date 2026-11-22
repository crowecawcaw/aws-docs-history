

# How Resolutions works

 This topic explains the terms you see in Resolutions and how they relate to Connect Customer resources. It uses a sample loan approval process as a running example. 

## Key concepts
<a name="resolutions-how-it-works-key-concepts"></a>

*Work plan*  
 A structured version of one of your standard operating procedures (SOPs). A Work plan defines the Phases and Steps for one type of request, the order they run in, and who or what performs each Step. 

*Work plan version*  
 A published snapshot of a Work plan. A published version can't be changed. To change it, you clone the version, edit the clone, and publish it as a new version. Each Work plan has one default version. 

*Phase*  
 A stage of completion for a Resolutions Case, such as *Documentation Collection*. Every Resolutions Case on the Work plan moves through the Phases in order. Resolutions uses Phases to report the progress of each Resolutions Case in real time. 

*Step*  
 One unit of work inside a Phase that moves the request forward, such as *Prequalify Applicant* or *Collect Signed Disclosures*. Each Step has a description of the work and the configurations it needs to run. 

*Configuration and open items*  
 The values a Step needs before Resolutions can generate its flow, such as a flow module, a queue, or a from email address. Resolutions marks each missing value as an open item. You can publish a Work plan only after you resolve every open item. 

*Resolutions AI assistant*  
 The conversational assistant that reads your SOP, asks clarifying questions, generates the Work plan, and helps you finish its configuration. 

*Resolutions Case*  
 The record of one request. Resolutions creates a Resolutions Case from the Work plan's Case template when a request arrives. The Resolutions Case stores the request details in Case fields and shows the activity of every Phase and Step. 

*Specialist*  
 A person in your organization who completes Steps that need judgment, such as a loan officer who reviews a borderline application. Specialists receive these Steps as Tasks in the agent workspace. 

*Flow module*  
 A reusable flow that a Step calls to perform work outside the Work plan, such as pulling a credit report from a business application. For more information, see [Connect business applications](resolutions-integrations.md). 

## Resources that Resolutions creates
<a name="resolutions-how-it-works-resources-that-resolutions-creates"></a>

 When you generate flows and publish a Work plan version, Resolutions creates the following Connect Customer resources for that version. 


| Resource | Purpose | 
| --- | --- | 
| Work plan flow | Runs the version's Phases and Steps in order. | 
| Step flows |  One flow for each Step. Each Step flow performs the Step's work, such as creating a Task, sending an email, or invoking a flow module.  | 
| Information extraction flow |  Uses the prebuilt agentic data extraction capability in Connect Customer to read an inbound customer message and its attachments. Writes the extracted values to Case fields, creates a new Resolutions Case or updates an existing one, and starts the Work plan. You add this flow to your inbound contact flow.  | 
| Case template |  The template that every Resolutions Case on this version uses. Resolutions associates it with the version when you publish.  | 
| Case fields |  The fields that the information extraction flow and Step flows read and write, such as loanType or prequalificationOutcome.  | 
| Task templates |  Capture human input on specialist Steps, such as reviews, approvals, decisions, or exception handling.  | 
| Outbound queue and outbound whisper flow |  Send the Work plan's email to customers and link each email to its Resolutions Case. Resolutions creates these when you ask it to create a dedicated outbound queue, and sets the whisper flow on the queue. If you choose an existing queue instead, you set its outbound email flow yourself.  | 
| Information extraction definitions |  The entities to extract from customer messages. You can view them under Rules on the Information extraction tab.  | 

**Note**  
 Resolutions creates these resources on behalf of the user who generates the Work plan. That user's security profile must include permissions for each resource type. For more information, see [Grant access to Resolutions](resolutions-grant-access.md). 

## How Resolutions relates to Cases and Tasks
<a name="resolutions-how-it-works-how-resolutions-relates-to-cases-and-tasks"></a>

Resolutions coordinates work. Cases and Tasks record and route it.
+  **Cases** are the system of record. Each request has one Resolutions Case, and the Resolutions Case collects every email, Task, and decision for that request. Cases support Phases, which show the stage of the resolution lifecycle that each Resolutions Case is in. 
+  **Tasks** route each Step to the required application or human specialist. A Step that needs a specialist becomes a Task in the queue you choose for that Step. 
+  **Resolutions** decides what happens next. The Work plan determines which Step runs, what that Step does, and which Phase the Resolutions Case is in. 

 If you already use Cases and Tasks without Resolutions, those workloads keep working as they do today. You choose which processes to move onto a Work plan. 

## Example Work plan
<a name="resolutions-how-it-works-example-work-plan"></a>

 The screenshots in this guide use a sample mortgage process that the Resolutions AI assistant generated from a PDF SOP. The Work plan has 5 Phases and 10 Steps. After you publish a Work plan, its **Version details** tab summarizes the Phases and Steps and links to the flows that Resolutions created. 

 In the sample, the **Version details** tab starts with an overview that reads **Overview (5 phases, 10 steps)**. The **Phases** section lists **Phase 1: Application & Prequalification**, which contains **1.1: Prequalify Applicant**. 

![The Version details tab for the sample mortgage Work plan, showing the Overview and Phase 1.](https://docs.aws.amazon.com/connect/latest/adminguide/images/resolutions-example-work-plan-overview.png)


The following table lists every Step in the sample Work plan by Phase.



- **1. Application & Prequalification**
  - **Step:** 1.1 Prequalify Applicant
  - **Who or what performs the work:** A flow module pulls the credit report and checks loan limits. Failures and borderline results go to a loan officer.

- **2. Documentation Collection**
  - **Step:** 2.1 Collect Required Documents / **Who or what performs the work:** The Work plan emails the applicant for missing documents and sends reminders.
  - **Step:** 2.2 Verify Documents in Good Order / **Who or what performs the work:** A loan officer verifies the documents.

- **3. Credit & Collateral Review**
  - **Step:** 3.1 Underwrite Credit Risk / **Who or what performs the work:** An underwriter assesses credit risk.
  - **Step:** 3.2 Appraise Collateral & LTV / **Who or what performs the work:** A flow module orders the appraisal for secured loans.

- **4. Decision & Terms**
  - **Step:** 4.1 Determine Final Loan Decision / **Who or what performs the work:** The Work plan approves clean applications automatically and sends other combinations to a loan officer.
  - **Step:** 4.2 Issue Decision & Terms / **Who or what performs the work:** The Work plan emails the decision and terms to the applicant.
  - **Step:** 4.3 Collect Signed Disclosures / **Who or what performs the work:** The Work plan emails the applicant to request signatures.

- **5. Closing & Funding**
  - **Step:** 5.1 Execute Closing Documents / **Who or what performs the work:** A closing officer executes the documents.
  - **Step:** 5.2 Disburse Loan Funds / **Who or what performs the work:** A flow module disburses funds, and the Work plan emails a funding confirmation.



 Each Phase groups the Steps that complete one stage of the request. Each Step has its own description and configuration, and its own flow. 

 The following example shows **Phase 3: Credit & Collateral Review** expanded. It contains **3.1: Underwrite Credit Risk**, which sets the target queue to the Underwriting queue, and **3.2: Appraise Collateral & LTV**, which has an **InvokeFlowModule (Flows)** configuration. 

![Phase 3 expanded on the Version details tab, showing Steps 3.1 and 3.2.](https://docs.aws.amazon.com/connect/latest/adminguide/images/resolutions-example-phase-with-two-steps.png)
