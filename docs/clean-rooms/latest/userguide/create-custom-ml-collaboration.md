# Creating and joining the collaboration

in AWS Clean Rooms ML

The collaboration creator is responsible for creating the collaboration, inviting
members, and assigning their roles. The invited members join the collaboration and
specify results settings, trained model artifacts destination settings and accept
payment responsibilities, depending on how the collaboration is set up.

## Creating a collaboration for machine

learning

The following procedure shows how to create a collaboration for machine learning,
invite one or more members, and assign members that can start model training,
receive results, receive trained model results, including model artifacts and
metrics, and receive model inference results. The collaboration creator also assigns
a member who will pay for query compute, model training, and model inference costs.

Console

###### To create a collaboration for machine learning (console)

1. [Create a collaboration
   and invite one or more members to join the
   collaboration](create-collaboration.md "create-collaboration.md")
2. Assign the following **Member abilities** for
   **Analysis using queries and jobs**:
   - Assign **Run queries** to the member
     who will start model training.
   - Assign **Receive results from
     analysis** to the members who will receive
     query results.

3. Assign the following **Member abilities** for
   **ML modeling using purpose-built
   workflows**:
   - Assign **Receive output from trained
     models** to the member who will receive
     trained model results, including model artifacts and
     metrics.
   - Assign **Receive output from model
     inference** to the member who will receive
     the model inference results.

4. For **Configure payment**, specify the
   members who will pay for query compute, model training, and
   model inference costs. Each of these costs can be assigned to
   the same or different members. If an invited member is the
   member who is responsible to pay for payment costs, they must
   accept their payment responsibilities before joining the
   collaboration.
5. For **Configure membership**, the
   collaboration creator can decide to join the membership now or
   create a membership later. The collaboration creator must then
   set up the ML configuration.
   1. If the collaboration creator is also the results
      receiver, they must also specify the query results
      destination and format in the **Results settings
      defaults**.
   2. The ML configuration provides a role for Clean Rooms ML to
      publish metrics to an AWS account. If the
      collaboration creator is also receiving trained model
      artifacts, they can specify the Amazon S3 bucket used to
      receive results.
   3. In the **ML configurations** section,
      select **Create ML configuration** and
      then specify the **Model output destination on
      Amazon S3** and the **Service access
      role** needed to access this
      location.
   4. If the collaboration creator is the member who is
      responsible to pay for payment costs, they must accept
      their payment responsibilities before creating the
      collaboration.

API
To create a collaboration for machine learning (API)

1.  [Create a collaboration
    and invite one or more members to join the
    collaboration](create-collaboration.md "create-collaboration.md")
2.  Assign the following roles to collaboration members:

        * `CAN_QUERY` - assigned to the member who
         will start model training and inference.
        * `CAN_RECEIVE_MODEL_OUTPUT` - assigned to
         the members who will receive trained model
         results.
        * `CAN_RECEIVE_INFERENCE_OUTPUT` - assigned
         to the members who will receive model inference
         results.

    If the collaboration creator is also the results receiver,
    they must also specify the query results destination and format
    during collaboration creation. They also give a service role
    Amazon Resource Name (ARN) to write the results to the query
    results destination.

3.  Specify the members who will pay for query compute, model
    training, and model inference costs. Each of these costs can be
    assigned to the same or different members. If an invited member
    is the member who is responsible to pay for payment costs, they
    must accept their payment responsibilities before joining the
    collaboration.
4.  The following code creates a collaboration, invites a member
    that can run queries and receive results, and specifies the
    collaboration creator as the model artifacts receiver.

```
`import boto3
acr_client= boto3.client('cleanrooms')

collaboration = a_acr_client.create_collaboration(
 members=[
 {
 'accountId': '`invited_member_accountId`',
 'memberAbilities':["CAN_QUERY","CAN_RECEIVE_RESULTS"],
 'displayName': '`member_display_name`'
 }
 ],
 name='`collaboration_name`',
 description=`collaboration_description`,
 creatorMLMemberAbilities= {
 'customMLMemberAbilities':["CAN_RECEIVE_MODEL_OUTPUT", "CAN_RECEIVE_INFERENCE_OUTPUT"],
 },
 creatorDisplayName='`creator_display_name`',
 queryLogStatus="ENABLED",
 analyticsEngine="SPARK",
 creatorPaymentConfiguration={
 "queryCompute": {
 "isResponsible": True
 },
 "machineLearning": {
 "modelTraining": {
 "isResponsible": True
 },
 "modelInference": {
 "isResponsible": True
 }
 }
 }
)

collaboration_id = collaboration['collaboration']['id']
print("collaborationId: {collaboration_id}")

member_membership = a_acr_client.create_membership(
 collaborationIdentifier = collaboration_id,
 queryLogStatus = 'ENABLED',
 paymentConfiguration={
 "queryCompute": {
 "isResponsible": True
 },
 "machineLearning": {
 "modelTraining": {
 "isResponsible": True
 },
 "modelInference": {
 "isResponsible": True
 }
 }
 }
)`
```

5. The collaboration creator must then set up the ML
   configuration. The ML configuration provides a role for Clean Rooms ML
   to publish metrics and logs to an AWS account. If the
   collaboration creator is also receiving results (model artifacts
   or inference results), they can specify the Amazon S3 bucket used to
   receive results.

```
`import boto3
acr_ml_client= boto3.client('cleanroomsml')

acr_ml_client.put_ml_configuration(
 membershipIdentifier=`membership_id`,
 defaultOutputLocation={
 'roleArn':'arn:aws:iam::`account`:`role`/`roleName`',
 'destination':{
 's3Destination':{
 's3Uri':"s3://`bucketName/prefix`"
 }
 }
 }
 )`
```

## Joining a collaboration

After the collaboration creator has finished their tasks, the invited members must
complete theirs.

Console

###### To create a membership and join a collaboration (console)

1. The invited member [creates a
   membership and joins the collaboration](create-membership.md "create-membership.md").
2. If the invited member is the member who is responsible to pay,
   including query compute, model training, and model inference
   costs, they must accept their payment responsibilities before
   joining the collaboration.
3. The invited member sets up the ML configuration, which
   provides a role for Clean Rooms ML to publish model metrics to an
   AWS account. If they're also the member receiving trained
   model artifacts, they must give an Amazon S3 bucket where trained
   model artifacts are stored.

API
To create a membership and join a collaboration (API)

1. If the invited member is the member who can receive results,
   they specify the query results destination and format. They also
   provide a service role ARN that allows the service to write to
   the query results destination

If the invited member is the member who is responsible to pay,
including query compute, model training, and model inference
costs, they must accept their payment responsibilities before
joining the collaboration.

If the invited member is the member who is responsible to pay
for model training and model inference for custom modeling, they
must accept their payment responsibilities before joining the
collaboration.

The following code creates a membership with query logging
enabled.

```
`import boto3
acr_client= boto3.client('cleanrooms')

acr_client.create_membership(
 membershipIdentifier='`membership_id`',
 queryLogStatus='ENABLED'
)`
```

2. The invited member sets up the ML configuration, which
   provides a role for Clean Rooms ML to publish model metrics to an
   AWS account. If they're also the member receiving trained
   model artifacts, they must provide an Amazon S3 bucket where trained
   model artifacts are stored.

```
`import boto3
acr_ml_client= boto3.client('cleanroomsml')

acr_ml_client.put_ml_configuration(
 membershipIdentifier='`membership_id`',
 defaultOutputLocation={
 'roleArn':"arn:aws:iam::`account`:`role`/`role_name`",
 'destination':{
 's3Destination':{
 's3Uri':"s3://`bucket_name/prefix`"
 }
 }
 }
 )`
```
