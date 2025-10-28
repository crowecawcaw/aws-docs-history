# Navigating Capacity Manager in the AWS console

The Capacity Manager console is organized into tabs that provide different views of your capacity data:

- **Dashboard** — Provides a high-level overview of all On-Demand Capacity Reservations,
  On-Demand and Spot usage, including key metrics and top alerts to help improve your capacity posture.
- **Usage** — Provides an overview of your instance usage patterns for On-Demand and Spot instances.
  Analyze coverage by Capacity Reservations and identify optimization opportunities through flexible grouping and filtering.
- **Reservations** — Provides analysis of Capacity Reservation utilization,
  management capabilities, and detailed reservation metrics across accounts and Regions.
- **Spot** — Monitors Spot usage patterns and provides cost analysis for Spot instances
  across accounts and Regions.
- **Data exports** — Manages data export configuration to Amazon S3, including scheduling,
  formatting, and template selection.
- **Settings** — Provides service configuration options including organization access
  and regional settings.
  Within the Usage and Reservations tabs, Capacity Manager provides a hierarchical navigation structure that allows you to drill down
  from high-level overviews to detailed resource information. Understanding this navigation pattern helps you analyze your
  capacity data efficiently and identify optimization opportunities.

###### Topics

- [Navigation hierarchy](#navigation-hierarchy "#navigation-hierarchy")
- [View breakdown and details for Usage and Reservations](#navigation-page-breakdown "#navigation-page-breakdown")

## Navigation hierarchy

Capacity Manager uses a three-level navigation structure for Usage and Reservations:

1. **Overview page** — High-level summary with aggregated metrics.
2. **Breakdown page** — Detailed analysis with filtering and grouping options
3. **Detail pages:**
   - Usage details — Information about your selected dimension combination, which provides statistics and time-series data to help you understand usage patterns.
   - Reservation details — Information about a specific Capacity Reservation including utilization statistics, usage patterns over time, and configuration details.

###### Note

Spot follows a simplified structure with only the overview page.

## View breakdown and details for Usage and Reservations

Both Usage and Reservations tabs follow the same three-level navigation structure, allowing you to progress from overview
to breakdown to details pages. The processes for accessing breakdown and details pages are similar, with only minor differences
in where the navigation links are located within each tab.

###### To access the resource breakdown pages

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose **Capacity Manager**.
3. Choose the tab for the resource type you want to analyze: **Usage** or **Reservations**.
4. In the **Aggregations** section, locate the breakdown link:
   - **Usage**: In the **Actions** column, choose **View breakdown**.

   ###### Note

   Depending on your screen size or the number of dimensions you've applied, you might need to scroll horizontally across the
   page to find the View breakdown link.
   - **Reservations**: In the **Reservations** column, choose the number (the number is a link) of the reservation you want to view.

###### To access the details pages

1. On the breakdown page, navigate to the relevant section:
   - **Usage**: The Unique dimension combinations section.
   - **Reservations**: The Reservations section.

2. In the relevant section of your chosen resources, access the details page.
   - **Usage**: In the Actions column, choose **View details**.

   ###### Note

   Depending on your screen size or the number of dimensions you've applied, you might need to scroll horizontally across the page to find the View details link.
   - **Reservations**: In the Reservation ID column, choose the reservation you want to view.
