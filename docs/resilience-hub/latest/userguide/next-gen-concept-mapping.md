

# Concept mapping: AWS Resilience Hub v1 to Next generation Resilience Hub
<a name="next-gen-concept-mapping"></a>

The following table maps concepts from AWS Resilience Hub v1 to their equivalents in the next generation of Resilience Hub.


| AWS Resilience Hub v1 concept | Next generation Resilience Hub concept | Notes | 
| --- | --- | --- | 
| Application | Service | Your v1 "application" becomes a the next generation of Resilience Hub "service" – the primary unit of assessment | 
| Resilience checks | Failure mode assessment findings | Static checks replaced by GenAI-powered findings with reasoning | 
| Application assessment | Service failure mode assessment | Same concept, now at service level with richer output | 
| Assessment policy (RTO/RPO) | Resilience policy (modular) | Policies are now composable: DR \+ Availability SLO \+ Data recovery | 
| Application (as grouping) | System \+ User journeys | The "grouping" aspect of applications maps to systems and user journeys | 
| – (not available) | Dependency discovery | New capability in the next generation of Resilience Hub | 
| – (not available) | Service functions | Technical workflows within a service; new in the next generation of Resilience Hub | 