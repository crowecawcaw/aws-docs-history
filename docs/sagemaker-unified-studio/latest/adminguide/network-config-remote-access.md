# Network Configuration for Remote Access

## Configuring Amazon SageMaker Unified Studio Project Profiles to allow Internet Access

To allow Spaces to be created with internet access, you can set the tooling blueprint parameter `sagemakerDomainNetworkType` to `PublicInternetOnly`. By default, it is set to `VpcOnly`. To create an Amazon SageMaker Unified Studio project profile, see [Project profiles](project-profiles.md "project-profiles.md"). To update an existing project profile's `sagemakerDomainNetworkType`, you need to ensure there are no running Spaces in the project. For more details see [Update Project Profiles](update-project-profile.md "update-project-profile.md").

## Configuring Isolated VPC for Remote Access

To configure a VPC isolated from the internet and also enable remote access from VS Code, you need to create VPC endpoints and attach them to the VPC along with security groups to allow traffic to flow through the SSH tunnel. The recommended network setup is:

### Use service created project security group

- When you create a Project, the service always creates the Security group on your behalf. You can identify the security group by:
  - Searching for the Unified Studio `ProjectId` in the AWS VPC console. The `projectId` can be found in the project overview page in the portal/URL when accessing the Project through CLI/API.
  - Run the command `cat /opt/ml/metadata/resource-metadata.json | jq .` in the Space terminal to identify which service-created security group has been attached to the Space.

- Attach the identified Security group to the VPC endpoints created above. This setup is needed only once per project and not for every Space as security is reused across the project.
- Refer to the following table and create VPC endpoints that you require for your use cases and attach them to the Amazon SageMaker Unified Studio Domain VPC:

| Service       | Endpoint                                 | Purpose                                                  | Required for                                                                      |
| ------------- | ---------------------------------------- | -------------------------------------------------------- | --------------------------------------------------------------------------------- |
| STS           | com.amazonaws.<REGION>.sts               | Authentication and temporary credential management       | Service authentication and role assumption                                        |
| SSM           | com.amazonaws.<REGION>.ssm               | Parameter Store and configuration management             | Runtime configuration retrieval                                                   |
| SSM-Messages  | com.amazonaws.<REGION>.ssmmessages       | Session Manager communication                            | Secure shell access and command execution                                         |
| SM Studio     | aws.sagemaker.<REGION>.studio            | Studio service communication                             | Workspace management and orchestration                                            |
| SM Runtime    | com.amazonaws.<REGION>.sagemaker.runtime | Model inference and runtime operations                   | Code execution and model serving                                                  |
| SM API        | com.amazonaws.<REGION>.sagemaker.api     | SageMaker service API calls                              | Resource management and service operations                                        |
| DataZone      | com.amazonaws.<REGION>.datazone          | DataZone service access                                  | Data discovery, governance, and sharing capabilities                              |
| DataZone FIPS | com.amazonaws.<REGION>.datazone-fips     | FIPS-compliant secure access to Amazon DataZone services | Secure data access compliant with Federal Information Processing Standards (FIPS) |

To create your own security groups, ensure traffic is allowed to and from the service-created security group for the Project.
