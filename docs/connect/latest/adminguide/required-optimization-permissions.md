

# Security profile permissions for forecasting & agent scheduling in Connect Customer
<a name="required-optimization-permissions"></a>

Assign the following security profile permissions as needed to use forecasting & agent scheduling. 

**Analytics and Optimization permissions**
+ **Forecasting**: Grants permission to view and edit in forecasting pages. For example, you can: 
  + [Create forecast groups](create-forecast-groups.md) - **Edit** permission is required.
  + [Import historical data](import-data-for-forecasting.md) - **Edit** permission is required.
  + [Create forecasts](create-forecasts.md) - **Edit** permission is required.
  + [Inspect a forecast](inspect-forecast.md) - **Edit** permission is required.
  + [Download a forecast](download-forecasts.md) - **Edit** permission is required.
  + [Edit a forecast](edit-forecast.md) - **Edit** permission is required.
  + [Publish a forecast](publish-forecast.md) - **Publish** permission is required.
+ **Capacity planning**: Grants permission to view and edit in capacity planning pages, including scenario and capacity plans. It also grants permission to import future estimated shrinkage and available FTEs. For example, you can: 
  + [Create capacity planning scenarios](capacity-planning-create-scenarios.md) - **Edit** permission is required.
  + [Import estimated future shrinkage and available full-time employees](upload-estimated-future-shrinkage.md) - **Edit** permission is required.
  + [Create capacity plans using forecasts and scenarios](capacity-planning-use-forecast.md) - **Edit** permission is required.
  + [Review capacity plan output](capacity-planning-review-output.md) - **Edit** permission is required.
  + [Override a capacity plan](override-capacity-plan.md) - **Edit** permission is required.
  + [Download a capacity plan](download-capacity-plan.md) - **Edit** permission is required.
  + [Publish a capacity plan](publish-capacity-plan.md) - **Publish** permission is required.
+ **Forecast and schedule interval**: Grants permission to:
  + [Set the forecast and scheduling interval](set-forecast-scheduling-interval.md). Grants access to the **Forecast and schedule interval** tab on the **Forecasting** page. 
  + [Set the forecast and scheduling interval](set-forecast-scheduling-interval.md). Grants access to the **Forecast timezone** tab on the **Forecasting** page.

**Scheduling**
+ **Schedule manager**. Grants permission to view, edit, and publish generated schedules from the Schedule manager. You can also import an agents time off balance to Connect Customer
**Note**  
You need the **View** permission and the **Analytics and Optimization** - **Historical metrics** - **Access** permission to view historical [Schedule Adherence metrics](scheduling-metrics.md).
+ **Published schedule calendar**:
  + View - This option also enables the Time off requests - View option. 
  + Edit - This option also enables the Time off requests - View Edit, and Approve options. 
+ **Time off requests**
  + **View**. Grants permissions to agents to view time off requests in the Time off Requests drawer. Users with the View permission can not create or approve time off requests.
  + **Edit**. Grants permissions to create time off requests.
+ **Time off balance**. To access the Staff Rules page where time off balance is managed, users must have at least **Schedule manager - View**.
  + **View**. Grants permission to view and download time off balances. Users can also view time off balances with **Schedule manager - Edit**.
  + **Edit**. Grants permission to upload time off balances. Users can also upload time off balances with **Schedule manager - Edit**.

**Agent Applications**
+ **Agent application schedule calendar**. Grants permission to agents to **View** or **Edit** their schedule in their agent application. Agents require the **Edit** permission to request time off. 

  They can accept or decline VTO.

For information about how to add more permissions to an existing security profile, see [Update security profiles in Connect Customer](update-security-profiles.md).

By default, the **Admin** security profile already has permissions to perform all forecasting, capacity planning, and scheduling activities.