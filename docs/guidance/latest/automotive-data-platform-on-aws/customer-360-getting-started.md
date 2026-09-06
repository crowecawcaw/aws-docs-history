

# Getting started
<a name="customer-360-getting-started"></a>

Access the Customer 360 solution through Quick Suite dashboards and Bedrock agent.

## Accessing Quick Suite
<a name="accessing-quick-suite"></a>

1. Navigate to https://us-east-1.quicksight.aws.amazon.com/

1. Sign in with IAM or demo user credentials

1. Select the Customer 360 dashboard

1. Explore metrics and use AI chat for questions

## Testing the Bedrock agent
<a name="testing-the-bedrock-agent"></a>

 **Via AWS Console**: 1. Go to https://console.aws.amazon.com/bedrock/ 2. Select "Agents" → `customer-360-agent` 3. Click "Test" 4. Ask: "What’s causing declining customer sentiment?"

 **Via AWS CLI**:

```
aws bedrock-agent-runtime invoke-agent \
  --agent-id <AGENT_ID> \
  --agent-alias-id <ALIAS_ID> \
  --session-id test-1 \
  --input-text "Show me customer health trends"
```

## Next steps
<a name="next-steps"></a>
+ Configure Quick Automate workflows
+ Set up Slack and Jira integrations
+ Customize agent instructions
+ Add more playbooks to knowledge base