

# 21 – Evaluate SAP architecture patterns to improve environmental sustainability
<a name="design-principle-21"></a>

 **How do you design your SAP workload to minimize its environmental impact?** SAP architectures, as a rule, become more environmentally sustainable as underlying infrastructure footprints and energy utilization are reduced. For most cases where the SAP workload resides in AWS, this aligns with a more cost-optimized cloud infrastructure. For instance, running fewer instances with a higher utilization, as described in the [Well-Architected Framework Sustainability Pillar](https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/use-the-minimum-amount-of-hardware-to-meet-your-needs.html), is a standard method of achieving a lower-cost footprint. Business stakeholders and SAP architecture teams must keep in mind that this can require [changes in business objectives](best-practice-17-3.md) to prioritize sustainability over performance goals. In addition, stakeholders should encourage the adoption of iterative code development practices that optimize for energy efficiency over time.  


|   **ID**   |   **Priority**   |   **Best Practice**   | 
| --- | --- | --- | 
| ☐ BP 21.1 |  Required  |  Understand business requirements to make sustainability-centric design decisions  | 
| ☐ BP 21.2 |  Required  |  Implement sustainability improvements for infrastructure and SAP  | 
| ☐ BP 21.3 |  Required  |  Implement sustainability monitoring for infrastructure and SAP  | 
+  SAP Lens [Cost Optimization]: [Best Practice 17.3 – Understand business requirements to make cost-optimized design decisions per environment](best-practice-17-3.md) 
+  Well-Architected Framework [Sustainability]: [Use the minimum amount of hardware to meet your needs](https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/use-the-minimum-amount-of-hardware-to-meet-your-needs.html) 
+  Well-Architected Framework [Sustainability]: [Development and deployment process](https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/development-and-deployment-process.html) 