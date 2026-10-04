

AWS Well-Architected Agent is in preview release and is subject to change.

# Filter recommendations in AWS Well-Architected Agent
<a name="agent-filter-rec"></a>

Use filters to narrow down recommendations based on specific criteria to focus on the most relevant optimizations for your environment and priorities.

## Console
<a name="agent-filter-rec-console"></a>

The Filters panel on the left side of the dashboard allows you to refine recommendations by:
+ **Type:** Application, Architecture, or Resource-level recommendations
+ **Pillars:** Cost Optimization, Security, Resilience, or Performance
+ **Effort:** Small, Medium, or Large effort to fix
+ **Impact:** High, Medium, or Low impact fixes
+ **Services:** Select services from the list

You can select multiple filter criteria simultaneously. The **Clear filters** button removes all applied filters to return to the full recommendations view.

You can use the search bar to find a specific recommendation using keywords or recommendation names.

## CLI
<a name="agent-filter-rec-cli"></a>

To filter recommendations by state (open or closed):

```
aws wellarchitected list-agent-recommendations \
    --profile-arn "{{arn:aws:wellarchitected:us-east-1:111122223333:agent-profile/my-profile}}" \
    --state OPEN
```

To filter by pillar:

```
aws wellarchitected list-agent-recommendations \
    --profile-arn "{{arn:aws:wellarchitected:us-east-1:111122223333:agent-profile/my-profile}}" \
    --pillar COST_OPTIMIZATION
```