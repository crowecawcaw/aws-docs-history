

# Use views to customize the user interface for agents, customers, and other user personas in Connect Customer
<a name="view-resources-sg"></a>

*Views* are custom user interfaces (UIs) that you can use to customize the user experience for agents (in the agent workspace), customers (in chat conversations), and other user personas in Connect Customer. For example, you can use views to display contact attributes to an agent, provide forms for entering disposition codes, provide call notes, and present UI pages for walking agents through step-by-step guides. 

Connect Customer includes [AWS managed views](view-resources-managed-view.md). You can also create your own views in the [UI builder](no-code-ui-builder.md) or with Connect Customer APIs.

When you configure a view in the [Show view](show-view-block.md) block, you can define both static and dynamic content. Each view has three parts: a template, an input schema, and actions.

**Tip**  
For the best data mapping experience, use the **Set JSON** option in the [Show view](show-view-block.md) block. You can reference any flow namespace in the **Show view** block, including `$.External`, so any view can show data from external systems. You can combine data from Connect Customer and other sources in one view.