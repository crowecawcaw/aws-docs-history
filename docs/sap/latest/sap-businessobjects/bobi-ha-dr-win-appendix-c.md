# Additional Tips

## Tagging AWS Resources

Adding tags to AWS objects will make it much easier to manage the SAP HA environment, and can also help you search for resources quickly. You can use Amazon EC2 API calls in conjunction with a special tag filter. For more information about tagging resources, see the [AWS documentation](../../../awsconsolehelpdocs/latest/gsg/tagging-resources.md "../../../awsconsolehelpdocs/latest/gsg/tagging-resources.md").

## Third-Party Software Components

Additional third-party components might be integral to running business processes within an SAP environment. After you determine your requirements, consider leveraging some of the concepts discussed in this guide, such as:

- Installing third-party software components on multiple instances
- Creating Amazon EBS-backed AMI images of key third-party systems, so you can launch them on demand in case of failures
- Using multiple interfaces to control access to specific software components
- Using multiple Availability Zones for critical third-party software components
