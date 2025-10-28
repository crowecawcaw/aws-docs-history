# Error handling

The way errors are communicated back to the client varies depending on the type of error
that occurs. In this section, we focus only on the error conditions that are unique to the
Amazon Nova model. The three primary types of errors you will want to handle in your application
code are **input validation** errors, **Responsible AI (RAI) input deflection** errors, and **RAI
output deflection** errors.

**Input validation:** Input validation errors occur when you
use an unsupported value for an input parameter. For example, an out-of-bounds value for
temperature, or incorrect format of the input `image`. All input validation
errors are expressed as a **ValidationException** which
contains a message string describing the cause of the problem.

**RAI input deflection** errors occur when any of the input
text values or images are determined to violate the AWS Responsible AI policy. These
errors are expressed as a **ValidationException** with one of
the following messages:

- **Input text** validation message: "This request has
  been blocked by our content filters. Please adjust your text prompt to submit a new
  request."
- **Input image** validation message: "This request has
  been blocked by our content filters. Please adjust your input image to submit a new
  request."
- **Input Video** validation message: "This request has
  been blocked by our content filters. Please adjust your input video to submit a new
  request."
  RAI output deflection errors occur when an the output is generated but it is determined to
  be misaligned with the AWS Responsible AI policy. When this occurs, an exception is not
  used. Instead, a successful response is returned, and its structure contains an
  `error` field which is a string with one of the following values:

- **Output text** validation message: "The generated
  text has been blocked by our content filters."
