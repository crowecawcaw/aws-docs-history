

# Bedrock AI Agent
<a name="customer-360-bedrock-agent"></a>

The Bedrock AI Agent provides conversational analytics with natural language queries and AI-powered recommendations.

## Building the knowledge base
<a name="building-the-knowledge-base"></a>

The knowledge base stores remediation playbooks as vector embeddings for semantic search.

### Aurora PostgreSQL with pgvector
<a name="aurora-postgresql-with-pgvector"></a>

 **Cluster configuration**: \* Engine: Aurora PostgreSQL 15.4 \* Instance: db.r6g.large (Graviton3) \* Scaling: Serverless v2 (0.5-2 ACUs) \* Multi-AZ: Enabled \* Encryption: KMS at rest, TLS in transit

 **Vector table schema**:

```
CREATE EXTENSION vector;
CREATE SCHEMA bedrock_integration;
CREATE TABLE bedrock_integration.bedrock_kb (
    id UUID PRIMARY KEY,
    embedding vector(1536),
    chunks TEXT,
    metadata JSONB
);
CREATE INDEX ON bedrock_integration.bedrock_kb
USING hnsw (embedding vector_cosine_ops);
```

### Knowledge base content
<a name="knowledge-base-content"></a>

 **Battery remediation playbook**: \* Supplier batch defects \* Thermal management issues \* BMS failures \* Charging problems \* Success rates and timelines

 **Customer churn analysis playbook**: \* Churn risk factors \* Retention strategies by segment \* Proactive engagement tactics \* Win-back campaigns \* ROI calculations

 **Analytics metadata guide**: \* Data schema and tables \* KPI calculations \* Metric thresholds \* Query examples \* Dashboard interpretation

### Document format
<a name="document-format"></a>

Documents stored as markdown for rich context:

```
## Supplier Batch Defect Issues

### Early Battery Health Degradation

**Symptoms:**
- Battery health < 80% within 12 months
- Q2 2024 production batches
- Premium segment concentration

**Severity:** Critical

**Root Cause:**
Supplier defect in thermal management affecting 12,000 vehicles

**Recommended Action:**
1. Proactive battery replacement
2. Customer notification within 48 hours
3. Priority scheduling
4. Loaner vehicle provision

**Success Metrics:**
- Success Rate: 94%
- Resolution Time: 5 days
- Revenue Recovery: 87%
- Satisfaction: 4.2/5.0
```

### Knowledge base ingestion
<a name="knowledge-base-ingestion"></a>

To populate the knowledge base, documents are uploaded to S3 and an ingestion job is started:

```
# Upload playbook documents
aws s3 sync source/knowledge-base/ \
  s3://cx360-knowledge-base-<ACCOUNT-ID>/docs/

# Start ingestion job
aws bedrock-agent start-ingestion-job \
  --knowledge-base-id <KB_ID> \
  --data-source-id <DS_ID>
```

### Chunking strategy
<a name="chunking-strategy"></a>

 **Document chunking configuration**: \* 500 tokens per chunk \* 50 token overlap \* Keep related info together \* Use markdown structure

These parameters balance retrieval precision with context completeness. A 500-token chunk is large enough to include the full context of a remediation step (symptom, root cause, recommended action, success metrics) without splitting related content across chunks. The 50-token overlap ensures that sentences near chunk boundaries appear in adjacent chunks, preventing retrieval gaps when a query matches content that spans a boundary.

## Building action groups
<a name="building-action-groups"></a>

Action groups enable the agent to query real-time customer data.

### Action group 1: Query customer health
<a name="action-group-1-query-customer-health"></a>

 **Purpose**: Retrieve health scores, churn risk, lifetime value

 **Lambda function**:

```
def query_customer_health(params):
    min_score = params.get('min_score', '0')
    max_score = params.get('max_score', '100')

    query = f"""
    SELECT customer_id, health_score, churn_probability
    FROM {GLUE_DATABASE}.customer_health
    WHERE health_score BETWEEN {min_score} AND {max_score}
    ORDER BY health_score ASC
    LIMIT 100
    """

    results = execute_athena_query(query)
    return {'customers': results}
```

### Action group 2: Query at-risk revenue
<a name="action-group-2-query-at-risk-revenue"></a>

 **Purpose**: Calculate revenue at risk by segment

```
def query_at_risk_customers(params):
    segment = params.get('segment', 'all')

    query = f"""
    SELECT customer_type, at_risk_revenue, at_risk_customers
    FROM {GLUE_DATABASE}.at_risk_revenue_view
    WHERE month_date = (SELECT MAX(month_date)
                        FROM at_risk_revenue_view)
    """

    results = execute_athena_query(query)
    return {'segments': results}
```

### Action group 3: Query sentiment trends
<a name="action-group-3-query-sentiment-trends"></a>

 **Purpose**: Analyze sentiment and NPS trends

```
def query_customer_trends(params):
    months = params.get('months', '12')

    query = f"""
    SELECT month_label, nps_score, health_score
    FROM {GLUE_DATABASE}.kpi_trends
    ORDER BY month_date DESC
    LIMIT {months}
    """

    results = execute_athena_query(query)
    return {'trends': results}
```

## Configuring the Bedrock agent
<a name="configuring-the-bedrock-agent"></a>

The agent orchestrates knowledge base retrieval and action group execution.

### Agent configuration
<a name="agent-configuration"></a>

 **Foundation model**: Claude 3.5 Sonnet v2

 **Agent instructions**:

```
You are a customer analytics expert helping automotive teams
understand customer sentiment, health trends, and churn risk.

Your capabilities:
1. Query customer data using action groups
2. Retrieve remediation playbooks from knowledge base
3. Analyze trends and identify root causes
4. Provide actionable recommendations

Guidelines:
- Always cite data sources
- Include specific metrics
- Reference relevant playbooks
- Prioritize by revenue impact
- Be concise but thorough
```

### Adding knowledge base
<a name="adding-knowledge-base"></a>

```
aws bedrock-agent associate-agent-knowledge-base \
  --agent-id <AGENT_ID> \
  --knowledge-base-id <KB_ID> \
  --description "Customer remediation playbooks"
```

### Adding action groups
<a name="adding-action-groups"></a>

```
aws bedrock-agent create-agent-action-group \
  --agent-id <AGENT_ID> \
  --action-group-name query-customer-health \
  --action-group-executor '{"lambda": "<LAMBDA_ARN>"}'
```

### Configuring guardrails
<a name="configuring-guardrails"></a>

 **PII filtering**:

```
aws bedrock create-guardrail \
  --name customer-360-guardrail \
  --sensitive-information-policy-config '{
    "piiEntitiesConfig": [
      {"type": "EMAIL", "action": "BLOCK"},
      {"type": "PHONE", "action": "BLOCK"},
      {"type": "SSN", "action": "BLOCK"}
    ]
  }'
```

## Using the AI agent
<a name="using-the-ai-agent"></a>

The agent provides conversational analytics through natural language.

### Example conversation: Declining sentiment
<a name="example-conversation-declining-sentiment"></a>

```
User: "What's causing declining customer sentiment?"

Agent: Based on analysis of the past 12 months:

**Trend Analysis:**
- NPS declined from 52 to 42 (19% decrease)
- Health scores dropped from 65 to 56 (14% decrease)
- At-risk customers increased 73%

**Root Cause:**
Battery issues increased from 15% to 40% of cases,
primarily affecting premium segment (12,450 customers).

**Revenue Impact:**
$2.3M at risk from premium customers.

**Recommended Actions:**
From Battery Remediation Playbook:

1. **Proactive Battery Replacement**
   - Success Rate: 94%
   - Resolution Time: 5 days
   - Customer Satisfaction: 4.2/5.0

2. **Customer Communication Campaign**
   - Notify within 48 hours
   - Priority scheduling
   - Expected recovery: 87%

[Citations: Battery Remediation Playbook, KPI Trends]
```

### Example conversation: Segment analysis
<a name="example-conversation-segment-analysis"></a>

```
User: "Which customer segments are at highest risk?"

Agent: Analyzing at-risk revenue by segment:

**Premium Segment** (Highest Risk)
- At-Risk Revenue: $1.8M
- At-Risk Customers: 3,200
- Avg Lifetime Value: $85K
- Primary Issue: Battery degradation

**Standard Segment** (Medium Risk)
- At-Risk Revenue: $450K
- At-Risk Customers: 8,100
- Avg Lifetime Value: $42K
- Primary Issue: Service quality

**Recommendation:**
Focus on premium segment first due to highest
revenue impact and clear remediation path.

[Citations: At-Risk Revenue View, Customer Health]
```

## Optimization and best practices
<a name="optimization-and-best-practices"></a>

### Agent instruction tuning
<a name="agent-instruction-tuning"></a>

 **Iterative improvement**: 1. Test with common questions 2. Review response quality 3. Refine instructions for clarity 4. Add examples for complex scenarios 5. Test edge cases

 **Instruction patterns**:

```
# Good: Specific and actionable
"When analyzing declining metrics, always:
1. Query the last 12 months
2. Calculate month-over-month changes
3. Identify top 3 factors
4. Cite specific data points"

# Bad: Vague
"Analyze the data and provide insights"
```

### Knowledge base optimization
<a name="knowledge-base-optimization"></a>

 **Document quality**: \* Use clear section headers \* Include specific metrics \* Add real-world examples \* Update regularly \* Remove outdated information

 **Chunking strategy**: \* 500 tokens per chunk \* 50 token overlap \* Keep related info together \* Use markdown structure

### Cost optimization
<a name="cost-optimization"></a>

 **Estimated monthly costs** (us-east-1 region):


| Service | Usage | Monthly Cost | Notes | 
| --- | --- | --- | --- | 
| Amazon Aurora Serverless v2 | 0.5-2 ACU, pgvector | $45-90 | Auto-pause after 5 min idle | 
| Amazon Bedrock (Claude Sonnet) | 1,000 queries/mo, \~2K tokens avg | $30-60 | Input \~$0.003/1K, Output \~$0.015/1K | 
| Amazon Bedrock (Titan Embeddings) | 500K embeddings | $5 | KB sync and retrieval | 
| Amazon QuickSight Enterprise | 1 author \+ 5 readers | $67 | $24/author \+ $5/reader \+ SPICE | 
| Amazon Athena | 100 GB scanned/mo | $0.50 | $5/TB, partitioned tables reduce cost | 
| AWS Glue ETL | 2 DPU, 10 runs/mo | $9 | Crawler \+ ETL jobs | 
| Amazon S3 | 10 GB data lake | $0.25 | 11 datasets \+ synthetic data | 
| AWS Lambda | 5,000 invocations | $1 | Agent tool executor | 
|  **Total**  |  |  **\~$160-235**  | Scales with query volume | 

 **Cost optimization tips**:

 **Aurora Serverless**: \* Auto-pause after 5 minutes idle \* Min ACU: 0.5, Max: 2 \* Use read replicas only if needed

 **Bedrock costs**: \* Input tokens: \~$0.003 per 1K \* Output tokens: \~$0.015 per 1K \* Embeddings: \~$0.0001 per 1K \* Optimize prompt length

 **Athena costs**: \* $5 per TB scanned \* Use partitioned tables \* Leverage views \* Set result limits