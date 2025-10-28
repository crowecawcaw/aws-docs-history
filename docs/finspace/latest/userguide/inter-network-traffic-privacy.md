After careful consideration, we decided to end support for Amazon FinSpace, effective October 7, 2026. Amazon FinSpace will no longer accept new customers beginning October 7, 2025. As an existing customer with an Amazon FinSpace environment created before October 7, 2025, you can continue to use the service as normal. After October 7, 2026, you will no longer be able to use Amazon FinSpace. For more information, see
[Amazon FinSpace end of support](amazon-finspace-end-of-support.md "amazon-finspace-end-of-support.md").

# Inter-network traffic privacy in

Amazon FinSpace Dataset browser

**Take following network considerations into account when using
the Amazon FinSpace web application**

1. To use FinSpace web application, you need access to the internet.
2. You will need access to a [compatible
   browser](supported-browsers.md "supported-browsers.md").
3. Your connections to FinSpace are protected through the use of TLS. So that you can
   access the FinSpace notebook environment that runs on SageMaker Studio, you must allow
   access to HTTPS and WebSockets Secure (wss://) protocol. You will need to
   allow-list access to SageMaker to access the Notebook environment. An example for
   allow-listing string is `*.us-east-1.sagemaker.aws`. You may change the
   region depending on the region you have setup FinSpace.
4. By default, FinSpace notebooks allow public internet access. You can request the
   access be blocked by contacting AWS support.
