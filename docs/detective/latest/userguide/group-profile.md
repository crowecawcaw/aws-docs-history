# Finding group profiles

When you select a group title, a finding group profile opens with additional details
about that group. The details panel in the finding groups profile page supports the
display of up to 1000 entities and findings for finding groups parent and
children.

The group profile page displays the set **Scope time** of the group.
This is the date and time from the earliest finding or evidence included in the group to
the most recently updated finding or evidence in a group. You can also see the
**Finding group severity**, which is equal to the highest severity
category among findings in the group. Other details within this profile panel
include:

- The
  **Involved tactics** chain shows you
  which tactics, are attributed to the findings in the group. Tactics are based on
  the [MITRE ATT&CK
  Matrix for Enterprise](https://attack.mitre.org/matrices/enterprise/ "https://attack.mitre.org/matrices/enterprise/"). The tactics are shown as a chain of colored
  dots that represents the typical progression of an attack from the earliest to
  latest stages. This means the leftmost circles on the chain typically represent
  less severe activities where an adversary is trying to gain or maintain access
  your environment. Conversely, activities toward the right are the most severe
  and can include data tampering or destruction.
- The relationships that this group has with other groups. Occasionally, one or more previously
  unconnected groups of findings could be merged into a new group based on a newly
  discovered link, for example, a finding that involves entities from the existing
  groups. In this case, Amazon Detective deactivates the parent groups and creates a
  child group. You can trace the lineage for any group back to its parent groups.
  Groups can have the following relationships:

      + **Child finding group** – A finding group created when a
       finding involved in two other finding groups is involved in a new
       finding. The parent groups of the finding are listed for any child
       group.
      + **Parent finding group** – A finding group is a parent
       when a child group has been created from it. If a finding group is a
       parent, the related children are listed with it. A parent group's status
       becomes **Inactive** when it's merged into an
       **Active** child group.

  There are two information tabs that open profile panels. Using the
  **Involved entities** and **Involved findings**
  tabs, you can view further details about the group.

Use **Run investigation** to generate an investigation report. The generated report details anomalous behavior that indicates compromise. .

## Profile within groups

**Involved entities**
Focuses on the entities in the finding group, including what findings within the group each
entity is linked to. The tags attached to each entity are also displayed
so you can quickly identify important entities based on tagging. Select
an entity to view its entity profile.

**Involved findings**
Has details about each finding, including finding severity, each entity involved, and when
that finding was first and last seen. Select a finding type in the list
to open a finding details panel with additional information about that
finding. As part of the **Involved findings** panel,
you may see **Informational** findings based on Detective
evidence from your behavior graph.
