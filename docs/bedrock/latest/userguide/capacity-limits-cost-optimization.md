# Capacity, Limits, and Cost Optimization

Amazon Bedrock offers flexible capacity options to match your workload requirements and budget. Understanding the differences between on-demand tiers (Flex, Priority, Standard), reserved tier, batch processing, and cross-region inference helps you optimize both performance and cost.

## Capacity Options

| Capacity Type          | Use Case                                   | Key Characteristics                                                                                           |
| ---------------------- | ------------------------------------------ | ------------------------------------------------------------------------------------------------------------- |
| On-Demand: Flex        | Sporadic, low-volume workloads             | • Lowest cost per token<br>• Best-effort availability<br>• May experience throttling<br>• No SLA              |
| On-Demand: Standard    | Regular production workloads               | • Balanced cost and performance<br>• Moderate throughput guarantees<br>• Standard SLA<br>• Most common choice |
| On-Demand: Priority    | High-priority, latency-sensitive apps      | • Highest on-demand cost<br>• Premium throughput allocation<br>• Enhanced SLA<br>• Reduced throttling risk    |
| Reserved Tier          | Consistent, high-volume workloads          | • Reserved model units<br>• Guaranteed capacity<br>• 1 or 6 month commitments<br>• Predictable performance    |
| Batch                  | Large-scale, non-time-sensitive processing | • 50% cost savings vs on-demand<br>• 24-hour processing window<br>• Ideal for bulk inference                  |
| Cross-Region Inference | High availability, traffic bursting        | • Automatic failover<br>• Route to less-busy regions<br>• Improved uptime<br>• Uses on-demand pricing         |

## Limits & Quotas

### On-Demand Limits (by tier)

| Tier     | RPM Range | TPM Range  | Throttling Risk |
| -------- | --------- | ---------- | --------------- |
| Flex     | 10-100    | 5K-50K     | High            |
| Standard | 100-500   | 50K-150K   | Medium          |
| Priority | 500-1000+ | 150K-300K+ | Low             |

- Burst capacity: Available across all tiers for short spikes
- Soft limits: Increasable via service quota requests
- Model-specific: Actual limits vary by foundation model

### Reserved Tier Limits

- Minimum commitment: 1 model unit
- Maximum units: Account and region-specific
- Input/output token limits: Based on purchased units
- No RPM throttling within purchased capacity

### Batch Processing Limits

- Job size: Up to 10,000 records per batch
- File size: Maximum 200 MB input file
- Processing time: 24-hour completion window
- Concurrent jobs: Region-specific quotas

### Cross-Region Inference

- Inherits on-demand tier limits per region
- No additional quota overhead
- Automatic routing (no manual limit management)

## Cost Optimization

### Decision Framework

| Scenario                  | Recommended Option     | Why                                        |
| ------------------------- | ---------------------- | ------------------------------------------ |
| Development/testing       | Flex                   | Lowest cost, acceptable for non-production |
| Standard production       | Standard               | Best cost-performance balance              |
| Critical user-facing apps | Priority               | Reliability and performance over cost      |
| Steady high-volume load   | Reserved Tier          | 30-50% savings with commitment             |
| Bulk data processing      | Batch                  | 50% discount, non-urgent workloads         |
| Mission-critical uptime   | Cross-Region Inference | Availability > cost                        |

### Optimization Strategies

**Choose the Right On-Demand Tier**

- Start with Standard for most workloads
- Downgrade to Flex for dev/test environments
- Upgrade to Priority only when throttling impacts users
- Monitor CloudWatch throttle metrics to inform decisions

**Transition to Reserved Tier**

- When consistent load exceeds 40% of on-demand costs
- Calculate break-even: (Monthly on-demand cost) vs (Reserved commitment)
- Use 1-month commitment initially
- Reserved tier can work alongside any on-demand tier

**Leverage Batch for**

- Training data generation
- Content moderation backlogs
- Report generation
- Data enrichment pipelines

**Combine Approaches**

- Reserved tier for baseline traffic
- Standard on-demand for moderate bursts
- Priority on-demand for critical peak periods
- Batch for offline processing
- Cross-region for failover only

**Cost Monitoring**

- Compare tier costs: Flex < Standard < Priority
- Track tokens per request (optimize prompts)
- Use CloudWatch metrics for utilization and throttling
- Set billing alarms for unexpected spikes
- Review reserved tier utilization monthly
- Evaluate tier upgrades only when throttling occurs
