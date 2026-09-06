

# Alignment to demand
<a name="alignment-to-demand"></a>


| CMSUS\_2: Are you scaling the infrastructure in use at edge and cloud as per workload requirements? Do you have this process under full automation?  | 
| --- | 
|   | 

**CMSUS\_BP2.1: Scale workload infrastructure dynamically** 

Use elasticity of the cloud and scale your cloud and connected devices dynamically to match supply of cloud resources to demand and avoid over-provisioned capacity in your workload. For more details, see  [SUS02-BP01](https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/sus_sus_user_a2.html) in the *Sustainability Pillar whitepaper*. 

**Prescriptive guidance:**
+  Monitor edge capacity and use onboard capability to the fullest for data processing at the edge, if possible. Make processing at the edge automated and configurable to run only required services based on the state of the vehicle (stopped or moving), and battery conditions (for EV). 


| CMSUS\_3: Are you defining SLAs as per sustainability goals in terms of what data gets transferred and processed in real time versus batch upload at a later period?   | 
| --- | 
|   | 

**CMSUS\_BP3.1: Align SLAs with sustainability goals** 

Review and optimize workload service level agreements (SLAs) based on your sustainability goals to minimize the resources required to support your workload while continuing to meet business needs. For more details, see  [SUS02-BP02](https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/sus_sus_user_a3.html) in the *Sustainability Pillar whitepaper*. 

**Prescriptive guidance:**
+  Configure workloads to send only the minimum and required dataset to the cloud using low bandwidth network. The rest of the data can move to the cloud when the edge device is connected with Wi-Fi.  
+  If it meets business requirements, get data processed at the edge itself and only send processed data to the cloud for further usage. Transform data in a human readable format at the edge itself, if possible. 