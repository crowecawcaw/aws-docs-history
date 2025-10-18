# 
 Using a data table widget 
 in a CloudWatch dashboard

**Table properties**

A data table has a default set of properties that don’t require any changes to be made to the 
 options or source. These properties include a sticky label column, all summary columns enabled, 
 datapoints rounded, and their units converted.

Each data table widget can have the following properties. The information
 about each property includes how to configure it in the JSON source of the dashboard. For more information
 about dashboard JSON, see 
 [Dashboard Body Structure and Syntax](../APIReference/CloudWatch-Dashboard-Body-Structure.md "../APIReference/CloudWatch-Dashboard-Body-Structure.md").



**Summary**
Summary columns are a new property introduced with the data table widget. These columns are 
 a specific subset of summaries of your current table. For example, the **Sum** summary 
 is a sum of all displayed datapoints in its row. The summary columns are not the same as 
 CloudWatch statistics. Represented in source as:



```
 "table": {
        "summaryColumns": [
            "MIN",
            "MAX",
            "SUM",
            "AVG"
        ]
    },
```

**Thresholds**
Use this to apply thresholds to your table. When a data point falls within a threshold, 
 its cell is highlighted with the threshold color. Represented in source as:



```
"annotations": {
    "horizontal": [
        {
            "label": string,
            "value": int,
            "fill": "above" | "below"
        }
    ]
}
```

Unit in label column
To display what unit is associated with the metric, you can enable this option to 
 display the unit in the label column beside the label. Represented in source as:



```
"yAxis": {
    "left": {
        "showUnits": true | false
    }
}
```

**Invert rows and columns**
This transforms the table so that the datapoints swap from columns to rows, and the 
 metrics become columns. Represented in source as:



```
 "table": {
    "layout": "vertical" | "horizontal"
}
```

**Sticky summary columns**
This makes the summary columns sticky, so that they remain in view while you scroll.
 The label is already sticky. 
 Represented in source as:



```
"table": {
    "stickySummary": true | false
}
```

**Display only summary columns**
This prevents the columns of datapoints from being displayed, so that only the label
 and summary columns are displayed. Represented in source as:



```
 "table": {
    "showTimeSeriesData": false | true
}
```

**Live data**
Displays the most recent data point, even if it is not yet fully 
 aggregated. Represented in source as:



```
"liveData": true | false
```

**Number widget format**
Displays as many digits as can fit in the cell, before rounding and converting. Represented in source as:



```
"singleValueFullPrecision": true | false
```
