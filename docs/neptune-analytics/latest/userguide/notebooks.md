# Using notebooks with Neptune Analytics

The Neptune managed open-source [graph-notebook
project](https://github.com/aws/graph-notebook "https://github.com/aws/graph-notebook") provides a plethora of [Jupyter](Jupyter.md "Jupyter.md") extensions and sample
notebooks that make it easy to interact with and learn to use a Neptune Analytics graph.

These graph notebooks support a suite of intuitive Jupyter line- and cell-magic commands.
The magic commands abstract away much of the initial setup typically required for using Neptune Analytics,
and take care of SigV4 signing of requests. They can create graph connections, load data,
run openCypher queries, and interact with various Neptune Analytics APIs.

You can find a list of the full set of Neptune graph-notebook magics and their
options [in
the Neptune Userguide](../../../neptune/latest/userguide/notebooks-magics.md "../../../neptune/latest/userguide/notebooks-magics.md"). However, only the following magics are compatible with
Neptune Analytics graphs:

- [%seed](../../../neptune/latest/userguide/notebooks-magics.md#notebooks-line-magics-seed "../../../neptune/latest/userguide/notebooks-magics.md#notebooks-line-magics-seed")  
  (adds sample data to a graph).
- [%load](../../../neptune/latest/userguide/notebooks-magics.md#notebooks-line-magics-load "../../../neptune/latest/userguide/notebooks-magics.md#notebooks-line-magics-load")  
  (uses the [neptune-load()](batch-load.md "batch-load.md") openCypher
  integration to let you batch-load data).
- [%status](../../../neptune/latest/userguide/notebooks-magics.md#notebooks-line-magics-status "../../../neptune/latest/userguide/notebooks-magics.md#notebooks-line-magics-status") or
  [%get_graph](../../../neptune/latest/userguide/notebooks-magics.md#notebooks-line-magics-get-graph "../../../neptune/latest/userguide/notebooks-magics.md#notebooks-line-magics-get-graph")   (gets status information about the graph).
- [%%opencypher or %%oc](../../../neptune/latest/userguide/notebooks-magics.md#notebooks-cell-magics-opencypher "../../../neptune/latest/userguide/notebooks-magics.md#notebooks-cell-magics-opencypher")  
  (issues an openCypher query).
- [%opencypher_status, or %oc_status](../../../neptune/latest/userguide/notebooks-magics.md#notebooks-line-magics-opencypher-status "../../../neptune/latest/userguide/notebooks-magics.md#notebooks-line-magics-opencypher-status")  
  (retrieves query status for, or cancels, an openCypher query).
- [%%graph_notebook_config](../../../neptune/latest/userguide/notebooks-magics.md#notebooks-cell-magics-graph-notebook-config "../../../neptune/latest/userguide/notebooks-magics.md#notebooks-cell-magics-graph-notebook-config")  
  (displays a JSON object containing the configuration that the notebook is using).
- [%graph_notebook_host](../../../neptune/latest/userguide/notebooks-magics.md#notebooks-line-magics-graph-notebook-host "../../../neptune/latest/userguide/notebooks-magics.md#notebooks-line-magics-graph-notebook-host")  
  (sets the line input as the notebook's host).
- [%graph_notebook_version](../../../neptune/latest/userguide/notebooks-magics.md#notebooks-line-magics-graph-notebook-version "../../../neptune/latest/userguide/notebooks-magics.md#notebooks-line-magics-graph-notebook-version")  
  (returns the Neptune workbench notebook release number).
- [%graph_notebook_service](../../../neptune/latest/userguide/notebooks-magics.md#notebooks-line-magics-graph-notebook-service "../../../neptune/latest/userguide/notebooks-magics.md#notebooks-line-magics-graph-notebook-service")  
  (sets the line input as the Neptune service name to use).
- [%%graph_notebook_vis_options](../../../neptune/latest/userguide/notebooks-magics.md#notebooks-cell-magics-graph-notebook-vis-options "../../../neptune/latest/userguide/notebooks-magics.md#notebooks-cell-magics-graph-notebook-vis-options")  
  (lets you set visualization options for the notebook).
- [%summary](../../../neptune/latest/userguide/notebooks-magics.md#notebooks-line-magics-summary "../../../neptune/latest/userguide/notebooks-magics.md#notebooks-line-magics-summary")  
  (retrieves graph summary information).
- [%graph_reset](../../../neptune/latest/userguide/notebooks-magics.md#notebooks-line-magics-reset-graph "../../../neptune/latest/userguide/notebooks-magics.md#notebooks-line-magics-reset-graph")  
  (empties the data from a graph).
  You can use a Neptune graph notebook to generate an interactive visualization of the results returned
  from an openCypher query, and use options to customize the appearance of the visualized graph (see
  [Graph visualization
  in the Neptune workbench](../../../neptune/latest/userguide/notebooks-visualization.md "../../../neptune/latest/userguide/notebooks-visualization.md")).

## Take advantage of all the sample notebooks

A wide variety of sample Jupyter notebooks are available in the Neptune
[graph-notebook project](https://github.com/aws/graph-notebook "https://github.com/aws/graph-notebook").
Some of these are purpose-built for learning how to get the most of a Neptune Analytics graph and its
powerful built-in algorithms in the context of common real-world applications.

After installing the graph-notebook project either locally or on SageMaker AI, you
should be able to find sample notebooks under the notebook directory,
`../Neptune/02-Neptune-Analytics`.
