

# Onboarding
<a name="onboarding"></a>

## Onboarding for Amazon Connect Decisions
<a name="onboarding-overview"></a>

Amazon Connect Decisions's onboarding agent serves as your AI setup teammates, abstracting away the technical complexity of configuring insights monitoring. Instead of manually defining SQL queries, mapping data schemas, or translating business requirements into technical specifications, you work conversationally with the agent to set up your monitoring system.

**What the onboarding agent can help you with:**

1. **Understanding your business context:** Share your standard operating procedures, business policies, and operational guidelines in natural language or by uploading existing documents. Agents analyze your materials and extract relevant configuration parameters automatically.

1. **Translating requirements into configurations:** Describe what you want to monitor in plain language; for example, “I need to track forecast accuracy for high-value products” or “Alert me when inventory drops below safety stock levels.” The agent translates these business requirements into the appropriate metric definitions, rules, and thresholds without requiring SQL knowledge.

1. **Iterating on configurations:** Refine your monitoring setup through conversation. Ask questions like “Can we make this rule more sensitive?” or “Should we add filtering criteria for specific product categories?” The agent helps you explore options and understand trade-offs before committing changes.

1. **Validating changes before production:** Use the preview function to see how your configurations would perform against real data, enabling you to review insights that would be generated with your new settings before you save changes to production.

1. **Troubleshooting and optimization:** When configurations don't produce expected results, describe what you're seeing and the agent helps diagnose issues and recommend improvements.

This conversational approach means you can configure sophisticated supply chain monitoring without deep technical expertise. AI teammates handle the complexity while you focus on defining your business requirements and operational priorities.

## Prerequisites
<a name="onboarding-prerequisites"></a>

**Prerequisites**

Before configuring insights, ensure:
+ Amazon Connect Decisions instance is set up with data flows configured and running
+ Manager role permissions to access configuration settings
+ Required data entities uploaded to your Supply Chain Data Lake, including:
  + Historical demand or sales data (minimum 12 months recommended)
  + Product master data with classifications and attributes
  + Site and location information
  + Current inventory positions
  + Supplier and lead time data (if configuring supply monitoring)
+ Standard operating procedures or business policies prepared for upload (optional but recommended to accelerate configuration)