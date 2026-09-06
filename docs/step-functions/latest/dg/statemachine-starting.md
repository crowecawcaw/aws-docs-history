

# Starting state machine executions in Step Functions
<a name="statemachine-starting"></a>

A state machine *execution* occurs when an AWS Step Functions state machine runs and performs its tasks. Each Step Functions state machine can have multiple simultaneous executions, which you can initiate from the [Step Functions console](https://console.aws.amazon.com/states/home?region=us-east-1#/), or by using the AWS SDKs, the Step Functions API actions, or the AWS Command Line Interface (AWS CLI). An execution receives JSON input and produces JSON output. You can start a Step Functions execution in the following ways:
+ Start an execution in the Step Functions console.

  You can start a state machine in the console, watch the execution, and debug failures.
+ Call the [StartExecution](https://docs.aws.amazon.com/step-functions/latest/apireference/API_StartExecution.html) API action.
+ Use Amazon EventBridge to [start an execution](tutorial-cloudwatch-events-s3.md) in response to an event.
+ Use Amazon EventBridge Scheduler to [start a state machine execution](using-eventbridge-scheduler.md) on a schedule.
+ Start a [nested workflow execution](concepts-nested-workflows.md) from a Task state.
+ Start an execution with [Amazon API Gateway](tutorial-api-gateway.md).

**Tip**  
To learn how to monitor running executions, see the tutorial: [Examining state machine executions in Step Functions](debug-sm-exec-using-ui.md)