

# Accessing domain management
<a name="accessing-domain-management-idc"></a>

Access to domain management requires an administration project named `admin-project-{{accountID}}` to be present in your domain. Amazon SageMaker Unified Studio creates this project automatically, and it controls who can access domain management.

All members of the administration project are granted access to domain management and have a designation of Administrator. To remove a user's access to domain management, remove them from this project.

The administration project is created under the following conditions:
+ **Quick setup flow** – The project is created automatically for new domains.
+ **Manual setup flow** – The project is created when you enable the Tooling blueprint.

After the administration project is created, you can access domain management from two locations:
+ **From the AWS SageMaker console** – Navigate to your domain in the SageMaker console. In the domain details page, choose **Domain management** at the top of the page. This opens domain management in a new tab.  
![Domain management button in the SageMaker console domain details page](http://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/images/AdminPortal/DomainDetail.png)
+ **From the Amazon SageMaker Unified Studio portal** – Log in to the Amazon SageMaker Unified Studio portal. In the left navigation panel, choose **Domain management**. This opens domain management in a new tab.

  If the **Domain management** link is not present, your user either doesn't have access to domain management or the administration project has not been created. For more information, see [Setting up access to domain management](#setup-access-domain-management).  
![Domain management link in the Amazon SageMaker Unified Studio portal left navigation](http://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/images/AdminPortal/PortalAccess.png)

## Setting up access to domain management
<a name="setup-access-domain-management"></a>

To access domain management, an administration project named `admin-project-{{accountID}}` must exist in the domain. This project controls who can access domain management. You might need to take additional steps to set up access to domain management in the following scenarios.

**Note**  
To set up access to domain management, the Tooling blueprint must first be enabled. Choose the **Domain management** button in the banner of the domain details page in the SageMaker console. You are prompted to enable the Tooling blueprint. As part of the blueprint enablement, an administration project named `admin-project-{{accountID}}` is created. Return to the domain details page and choose the **Domain management** button in the banner to access domain management.

### If an administration project exists in the domain
<a name="setup-access-admin-project-exists"></a>

If an administration project (for example, `admin-project-{{accountID}}`) already exists in your domain, take the following steps to set up access to domain management:
+ In the AWS SageMaker console on the domain details page, choose the **Domain management** button in the banner at the top. The [SageMakerStudioAdminIAMDefaultExecutionPolicy](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/security-iam-awsmanpol-SageMakerStudioAdminIAMDefaultExecutionPolicy.html) IAM policy is updated for the administration project's provisioning IAM role. This also runs an update project action on the administration project, which can take a few minutes to complete. Domain management is not accessible until the project update completes.
+ You can also set up access to domain management from the Tooling blueprint. On the **Provisioning** tab, choose **Update project**. This performs an update project action to attach the [SageMakerStudioAdminIAMDefaultExecutionPolicy](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/security-iam-awsmanpol-SageMakerStudioAdminIAMDefaultExecutionPolicy.html) AWS managed policy to the administration project's execution role.  
![Update project option in the Tooling blueprint Provisioning tab](http://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/images/AdminPortal/UpdateProjectConsole.png)

### If an administration project does not exist in the domain
<a name="setup-access-admin-project-not-exists"></a>

If an administration project does not exist in your domain, take the following steps to create it and set up access to domain management:
+ In the AWS SageMaker console on the domain details page, choose the **Domain management** button in the banner at the top. Choose **Set up** to create the administration project. This begins the process to create the `admin-project-{{accountID}}` project for your domain. A banner confirmation appears when domain management is successfully set up. You can now access domain management using the methods described in [Accessing domain management](#accessing-domain-management-idc).
+ You can also set up access to domain management from the Tooling blueprint. On the **Provisioning** tab, choose **Create** to create the administration project. After the project is successfully created, you can access domain management using the methods described in [Accessing domain management](#accessing-domain-management-idc).  
![Create administration project option in the Tooling blueprint Provisioning tab](http://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/images/AdminPortal/CreateProjectConsole.png)
+ From the Amazon SageMaker Unified Studio portal, a banner displays for root domain owners with an action button to domain management. If the administration project has not been created, a popup directs you to the AWS Management Console to create the project using the steps above.