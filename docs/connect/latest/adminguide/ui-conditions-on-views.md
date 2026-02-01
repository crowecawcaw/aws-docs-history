# Build conditional UIs with View

The UI conditions capability of Views enables customers to change properties of components within a View based on user interaction with other components within that same View. For example, when a user updates an input value in component A, such as a dropdown, component B, such as a container, will be hidden in the View. Conditions enable you to create tailored experiences for your agents, end customers, or supervisors based on the given needs of the task or interaction.

To create a UI condition, visit the UI builder and drag a supported component onto the canvas. Visit the settings panel of the component on the right side of the screen and click into the UI conditions tab. The UI conditions tab is organized to collect the following inputs:

1. Change Type: The property of the selected component that you would like to update based on a condition
   - Visibility: Makes a component visible or hidden
   - DefaultValue: Updates the default value(s) of a component
   - Required: Updates the required property of a component
   - Disable: Makes a component disabled or enabled
   - Options: Updates the options available for the user to select from a component

2. Select trigger component: The component that will trigger the applied condition
3. Apply condition when: The operation evaluated based on the value of the trigger component
4. Apply when value matches: The value of the trigger component that will be evaluated to trigger the condition
5. Apply results: The desired change to the selected component once the evaluation on the trigger component is met
   When conditions are set on a component, it will be outlined in dashed lines in the UI builder. You can remove conditions by clicking on the trash icon in the conditions tab in the component's settings panel.
