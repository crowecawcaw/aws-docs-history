

# Understanding Your Homepage
<a name="understanding-your-homepage"></a>

 Welcome to Amazon Connect Decisions. The homepage is your central hub for supply chain decision intelligence. This guide walks you through each section of the homepage so you can quickly orient yourself and start taking action. The homepage is comprised of four key sections: Section 1: Metrics, Section 2: Top topics for today, Section 3: Natural Language Interface (NLI) / Decisions Teammate, and Section 4: Navigation bar. 

![](http://docs.aws.amazon.com/connect-decisions/latest/userguide/images/understanding-your-homepage-overview.png)


## Key metrics
<a name="understanding-your-homepage-key-metrics"></a>

 The top of the homepage displays a maximum of five metric cards that give you a real-time snapshot of your supply chain health. Depending on the rules defined by the manager persona, these metrics can vary for your account compared to other accounts. 


| Metric | Description | 
| --- | --- | 
| **Total Open Insights** | The total number of active insights across all monitors. Includes a daily count of new insights created today. | 
| **Low Safety Stock (sample)** | Tracks SKUs where inventory has fallen below the safety stock threshold. | 
| **Projected Out of Stock (sample)** | Flags items at risk of stocking out based on current demand and supply signals. | 
| **Excess Safety Stock (sample)** | Identifies items carrying more inventory than needed, tying up working capital. | 
| **Days of Cover (sample)** | Monitors how many days of supply remain for tracked items. | 

Each card shows:
+ The **current total** of open insights in that category
+ A **daily increment** (for example, \+308 created today) indicating how many new insights were generated since midnight

**Tip**  
Click on any metric card to drill into the full list of insights for that category.

**Note**  
The Admin persona also sees metrics related to data validation errors and the total number of users in the account.

## Top topics for today
<a name="understanding-your-homepage-top-topics"></a>

 Below the metrics, the "Top Topics for Today" section surfaces the most important insight groups for your attention. Each topic card displays the number of insights and their associated financial impact for the planner persona. These topic cards vary if you are an Admin. 


| Topic card | Number of insights (sample values) | Financial impact (sample values) | What it means | 
| --- | --- | --- | --- | 
| **Highest Financial Impact** | 73 | $10,530,538 | Insights with the greatest dollar value at stake. Start here for maximum ROI. | 
| **Most Urgent to Act On** | 100 | $991 | Time-sensitive insights requiring immediate action, regardless of financial size. | 
| **In Progress** | 13 | $1,694,240 | Insights your team is actively working on. | 
| **Overdue** | 100 | $0 | Insights that have passed their action deadline and need immediate follow-up. | 

 Each card includes a **Review** button. Clicking it takes you to the full filtered list of insights for that topic. 

**Note**  
 Financial impact values are system-calculated estimates based on inventory exposure and demand signals. This can only be shown if your admin has provided financial information to Amazon Connect Decisions, otherwise it will be zero. 

## Natural Language Interface (NLI) / Decisions Teammate
<a name="understanding-your-homepage-nli"></a>

 The Decisions Teammate panel is located on the right side of the homepage. It is an AI-powered teammate that helps you navigate the application, interpret insights, and answer supply chain questions in plain language. It is always available across the application. 

**How to use it:**

1. Type a question in the **"Ask a question"** text field.

1. The teammate responds with contextual answers drawn from your data and insights.

1. You can ask questions like: *"What are my top stockout risks this week?"*, *"Show me insights for a specific product or region"*, *"What does days of cover mean for my portfolio?"* 

**Best ways to use NLI:**
+ When you need a quick summary of your current supply chain insights and plans.
+ When you want to explore insights without manually navigating filters.
+ When you need help understanding a specific insight, root cause, or recommendation.
+ When you want to know more about the demand plan or supply plan.
+ When you want to share feedback about system-generated insights or plans.

 As an agentic application, leverage the NLI whenever you want to learn more, take actions, and share feedback. The capabilities of NLI will continue to be enhanced over time. 

## Navigation bar
<a name="understanding-your-homepage-navigation-bar"></a>

 Amazon Connect Decisions uses two navigation elements to help you move through the platform. 

**Top Navigation Bar**
+ Amazon Connect Decisions logo – Click to return to the homepage from anywhere.
+ Home – Returns you to this homepage.
+ Insights – Opens the full Insights view with filtering, sorting, and detail capabilities.
+ Plans – Navigates to your Demand Plans and/or Supply Plans.
+ Notification bell – Alerts you to system updates.
+ User profile – Access your account settings, preferences, and sign-out options.

**Left Sidebar Menu**
+ Home – Homepage shortcut.
+ Insights – Expands to show sub-navigation including Configuration, where admins can manage insight monitors and thresholds.
+ Plans – Access demand and supply planning workflows.
+ Collapse/Expand button – Toggle the sidebar to maximize your workspace.

**Tip**  
The left sidebar can be collapsed to give you more screen space.