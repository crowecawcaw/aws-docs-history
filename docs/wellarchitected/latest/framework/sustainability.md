

# Sustainability

 The discipline of sustainability addresses the long-term environmental, economic, and societal impact of your business activities. The [United Nations World Commission on Environment and Development](https://www.un.org/en/academic-impact/sustainability) defines sustainable development as "development that meets the needs of the present without compromising the ability of future generations to meet their own needs." A business can have negative environmental impacts such as direct or indirect carbon emissions, unrecyclable waste, and damage to shared resources like clean water. 

 When building cloud workloads, the practice of sustainability means understanding the impact of the services you use, quantifying that impact across the entire workload lifecycle, and applying design principles and best practices to reduce it. This pillar focuses on environmental impact, especially the energy consumption and efficiency of the resources your workloads provision, because those are the levers architects control most directly. 

 To understand where that impact is accounted for, the [Greenhouse Gas Protocol](https://ghgprotocol.org/) organizes carbon emissions into three scopes. For a cloud provider such as AWS: 
+  **Scope 1:** All direct emissions from the activities of an organization or under its control. For example, fuel combustion by data center backup generators. 
+  **Scope 2:** Indirect emissions from electricity purchased and used to power data centers and other facilities. For example, emissions from commercial power generation. 
+  **Scope 3:** All other indirect emissions from activities of an organization from sources it doesn't control. AWS examples include emissions related to data center construction, and the manufacture and transportation of IT hardware deployed in data centers. 

 From an AWS customer's perspective, the emissions from your workloads running on AWS are indirect emissions and form part of your Scope 3 total. Each workload generates a fraction of AWS emissions across those scopes, and the amount varies with the services used, the energy those services consume, the carbon intensity of the electric grids serving the data centers where they run, and the renewable energy AWS procures. 

 Sustainability in the cloud is built across four capabilities: 

## Measure sustainability
<a name="measure-sustainability"></a>
+  **Measure and monitor sustainability.** Define resource usage efficiency metrics tied to business value, combine efficiency and carbon emissions data in dashboards, and factor grid carbon intensity into where workloads run. 

## Reduce workload impact
<a name="reduce-workload-impact"></a>
+  **Optimize resource provisioning.** Provision only the resources a workload needs by making capacity follow demand, running non-production environments on demand, and reserving capacity for predictable, steady-state workloads. 
+  **Enhance workload efficiency.** Measure and remove waste continuously, flatten demand peaks for higher utilization, choose the lightest adequate computational approach, and match components to energy-efficient hardware. 
+  **Optimize data and processing.** Retain only data with business value, match file formats and compression to the access pattern, and move computation to the data rather than data to the computation. 

 Take a measured approach to building a sustainable architecture. Establish a baseline of the resources your workload provisions per unit of business value, review your choices as the AWS Cloud and its more efficient hardware and services evolve, and make deliberate trade-offs, such as relaxing a latency or availability target where the business can absorb it, to reduce the resources your workload consumes. 