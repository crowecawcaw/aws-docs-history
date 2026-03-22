# Using the AWS SDK to configure auto scaling on Amazon DynamoDB tables

In addition to using the AWS Management Console and the AWS Command Line Interface (AWS CLI), you can write applications
that interact with Amazon DynamoDB auto scaling. This section contains two Java programs that you
can use to test this functionality:

- `EnableDynamoDBAutoscaling.java`
- `DisableDynamoDBAutoscaling.java`

## Enabling Application Auto Scaling for a table

The following program shows an example of setting up an auto scaling policy for a
DynamoDB table (`TestTable`). It proceeds as follows:

- The program registers write capacity units as a scalable target for
  `TestTable`. The range for this metric is between 5 and 10 write
  capacity units.
- After the scalable target is created, the program builds a target tracking
  configuration. The policy seeks to maintain a 50 percent target ratio between
  consumed write capacity and provisioned write capacity.
- The program then creates the scaling policy, based on the target tracking
  configuration.

###### Note

When you manually remove a table or global table replica, you do not automatically remove any
associated scalable targets, scaling policies, or CloudWatch alarms.

Java v2

```
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.applicationautoscaling.ApplicationAutoScalingClient;
import software.amazon.awssdk.services.applicationautoscaling.model.ApplicationAutoScalingException;
import software.amazon.awssdk.services.applicationautoscaling.model.DescribeScalableTargetsRequest;
import software.amazon.awssdk.services.applicationautoscaling.model.DescribeScalableTargetsResponse;
import software.amazon.awssdk.services.applicationautoscaling.model.DescribeScalingPoliciesRequest;
import software.amazon.awssdk.services.applicationautoscaling.model.DescribeScalingPoliciesResponse;
import software.amazon.awssdk.services.applicationautoscaling.model.PolicyType;
import software.amazon.awssdk.services.applicationautoscaling.model.PredefinedMetricSpecification;
import software.amazon.awssdk.services.applicationautoscaling.model.PutScalingPolicyRequest;
import software.amazon.awssdk.services.applicationautoscaling.model.RegisterScalableTargetRequest;
import software.amazon.awssdk.services.applicationautoscaling.model.ScalingPolicy;
import software.amazon.awssdk.services.applicationautoscaling.model.ServiceNamespace;
import software.amazon.awssdk.services.applicationautoscaling.model.ScalableDimension;
import software.amazon.awssdk.services.applicationautoscaling.model.MetricType;
import software.amazon.awssdk.services.applicationautoscaling.model.TargetTrackingScalingPolicyConfiguration;
import java.util.List;

/**
 * Before running this Java V2 code example, set up your development environment, including your credentials.
 *
 * For more information, see the following documentation topic:
 *
 * https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/get-started.html
 */
public class EnableDynamoDBAutoscaling {
    public static void main(String[] args) {
        final String usage = """

            Usage:
               <tableId> <roleARN> <policyName>\s

            Where:
               tableId - The table Id value (for example, table/Music).
               roleARN - The ARN of the role that has ApplicationAutoScaling permissions.
               policyName - The name of the policy to create.

            """;

        if (args.length != 3) {
            System.out.println(usage);
            System.exit(1);
        }

        System.out.println("This example registers an Amazon DynamoDB table, which is the resource to scale.");
        String tableId = args[0];
        String roleARN = args[1];
        String policyName = args[2];
        ServiceNamespace ns = ServiceNamespace.DYNAMODB;
        ScalableDimension tableWCUs = ScalableDimension.DYNAMODB_TABLE_WRITE_CAPACITY_UNITS;
        ApplicationAutoScalingClient appAutoScalingClient = ApplicationAutoScalingClient.builder()
            .region(Region.US_EAST_1)
            .build();

        registerScalableTarget(appAutoScalingClient, tableId, roleARN, ns, tableWCUs);
        verifyTarget(appAutoScalingClient, tableId, ns, tableWCUs);
        configureScalingPolicy(appAutoScalingClient, tableId, ns, tableWCUs, policyName);
    }

    public static void registerScalableTarget(ApplicationAutoScalingClient appAutoScalingClient, String tableId, String roleARN, ServiceNamespace ns, ScalableDimension tableWCUs) {
        try {
            RegisterScalableTargetRequest targetRequest = RegisterScalableTargetRequest.builder()
                .serviceNamespace(ns)
                .scalableDimension(tableWCUs)
                .resourceId(tableId)
                .roleARN(roleARN)
                .minCapacity(5)
                .maxCapacity(10)
                .build();

            appAutoScalingClient.registerScalableTarget(targetRequest);
            System.out.println("You have registered " + tableId);

        } catch (ApplicationAutoScalingException e) {
            System.err.println(e.awsErrorDetails().errorMessage());
        }
    }

    // Verify that the target was created.
    public static void verifyTarget(ApplicationAutoScalingClient appAutoScalingClient, String tableId, ServiceNamespace ns, ScalableDimension tableWCUs) {
        DescribeScalableTargetsRequest dscRequest = DescribeScalableTargetsRequest.builder()
            .scalableDimension(tableWCUs)
            .serviceNamespace(ns)
            .resourceIds(tableId)
            .build();

        DescribeScalableTargetsResponse response = appAutoScalingClient.describeScalableTargets(dscRequest);
        System.out.println("DescribeScalableTargets result: ");
        System.out.println(response);
    }

    // Configure a scaling policy.
    public static void configureScalingPolicy(ApplicationAutoScalingClient appAutoScalingClient, String tableId, ServiceNamespace ns, ScalableDimension tableWCUs, String policyName) {
        // Check if the policy exists before creating a new one.
        DescribeScalingPoliciesResponse describeScalingPoliciesResponse = appAutoScalingClient.describeScalingPolicies(DescribeScalingPoliciesRequest.builder()
            .serviceNamespace(ns)
            .resourceId(tableId)
            .scalableDimension(tableWCUs)
            .build());

        if (!describeScalingPoliciesResponse.scalingPolicies().isEmpty()) {
            // If policies exist, consider updating an existing policy instead of creating a new one.
            System.out.println("Policy already exists. Consider updating it instead.");
            List<ScalingPolicy> polList = describeScalingPoliciesResponse.scalingPolicies();
            for (ScalingPolicy pol : polList) {
                System.out.println("Policy name:" +pol.policyName());
            }
        } else {
            // If no policies exist, proceed with creating a new policy.
            PredefinedMetricSpecification specification = PredefinedMetricSpecification.builder()
                .predefinedMetricType(MetricType.DYNAMO_DB_WRITE_CAPACITY_UTILIZATION)
                .build();

            TargetTrackingScalingPolicyConfiguration policyConfiguration = TargetTrackingScalingPolicyConfiguration.builder()
                .predefinedMetricSpecification(specification)
                .targetValue(50.0)
                .scaleInCooldown(60)
                .scaleOutCooldown(60)
                .build();

            PutScalingPolicyRequest putScalingPolicyRequest = PutScalingPolicyRequest.builder()
                .targetTrackingScalingPolicyConfiguration(policyConfiguration)
                .serviceNamespace(ns)
                .scalableDimension(tableWCUs)
                .resourceId(tableId)
                .policyName(policyName)
                .policyType(PolicyType.TARGET_TRACKING_SCALING)
                .build();

            try {
                appAutoScalingClient.putScalingPolicy(putScalingPolicyRequest);
                System.out.println("You have successfully created a scaling policy for an Application Auto Scaling scalable target");
            } catch (ApplicationAutoScalingException e) {
                System.err.println("Error: " + e.awsErrorDetails().errorMessage());
            }
        }
    }
}

```

Java v1
The program requires that you provide an Amazon Resource Name (ARN) for a valid Application Auto Scaling service linked role. (For example: `arn:aws:iam::122517410325:role/AWSServiceRoleForApplicationAutoScaling_DynamoDBTable`.) In the following program, replace `SERVICE_ROLE_ARN_GOES_HERE` with the actual ARN.

```
package com.amazonaws.codesamples.autoscaling;

import com.amazonaws.services.applicationautoscaling.AWSApplicationAutoScalingClient;
import com.amazonaws.services.applicationautoscaling.AWSApplicationAutoScalingClientBuilder;
import com.amazonaws.services.applicationautoscaling.model.DescribeScalableTargetsRequest;
import com.amazonaws.services.applicationautoscaling.model.DescribeScalableTargetsResult;
import com.amazonaws.services.applicationautoscaling.model.DescribeScalingPoliciesRequest;
import com.amazonaws.services.applicationautoscaling.model.DescribeScalingPoliciesResult;
import com.amazonaws.services.applicationautoscaling.model.MetricType;
import com.amazonaws.services.applicationautoscaling.model.PolicyType;
import com.amazonaws.services.applicationautoscaling.model.PredefinedMetricSpecification;
import com.amazonaws.services.applicationautoscaling.model.PutScalingPolicyRequest;
import com.amazonaws.services.applicationautoscaling.model.RegisterScalableTargetRequest;
import com.amazonaws.services.applicationautoscaling.model.ScalableDimension;
import com.amazonaws.services.applicationautoscaling.model.ServiceNamespace;
import com.amazonaws.services.applicationautoscaling.model.TargetTrackingScalingPolicyConfiguration;

public class EnableDynamoDBAutoscaling {

	static AWSApplicationAutoScalingClient aaClient = (AWSApplicationAutoScalingClient) AWSApplicationAutoScalingClientBuilder
			.standard().build();

	public static void main(String args[]) {

		ServiceNamespace ns = ServiceNamespace.Dynamodb;
		ScalableDimension tableWCUs = ScalableDimension.DynamodbTableWriteCapacityUnits;
		String resourceID = "table/TestTable";

		// Define the scalable target
		RegisterScalableTargetRequest rstRequest = new RegisterScalableTargetRequest()
				.withServiceNamespace(ns)
				.withResourceId(resourceID)
				.withScalableDimension(tableWCUs)
				.withMinCapacity(5)
				.withMaxCapacity(10)
				.withRoleARN("SERVICE_ROLE_ARN_GOES_HERE");

		try {
			aaClient.registerScalableTarget(rstRequest);
		} catch (Exception e) {
			System.err.println("Unable to register scalable target: ");
			System.err.println(e.getMessage());
		}

		// Verify that the target was created
		DescribeScalableTargetsRequest dscRequest = new DescribeScalableTargetsRequest()
				.withServiceNamespace(ns)
				.withScalableDimension(tableWCUs)
				.withResourceIds(resourceID);
		try {
			DescribeScalableTargetsResult dsaResult = aaClient.describeScalableTargets(dscRequest);
			System.out.println("DescribeScalableTargets result: ");
			System.out.println(dsaResult);
			System.out.println();
		} catch (Exception e) {
			System.err.println("Unable to describe scalable target: ");
			System.err.println(e.getMessage());
		}

		System.out.println();

		// Configure a scaling policy
		TargetTrackingScalingPolicyConfiguration targetTrackingScalingPolicyConfiguration = new TargetTrackingScalingPolicyConfiguration()
				.withPredefinedMetricSpecification(
						new PredefinedMetricSpecification()
								.withPredefinedMetricType(MetricType.DynamoDBWriteCapacityUtilization))
				.withTargetValue(50.0)
				.withScaleInCooldown(60)
				.withScaleOutCooldown(60);

		// Create the scaling policy, based on your configuration
		PutScalingPolicyRequest pspRequest = new PutScalingPolicyRequest()
				.withServiceNamespace(ns)
				.withScalableDimension(tableWCUs)
				.withResourceId(resourceID)
				.withPolicyName("MyScalingPolicy")
				.withPolicyType(PolicyType.TargetTrackingScaling)
				.withTargetTrackingScalingPolicyConfiguration(targetTrackingScalingPolicyConfiguration);

		try {
			aaClient.putScalingPolicy(pspRequest);
		} catch (Exception e) {
			System.err.println("Unable to put scaling policy: ");
			System.err.println(e.getMessage());
		}

		// Verify that the scaling policy was created
		DescribeScalingPoliciesRequest dspRequest = new DescribeScalingPoliciesRequest()
				.withServiceNamespace(ns)
				.withScalableDimension(tableWCUs)
				.withResourceId(resourceID);

		try {
			DescribeScalingPoliciesResult dspResult = aaClient.describeScalingPolicies(dspRequest);
			System.out.println("DescribeScalingPolicies result: ");
			System.out.println(dspResult);
		} catch (Exception e) {
			e.printStackTrace();
			System.err.println("Unable to describe scaling policy: ");
			System.err.println(e.getMessage());
		}

	}

}


```

## Disabling Application Auto Scaling for a table

The following program reverses the previous process. It removes the auto scaling
policy and then deregisters the scalable target.

Java v2

```
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.applicationautoscaling.ApplicationAutoScalingClient;
import software.amazon.awssdk.services.applicationautoscaling.model.ApplicationAutoScalingException;
import software.amazon.awssdk.services.applicationautoscaling.model.DeleteScalingPolicyRequest;
import software.amazon.awssdk.services.applicationautoscaling.model.DeregisterScalableTargetRequest;
import software.amazon.awssdk.services.applicationautoscaling.model.DescribeScalableTargetsRequest;
import software.amazon.awssdk.services.applicationautoscaling.model.DescribeScalableTargetsResponse;
import software.amazon.awssdk.services.applicationautoscaling.model.DescribeScalingPoliciesRequest;
import software.amazon.awssdk.services.applicationautoscaling.model.DescribeScalingPoliciesResponse;
import software.amazon.awssdk.services.applicationautoscaling.model.ScalableDimension;
import software.amazon.awssdk.services.applicationautoscaling.model.ServiceNamespace;

/**
 * Before running this Java V2 code example, set up your development environment, including your credentials.
 *
 * For more information, see the following documentation topic:
 *
 * https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/get-started.html
 */

public class DisableDynamoDBAutoscaling {
    public static void main(String[] args) {
        final String usage = """

            Usage:
               <tableId> <policyName>\s

            Where:
               tableId - The table Id value (for example, table/Music).\s
               policyName - The name of the policy (for example, $Music5-scaling-policy).

            """;
        if (args.length != 2) {
            System.out.println(usage);
            System.exit(1);
        }

        ApplicationAutoScalingClient appAutoScalingClient = ApplicationAutoScalingClient.builder()
            .region(Region.US_EAST_1)
            .build();

        ServiceNamespace ns = ServiceNamespace.DYNAMODB;
        ScalableDimension tableWCUs = ScalableDimension.DYNAMODB_TABLE_WRITE_CAPACITY_UNITS;
        String tableId = args[0];
        String policyName = args[1];

        deletePolicy(appAutoScalingClient, policyName, tableWCUs, ns, tableId);
        verifyScalingPolicies(appAutoScalingClient, tableId, ns, tableWCUs);
        deregisterScalableTarget(appAutoScalingClient, tableId, ns, tableWCUs);
        verifyTarget(appAutoScalingClient, tableId, ns, tableWCUs);
    }

    public static void deletePolicy(ApplicationAutoScalingClient appAutoScalingClient, String policyName, ScalableDimension tableWCUs, ServiceNamespace ns, String tableId) {
        try {
            DeleteScalingPolicyRequest delSPRequest = DeleteScalingPolicyRequest.builder()
                .policyName(policyName)
                .scalableDimension(tableWCUs)
                .serviceNamespace(ns)
                .resourceId(tableId)
                .build();

            appAutoScalingClient.deleteScalingPolicy(delSPRequest);
            System.out.println(policyName +" was deleted successfully.");

        } catch (ApplicationAutoScalingException e) {
            System.err.println(e.awsErrorDetails().errorMessage());
        }
    }

    // Verify that the scaling policy was deleted
    public static void verifyScalingPolicies(ApplicationAutoScalingClient appAutoScalingClient, String tableId, ServiceNamespace ns, ScalableDimension tableWCUs) {
        DescribeScalingPoliciesRequest dscRequest = DescribeScalingPoliciesRequest.builder()
            .scalableDimension(tableWCUs)
            .serviceNamespace(ns)
            .resourceId(tableId)
            .build();

        DescribeScalingPoliciesResponse response = appAutoScalingClient.describeScalingPolicies(dscRequest);
        System.out.println("DescribeScalableTargets result: ");
        System.out.println(response);
    }

    public static void deregisterScalableTarget(ApplicationAutoScalingClient appAutoScalingClient, String tableId, ServiceNamespace ns, ScalableDimension tableWCUs) {
        try {
            DeregisterScalableTargetRequest targetRequest = DeregisterScalableTargetRequest.builder()
                .scalableDimension(tableWCUs)
                .serviceNamespace(ns)
                .resourceId(tableId)
                .build();

            appAutoScalingClient.deregisterScalableTarget(targetRequest);
            System.out.println("The scalable target was deregistered.");

        } catch (ApplicationAutoScalingException e) {
            System.err.println(e.awsErrorDetails().errorMessage());
        }
    }

    public static void verifyTarget(ApplicationAutoScalingClient appAutoScalingClient, String tableId, ServiceNamespace ns, ScalableDimension tableWCUs) {
        DescribeScalableTargetsRequest dscRequest = DescribeScalableTargetsRequest.builder()
            .scalableDimension(tableWCUs)
            .serviceNamespace(ns)
            .resourceIds(tableId)
            .build();

        DescribeScalableTargetsResponse response = appAutoScalingClient.describeScalableTargets(dscRequest);
        System.out.println("DescribeScalableTargets result: ");
        System.out.println(response);
    }
}

```

Java v1

```
package com.amazonaws.codesamples.autoscaling;

import com.amazonaws.services.applicationautoscaling.AWSApplicationAutoScalingClient;
import com.amazonaws.services.applicationautoscaling.model.DeleteScalingPolicyRequest;
import com.amazonaws.services.applicationautoscaling.model.DeregisterScalableTargetRequest;
import com.amazonaws.services.applicationautoscaling.model.DescribeScalableTargetsRequest;
import com.amazonaws.services.applicationautoscaling.model.DescribeScalableTargetsResult;
import com.amazonaws.services.applicationautoscaling.model.DescribeScalingPoliciesRequest;
import com.amazonaws.services.applicationautoscaling.model.DescribeScalingPoliciesResult;
import com.amazonaws.services.applicationautoscaling.model.ScalableDimension;
import com.amazonaws.services.applicationautoscaling.model.ServiceNamespace;

public class DisableDynamoDBAutoscaling {

	static AWSApplicationAutoScalingClient aaClient = new AWSApplicationAutoScalingClient();

	public static void main(String args[]) {

		ServiceNamespace ns = ServiceNamespace.Dynamodb;
		ScalableDimension tableWCUs = ScalableDimension.DynamodbTableWriteCapacityUnits;
		String resourceID = "table/TestTable";

		// Delete the scaling policy
		DeleteScalingPolicyRequest delSPRequest = new DeleteScalingPolicyRequest()
				.withServiceNamespace(ns)
				.withScalableDimension(tableWCUs)
				.withResourceId(resourceID)
				.withPolicyName("MyScalingPolicy");

		try {
			aaClient.deleteScalingPolicy(delSPRequest);
		} catch (Exception e) {
			System.err.println("Unable to delete scaling policy: ");
			System.err.println(e.getMessage());
		}

		// Verify that the scaling policy was deleted
		DescribeScalingPoliciesRequest descSPRequest = new DescribeScalingPoliciesRequest()
				.withServiceNamespace(ns)
				.withScalableDimension(tableWCUs)
				.withResourceId(resourceID);

		try {
			DescribeScalingPoliciesResult dspResult = aaClient.describeScalingPolicies(descSPRequest);
			System.out.println("DescribeScalingPolicies result: ");
			System.out.println(dspResult);
		} catch (Exception e) {
			e.printStackTrace();
			System.err.println("Unable to describe scaling policy: ");
			System.err.println(e.getMessage());
		}

		System.out.println();

		// Remove the scalable target
		DeregisterScalableTargetRequest delSTRequest = new DeregisterScalableTargetRequest()
				.withServiceNamespace(ns)
				.withScalableDimension(tableWCUs)
				.withResourceId(resourceID);

		try {
			aaClient.deregisterScalableTarget(delSTRequest);
		} catch (Exception e) {
			System.err.println("Unable to deregister scalable target: ");
			System.err.println(e.getMessage());
		}

		// Verify that the scalable target was removed
		DescribeScalableTargetsRequest dscRequest = new DescribeScalableTargetsRequest()
				.withServiceNamespace(ns)
				.withScalableDimension(tableWCUs)
				.withResourceIds(resourceID);

		try {
			DescribeScalableTargetsResult dsaResult = aaClient.describeScalableTargets(dscRequest);
			System.out.println("DescribeScalableTargets result: ");
			System.out.println(dsaResult);
			System.out.println();
		} catch (Exception e) {
			System.err.println("Unable to describe scalable target: ");
			System.err.println(e.getMessage());
		}

	}

}


```
