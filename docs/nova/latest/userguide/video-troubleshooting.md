# Video generation models

There are three primary types of errors that you want to handle in your application code.
These are input validation errors, AWS Responsible AI (RAI) input deflection errors, and
RAI output deflection errors. These errors are unique to Amazon Nova Reel.

Input validation errors occur if your request is malformed or if you use an unsupported
value for an input parameter—for example, a `duration` value that does not match
one of the supported values or an input `image` that is not exactly 1280x720
resolution. All input validation errors are expressed as a **ValidationException** which contains a message string describing the cause of
the problem. This exception will be raised when calling the
`start_async_invoke()` method of the Amazon Bedrock Runtime.

RAI input deflection errors occur when the input text value or input image are determined
to violate [AWS core dimensions of responsible AI](https://aws.amazon.com/ai/responsible-ai/ "https://aws.amazon.com/ai/responsible-ai/"). These errors are expressed as a **ValidationException** with one of the following messages:

- **Input text** validation message: "This request has
  been blocked by our content filters. Please adjust your text prompt to submit a new
  request."
- **Input image** validation message: "This request has
  been blocked by our content filters. Please adjust your input image to submit a new
  request."
  RAI output deflection errors occur when a video is generated but it is determined to be
  misaligned with [our core dimensions of responsible AI](https://aws.amazon.com/ai/responsible-ai/ "https://aws.amazon.com/ai/responsible-ai/"). When this occurs, an exception is not used.
  Instead, the job is marked as "Failed" and the file is never written to Amazon S3. When querying
  the status of the job (for example, using `get_invoke()`), the response will have
  a `status` field value of "Failed" and a `failureMessage` field value
  of "The generated video has been blocked by our content filters."
