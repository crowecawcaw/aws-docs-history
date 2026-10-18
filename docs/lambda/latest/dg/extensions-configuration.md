

# Configuring Lambda extensions
<a name="extensions-configuration"></a>

## Configuring extensions (.zip file archive)
<a name="using-extensions-config"></a>

You can add an extension to your Lambda Event Function as a [Lambda layer](chapter-layers.md). Using layers, you can share extensions across your organization or to the entire community of Lambda developers. You can add one or more extensions to a layer. You can register up to 10 extensions for an Event Function.

You add the extension to your Event Function using the same method as you would for any layer. For more information, see [Managing Lambda Event Function dependencies with layers](chapter-layers.md).

**Add an extension to your Event Function (console)**

1. Open the [Event Functions page](https://console.aws.amazon.com/lambda/home#/functions) of the Lambda console.

1. Choose an Event Function.

1. Choose the **Code** tab if it is not already selected.

1. Under **Layers**, choose **Edit**.

1. For **Choose a layer**, choose **Specify an ARN**.

1. For **Specify an ARN**, enter the Amazon Resource Name (ARN) of an extension layer.

1. Choose **Add**.

## Using extensions in container images
<a name="invocation-extensions-images"></a>

You can add extensions to your [container image](images-create.md). The ENTRYPOINT container image setting specifies the main process for the Event Function. Configure the ENTRYPOINT setting in the Dockerfile, or as an override in the Event Function configuration. 

You can run multiple processes within a container. Lambda manages the lifecycle of the main process and any additional processes. Lambda uses the [Extensions API](runtimes-extensions-api.md) to manage the extension lifecycle. 

### Example: Adding an external extension
<a name="extensions-images-ex1"></a>

An external extension runs in a separate process from the Lambda Event Function. Lambda starts a process for each extension in the `/opt/extensions/` directory. Lambda uses the Extensions API to manage the extension lifecycle. After the Event Function has run to completion, Lambda sends a `Shutdown` event to each external extension.

**Example of adding an external extension to a Python base image**  

```
FROM public.ecr.aws/lambda/python:3.11

# Copy and install the app
COPY /app /app
WORKDIR /app
RUN pip install -r requirements.txt

# Add an extension from the local directory into /opt/extensions
ADD my-extension.zip /opt/extensions
CMD python ./my-function.py
```

## Next steps
<a name="using-extensions-next"></a>

To learn more about extensions, we recommend the following resources:
+ For a basic working example, see [Building Extensions for AWS Lambda](https://aws.amazon.com/blogs/compute/building-extensions-for-aws-lambda-in-preview/) on the AWS Compute Blog.
+ For information about extensions that AWS Lambda Partners provides, see [Introducing AWS Lambda Extensions](https://aws.amazon.com/blogs/compute/introducing-aws-lambda-extensions-in-preview/) on the AWS Compute Blog.
+ To view available example extensions and wrapper scripts, see [AWS Lambda Extensions](https://github.com/aws-samples/aws-lambda-extensions) on the AWS Samples GitHub repository.