

# Filtering and Sorting Insights
<a name="filtering-and-sorting-insights"></a>

Amazon Connect Decisions provides comprehensive filtering and sorting capabilities that help you quickly focus on the insights most relevant to your supply chain responsibilities. You can navigate to the Insights page from multiple entry points and apply filters based on product hierarchies, site hierarchies, insight properties, and custom business segments.

## Accessing the Insights Page
<a name="filtering-and-sorting-insights-accessing"></a>

You can access the Insights page through several pathways:
+ Select **Insights** from the left navigation menu or from top navigation bar
+ The Insights page displays with your default view settings

### From the Homepage
<a name="filtering-and-sorting-insights-from-homepage"></a>

The homepage provides quick access to insights through status summary cards displaying insight counts by status or severity. Select any cards to navigate to the Insights page with that filter pre-applied.

When you navigate from a homepage card, the Insights page opens with relevant filters already applied.

![](http://docs.aws.amazon.com/connect-decisions/latest/userguide/images/filtering-and-sorting-insights-page-layout.png)


## Understanding the Insights Page Layout
<a name="filtering-and-sorting-insights-page-layout"></a>

The Insights page is organized into four main sections:

### Status Summary Bar
<a name="filtering-and-sorting-insights-status-summary-bar"></a>

At the top of the page, status cards display insight counts by status category:
+ **Not started**: Newly created insights with no user interaction
+ **Processing**: Insights currently being analyzed or acted upon by the system
+ **In progress**: Insights where you have initiated action on a recommendation
+ **Pending resolution**: Insights that have been actioned but are not yet fully resolved
+ **Completed**: Insights that are resolved and no longer meet the rule thresholds
+ **Dismissed**: Insights you have explicitly chosen to discard
+ **Archived**: Insights that have been moved to archive storage

Each card shows the status name and count in blue. Select any status card to filter the insights table to that status.

### Filtering and Search Area
<a name="filtering-and-sorting-insights-filtering-search-area"></a>

Below the status bar, you'll find filtering controls:

**Saved filter sets**: A dropdown on the left allows you to apply pre-configured filter combinations

**Date range filter**: In the center, "Filter by created on date range" displays the currently selected date range (for example, "2025-01-01 — 2025-12-31"). Select to open a date picker where you can choose start and end dates.

**Search filter properties**: On the right, a search bar allows you to search for specific insights by Task ID, product name, site name, or other properties

### Active Filters Display
<a name="filtering-and-sorting-insights-active-filters-display"></a>

Below the filtering controls, applied filters appear as removable chips showing:
+ The column name and filter criteria (for example, "Severity = High")
+ An X button to remove individual filters
+ A results count showing matching insights (for example, "279 Matches")
+ A "Clear filters" button with dropdown for filter management options

### Insights Table
<a name="filtering-and-sorting-insights-table"></a>

The main table displays all insights with the following columns:
+ **Insight ID**: Unique Task ID as a clickable link to view insight details
+ **Description**: Brief summary of the issue detected
+ **Status**: Current workflow state with icon indicator
+ **Severity**: Priority level (Critical, High, Medium, Low) with color coding
+ **Urgency**: Time-sensitive priority with sort capability
+ **Assigned to**: User or team responsible for the insight
+ **Impact**: Financial or operational impact when calculable
+ **Impact date**: When the issue is expected to occur
+ **Created on**: When the system detected the insight (with date and time)
+ **Product**: Product identifier affected by the insight
+ **Actions**: Three-dot menu with quick actions for each insight

## Filtering Insights
<a name="filtering-and-sorting-insights-filtering"></a>

Amazon Connect Decisions supports multiple filtering approaches to help you find relevant insights quickly.

### Using the Search Bar
<a name="filtering-and-sorting-insights-using-search-bar"></a>

The "Search filter properties" bar provides quick access to filtering:

1. Select the search bar

1. Begin typing your search term (Task ID, product name, site name, keywords)

1. The system provides real-time search results as you type

1. Applied filters appear as chips below the search area

### Hierarchical Filtering (Product and Site)
<a name="filtering-and-sorting-insights-hierarchical-filtering"></a>

When filtering by product or site hierarchies, the system searches across all five hierarchy levels simultaneously.

**To apply a hierarchical filter:**

1. Use the search bar to enter a product or site name

1. The system displays matching results grouped by hierarchy level (Level 1 through Level 5)

1. Select the hierarchy value you want to filter by

1. Click on "Apply"

1. A filter chip appears showing the complete hierarchy path

The system uses prefix-based matching with multi-word support. For example, typing "temp" matches "Temperature Sensors" because it matches the prefix of "Temperature."

When you select a hierarchy level, the filter automatically includes all child items within that hierarchy. For example, filtering by "Electronics" at Product Level 1 shows all insights for any products within the Electronics category, regardless of their specific subcategory or SKU.

### Filtering by Insight Properties
<a name="filtering-and-sorting-insights-by-properties"></a>

You can filter by specific columns to find insights based on exact field values.

**To apply a property filter:**

1. Use the search bar or column-specific filters

1. The filter input adapts based on field type:
   + **Text fields** (Status, Severity): Provides dropdown with predefined options
   + **Numeric fields** (Impact): Provides numeric input with comparison operators
   + **Date fields** (Created on, Impact date): Provides date picker with range selection

1. Select or enter your filter value

1. Click on "Apply"

1. A filter chip appears showing the property name and value (for example, "Status: Not started")

### Date Range Filtering
<a name="filtering-and-sorting-insights-date-range"></a>

The date range filter provides a dedicated interface for filtering by insight creation dates.

**To apply a date range filter:**

1. Select "Filter by created on date range"

1. The date picker displays showing the current date range

1. Select the start date and end date from the calendar

1. The filter applies automatically, showing the date range

1. The results count updates to show matching insights

### Segmentation-Based Filtering
<a name="filtering-and-sorting-insights-segmentation"></a>

If you have configured custom business segments, you can use them to filter insights based on meaningful business categories such as customer tiers, product lines, or geographic regions.

**To apply a segment filter:**

1. Use the search functionality to find segment types

1. Choose the segment type you want to use (for example, "Customer Tier")

1. Select the segment value (for example, "Tier 1")

1. Click on "Apply"

1. A filter chip appears showing "Segment Type: Segment Value"

### Setting Up Segmentation
<a name="filtering-and-sorting-insights-setting-up-segmentation"></a>

Segmentation allows you to group products, sites, customers, and channels based on business criteria that matter to your operations. To use segmentation filtering, you must first upload a Segmentation Rules table that defines your business groupings.

**Segmentation table logic:**
+ **Within a single row (AND logic)**: When you fill in multiple fields in one row, ALL of those fields must match for a record to belong to that segment
+ **Across multiple rows (OR logic)**: When you create multiple rows with the same segment\_type and segment\_value, a record qualifies if it matches ANY of those rows
+ **NULL values (wildcards)**: Leaving a field blank means "match any value"

The segmentation table supports up to five hierarchy levels for both products and sites, along with additional fields like city, state, country, trading partner, company, and channel.

**Important considerations:**
+ Segment updates apply only to future insights, not historical data
+ segment\_type and segment\_value must each be 30 characters or fewer
+ A single insight can belong to multiple segments
+ Use hierarchy levels when possible, rather than listing hundreds of individual IDs

## Managing Applied Filters
<a name="filtering-and-sorting-insights-managing-filters"></a>

All applied filters appear as removable chips below the search area.

**To remove a single filter:**

1. Select the **X** button on the filter chip

1. The system removes that filter and updates results

**To remove all filters:**

1. Select **Clear filters**

1. The system removes all filter chips and displays the unfiltered view

**Note**  
The Access Control filter toggle (if enabled in your profile settings) operates independently and is not removed by the "Clear filters" action.

## Using Saved Filter Sets
<a name="filtering-and-sorting-insights-saved-filter-sets"></a>

Saved filter sets allow you to store frequently used filter combinations and apply them quickly in future sessions.

**To apply a saved filter set:**

1. Select the **Saved filter sets** dropdown

1. Choose the filter set you want to apply

1. Click on "Apply"

1. The system applies all filters in that set at once

1. Filter chips appear for each filter in the set

## Using the Access Control Filter Toggle
<a name="filtering-and-sorting-insights-access-control"></a>

The Access Control filter toggle restricts visible data to products and sites matching your assigned permissions. This toggle operates independently from the filter chip system.

**To configure the Access Control toggle:**

1. Select your name in the top right corner

1. Choose **Profile** from the dropdown menu

1. Navigate to the **Assigned Scope** tab

1. Toggle **Filter views by my assigned scope** on or off

1. Select **Save**

**When the toggle is enabled:**
+ A visual indicator appears on the Insights page showing that Access Control filtering is active
+ You see only insights for products and sites matching your assigned scope
+ This filtering applies in addition to any filter chips you manually apply

**When the toggle is disabled:**
+ You see all insights across the organization (subject to your role permissions)
+ Manual filter chips still apply normally

If your administrator has configured the system to enforce Access Control filtering for all users, you cannot disable this toggle.

## Sorting Insights
<a name="filtering-and-sorting-insights-sorting"></a>

All columns in the Insights table support sorting, helping you organize insights by priority, impact, or timing.

**To sort the Insights list:**

1. Select any column header in the Insights table

1. The system sorts insights by that column in ascending order

1. An arrow appears on the column header showing the sort direction

1. Select the same column header again to toggle to descending order

The default sort order is by Severity (Critical to Low). Your sort selection persists during your current session and works with applied filters.

## Understanding Filter Results
<a name="filtering-and-sorting-insights-understanding-results"></a>

The results count appears below the search area, showing how many insights match your current filters.

**Results count format**: "X Matches" where X is the count of insights meeting all applied filter criteria

**When filters return no results:**

The system displays: "No insights found for selected filters. Try removing some filters or adjusting your criteria."

The empty state includes:
+ A **Clear filters** button
+ A list of currently applied filters
+ If the Access Control toggle is ON and you see no results, the message indicates: "No insights available for your assigned products/sites. Contact your administrator if you believe this is incorrect."