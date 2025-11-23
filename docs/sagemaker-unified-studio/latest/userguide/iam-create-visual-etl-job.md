# Create a Visual ETL job in IAM-based

domains

To create a job using Visual ETL in Amazon SageMaker Unified Studio IAM-based domains:

1. Log in to Amazon SageMaker Unified Studio.
2. Navigate to the Visual ETL tool using the left menu, selecting "Visual ETL".
3. Choose "Create Visual job" to open the Visual ETL editor.
4. Give the job a name when you begin authoring the job and choose "save".
5. Open the "Add nodes" menu by choosing the plus icon and select a node, choosing your
   node from one of the three tabs: "Data sources", "Transforms", or "Data targets".
6. Drag a source component onto the canvas.
7. Configure the component by choosing the node and editing the configurations, to
   connect to your data source.
8. Add transformation components as needed, connecting them in the desired
   order.
9. Drag a data target onto the canvas and configure it to specify where the processed
   data should be stored.
10. Connect the components to create a complete job.
11. Choose the "Checklist" button to check for any configuration errors.
12. Choose "Save" when you are done correcting all errors.
13. Select "Run" to execute it immediately or choose the schedule icon to create a
    reoccurring run schedule.
