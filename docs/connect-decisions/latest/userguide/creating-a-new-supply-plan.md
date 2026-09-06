

# Creating a New Supply Plan
<a name="creating-a-new-supply-plan"></a>

To create a supply plan:

1. Navigate to the **Plans** section in Amazon Connect Decisions and click **Create Plan** in the **Supply Plan** section. Once a supply plan is created, you have the flexibility to edit it at any time to reflect changing business needs or incorporate new information.
**Note**  
Amazon Connect Decisions currently supports 1 plan per instance. We do not support more than 1 supply plan within the same instance.

1. **Configure Time Horizon settings**:

   1. **Time bucket**: Select **Daily** or **Weekly** based on your planning needs.

   1. **Plan horizon**: Specify the forecast horizon:

      1. **Daily**: 1 to 365 days

      1. **Weekly**: 1 to 52 weeks

   1. **Plan start date**: For weekly plans, a day of the week can be selected as the plan start date. It also indicates the beginning of the week.

1. **Plan Schedule**: Choose between **One time run** and **Recurring Schedule**.

   1. For **Recurring Schedule**, choose **Schedule Frequency**:

     1. **Daily**: Enter the UTC schedule time

     1. **Weekly**: Select the day of the week and enter the UTC schedule time

     1. **Monthly**: Select the day of the month and enter the UTC schedule time

1. **Demand Netting**: Configure what demands to drive the supply plan generation. Choose **Forecast**, **sales order**, or both.

   1. **Forecast**: Forecasted demand

   1. **Sales order**: Actual sales order demand

1. **Demand Time Fence**: The period during which the supply plan will ignore the forecasted demand.

1. **Forecast consumption window**: The period in which actual customer orders replace or consume forecasted demand.

   1. Forecast consumption window - forward days

   1. Forecast consumption window - backward days

1. **Historical Period for Demand**: Number of historical days to consider for average historical demand calculation.

1. **Past due supply days**: The number of days the supply orders can be past due but still considered as supply.

1. **Planning time fence**: The period in which the supply plan is frozen. No new planned orders will be created within the planning time fence.

1. **Configuration rules**: Constraint rules that guide the system in generating plans aligned with your business objectives. Add rules using the production capacity constraints template or warehouse space limit template.

   1. **Production Capacity Constraints**: Download the Production Capacity Constraints template csv files (zipped). Populate the data and upload 3 csv files (not zipped) back using Decision teammate.

   1. **Warehouse Space Limit**: Download the Warehouse Space Limit template csv file. Populate the data and upload it back using Decision teammate.

1. **Generate Supply Plan**: Click on the **Generate supply plan** button on the top to start the plan generation job, or wait for the scheduled plan run.