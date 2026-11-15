

# Extend agents with knowledge bases
<a name="genai-knowledge-bases"></a>

Enhance your CID Operations Advisor with Cloud Financial Management (CFM) best practices by adding the [CFM Technical Implementation Playbooks (CFM TIPs)](https://catalog.workshops.aws/awscff/en-US) as a knowledge base. This enables your chat agent and flows to provide more effective guidance grounded in proven CFM frameworks and actionable examples.

For full details on Web Crawler integration, see [Web Crawler integration in Amazon Quick](https://docs.aws.amazon.com/quick/latest/userguide/web-crawler-integration.html).

## Step 1: Create a Web Crawler Knowledge Base
<a name="step-1-create-a-web-crawler-knowledge-base"></a>

1.  **Navigate to Quick Knowledge Bases** 
   + Open Amazon Quick console
   + Select "Knowledge bases" from navigation menu
   + Click "Create knowledge base"

1.  **Select Web Crawler as Source** 
   + Choose "Web Crawler" as the integration type
   + Click "Create"

1.  **Configure the Web Crawler** 
   + Knowledge base name: "CFM Technical Implementation Playbooks"
   + Description: "Cloud Financial Management TIPs from the AWS Cloud Financial Framework workshop"
   + Source URL: `https://catalog.workshops.aws/awscff/en-US` 
   + Authentication: No authentication (public website)
   + Review crawl scope and content filter settings as needed

1.  **Start Data Sync** 
   + After clicking create, the initial data sync starts automatically
   + Wait for the sync to complete before proceeding

## Step 2: Add Knowledge Base to Your CID Space
<a name="step-2-add-knowledge-base-to-your-cid-space"></a>

1.  **Open Your CID Space** 
   + In Quick console, select "Spaces"
   + Open the Space of the agent you want to extend, for example "CID FinOps Space" or "CID Operations Space" created by `cid-cmd create-agent`, or your own CID Space

1.  **Link the CFM Knowledge Base** 
   + Click on "Knowledge bases"
   + Click "Add knowledge base"
   + Select "CFM Technical Implementation Playbooks"
   + Click "Add"

1.  **Verify Integration** 
   + Confirm the knowledge base appears in your Space’s linked sources
   + The agents and flows linked to this Space now have access to CFM TIPs content. `cid-cmd update-agent` keeps knowledge bases you added, unless you pass `--on-drift override` 

## Step 3: Test the Enhanced Agent
<a name="step-3-test-the-enhanced-agent"></a>

Test your CID Operations Advisor with CFM-specific prompts to verify the knowledge base integration:
+ Based on my CUDOS data, which CFM playbook should I follow to reduce EC2 costs?
+ What does the CFM framework recommend for organizations at our stage of cloud financial maturity?

The agent will now combine your CID dashboard data with CFM TIPs guidance to provide recommendations grounded in both your actual cloud usage and proven CFM frameworks.