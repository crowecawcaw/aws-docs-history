# FSIOPS7: Have you developed a continuous improvement model?

Financial institutions should continually assess and optimize their operational processes.

## FSIOPS07-BP01 Test, model, and simulate scenarios before rollout

One of the best practices to determine if you have addressed your risk with
appropriate controls is to actually run scenarios against your cloud control framework
and operational procedures. Once your risk and control program is established, financial
institutions should continually asses and optimize their operational processes. Regular
[game days](../security-pillar/sec_incident_response_run_game_days.md "../security-pillar/sec_incident_response_run_game_days.md") for workloads deployed on AWS can help build your team's muscle
memory and validate that all operational procedures are effective in supporting your
recovery objectives and compliance with notification requirements to regulatory bodies.
We recommend designing game days to test your risk appetite and include severe, but
plausible scenarios.

### Prescriptive guidance

Identify financial services compliance requirements first, and then structure
your game days to meet those requirements. Align the complexity of game days with the
resources available within your organization. For large organizations, game days are
often scoped to a specific business unit or product team. It's acceptable to presume
certain inputs from other teams during your initial game days, which can make
scheduling more practical. It's more important to complete simple game days regularly,
and iterate on the scope and complexity over time, than to try to run complex game
days from the beginning. The most critical piece of a game day is the retrospective
review of lessons learned and the iterative improvement over time. Sufficient time to
accomplish this should be set aside early in the planning process so that it can occur
in the days immediately following the game day.

## FSIOPS07-BP02 Conduct post-event operational reviews

Post-event operational reviews should be conducted after an incident. After
troubleshooting and performing repair procedures, follow-up documentation and actions
should be assigned. An effective post-event review results in a list of practical
actions that address each of the issues that allowed the threat actor to succeed. These
actions should minimize the impact of the event and teach the wider enterprise how to
prevent, detect, and respond to a similar event in the future. For significant events, a
Correction of Error (COE) document should be composed to capture the root cause and take
preventative actions for the future. Implementation of the preventative measures should
be measured in future operations meetings.

### Prescriptive guidance

Post-event operational reviews are comprised of two components: identification of
the problem (root cause analysis) and the identification of actions to help prevent a
reoccurrence of the event (corrective actions). Identify a mechanism, such as an ITSM
tool or ticketing system, to track root cause analysis efforts and associated
corrective actions. Ownership for each task should be assigned to an individual, and a
periodic review should be used to track status. In a large and complex environment,
competing priorities and urgent activities can supersede processes such as post-event
reviews that are important for long-term stability. Leaders should establish a culture
which prioritizes these reviews, and should encourage teams to set aside a recurring
time to spend on analysis and corrective actions.
