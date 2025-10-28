# Transform data

This documentation topic is designed
for Grafana workspaces that support **Grafana version
10.x**.

For Grafana workspaces that support Grafana version 9.x, see
[Working in Grafana version 9](using-grafana-v9.md "using-grafana-v9.md").

For Grafana workspaces that support Grafana version 8.x, see
[Working in Grafana version 8](using-grafana-v8.md "using-grafana-v8.md").

Transformations are a powerful way to manipulate data returned by a query before
the system applies a visualization. Using transformations, you can:

- Rename fields
- Join time series data
- Perform mathematical operations across queries
- Use the output of one transformation as the input to another
  transformation
  For users that rely on multiple views of the same dataset, transformations offer
  an efficient method of creating and maintaining numerous dashboards.

You can also use the output of one transformation as the input to another
transformation, which results in a performance gain.

###### Note

Sometimes the system cannot graph transformed data. When that happens, click
the **Table view** toggle above the visualization to switch to
a table view of the data. This can help you understand the final result of your
transformations.

## Transformation types

Grafana provides a number of ways that you can transform data. There is a
complete list of transformation functions below.

## Order of transformations

When there are multiple transformations, Grafana applies them in the order
they are listed. Each transformation creates a result set that then passes on to
the next transformation in the processing pipeline.

The order in which Grafana applies transformations directly impacts the
results. For example, if you use a Reduce transformation to condense all the
results of one column into a single value, then you can only apply
transformations to that single value.

## Add a transformation function to

data

The following steps guide you in adding a transformation to data. This
documentation does not include steps for each type of transformation.

###### To add a transformation to a panel

1. Navigate to the panel where you want to add one or more
   transformations.
2. Hover over any part of the panel to display the actions menu on the
   top right corner.
3. From the actions menu choose **Edit**.
4. Select the **Transform** tab.
5. Select a transformation. A transformation row appears where you
   configure the transformation options.
6. To apply another transformation, Choose **Add
   transformation**. This transformation acts on the result
   set returned by the previous transformation.

## Debug a transformation

To see the input and the output result sets of the transformation, choose the
debug (bug) icon on the right side of the transformation row. This will display
the input data, and the result of the transformation as output.

The input and output results sets can help you debug a transformation.

## Disable a transformation

You can disable or hide a transformation by choosing the show (eye) icon on
the top right of the transformation row. This disables the applied actions of
that specific transformation and can help to identify issues when you change
several transformations one after another.

## Filter a transformation

If your transformation uses more than one query, you can filter these, and
apply the selected transformation to only one of the queries. To do this, choose
the filter icon on the top right of the transformation row. This opens a
dropdown with a list of queries used on the panel. From here, you can select the
query you want to transform.

You can also filter by annotations (which includes exemplars) to apply
transformations to them. When you do so, the list of fields changes to reflect
those in the annotation or exemplar tooltip.

The filter icon is always displayed if your panel has more than one query or
source of data (that is panel or annotation data), but it may not work if
previous transformations for merging the queries' outputs are applied. This is
because one transformation takes the output of the previous one.

## Delete a transformation

We recommend that you remove transformations that you don’t need. When you
delete a transformation, you remove the data from the visualization.

Prerequisites:

Identify all dashboards that rely on the transformation and inform impacted
dashboard users.

###### To delete a transformation

1. Open a panel for editing.
2. Select the **Transform** tab.
3. Choose the trash icon next to the transformation you want to
   delete.
