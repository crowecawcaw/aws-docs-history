# Integrate Views with Connect Resources

You can create Views used in Guides that poll live data sources through specified intervals with View integrations. View integrations are view-level configurations available from the UI builder's global settings panel, as shown below.

The view integrations panel allows you to configure and reference data on your view. Start by configuring a new tool to integrate with. A tool is a specific integration point between the View and a Connect resource. The following properties are required to configure a tool:

1. Integration Name: The custom name for the integration that will be used later to reference data on the view itself
2. Integration Type: The format for the integration between the view and the Connect resource
3. Tool: The integration source that the View will integrate with, such as Flow modules
4. Version or Alias: The flow module version/alias that the view will call to fetch new information
5. Enable refresh (seconds): A boolean value to call the integration as the view is running in a guide
6. Refresh intervals: The intervals at which the View will make a call to the integration to fetch the information
7. Tool input object: A JSON object representing the data sent from the view to the source (e.g., Flow module) to fetch the latest relevant information to update the view
   Once an integration is configured, you will be able to use that view to reference outputs from the integration. References displayed in the UI builder are based on the output data available from the particular integration.

To utilize the reference data from your integration, you must first understand how to reference the data from the UI components and their properties. Similarly to how contact attributes are referenced in Flows and Views `($.Attributes.MyCustomAttribute)`, you can reference output data for the integration using the following syntax: `$.#[IntegrationName].[ReferenceObject]`. Keep in mind that you are responsible to make sure that the reference object used is returned in the right format the view’s component property will accept. To understand the integration output reference visit the module configuration page.

At run-time, when a view with an integration is loaded, it will populate data from the integration as defined in the view schema. In addition, if you set refresh intervals, the view will invoke the integration at each interval, and if there is new data, the view will prompt the user to refresh the view with the latest information.
