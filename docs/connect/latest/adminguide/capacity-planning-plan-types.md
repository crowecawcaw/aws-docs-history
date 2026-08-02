# Capacity plan types in Connect Customer

When you create a capacity plan, you choose a **Plan type**.
Your choice sets the purpose of the plan, the forecast inputs, and the output
format.

Connect Customer provides the following plan types:

- **Hiring plan** — Focused on hiring
  and workforce planning. Produces daily, weekly, or monthly FTE estimates you
  can share with Human Resources and Finance.
- **Scheduling plan** — Focused on
  scheduling and resource use. Produces headcount needs and service level
  data at 15-minute or 30-minute intervals.

## Forecast requirements by plan type

Each plan type has different forecast needs:

- **Hiring plan** — Requires a
  published long-term forecast and a published short-term forecast. The
  two must overlap by at least one day. For best results, use at least
  4 weeks of overlap.
- **Scheduling plan** — Requires
  only a published short-term forecast. No long-term forecast is needed.
  If the short-term forecast is not published, you cannot generate a
  Scheduling plan.

## Date range requirements

For a Scheduling plan, the plan start and end dates must fall within the
short-term forecast date range. For a Hiring plan, the plan dates use the
long-term forecast range instead.

## Shrinkage

Both plan types support a total shrinkage percentage. Enter this value in the
**Shrinkage** field in the **Scenario
inputs** section when you [Create capacity
planning scenarios](capacity-planning-create-scenarios.md "capacity-planning-create-scenarios.md"). You can override
this value with interval-level or day-level values by uploading a CSV on the
**Import** tab.
