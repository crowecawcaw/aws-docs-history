# Manage deployments

1. From the left navigation pane, choose **SAP**.
2. Under the **Deployments** tab, select the check box next to
   the application that you want to manage, and then choose
   **Actions**. You can do the following:
   1. **Manage resources on the EC2 console**.
      You are directed to the Amazon EC2 console, where you can view and manage
      your SAP application resources, such as Amazon EC2, Amazon EBS, Amazon VPC, Subnets,
      NAT Gateways, and Elastic IPs.
   2. **View resource group with Systems Manager**. In
      the Systems Manager console, you can manage your application with built-in
      integrations through resource groups. Launch Wizard automatically tags your
      deployment with resource groups. When you access Systems Manager through Launch
      Wizard, the resources are automatically filtered for you based on your
      resource group. You can manage, patch, and maintain your applications in
      Systems Manager.
   3. **View CloudWatch application logs.** You are
      directed to the CloudWatch dashboard, where you can view your logs.
   4. **View CloudFormation template.** You are
      directed to the AWS CloudFormation to view the templates created for this
      deployment.
   5. **View Service Catalog product.** You
      are directed to the AWS Service Catalog console to view the
      AWS Service Catalog product that was created for this
      deployment.

3. Select the check box next to the application that you want to manage, and then
   choose **Manage Application**:
   - You are redirected to the **Application Detail** page
     in Application Manager if the deployment is complete, and the
     application is supported and onboarded to AWS Systems Manager for SAP.
   - You are redirected to the **Register Application**
     page in Application Manager if the deployment is complete, the
     application is supported but not onboarded to AWS Systems Manager for SAP.
   - **Manage Application** is disabled if the deployment
     is not complete, or if the application is unsupported by AWS Systems Manager for
     SAP.

4. To delete a deployment, select the application that you want to delete, and
   select **Delete**. You are prompted to confirm the
   deletion.

###### Important

When you delete a deployment, Launch Wizard attempts to delete only the
AWS resources it created in your account as part of the deployment. Launch Wizard
considers certain resources, such as security groups, infrastructure
configuration templates created during a deployment, and EFS file systems
created for a transport directory, as shared resources between multiple
deployments. Shared resources are not deleted when you delete a
deployment. 5. For more information about your application resources, choose the
**Application name**. You can then view the
**Deployment events** and **Summary**
details for your application using the tabs at the top of the page.
