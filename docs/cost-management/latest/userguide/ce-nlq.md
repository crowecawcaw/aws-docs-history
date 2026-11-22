

# Asking questions about your costs using AWS assistant

Cost Explorer enables you to ask questions about your AWS costs using suggested prompts or in your own words via the **Ask question** button, powered by **AWS assistant**. You can receive detailed insights in **AWS assistant** while Cost Explorer automatically updates its charts, tables, and report parameters including filters, groupings, and dates to reflect the analysis. This capability is available through two features: suggested prompts and the **Ask question** button.

**Topics**
+ [Using suggested prompts](#ce-nlq-suggested-prompts)
+ [Using the Ask question button](#ce-nlq-ask-question)
+ [Understanding visualization updates](#ce-nlq-visualization-updates)
+ [Using Analyze with AWS assistant](#ce-nlq-analyze-with-q)
+ [Continuing the conversation with follow-up questions](#ce-nlq-follow-up)
+ [Permissions](#ce-nlq-permissions)

## Using suggested prompts
<a name="ce-nlq-suggested-prompts"></a>

Cost Explorer displays suggested prompts above your Cost & Usage Overview data. These prompts surface the most commonly asked cost questions, such as "Show me my top spending services this month" or "Show my projected database cost for next month." You can click any prompt to instantly receive insights from **AWS assistant** without needing to type a question.

When you click a suggested prompt, the following occurs:

1. The **AWS assistant** chat panel opens automatically.

1. The prompt is submitted to **AWS assistant** without requiring additional input.

1. **AWS assistant** generates detailed insights in the chat panel.

1. Cost Explorer refreshes with the corresponding visualization, and all report parameters including filters, groupings, and date ranges are automatically configured in the **Report Parameters** panel.

Each time you load the page or complete a query, the prompts refresh with new suggestions. When you click a prompt during a session, it is replaced with a new prompt, ensuring you always have fresh analytical options to explore. You can scroll horizontally through the prompt container to discover additional suggestions beyond those initially visible.

## Using the Ask question button
<a name="ce-nlq-ask-question"></a>

For questions that go beyond the suggested prompts, the **Ask question** button is positioned next to the suggested prompts. When you click this button, the **AWS assistant** chat panel opens and you can type any cost related question in your own words, such as "What is my current month's cost and usage compared to the previous month?" or "Show me my EC2 costs broken down by instance type for the last 3 months."

**AWS assistant** processes your question and delivers insights in the chat panel while determining how to display the visualization. Cost Explorer automatically updates charts and tables when analysis is based on your cost and usage data. When **AWS assistant** compiles insights from additional datasets such as pricing or anomaly detection, visualizations are displayed in **AWS assistant**'s new artifacts panel.

## Understanding visualization updates
<a name="ce-nlq-visualization-updates"></a>

When you interact with suggested prompts or the **Ask question** button, Cost Explorer automatically updates its charts and tables when the analysis is based on your cost and usage data. All corresponding report parameters, including filters, groupings, and date ranges, are visible in the **Report Parameters** panel so you can verify exactly which data subset is included in the analysis.

When **AWS assistant** draws from additional datasets to provide richer analysis, visualizations are displayed in **AWS assistant**'s artifacts panel alongside the chat.

After **AWS assistant** updates your Cost Explorer view, you can:
+ Save the view as a Cost Explorer report.
+ Share the URL with colleagues. All filters are preserved in the URL.
+ Bookmark the view for future reference.
+ Export the data to CSV for further analysis.
+ Manually adjust any of the filters and groupings in the **Report Parameters** panel to refine your view.

## Using Analyze with AWS assistant
<a name="ce-nlq-analyze-with-q"></a>

When you configure a cost report in Cost Explorer with your preferred filters, date range, and groupings, you can click **Analyze with AWS assistant** to receive a comprehensive explanation of what you're viewing. **AWS assistant** analyzes the complete context of your current cost report and delivers detailed explanations in its chat panel.

When you click **Analyze with AWS assistant**, the following occurs:

1. The **AWS assistant** chat panel opens automatically.

1. A prompt is auto-submitted based on your current view's time period.

1. **AWS assistant** analyzes your cost data based on your applied Report Parameters (filters, dimensions, granularity, and date range).

1. A comprehensive explanation is delivered in the chat panel covering cost trends, top drivers, anomalies, and guidance to explore optimization opportunities.

Your Cost Explorer view remains unchanged. The analysis appears only in the **AWS assistant** chat panel.

The analysis adapts based on the time period you are viewing:
+ **Historical dates**: When your cost report covers past dates, **AWS assistant** explains what drove your cost changes, identifies top cost drivers with specific amounts and percentages, and surfaces anomalies detected by AWS Cost Anomaly Detection with explanations of their likely causes.
+ **Future dates**: When your cost report covers future dates, **AWS assistant** delivers forecast explanations covering projected spending trajectories, the services expected to drive future costs with service-level breakdowns, and the factors influencing your projections. Anomalies are not included for future-only periods.
+ **Mixed periods**: When your cost report spans both historical and future dates, **AWS assistant** provides a unified explanation covering both what happened in the past and what is projected going forward.
+ **Compare mode**: When you are using the Cost Explorer Compare feature (month over month or custom month selection), clicking **Analyze with AWS assistant** delivers a comparison analysis identifying the largest cost changes between the two selected months, with anomaly detection.

After receiving your initial analysis, you can ask follow-up questions to explore any finding in greater detail. For example, you can ask "Tell me more about the anomalies detected this month" or "What are my optimization opportunities?" **AWS assistant** maintains the full context of your conversation, allowing you to progressively drill deeper into your cost data.

**Note**  
**Analyze with AWS assistant** does not update your Cost Explorer visualization. Your configured view remains exactly as you set it. All analysis output appears only in the **AWS assistant** chat panel.

**Note**  
For historical and compare analyses, the response includes guidance to discover optimization opportunities through follow-up questions. When you ask about optimization opportunities, **AWS assistant** provides recommendations from Cost Optimization Hub.

## Continuing the conversation with follow-up questions
<a name="ce-nlq-follow-up"></a>

After clicking a suggested prompt or asking a question using the **Ask question** button, you can continue the dialogue in **AWS assistant** to drill deeper into your costs. For example, after seeing your top spending services, you might ask "Why did my RDS costs increase last month?" or "Break this down by region." **AWS assistant** maintains the conversation context, allowing natural exploration of your cost data.

**AWS assistant** draws from extensive knowledge beyond what is visible in your current Cost Explorer view, including pricing data, budget information, and anomaly detection data, to provide richer context and more comprehensive answers. If a follow-up question produces a visualization that Cost Explorer can display, it updates automatically. Otherwise, the visualization appears in **AWS assistant**'s artifacts panel while insights continue in the chat.

## Permissions
<a name="ce-nlq-permissions"></a>

To use the suggested prompts and **Ask question** button in Cost Explorer, you need the following permissions in addition to your existing Cost Explorer permissions:
+ ****AWS assistant** permissions**: `q:StartConversation`, `q:SendMessage`
+ **Pass request permission**: `q:PassRequest`, which allows **AWS assistant** to call AWS APIs on your behalf

For least-privilege access, create a custom IAM policy that grants only `q:StartConversation`, `q:SendMessage`, and `q:PassRequest`. Alternatively, administrators who already use **AWS assistant** across multiple integrations can use the `AmazonQFullAccess` managed policy, which includes these permissions along with broader **AWS assistant** access. The integration respects all existing IAM boundaries. **AWS assistant** only accesses cost data you are authorized to view through Cost Explorer.

For detailed permission configurations and security considerations, see [Security for cost management capabilities in AWS assistant](ce-q-security.md).

**Note**  
Organizations can restrict access to the suggested prompts and **Ask question** button while maintaining Cost Explorer access using IAM condition keys. For more information, see the [AWS assistant security documentation](https://docs.aws.amazon.com/assistant/latest/userguide/security.html#security-iam).