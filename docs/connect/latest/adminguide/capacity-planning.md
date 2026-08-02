# Capacity planning in Connect Customer

A capacity plan helps you determine how many agents your contact center needs. It
uses forecasts and scenario inputs to set staffing targets for a given time
period.

When you create a capacity plan, you choose one of two plan types.
With a _Hiring plan_, you get long-term FTE estimates for hiring and
workforce planning. With a _Scheduling plan_, you get interval-level
headcount needs for scheduling and resource use. For more information, see
[Capacity plan
types](capacity-planning-plan-types.md "capacity-planning-plan-types.md").

For Hiring plans, capacity planning estimates your long-term FTE (full-time
equivalent) needs up to 64 weeks in the future. You can share these estimates with Human
Resources, Finance, and Training. These estimates help when your business launches a new
product or enters a new Region and needs to hire staff.

Hiring plans use both long-term and short-term forecasts as inputs, along with
scenario data that you provide. We recommend an overlap of at least 4 weeks between
the two forecasts. The overlap helps identify contact patterns within a day. At a
minimum, the two forecasts must overlap by at least 1 day.

Scheduling plans require only a published short-term forecast for the forecast
group. No long-term forecast or overlap is needed. The plan gives you headcount needs
in 15-minute or 30-minute intervals. The interval size matches your short-term forecast
settings. Your plan dates must fall within the forecast date range. For more
information, see [Forecast requirements by plan type](capacity-planning-plan-types.md#capacity-planning-plan-types-forecast-requirements "capacity-planning-plan-types.md#capacity-planning-plan-types-forecast-requirements") and [Date range requirements](capacity-planning-plan-types.md#capacity-planning-plan-types-date-range "capacity-planning-plan-types.md#capacity-planning-plan-types-date-range").

Use Scheduling plan output to find staffing gaps across a short horizon. You can
see how many agents you need in each interval and align staffing to demand patterns.
The output also shows how each interval performs against your target metric. For
details, see [Review Scheduling plan output](capacity-planning-review-output.md#capacity-planning-scheduling-plan-output "capacity-planning-review-output.md#capacity-planning-scheduling-plan-output").

The following diagram shows the Hiring plan flow and the integration among
published long-term forecasts, capacity planning, and capacity planning
output.

![Hiring plan flow from long-term forecasts through capacity planning inputs to capacity planning output.](images/wfm-capacity-planning-diagram.png)

## Getting started

To create and share a capacity plan, complete the following steps. Some steps
differ depending on whether you create a Hiring plan or a Scheduling
plan.

1. [Create capacity
   planning scenarios](capacity-planning-create-scenarios.md "capacity-planning-create-scenarios.md")
2. (Optional) [Import estimated future shrinkage and available full-time employees in Connect Customer](upload-estimated-future-shrinkage.md "upload-estimated-future-shrinkage.md"): This step
   can improve the accuracy of your capacity plan. For Hiring plans, you upload
   day-level shrinkage and Available FTE data. For Scheduling plans, you import
   interval-level headcount and shrinkage data instead (see [Import headcount and shrinkage data for Scheduling plans](upload-estimated-future-shrinkage.md#upload-scheduling-headcount-shrinkage "upload-estimated-future-shrinkage.md#upload-scheduling-headcount-shrinkage")).
3. [Manage starting
   backlog projections](capacity-planning-backlog-projections.md "capacity-planning-backlog-projections.md"): If you use
   an average time to complete target for the Task or Email channels, Connect Customer
   automatically generates starting backlog projections for capacity planning
   to use. You can review or override these projections.
4. [Create capacity plans
   using forecasts and scenarios](capacity-planning-use-forecast.md "capacity-planning-use-forecast.md")
5. [Review capacity plan
   output](capacity-planning-review-output.md "capacity-planning-review-output.md")
6. [Review](capacity-planning-review-output.md "capacity-planning-review-output.md"), [override](override-capacity-plan.md "override-capacity-plan.md"), [re-run](rerun-capacity-plan.md "rerun-capacity-plan.md"), or [download](download-capacity-plan.md "download-capacity-plan.md") a capacity plan.

###### Note

Plan override is not available for Scheduling plans. 7. [Publish a capacity
plan](publish-capacity-plan.md "publish-capacity-plan.md")
