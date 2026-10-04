

# Hierarchy filters
<a name="hierarchy-filter"></a>

A *hierarchy filter* lets you offer rich, multi-level filtering in a single compact control. Instead of adding separate filter controls for each level of a dimension, such as Region, Country, and City, you combine them into one control. Readers drill through this control from broadest to most detailed. This reduces clutter on the sheet and guides readers to the data they need in fewer clicks.

Use a hierarchy filter when your data has a natural parent-child structure and you want readers to explore it along a defined path. Use standard independent filters when the dimensions are unrelated or readers need to filter each one on its own.

**Hierarchy filter compared to cascading filter.** Both help readers drill through related dimensions, but they work differently. A hierarchy filter packs the entire drill path (for example, Region → Country → City) into a *single* control, with each level nested inside the one above it. A [Creating cascading filters](use-a-cascading-filter.md) uses *separate* controls, where a selection in one control narrows the values available in the next. Use a hierarchy filter when you want one compact control for the whole path. Use cascading filters when you want distinct controls that readers see and set individually.

## Benefits
<a name="hierarchy-filter-benefits"></a>

A hierarchy filter offers the following benefits:
+ **Reduced visual clutter.** Readers see a short list of top-level values first (for example, regions) rather than hundreds of values upfront. The interface stays clean at every step.
+ **Fewer clicks and guided exploration.** Readers drill down a logical path (Region → Country → City) instead of scanning a flat list. Each selection narrows the next.
+ **Mix-and-match selection.** Readers can combine levels in one control. For example, they can select an entire country such as Japan alongside a single city such as New York.
+ **Scales without overwhelming.** A single control supports deep hierarchies (up to five levels) without crowding the toolbar with separate controls.
+ **Prevents confusion.** Readers don't need to know which country belongs to which region. The hierarchy encodes that relationship, making the dashboard self-guiding.

## Prerequisites
<a name="hierarchy-filter-prerequisites"></a>

You need author access to create and manage analyses and dashboards.

## Step 1: Add a filter and set its type to hierarchy filter
<a name="hierarchy-filter-step1"></a>

1. In the **Filters** pane, choose **Add**, and then select the field to filter on (for example, **Region**).

1. Choose the filter to open the **Edit filter** pane.

1. Open the **Filter type** dropdown, and under **ADVANCED FILTER**, choose **Hierarchy filter**.

## Step 2: Add and arrange the fields
<a name="hierarchy-filter-step2"></a>

A hierarchy filter is a single filter that holds several related fields, up to five levels (for example, Region → Subregion → Country → City → Town). The fields don't have to be geographic. Any parent-child dimensions work, such as Product Category → Product.

1. Under **FIELD HIERARCHY**, use **Add field** to add **Region**, **Country**, and **City**.

1. Arrange the fields from broadest to most detailed: **Region**, then **Country**, then **City**. Use each field's **move up** and **move down** control to reorder. The order sets the reader's drill-down path.
**Note**  
Reordering the fields later clears any selections already saved on the filter.

1. Set **Filter condition** to **Include**, and then choose your **Null options**.

1. Set the scope with the **Applied to** icons at the top of the pane. The default is **Only this visual**. Switch it to **Cross-sheet (All sheets and visuals)** so the control filters the whole dashboard.

1. Choose **Apply**.

## Step 3: Add the control to the sheet and publish
<a name="hierarchy-filter-step3"></a>

1. From the filter's options menu (**⋮**), choose **Add to sheet**. The filter appears as a single control, labeled by default something like **Hierarchy control for Region**, that you can pin to the top of the sheet.

1. Remove any older standalone Region, Country, or City controls. The one hierarchy control replaces all three.

1. Publish the analysis as a dashboard.

## Reader experience
<a name="hierarchy-filter-reader-experience"></a>

The hierarchy filter appears as a single dropdown control. Opening it reveals a hierarchy: a **Select all** option, and then each top-level value as an expandable node.
+ **Collapsed.** The control shows the top level only (for example, AMER, APAC, and EMEA), each with an expand arrow. The dashboard shows all data.
+ **Expanded.** When a reader chooses the arrow next to a value such as EMEA, its child values appear nested beneath it (France, Germany, and UK). Expanding UK in turn reveals its cities (London, Manchester, and Edinburgh). The relationships are visible directly in the hierarchy, so readers don't need to know the geography in advance.

## Constraints and considerations
<a name="hierarchy-filter-constraints"></a>

Keep the following in mind when you build a hierarchy filter:
+ **Number of levels.** A hierarchy filter holds up to five data fields (levels).
+ **Supported field types.** You can add only dimension fields as levels. Text, numeric dimensions, and boolean fields all qualify. You can't add measures (for example, Sales or Quantity) as levels.
+ **Reordering.** You reorder fields with **move up** and **move down** (one position at a time), not drag-and-drop. The order defines the parent-to-child path.
+ **Selection behavior.** Selecting a value at a lower level auto-selects its parent chain. Selecting a city marks its country and region as partially selected, so the reader always sees the full path of their choice.
+ **Null handling.** A **Null options** setting (for example, Exclude nulls) controls whether rows with a blank value in a hierarchy field are included. This setting applies only to the values shown in your visuals. It does not affect how null values appear in the hierarchy filter control itself.
+ **Search behavior.**
  + The search bar at the top of the filter searches values in the highest hierarchy level only (for example, Region). It does not search across the whole hierarchy.
  + Lower levels have their own search boxes, so you can search values at those levels too. A separate search box appears at a lower level whenever that level contains more than 10 unique values.
  + If a hierarchy level contains more than 1,000 unique values, only a search box appears and no values are displayed. Use it to find and select the specific values you want to filter on.