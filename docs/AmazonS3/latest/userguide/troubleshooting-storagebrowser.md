# Troubleshooting Storage Browser for S3

If you’re experiencing issues with Storage Browser for S3, make sure to review the following troubleshooting tips:


* Avoid trying to use the same token (`idToken` or `accessToken`) for multiple requests. Tokens can't be reused. This will result in a request failure.
* Make sure that the IAM credentials that you provide to the Storage Browser component includes permissions to invoke the `s3:GetDataAccess` operation. Otherwise, your end users won’t be able to access your data.
Alternatively, you can check the following resources:


* Storage Browser for S3 is backed by AWS Support. If you need assistance, contact the
 [AWS Support
 Center](https://console.aws.amazon.com/support/home#/ "https://console.aws.amazon.com/support/home#/").
* If you’re having trouble with Storage Browser for S3 or would like to submit feedback, visit
 the [Amplify GitHub page](https://github.com/aws-amplify/amplify-ui "https://github.com/aws-amplify/amplify-ui").
* If you discover a potential security issue in this project, you can notify AWS
 Security through the [AWS Vulnerability Reporting](https://aws.amazon.com/security/vulnerability-reporting/ "https://aws.amazon.com/security/vulnerability-reporting/") page.
