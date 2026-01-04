# Automated NF installation and configuration

AWS TNB performs the installation and configuration of the 5G NFs (for example, CU,
AMF, UPF, and SMF) on the provisioned infrastructure.

**Recommendations:** Verify the NF packages and Helm charts
are properly designed to use the capabilities of Kubernetes and the underlying cloud
infrastructure. Implement automated testing and canary deployments to validate the NF
installations.

**Practical advice:** Monitor the NF deployments for errors
or issues and leverage the AWS TNB APIs to programmatically retrieve logs and metrics for
troubleshooting. Establish automated rollback and recovery procedures in case of deployment
failures.
