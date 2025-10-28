# Use AWS Lambda layers

There are two ways you can use layers to enable CodeGuru in Lambda functions using
Python. The preferred method uses a wrapper script and only works for applications that run
on Python 3.8 or 3.9. The second method works for Python 3.7, and can also be used for Python 3.8
and 3.9 if you already have a lambda wrapper or if the preferred method otherwise does not work.

###### For applications that run on Python 3.8 or 3.9 (preferred)

1. Add the CodeGuru Profiler layer to Lambda. Choose **Specify an ARN** and add
   `arn:aws:lambda:`region`:157417159150:layer:AWSCodeGuruProfilerPythonAgentLambdaLayer:11`.
   For more information on adding a Lambda layer, see [AWS Lambda layers](../../../lambda/latest/dg/chapter-layers.md "../../../lambda/latest/dg/chapter-layers.md").
2. Add the following environment variable:
   `AWS_LAMBDA_EXEC_WRAPPER=/opt/codeguru_profiler_lambda_exec`
3. Add an environment variable with your profiling group name or ARN. For information
   on using your ARN, see the table listed in [Apply the CodeGuru Profiler
   function decorator to your handler function](python-lambda-command-line.md "python-lambda-command-line.md").

###### Note

You can only have one Lambda wrapper script. If you are currently using one, try the
solution for applications that run on Python 3.7, 3.8 or 3.9.

###### For applications that run on Python 3.7, 3.8 or 3.9

1. Add the CodeGuru Profiler layer to Lambda. Choose **Specify an ARN** and
   `arn:aws:lambda:`region`:157417159150:layer:AWSCodeGuruProfilerPythonAgentLambdaLayer:11`.
   For more information on adding a Lambda layer, see [AWS Lambda layers](../../../lambda/latest/dg/chapter-layers.md "../../../lambda/latest/dg/chapter-layers.md").
2. Set the environment variable, `HANDLER_ENV_NAME_FOR_CODEGURU` to your
   handler function.
3. Change the Lambda handler function to
   `codeguru_profiler_agent.aws_lambda.lambda_handler.call_handler`.
4. Add an environment variable with your profiling group name or ARN. For information
   on using your ARN, see the table listed in [Apply the CodeGuru
   Profiler function decorator to your handler function](python-lambda-command-line.md "python-lambda-command-line.md").

###### Note

You can only have up to five layers for a Lambda function. If you are already using
five layers, see [Apply the CodeGuru Profiler function
decorator to your handler function](python-lambda-command-line.md "python-lambda-command-line.md").
