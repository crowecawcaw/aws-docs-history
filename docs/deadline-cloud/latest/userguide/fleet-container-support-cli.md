

# Creating a Docker-enabled fleet with the AWS CLI
<a name="fleet-container-support-cli"></a>

The queue role requires permission to authenticate to Amazon ECR and pull the image selected by the Docker queue environment. The fleet role permission is optional for the default queue environment. Add it when host configuration actions or worker-side tools pull images outside a queue session.

## Prerequisites
<a name="fleet-container-cli-prerequisites"></a>

Before you begin, configure the AWS CLI with permission to create Deadline Cloud fleets and attach policies to the queue and fleet roles. You also need an existing farm, queue, queue role, fleet role, and container image in an Amazon ECR private repository.

## Create the fleet
<a name="fleet-container-cli-create"></a>

**To create a Docker-enabled fleet**

1. Set your farm, queue, and role values.

   ```
   FARM_ID={{farm-0123456789abcdef0123456789abcdef}}
   QUEUE_ID={{queue-0123456789abcdef0123456789abcdef}}
   FLEET_ROLE_ARN={{arn:aws:iam::123456789012:role/DeadlineFleetRole}}
   MAX_WORKERS={{10}}
   
   QUEUE_ROLE_ARN=$(aws deadline get-queue \
       --farm-id "$FARM_ID" \
       --queue-id "$QUEUE_ID" \
       --query roleArn \
       --output text)
   QUEUE_ROLE_NAME=${QUEUE_ROLE_ARN##*/}
   FLEET_ROLE_NAME=${FLEET_ROLE_ARN##*/}
   ECR_READ_ONLY_POLICY=arn:aws:iam::aws:policy/AmazonEC2ContainerRegistryReadOnly
   ```

1. Attach the Amazon ECR read-only policy to the queue role. The default Docker queue environment uses queue credentials to authenticate and pull the image.

   ```
   aws iam attach-role-policy \
       --role-name "$QUEUE_ROLE_NAME" \
       --policy-arn "$ECR_READ_ONLY_POLICY"
   ```

1. (Optional) Attach the same policy to the fleet role when host configuration actions or worker-side tools must pull images outside the queue session.

   ```
   aws iam attach-role-policy \
       --role-name "$FLEET_ROLE_NAME" \
       --policy-arn "$ECR_READ_ONLY_POLICY"
   ```

1. Create a file named `docker-fleet-configuration.json` with the following fleet configuration:

   ```
   {
     "serviceManagedEc2": {
       "instanceCapabilities": {
         "vCpuCount": {
           "min": 4,
           "max": 16
         },
         "memoryMiB": {
           "min": 8192,
           "max": 65536
         },
         "osFamily": "linux",
         "cpuArchitectureType": "x86_64",
         "softwareAddOns": [
           {
             "name": "docker"
           }
         ]
       },
       "instanceMarketOptions": {
         "type": "spot"
       }
     }
   }
   ```

1. Create the service-managed fleet and save its fleet ID.

   ```
   FLEET_ID=$(aws deadline create-fleet \
       --farm-id "$FARM_ID" \
       --display-name "Docker fleet" \
       --role-arn "$FLEET_ROLE_ARN" \
       --min-worker-count 0 \
       --max-worker-count "$MAX_WORKERS" \
       --configuration file://docker-fleet-configuration.json \
       --query fleetId \
       --output text)
   
   echo "$FLEET_ID"
   ```

1. Associate the queue with the fleet.

   ```
   aws deadline create-queue-fleet-association \
       --farm-id "$FARM_ID" \
       --queue-id "$QUEUE_ID" \
       --fleet-id "$FLEET_ID"
   ```

## Verify the fleet and role permissions
<a name="fleet-container-cli-verify"></a>

**To verify container support**

1. Verify that the fleet configuration includes the Docker software add-on.

   ```
   aws deadline get-fleet \
       --farm-id "$FARM_ID" \
       --fleet-id "$FLEET_ID" \
       --query 'configuration.serviceManagedEc2.instanceCapabilities.softwareAddOns'
   ```

   Confirm that the response contains `"name": "docker"`.

1. Verify that the queue role has the Amazon ECR read-only policy.

   ```
   aws iam list-attached-role-policies \
       --role-name "$QUEUE_ROLE_NAME" \
       --query 'AttachedPolicies[?PolicyName==`AmazonEC2ContainerRegistryReadOnly`]'
   ```

1. If you attached the policy to the fleet role, repeat the command with `--role-name "$FLEET_ROLE_NAME"`.

The fleet provides rootless Docker, but the queue still needs a Docker queue environment that identifies an image. For queue configuration details, see [Container support for service-managed fleets](fleet-container-support.md).