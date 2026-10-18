

# Integrate views with Connect Customer resources
<a name="integrate-views-with-connect-resources"></a>

With view integrations, a view in a guide can poll a live data source at set intervals. You configure integrations for the whole view, in the global settings of the **Customize** panel in the UI builder.

To add an integration, configure a tool. A tool is the connection between the view and a Connect Customer resource. A tool needs the following properties:
+ **Integration Name** – The name you use to reference the integration's data in the view.
+ **Integration Type** – The type of integration between the view and the Connect Customer resource.
+ **Tool** – The resource the view integrates with, such as a flow module.
+ **Version or Alias** – The flow module version or alias that the view calls to fetch new information.
+ **Enable refresh (seconds)** – Whether the view calls the integration again while it runs in a guide.
+ **Refresh intervals** – How often the view calls the integration to fetch new information.
+ **Tool input object** – A JSON object that the view sends to the source, such as a flow module, to fetch the latest information.

**Note**  
Polling works best with one tab open. If the guide is open in more than one tab, each view polls the data source, which can cause throttling and leave some views out of date.

After you configure an integration, components in the view can reference its outputs. The UI builder shows the references that the integration's output makes available.

To reference integration data in a component property, use the syntax `$.#[IntegrationName].[ReferenceObject]`. Contact attributes use the same pattern, such as `$.Attributes.MyCustomAttribute`. Make sure that the reference object returns data in the format that the component property accepts. To see what an integration outputs, open the flow module's configuration page.

When a view with an integration loads, it fills in data from the integration as the view schema defines. If you set refresh intervals, the view calls the integration at each interval. When there's new data, the view prompts the user to refresh.