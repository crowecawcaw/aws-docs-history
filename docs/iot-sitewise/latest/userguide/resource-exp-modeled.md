

# Modeled
<a name="resource-exp-modeled"></a>

**Note**  
The SiteWise Monitor feature is no longer available to new customers. Existing customers can continue to use the service as normal. For more information, see [SiteWise Monitor availability change](https://docs.aws.amazon.com/iot-sitewise/latest/appguide/iotsitewise-monitor-availability-change.html).

 This section describes the process of selecting and visualization of modeled assets. 

## Selection of assets
<a name="resource-exp-modeled-asset-selection"></a>

Assets can be queried as follows:
+ Search for an asset name. Use a wildcard `*`. For example, `Wind*` returns asset names that start with the text `Wind`. You must [integrate with AWS IoT TwinMaker](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/sql.html#prereqs) to avail this feature.
+ All assets are listed by default.

From the assets listed, filter by name, description, ID, or asset model ID. Select one asset to list its properties (data streams) and alarms.

### Data stream selection
<a name="resource-exp-modeled-asset-selection-data"></a>

 Data streams are listed below the **Data Streams** menu. Filter the data streams listed by [Property](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_Property.html) metadata in the *https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/*. Select one or more data streams depending on the selected widget. 
+ **KPI** and **Gauge** support only a single data stream.
+ The remaining widgets support multiple data streams with multi-selection.

### Alarm selection
<a name="resource-exp-modeled-asset-selection-alarm"></a>

 AWS IoT SiteWise alarms are listed below the **Alarm Data Streams** menu. Filter the alarm data streams listed by alarm metadata. **name**, **input property**, and **composite model ID** are some metadata used for filtering. Select one or more data streams depending on the selected widget. 
+ **KPI** and **Gauge** support only a single alarm.
+ The remaining widgets support multiple alarms with multi-selection.

## Modeled assets visualization
<a name="resource-exp-modeled-asset-selection-procedure"></a>

1. Drag the widget to the canvas. Select the properties for each widget panel to construct a dashboard.

1. The **Filter** option filters the assets to choose the asset to visualize. Filtering is done by text, property or value. Filtering is for assets loaded into the browser, and not backend filtering.

1. **Search** to list an asset to add to your widget.

1. **Add** the asset to the widget in the canvas.

1. Choose **Reset** to select another asset, or make modifications to the asset chosen.

1. Save the dashboard. In the **Preview** mode, choose different assets from the drop down menu to monitor the properties under each asset without reconstructing the data panels.

**Note**  
 The configuration settings wheel on the right hand side displays **Preferences** for the user to choose like **Page size**, **Sticky first columns**, **Sticky last columns**, and **Column preferences**. Customize your preferences, and choose **Confirm** to apply the changes. 

![The IoT dashboard Project page with modeled assets shown.](http://docs.aws.amazon.com/iot-sitewise/latest/userguide/images/ai-dashboard-modeled-assets.png)
