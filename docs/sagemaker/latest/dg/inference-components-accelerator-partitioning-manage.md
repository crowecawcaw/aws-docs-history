

# Manage GPU partitioned endpoints
<a name="inference-components-accelerator-partitioning-manage"></a>

After you deploy models to a partitioned endpoint, you can scale them, move them to a different partition type, or delete the endpoint. The examples in this topic use the resources from [Create an endpoint with GPU partitions](inference-components-accelerator-partitioning-create.md) and [Deploy models to GPU partitions with inference components](inference-components-accelerator-partitioning-deploy.md).

## Update partitioned resources
<a name="accelerator-partitioning-update"></a>

To serve more requests with a model, increase `CopyCount` on its inference component. SageMaker AI places each copy on a free partition of the same type. The following `update-inference-component` command scales `demo-ic-4g` to 2 copies:

```
aws sagemaker update-inference-component \
  --region us-west-2 \
  --inference-component-name demo-ic-4g \
  --runtime-config '{"CopyCount": 2}'
```

An endpoint has as many partitions of a type as the layout declares, multiplied by the number of accelerators and instances. To adjust the number of copies automatically, see [Automatic scaling of Amazon SageMaker AI models](endpoint-auto-scaling.md).

**Note**  
You can't change the partition type of an existing inference component. `UpdateInferenceComponent` rejects a change to `AcceleratorPartitionType`. To run a model on a different partition type, create a new inference component with the new type, wait until it's `InService`, move your clients to the new name, and then delete the old inference component. The new type must be one that the endpoint layout declares.

**Note**  
You can't change the partition layout of a running endpoint. An `UpdateEndpoint` request to an endpoint configuration with a different layout, including the same types in a different order, returns a 400 error. To use a different layout, create a new endpoint configuration and endpoint with the new layout, create the inference components on it, move your traffic, and then delete the old endpoint.

## Delete a partitioned endpoint
<a name="accelerator-partitioning-delete"></a>

A partitioned endpoint incurs charges for its instances until you delete it. Delete the inference components first, and then the endpoint and the endpoint configuration. You can't delete an endpoint while its status is `Creating`. Wait until the status changes, and then delete it.

**To delete a partitioned endpoint (AWS CLI)**

1. Delete the inference components. The following `delete-inference-component` command deletes `demo-ic-4g`. Repeat it for each inference component on the endpoint.

   ```
   aws sagemaker delete-inference-component --region us-west-2 --inference-component-name demo-ic-4g
   ```

1. Delete the endpoint, and wait until it's deleted. The following commands delete the endpoint `partition-demo` and wait for the deletion:

   ```
   aws sagemaker delete-endpoint --region us-west-2 --endpoint-name partition-demo
   aws sagemaker wait endpoint-deleted --region us-west-2 --endpoint-name partition-demo
   ```

1. Delete the endpoint configuration. The following `delete-endpoint-config` command deletes `partition-demo-config`:

   ```
   aws sagemaker delete-endpoint-config --region us-west-2 --endpoint-config-name partition-demo-config
   ```

After you delete a partitioned endpoint, its accelerators can take several minutes to become available again.