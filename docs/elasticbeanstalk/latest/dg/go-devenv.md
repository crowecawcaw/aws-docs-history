# Setting up your Go development environment for Elastic Beanstalk

This topic provides instructions to set up a Go development environment to test your application locally prior to deploying it to AWS Elastic Beanstalk.
It also references websites that provide installation instructions for useful tools.

## Installing Go

To run Go applications locally, install Go. If you don't need a specific version, get the latest version that Elastic Beanstalk supports. For a list of supported
versions, see [Go](../platforms/platforms-supported.md#platforms-supported.go "../platforms/platforms-supported.md#platforms-supported.go") in the _AWS Elastic Beanstalk Platforms_
document.

Download Go at [https://golang.org/doc/install](https://golang.org/doc/install "https://golang.org/doc/install").

## Installing the AWS SDK for Go

If you need to manage AWS resources from within your application, install the AWS SDK for Go by using the following command.

```
$ `go get github.com/aws/aws-sdk-go`
```

For more information, see [AWS SDK for Go](https://aws.amazon.com/sdk-for-go/ "https://aws.amazon.com/sdk-for-go/").
