# Error handling

There are three primary types of errors that you want to handle in your application code.
These are input validation errors, AWS Responsible AI (RAI) input deflection errors, and
RAI output deflection errors. These errors are unique to Amazon Nova Canvas.

Input validation errors occur when you use an unsupported value for an input parameter.
For example, a width value that doesn’t match one of the supported resolutions, an input
image that exceeds the maximum allowed size, or a `maskImage` that contains
colors other than pure black and white. All input validation errors are expressed as a
`ValidationException` which contains a message string describing the cause of
the problem.

RAI input deflection errors occur when any of the input text values or images are
determined to violate the AWS Responsible AI policy. These errors are expressed as a
`ValidationException` with one of the following messages:

- Input text validation message - “This request has been blocked by our content
  filters. Please adjust your text prompt to submit a new request.”
- Input image validation message - “This request has been blocked by our content
  filters. Please adjust your input image to submit a new request.”
  RAI output deflection errors occur when an image is generated but it is misaligned with
  the AWS Responsible AI policy. When this occurs, an exception is not used. Instead, a
  successful response is returned, and its structure contains an error field which is a string
  with one of the following values:

- If all requested images violate RAI policy - “All of the generated images have
  been blocked by our content filters.”
- If some, but not all, requested images violate RIA policy - “Some of the generated
  images have been blocked by our content filters.”
