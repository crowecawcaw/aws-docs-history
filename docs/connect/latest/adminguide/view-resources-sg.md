# Views: UI templates to customize an agent's

workspace in Amazon Connect

_Views_ are UI templates that you can use to customize your agent's
workspace. For example, you can use views to display contact attributes to an agent,
provide forms for entering disposition codes, provide call notes, and present UI pages
for walking agents through step-by-step guides.

Amazon Connect includes a set of views that you can add your agent's workspace, and you can
also create your own views using our public APIs.

When configuring views in flows using the [Show view](show-view-block.md "show-view-block.md") block, you can define both static and
dynamic content for each view. The content for a specific view is composed of three key
elements: a template, an input schema, and actions.

###### Tip

For the best data mapping experience, we recommend using the **Set
JSON** option in the [Show view](show-view-block.md "show-view-block.md") block. All namespaces in flows can be
referenced in the **Show View** block, including
`$.External`, so you will be able to share data from external systems
to your agent in whichever view you create. You can mix and match data from Amazon Connect
and other sources in order to create a consolidated UI for your agent.
