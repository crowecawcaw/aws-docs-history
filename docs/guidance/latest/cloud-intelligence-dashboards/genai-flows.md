

# Flows
<a name="genai-flows"></a>

Create intelligent workflows that monitor your CID dashboards and automatically take actions based on dashboard insights. Amazon Quick offers multiple approaches for creating flows, allowing you to choose the method that best fits your workflow preferences and technical requirements.

Flows can use the same Spaces as the CID agents. Ready-made CID flows are coming; until then, start from the examples below.

## Flow Creation Methods
<a name="flow-creation-methods"></a>

You can create CID flows using different approaches. This guide demonstrates two methods:

 **Method 1: Natural Language Prompt (NLP)** - Describe your desired flow in plain language and let Quick generate it automatically using AI-powered flow creation.

 **Method 2: Build from Scratch** - Create a blank flow and configure each step manually for complete control over workflow design and logic.

## Flow Example 1: Automated Cost Anomaly Investigation & Action
<a name="flow-example-1-automated-cost-anomaly-investigation-action"></a>

This flow automatically detects cost spikes in your CUDOS dashboard and instantly investigates root causes using AI-powered analysis. When anomalies exceed your threshold, it generates immediate action plans and alerts teams with specific remediation steps.

### Method 1: Create Using Natural Language Prompt
<a name="method-1-create-using-natural-language-prompt"></a>

#### Click to see the demo
<a name="genai-create-flow-1-2-demo"></a>

![Amazon Quick Create Flow 12](https://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/images/QuickSuite_create_flow_1_2.gif)


 **Navigate to Quick Flows** 
+ In Quick console, select "Flows"
+ Click "Create Flow"
+ Click "Generate"

 **Enter Flow Description** 

```
Create a flow named "Cost Anomaly Investigation & Action" that automatically detects AWS cost spikes and investigates root causes.

Setup:
* Add text input "Alert Threshold" (default: "20% increase")
* Add text input "Analysis Time Period" (default: "Last 30 days")
* Add dashboard step "Extract CUDOS Cost Data" using your CUDOS dashboard to analyze cost trends above @Alert Threshold for @Analysis Time Period
* Add reasoning group "Anomaly Detection" (runs once) that triggers investigation only if anomaly detected

Inside reasoning group, add these steps in order:
1. Web search step titled "Research Causes" to research AWS cost spike causes for the identified services
2. Analysis step titled "Root Cause Analysis" using Versatility and Performance model to identify likely causes based on the extracted cost data and research findings
3. Analysis step titled "Generate Action Plan" using Fast Response model to create immediate action plan with containment, investigation, resolution, and prevention measures
4. Analysis step titled "Alert" using Fast Response model to create concise alert message with issue summary, root cause, top 3 actions, and call-to-action
```

 **Complete Setup** 
+ Click "Generate Flow"
+ Review and adjust the generated flow as needed
+ Click "Share and publish"
+ Click "Run mode" and "Start"

### Method 2: Build from Scratch
<a name="method-2-build-from-scratch"></a>

#### Click to see the demo
<a name="genai-create-flow-1-demo"></a>

![Amazon Quick Create Flow 11](https://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/images/QuickSuite_create_flow_1_1.gif)


 **Navigate to Quick Flows** 
+ In Quick console, select "Flows"
+ Click "Create Flow"
+ Click "Create a blank flow"

 **Configure Flow Settings** 
+  **Flow name**: "Cost Anomaly Investigation & Action"
+  **Description**: "Automatically detects cost spikes and investigates root causes with action plans"

 **Step 1: Text Input** 
+ Title: *Alert Threshold* 
+ Placeholder: *Enter cost spike threshold (e.g., 20% increase or $1000)* 
+ Default value: 20% increase

 **Step 2: Text Input** 
+ Title: *Analysis Time Period* 
+ Placeholder: *Specify analysis period (e.g., "last 30 days", "last 30 days vs previous 30 days", "current quarter vs last quarter")* 
+ Default value: Last 30 days

 **Step 3: Dashboard and Topics** 
+ Title: *Extract CUDOS Cost Data* 
+ Sources: CUDOS Dashboard v5
+ Prompt:

```
Analyze recent cost trends and identify any anomalies above @Alert Threshold. Show cost variance by service, time period, and resource type. Do this for the following period: @Analysis Time Period.
```

 **Step 4: Reasoning Group** 
+ Title: *Anomaly Detection* 
+ Run these steps: Once
+ Reasoning instructions: If cost anomaly detected in @Extract CUDOS Cost Data above @Alert Threshold, then run investigation and remediation steps. If no significant anomaly, skip detailed analysis.

 **Step 4.1: Web Search Output** 
+ Title: *Research Causes* 
+ Prompt:

```
Research AWS cost spike causes for services identified in @Extract CUDOS Cost Data. Find common root causes, resolution best practices, and prevention strategies.
```

 **Step 4.2: General Knowledge - Versatility and Performance** 
+ Title: *Root Cause Analysis* 
+ Prompt:

```
Based on @Extract CUDOS Cost Data and @Research Causes, provide detailed root cause analysis for the cost anomaly. Identify most likely causes and prioritize investigation steps.
```

 **Step 4.3: General Knowledge - Fast Response** 
+ Title: *Generate Action Plan* 
+ Prompt:

```
Create immediate action plan based on @Root Cause Analysis. Include: 1) Immediate containment steps, 2) Investigation procedures, 3) Resolution actions, 4) Prevention measures.
```

 **Step 4.4: General Knowledge - Fast Response** 
+ Title: *Alert* 
+ Prompt:

```
Create a concise cost alert message using this template. Keep total message under 200 words, prioritize by biggest cost impact, use clear business language:

"🚨 Cost Spike Alert

ISSUE: [Extract top cost anomaly from @Extract CUDOS Cost Data with $ amount and % increase]

ROOT CAUSE: [Summarize main driver from @Root Cause Analysis in 1-2 sentences]

IMMEDIATE ACTION: [List top 3 actions from @Generate Action Plan, ranked by impact]

THRESHOLD: @Alert Threshold exceeded

PERIOD: @Analysis Time Period

[End with clear next step for reader]"

Make it scannable with bullet points, focus on dollar impact, and end with a specific call-to-action like "Review detailed analysis in CUDOS dashboard".
```

 **Deploy and Run** 
+ Verify all configuration is correct
+ Click "Share and publish"
+ Click "Run mode" and "Start"

## Flow Example 2: Top 5 Cost Optimization Quick Wins
<a name="flow-example-2-top-5-cost-optimization-quick-wins"></a>

This flow instantly analyzes your CUDOS dashboard to identify and prioritize the top 5 cost optimization opportunities that deliver maximum savings with minimal effort.

### Method 1: Create Using Natural Language Prompt
<a name="method-1-create-using-natural-language-prompt-2"></a>

#### Click to see the demo
<a name="genai-create-flow-2-2-demo"></a>

![Amazon Quick Create Flow 22](https://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/images/QuickSuite_create_flow_2_2.gif)


 **Navigate to Quick Flows** 
+ In Quick console, select "Flows"
+ Click "Create Flow"
+ Click "Generate"

 **Enter Flow Description** 

```
Create a flow named "Top 5 Cost Optimization Quick Wins" that identifies and prioritizes top 5 cost optimization opportunities with maximum savings and minimal effort.

Setup:
* Add dashboard step "Extract CUDOS Data" using your CUDOS dashboard to extract cost optimization recommendations
* Add analysis step "Rank Opportunities" using Versatility and Performance model to rank opportunities by savings potential, implementation ease, and business risk
* Add reasoning group "Top 5 Selection" (runs once) to select top 5 highest-impact quick wins

Inside reasoning group:
* Analysis step "Quick Action Plans" using Fast Response model for concise action plans with savings, timeline, and 3-step implementation

After reasoning group:
* Web search step "Implementation Guidance" for AWS best practices
* Analysis step "Final Report" using Fast Response model for executive summary with top 5 opportunities (max 100 words each)
* Analysis step "Quick Wins Report" using Fast Response model for email-ready report (max 1000 characters) with template: "🚀 Your Top 5 Cost Optimization Quick Wins Ready for Implementation: @Final Report. For detailed analysis, review your CUDOS dashboard."
```

 **Complete Setup** 
+ Click "Generate Flow"
+ Review and adjust the generated flow as needed
+ Click "Share and publish"
+ Click "Run mode" and "Start"

### Method 2: Build from Scratch
<a name="method-2-build-from-scratch-2"></a>

#### Click to see the demo
<a name="genai-create-flow-2-1-demo"></a>

![Amazon Quick Create Flow 21](https://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/images/QuickSuite_create_flow_2_1.gif)


 **Navigate to Quick Flows** 
+ In Quick console, select "Flows"
+ Click "Create Flow"
+ Click "Create a blank flow"

 **Configure Flow Settings** 
+  **Flow name**: "Top 5 Cost Optimization Quick Wins"
+  **Description**: "Identifies and prioritizes top 5 cost optimization opportunities with maximum savings and minimal effort"

 **Step 1: Dashboard and Topics** 
+ Title: *Extract CUDOS Data* 
+ Sources: CUDOS Dashboard v5
+ Prompt:

```
Extract all cost optimization recommendations from CUDOS dashboard including estimated savings, affected services, implementation complexity, current monthly costs, and resource utilization data. Include unused resources, right-sizing opportunities, reserved instance recommendations, and storage optimizations.
```

 **Step 2: General Knowledge - Versatility and Performance** 
+ Title: *Rank Opportunities* 
+ Prompt:

```
Analyze @Extract CUDOS Data and rank ALL optimization opportunities by impact score based on: 1) Monthly savings potential (dollars), 2) Implementation ease (simple/moderate/complex), 3) Business risk (low/medium/high). Prioritize low-risk, high-savings, easy-to-implement opportunities.
```

 **Step 3: Reasoning Group** 
+ Title: *Top 5 Selection* 
+ Run these steps: Once
+ Reasoning instructions: Select the top 5 highest-impact opportunities from @Rank Opportunities. Ensure variety in optimization types (unused resources, right-sizing, purchasing options, storage) and focus on quick wins that can be implemented within 1-2 weeks.

 **Step 3.1: General Knowledge - Fast Response** 
+ Title: *Action Plans* 
+ Prompt:

```
For the top 5 opportunities from @Rank Opportunities, create concise action plans with: 1) Specific monthly savings, 2) Implementation time (hours/days), 3) 3-step action summary, 4) Risk level. Format as actionable checklist items that teams can execute immediately.
```

 **Step 4: Web Search Output** 
+ Title: *Implementation Guidance* 
+ Prompt:

```
Research current AWS best practices for the specific optimization types identified in @Quick Action Plans. Find latest AWS documentation, common implementation steps, and potential gotchas to avoid.
```

 **Step 5: General Knowledge - Fast Response** 
+ Title: *Final Report* 
+ Prompt:

```
Create executive-ready optimization report combining @Quick Action Plans and @Implementation Guidance. Format as: 1) Executive summary with total savings potential, 2) Top 5 opportunities with savings/effort/steps, 3) "Take Action Now" vs "Review in CUDOS" guidance for each item. Keep concise and action-oriented. Have maximum 100 words per quick win.
```

 **Step 6: General Knowledge - Fast Response** 
+ Title: *Quick Wins Report* 
+ Prompt:

```
Prepare an actionable cost optimization report, short, concise, readable that I can send as an email. Have maximum 1000 characters. Here it the template: "🚀 Your Top 5 Cost Optimization Quick Wins Ready for Implementation: @Final Report. For detailed analysis, review your CUDOS dashboard. Total potential monthly savings and immediate action steps included."
```

 **Deploy and Run** 
+ Verify all configuration is correct
+ Click "Share and publish"
+ Click "Run mode" and "Start"

## Flow automation tips
<a name="flow-automation-tips"></a>
+ Start with simple, well-defined processes
+ Test flows with sample data before production deployment
+ Set appropriate thresholds to avoid alert fatigue
+ Design flows with clear success and failure paths