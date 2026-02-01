# Scenarios

Digital sovereignty encompasses the principles and practices that customers use to maintain
control over their data, infrastructure, and operations within specific jurisdictions. The
following scenarios represent common situations where digital sovereignty requirements apply.
Review these scenarios to identify which are relevant to your organization or solution.

1. **Design and develop nationally-critical digital
   infrastructure:** Digital infrastructure serving the daily needs of citizens must
   be secure, resilient, and highly available. Examples include digital payment platforms,
   border control systems, securities and commodities trading platforms, healthcare systems,
   and other public service platforms.

Disruptions to nationally important infrastructure can cause significant inconvenience
to citizens. When designing and developing these workloads, consider the _three
Cs_: compliance, control, and continuity. First, identify and baseline your
regulatory requirements. Second, implement necessary controls to protect personally
identifiable information (PII) and protected health information (PHI). Third, define the
minimum restorable service levels needed to maintain business continuity. These measures
support both regulatory adherence and reliable service delivery. 2. **Set up and operate workloads in new jurisdictions:**
Businesses expand their global footprint by launching new digital products worldwide. These
products require adaptation to meet regional regulatory standards, data protection
requirements, and adhere to cultural sensitivities.

Consider setting up self-sufficient engineering teams in each jurisdiction. These teams
should manage their own infrastructure, avoiding the need for cross-border remote access.
Recruit talent from the target jurisdiction, as these professionals bring insights into
local customs and regulations. Partner with regional legal and privacy experts to improve
compliance with jurisdiction-specific requirements. 3. **Protect citizens' data by complying with local data export controls
and privacy legislations:** Sovereign nations own citizens' data. Businesses
collecting personal data must comply with regional data privacy legislations and only allow
authorized cross-border data transfers.

Handling PII and PHI requires careful planning. Define trust boundaries and authorize
and record data transfers across your trust boundaries. Protect data at rest and in transit,
and apply supplemental measures if required. Apply [privacy by design](../../../whitepapers/latest/navigating-gdpr-compliance/data-protection-by-design-by-default.md "../../../whitepapers/latest/navigating-gdpr-compliance/data-protection-by-design-by-default.md") principles to manage data at scale. Create a culture of
compliance within the organization and be consistently ready for audits.

Every jurisdiction has explicit controls over export of data. However, some
jurisdictions allow data to be exported using bi-lateral adequacy arrangements or similar
mechanisms. Read the [Navigating GDPR Compliance on AWS](../../../whitepapers/latest/navigating-gdpr-compliance/general-data-protection-regulation-overview.md "../../../whitepapers/latest/navigating-gdpr-compliance/general-data-protection-regulation-overview.md") to understand your options regarding data
transfer between the European Union (EU) to the United States (US). 4. **Restrict who can provide operational support, to what extent, and from
where:** Allow only authorized personnel, resident within specific geographies
and subject to local laws, to provide operational support.

Providing operational support from approved locations can improve your compliance
posture in relation to regional data privacy laws and related data export controls. Build a
strong identity foundation and apply principles of least privilege. Decide who needs to
access what, why do they need it, from where, and for how long.

Understand residency and citizenship requirements, audit standards, and other legal and
economic implications involving the location of your support center and staff. Regularly
review and update access policies based on changing requirements and in compliance with
local laws. 5. **Reduce the impact of unexpected disruptions:** Assess
potential impacts of reduced access to critical software and services, physical
infrastructure, and technical skills required to support your digital footprint. Create
resiliency and continuity plans to protect against disruptions from international trade
disputes, intellectual-property right conflicts, and unforeseen geopolitical events.

Consider where you want your disaster recovery (DR) site to be located. Your DR plan
must support business continuity when faced with disruptions brought about by regional wars
and conflicts, power grid failures, network outages, cybersecurity issues, and
climate-related events.

Consider aligning with open source technologies, open standards (publicly available
specifications free from proprietary restrictions), and open data formats to enhance
portability and interoperability options. Build abstractions into your code and
configurations to deploy workloads consistently across AWS Regions, AWS edge locations,
or other managed infrastructure. This approach reduces significant rework if you need to
replace dependencies. Alternatively, use infrastructure-agnostic independent software vendor
(ISV) solutions to gain more independence and flexibility when porting workloads to
different environments. 6. **Align with policy-led technology initiatives:** Nations
aspire to be self-sufficient by supporting and nurturing a thriving landscape of local
technology providers. This creates more choice and competition in the market, creating room
for innovation and stimulates local economic growth. However, some nations or their
designated regulators may mandate the use of domestically developed technology stacks to
accelerate this process.

Follow regulatory mandates and align with national and regional policy initiatives.
Engage with regulators and policy makers to understand the long and mid-term approach of
putting their decisions into practice. 7. **Navigate data disclosure requests:** Organizations are often
required to assist law enforcement agencies to disclose information related to subjects of
interests. Data disclosure requests may originate from local as well as foreign enforcement
agencies.

Develop a formal process to accept and track data disclosure requests using secure
digital channels. Based on the request, derive the minimum amount of data required to comply
with an order, the most secure method of data transfer, and the timelines involved. Work
with your technology service providers and delegate their share of responsibilities. 8. **Implement new technology through digital sovereignty
initiatives:** Find ways of taking advantage of emerging technology without
compromising on sovereign controls. Organizations that fully grasp sovereignty-related
requirements can enter new regulated markets with confidence, build customer trust, adapt
quickly to changing regulatory landscapes, and maintain operational resilience when faced
with unforeseen disruptions.

Consider setting up a center of excellence (CoE) or a _practice
area_ to address sovereignty-related requirements and challenges. Include
experts from legal, technical, compliance, and security domains. A digital sovereignty
practice must be equipped to handle multidisciplinary challenges and respond in a variety of
ways, not just with technical solutions.
