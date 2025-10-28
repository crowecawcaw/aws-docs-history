# Finding group visualization

Amazon Detective provides an interactive visualization of finding groups. This visualization
is designed to help you investigate issues faster and more thoroughly with less effort.
The finding group **Visualization** panel displays the findings and
entities involved in a finding group. You can use this interactive visualization to
analyze, understand, and triage the impact of the finding group. This panel helps
visualize the information presented in the **Involved entities** and
**Involved findings** table. From the visual presentation, you can
select findings or entities for further analysis.

Detective finding groups with aggregated findings are a cluster of findings that are
connected to the same type of resource. With aggregated findings, you can quickly assess
the makeup of a finding group and interpret security issues faster. In the finding
groups details panel, similar findings are combined and you can expand the findings to
view relatively similar findings together. For example, an evidence node, which has
informational findings and medium findings of the same type are aggregated. Currently,
you can view the title, source, type, and severity of finding groups with aggregated
findings.

From this interactive panel, you can:

- Use **Run investigation** to generate an investigation
  report. The generated report details anomalous behavior that indicates
  compromise. For more details, see [Detective Investigations](investigations-about.md "investigations-about.md").
- View more details on finding groups with aggregated findings to analyze the
  involved evidence, entities, and findings.
- View the labels for the entities and findings to identify the affected
  entities with potential security issues. You can toggle off the **Label**.
- Rearrange the entities and findings to better understand their
  interconnectedness. Isolate entities and findings from a group by moving the
  selected item in the finding group.
- Select the evidences, entities, and findings to view more details about them.
  To select multiple items, choose `command/control` and
  either choose the items, or drag and drop them using your pointer.
- Adjust the layout to fit all entities and findings into the finding group window. View what entity types are prevalent in a finding group.

###### Note

The finding group **Visualization** panel supports the display of
finding groups with up to 100 entities and findings.

You can use the drop-down to view the findings and entities in a
**Radial**, **Circle**,
**Force-directed**, or **Grid** layout. The
**Radial** layout provides improved visualization for easier data
interpretation. The **Force-directed** layout positions the entities
and findings so that links are a consistent length between items and the links are
distributed evenly. This helps to reduce overlapping. The layout that you select defines
the placement of findings in the **Visualization** panel.

## Timeline layout

The timeline layout provides a dynamic way to visualize how your finding groups evolve over time. This allows you to see the progression of events, helping you to better understand the sequence and potential causality of security incidents using Detective.

Use the timeline slider at the bottom of the visualization panel to select a specific point in time. The visualization will update to show the state of your finding group at that moment. The play button that allows you to automatically progress through the timeline. Click the play button to start the animation. The visualization will update in real-time, showing how the finding group changes over time. Use the pause button to stop the animation at any point.

You can now filter findings based on their severity level using the Filter dropdown. When you apply a filter, the visualization will update to show only the findings that match your selected severity level. The filter only affects the findings shown in the timeline, not in the full Finding Group visualization. This allows you to quickly focus on high-priority issues or investigate specific types of findings.

You can use the filtering feature in combination with the Timeline Layout to see how findings of different severity levels emerge and evolve over time.

**Enhanced Investigation Workflow**

With the addition of the Timeline Layout and filtering capabilities, you can now conduct even more comprehensive investigations:

1. Start by viewing the entire finding group using one of the static layouts (Radial, Circle, Force-directed, or Grid).
2. Use timelines to understand how the situation developed over time.
3. Use the play button to automatically progress through the timeline, watching for key moments or patterns.
4. Pause at significant points to investigate further.
5. Apply filters to focus on findings of specific severity levels.
6. Use the keyboard shortcuts and selection tools to dive deeper into entities and findings of interest.

This enhanced workflow allows for a more nuanced and thorough investigation of complex security scenarios. You can conduct more efficient and effective security investigations, leading to faster incident resolution and improved overall security posture.

## Keyboard shortcuts

You can use the following keyboard shortcuts to interact with the finding group
Visualization panel:

- Click – Selects a single node, deselects all other nodes, deselects all nodes if white
  space is clicked.
- Ctrl + Click – Selects a single node, does not deselect other nodes.
- Drag – Pans the view.
- Ctrl + Drag – Marquee selects, does not deselect other nodes.
- Shift + Drag – Marquee selects, deselects all other nodes.
- Arrow keys – Changes the focus between nodes.
- Ctrl + Space – Selects or deselects the currently focused node.
- Shift + Arrow keys – Changes the focus between nodes and selects them.

The dynamic **Legend** changes based on the entities and findings in your current graph. It helps you identify what each visual element represents.
