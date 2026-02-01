# Optimize over time

You can optimize cost over time by reviewing new services and implementing them in your
workload. As AWS releases new services and features, it is a best practice to review your
existing architectural decisions to ensure that they remain cost effective. As your
requirements change, be aggressive in decommissioning resources, components, and workloads
that you no longer require. Consider the following best practices to help you optimize over
time. While optimizing your workloads over time and improving your [CFM](../cost-optimization-pillar/practice-cloud-financial-management.md "../cost-optimization-pillar/practice-cloud-financial-management.md") culture in your organization, evaluate
the cost

of effort for operations in the cloud, review your time-consuming cloud operations, and
automate them to reduce human efforts and cost by adopting related AWS services, third-party
products, or custom tools (like [AWS CLI](https://aws.amazon.com/cli/ "https://aws.amazon.com/cli/") or [AWS SDKs](https://aws.amazon.com/developer/tools/ "https://aws.amazon.com/developer/tools/")).

**Optimize over time**

Establish a quarterly generative AI cost optimization cadence that includes:

- Re-running evaluation benchmarks to validate model price-performance ratios
- Re-ranking models by business criticality and cost per task
- Tuning RAG caches and vector retrieval thresholds
- Pruning inactive embeddings or knowledge bases to reduce silent storage growth
- Archiving old fine-tuning artifacts to lower storage and inference costs
  This helps your generative AI workloads evolve with business demand, maintain cost
  efficiency, and prevent silent spend creep over time.

###### Best practice questions

- [FSICOST15: Have you reviewed your ongoing cost structure
  tradeoffs for your current AWS services lately?](fsicost15.md "fsicost15.md")
- [FSICOST16: Are you continuously assessing the ongoing costs and
  usage of your cloud implementations?](fsicost16.md "fsicost16.md")
- [FSICOST17: Are you continually reviewing your workload to
  provide the most cost-effective resources?](fsicost17.md "fsicost17.md")
- [FSICOST18: Do you have specific workload modernization or
  refactoring goals in your cloud strategy?](fsicost18.md "fsicost18.md")
- [FSICOST19: Do you use the cloud to drive innovation and
  operational excellence of your business model to impact both the top and bottom
  line?](fsicost19.md "fsicost19.md")
