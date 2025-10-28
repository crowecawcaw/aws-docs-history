# Starting or stopping an Amazon EventBridge pipe

By default, a pipe is `Running` and processes events when it's created.

If you create a pipe with Amazon SQS, Kinesis, or DynamoDB sources, pipe creation can typically take a minute or two.

If you create a pipe with Amazon MSK, self managed Apache Kafka, or Amazon MQ sources, pipes creation can take up to ten minutes.

###### To

create a pipe without processing events using the console

- Turn off the **Activate pipe** setting.

###### To create a pipe without processing events programmatically

- In your API call, set the `DesiredState` to `Stopped`.

###### To start or stop an existing pipe using the console

- On the **Pipes settings** tab, under **Activation**, for
  **Activate pipe**, turn **Active** on or off.

###### To start or stop an existing pipe programmatically

- In your API call, set the `DesiredState` parameter to either `RUNNING` or `STOPPED`.
  There can be a delay between when a pipe is `STOPPED`
  and when it no longer processes events:

- For Amazon SQS and stream sources, this delay is typically less than two minutes.
- For Amazon MQ and Apache Kafka sources, this delay may be up to fifteen minutes.
