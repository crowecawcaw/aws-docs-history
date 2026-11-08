

# Example agent use cases
<a name="agent-access-use-cases"></a>

With Amazon WorkSpaces Applications agent access, your agent works in a governed desktop session, operating in desktop applications, mainframe terminals, and browser sessions to complete tasks. This gives it access to the software your team already relies on. You bring your own agent, and agent access provides the session it runs in.

The agent runs under your IAM permissions, and you can review its activity through AWS CloudTrail logs and captured screenshots.

**Note**  
You can monitor agent performance through CloudWatch metrics.

## Back-office operations
<a name="agent-access-use-cases-back-office"></a>

Agents work through queues and batches to make judgment-heavy updates in the applications you rely on. Each case differs, so the agent reads the work, interprets it, and decides what to do.
+ Data extraction from files and entry into ERP systems
+ Insurance claims processing
+ Transaction reconciliation and processing

## Contact-initiated workflows
<a name="agent-access-use-cases-contact"></a>

A customer or employee request kicks off an agent that completes the follow-up work across backend systems right away. You can invoke the agent through an API, so it starts the moment a request arrives, and your team can focus on higher-value work while the agent handles the busy work and reports back when it is done.
+ CRM system contact data change
+ Clinician update to an EHR system
+ Payment terms change for billing

## Software testing and IT operations
<a name="agent-access-use-cases-testing-it"></a>

Agents run test cycles and recurring operational chores that teams otherwise do by hand or skip, reporting results back for review. This work runs against changing software, screens, and conditions. When a screen differs or an unexpected dialog appears, the agent adapts.
+ Run nightly regression subsets against legacy applications.
+ Validate image builds and patches.
+ Perform desktop application-packaging checks.
+ Perform configuration management across desktops and images.
+ Run periodic access audits that capture screenshot evidence.
+ Provide remote IT support by working directly on a user's desktop.
+ Complete forms in multiple languages.