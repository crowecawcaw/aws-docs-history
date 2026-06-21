# Insights

## Billed revenue

The Billed Revenue report shows the total revenue invoiced through your AWS Marketplace products over a selected time period. Use this report to track billing performance and identify trends.

### To view billed revenue

1. In your connected account, choose **Insights**.
2. Choose **Billed Revenue**.
3. The report displays the following key metrics:

   - **Gross revenue**
   - **Gross refund**
   - **Listing fee**
   - **Wholesale cost**
   - **Seller net revenue**

4. The data table contains the following columns:

   - Invoice date
   - Payment due date
   - Payment terms
   - Invoice ID
   - Listing fee invoice ID
   - Subscriber company
   - Actions

### Filtering

Use the filter bar to narrow the report:

| Filter   | Options                                                                                        |
| -------- | ---------------------------------------------------------------------------------------------- |
| Currency | Choose a currency                                                                              |
| Date     | Custom; Past 30 days; Past 60 days; Past 90 days; Trailing 12 months (TTM); Year to date (YTD) |

### Column visibility

Customize which columns appear in the data table:

1. Choose the **Columns** button above the table.
2. Select or deselect columns to show or hide.
3. Column preferences are saved for your session.

For more information about using filters across all reports, see Using filters and column visibility.

### Exporting data

1. Configure your desired filters.
2. Choose **Export**.
3. Select the format (CSV).
4. The filtered data is downloaded.

### Notes

- Revenue data is sourced from your connected AWS Marketplace account and may have a 24-48 hour delay.
- Billed revenue represents invoiced amounts (pre-tax). It does not reflect collected or disbursed amounts.
- For disbursement data, see Collections and disbursements.

### Related topics

- [Collections and disbursements](#collections-and-disbursements "#collections-and-disbursements")
- [Agreements and renewals](#agreements-and-renewals "#agreements-and-renewals")
- [Using filters and column visibility](#using-filters-and-column-visibility "#using-filters-and-column-visibility")

## Collections and disbursements

The Disbursements report tracks disbursement of funds to your account, providing visibility into your cash flow from AWS Marketplace transactions.

### To view disbursements

1. In your connected account, choose **Insights**.
2. Choose **Disbursements**.
3. The report displays the following key metrics:

   - **Gross revenue**
   - **Net revenue**
   - **Wholesale cost**
   - **Amount disbursed**
   - **Amount undisbursed (past due)**

### Data table

The detail table contains the following columns:

| Column                 |
| ---------------------- |
| Account                |
| Invoice date           |
| Payment due date       |
| Payment terms          |
| Invoice ID             |
| Listing fee invoice ID |
| Actions                |

### Filtering

| Filter               | Options                                                                                        |
| -------------------- | ---------------------------------------------------------------------------------------------- |
| Currency             | Choose a currency                                                                              |
| Choose Date Category | Disbursement date                                                                              |
| Date                 | Custom; Past 30 days; Past 60 days; Past 90 days; Trailing 12 months (TTM); Year to date (YTD) |

### Notes

- Disbursement timing follows AWS Marketplace payment terms (typically Net 30-60 days from invoice date).
- The difference between billed revenue and disbursed amounts reflects listing fees, refunds, and collection timing.
- For more information about AWS Marketplace disbursement schedules, see [Disbursement](../userguide/disbursement.md "../userguide/disbursement.md") in the AWS Marketplace Seller Guide.

### Related topics

- [Billed revenue](#billed-revenue "#billed-revenue")
- [Agreements and renewals](#agreements-and-renewals "#agreements-and-renewals")
- Account dashboard

## Agreements and renewals

The Agreements/Renewals report provides a lifecycle view of your AWS Marketplace agreements, showing active and ended agreement data.

### To view agreements and renewals

1. In your connected account, choose **Insights**.
2. Choose **Agreements/Renewals**.
3. The report displays the following key metrics:

   - **Number of active agreements**
   - **Number of ended agreements**

### Renewal tracking table

The data table contains the following columns:

| Column                          |
| ------------------------------- |
| Subscriber company name         |
| Subscriber AWS account ID       |
| Subscriber encrypted account ID |
| Subscriber email domain         |
| Subscriber country              |
| Subscriber state                |

### Filtering

| Filter                  | Options                           |
| ----------------------- | --------------------------------- |
| Agreement ending period | Choose an agreement ending period |
| Choose Date Category    | Agreement end date                |
| Date                    | Choose a date range               |

### Notes

- Agreement data is synced from your connected AWS Marketplace account.

### Related topics

- [Billed revenue](#billed-revenue "#billed-revenue")
- [Collections and disbursements](#collections-and-disbursements "#collections-and-disbursements")
- [Using filters and column visibility](#using-filters-and-column-visibility "#using-filters-and-column-visibility")

## Using filters and column visibility

All Insights reports support consistent filtering and column customization. Use these features to focus on the data that matters for your analysis.

### Date filters

Every report includes a Date filter:

1. Choose the **Date** dropdown at the top of the report.
2. Choose a preset range or choose **Custom**:

   - Custom
   - Past 30 days
   - Past 60 days
   - Past 90 days
   - Trailing 12 months (TTM)
   - Year to date (YTD)

3. The report updates automatically.

### Column filters

Filter data by specific column values:

1. Choose the filter icon on any column header.
2. Select or search for values to include.
3. Choose **Apply**.

Multiple column filters can be active simultaneously (AND logic).

### Column visibility

Customize which columns appear in report tables:

1. Choose the **Columns** button above the data table.
2. The column visibility menu provides the following controls:

   - A Search field to find columns by name
   - A checkbox list to show or hide individual columns
   - **Show/Hide All** to toggle all columns at once
   - **Reset** to restore default column visibility

3. The table updates immediately.

Required columns, for example Invoice ID, are disabled in the menu and cannot be hidden.

Column visibility preferences persist for your browser session.

### Sorting

1. Choose any column header to sort by that column.
2. Choose again to toggle between ascending and descending order.
3. A sort indicator arrow shows the current sort direction.

### Exporting filtered data

1. Apply your desired filters and column selections.
2. Choose **Export** (or **Download CSV**).
3. The export includes only the currently visible, filtered data.

### Notes

- Filters do not persist across page navigation. Returning to a report resets to defaults.
- The maximum export size is 10,000 rows. For larger datasets, narrow the date range.
- All reports use the same filtering interface for consistency.

### Related topics

- [Billed revenue](#billed-revenue "#billed-revenue")
- [Collections and disbursements](#collections-and-disbursements "#collections-and-disbursements")
- [Agreements and renewals](#agreements-and-renewals "#agreements-and-renewals")
