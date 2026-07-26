# Using the conversion assessment report for migration planning

The conversion assessment report is the first step in your database migration
journey. Organizations use the report to evaluate migration complexity and make
informed go/no-go decisions before committing to a full-scale migration
project.

## Calculating total migration effort

The `Action_Items_Summary` CSV file provides three values for each
action item type that you use to estimate effort:

- **Learning curve effort** — The
  one-time cost to understand the incompatibility and design a conversion
  approach for this action item type. You incur this cost once per action
  item type, regardless of how many database objects are affected.
- **Effort to convert an occurrence**
  — The cost to resolve a single occurrence of this action item,
  after you have already designed the conversion approach.
- **Number of occurrences** — The
  number of individual database objects affected by this action item
  type.

###### Note

The effort values in the CSV are relative units on a weighted scale, not
hours. To convert to person-hours or person-days, multiply by a calibration
factor derived from your team's historical velocity on similar migration
work.

###### Conservative upper-bound estimate

The simplest estimate treats every occurrence as equally difficult. Use this
formula as a worst-case upper bound:

```
Effort for one action item type =
    Learning curve effort + (Effort per occurrence × Number of occurrences)
```

Sum this across all action item types to get your total upper-bound
estimate:

```
Total effort (upper bound) =
    Sum of [ Learning curve effort + (Effort per occurrence × Occurrences) ]
    for every action item type
```

For example, action item 5028 in a sample Oracle-to-PostgreSQL assessment has
a learning curve effort of 40, a per-occurrence effort of 8, and 12 occurrences.
Its upper-bound total is 40 + (8 × 12) = 136.

###### Realistic scenario-based estimate

The upper-bound formula overstates effort because it assumes every occurrence
takes the same amount of work. In practice, once your team has resolved the
first few occurrences of an action item type, subsequent occurrences become
faster — the solution is known and the conversion is routine. A more realistic
model discounts the majority of occurrences.

Split occurrences into two groups: a leading group that you work through at
full effort while establishing the solution, and a remaining group that you
resolve at half effort once the pattern is established. Choose the split
based on your team's confidence level:

```
Realistic effort for one action item type =
    (Leading% × Occurrences × Effort per occurrence)
  + (Remaining% × Occurrences × (Effort per occurrence ÷ 2))
```

The following table shows three scenarios for a migration team to choose
from:

Effort estimation scenarios| Scenario | Leading group | Remaining group | When to use |
| --- | --- | --- | --- |
| Optimistic | 10% | 90% | Experienced team, well-understood target engine, most<br>incompatibilities are mechanical and highly repetitive. |
| Moderate | 30% | 70% | Mixed experience level, some action item types are novel to<br>the team, typical migration project. |
| Conservative | 50% | 50% | New team, first migration to this target engine, or action<br>items span many different database object types. |

For example, action item 5127 ("Using CROSS JOIN in PostgreSQL might lead
to slow performance") has 8 occurrences and a per-occurrence effort of 160.
The upper-bound estimate is 16 + (160 × 8) = 1,296. Using the moderate scenario
(30/70 split): (0.30 × 8 × 160) + (0.70 × 8 × 80) = 384 + 448 = 832 — a 36%
reduction. Using the optimistic scenario (10/90 split): (0.10 × 8 × 160) +
(0.90 × 8 × 80) = 128 + 576 = 704 — a 46% reduction.

###### Note

The learning curve effort in the CSV is a fixed one-time cost and does
not decrease with repetition. Add it once per action item type on top of the
scenario-based occurrence cost. The scenario discount applies only to the
per-occurrence effort, not to the learning curve effort.

To calculate your total realistic migration effort, apply your chosen scenario
to every action item type and sum the results:

```
Total realistic effort =
    Sum of [ Learning curve effort
             + (Leading% × Occurrences × Effort per occurrence)
             + (Remaining% × Occurrences × (Effort per occurrence ÷ 2)) ]
    for every action item type
```

## Prioritizing action items

Use the complexity category and occurrence count of each action item to decide
the order in which you resolve them. Prioritizing action items this way helps you
address the work that has the greatest impact on your migration timeline
first.

1. **Complex actions with high occurrence
   counts** — Address these action items first. They
   require the most manual effort per occurrence, and a high occurrence
   count multiplies that effort across your schema.
2. **Medium-complexity actions** —
   Address these action items next. They typically require less effort to
   design a conversion approach for than complex actions, but still require
   manual conversion work.
3. **Simple actions** — Give these
   action items the lowest priority among the action items that require
   manual work. They typically require the least effort to resolve.
4. **Automatically converted database
   objects** — These database objects need no action.
   DMS Schema Conversion converts them without any manual intervention.

To find the complexity category for an action item, view the
**Action items** tab in the AWS DMS console, or the
`Objects with simple actions`,
`Objects with medium-complexity actions`, and
`Objects with complex actions` columns in the Summary CSV
file. To find the occurrence count for an action item type, see the
`Number of occurrences` column in the
`Action_Items_Summary` CSV file.

## Evaluating migration risk and scope

Beyond calculating effort and prioritizing individual action items, use your
conversion assessment report to evaluate the overall risk and scope of your
migration project.

- **Identify high-risk database objects**
  — Database objects that DMS Schema Conversion classifies with medium-complexity
  or complex actions require manual conversion, and represent the highest
  risk to your migration timeline. Database objects that DMS Schema Conversion
  converts automatically, or that have only simple actions, carry
  comparatively low risk. For more information about how DMS Schema Conversion assigns
  these categories, see [Complexity categories](assessment-reports-understanding.md#assessment-reports-understanding-complexity "assessment-reports-understanding.md#assessment-reports-understanding-complexity").
- **Estimate overall migration scope and
  timeline** — Use the database object counts in the
  **Summary** tab, or in the Summary CSV file, to
  estimate how much of your schema requires manual conversion. Compare the
  number of database objects with medium-complexity and complex actions
  against the total number of database objects to gauge the overall scope
  of the migration. Combine this scope with the total migration effort that
  you calculated (see [Calculating
  total effort](#assessment-reports-planning-effort "#assessment-reports-planning-effort")) and your
  team's available capacity to project a timeline for completing the manual
  conversion work.
- **Plan the sequence of manual conversion
  tasks** — The **Action items** tab and
  the action items CSV file provide a recommended action for each action
  item type. Use these recommendations, together with the priority order
  that you established (see [Prioritizing action items](#assessment-reports-planning-prioritization "#assessment-reports-planning-prioritization")),
  to plan the order in which your team resolves action items. Group action
  items that affect related database objects, such as objects in the same
  schema or database objects that depend on one another, so that your team
  can resolve related issues together.
