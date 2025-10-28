# Running code with Lambda

When you write a Lambda function, you are creating code that will run in a unique serverless environment. Understanding how Lambda actually runs your code involves two key aspects:
the [programming model](foundation-progmodel.md "foundation-progmodel.md") that defines how your code interacts with Lambda, and the [execution environment](lambda-runtime-environment.md "lambda-runtime-environment.md")
lifecycle that determines how Lambda manages your code's runtime environment.

## The Lambda programming model

[Programming model](foundation-progmodel.md "foundation-progmodel.md") functions as a common set of rules for how Lambda works with your code, regardless of whether you're writing in Python, Java, or any other supported language.
The programming model includes your runtime and handler.

1. Lambda receives an event.
2. Lambda uses the runtime (like Python or Java) to prepare the event in a format your code can use.
3. The runtime sends the formatted event to your handler.
4. Your handler processes the event using the code you've written in your Lambda function.

Essential to this model is the _handler_, where Lambda sends events to be processed by your code.
Think of it as the entry point to your code. When Lambda receives an event, it passes this event and some context information to your handler.
The handler then runs your code to process these events - for example, it might read a file when it's uploaded to Amazon S3, analyze an image, or update a database.
Once your code finishes processing an event, the handler is ready to process the next one.

## The Lambda execution model

While the programming model defines how Lambda interacts with your code, [Execution environment](lambda-runtime-environment.md "lambda-runtime-environment.md") is where Lambda actually runs your function — it's a secure, isolated compute space created specifically for your function. Each environment follows a lifecycle of three phases.

1. **Initialization:** Lambda creates the environment and gets everything ready to run your function. This includes setting up your chosen runtime, loading your code, and running any startup code you've written.
2. **Invocation:** When events arrive, Lambda uses this environment to run your function. The environment can process many events over time, one after another.
   As more events come in, Lambda creates additional environments to handle the increased demand. When demand drops, Lambda stops environments that are no longer needed.
3. **Shutdown:** Eventually, Lambda will shut down environments. Before doing this, it gives your function a chance to clean up any remaining tasks.

This environment handles important aspects of running your function. It provides your function with memory and a `/tmp` directory for temporary storage.
It maintains resources like database connections between invocations, so your function can reuse them. It offers features like _provisioned concurrency_, where Lambda prepares environments in advance to improve performance.
