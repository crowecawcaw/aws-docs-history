# Use Step by Step Guides in Workspace for Managers

You can utilize Guides in the persona-based Workspace to run structured workflows that virtually any Connect user can follow. Before proceeding, make sure you've created a persona-based workspace first.

Once in the UI builder, find the "Connect Application" component and drag it onto the canvas. This component allows you to embed a first-party Connect application in the View. You can configure the component with the following properties:

1. Application Namespace: The type of application to embed in the component
2. ContactFlowId: If 'Guide' is selected as the application namespace, choose the guide's contact flow ID to run in the component.
   When using the Connect application component, users can start the guide by clicking the "Begin" button, which will create the background chat contact to operate the guide. Once a guided workflow is completed, users can start the guide from the beginning of the flow by clicking the "Restart" button. Keep in mind that nesting the guide application component in a view already used in a guide is not supported. The guide in the Connect application component can only be embedded in a static view used as a page in persona-based Workspaces.
