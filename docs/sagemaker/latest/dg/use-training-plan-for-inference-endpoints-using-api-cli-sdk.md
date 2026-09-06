

# Deploy an inference endpoint using the API, AWS CLI
<a name="use-training-plan-for-inference-endpoints-using-api-cli-sdk"></a>

To use SageMaker training plans on a SageMaker inference endpoint, specify the `MlReservationArn` parameter with the desired training plan resource ARN in the `CapacityReservationConfig` when calling the [`CreateEndpointConfig`](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateEndpointConfig.html) API operation. You can use exactly one plan per inference endpoint.

**Important**  
The `InstanceType` field set in the `ProductionVariants` section of the `CreateEndpointConfig` request must match the `InstanceType` of your training plan.

## Create an endpoint configuration with training plan reservation
<a name="inference-endpoint-create-config"></a>

Create an endpoint configuration that binds your inference endpoint to the reserved capacity. Include the `CapacityReservationConfig` object in the `ProductionVariants` section, setting the `MlReservationArn` to your training plan ARN.

```
aws sagemaker create-endpoint-config \
  --endpoint-config-name "{{ftp-ep-config}}" \
  --production-variants '[{
          "VariantName": "AllTraffic",
          "ModelName": "{{my-model}}",
          "InitialInstanceCount": {{1}},
          "InstanceType": "{{ml.p4d.24xlarge}}",
          "InitialVariantWeight": 1.0,
          "CapacityReservationConfig": {
              "CapacityReservationPreference": "capacity-reservations-only",
              "MlReservationArn": "{{arn:aws:sagemaker:us-east-1:123456789123:training-plan/p4-for-inference-endpoint}}"
          }
      }]'
```

The `CapacityReservationPreference` setting of `capacity-reservations-only` ensures the endpoint only runs on the reserved capacity and stops serving traffic when the reservation ends.

## Deploy the endpoint on reserved capacity
<a name="inference-endpoint-deploy"></a>

With the endpoint configuration ready, deploy the endpoint.

```
aws sagemaker create-endpoint \
  --endpoint-name "{{my-endpoint}}" \
  --endpoint-config-name "{{ftp-ep-config}}"
```

The endpoint now runs entirely within the reserved training plan capacity. After the endpoint reaches `InService` status, you can invoke it for inference.

## Invoke the endpoint
<a name="inference-endpoint-invoke"></a>

During the active reservation window, the endpoint operates normally with predictable access to capacity.

```
aws sagemaker-runtime invoke-endpoint \
  --endpoint-name "{{my-endpoint}}" \
  --body fileb://input.json \
  --content-type "application/json" \
  output.json
```

## Update the endpoint
<a name="inference-endpoint-update"></a>

SageMaker AI supports several update scenarios while maintaining the connection to reserved capacity.

**Update to a new model version**  
You can update to a new model version while keeping the same reserved capacity.

```
aws sagemaker create-endpoint-config \
  --endpoint-config-name "{{ftp-ep-config-v2}}" \
  --production-variants '[{
          "VariantName": "AllTraffic",
          "ModelName": "{{my-model-v2}}",
          "InitialInstanceCount": {{1}},
          "InstanceType": "{{ml.p4d.24xlarge}}",
          "InitialVariantWeight": 1.0,
          "CapacityReservationConfig": {
              "CapacityReservationPreference": "capacity-reservations-only",
              "MlReservationArn": "{{arn:aws:sagemaker:us-east-1:123456789123:training-plan/p4-for-inference-endpoint}}"
          }
      }]'

aws sagemaker update-endpoint \
  --endpoint-name "{{my-endpoint}}" \
  --endpoint-config-name "{{ftp-ep-config-v2}}"
```

**Migrate from training plan to on-demand capacity**  
To transition the endpoint beyond the reservation period, you can migrate to on-demand capacity.

```
aws sagemaker create-endpoint-config \
  --endpoint-config-name "{{ondemand-ep-config}}" \
  --production-variants '[{
          "VariantName": "AllTraffic",
          "ModelName": "{{my-model}}",
          "InitialInstanceCount": {{1}},
          "InstanceType": "{{ml.p4d.24xlarge}}",
          "InitialVariantWeight": 1.0
    }]'

aws sagemaker update-endpoint \
  --endpoint-name "{{my-endpoint}}" \
  --endpoint-config-name "{{ondemand-ep-config}}"
```

## Scale the endpoint
<a name="inference-endpoint-scale"></a>

If you reserved more capacity than initially deployed, you can scale up within the reservation limits.

```
aws sagemaker update-endpoint-weights-and-capacities \
  --endpoint-name "{{my-endpoint}}" \
  --desired-weights-and-capacities '[{
          "VariantName": "AllTraffic",
          "DesiredInstanceCount": 2
      }]'
```

**Important**  
If you attempt to scale beyond the reserved capacity, the request fails with a `ValidationException` indicating that the requested instance count exceeds the reserved capacity.

## Delete the endpoint
<a name="inference-endpoint-delete"></a>

When you no longer need the inference endpoint, delete it along with the endpoint configuration.

```
aws sagemaker delete-endpoint \
  --endpoint-name "{{my-endpoint}}"

aws sagemaker delete-endpoint-config \
  --endpoint-config-name "{{ftp-ep-config}}"
```

**Note**  
Deleting the endpoint does not cancel the training plan reservation.
The reserved capacity remains allocated until the training plan reservation window expires.
You can create a new endpoint using the same training plan reservation ARN if capacity is available and the reservation is active.
You are charged for the full reservation period regardless of when you delete the endpoint.