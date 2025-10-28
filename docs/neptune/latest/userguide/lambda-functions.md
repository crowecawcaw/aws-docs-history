# Using AWS Lambda functions in Amazon Neptune

AWS Lambda functions have many uses in Amazon Neptune applications. Here we provide
general guidance for using Lambda functions with any of the popular Gremlin drivers and
language variants, and specific examples of Lambda functions written in Java, JavaScript,
and Python.

###### Note

The best way to use Lambda functions with Neptune has changed with recent
engine releases. Neptune used to leave idle connections open long after a Lambda execution
context had been recycled, potentially leading to a resource leak on the server. To mitigate
this, we used to recommend opening and closing a connection with each Lambda invocation.
Starting with engine version 1.0.3.0, however, the idle connection timeout has been reduced
so that connections no longer leak after an inactive Lambda execution context has been
recycled, so we now recommend using a single connection for the duration of the execution
context. This should include some error handling and back-off-and-retry boilerplate code
to handle connections being closed unexpectedly.
