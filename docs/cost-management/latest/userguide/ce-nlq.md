# Asking questions about your costs using Amazon Q Developer

Cost Explorer enables you to ask questions about your AWS costs using suggested prompts or in your own words via the **Ask question** button, powered by **Amazon Q Developer**. You can receive detailed insights in **Amazon Q Developer** while Cost Explorer automatically updates its charts, tables, and report parameters including filters, groupings, and dates to reflect the analysis. This capability is available through two features: suggested prompts and the **Ask question** button.

###### Topics

- [Using suggested prompts](#ce-nlq-suggested-prompts "#ce-nlq-suggested-prompts")
- [Using the Ask question button](#ce-nlq-ask-question "#ce-nlq-ask-question")
- [Understanding visualization updates](#ce-nlq-visualization-updates "#ce-nlq-visualization-updates")
- [Continuing the conversation with follow-up questions](#ce-nlq-follow-up "#ce-nlq-follow-up")
- [Permissions](#ce-nlq-permissions "#ce-nlq-permissions")

## Using suggested prompts

Cost Explorer displays suggested prompts above your Cost & Usage Overview data. These prompts surface the most commonly asked cost questions, such as "Show me my top spending services this month" or "Show my projected database cost for next month." You can click any prompt to instantly receive insights from **Amazon Q Developer** without needing to type a question.

When you click a suggested prompt, the following occurs:

1. The **Amazon Q Developer** chat panel opens automatically.
2. The prompt is submitted to **Amazon Q Developer** without requiring additional input.
3. **Amazon Q Developer** generates detailed insights in the chat panel.
4. Cost Explorer refreshes with the corresponding visualization, and all report parameters including filters, groupings, and date ranges are automatically configured in the **Report Parameters** panel.

Each time you load the page or complete a query, the prompts refresh with new suggestions. When you click a prompt during a session, it is replaced with a new prompt, ensuring you always have fresh analytical options to explore. You can scroll horizontally through the prompt container to discover additional suggestions beyond those initially visible.

## Using the Ask question button

For questions that go beyond the suggested prompts, the **Ask question** button is positioned next to the suggested prompts. When you click this button, the **Amazon Q Developer** chat panel opens and you can type any cost related question in your own words, such as "What is my current month's cost and usage compared to the previous month?" or "Show me my EC2 costs broken down by instance type for the last 3 months."

**Amazon Q Developer** processes your question and delivers insights in the chat panel while determining how to display the visualization. Cost Explorer automatically updates charts and tables when analysis is based on your cost and usage data. When **Amazon Q Developer** compiles insights from additional datasets such as pricing or anomaly detection, visualizations are displayed in **Amazon Q Developer**'s new artifacts panel.

## Understanding visualization updates

When you interact with suggested prompts or the **Ask question** button, Cost Explorer automatically updates its charts and tables when the analysis is based on your cost and usage data. All corresponding report parameters, including filters, groupings, and date ranges, are visible in the **Report Parameters** panel so you can verify exactly which data subset is included in the analysis.

When **Amazon Q Developer** draws from additional datasets to provide richer analysis, visualizations are displayed in **Amazon Q Developer**'s artifacts panel alongside the chat.

After **Amazon Q Developer** updates your Cost Explorer view, you can:

- Save the view as a Cost Explorer report.
- Share the URL with colleagues. All filters are preserved in the URL.
- Bookmark the view for future reference.
- Export the data to CSV for further analysis.
- Manually adjust any of the filters and groupings in the **Report Parameters** panel to refine your view.

## Continuing the conversation with follow-up questions

After clicking a suggested prompt or asking a question using the **Ask question** button, you can continue the dialogue in **Amazon Q Developer** to drill deeper into your costs. For example, after seeing your top spending services, you might ask "Why did my RDS costs increase last month?" or "Break this down by region." **Amazon Q Developer** maintains the conversation context, allowing natural exploration of your cost data.

**Amazon Q Developer** draws from extensive knowledge beyond what is visible in your current Cost Explorer view, including pricing data, budget information, and anomaly detection data, to provide richer context and more comprehensive answers. If a follow-up question produces a visualization that Cost Explorer can display, it updates automatically. Otherwise, the visualization appears in **Amazon Q Developer**'s artifacts panel while insights continue in the chat.

## Permissions

To use the suggested prompts and **Ask question** button in Cost Explorer, you need the following permissions in addition to your existing Cost Explorer permissions:

- \***\*Amazon Q Developer** permissions\*\*: `q:StartConversation`, `q:SendMessage`
- **Pass request permission**: `q:PassRequest`, which allows **Amazon Q Developer** to call AWS APIs on your behalf

For least-privilege access, create a custom IAM policy that grants only `q:StartConversation`, `q:SendMessage`, and `q:PassRequest`. Alternatively, administrators who already use **Amazon Q Developer** across multiple integrations can use the `AmazonQFullAccess` managed policy, which includes these permissions along with broader **Amazon Q Developer** access. The integration respects all existing IAM boundaries. **Amazon Q Developer** only accesses cost data you are authorized to view through Cost Explorer.

For detailed permission configurations and security considerations, see [Security for cost management capabilities in Amazon Q Developer](ce-q-security.md "ce-q-security.md").

###### Note

Organizations can restrict access to the suggested prompts and **Ask question** button while maintaining Cost Explorer access using IAM condition keys. For more information, see the [Amazon Q Developer security documentation](../../../amazonq/latest/qdeveloper-ug/security-iam.md "../../../amazonq/latest/qdeveloper-ug/security-iam.md").
