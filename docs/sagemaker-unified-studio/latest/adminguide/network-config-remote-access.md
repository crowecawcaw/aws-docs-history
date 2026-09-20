

# Network Configuration for Remote Access
<a name="network-config-remote-access"></a>

## Configuring Amazon SageMaker Unified Studio Project Profiles to allow Internet Access
<a name="configuring-unified-studio-project-profiles-internet-access"></a>

To allow Spaces to be created with internet access, you can set the tooling blueprint parameter `sagemakerDomainNetworkType` to `PublicInternetOnly`. By default, it is set to `VpcOnly`. To create an Amazon SageMaker Unified Studio project profile, see [Project profiles](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/project-profiles.html). To update an existing project profile's `sagemakerDomainNetworkType`, you need to ensure there are no running Spaces in the project. For more details see [Update Project Profiles](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/update-project-profile.html).

**Note**  
This configuration is only applicable for enabling Local IDE support in Identity Center based domains, not in IAM-based domains. 

## Configuring Isolated VPC for Remote Access
<a name="configuring-isolated-vpc-remote-access"></a>

To configure a VPC isolated from the internet and also enable remote access from VS Code, you need to create VPC endpoints and attach them to the VPC along with security groups to allow traffic to flow through the SSH tunnel. The recommended network setup is:

### Use service created project security group
<a name="use-service-created-project-security-group"></a>
+ When you create a Project, the service always creates the Security group on your behalf. You can identify the security group by:
  + Searching for the Unified Studio `ProjectId` in the AWS VPC console. The `projectId` can be found in the project overview page in the portal/URL when accessing the Project through CLI/API.
  + Run the command `cat /opt/ml/metadata/resource-metadata.json | jq .` in the Space terminal to identify which service-created security group has been attached to the Space.
+ Attach the identified Security group to the VPC endpoints created above. This setup is needed only once per project and not for every Space as security is reused across the project.
+ Refer to the following table and create VPC endpoints that you require for your use cases and attach them to the Amazon SageMaker Unified Studio Domain VPC:


<table>
<thead>
  <tr><th>Service</th><th>Endpoint</th><th>Purpose</th><th>Required for</th></tr>
</thead>
<tbody>
  <tr><td>STS</td><td>com.amazonaws.&lt;REGION&gt;.sts</td><td>Authentication and temporary credential management</td><td>Service authentication and role assumption</td></tr>
  <tr><td>SSM</td><td>com.amazonaws.&lt;REGION&gt;.ssm</td><td>Parameter Store and configuration management</td><td>Runtime configuration retrieval</td></tr>
  <tr><td>SSM-Messages</td><td>com.amazonaws.&lt;REGION&gt;.ssmmessages</td><td>Session Manager communication</td><td>Secure shell access and command execution</td></tr>
  <tr><td>SM Studio</td><td>aws.sagemaker.&lt;REGION&gt;.studio</td><td>Studio service communication</td><td>Workspace management and orchestration</td></tr>
  <tr><td>SM Runtime</td><td>com.amazonaws.&lt;REGION&gt;.sagemaker.runtime</td><td>Model inference and runtime operations</td><td>Code execution and model serving</td></tr>
  <tr><td>SM API</td><td>com.amazonaws.&lt;REGION&gt;.sagemaker.api</td><td>SageMaker service API calls</td><td>Resource management and service operations</td></tr>
  <tr><td>DataZone</td><td>com.amazonaws.&lt;REGION&gt;.datazone</td><td>DataZone service access</td><td>Data discovery, governance, and sharing capabilities</td></tr>
  <tr><td>DataZone FIPS</td><td>com.amazonaws.&lt;REGION&gt;.datazone-fips</td><td>FIPS-compliant secure access to Amazon DataZone services</td><td>Secure data access compliant with Federal Information Processing Standards (FIPS)</td></tr>
</tbody>
</table>


To create your own security groups, ensure traffic is allowed to and from the service-created security group for the Project.