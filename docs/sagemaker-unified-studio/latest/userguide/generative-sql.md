# Generative SQL

Amazon SageMaker Unified Studio allows you to generate SQL queries using natural language through the SageMaker
Data Agent. The agent understands the context of your data and generates SQL queries that you
can use in your analysis. In IAM-based domains, the SageMaker Data Agent provides multi-turn
conversational SQL development with step-by-step planning and error correction. For more
information, see [Getting started with the SageMaker Data Agent for Query Editor](data-agent-query-editor.md "data-agent-query-editor.md").

You can find the Generative SQL tool in the Query Editor of a project.

![The SageMaker Data Agent panel in the Query Editor, showing sample prompts and the chat interface.](images/data-agent/qe-welcome.png)
The Generative SQL interface understands the context of your data and lets you ask natural
language questions like "What are the columns in the job success table?", in order to generate
SQL. When you ask a question, an SQL query is generated based on the question you have provided.
After creating a query with the tool you can add the generated SQL to your querybook with a
single click.

Once you have created a query, the query can be saved for later use by yourself or others with access to
the project. Query results can be exported in CSV of JSON formats. You can create visualizations directly in the Query editor.
