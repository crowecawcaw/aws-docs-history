# Using Amazon Q Developer for line-by-line recommendations

Depending on your use case, Amazon Q may not be able to generate an entire function block
in one recommendation. However, Amazon Q can still provide line-by-line recommendations.

Go and GoLand
In this example, Amazon Q provides line-by-line recommendations.

![An example of the line-by-line completion feature.](images/jb-line-by-line-go.gif)

Here is another example of line-by-line recommendations, this time with a unit test.

![An example of the line-by-line completion feature.](images/jb-line-by-line-unit-test-go.gif)

C++ and CLion
In this example, Amazon Q provides line-by-line recommendations.

![An example of the line-by-line completion feature.](images/jb-line-by-line-cpp.gif)

Python
In the following image, the customer has written an initial comment indicating that they
want to publish a message to an Amazon CloudWatch Logs group. Given this context, Amazon Q is only able to
suggest the client initialization code in its first recommendation, as shown in the following
image.

![A screenshot that shows the first Amazon Q recommendation when prompted for a function that publishes messages to a CloudWatch Logs log group.](images/whisper-line-by-line-cwlogs-1.png)

However, if the user continues to request line-by-line recommendations, Amazon Q also
continues to suggest lines of code based on what's already been written.

![A screenshot that shows the next few Amazon Q recommendations that begin to form the implementation the function to publish messages to a CloudWatch Logs log group.](images/whisper-line-by-line-cwlogs-2.png)

###### Note

In the example above, `VPCFlowLogs` may not be the correct constant value. As
Amazon Q makes suggestions, remember to rename any constants as required.

Amazon Q can eventually complete the entire code block as shown in the following
image.

![A screenshot that shows the completed implementation of a code block that publishes messages to a CloudWatch Logs log group, based only on Amazon Q recommendations.](images/whisper-line-by-line-cwlogs-3.png)

In this example, Amazon Q provides recommendations, one line at at time.

![An example of the line-by-line completion feature.](images/python_sagemakerstudio_linebyline.gif)
