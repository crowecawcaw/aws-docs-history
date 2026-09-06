

# Manage Policies and Policy Engines
<a name="manage-policies-engines"></a>

Use these operations to manage your Policy Engines and policies.

**Topics**
+ [List Policy Engines](#list-policy-engines)
+ [Get Policy Engine](#get-policy-engine)
+ [List policies in a Policy Engine](#list-policies-in-engine)
+ [Get Policy](#get-policy)
+ [Update existing policies](#update-existing-policies)
+ [Delete policies](#delete-policies)
+ [Delete Policy Engine](#delete-policy-engine)

## List Policy Engines
<a name="list-policy-engines"></a>

View all Policy Engines in your account.

Select one of the following methods:

**Example**  

1. 

   ```
   aws bedrock-agentcore-control list-policy-engines
   ```

1. 

   ```
   import boto3
   
   client = boto3.client('bedrock-agentcore-control')
   
   response = client.list_policy_engines()
   for engine in response['policyEngines']:
       print(f"Policy Engine: {engine['name']} (ID: {engine['policyEngineId']})")
       print(f"Status: {engine['status']}")
       print(f"Created: {engine['createdAt']}")
       print(f"ARN: {engine['policyEngineArn']}")
   ```

## Get Policy Engine
<a name="get-policy-engine"></a>

Retrieve detailed information about a specific Policy Engine:

**Example**  

1. 

   ```
   aws bedrock-agentcore-control get-policy-engine --policy-engine-id my-policy-engine-id
   ```

1. 

   ```
   import boto3
   
   client = boto3.client('bedrock-agentcore-control')
   
   response = client.get_policy_engine(
       policyEngineId='my-policy-engine-id'
   )
   
   print(f"Policy Engine: {response['name']}")
   print(f"ID: {response['policyEngineId']}")
   print(f"ARN: {response['policyEngineArn']}")
   print(f"Status: {response['status']}")
   print(f"Created: {response['createdAt']}")
   print(f"Updated: {response['updatedAt']}")
   ```

## List policies in a Policy Engine
<a name="list-policies-in-engine"></a>

View all policies within a specific Policy Engine:

**Example**  

1. 

   ```
   aws bedrock-agentcore-control list-policies --policy-engine-id my-policy-engine-id
   ```

1. 

   ```
   import boto3
   
   client = boto3.client('bedrock-agentcore-control')
   
   response = client.list_policies(
       policyEngineId='my-policy-engine-id'
   )
   
   for policy in response['policies']:
       print(f"Policy: {policy['name']} (ID: {policy['policyId']})")
       print(f"Status: {policy['status']}")
       print(f"Description: {policy.get('description', 'No description')}")
       print(f"Created: {policy['createdAt']}")
   ```

## Get Policy
<a name="get-policy"></a>

Retrieve detailed information about a specific policy:

**Example**  

1. 

   ```
   aws bedrock-agentcore-control get-policy --policy-engine-id my-policy-engine-id --policy-id my-policy-id
   ```

1. 

   ```
   import boto3
   
   client = boto3.client('bedrock-agentcore-control')
   
   response = client.get_policy(
       policyId='my-policy-id',
       policyEngineId='my-policy-engine-id'
   )
   
   print(f"Policy: {response['name']}")
   print(f"ID: {response['policyId']}")
   print(f"ARN: {response['policyArn']}")
   print(f"Status: {response['status']}")
   print(f"Created: {response['createdAt']}")
   print(f"Updated: {response['updatedAt']}")
   print(f"Cedar Statement: {response['definition']['cedar']['statement']}")
   ```

## Update existing policies
<a name="update-existing-policies"></a>

Update a policy’s definition.

**Note**  
If the updated policy is a temporal policy, or the update adds or removes temporal expressions, updating it invalidates the engine’s active temporal policy sessions. In-flight sessions return an HTTP 409 `ConflictException` and must be restarted. For more information, see [Session invalidation](policy-temporal.md#policy-temporal-session-invalidation).

**Example**  

1. 

   ```
   aws bedrock-agentcore-control update-policy \
     --policy-id my-policy-id \
     --policy-engine-id my-policy-engine-id \
     --definition '{
       "cedar": {
         "statement": "permit(principal, action, resource);"
       }
     }'
   ```

1. 

   ```
   import boto3
   
   client = boto3.client('bedrock-agentcore-control')
   
   client.update_policy(
       policyId='my-policy-id',
       policyEngineId='my-policy-engine-id',
       definition={
           'cedar': {
               'statement': 'permit(principal, action, resource);'
           }
       }
   )
   
   waiter = client.get_waiter('policy_active')
   waiter.wait(PolicyEngineId="my-policy-engine-id", PolicyId="my-policy-id")
   ```

## Delete policies
<a name="delete-policies"></a>

Delete a policy from the Policy Engine.

**Example**  

1. 

   ```
   aws bedrock-agentcore-control delete-policy --policy-engine-id my-policy-engine-id --policy-id my-policy-id
   ```

1. 

   ```
   import boto3
   
   client = boto3.client('bedrock-agentcore-control')
   
   client.delete_policy(policyId='my-policy-id', policyEngineId='my-policy-engine-id')
   waiter = client.get_waiter('policy_deleted')
   waiter.wait(PolicyEngineId="my-policy-engine-id", PolicyId="my-policy-id")
   ```

## Delete Policy Engine
<a name="delete-policy-engine"></a>

Delete an entire Policy Engine and all its policies.

**Note**  
\* You cannot delete a Policy Engine that is currently attached to a gateway. First detach it by updating the gateway configuration. \* You cannot delete a Policy Engine that has policies in it. First delete all the policies and then delete the engine

**Example**  

1. 

   ```
   aws bedrock-agentcore-control delete-policy-engine --policy-engine-id my-policy-engine-id
   ```

1. 

   ```
   import boto3
   
   client = boto3.client('bedrock-agentcore-control')
   
   client.delete_policy_engine(policyEngineId='my-policy-engine-id')
   ```