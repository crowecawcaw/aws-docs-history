# Analyzing findings in Amazon Detective

A finding is an instance of potentially malicious activity or other risk that was detected.
Amazon GuardDuty and AWS security findings are loaded into Amazon Detective so that you can use Detective to
investigate the activity associated with the involved entities. GuardDuty findings are part of the
Detective core package and are ingested by default. All other AWS security findings that are
aggregated by Security Hub CSPM are ingested as an optional data source. See [Source data used in a behavior graph](detective-source-data-about.md "detective-source-data-about.md") for more details.

A Detective finding overview provides detailed information about the finding. It also displays a
summary of the involved entities, with links to the associated entity profiles.

If a finding is correlated to a larger activity, Detective notifies you to **Go to finding group**. We recommend using finding groups to continue your investigation, as finding groups enable you to examine multiple activities that relate to a potential security event. See [Analyzing finding groups](groups-about.md "groups-about.md").

Amazon Detective provides an interactive visualization of finding groups. This visualization
is designed to help you investigate issues faster and more thoroughly with less effort.
The finding group **Visualization** panel displays the findings and
entities involved in a finding group. You can use this interactive visualization to
analyze, understand, and triage the impact of the finding group. This panel helps
visualize the information presented in the **Involved entities** and
**Involved findings** table. From the visual presentation, you can
select findings or entities for further analysis. See [Finding group visualization](group-visual-finding-group.md "group-visual-finding-group.md").

###### Contents

- [Analyzing a finding overview in Detective](finding-overview.md "finding-overview.md")
- [Analyzing finding groups](groups-about.md "groups-about.md")
- [Finding group summary powered by generative
  AI](finding-group-summary.md "finding-group-summary.md")
- [Archiving an Amazon GuardDuty finding](finding-update-status.md "finding-update-status.md")
