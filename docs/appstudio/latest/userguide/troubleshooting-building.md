# Troubleshooting in the application studio

This topic contains troubleshooting and debugging guidance for issues when building applications.

## Using the debug panel

To assist with live debugging while you're building your apps, App Studio provides a collapsible builder debug panel
that spans the pages, automations, and data tabs of the application studio. This panel shows both errors and warnings. While warnings
serve as actionable suggestions, such as resources that haven't been configured, errors must be resolved to succesfully preview or publish your app.
Each error or warning includes a **View** link which can be used to navigate to the location of the issue.

The debug panel automatically updates with new errors or warnings as they occur, and the errors or warnings
automatically disappear once resolved. The state of these warning and error messages is persisted when you leave the builder.

## JavaScript expression syntax and data type handling

App Studio features JavaScript error detection, highlighting errors by underlining your code with red lines.
These compile errors, which will prevent the app from building successfully, indicate issues such as typos, invalid references, invalid operations,
and incorrect outputs for required data types. See the following list for common issues:

1. **Errors caused by renaming resources:** When JavaScript expressions reference resource names in App Studio,
   changing those names will cause the expressions to be incorrect and produce errors. You can view these errors in the debug panel.
2. **Data type issues:** Data type mismatches will produce errors in your app. For example, if an
   automation is configured to accept a parameter of type `String`, but a component is configured to send a value of
   type `Integer`, an error will be occur. Check that data types match between appropriate resources, including components, automations,
   and data entities and actions. You may need to change the type of the value in a JavaScript expression.
