End of support notice: On May 20, 2026, AWS
will end support for AWS SimSpace Weaver. After May 20, 2026, you will
no longer be able to access the SimSpace Weaver console or SimSpace Weaver resources.
For more information, see [AWS SimSpace Weaver end of support](simspaceweaver-end-of-support.md "simspaceweaver-end-of-support.md").

# Failure during custom container creation

If you get an error `no basic auth credentials` after you run
`quick-start.py` then there could be a problem with
your temporary credentials for Amazon ECR. Run the following command with your
AWS Region ID and AWS account number:

```
aws ecr get-login-password --region `region` | docker login --username AWS --password-stdin `account_id`.dkr.ecr.region.amazonaws.com
```

###### Example

```
aws ecr get-login-password --region us-west-2 | docker login --username AWS --password-stdin 111122223333.dkr.ecr.region.amazonaws.com
```

###### Important

Make sure that the AWS Region you specify is the same one that you use for your simulation. Use one of the
AWS Regions that SimSpace Weaver supports. For more information, see [SimSpace Weaver endpoints and quotas](service-quotas.md "service-quotas.md").

After you run the `aws ecr` command, run `quick-start.py` again.

###### Other troubleshooting resources to check

- [Troubleshooting custom containers](working-with_custom-containers_troubleshooting.md "working-with_custom-containers_troubleshooting.md")
- [Amazon ECR troubleshooting](../../../AmazonECR/latest/userguide/troubleshooting.md "../../../AmazonECR/latest/userguide/troubleshooting.md")
  in the _Amazon ECR User Guide_
- [Setting up with Amazon ECR](../../../AmazonECR/latest/userguide/get-set-up-for-amazon-ecr.md "../../../AmazonECR/latest/userguide/get-set-up-for-amazon-ecr.md") in the
  _Amazon ECR User Guide_
