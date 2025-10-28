# Visual types in Amazon Quick Sight

Amazon Quick Sight offers a range of visual types that you can use to display your data. Use the
topics in this section to learn more about the capabilities of each visual type.

###### Topics

- [Measures and dimensions](#measures-and-dimensions "#measures-and-dimensions")
- [Display limits](#display-limits "#display-limits")
- [Hiding or displaying the other category](#other-category "#other-category")
- [Customizing the number of data
  points to display](#customizing-number-of-data-points "#customizing-number-of-data-points")
- [Using AutoGraph](autograph.md "autograph.md")
- [Using bar charts](bar-charts.md "bar-charts.md")
- [Using box plots](box-plots.md "box-plots.md")
- [Using combo charts](combo-charts.md "combo-charts.md")
- [Using custom visual content](custom-visual-content.md "custom-visual-content.md")
- [Using donut charts](donut-chart.md "donut-chart.md")
- [Using funnel charts](funnel-charts.md "funnel-charts.md")
- [Using gauge charts](gauge-chart.md "gauge-chart.md")
- [Using heat maps](heat-map.md "heat-map.md")
- [Using Highcharts](highchart.md "highchart.md")
- [Using histograms](histogram-charts.md "histogram-charts.md")
- [Using image components](image-component.md "image-component.md")
- [Using KPIs](kpi.md "kpi.md")
- [Using layer maps](layered-maps.md "layered-maps.md")
- [Using line charts](line-charts.md "line-charts.md")
- [Creating maps and geospatial charts](geospatial-charts.md "geospatial-charts.md")
- [Using small multiples](small-multiples.md "small-multiples.md")
- [Using pie charts](pie-chart.md "pie-chart.md")
- [Using pivot tables](pivot-table.md "pivot-table.md")
- [Using radar charts](radar-chart.md "radar-chart.md")
- [Using Sankey diagrams](sankey-diagram.md "sankey-diagram.md")
- [Using scatter plots](scatter-plot.md "scatter-plot.md")
- [Using tables as visuals](tabular.md "tabular.md")
- [Using text boxes](textbox.md "textbox.md")
- [Using tree maps](tree-map.md "tree-map.md")
- [Using waterfall charts](waterfall-chart.md "waterfall-chart.md")
- [Using word clouds](word-cloud.md "word-cloud.md")

## Measures and dimensions

We use the term _measure_ to refer to numeric values that you use
for measurement, comparison, and aggregation in visuals. A measure can be either a
numeric field, like product cost, or a numeric aggregate on a field of any data type,
like count of transaction IDs.

We use the term _dimension_ or _category_ to
refer to text or date fields that can be items, like products, or attributes that are
related to measures and can be used to partition them. Examples are sales date for sales
figures or product manufacturer for customer satisfaction numbers. Amazon Quick Sight automatically
identifies a field as a measure or a dimension based on its data type.

Numeric fields can act as dimensions, for example ZIP codes and most ID numbers.
It's helpful to give such fields a string data type during data preparation. This
way, Amazon Quick Sight understands that they are to be treated as dimensions and are not useful
for performing mathematical calculations.

You can change whether a field is displayed as a dimension or measure on an
analysis-by-analysis basis instead. For more information, see [Fields as dimensions and measures](creating-a-visual.md#dimensions-and-measures "creating-a-visual.md#dimensions-and-measures").

## Display limits

All visual types limit the number of data points they display, so that the visual
elements (like lines, bars, or bubbles) are still easy to view and analyze. The visual
selects the first _n_ number of rows for display up to the limit for
that visual type. The selection is either according to sort order, if one has been
applied, or in default order otherwise.

The number of data points supported varies by visual type. To learn more about display
limits for a particular visual type, see the topic for that type.

The visual title identifies the number of data points displayed if you have reached
the display limit for that visual type. If you have a large dataset and want to avoid
running into the visual display limit, use one or more filters to reduce the amount of
data displayed. For more information about using filters with visuals, see [Filtering data in Amazon Quick Sight](adding-a-filter.md "adding-a-filter.md").

For dashboards and analyses, Amazon Quick Sight supports the following:

- 50 datasets per dashboard
- 20 sheets per dashboard
- 30 visualization objects per sheet

You can also choose to limit how many data points you want to display in your visual,
before they are added to the **other** category. This category contains
the aggregated data for all the data beyond the cutoff limit for the visual type you are
using—either the one you impose, or the one based on display limits. You can use
the on-visual menu to choose whether to display the **other** category.
The **other** category doesn't show on scatter plots, heat maps,
maps, tables (tabular reports), or key performance indicators (KPIs). It also
doesn't show on line charts when the x-axis is a date. Drilling down into the
**other** category is not supported.

## Hiding or displaying the other category

Use the following procedure to hide or display the "other" category.

###### To hide or display the "other" category

1. On the analysis page, choose the visual that you want to modify.
2. Choose the on-visual menu at the upper-right corner of the visual, and then
   choose **Hide "other" category** or **Show "other"
   category**, as appropriate.

## Customizing the number of data

points to display

You can choose the number of data points to display on the main axis of some visuals.
After this number is displayed in the chart, any additional data points are included in
the "other" category. For example, if you choose to include 10 data points out of 200,
10 display in the chart and 190 become part of the "other" category.

To find this setting, choose the **v**-shaped on-visual menu, then
choose **Format visual**. You can use the following table to determine
which field well contains the data point setting and what number of data points the
visual type displays by default.

| Visual type           | Where to find the data point setting                                                  | Default number of data points |
| --------------------- | ------------------------------------------------------------------------------------- | ----------------------------- |
| Bar chart, horizontal | **Y-axis** – **Number of data points displayed**                                      | 10,000                        |
| Bar chart, vertical   | **X-axis** – **Number of data points displayed**                                      | 10,000                        |
| Combo chart           | **X-axis** – **Number of data points displayed**                                      | 2,500                         |
| Heat map              | **Rows** – **Number of rows displayed** **Columns** – **Number of columns displayed** | 100                           |
| Line chart            | **X-axis** – **Number of data points displayed**                                      | 10,000                        |
| Pie chart             | **Group/Color** – **Number of slices displayed**                                      | 20                            |
| Tree map              | **Group by** – **Number of squares displayed**                                        | 100                           |
