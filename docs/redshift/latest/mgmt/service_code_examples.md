Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Code examples for Amazon Redshift using AWS SDKs

The following code examples show how to use Amazon Redshift with an AWS software development kit (SDK).

_Basics_ are code examples that show you how to perform the essential operations within a service.

_Actions_ are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

_Scenarios_ are code examples that show you how to accomplish specific tasks by calling multiple functions within a service or combined with other AWS services.

For a complete list of AWS SDK developer guides and code examples, see
[Using this service with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.

**Get started**

The following code examples show how to get started using Amazon Redshift.

.NET

**SDK for .NET (v4)**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/dotnetv4/Redshift#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/dotnetv4/Redshift#code-examples").

```
    /// <summary>
    /// Main method to run the Hello Amazon Redshift example.
    /// </summary>
    /// <param name="args">Command line arguments (not used).</param>
    public static async Task Main(string[] args)
    {
        var redshiftClient = new AmazonRedshiftClient();

        Console.WriteLine("Hello, Amazon Redshift! Let's list available clusters:");

        var clusters = new List<Cluster>();

        try
        {
            // Use pagination to retrieve all clusters.
            var clustersPaginator = redshiftClient.Paginators.DescribeClusters(new DescribeClustersRequest());

            await foreach (var response in clustersPaginator.Responses)
            {
                if (response.Clusters != null)
                    clusters.AddRange(response.Clusters);
            }

            Console.WriteLine($"{clusters.Count} cluster(s) retrieved.");

            foreach (var cluster in clusters)
            {
                Console.WriteLine($"\t{cluster.ClusterIdentifier} (Status: {cluster.ClusterStatus})");
            }
        }
        catch (AmazonRedshiftException ex)
        {
            Console.WriteLine($"Couldn't list clusters. Here's why: {ex.Message}");
        }
        catch (Exception ex)
        {
            Console.WriteLine($"An error occurred: {ex.Message}");
        }
    }


```

- For API details, see
  [DescribeClusters](../../../goto/DotNetSDKV4/redshift-2012-12-01/DescribeClusters.md "../../../goto/DotNetSDKV4/redshift-2012-12-01/DescribeClusters.md")
  in _AWS SDK for .NET API Reference_.

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

###### Code examples

- [Basics](service_code_examples_basics.md "service_code_examples_basics.md")
  - [Hello Amazon Redshift](example_redshift_Hello_section.md "example_redshift_Hello_section.md")
  - [Learn the basics](example_redshift_Scenario_section.md "example_redshift_Scenario_section.md")
  - [Actions](service_code_examples_actions.md "service_code_examples_actions.md")
    - [CreateCluster](example_redshift_CreateCluster_section.md "example_redshift_CreateCluster_section.md")
    - [DeleteCluster](example_redshift_DeleteCluster_section.md "example_redshift_DeleteCluster_section.md")
    - [DescribeClusters](example_redshift_DescribeClusters_section.md "example_redshift_DescribeClusters_section.md")
    - [DescribeStatement](example_redshift_DescribeStatement_section.md "example_redshift_DescribeStatement_section.md")
    - [ExecuteStatement](example_redshift_ExecuteStatement_section.md "example_redshift_ExecuteStatement_section.md")
    - [GetStatementResult](example_redshift_GetStatementResult_section.md "example_redshift_GetStatementResult_section.md")
    - [ListDatabases](example_redshift_ListDatabases_section.md "example_redshift_ListDatabases_section.md")
    - [ModifyCluster](example_redshift_ModifyCluster_section.md "example_redshift_ModifyCluster_section.md")

- [Scenarios](service_code_examples_scenarios.md "service_code_examples_scenarios.md")
  - [Create a web application to track Amazon Redshift data](example_cross_RedshiftDataTracker_section.md "example_cross_RedshiftDataTracker_section.md")
