# Plan your deployment

## Platform Foundation Cost Breakdown

**Additional monthly costs** for SageMaker Unified Studio:

| Service                  | Usage                 | Monthly Cost  | Notes                       |
| ------------------------ | --------------------- | ------------- | --------------------------- |
| SageMaker Unified Studio | 1 domain, 10 users    | $100-200      | Varies by usage             |
| Amazon DataZone          | 1 domain, 10 projects | $50           | Data catalog and governance |
| AWS Lake Formation       | Cross-region shares   | $0            | No additional charge        |
| Additional S3            | Metadata storage      | $5            | DataZone metadata           |
| **Total**                |                       | **~$155-255** | Add to solution costs       |

## Cost Scaling Factors

**Customer 360**:

- Data volume: Costs scale linearly with customer count
- Query frequency: More Athena queries = higher costs
- Quick Suite users: Each author/reader adds to monthly cost
- Bedrock usage: Token consumption varies by query complexity

**Predictive Maintenance**:

- Fleet size: Larger fleets require more Glue and SageMaker capacity
