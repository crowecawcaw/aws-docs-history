

AWS Well-Architected Agent is in preview release and is subject to change.

# Editing goals
<a name="agent-edit-goals"></a>

**Important**  
Each profile requires at least one goal. If you delete all goals from a profile, scheduled recommendations are not generated until you add a new goal.

## Console
<a name="agent-edit-goals-console"></a>

Goals can be added either in **Agent profiles** or in the **Dashboard** for the profile.

**To add goals from the profile**

1. Choose **Agent profiles** in the left-hand navigation.

1. Choose **Actions**, then **Edit profile**.

1. In **Optimization pillars**, enter a free text goal statement for each optimization pillar you are reviewing.
**Note**  
Concrete, specific goals help AWS WA Agent prioritize and recommend actions. For example, "optimize costs" is vague, while "optimize cost of X and Y AWS service by 15%" is specific and measurable.

1. After entering goals, choose **Save**.

**To add goals from the dashboard**

1. Choose **Dashboard** in the left-hand navigation.

1. Verify that you have the correct profile selected under **Profile**.

1. On the right side of the screen, choose the **pencil icon** in **Your goals**.

1. Enter, update, or remove **Optimization pillars** and **Goal statements**.

1. Choose **Save**.

## CLI
<a name="agent-edit-goals-cli"></a>

To create a new goal:

```
aws wellarchitected create-agent-goal \
    --profile-arn "{{profile-arn}}" \
    --title "{{Reduce EC2 spend by 20%}}" \
    --pillars COST_OPTIMIZATION
```

To update an existing goal:

```
aws wellarchitected update-agent-goal \
    --profile-arn "{{profile-arn}}" \
    --goal-id "{{goal-id}}" \
    --title "{{Updated goal statement}}"
```

To delete a goal:

```
aws wellarchitected delete-agent-goal \
    --profile-arn "{{profile-arn}}" \
    --goal-id "{{goal-id}}"
```