# Customize at the edge with Lambda@Edge

Lambda@Edge is an extension of AWS Lambda. Lambda@Edge is a compute service that lets you
execute functions that customize the content that Amazon CloudFront delivers. You can author Node.js
or Python functions in the Lambda console in one AWS Region, US East (N. Virginia).

After you create the function, you can add triggers using the Lambda console or CloudFront
console so that the functions run in AWS locations that are closer to the viewer, without
provisioning or managing servers. Optionally, you can use Lambda and CloudFront API operations to
set up your functions and triggers programmatically.

Lambda@Edge scales automatically, from a few requests per day to thousands per second.
Processing requests at AWS locations closer to the viewer instead of on origin servers
significantly reduces latency and improves the user experience.

###### Note

Lambda@Edge isn't supported with gRPC requests. For more information. see [Using gRPC with CloudFront distributions](distribution-using-grpc.md "distribution-using-grpc.md").

###### Topics

- [How Lambda@Edge works with requests
  and responses](lambda-edge-event-request-response.md "lambda-edge-event-request-response.md")
- [Ways to use Lambda@Edge](lambda-edge-ways-to-use.md "lambda-edge-ways-to-use.md")
- [Get started with Lambda@Edge functions (console)](lambda-edge-how-it-works.md "lambda-edge-how-it-works.md")
- [Set up IAM permissions and roles for
  Lambda@Edge](lambda-edge-permissions.md "lambda-edge-permissions.md")
- [Write and create a Lambda@Edge
  function](lambda-edge-create-function.md "lambda-edge-create-function.md")
- [Add triggers for a Lambda@Edge
  function](lambda-edge-add-triggers.md "lambda-edge-add-triggers.md")
- [Test and debug Lambda@Edge
  functions](lambda-edge-testing-debugging.md "lambda-edge-testing-debugging.md")
- [Delete Lambda@Edge functions and
  replicas](lambda-edge-delete-replicas.md "lambda-edge-delete-replicas.md")
- [Lambda@Edge event structure](lambda-event-structure.md "lambda-event-structure.md")
- [Work with requests and
  responses](lambda-generating-http-responses.md "lambda-generating-http-responses.md")
- [Lambda@Edge example functions](lambda-examples.md "lambda-examples.md")
