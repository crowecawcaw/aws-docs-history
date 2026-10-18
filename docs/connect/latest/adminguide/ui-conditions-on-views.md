

# Build conditional UIs with views
<a name="ui-conditions-on-views"></a>

UI conditions change a component's properties based on how users interact with other components in the same view. For example, when a user changes a dropdown, a container can be hidden. Use conditions to tailor a view for agents, end customers, or supervisors, based on the task.

To create a UI condition, drag a supported component onto the canvas in the UI builder. In the **Customize** panel, choose the **UI conditions** tab. The tab has the following fields:
+ **Change Type** – The property of the selected component that you want to update based on a condition.
  + **Visibility** – Makes a component visible or hidden.
  + **DefaultValue** – Updates the default value(s) of a component.
  + **Required** – Updates the required property of a component.
  + **Disable** – Makes a component disabled or enabled.
  + **Options** – Updates the options available for the user to select from a component.
+ **Select trigger component** – The component that triggers the applied condition.
+ **Apply condition when** – The operation evaluated based on the value of the trigger component.
+ **Apply when value matches** – The value of the trigger component that is evaluated to trigger the condition.
+ **Apply results** – The change to apply when the condition is met.

A component with conditions has a dashed outline in the UI builder. To remove a condition, choose the trash icon in the **UI conditions** tab.