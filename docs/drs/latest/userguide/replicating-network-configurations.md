# Replicating your network configurations

in Elastic Disaster Recovery

Once you install your agent and created the required role, go to the **Source networks** page and take the following steps:

1. Select the network you want to replicate from the list.
2. Click **Actions** and select **Start
   replication** from the drop-down menu.
3. Click **Select S3 bucket**. This will allow to save the
   CloudFormation stack in your account’s S3 bucket. You must specify the S3 bucket before
   you initiate network recovery. It is recommended that you employ S3 bucket security and
   access management policies.

You can choose between selecting an existing S3 bucket and creating a new bucket using
the S3 bucket console.

###### Note

You must enable S3 versioning. 4. To test or recover your network configurations, click **Initiate
recovery job** and the **Initiate recovery job**
prompt will appear.

If this is the first time you are replicating network configurations, you will need to
create a new stack.

If you already created a stack, you can choose between 3 options:

    1. **Update a recommended stack** – The recommended
     stack is always the last stack you used.


    ###### Note

    If the update is not successful, simply create a new stack.
    2. **Create new stack**
    3. **Use a previously created stack** – if you want to
     choose a stack that you have previously used, select your preferred stack from the
     drop-down. This will only update the launch templates. The selected stack will then
     become the recommended stack, allowing you to update it.

Once the recovery job is marked as **Successful**, the
network (VPC) is launched in the target Region. All the EC2 launch templates of the source
servers in the relevant network will be automatically updated and will feature the new
values. This means that when you perform a recovery, those source servers will be launched
as part of the new network and the correct subnet.
