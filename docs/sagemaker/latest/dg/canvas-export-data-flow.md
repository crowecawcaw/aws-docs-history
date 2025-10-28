# Export a data flow

Exporting your data flow translates the operations that you've made in Data Wrangler and
exports it into a Jupyter notebook of Python code that you can modify and run. This can be
helpful for integrating the code for your data transformations into your machine
learning pipelines.

You can choose any data node in your data flow and export it. Exporting the data node
exports the transformation that the node represents and the transformations that precede
it.

###### To export a data flow as a Jupyter notebook

1. Navigate to your data flow.
2. Choose the ellipsis icon next to the node that you want to export.
3. In the context menu, hover over **Export**, and then hover
   over **Export via Jupyter notebook**.
4. Choose one of the following:
   - **SageMaker Pipelines**
   - **Amazon S3**
   - **SageMaker AI Inference Pipeline**
   - **SageMaker AI Feature Store**
   - **Python Code**

5. The **Export data flow as notebook** dialog box opens. Select
   one of the following:
   - **Download a local copy**
   - **Export to S3 location**

6. If you selected **Export to S3 location**, enter the Amazon S3
   location to which you want to export the notebook.
7. Choose **Export**.
   Your Jupyter notebook should either download to your local machine, or you can find it
   saved in the Amazon S3 location you specified.
