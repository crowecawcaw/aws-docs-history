# Preventing future incidents

AWS DevOps Agent analyzes patterns across your incident investigations to deliver targeted recommendations that continuously improve your operational posture and prevent future incidents. Access the Prevention feature through the Prevention page in the Operator Web App.

## How prevention works

AWS DevOps Agent evaluates recent incident investigations to identify lasting improvements to prevent future incidents and quicken the mean time to detection (MTTD). The agent analyzes multiple incidents to identify recommendations that may prevent whole classes of incidents in the future, focusing on the most impactful recommendations to ensure they are actionable.

The agent automatically runs evaluations weekly. You can also manually trigger an evaluation at any time, which is useful when a recent investigation warrants a quick turnaround on recommended improvements.

The agent identifies improvements across four areas:

- **Observability posture** – Recommendations to enhance monitoring, alerting, and logging capabilities to detect issues quicker and more accurately.
- **Testing gaps** – Recommendations to strengthen testing and validation processes in your deployment pipelines.
- **Code changes** – Recommendations to better improve resilience and performance.
- **Infrastructure architecture** – Recommendations to optimize resource configurations, implement autoscaling, and improve system resilience.

## Benefits

- **Prevent recurring incidents** – Address root causes systematically rather than repeatedly responding to the same types of issues
- **Reduce operational toil** – Free your team from repetitive firefighting to focus on innovation and strategic improvements
- **Improve system resilience** – Strengthen your infrastructure, observability, and deployment processes based on real incident data
- **Learn from historical patterns** – Leverage insights from past incidents to make targeted improvements that have the greatest impact

## Agent summary

The Agent Summary in the Prevention page of the Web App provides a description of the outcomes from the last evaluation of recent incidents. The summary explains the number of incident investigations analyzed, which incidents are similar to past ones, and which recommendations were created or updated with new information.

The summary helps you quickly understand what the agent discovered during its most recent evaluation and highlights the most notable recommendations that could have the greatest impact on your operational posture.

## Recommendation categorization

The Recommendation Categorization chart shows the distribution of recommendations across four key categories:

- **Code optimization** – Recommendations to improve application code quality, performance, and error handling.
- **Observability** – Recommendations to enhance monitoring, alerting, logging, and system visibility.
- **Infrastructure** – Recommendations to optimize resource configurations, capacity tuning, and architectural resilience.
- **Governance** – Recommendations to strengthen deployment processes, testing practices, and operational controls.

This categorization helps you understand where your operational improvements are most needed and allows you to prioritize recommendations based on your team's focus areas.

## Controlling evaluations

You can control when AWS DevOps Agent evaluates incidents and generates recommendations:

- **Running evaluations manually** – Click the **Run Now** button in the Prevention page to start an evaluation immediately. This is useful when a recent investigation warrants a quick turnaround on recommended improvements.
- **Stopping active evaluations** – Click the **Stop Evaluation** button in the Prevention page to halt an evaluation that is currently in progress.

## Managing recommendations

AWS DevOps Agent provides recommendations in the Prevention page where you can review and manage them:

- **Viewing recommendation details** – Click on a recommendation to open the recommendation details page, where you can see more information about the suggested improvement including the incidents that informed the recommendation, the expected impacts, and next steps.
- **Accepting recommendations** – To accept a recommendation, click ‘Accept’ in the recommendation table. When you accept a recommendation, it remains in the recommendation table for tracking. This allows you to monitor which improvements you plan to implement and track their progress.
- **Rejecting recommendations** – To reject a recommendation, click ‘Reject’ in the recommendation table. When you reject a recommendation, you can provide a natural language explanation of why it doesn't meet your needs. The agent learns from this feedback and uses it to inform future recommendations, ensuring they become more aligned with your operational priorities and requirements over time.
- **Automatic removal** – Recommendations that are not accepted may be removed after approximately 6 weeks if no new incidents would have been prevented by implementing the recommendation. This ensures the Prevention page focuses on the most relevant improvements for your operational challenges.
- **Recommendation updates** – Existing recommendations are updated when newer incidents are found that would have been prevented by the recommendation. Updates may change the recommendation's priority or refine the recommendation based on new insights.

## Implementing recommendations

To maximize the value of Prevention recommendations, consider the following practices for acting on them:

- **Adding recommendations to your ticket backlog** – Copy accepted recommendations to your team's ticketing system or project management tool to ensure they are prioritized alongside other engineering work.
- **Prioritizing recommendations based on impact** – Focus first on recommendations that address the most frequent or severe incident types, or those that affect critical systems.
- **Tracking implementation progress** – Monitor which recommendations have been implemented and measure their effectiveness by observing whether similar incidents decrease over time.
- **Coordinating with development teams** – Share recommendations with the appropriate teams who own the affected systems, ensuring they have the context and resources needed to implement improvements.
