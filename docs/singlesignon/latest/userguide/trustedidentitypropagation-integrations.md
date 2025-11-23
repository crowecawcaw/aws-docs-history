# Trusted identity

propagation use cases

As an IAM Identity Center administrator, you might be asked to help configure trusted identity
propagation from user facing applications to AWS services. To support this
request, you'll need the following information:

- What client-facing application will your users interface with?
- Which AWS services are used to query the data and to authorize access to
  the data?
- Which AWS service authorizes access to the data?
  Your role in enabling **trusted identity propagation use cases that do not
  involve third-party applications or custom-developed applications** is
  to:

1. [Enable IAM Identity Center](enable-identity-center.md "enable-identity-center.md").
2. [Connect your existing
   source of identities to IAM Identity Center](tutorials.md "tutorials.md").
   The remaining steps of the trusted identity configuration for these use cases are
   performed within the connected AWS services and applications. The administrators
   of the connected AWS services or applications should refer to the respective user
   guides for comprehensive service-specific guidance.

Your role in enabling **trusted identity propagation use cases that
involve third-party applications or custom-developed applications**
includes the steps of [Enable IAM Identity Center](enable-identity-center.md "enable-identity-center.md") and [connecting your source of identities](tutorials.md "tutorials.md") as well
as:

1. Configuring the connection of your identity provider (IdP) to the
   third-party party or custom-developed application.
2. Enabling IAM Identity Center to recognize the third-party or custom-developed
   application.
3. Configuring your IdP as a trusted token issuer in IAM Identity Center. For more
   information, see [Using applications with a
   trusted token issuer](using-apps-with-trusted-token-issuer.md "using-apps-with-trusted-token-issuer.md").
   The administrators of the connected applications and AWS services should refer
   to the respective user guides for comprehensive service-specific guidance.

## Analytics, data

lakehouse, and machine learning use cases

You can enable trusted propagation use cases with the following analytics and
machine learning services:

- **Amazon Redshift** - For guidance, see [Trusted identity propagation with
  Amazon Redshift](tip-usecase-redshift.md "tip-usecase-redshift.md").
- **Amazon EMR** - For guidance, see [Trusted identity propagation with
  Amazon EMR](tip-usecase-emr.md "tip-usecase-emr.md").
- **Amazon Athena** - For guidance, see [Trusted identity propagation with
  Amazon Athena](tip-usecase-ate.md "tip-usecase-ate.md").
- **SageMaker Studio** - For guidance, see [Trusted identity propagation with Amazon SageMaker Studio](trusted-identity-propagation-usecase-sagemaker-studio.md "trusted-identity-propagation-usecase-sagemaker-studio.md").

## Additional use cases

You can enable IAM Identity Center and trusted identity propagation with these additional
AWS services:

- **Amazon Q Business** - for guidance, see:
  - [Admin workflow for apps using IAM Identity Center](../../../amazonq/latest/qbusiness-ug/how-it-works.md#admin-flow-idc "../../../amazonq/latest/qbusiness-ug/how-it-works.md#admin-flow-idc").
  - [Configuring an Amazon Q Business application using
    IAM Identity Center](../../../amazonq/latest/qbusiness-ug/create-application.md "../../../amazonq/latest/qbusiness-ug/create-application.md").
  - [Configure Amazon Q Business with IAM Identity Center trusted identity
    propagation](https://aws.amazon.com/blogs//machine-learning/configuring-amazon-q-business-with-aws-iam-identity-center-trusted-identity-propagation/ "https://aws.amazon.com/blogs//machine-learning/configuring-amazon-q-business-with-aws-iam-identity-center-trusted-identity-propagation/").

- **Amazon OpenSearch Service** - for guidance, see:
  - [IAM Identity Center Trusted Identity Propagation Support for
    Amazon OpenSearch Service](../../../opensearch-service/latest/developerguide/idc-aos.md "../../../opensearch-service/latest/developerguide/idc-aos.md").
  - [Centralized OpenSearch user interface (Dashboards) with
    Amazon OpenSearch Service](../../../opensearch-service/latest/developerguide/application.md "../../../opensearch-service/latest/developerguide/application.md").

- **AWS Transfer Family** - for guidance, see:
  - [Transfer Family web
    apps](../../../transfer/latest/userguide/web-app.md "../../../transfer/latest/userguide/web-app.md").

###### Topics

- [Trusted identity propagation with
  Amazon Redshift](tip-usecase-redshift.md "tip-usecase-redshift.md")
- [Trusted identity propagation with
  Amazon EMR](tip-usecase-emr.md "tip-usecase-emr.md")
- [Trusted identity propagation with
  Amazon Athena](tip-usecase-ate.md "tip-usecase-ate.md")
- [Trusted identity propagation with Amazon SageMaker Studio](trusted-identity-propagation-usecase-sagemaker-studio.md "trusted-identity-propagation-usecase-sagemaker-studio.md")
