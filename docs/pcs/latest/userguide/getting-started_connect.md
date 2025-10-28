# Connect to your AWS PCS cluster

After the status of the `login` compute node group becomes
**Active**, you can connect to the EC2 instance it created.

###### To connect to the login node

- Open the [AWS PCS console](https://console.aws.amazon.com/pcs "https://console.aws.amazon.com/pcs") and navigate to **Clusters**.
- Select the cluster named `get-started`.
- Choose **Compute node groups**.
- Navigate to the compute node group named `login`.
- Find the **Compute node group ID**.
- In another browser window or tab, open the [Amazon EC2 console](https://console.aws.amazon.com/ec2 "https://console.aws.amazon.com/ec2").
  - Choose **Instances**.
  - Search for EC2 instances with the following tag. Replace `node-group-id` with the value of
    the **Compute node group ID** from the previous step. There should be 1 instance.

  ```
  aws:pcs:compute-node-group-id=`node-group-id`
  ```

  - Connect to the EC2 instance. You can use Session Manager or SSH.

  Session Manager

      - Select the instance.
      - Choose **Connect**.
      - Under **Connect to instance**, select **Session Manager**.
      - Choose **Connect**.
      - Choose **Connect**. An interactive terminal launches in your browser.

  SSH

      - Select the instance.
      - Choose **Connect**.
      - Under **Connect to instance**, select **SSH client**.
      - Follow the instructions provided by the console.


      ###### Note

      The user name for the
       instance is **`ec2-user`** not `root`.
