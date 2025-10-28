#

Working with streaming operations in AWS Glue interactive sessions

##

Switching streaming session type

Use the AWS Glue interactive sessions configuration magic, `%streaming`, to define the job you are running
and initialize a streaming interactive session.

##

Sampling input stream for interactive development

One tool we have derived to help enhance the interactive experience in AWS Glue interactive sessions is the addition
of a new method under `GlueContext` to obtain a snapshot of a stream in a static DynamicFrame. `GlueContext` allows
you to inspect,
interact and implement your workflow.

With the `GlueContext` class instance, you will be able to
locate the method `getSampleStreamingDynamicFrame`. Required arguments for this method are:

- `dataFrame`: The Spark Streaming DataFrame
- `options`: See available options below

Available options include：

- **windowSize**: This is also called Microbatch Duration. This parameter will determine how long a
  streaming query will wait after previous batch was triggered. This parameter value must be smaller than `pollingTimeInMs`.
- **pollingTimeInMs**: The total length of time the method will run. It will fire off at least one micro batch
  to obtain sample records from the input stream.
- **recordPollingLimit**: This parameter helps you limit the total number of records you will poll from the stream.
- (Optional) You can also use `writeStreamFunction` to apply this custom function to every record sampling function. See below for
  examples in Scala and Python.

Scala

```
val sampleBatchFunction = (batchDF: DataFrame, batchId: Long) => {//Optional but you can replace your own forEachBatch function here}
val jsonString: String = s"""{"pollingTimeInMs": "10000", "windowSize": "5 seconds"}"""
val dynFrame = glueContext.getSampleStreamingDynamicFrame(YOUR_STREAMING_DF, JsonOptions(jsonString), sampleBatchFunction)
dynFrame.show()

```

Python

```
def sample_batch_function(batch_df, batch_id):
       //Optional but you can replace your own forEachBatch function here
options = {
            "pollingTimeInMs": "10000",
            "windowSize": "5 seconds",
        }
glue_context.getSampleStreamingDynamicFrame(YOUR_STREAMING_DF, options, sample_batch_function)

```

###### Note

When the sampled `DynFrame` is empty, it could be caused by a few reasons:

- The Streaming source is set to "Latest" and no new data has been ingested during the sampling period.
- The polling time is not enough to process the records it ingested. Data won't show up unless the whole batch has been processed.

##

Running streaming applications in interactive sessions

In AWS Glue interactive sessions, you can run a the AWS Glue streaming application like how you would
create a streaming application in the AWS Glue Console. Since interactive sessions is session-based,
encountering exceptions in the runtime does not cause the session to stop.
We now have the added benefit of developing your batch function iteratively. For example:

```
def batch_function(data_frame, batch_id):
    log.info(data_frame.count())
    invalid_method_call()
glueContext.forEachBatch(frame=streaming_df, batch_function = batch_function, options = {**})

```

In the example above, we included an invalid usage of a method and unlike regular AWS Glue jobs
which will exit the entire application, the user's coding context and definitions are fully preserved and the session is still operational.
There is no need to bootstrap a new cluster and rerun all the preceding transformation. This allows you to focus on quickly
iterating your batch function implementations to obtain desirable outcomes.

It is important to note that Interactive Session evaluates each statement in a blocking manner
so that the session will only execute one statement at a time. Since streaming queries are continuous and never ending,
sessions with active streaming queries won't be able to handle any follow up statements unless they are interrupted.
You can issue the interruption command directly from Jupyter Notebook and our kernel will handle the cancellation for you.

Take the following sequence of statements which are waiting for execution as an example:

```
Statement 1:
      val number = df.count()
      #Spark Action with deterministic result
      Result: 5

Statement 2:
      streamingQuery.start().awaitTermination()
      #Spark Streaming Query that will be executing continously
      Result: Constantly updated with each microbatch

Statement 3:
      val number2 = df.count()
      #This will not be executed as previous statement will be running indefinitely

```
