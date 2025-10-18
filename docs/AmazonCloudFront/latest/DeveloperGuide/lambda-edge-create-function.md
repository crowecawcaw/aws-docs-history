# Write and create a Lambda@Edge
 function

To use Lambda@Edge, you *write* the code for your
 AWS Lambda function. To help you write Lambda@Edge functions, see the following
 resources:


* [Lambda@Edge event structure](lambda-event-structure.md "lambda-event-structure.md")
 – Understand the event structure to use with Lambda@Edge.
* [Lambda@Edge example functions](lambda-examples.md "lambda-examples.md") –
 Example functions, such as A/B testing and generating an HTTP redirect.
The programming model for using Node.js or Python with Lambda@Edge is the same as using
 Lambda in an AWS Region. For more information, see [Building Lambda
 functions with Node.js](https://docs.aws.amazon.com/lambda/latest/dg/lambda-nodejs.html "https://docs.aws.amazon.com/lambda/latest/dg/lambda-nodejs.html") or [Building Lambda functions with Python](https://docs.aws.amazon.com/lambda/latest/dg/lambda-python.html "https://docs.aws.amazon.com/lambda/latest/dg/lambda-python.html") in the
 *AWS Lambda Developer Guide*.

In your Lambda@Edge function, include the `callback` parameter and return
 the applicable object for request or response events:


* **Request events** – Include the
 `cf.request` object in the response.


If you're generating a response, include the `cf.response` object
 in the response. For more information, see [Generate HTTP
 responses in request triggers](lambda-generating-http-responses.md#lambda-generating-http-responses-in-requests "lambda-generating-http-responses.md#lambda-generating-http-responses-in-requests").
* **Response events** – Include the
 `cf.response` object in the response.
After you write your own code or use one of the examples, you then create the function
 in Lambda. To create a function or edit an existing one, see the following topics:

###### Topics

* [Create a Lambda@Edge
 function](lambda-edge-create-in-lambda-console.md "lambda-edge-create-in-lambda-console.md")
* [Edit a Lambda function](lambda-edge-edit-function.md "lambda-edge-edit-function.md")
 After you create the function in Lambda, you set up Lambda to run the function based on
 specific CloudFront events, which are called *triggers*. For more
 information, see [Add triggers for a Lambda@Edge
 function](lambda-edge-add-triggers.md "lambda-edge-add-triggers.md").
