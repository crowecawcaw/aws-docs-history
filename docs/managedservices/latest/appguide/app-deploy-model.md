# Application deployment model

Considerations of how you plan your application deployments. See [What is my operating model?](op-model-aog.md "op-model-aog.md")

- Automated or manual? No deployment automation means no Auto Scale. If you request access and log in and manually update your application,
  and your update fails. AMS would expect you to rollback your update or alert us through a service request so we can assist you.
- If automated, what is the framework? Scripts? Agent-based (puppet/chef)? Agentless
  (SALT/Ansible)? CodeDeploy? Agent-based and agentless deployment tooling require a
  separate instance be created and deployed as the master server for the tooling.
  AMS expects you to be aware of all of the elements necessary for successful
  application deployment tooling; however, we are happy to help with related
  infrastructure questions.
- Do your Line-of-Business applications (those applications that you use to create and manage your applications) require patching?
