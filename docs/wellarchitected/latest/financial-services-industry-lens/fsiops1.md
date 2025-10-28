# FSIOPS1: Have you defined risk management roles for the cloud?

Financial institutions typically adopt a Three Lines of Defense model to improve effectiveness of risk management. The second and third lines of defense must have the appropriate skills and training necessary to understand the risks involved in the delivery of business services using cloud - services owned and managed by the first line. Establish clear roles and responsibilities both within and across the three lines of defense's functions to verify the effectiveness and auditability of the cloud operating model. Reassess these roles and responsibilities at regular intervals to keep the governance model efficient and effective.

## FSIOPS01-BP01 Define roles and responsibilities across risk functions

As explained in the preceding general design principles section, financial
institutions typically adopt a Three Lines of Defense model to improve effectiveness of
risk management. The second and third lines of defense must have the appropriate skills
and training necessary to understand the risks involved in the delivery of business
services using the cloud (services owned and managed by the first line). Clear roles and
responsibilities need to be established both within and across the three lines of
defense's functions to verify the effectiveness and auditability of the cloud operating
model. These roles and responsibilities must be reassessed at regular intervals to keep
the governance model efficient and effective.

### Prescriptive guidance

The roles and responsibilities of each of the three lines of defense should be
clearly communicated and understood. Publishing a RACI (Responsible, Accountable,
Consulted, Informed) matrix on an intranet or wiki page is a good way to reduce
misunderstandings about which role owns each activity. Periodic review of these roles
and responsibilities should occur more frequently immediately after they are defined
or dramatically changed, and can be less frequent otherwise. The people who fill roles
within the three lines of defense should be documented as well, and membership in
these roles should require a standard level of training in order to consistently
handle risk management.

## FSIOPS01-BP02 Engage with your risk management and internal audit functions to

implement a process for the approval of cloud risk controls

Significant changes in technology necessitate a refreshed assessment of new
potential risks and their validations. Technology changes include migrating to the
cloud, use of newer database tools, extensive mobile application usage, and AI/ML
technologies. These changes may present risks to the existing control environment such
that it may be unable to mitigate the original identiﬁed risks, but also may not be
eﬀective across a much broader spectrum of changes. Engagement with the risk and
internal audit functions helps align with required governance obligations as cloud usage
increases. This engagement needs to include documentation and demonstration by the first
line, to the second and third lines, of the controls, technology, and processes that
have been implemented to secure and operate the cloud environment. This process can
contain a regular review cadence for new controls, so the first line can evolve their
implementations as needed to quickly and safely adopt best practices for new threats.

### Prescriptive guidance

All stakeholders from the three lines of defense should be invited to participate
in suggesting, evaluating, and approving changes to risk controls. A periodic review
of risk controls, as well as an out-of-cycle mechanism to suggest updates, should be
clearly documented and understood by all stakeholders. The lifecycle of a risk control
(suggestion, review, approval, training, implementation, and retirement) should also
be documented and understood. Prior to implementation of a specific risk control,
metrics should be identified to indicate the effectiveness of the control. These
metrics should be generated and compiled automatically and should be reviewed
periodically throughout the risk control's lifecycle. Thresholds that indicate
effectiveness should be established, and the continued breach of those thresholds
should prompt review of the risk control, with an expectation that it be updated or
retired.

## FSIOPS01-BP03 Implement a process for adopting appropriate risk appetites

Failures can happen at any time. The appropriate risk authority within the firm
(for example, the board of directors, chief risk officers, or business risk officers)
needs to evaluate the criticality of a business process (and the underlying workloads
that support that process) and specify the level of availability that the firm requires
for that process. This must take into consideration the potential impact that a
disruption of that process has on the firm, the market, the customers, and regulatory
bodies managing the financial infrastructure, as well as the cost of operating the
workload in a high availability mode weighed against business agility and innovation.
Working backwards from these risk appetites allows you to drive the operational
priorities and the resiliency design choices of cloud workloads supporting business
services in a prioritized manner. Setting clear risk appetites allows for effective risk
management and governance.

### Prescriptive guidance

All workloads should be categorized based on their criticality and associated
risk tolerance. In financial services organizations, this classification has often
already occurred as part of disaster recovery planning, and these risk categorizations
can be reused elsewhere. Once risk categories are established, requirements should be
identified to be applied to workloads within each risk category. Examples of
requirements might be recovery time objective (RTO) or recovery point objective (RPO)
expectations, use of encryption for data in-transit and at rest, and geographies
within which data must be stored. Building upon these requirements, preferred
architectural patterns should be identified that help meet the needs of each risk category
in an efficient and manageable way. Publishing these reference architectures is a good
way to encourage their adoption, as it simplifies the use of a consistent and
preferred architecture, and also provides a foundation for automation.
