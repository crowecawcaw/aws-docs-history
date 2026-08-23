# Creating and Configuring a Demand Plan

**To create a demand plan:**

1. Navigate to the Plans section in Amazon Connect Decisions and click
   **Create Plan**. Once a plan is created, you have the
   flexibility to edit it at any time to reflect changing business needs or incorporate
   new information.
2. **Configure Time Horizon settings:**

   - **Time bucket**: Select Daily, Weekly, or
     Monthly based on your planning needs.
   - **Plan horizon**: Specify the forecast
     horizon:

     - Daily: 1 to 28 days
     - Weekly: 1 to 26 weeks
     - Monthly: 1 to 12 months

   - **Forecast start date**: Must be on Mondays
     for weekly plans or the 1st day of the month for monthly plans. If a
     non-compliant date is selected, the system automatically adjusts to the start
     of the same time bucket. For weekly plans, the date will shift to the Monday
     of the same week. For monthly plans, the date will shift to the 1st day of
     the following month.

3. **Select Planning Grain:**

Choose the level of detail for your forecasts:

    * **Product**: Forecast by product across all
     locations
    * **Site**: Forecast by location across all
     products
    * **Ship from site ID**: Forecast by specific
     shipping location
    * **None**: Configures the plan at the product
     level only

4. **Set Prediction Lead Time:**

This parameter determines the input to forecast accuracy calculations. The
prediction lead time is the number of periods ahead for which forecasts are compared
against actual demand. 5. **Configure Consensus Plan Rules**
(optional):

Consensus rules combine multiple forecast inputs into a unified forecast. You can
create rules that specify how different forecast types should be combined.

**Example rules:**

    * "For product category = Automotive, use average of sales forecasts,
     marketing forecasts, customer forecasts, and baseline forecasts"
    * "If customer forecast is zero, then the forecast for that item must be
     zero"
    * "For product categories Professional Power Tools, always use customer
     forecasts"

**Requirements for consensus rules:**

    * The referenced data must exist in your Amazon Connect Decisions Data Lake
     (Entity Name = Forecast) for all forecast types. For example, if you specify
     a rule as "Use maximum of sales forecast and baseline forecast", both the
     "sales forecast" and "baseline forecast" must be present in the SCDL Forecast
     entity with their respective `plan_type` values
     (`plan_type` = "Sales Forecast" and `plan_type` =
     "Baseline Forecast").
    * Rules should be arranged in the order they need to be executed in.
    * Forecast data format must match your plan configuration
     granularity.
