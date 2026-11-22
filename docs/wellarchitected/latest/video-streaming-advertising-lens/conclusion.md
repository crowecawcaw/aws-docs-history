

# Conclusion

 This lens provided architectural guidance for designing and building efficient, cost-effective, and scalable video streaming advertising workloads in the cloud. We captured common architectures and overarching design tenets for video advertising workload needs. The lens addressed the AWS Well-Architected Framework pillars through an advertising lens, providing a set of questions and best practices to consider for new or existing workloads. 

 Applying the framework to your architecture helps you build efficient, cost-effective, and scalable video advertising systems. Key takeaways from this lens: 
+  **Latency directly affects revenue.** In real-time bidding, a bid response that arrives even a few milliseconds late misses the auction window entirely. Every architectural decision on the bid path must be evaluated against its latency impact. 
+  **Cost compounds at scale.** At millions of transactions per second, a $0.01/GB cross-AZ transfer charge becomes the largest infrastructure cost. Architecture decisions that seem minor, such as Availability Zone placement, connection pooling, and payload compression, determine profitability at advertising scale. 
+  **Privacy must be enforced in architecture, not just policy.** GDPR, CCPA, and third-party signal deprecation require privacy requirements to be enforced at the infrastructure level through service control policies, encryption key boundaries, and consent-aware data pipelines, not only through application logic that can be misconfigured. 
+  **Convergence is where the industry is heading.** Linear TV and digital advertising will operate on shared infrastructure for a decade or more. Building converged measurement, identity, and campaign management today avoids compounding technical debt from parallel systems. 
+  **Automation scales, but human judgment governs.** Agentic AI workflows can automate campaign planning, brand safety monitoring, and bid optimization at a scale no human team can match. The organizations that benefit most will be those that pair automation efficiency with well-designed human oversight at the decisions that carry the highest risk. 

 To continue improving your advertising workload architecture, use the AWS Well-Architected Tool to conduct a formal review using this lens, engage with AWS Partners with advertising industry expertise, and review the reference implementations linked in the scenario sections. 