# Security profile permissions for

forecasting, capacity planning, and scheduling in Amazon Connect

Assign the following security profile permissions as needed to use forecasting, capacity planning, and scheduling.

###### Analytics and Optimization permissions

- **Forecasting**: Grants permission to view and edit in
  forecasting pages. For example, you can:
  - [Create forecast
    groups](create-forecast-groups.md "create-forecast-groups.md") -
    **Edit** permission is required.
  - [Import historical
    data](import-data-for-forecasting.md "import-data-for-forecasting.md") -
    **Edit** permission is required.
  - [Create forecasts](create-forecasts.md "create-forecasts.md") -
    **Edit** permission is required.
  - [Inspect a forecast](inspect-forecast.md "inspect-forecast.md") -
    **Edit** permission is required.
  - [Download a forecast](download-forecasts.md "download-forecasts.md") -
    **Edit** permission is required.
  - [Edit a forecast](edit-forecast.md "edit-forecast.md") - **Edit** permission is required.
  - [Publish a forecast](publish-forecast.md "publish-forecast.md") -
    **Publish** permission is required.

- **Capacity planning**: Grants permission to view and edit
  in capacity planning pages, including scenario and capacity plans. It also
  grants permission to import future estimated shrinkage and available FTEs.
  For example, you can:
  - [Create capacity
    planning scenarios](capacity-planning-create-scenarios.md "capacity-planning-create-scenarios.md") -
    **Edit** permission is required.
  - [Import estimated
    future shrinkage and available full-time employees](upload-estimated-future-shrinkage.md "upload-estimated-future-shrinkage.md") -
    **Edit** permission is required.
  - [Create capacity plans
    using forecasts and scenarios](capacity-planning-use-forecast.md "capacity-planning-use-forecast.md") -
    **Edit** permission is required.
  - [Review capacity plan
    output](capacity-planning-review-output.md "capacity-planning-review-output.md") -
    **Edit** permission is required.
  - [Override a capacity
    plan](override-capacity-plan.md "override-capacity-plan.md") -
    **Edit** permission is required.
  - [Download a capacity
    plan](download-capacity-plan.md "download-capacity-plan.md") -
    **Edit** permission is required.
  - [Publish a capacity
    plan](publish-capacity-plan.md "publish-capacity-plan.md") -
    **Publish** permission is required.

- **Forecast and schedule interval**: Grants permission
  to:
  - [Set the forecast and
    scheduling interval](set-forecast-scheduling-interval.md "set-forecast-scheduling-interval.md"). Grants
    access to the **Forecast and schedule interval**
    tab on the **Forecasting** page.
  - [Set the forecast and
    scheduling interval](set-forecast-scheduling-interval.md "set-forecast-scheduling-interval.md"). Grants
    access to the **Forecast timezone** tab on the
    **Forecasting** page.

###### Scheduling

- **Schedule manager**. Grants permission to view, edit,
  and publish generated schedules from the Schedule manager. You can also
  import an agents time off balance to Amazon Connect

###### Note

You need the **View** permission and the
**Analytics and Optimization** -
**Historical metrics** -
**Access** permission to view historical [Schedule Adherence
metrics](scheduling-metrics.md "scheduling-metrics.md").

- **Published schedule calendar**:
  - View - This option also enables the Time off requests - View
    option.
  - Edit - This option also enables the Time off requests - View Edit,
    and Approve options.

- **Time off requests**
  - **View**. Grants permissions to agents to view
    time off requests in the Time off Requests drawer. Users with the
    View permission can not create or approve time off requests.
  - **Edit**. Grants permissions to create time off
    requests.

- **Time off balance**. Grants permission to agents to view
  and upload time off balances. Supervisors do not require this
  permission.

###### Agent Applications

- **Agent application schedule calendar**. Grants
  permission to agents to **View** or
  **Edit** their schedule in their agent application.
  Agents require the **Edit** permission to request time off.

They can accept or decline VTO.
For information about how to add more permissions to an existing security profile,
see [Update security profiles in Amazon Connect](update-security-profiles.md "update-security-profiles.md").

By default, the **Admin** security profile already has
permissions to perform all forecasting, capacity planning, and scheduling
activities.
