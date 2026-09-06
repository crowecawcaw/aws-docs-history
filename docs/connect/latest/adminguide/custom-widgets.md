

# Custom widgets
<a name="custom-widgets"></a>

Create tailored dashboard components from the ground up to meet your specific business needs. With custom widgets, you can build unique visualizations without any predefined data.

![Add customer widgets in the Profile explorer layout.](http://docs.aws.amazon.com/connect/latest/adminguide/images/custom-widgets-1.png)


## Available custom components
<a name="available-custom-components"></a>
+ [Table](#table-widget)
+ [Key value pair](#key-value-pair)
+ [Key metric](#key-metric)
+ [Donut chart](#donut-chart)

## Building custom widgets
<a name="building-custom-widgets"></a>

**Each custom widget can be configured with:**
+ Custom data sources
+ Custom displays
+ Custom fields
+ Custom item interactions

## Table
<a name="table-widget"></a>

The custom table component provides flexible configuration options for displaying your data in a tabular format, with advanced features for interaction and organization.

### Features
<a name="table-features"></a>

1. **Column configurations**
   + Define custom column headers
   + Specify data for each column
   + Set data formatting options
   + Define column placement

1. **Filtering**
   + Quickly filter items within your table

1. **Linking**
   + Connect Resource Links
     + Seamless navigation to:
       + Segments
       + Calculated attributes
     + Opens in new tab
   + **External URL links**
     + Convert row item value into URLs that you can choose
     + Opens in new tab
     + Dynamically generate links based on row data
   + Drawer view links
     + Open detailed information in side drawer
     + View complete record details without leaving the page

1. Data organization
   + Grouping
     + Group rows by specific field names
     + Persistent group settings
   + Sorting
     + Sort by any column field
     + Ascending order organization
     + Persistent sort settings

**Figure 1**

![Custom table widget editing example.](http://docs.aws.amazon.com/connect/latest/adminguide/images/table-features-1.png)


**Figure 2**

![Another custom table widget editing example.](http://docs.aws.amazon.com/connect/latest/adminguide/images/table-features-2.png)


### Example configuration
<a name="table-example-configuration"></a>

```
{
    "Type": "Table",
    "Props": {
        "ColumnDefinitions": [
            {
                "Header": "Table column header"
                "Cell": {
                    "Content": {
                        "Props": {
                            "Variant": "Link",
                            "LinkOptions": {
                                "LinkType": "Drawer"
                            }
                        },
                        "Type": "TextContent",
                        "Children": ["string"]
                    }
                },
            }
        ]
    }
}
```

## Key value pair
<a name="key-value-pair"></a>

With the Key Value Pair component, you can create organized displays of related data points in a flexible, readable format.

### Overview
<a name="key-value-pair-overview"></a>

Create dynamic data displays by defining custom key-value relationships. This component is particularly useful for showing attribute pairs such as:
+ Customer details
+ Account information

### Features
<a name="key-value-pair-features"></a>

1. **Interactive link options**
   + Connect resource links
     + Link directly to related resources
     + Seamless navigation to:
       + Calculated attributes
       + Segments
     + Opens in new tab
   + External URL Links
     + Convert item value into URLs that you can choose
     + Opens in new tab
   + Drawer View Links
     + Open detailed information in side drawer
     + View complete details without leaving the page

1. Column configuration
   + Define 1-4 columns of key-value pairs

1. Organize pairs in logical groupings

**Figure 1**

![Custom key value pair widget editing example.](http://docs.aws.amazon.com/connect/latest/adminguide/images/key-value-pair-features-1.png)


**Figure 2**

![Another custom key value pair widget editing example.](http://docs.aws.amazon.com/connect/latest/adminguide/images/key-value-pair-features-2.png)


### Example configuration
<a name="key-value-pair-example-configuration"></a>

```
{
    "Type": "KeyValuePair",
    "Id": "UniqueId",
    "Props": {
        "Columns": 2,
        "Items": [
            {
                "Label": {
                    "Content": {
                        "Type": "TextContent",
                        "Id": "UniqueId",
                        "Props": {
                            "FontWeight": "bold"
                        },
                        "Children": ["Profile id"]
                    }
                },
                "Value": {
                    "Content": {
                        "Type": "TextContent",
                        "Id": "UniqueId",
                        "Props": {},
                        "Children": ["[string]"]
                    }
                }
            }
        ]
    }
}
```

**Note**  
This component does not currently support `ProfileObjects` in the UI builder.

## Key metric
<a name="key-metric"></a>

With the Key Metric component, you can prominently display critical business metrics, KPIs, and vital statistics in an easily digestible format.

### Overview
<a name="key-metric-overview"></a>

Create high-visibility metric displays that highlight important data points, trends, or status indicators. This component is ideal for showcasing:
+ Performance indicators
+ Critical measurements
+ Status summaries
+ Trend indicators

### Features
<a name="key-metric-features"></a>

1. **Large display text**

1. **Metric format**

1. **Interactive link options**
   + Connect resource links
     + Link directly to related resources
     + Seamless navigation to:
       + Calculated attributes
       + Segments
     + Opens in new tab
   + External URL links
     + Convert item value into URLs that you can choose
     + Opens in new tab
   + Drawer view links
     + Open detailed information in side drawer
     + View complete details without leaving the page

1. **Organize metrics layout**

**Figure 1**

![Custom key metric widget editing example.](http://docs.aws.amazon.com/connect/latest/adminguide/images/key-metric-features-1.png)


**Figure 2**

![Another custom key metric widget editing example.](http://docs.aws.amazon.com/connect/latest/adminguide/images/key-metric-features-2.png)


### Example configuration
<a name="key-metric-example-configuration"></a>

```
{
    "Type": "KeyMetrics",
    "Props": {
        "MetricDefinitions": [
            {
                "MetricLabel": "Total Revenue",
                "MetricValue": {
                    "Content": {
                        "Type": "TextContent",
                        "Props": {
                            "Format": "USD",
                            "FontSize": "large",
                            "FontWeight": "bold"
                        },
                        "Children": ["[string]"]
                    }
                },
                "Columns": 1
            }
        ]
    }
}
```

**Note**  
This component does not currently support `ProfileObjects` in the UI builder.

## Donut chart
<a name="donut-chart"></a>

The donut chart component enables visualization of sentiment scoring through a circular donut chart.

### Overview
<a name="donut-chart-overview"></a>

Create dynamic sentiment visualizations by defining custom scoring criteria. This component is particularly useful for showing:
+ Success metrics
+ Achievement rates
+ Risk assessments
+ Performance indicators

### Features
<a name="donut-chart-features"></a>

1. Sentiment Analysis Options
   + Positive Sentiment
     + Starts from zero
     + Tracks achievement against criteria:
       + Custom point values
       + Color-coded segments
       + Grey for unmet conditions
     + Shows success rate percentage
   + Negative Sentiment
     + Starts from maximum value
     + Tracks deductions:
       + Color-coded segments
       + Point reduction system
       + Green for remaining value
     + Shows final score

1. Calculated attribute value

1. Operator Options
   + Equal To
   + Not Equal To
   + Greater Than
   + Less Than

1. Value Condition

1. Allotted points per condition

**Figure 1: Positive sentiment example**

![Positive sentiment widget editing example.](http://docs.aws.amazon.com/connect/latest/adminguide/images/donut-chart-features-1.png)


**Figure 2: Negative sentiment example**

![Negative sentiment widget editing example.](http://docs.aws.amazon.com/connect/latest/adminguide/images/donut-chart-features-2.png)


### Example configuration
<a name="donut-chart-example-configuration"></a>

```
{
    "Type": "DonutChart",
    "Props": {
        "Variant": "PositiveSentiment",
        "ConditionDefinitions": [
            {
                "Title": "Customer Satisfaction",
                "Color": "#4CAF50",
                "CalculatedAttribute": "satisfaction_score",
                "Operator": "GREATER_THAN",
                "ValueCondition": 8,
                "Points": 10
            }
        ]
    }
}
```

**Note**  
**Donuts only support Calculated attributes as a data source at this time.**
**All condition definitions must include a title, color, calculated attribute, operator, value condition, and points value.**