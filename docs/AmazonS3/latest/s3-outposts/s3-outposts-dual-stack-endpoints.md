# Using S3 on Outposts dual-stack endpoints

S3 on Outposts dual-stack endpoints support requests to S3 on Outposts buckets over IPv6
and IPv4. This section describes how to use S3 on Outposts dual-stack endpoints.

###### Topics

- [S3 on Outposts dual-stack endpoints](#s3-outposts-dual-stack-endpoints-description "#s3-outposts-dual-stack-endpoints-description")
- [Using dual-stack endpoints from the AWS CLI](#s3-outposts-dual-stack-endpoints-cli "#s3-outposts-dual-stack-endpoints-cli")
- [Using S3 on Outposts dual-stack endpoints from the AWS SDKs](#s3-outposts-dual-stack-endpoints-sdks "#s3-outposts-dual-stack-endpoints-sdks")

## S3 on Outposts dual-stack endpoints

When you make a request to a dual-stack endpoint, the S3 on Outposts bucket URL resolves
to an IPv6 or an IPv4 address. For more information about accessing an
S3 on Outposts bucket over IPv6, see [Making requests to S3 on Outposts over IPv6](S3OutpostsIPv6-access.md "S3OutpostsIPv6-access.md").

To access an S3 on Outposts bucket through a dual-stack endpoint, use a path-style
endpoint name. S3 on Outposts supports only Regional dual-stack endpoint names, which
means that you must specify the Region as part of the name.

For a dual-stack path-style FIPs endpoint, use the following naming convention:

```
s3-outposts-fips.`region`.api.aws
```

For dual-stack non-FIPS endpoint, use the following naming convention:

```
s3-outposts.`region`.api.aws
```

###### Note

Virtual hosted-style endpoint names aren't supported in S3 on Outposts.

## Using dual-stack endpoints from the AWS CLI

This section provides examples of AWS CLI commands used to make requests to a dual-stack
endpoint. For instructions on setting up the AWS CLI, see [Getting started by using the AWS CLI and SDK for Java](S3OutpostsGSCLIJava.md "S3OutpostsGSCLIJava.md").

You set the configuration value `use_dualstack_endpoint` to
`true` in a profile in your AWS Config file to direct all Amazon S3 requests
made by the `s3` and `s3api` AWS CLI commands to the dual-stack
endpoint for the specified Region. You specify the Region in the configuration file or
in a command using the `--region` option.

When using dual-stack endpoints with the AWS CLI, only `path` addressing
style is supported. The addressing style, set in the configuration file, determines
whether the bucket name is in the hostname or in the URL. For more information, see
[s3outposts](../../../cli/latest/reference/s3outposts.md "../../../cli/latest/reference/s3outposts.md") in the _AWS CLI User
Guide_.

To use a dual-stack endpoint via the AWS CLI, use the `--endpoint-url`
parameter with the `http://s3.dualstack.`region`.amazonaws.com` or
`https://s3-outposts-fips.`region`.api.aws`
endpoint for any `s3control` or `s3outposts` commands.

For example:

```
`$`  aws s3control list-regional-buckets --endpoint-url https://s3-outposts.`region`.api.aws
```

## Using S3 on Outposts dual-stack endpoints from the AWS SDKs

This section provides examples of how to access a dual-stack endpoint by using the
AWS SDKs.

### AWS SDK for Java 2.x dual-stack endpoint example

The following examples show how to use the `S3ControlClient` and
`S3OutpostsClient` classes to enable dual-stack endpoints when
creating an S3 on Outposts client using the AWS SDK for Java 2.x. For instructions on creating
and testing a working Java example for Amazon S3 on Outposts, see [Getting started by using the AWS CLI and SDK for Java](S3OutpostsGSCLIJava.md "S3OutpostsGSCLIJava.md").

###### Example– Create an `S3ControlClient` class with dual-stack endpoints enabled

```
import com.amazonaws.AmazonServiceException;
import com.amazonaws.SdkClientException;
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.s3control.S3ControlClient;
import software.amazon.awssdk.services.s3control.model.ListRegionalBucketsRequest;
import software.amazon.awssdk.services.s3control.model.ListRegionalBucketsResponse;
import software.amazon.awssdk.services.s3control.model.S3ControlException;


public class DualStackEndpointsExample1 {

    public static void main(String[] args) {
        Region clientRegion = Region.of("`us-east-1`");
        String accountId = "`111122223333`";
        String navyId = "`9876543210`";

        try {
            // Create an S3ControlClient with dual-stack endpoints enabled.
            S3ControlClient s3ControlClient = S3ControlClient.builder()
                                                             .region(clientRegion)
                                                             .dualstackEnabled(true)
                                                             .build();
            ListRegionalBucketsRequest listRegionalBucketsRequest = ListRegionalBucketsRequest.builder()
                                                                                              .accountId(accountId)
                                                                                              .outpostId(navyId)
                                                                                              .build();

            ListRegionalBucketsResponse listBuckets = s3ControlClient.listRegionalBuckets(listRegionalBucketsRequest);
            System.out.printf("ListRegionalBuckets Response: %s%n", listBuckets.toString());
        } catch (AmazonServiceException e) {
            // The call was transmitted successfully, but Amazon S3 on Outposts couldn't process
            // it, so it returned an error response.
            e.printStackTrace();
        }
        catch (S3ControlException e) {
            // Unknown exceptions will be thrown as an instance of this type.
            e.printStackTrace();
        } catch (SdkClientException e) {
            // Amazon S3 on Outposts couldn't be contacted for a response, or the client
            // couldn't parse the response from Amazon S3 on Outposts.
            e.printStackTrace();
        }
    }
}
```

###### Example– Create an `S3OutpostsClient` with dual-stack endpoints enabled

```
import com.amazonaws.AmazonServiceException;
import com.amazonaws.SdkClientException;
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.s3outposts.S3OutpostsClient;
import software.amazon.awssdk.services.s3outposts.model.ListEndpointsRequest;
import software.amazon.awssdk.services.s3outposts.model.ListEndpointsResponse;
import software.amazon.awssdk.services.s3outposts.model.S3OutpostsException;


public class DualStackEndpointsExample2 {

    public static void main(String[] args) {
        Region clientRegion = Region.of("`us-east-1`");

        try {
            // Create an S3OutpostsClient with dual-stack endpoints enabled.
            S3OutpostsClient s3OutpostsClient = S3OutpostsClient.builder()
                                                              .region(clientRegion)
                                                              .dualstackEnabled(true)
                                                              .build();
            ListEndpointsRequest listEndpointsRequest = ListEndpointsRequest.builder().build();

            ListEndpointsResponse listEndpoints = s3OutpostsClient.listEndpoints(listEndpointsRequest);
            System.out.printf("ListEndpoints Response: %s%n", listEndpoints.toString());
        } catch (AmazonServiceException e) {
            // The call was transmitted successfully, but Amazon S3 on Outposts couldn't process
            // it, so it returned an error response.
            e.printStackTrace();
        }
        catch (S3OutpostsException e) {
            // Unknown exceptions will be thrown as an instance of this type.
            e.printStackTrace();
        } catch (SdkClientException e) {
            // Amazon S3 on Outposts couldn't be contacted for a response, or the client
            // couldn't parse the response from Amazon S3 on Outposts.
            e.printStackTrace();
        }
    }
}
```

If you're using the AWS SDK for Java 2.x on Windows, you might have to set the following
Java virtual machine (JVM) property:

```
java.net.preferIPv6Addresses=true
```
