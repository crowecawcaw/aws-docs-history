

# Definitions
<a name="definitions"></a>

 This document contains sovereignty-specific definitions and terminology used across the AWS Well-Architected Digital Sovereignty Lens pillars. Terms with established AWS definitions are linked rather than redefined. 
+  **Data residency**: The requirement of keeping data in a certain jurisdiction. 
+  **Data sovereignty**: Refers to data being subject to the laws and regulations of its physical location. This can mean data in storage, processing, or transmission, regardless of the physical location of an organization. See [What is data sovereignty](https://aws.amazon.com/what-is/data-sovereignty/) 
+  **Data classification:** In sovereign architectures, data classification drives enforcement of encryption requirements, access restrictions, geographic boundaries, and retention policies based on sensitivity level. Classification tags are the foundation for ABAC-based sovereignty controls. 
+  **Data protection authority (DPA):** Regulatory body overseeing data protection regulations within a jurisdiction (such as CNIL in France or ICO in the UK). Organizations report data breaches to the relevant DPA and may be subject to audits and enforcement actions. 
+  **Third-party risk management (TPRM):** Process of identifying, assessing, and mitigating risks associated with third-party vendors and service providers. For sovereign workloads, this verifies that vendors meet data residency requirements, have appropriate security controls, and comply with relevant regulations. 
+  **Open data formats:** Publicly documented formats readable across vendors without proprietary restrictions. For sovereign workloads, open data formats maintain data portability and avoid format lock-in that could compromise data sovereignty. 
+  **Open table formats:** Vendor-neutral table formats that enable interoperability across compute engines. For sovereign architectures, they facilitate data portability and the flexibility to change analytics tooling without compromising data residency or sovereignty requirements. 