# Customer relationship management (CRM)

AWS Managed Services (AMS) provides a customer relationship management (CRM) process to ensure that a well-defined relationship is established and maintained
with you. The foundation of this relationship is based on AMS’s insight into your business requirements.
The CRM process facilitates accurate and comprehensive understanding of:

- Your business needs and how to fill those needs
- Your capabilities and constraints
- AMS and your different responsibilities and obligations
  The CRM process allows AMS to use consistent methods to deliver services to you and provide governance
  for your relationship with AMS. The CRM process includes:

- Identifying your key stakeholders
- Establishing a governance team
- Conducting and documenting service review meetings with you
- Providing a formal service complaint procedure with an escalation procedure
- Implementing and monitoring your satisfaction and feedback process
- Managing your contract

## CRM Process

The CRM process includes these activities:

- Identifying and understanding your business processes and needs. Your agreement with AMS
  identifies your stakeholders.
- Defining the services to be provided to meet your needs and requirements.
- Meeting with you in the service review meetings to discuss any changes in the AMS service
  scope, SLA, contract, and your business needs. Interim meetings may be held with you to discuss performance,
  achievements, issues, and action plans.
- Monitoring your satisfaction by using our customer satisfaction survey and feedback given at
  meetings.
- Reporting performance on monthly internally-measured performance reports.
- Reviewing the service with you to determine opportunities for improvements. This includes
  frequent communication with you regarding the level and quality of the AMS service provided.

## CRM meetings

AMS cloud service delivery managers (CSDMs) conduct meetings with you regularly to discuss service tracks
(operations, security, and product innovations) and executive tracks
(SLA reports, satisfaction measures, and changes in your business needs).

| Meeting                         | Purpose                                                                                                                                                                                                                                                                                                                      | Mode                                    | Participants                                                                                                                                                                       |
| ------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Weekly status review (optional) | Outstanding issues or incidents, patching, security events, problem records<br>12-week operational trend (+/<br>• 6)<br>Application operator concerns<br>Weekend schedule                                                                                                                                                    | On-site customer location/Telecom/Chime | AMS: CSDM and cloud architect (CA)<br>Customer assigned team members (ex: Cloud/Infrastructure, Application Support, Architecture teams, etc.)                                     |
| Monthly business review         | Review service level performance (reports, analysis, and trends)<br>Financial analysis<br>Product roadmap<br>CSAT                                                                                                                                                                                                            | On-site customer location/Telecom/Chime | AMS: CSDM, cloud architect (CA), AMS account team, AMS<br>technical product manager (TPM) (optional), AMS OPS manager (optional)<br>You: Application Operator representative       |
| Quarterly business review       | Scorecard and service level agreement (SLA) performance and trends (6 months)<br>Upcoming 3/6/9/12 months plans/migrations<br>Risk and risk mitigations<br>Key improvement initiatives<br>Product roadmap items<br>Future direction aligned opportunities<br>Financials<br>Cost savings initiatives<br>Business optimization | On-site customer location               | AMS: CSDM, cloud architect, AMS account team, AMS service director,<br>AMS operation manager<br>You: Application operator representative, service representative, service director |

## CRM Meeting Arrangements

The AMS CSDM is responsible for documenting the meeting, including:

- Creating the agenda, including action items, issues, and list of attendees.
- Creating the list of action items reviewed at each meeting to ensure items are completed and
  resolved on schedule.
- Distributing meeting minutes and the action item list to meeting attendees by email within
  one business day after the meeting.
- Storing meeting minutes in the appropriate document repository.

In absence of the CSDM, the AMS representative leading the meeting creates and distributes minutes.

###### Note

Your CSDM works with you to establish your account governance.

## CRM monthly reports

Your AMS CSDM prepares and sends out monthly service performance presentations. The presentations include information
on the following:

- Report date
- Summary and Insights:
  - Key Call Outs: total and active stack count, stack patching status, account onboarding status
    (during onboarding only), customer-specific issues summaries
  - Performance: Stats on incident resolution, alerts, patching, requests for change (RFCs),
    service requests, and console and API availability
  - Issues, challenges, concerns, and risks: Customer-specific issues status
  - Upcoming items: Customer-specific onboarding or incident resolution plans

- Managed Resources: Graphs and pie charts of stacks
- AMS Metrics: Monitoring and event metrics, incident metrics, AMS SLA adherence metrics,
  service request metrics, change management metrics, storage metrics, continuity metrics, Trusted Advisor
  metrics, and cost summaries (presented several ways). Feature requests. Contact information.

###### Note

In addition to the described information, your CSDM also informs you of any material change in scope
or terms, including use of subcontractors by AMS for operational activities.

AMS generates reports about patching and backup that your CSDM includes in your
monthly report. As part of the report generating system, AMS adds some
infrastructure to your account that is not accessible to you:

- An S3 Bucket, with the raw data reported
- An Athena instance, with query definitions to query the data
- A Glue Crawler to read the raw data from the S3 bucket
