# Planned event management in AWS Managed Services

AWS Managed Services (AMS) planned event management (PEM) is an AMS service offering. PEM
engages, coordinates, and assists during customer events and projects using AMS services. PEM assists in coordinating a set of related RFCs that align with the agreed scope and timeline of the PEM event or project.

## AMS PEM criteria

A planned event is a scope-bound and time-bound project. AMS uses details that you provide (including plan and scope, expected outcomes, and changes that AMS operations are expected to perform) to effectively support you during PEM activity. Your Cloud Architects (CAs) then review and assess the PEM activity for completeness, technical implementation, and AMS operations engagement. After CA review, AMS operations reviews the plans and coordinates with your cloud service delivery manager (CSDM) for operations team engagement.

## Types of PEM

The following are the available PEM types:

- **Gamedays**
  - **Operational Gameday:** A scenario-based gaming approach to operational response, aimed at validating the integration of processes, people, and systems.
  - **Security Gameday:** A security incident response strategy that employs a scenario-based gaming approach to assess the integration of systems, processes, and personnel.

- **BYOEPS:** Use the AMS "bring your own endpoint security" (BYOEPS) feature to substitute the default Trend Micro Deep Security agent with your preferred endpoint security solution or a custom Trend Micro license. For more information, see [AMS bring your own EPS](ams-byoeps.md "ams-byoeps.md").
- **Disaster Recovery:** Disaster Recovery events involve AMS assisting you during your planned DR activities. For more information, see [Disaster recovery planning](ams-disaster-recovery.md "ams-disaster-recovery.md").
- **Customer Security Event:** Planned security events. For example, root user activity and penetration testing.
- **Migration Support:** Support for planned onboarding and migration activity.

This workflow facilitates collaboration with AMS for coordinating planned events and migration activities regarding AMS support. For priority execution of RFCs, it's a best practice to use the Operations on Demand (OOD) engagement. For more information, see [Operations On Demand](ops-on-demand.md "ops-on-demand.md").

## The AMS PEM process

The PEM process consists of the following phases:

- **PEM initiation:** You work with your CSDM to define your objective for the planned event and determine what's needed from AMS Operations. AMS CAs review the technical aspects of the PEM plan. The CAs work with AMS Security and Operations on compliance, execution optimization and automation, and to define pre-PEM execution tasks and deliverables. Then, your CSDM creates the PEM ticket and provides AMS with the project information and technical details. AMS requires a lead time of 14 calendar days to allow the AMS Operations team time to plan, provide technical review, and assign resources.
- **PEM review:** The AMS Operations team reviews the PEM request and works with your CSDM to verify that the information in the PEM plan is correct and complete.
- **PEM acceptance:** AMS reviews the provided information and communicates to the CSDM what the level of support will be during the PEM activity. If the PEM contains complete information and your CSDM agrees with the scope of work, then the PEM is approved.
- **Readiness and execution:** AMS makes sure that
  tasks needed before the PEM begins are completed and facilitates internal and customer communications. AMS
  makes sure that the PEM plan runs correctly and provides status and
  progress reporting.

## PEM FAQs

**How do I engage AMS with a RFC/Service Request (SR) during a PEM event?**

- Use the PEM ID shared by your CSDM in the RFC/SR subject line in the format `PEM-ID`.
- You can also create a Service Request (SR) to discuss your use cases or for questions about your planned event. If you use an SR, then the PEM doesn't have to be valid.

**What validations are performed when a PEM-related RFC is submitted?**

- Verification that the Account ID is listed on the PEM.
- Verification that the PEM status is approved and active between the provided start and end dates.

**Are there SLAs or SLOs for PEM requests?**

- PEMs are not associated with SLAs or SLOs.
- SLAs and SLOs for PEM-related work items (RFC/Service Request) are defined by AMS SLOs.

For more information, see [AMS service level objectives (SLOs)](apx-slo.md "apx-slo.md").

**Can we create a PEM through a Service Request (SR)?**

- No, PEM creation must be managed by the Cloud Service Delivery Manager (CSDM).
