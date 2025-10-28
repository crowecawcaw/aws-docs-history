# VPC endpoints and DNS

configuration for AWS services in the AWS Management Console

The AWS Management Console calls AWS services through a combination of direct browser requests and
requests that are proxied by web servers. To direct this traffic to your AWS Management Console VPC
endpoint, you must add the VPC endpoint and configure DNS for each dependent
AWS service.

The following json files list the AWS PrivateLink supported AWS services
that are available for you to use. If a service doesn't integrate with AWS PrivateLink, it
isn't included in these files.

- [https://configuration.private-access.console.amazonaws.com/us-east-1.config.json](https://configuration.private-access.console.amazonaws.com/us-east-1.config.json "https://configuration.private-access.console.amazonaws.com/us-east-1.config.json")
- [https://configuration.private-access.console.amazonaws.com/us-east-2.config.json](https://configuration.private-access.console.amazonaws.com/us-east-2.config.json "https://configuration.private-access.console.amazonaws.com/us-east-2.config.json")
- [https://configuration.private-access.console.amazonaws.com/us-west-2.config.json](https://configuration.private-access.console.amazonaws.com/us-west-2.config.json "https://configuration.private-access.console.amazonaws.com/us-west-2.config.json")
- [https://configuration.private-access.console.amazonaws.com/ap-northeast-1.config.json](https://configuration.private-access.console.amazonaws.com/ap-northeast-1.config.json "https://configuration.private-access.console.amazonaws.com/ap-northeast-1.config.json")
- [https://configuration.private-access.console.amazonaws.com/ap-northeast-2.config.json](https://configuration.private-access.console.amazonaws.com/ap-northeast-2.config.json "https://configuration.private-access.console.amazonaws.com/ap-northeast-2.config.json")
- [https://configuration.private-access.console.amazonaws.com/ap-southeast-1.config.json](https://configuration.private-access.console.amazonaws.com/ap-southeast-1.config.json "https://configuration.private-access.console.amazonaws.com/ap-southeast-1.config.json")
- [https://configuration.private-access.console.amazonaws.com/ap-southeast-2.config.json](https://configuration.private-access.console.amazonaws.com/ap-southeast-2.config.json "https://configuration.private-access.console.amazonaws.com/ap-southeast-2.config.json")
- [https://configuration.private-access.console.amazonaws.com/ap-south-1.config.json](https://configuration.private-access.console.amazonaws.com/ap-south-1.config.json "https://configuration.private-access.console.amazonaws.com/ap-south-1.config.json")
- [https://configuration.private-access.console.amazonaws.com/ap-south-2.config.json](https://configuration.private-access.console.amazonaws.com/ap-south-2.config.json "https://configuration.private-access.console.amazonaws.com/ap-south-2.config.json")
- [https://configuration.private-access.console.amazonaws.com/ca-central-1.config.json](https://configuration.private-access.console.amazonaws.com/ca-central-1.config.json "https://configuration.private-access.console.amazonaws.com/ca-central-1.config.json")
- [https://configuration.private-access.console.amazonaws.com/eu-central-1.config.json](https://configuration.private-access.console.amazonaws.com/eu-central-1.config.json " https://configuration.private-access.console.amazonaws.com/eu-central-1.config.json")
- [https://configuration.private-access.console.amazonaws.com/eu-west-1.config.json](https://configuration.private-access.console.amazonaws.com/eu-west-1.config.json "https://configuration.private-access.console.amazonaws.com/eu-west-1.config.json")
- [https://configuration.private-access.console.amazonaws.com/eu-west-2.config.json](https://configuration.private-access.console.amazonaws.com/eu-west-2.config.json "https://configuration.private-access.console.amazonaws.com/eu-west-2.config.json")
- [https://configuration.private-access.console.amazonaws.com/il-central-1.config.json](https://configuration.private-access.console.amazonaws.com/il-central-1.config.json "https://configuration.private-access.console.amazonaws.com/il-central-1.config.json")
  Use the `ServiceName` field for the corresponding service’s VPC endpoint to
  add to your VPC.

###### Note

We update this list each month as we add support for AWS Management Console Private Access to more
service consoles. To stay current, periodically pull the preceding list of files and
update your VPC endpoints.
