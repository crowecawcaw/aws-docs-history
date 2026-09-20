

# View step dependencies as a graph
<a name="view-step-dependency-graph"></a>

The **Steps** list can show your steps as a table or as a dependency graph. The graph shows each step as a node and each dependency as an arrow that points from a step to the step that depends on it, so you can see the order in which your steps run. Each node shows the step's name and run status.

Jobs with dependencies are created by workflows that submit dependent steps, such as a job that renders frames and then publishes the result. If a job has no step dependencies, the graph reports that none were found.

![The Steps panel in graph view, with five step nodes connected by dependency arrows that flow from left to right.](https://docs.aws.amazon.com/deadline-cloud/latest/userguide/images/monitor/step-dependency-graph.png)


**To view the step dependency graph**

1. Select a job from the **Jobs** list.

1. At the top of the **Steps** list, choose **Graph**. To return to the table, choose **Table**.

In the graph, you can do the following:
+ Choose a node to select its step. The **Tasks** list then shows the tasks in that step.
+ On a node, choose the actions menu, then choose **View step dependencies** to filter the panel to the steps that the selected step depends on and the steps that depend on it.
+ Move a node to make a crowded part of the graph easier to read. To move a node with the keyboard, select the node, and then use the arrow keys. To move it in larger increments, hold down Shift. To return every node to the position that the graph computed for it, choose **Reset layout**.
+ Change the direction that dependencies flow. The graph flows from left to right by default. To flow it from top to bottom instead, choose **Flow top to bottom**. To flow it from left to right again, choose **Flow left to right**. Changing the direction returns any node that you moved to its computed position. The Deadline Cloud monitor remembers the direction that you choose and uses it the next time that you view a graph.

## Graph controls
<a name="step-graph-controls"></a>

The graph controls are in the lower-left corner of the graph. To see what a control does, point to it or move the keyboard focus to it. The graph provides the following controls.

**Zoom in**  
Magnifies the graph so that you can read the steps in a crowded area.

**Zoom out**  
Shrinks the graph so that you can see more of it at once.

**Fit view**  
Resizes and centers the graph so that every step fits in the panel. Choose this control to return to a full view of the graph after you move or zoom it.

**Flow top to bottom, Flow left to right**  
Changes the direction that dependencies flow. This control names the direction that it changes the graph to, so it shows **Flow top to bottom** while the graph flows from left to right.

**Reset layout**  
Returns every node to the position that the graph computed for it, which discards the position of any node that you moved.