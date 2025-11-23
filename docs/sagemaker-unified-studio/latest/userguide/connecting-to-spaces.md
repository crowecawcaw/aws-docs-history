# Connecting to Amazon SageMaker Unified Studio Spaces

Amazon SageMaker Unified Studio's remote connectivity establishes a secure tunnel between your local VS Code
and SageMaker Spaces, enabling interactive development and code execution using cloud
compute resources while maintaining your familiar local environment.

###### Note

Ensure network configuration is setup to allow the SSH traffic. For domains set up
in virtual private cloud (VPC)-only mode (default), your domain should have a route
out to the internet through a proxy or a NAT gateway. For more details, see [Integrated Gateways](../../../vpc/latest/userguide/VPC_Internet_Gateway.md "../../../vpc/latest/userguide/VPC_Internet_Gateway.md"). If your domain is completely isolated from the
internet, refer to connecting to a Space from the AWS Toolkit in this page for
setting up the remote connection.

You must enable remote access for the Space to connect to the Space.

- For an existing Space, if the Space is in Stopped state, hover over the Space
  and choose the connect button. This should enable remote access, start the Space
  and connect to it.
- For an existing Space, if the Space is in Running state, the Space must be
  restarted with remote access enabled. You can do this by clicking Connect and
  following the prompts to restart with remote access enabled.
- To enable remote access, while [creating a Space](create-space.md "create-space.md") in the portal, under Remote Access, toggle the
  switch to Enabled.
  To connect to a Space in Amazon SageMaker Unified Studio from the AWS Toolkit:

1. Under **Project**, choose **Compute** and then choose **Spaces**.
2. In the row of the Space you want to connect to, choose the icon that says
   **Connect to SageMaker Space** when you hover
   over it.
   - If your `instanceType` is less than 8 GB, a prompt appears
     asking you to start your Space with a larger `instanceType`.
     Choose yes to connect to your SageMaker Space. The state of the Space
     changes to **Running**.

3. After the connection is successful, a new window opens. This window shows all
   the files that you have access to in the selected project. All the changes made
   here are reflected in the Amazon SageMaker Unified Studio Space.
