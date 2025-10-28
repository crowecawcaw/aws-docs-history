# Use `DeleteDistribution` with an AWS SDK or CLI

The following code examples show how to use `DeleteDistribution`.

Action examples are code excerpts from larger programs and must be run in context. You can see this action in
context in the following code example:

- [Get started with CloudFront](example_cloudfront_GettingStarted_section.md "example_cloudfront_GettingStarted_section.md")

CLI

**AWS CLI**

**To delete a CloudFront distribution**

The following example deletes the CloudFront distribution with the ID
`EDFDVBD6EXAMPLE`. Before you can delete a distribution, you must disable it.
To disable a distribution, use the update-distribution command. For more information, see the
update-distribution examples.

When a distribution is disabled, you can delete it. To delete a distribution,
you must use the `--if-match` option to provide the distribution's `ETag`.
To get the `ETag`, use the get-distribution or
get-distribution-config command.

```
`aws cloudfront delete-distribution \
 --id `EDFDVBD6EXAMPLE` \
 --if-match `E2QWRUHEXAMPLE``

```

When successful, this command has no output.

- For API details, see
  [DeleteDistribution](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/delete-distribution.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/delete-distribution.html")
  in _AWS CLI Command Reference_.

Java

**SDK for Java 2.x**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/cloudfront#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/cloudfront#code-examples").

The following code example updates a distribution to _disabled_, uses a waiter that waits for the change to be deployed, then deletes the distribution.

```
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import software.amazon.awssdk.core.internal.waiters.ResponseOrException;
import software.amazon.awssdk.services.cloudfront.CloudFrontClient;
import software.amazon.awssdk.services.cloudfront.model.DeleteDistributionResponse;
import software.amazon.awssdk.services.cloudfront.model.DistributionConfig;
import software.amazon.awssdk.services.cloudfront.model.GetDistributionResponse;
import software.amazon.awssdk.services.cloudfront.waiters.CloudFrontWaiter;

public class DeleteDistribution {
        private static final Logger logger = LoggerFactory.getLogger(DeleteDistribution.class);

        public static void deleteDistribution(final CloudFrontClient cloudFrontClient, final String distributionId) {
                // First, disable the distribution by updating it.
                GetDistributionResponse response = cloudFrontClient.getDistribution(b -> b
                                .id(distributionId));
                String etag = response.eTag();
                DistributionConfig distConfig = response.distribution().distributionConfig();

                cloudFrontClient.updateDistribution(builder -> builder
                                .id(distributionId)
                                .distributionConfig(builder1 -> builder1
                                                .cacheBehaviors(distConfig.cacheBehaviors())
                                                .defaultCacheBehavior(distConfig.defaultCacheBehavior())
                                                .enabled(false)
                                                .origins(distConfig.origins())
                                                .comment(distConfig.comment())
                                                .callerReference(distConfig.callerReference())
                                                .defaultCacheBehavior(distConfig.defaultCacheBehavior())
                                                .priceClass(distConfig.priceClass())
                                                .aliases(distConfig.aliases())
                                                .logging(distConfig.logging())
                                                .defaultRootObject(distConfig.defaultRootObject())
                                                .customErrorResponses(distConfig.customErrorResponses())
                                                .httpVersion(distConfig.httpVersion())
                                                .isIPV6Enabled(distConfig.isIPV6Enabled())
                                                .restrictions(distConfig.restrictions())
                                                .viewerCertificate(distConfig.viewerCertificate())
                                                .webACLId(distConfig.webACLId())
                                                .originGroups(distConfig.originGroups()))
                                .ifMatch(etag));

                logger.info("Distribution [{}] is DISABLED, waiting for deployment before deleting ...",
                                distributionId);
                GetDistributionResponse distributionResponse;
                try (CloudFrontWaiter cfWaiter = CloudFrontWaiter.builder().client(cloudFrontClient).build()) {
                        ResponseOrException<GetDistributionResponse> responseOrException = cfWaiter
                                        .waitUntilDistributionDeployed(builder -> builder.id(distributionId)).matched();
                        distributionResponse = responseOrException.response()
                                        .orElseThrow(() -> new RuntimeException("Could not disable distribution"));
                }

                DeleteDistributionResponse deleteDistributionResponse = cloudFrontClient
                                .deleteDistribution(builder -> builder
                                                .id(distributionId)
                                                .ifMatch(distributionResponse.eTag()));
                if (deleteDistributionResponse.sdkHttpResponse().isSuccessful()) {
                        logger.info("Distribution [{}] DELETED", distributionId);
                }
        }
}


```

- For API details, see
  [DeleteDistribution](../../../goto/SdkForJavaV2/cloudfront-2020-05-31/DeleteDistribution.md "../../../goto/SdkForJavaV2/cloudfront-2020-05-31/DeleteDistribution.md")
  in _AWS SDK for Java 2.x API Reference_.

For a complete list of AWS SDK developer guides and code examples, see
[Using CloudFront with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
