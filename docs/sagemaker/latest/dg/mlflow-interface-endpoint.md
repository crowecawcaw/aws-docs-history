# Connecting to an MLflow tracking server through an

Interface VPC Endpoint

The MLflow tracking server runs in an Amazon Virtual Private Cloud managed by Amazon SageMaker AI.
You can connect to an MLflow tracking server from an endpoint in your own VPC. Your requests to the tracking server are not exposed to the public internet.
For more information about connecting your VPC to SageMaker AI, see [Connect to SageMaker AI Within your VPC](interface-vpc-endpoint.md "interface-vpc-endpoint.md").

###### Topics

- [Create a VPC Endpoint](mlflow-interface-endpoint-create.md "mlflow-interface-endpoint-create.md")
- [Create a VPC Endpoint Policy for
  SageMaker AI MLflow](mlflow-private-link-policy.md "mlflow-private-link-policy.md")
- [Allow Access only from within your
  VPC](mlflow-private-link-restrict.md "mlflow-private-link-restrict.md")
