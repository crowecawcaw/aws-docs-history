

# Tutorial: View state machine details
<a name="stepfunctions-configure"></a>

The AWS Batch console displays a list of your state machines in the current AWS Region that contain at least one workflow step that submits a AWS Batch job.

Choose a state machine to view a graphical representation of the workflow. Steps highlighted in blue represent AWS Batch jobs. Use the graph controls to zoom in, zoom out, and center the graph.

**Note**  
When a AWS Batch job is [dynamically referenced with JsonPath](https://docs.aws.amazon.com/step-functions/latest/dg/amazon-states-language-paths.html) in the state machine definition, the function details cannot be shown in the AWS Batch console. Instead, the job name is listed as a **Dynamic reference**, and the corresponding steps in the graph are grayed out.

**To view state machine details**

1. Open the AWS Batch console [Workflow orchestration powered by Step Functions page](https://console.aws.amazon.com/batch/home#stepfunctions).

1. Choose a state machine.

   The AWS Batch console opens the **Details** page.

For more information, see [Step Functions](https://docs.aws.amazon.com/step-functions/latest/dg/welcome.html) in the *AWS Step Functions Developer Guide*.