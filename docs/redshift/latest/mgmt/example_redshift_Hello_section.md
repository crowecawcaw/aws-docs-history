Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Hello Amazon Redshift

The following code examples show how to get started using Amazon Redshift.

Go

**SDK for Go V2**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/gov2/redshift#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/gov2/redshift#code-examples").

```

package main

import (
	"context"
	"fmt"

	"github.com/aws/aws-sdk-go-v2/aws"
	"github.com/aws/aws-sdk-go-v2/config"
	"github.com/aws/aws-sdk-go-v2/service/redshift"
)

// main uses the AWS SDK for Go V2 to create a Redshift client
// and list up to 10 clusters in your account.
// This example uses the default settings specified in your shared credentials
// and config files.
func main() {
	ctx := context.Background()
	sdkConfig, err := config.LoadDefaultConfig(ctx)
	if err != nil {
		fmt.Println("Couldn't load default configuration. Have you set up your AWS account?")
		fmt.Println(err)
		return
	}
	redshiftClient := redshift.NewFromConfig(sdkConfig)
	count := 20
	fmt.Printf("Let's list up to %v clusters for your account.\n", count)
	result, err := redshiftClient.DescribeClusters(ctx, &redshift.DescribeClustersInput{
		MaxRecords: aws.Int32(int32(count)),
	})
	if err != nil {
		fmt.Printf("Couldn't list clusters for your account. Here's why: %v\n", err)
		return
	}
	if len(result.Clusters) == 0 {
		fmt.Println("You don't have any clusters!")
		return
	}
	for _, cluster := range result.Clusters {
		fmt.Printf("\t%v : %v\n", *cluster.ClusterIdentifier, *cluster.ClusterStatus)
	}
}



```

- For API details, see
  [DescribeClusters](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/redshift#Client.DescribeClusters "https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/redshift#Client.DescribeClusters")
  in _AWS SDK for Go API Reference_.

Java

**SDK for Java 2.x**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/redshift#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/redshift#code-examples").

```
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.redshift.RedshiftClient;
import software.amazon.awssdk.services.redshift.paginators.DescribeClustersIterable;

/**
 * Before running this Java V2 code example, set up your development
 * environment, including your credentials.
 *
 * For more information, see the following documentation topic:
 *
 * https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/get-started.html
 */
public class HelloRedshift {
    public static void main(String[] args) {
        Region region = Region.US_EAST_1;
        RedshiftClient redshiftClient = RedshiftClient.builder()
            .region(region)
            .build();

        listClustersPaginator(redshiftClient);
    }

    public static void listClustersPaginator(RedshiftClient redshiftClient) {
        DescribeClustersIterable clustersIterable = redshiftClient.describeClustersPaginator();
        clustersIterable.stream()
            .flatMap(r -> r.clusters().stream())
            .forEach(cluster -> System.out
                .println(" Cluster identifier: " + cluster.clusterIdentifier() + " status = " + cluster.clusterStatus()));
    }
}


```

- For API details, see
  [DescribeClusters](../../../goto/SdkForJavaV2/redshift-2012-12-01/DescribeClusters.md "../../../goto/SdkForJavaV2/redshift-2012-12-01/DescribeClusters.md")
  in _AWS SDK for Java 2.x API Reference_.

Python

**SDK for Python (Boto3)**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/redshift#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/redshift#code-examples").

```
import boto3


def hello_redshift(redshift_client):
    """
    Use the AWS SDK for Python (Boto3) to create an Amazon Redshift client and list
    the clusters in your account. This list might be empty if you haven't created
    any clusters.
    This example uses the default settings specified in your shared credentials
    and config files.

    :param redshift_client: A Boto3 Redshift Client object.
    """
    print("Hello, Redshift! Let's list your clusters:")
    paginator = redshift_client.get_paginator("describe_clusters")
    clusters = []
    for page in paginator.paginate():
        clusters.extend(page["Clusters"])

    print(f"{len(clusters)} cluster(s) were found.")

    for cluster in clusters:
        print(f"  {cluster['ClusterIdentifier']}")


if __name__ == "__main__":
    hello_redshift(boto3.client("redshift"))


```

- For API details, see
  [DescribeClusters](../../../goto/boto3/redshift-2012-12-01/DescribeClusters.md "../../../goto/boto3/redshift-2012-12-01/DescribeClusters.md")
  in _AWS SDK for Python (Boto3) API Reference_.

For a complete list of AWS SDK developer guides and code examples, see
[Using this service with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
