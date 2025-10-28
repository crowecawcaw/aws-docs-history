# Create a lip-sync application with Amazon Polly using an AWS SDK

The following code example shows how to create a lip-sync application with Amazon Polly.

Python

**SDK for Python (Boto3)**

Shows how to use Amazon Polly and Tkinter to create a lip-sync application that
displays an animated face speaking along with the speech synthesized by Amazon Polly.
Lip-sync is accomplished by requesting a list of visemes from Amazon Polly that match
up with the synthesized speech.

- Get voice metadata from Amazon Polly and display it in a Tkinter application.
- Get synthesized speech audio and matching viseme speech marks from Amazon Polly.
- Play the audio with synchronized mouth movements in an animated face.
- Submit asynchronous synthesis tasks for long texts and retrieve the output from
  an Amazon Simple Storage Service (Amazon S3) bucket.

For complete source code and instructions on how to set up and run, see the full example on
[GitHub](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/polly#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/polly#code-examples").

###### Services used in this example

- Amazon Polly

For a complete list of AWS SDK developer guides and code examples, see
[Using Amazon Polly with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
