

End of support notice: On June 30, 2027, AWS will end support for AMS Advanced. After June 30, 2027, you will no longer be able to access the AMS Advanced console or AMS Advanced resources. For more information, see [AMS Advanced end of support](https://docs.aws.amazon.com/managedservices/latest/userguide/SunsetPlan.html). 

# Direct Change Mode use cases
<a name="dcm-use-cases"></a>

The following are uses cases for Direct Change Mode:

**Resource provision and management through CloudFormation**
+ Integrate existing CloudFormation-based tooling and processes.

**Ongoing resource management and updates**
+ Small atomic changes with low risk.
+ Changes that would otherwise run through a manual or automated RFC.
+ Tooling that requires native AWS API access.
+ The DCM role can be utilized if you're in the migration stage. Migration teams leverage the permissions on the DCM to create or modify stacks.
+ DCM roles can be used in the CI/CD pipeline to build new AMIs, create Amazon ECS tasks, and so on.