# Using the Amazon Q data integration in

AWS Glue

Amazon SageMaker Unified Studio supports the [Amazon Q data integration](../../../glue/latest/dg/q.md "../../../glue/latest/dg/q.md") in AWS Glue. It helps data engineers and ETL
developers create data integration jobs using natural language letting you automate aspects of
code authoring.

When using the Amazon Q data integration in AWS Glue, in the Jupyter Lab IDE, you
enter comments using natural language instructions, and then the PySpark kernel generates the
code on your behalf. You can customize the generated code to meet your own needs.

1. Open a Python notebook, and ensure the kernel is configured to use a PySpark
   connection.
2. You can request a prompt response by adding a comment and then placing it in a prompt,
   which will start Amazon Q processing.
3. If the prompt is AWS Glue related, the data integration generates a
   AWS Glue job script using PySpark.
4. Alternatively, you can continue to use your default auto-completions from Amazon Q
   Developer. If a prompt isn't Glue related, Amazon Q Developer will use autocomplete
   instead.
