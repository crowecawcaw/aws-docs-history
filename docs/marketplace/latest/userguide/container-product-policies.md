# Container-based product requirements for AWS Marketplace

AWS Marketplace maintains the following requirements for all container-based products and offerings
on AWS Marketplace. These requirements help to promote a safe, secure, and trustworthy catalog for our
customers. We also encourage sellers to review implementation of additional controls and
protocols as applicable to meet the needs of their specific products.

All products and their related metadata are reviewed when submitted to ensure they meet or exceed current AWS Marketplace policies. These policies are regularly updated to align with evolving security guidelines. AWS Marketplace continuously scans products to verify that existing listings continue to meet any changes to these requirements. If a product falls out of compliance, AWS Marketplace will contact the seller to update their product to meet new standards. In some cases, products might be temporarily made unavailable to new subscribers until issues are resolved. This process helps maintain the security and trustworthiness of the AWS Marketplace platform for all users.

###### Topics

- [Security policies](#container-security-requirements "#container-security-requirements")
- [Customer information
  requirements](#container-customer-info-requirements "#container-customer-info-requirements")
- [Product usage requirements](#container-usage-requirements "#container-usage-requirements")
- [Architecture requirements](#container-architecture-requirements "#container-architecture-requirements")
- [Helm chart structure requirements](#helm-chart-structure-requirements "#helm-chart-structure-requirements")
- [Container product usage
  instructions](#container-product-usage-instructions "#container-product-usage-instructions")
- [Requirements for Amazon EKS add-on products](#publishing-eks-add-on "#publishing-eks-add-on")

## Security policies

All container-based products must adhere to the following security
requirements:

- Container images must not contain any known vulnerabilities, malware or End-of-Life (EoL) software packages and operating systems.
- Containers must not request AWS credentials to access AWS services. When
  your product needs to access AWS services, you must use one of the
  following:
  - IAM roles for service accounts, for Amazon Elastic Kubernetes Service (Amazon EKS)
    workloads.
  - IAM roles for tasks, for Amazon Elastic Container Service (Amazon ECS) workloads.

- Container-based products must only require least privileges to run. For more information, see [Security in Amazon Elastic Container Service](../../../AmazonECS/latest/developerguide/security.md "../../../AmazonECS/latest/developerguide/security.md") and [Security in Amazon EKS](../../../eks/latest/userguide/security.md "../../../eks/latest/userguide/security.md").
- Container images should be configured to run with non-root privileges by default.
- Containers must not contain any hardcoded secrets such as passwords(even hashed) for system users and services, private keys, credentials, etc.
- Authentication in any services running inside the container must not use password-based authentication, even if the password is generated, reset, or defined by the user at launch. Null and blank passwords are not allowed as well.
- Container images must not include layers with unsupported architectures (for example, in-toto Attestation Framework metadata).

## Customer information

requirements

All container-based products must adhere to the following customer information
requirements:

- Software must not collect or export customer data without the customer's
  knowledge and express consent except as required by BYOL (Bring Your Own
  License). Applications that collect or export customer data must follow these
  guidelines:
  - The collection of the customer data must be self-service, automated,
    and secure. Buyers must not need to wait for sellers to approve to
    deploy the software.
  - Collection of customer data must be consistent with your agreements with AWS,
    including but not limited to, the [AWS
    Marketplace Terms and Conditions](https://aws.amazon.com/legal/seller-terms/ "https://aws.amazon.com/legal/seller-terms/"), [AWS
    Service Terms](https://aws.amazon.com/service-terms/ "https://aws.amazon.com/service-terms/"), [AWS Privacy Notice](https://aws.amazon.com/privacy/ "https://aws.amazon.com/privacy/")
    and [AWS Customer Agreement](https://aws.amazon.com/agreement/ "https://aws.amazon.com/agreement/").
  - Payment information must not be collected.

## Product usage requirements

All container-based products must adhere to the following product usage requirements:

- Sellers can only list fully functioning products. Beta or prerelease products
  for trial or evaluation purposes are not allowed. Developer, community, and BYOL
  editions of commercial software are supported if the seller provides an
  equivalent paid version on AWS Marketplace within 90 days of providing the free
  edition.
- All of a container-based product's usage instructions must include all steps
  to deploy container-based products. Usage instructions must provide commands and
  deployment resources pointing to the corresponding container images on
  AWS Marketplace.
- Container-based products must include all container images that a subscriber
  needs to use the software. In addition, container-based products must not
  require a user to launch the product using any images from outside AWS Marketplace (for
  example, container images from third-party repositories).
- Containers and their software must be deployable in a self-service manner and
  must not require additional payment methods or costs. Applications that require
  external dependencies on deployment must follow these guidelines:
  - The requirement must be disclosed in the description or the usage
    instructions of the listing. For example, _This product
    requires an internet connection to deploy properly. The following
    packages are downloaded on deployment: <list of
    package>._
  - Sellers are responsible for the use of and ensuring the availability
    and security of all external dependencies.
  - If the external dependencies are no longer available, the product must
    be removed from AWS Marketplace as well.
  - The external dependencies must not require additional payment methods
    or costs.

- Containers that require an ongoing connection to external resources not under
  the direct control of the buyer—for example, external APIs or
  AWS services managed by the seller or a third party—must follow these
  guidelines:
  - The requirement must be disclosed in the description or the usage
    instructions of the listing. For example, _This product
    requires an ongoing internet connection. The following ongoing
    external services are required to properly function: <list of
    resources>._
  - Sellers are responsible for the use of and ensuring the availability
    and security of all external resources.
  - If the external resources are no longer available, the product must be
    removed from AWS Marketplace as well.
  - The external resources must not require additional payment methods or
    costs and the setup of the connection must be automated.

- Product software and metadata must not contain language that redirects users
  to other cloud platforms, additional products, or upsell services that aren't
  available on AWS Marketplace.
- If your product is an add-on to another product or another ISV’s product, your
  product description must indicate that it extends the functionality of the other
  product and that without it, your product has very limited utility. For example,
  _This product extends the functionality of <product name> and
  without it, this product has very limited utility. Please note that
  <product name> might require its own license for full functionality with
  this listing._

## Architecture requirements

All container-based products must adhere to the following architecture requirements:

- Source container images for AWS Marketplace must be pushed to the Amazon Elastic Container Registry (Amazon ECR)
  repository owned by AWS Marketplace. You can create these repositories in the AWS Marketplace Management Portal
  under server products for each of your container product listings.
- Container images must be based on Linux.
- Paid container-based products must be able to be deployed on [Amazon ECS](../../../AmazonECS/latest/developerguide/Welcome.md "../../../AmazonECS/latest/developerguide/Welcome.md"), [Amazon EKS](../../../eks/latest/userguide/what-is-eks.md "../../../eks/latest/userguide/what-is-eks.md"), or [AWS Fargate](../../../AmazonECS/latest/userguide/what-is-fargate.md "../../../AmazonECS/latest/userguide/what-is-fargate.md").
- Paid container-based products with contract pricing and an integration with
  AWS License Manager should deploy on Amazon EKS, Amazon ECS, AWS Fargate, Amazon EKS Anywhere, Amazon ECS Anywhere, Red
  Hat OpenShift Service on AWS (ROSA), self-managed Kubernetes clusters
  on-premises, or on Amazon Elastic Compute Cloud.
- For Helm chart products, container image references must be structured according to the [Helm chart structure requirements](#helm-chart-structure-requirements "#helm-chart-structure-requirements") to support cross-region deployment.
- If your container-based product requires the buyer to deploy an Amazon Machine Image (AMI),
  it must either be an AWS-managed AMI or a separate AMI published in AWS Marketplace.
  If you publish your own AMI in AWS Marketplace, it must comply with the [AMI-based product requirements for AWS Marketplace](product-and-ami-policies.md "product-and-ami-policies.md")
  and you must indicate that it's an add-on product as required in the [Product usage policies](product-and-ami-policies.md#product-usage "product-and-ami-policies.md#product-usage").
  You can price your AMI-based product as BYOL because it's an extension of your container-based offering.
  AWS Marketplace scans AMI-based products for unpatched common vulnerabilities and exposures (CVEs) and security requirements.
  Your buyers must also subscribe to your AMI-based product before deploying it.

## Helm chart structure requirements

All Helm chart products submitted to AWS Marketplace must adhere to the following structure requirements to ensure proper regionalization
and deployment across AWS regions:

- Container image references must be defined exclusively in the `values.yaml` file and not hardcoded in any other
  files within the Helm chart. This enables AWS Marketplace to automatically replace these references when replicating your product to different regions.
- The `values.yaml` file must use variables for all container image references, including:
  - `Repository URI`
  - `Image name`
  - Optionally, you can include `registry` and `tag` fields on the same level as the repository to build up your image reference.

- Helm templates must reference these variables using the standard Helm templating syntax (e.g., `{{ .Values.image.repository }}:{{ .Values.image.tag }}`).
- Avoid using conditional logic in templates that would bypass the image references defined in `values.yaml`.
- When testing your Helm chart with different AWS regions, ensure that changing the region in `values.yaml` correctly updates all
  image references in the deployed resources.

AWS Marketplace validates that all container image references are properly defined in the `values.yaml` file during the product submission process.
Products that do not meet these requirements will be rejected.

### Example: Best practice for container image references in Helm charts

The following examples demonstrate approaches for structuring container image references in Helm charts:

**`values.yaml` (recommended format):**

```
image:
  registry: "709825985650.dkr.ecr.us-east-1.amazonaws.com"
  repository: "accuknox/kubearmor"
  tag: "v1.1.1"
```

###### Note

We recommend the approach above for the structure of your `values.yaml` , but the alternative methods
below are also valid.

**`values.yaml` (alternative format):**

```
image:
  repository: 709825985650.dkr.ecr.us-east-1.amazonaws.com/guance/datakit
  tag: 1.0
```

**`values.yaml` (alternative format):**

```
image:
  repository: 709825985650.dkr.ecr.us-east-1.amazonaws.com/guance/datakit:1.0
```

###### Note

For deployment template, the format below is the only valid format available.

**Deployment template:**

```
containers:
- name: kubearmor
  image: "{{ .Values.image.registry }}/{{ .Values.image.repository }}:{{ .Values.image.tag }}"
```

**Incorrect approach (do not use):**

```
containers:
- name: kubearmor
  image: "709825985650.dkr.ecr.us-east-1.amazonaws.com/accuknox/kubearmor:v1.1.1"
```

## Container product usage

instructions

When creating usage instructions for your container product, follow the steps and
guidance in [Creating AMI and container product usage
instructions for AWS Marketplace](ami-container-product-usage-instructions.md "ami-container-product-usage-instructions.md").

### Helm chart usage instructions

When creating usage instructions for Helm chart products:

- Clearly document all configurable parameters in your `values.yaml` file, including image repository, tag, and registry parameters.
- Provide examples of how to override these parameters when installing the Helm chart.
- Do not instruct users to modify any files other than `values.yaml` or to use `--set` parameters when installing the chart.
- Include information about how your product handles regionalization of container images.

## Requirements for Amazon EKS add-on products

An Amazon EKS add-on is software that provides operational capabilities to
Kubernetes applications but isn't specific to the application. For
example, an Amazon EKS add-on includes observability agents or Kubernetes
drivers that allow the cluster to interact with underlying AWS resources for
networking, compute, and storage.

As a seller of container products, you can choose among several deployment options
including Amazon EKS. You can publish a version of your product as an AWS Marketplace add-on into the
Amazon EKS add-on catalog. Your add-on appears in the Amazon EKS console next to add-ons
maintained by AWS and other vendors. Your buyers can deploy your software as an add-on
just as easily as they do the other add-ons.

For more information, see [Amazon EKS add-ons](../../../eks/latest/userguide/eks-add-ons.md "../../../eks/latest/userguide/eks-add-ons.md") in the
_Amazon EKS User Guide_.

### Preparing your container product as an AWS Marketplace

add-on

To publish your container product as an AWS Marketplace add-on, it must meet the following
requirements:

- Your container product must be published in AWS Marketplace.
- Your container product must be built compatible for both AMD64 and ARM64
  architectures.
- Your container product must not use the Bring Your Own License (BYOL)
  [pricing model](pricing-container-products.md "pricing-container-products.md").

###### Note

BYOL is not supported for Amazon EKS add-on delivery.

- You must adhere to all [container-based product requirements](container-product-policies.md "container-product-policies.md") including pushing all
  container images and Helm charts into AWS Marketplace managed Amazon ECR
  repositories. This requirement includes open-source images, for example,
  `nginx`. Images and charts can't be hosted in other external
  repositories including, but not limited to, [Amazon ECR Public
  Gallery](../../../AmazonECR/latest/public/public-repositories.md "../../../AmazonECR/latest/public/public-repositories.md"), Docker Hub, and
  Quay.
- **Helm charts** - Prepare and package your
  software as a Helm chart. The Amazon EKS
  add-on framework converts a Helm chart into a Kubernetes manifest. Some
  Helm features are not supported within Amazon EKS systems. The
  following list describes the requirements that must be met before
  onboarding your software as an Amazon EKS add-on. In this list, all Helm commands use
  Helm version 3.8.1:
  - All `Capabilities` objects are supported, with an
    exception for `.APIVersions`. `.APIVersions`
    is not supported for non-built-in custom Kubernetes
    APIs.
  - Only the `Release.Name` and
    `Release.Namespace` objects are supported.
  - Helm hooks and the `lookup` function are
    not supported.
  - All dependent charts must be located within the main
    Helm chart (specified with repository path
    file://...).
  - The Helm chart must successfully pass
    Helm Lint and Helm Template with
    no errors. The commands are as follows:
    - Helm Lint – `helm lint
`helm-chart``

    Common issues include undeclared charts in the parent
    chart’s metadata. For example, `chart metadata is
 missing these dependencies: chart-base Error: 1 chart(s)
 linted, 1 chart(s) failed`
    - Helm Template – `helm template
 `chart-name`
`chart-location` —set
 k8version=`Kubernetes-version`  —kube-version
 `Kubernetes-version` —namespace`addon-namespace`  —include-crds —no-hooks —f
 `any-overriden-values``

    Pass any overridden configurations with the
    `—f` flag.

  - Store all container binaries in AWS Marketplace Amazon ECR repos. To create a
    manifest, use the Helm template command that's shown
    earlier. Search the manifest for any external image references such
    as `busybox` or `gcr` images. Upload all
    container images along with dependencies into AWS Marketplace Amazon ECR repos
    created by using the **Add Repository** option in
    the request dropdown.

- **Custom configuration** – You can add
  custom variables during the deployment. For information about how to
  identify the end user experience, name the software
  `aws_mp_configuration_schema.json`, and package into a
  wrapper with the Helm chart, see [Amazon EKS
  add-ons: Advanced configuration](https://aws.amazon.com/blogs/containers/amazon-eks-add-ons-advanced-configuration/ "https://aws.amazon.com/blogs/containers/amazon-eks-add-ons-advanced-configuration/").

According to [The "$schema" Keyword](https://json-schema.org/draft/2020-12/json-schema-core#name-the-schema-keyword "https://json-schema.org/draft/2020-12/json-schema-core#name-the-schema-keyword"), `$schema` must be a URI that
points to a valid `application/schema+json` resource.

This file must not accept any sensitive information such as passwords,
license keys, and certificates.

To handle secrets and certificate installations, you can provide post- or
pre-Add-on installation steps to end users. The product should not rely on
any external licenses. The product should work based on AWS Marketplace
entitlements.

For more information about limitations for
`aws_mp_configuration_schema.json`, see [Add-on configuration requirements and best
practices for add-on providers](#eks-addon-configuration "#eks-addon-configuration").

- **Identify and create the namespace that the software
  will be deployed in** – In the first release of your
  product, you must identify the namespace that the software will be deployed
  in by adding a templatized namespace.
- **Custom resource definitions (CRDs)** –
  Amazon EKS addon framework does not support installation of CRDs
  and custom resource declarations based on CRDs applied
  with the same add-on. If your add-on has custom resources and relies on CRDs, you can either:
  - **Publish two add-ons:**Split CRD definition into
    a separate add-on (separate helm chart) and the actual
    [custom resource](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/ "https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/")
    installation into a separate add-on.
  - **Publish a single add-on with additional manual instructions:** Publish a single add-on which installs the CRDs on cluster. Provide usage instructions
    along with kubernetes manifest files for end users to set up custom resources that depend on
    those CRDs.

- **Create the `serviceAccount` if
  applicable** – If the software is either a paid software
  on AWS Marketplace or must connect with other AWS services, make sure that the
  Helm chart creates `serviceAccount` by
  default. If the `serviceAccount` creation is handled by a
  parameter in a `values.yaml` file, set the parameter value to
  `true`. For example, `serviceAccount.create =
true`. This is required because the customer might choose to
  install the add-on by inheriting permissions from the underlying node
  instance which already has the required permissions. If the Helm chart
  doesn't create the `serviceAccount`, then the permissions can't
  be tied to the `serviceAccount`.
- **Traceable Deployments or Daemonsets**
  – Make sure your Helm chart has a daemonset or deployment. Amazon EKS
  addon framework tracks deployment of your Amazon EKS resources using them.
  Without a traceable deployment or daemonset, your addon will face an
  deployment error. If your addon does not have a deployment or daemonset, for
  example, if your addon deploys a bunch of Custom resources or a Kubernetes
  job which are not traceable, add a dummy deployment or daemonset
  object.
- **Support for AMD and ARM architectures**
  – Many Amazon EKS customers use ARM64 today to use AWS Graviton
  instances. Third-party software must support both architectures.
- **Integrate with licensing or metering APIs from
  AWS Marketplace** – AWS Marketplace supports multiple billing models. For
  more information, see [Container product billing, metering,
  and licensing integrations](container-products-billing-integration.md "container-products-billing-integration.md"). If you want to
  sell your product through PAYG mechanisms, see [Configuring custom metering for container products with
  AWS Marketplace Metering Service](container-metering-meterusage.md "container-metering-meterusage.md"). If you want to sell
  your product through an upfront or contract model, see [Contract pricing for container products
  with AWS License Manager](container-license-manager-integration.md "container-license-manager-integration.md").
- **Upload the software and all the artifacts and
  dependencies** – The Helm chart must be self-contained,
  and it must not require dependencies from external sources, for example,
  GitHub. If the software requires external dependencies,
  then the dependencies must be pushed to AWS Marketplace private Amazon ECR repositories
  under the same AWS Marketplace listing.
- **Provide deployment instructions on your
  website** – We request that you host a deployment guide
  for customers to identify how to deploy your software through the [create-addon](../../../cli/latest/reference/eks/create-addon.md "../../../cli/latest/reference/eks/create-addon.md") command.
- **Add-on permissions/IAM roles** –
  If your add-on published from AWS Marketplace requires access to an AWS
  service, your software should have a Kubernetes service account annotated
  with IAM policies to access AWS services. You can choose from two options
  for your service account to make API requests to AWS services:

      + Credentials via IRSA: This option allows your software to obtain
       assume credentials from the Identity and Access Management (IAM) Role Service
       (IRSA). For more information, see [IAM roles for service accounts.](../../../eks/latest/userguide/iam-roles-for-service-accounts.md "../../../eks/latest/userguide/iam-roles-for-service-accounts.md")
      + Amazon EKS pod identity: This option allows your software to use the
       Pod Identity of the Amazon EKS pod to make API requests to AWS services.
       For more information, see [Learn how EKS Pod Identity
       grants pods access to AWS services](../../../eks/latest/userguide/pod-identities.md "../../../eks/latest/userguide/pod-identities.md")

  Your add-on must have an additional configuration file named
  `aws_mp_addon_parameters.json`
  in the top level of the Helm chart, in the same directory as the current custom
  configuration schema (`aws_mp_configuration_schema.json`). Currently,
  this file only handles pod identity-compatible permissions. The file format is
  as follows:

```
{
  "permissions": {
      "isPodIdentityCompatible" : true,
      "permissionsList": [
       {
        "serviceAccount" : "String",
        "managedPolicies" : ["Policy Arn"],
       }
     ]
    }
  }
```

**File name: `aws_mp_addon_parameters.json`**

###### Note

The `aws_mp_addon_parameters.json` file enables the **Add-on access**
section in the **Add-on configuration settings** page of the Amazon EKS console

| Field name              | Type         | Notes                                                                                                                                                | Example value                                |
| ----------------------- | ------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------- |
| isPodIdentityCompatible | Boolean      | Only `true` is supported for now. Field shows if the<br>permissions described in the following permissionsList list are<br>fitting with pod-identity | TRUE                                         |
| serviceAccount          | String       | The name of the service account the add-on will use to<br>access the permissions                                                                     | `kpow`                                       |
| managedPolicies         | List<String> | List of policy arns to use for this service account that may be<br>assumed by the EKS add-on                                                         | `["arn:aws:iam::aws:policy/ReadOnlyAccess"]` |

###### Note

Pay-as-you-go (PAYG) add-on products from AWS Marketplace can't use Amazon EKS Pod
Identity and must use IAM Roles for Service Accounts (IRSA) for access control.

- **Version updates** – Amazon EKS releases
  new Kubernetes versions a few weeks after the upstream release. As new Amazon EKS
  cluster versions become generally available, vendors have 45 days to certify
  or update their software to be compatible with the new Amazon EKS cluster version
  release. If your current versions of the add-on supports the new Kubernetes
  version, validate and certify the same so that we can update the version
  compatibility matrix. If a new add-on version is needed to support the new
  Kubernetes version release, then please submit the new version for
  onboarding.
- Partner’s software must fall into one of the following types or be an
  operational software that will enhance Kubernetes or Amazon EKS: Gitops |
  monitoring | logging | cert-management | policy-management | cost-management
  | autoscaling | storage | kubernetes-management | service-mesh | etcd-backup
  | ingress-service-type | load-balancer | local-registry| networking |
  Security | backup | ingress-controller | observability
- Software cannot be [Container Network Interface (CNI)](https://github.com/containernetworking/cni "https://github.com/containernetworking/cni").
- Software must be sold through AWS Marketplace and integrated with Licensing and
  metering APIs for paid products. BYOL products are not accepted.

### Add-on configuration requirements and best

practices for add-on providers

Amazon EKS requires configuration as a [Helm JSON schema](https://helm.sh/docs/topics/charts/#schema-files "https://helm.sh/docs/topics/charts/#schema-files")
string from add-on providers. Add-ons that either need required configurations or
allow optional configurations must include a
`aws_mp_configuration_schema.json` file with the Helm Chart submitted
to AWS Marketplace. Amazon EKS will use this schema to validate the configuration input from
customers and reject API calls with input values that do not conform to the schema.
Add-on configurations typically fall under two categories:

- Configuration for general Kubernetes properties like labels, tolerations,
  nodeSelector, etc.
- Configurations that are add-on specific like license key, feature
  enablement, URLs, etc.

This section is focused on the first category related to general Kubernetes
properties.

Amazon EKS recommends following best practices around configuration of Amazon EKS
add-ons.

- [Schema requirements](#schema-requirements "#schema-requirements")
- [Common parameters that are allowed for
  configuration](#parameters-allowed "#parameters-allowed")
- [Common parameters that aren't allowed for
  configuration](#parameters-not-available "#parameters-not-available")

#### Schema requirements

When defining the json schema, ensure you use a version of jsonschema that is
supported by Amazon EKS add-ons.

The list of supported schemas:

- https://json-schema.org/draft-04/schema
- https://json-schema.org/draft-06/schema
- https://json-schema.org/draft-07/schema
- https://json-schema.org/draft/2019-09/schema

Using any other json schema version is incompatible with Amazon EKS add-ons and
will cause the add-on to be unable to be released until this is fixed.

**Example Helm schema file**

```
{
"$schema": "http://json-schema.org/schema#",
  "type": "object",
  "properties": {
"podAnnotations": {
"description": "Pod Annotations"
"type": "object"
    },
    "podLabels": {
"description": "Pod Labels"
"type": "string"
    },
    "resources": {
"type": "object"
"description": "Resources"
    },
    "logLevel": {
"description": "Logging Level"
"type": "string",
      "enum": [
        "info",
        "debug"
      ]
    },
    "config": {
"description": "Custom Configuration"
"type": "object"
    }
  }
}
```

**camelCase**

Configuration parameters are required to be camelCase, and will be
rejected if not adhering to this format.

**Descriptions are required**

Always include meaningful descriptions for schema properties. This
description will be used to render label names in Amazon EKS console for
each configuration parameter.

**RBAC definition**

Add-on providers need to define and supply the RBAC permissions
needed to successfully install the add-on using the principle of
least privilege. If RBAC permissions need to change for newer
versions of add-on or any fixes to address a CVE, add-on providers
will need to inform the Amazon EKS team about this change. Required
permissions for each Kubernetes resource should be restricted to the
resource name of the object.

```
apiGroups: ["apps"]
resources: ["daemonsets"]
resourceNames: ["ebs-csi-node"]
verbs: ["create", "delete", "get", "list", "patch", "update", "watch"]
```

**Secrets Management**

This section only applies to add-ons that need customers to
configure secret information like application key, API key,
password, etc. Currently, Amazon EKS APIs do not support passing in
secret information in plain text due to the security implications.
However, customers can use configuration to pass in the name of the
Kubernetes Secret that holds the keys needed by the add-on.
Customers will be required to create Kubernetes Secret objects
containing the keys with the same namespace as a pre-requisite step
and then pass in the name of the Secret using configuration blob
when creating the add-on. We recommend that add-on providers name
the schema properties so that customers do not accidentally mistake
it for the actual key. For example: appSecretName,
connectionSecretName etc.

In summary, add-on providers can leverage the schema to allow
customers to pass in the name of the secret but not the keys which
will actually hold the secret itself.

**Example configuration values**

You can include configuration examples in your schema to help
customers with configuration of add-ons. The following example is
from the schema of AWS Distro for OpenTelemetry add-on.

```
"examples": [
      {
        "admissionWebhooks": {
          "namespaceSelector": {},
          "objectSelector": {}
        },
        "affinity": {},
        "collector": {
          "amp": {
            "enabled": true,
            "remoteWriteEndpoint": "https://aps-workspaces.us-west-2.amazonaws.com/workspaces/ws-xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/api/v1/remote_write"
          },
          "cloudwatch": {
            "enabled": true
          },
          "mode": "deployment",
          "replicas": 1,
          "resources": {
            "limits": {
              "cpu": "256m",
              "memory": "512Mi"
            },
            "requests": {
              "cpu": "64m",
              "memory": "128Mi"
            }
          },
          "serviceAccount": {
            "annotations": {},
            "create": true,
            "name": "adot-collector"
          },
          "xray": {
            "enabled": true
          }
        },
        "kubeRBACProxy": {
          "enabled": true,
          "resources": {
            "limits": {
              "cpu": "500m",
              "memory": "128Mi"
            },
            "requests": {
              "cpu": "5m",
              "memory": "64Mi"
            }
          }
        },
        "manager": {
          "env": {},
          "resources": {
            "limits": {
              "cpu": "100m",
              "memory": "128Mi"
            },
            "requests": {
              "cpu": "100m",
              "memory": "64Mi"
            }
          }
        },
        "nodeSelector": {},
        "replicaCount": 1,
        "tolerations": []
      }
    ]
```

#### Common parameters that are allowed for

configuration

The following are recommended parameters in a customer facing Helm schema
file.

| Parameter                 | Description                                                                                                                                                                                                                                                                                | Should have a default?                    |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------- |
| additionalLabels          | Add Kubernetes labels to all Kubernetes objects managed by<br>the add-on.                                                                                                                                                                                                                  | No                                        |
| additionalAnnotations     | Add Kubernetes annotations to all Kubernetes objects managed<br>by the add-on.                                                                                                                                                                                                             | No                                        |
| podLabels                 | Add Kubernetes labels to pods managed by the add-on.                                                                                                                                                                                                                                       | No                                        |
| podAnnotations            | Add Kubernetes annotations to pods managed by the<br>add-on.                                                                                                                                                                                                                               | No                                        |
| logLevel                  | Log level for components managed by the add-on.                                                                                                                                                                                                                                            | Yes                                       |
| nodeSelector              | Simplest recommended form of node selection constraint. You<br>can add the nodeSelector field to your Pod specification and<br>specify the node labels you want the target node to<br>have.                                                                                                | Potentially, for example Linux nodes only |
| tolerations               | Tolerations are applied to pods. Tolerations allow the<br>scheduler to schedule pods with matching taints. Tolerations<br>allow scheduling but don't guarantee scheduling.                                                                                                                 | Maybe, more common with daemonsets        |
| affinity                  | The affinity feature consists of two types of affinity: Node<br>affinity functions like the nodeSelector field but is more<br>expressive and allows you to specify soft rules, Inter-pod<br>affinity/anti-affinity allows you to constrain Pods against<br>labels on other Pods.           | Maybe                                     |
| topologySpreadConstraints | You can use topology spread constraints to control how Pods<br>are spread across your cluster among failure-domains such as<br>regions, zones, nodes, and other user-defined topology domains.<br>This can help to achieve high availability as well as efficient<br>resource utilization. | Maybe                                     |
| resource request/limits   | Specify how much cpu/memory each container needs. Requests<br>are strongly recommended to be set. Limits are optional.                                                                                                                                                                     | Yes                                       |
| replicas                  | Number of replicas of the pods managed by the add-on. Not<br>applicable for daemonsets.                                                                                                                                                                                                    | Yes                                       |

###### Note

For workload scheduling configuration parameters, you may need to separate
out top level components in the Schema where necessary. Example, Amazon EBS CSI
driver contains two main components, controller and node agent - customers
require different node selectors/tolerations for each component.

###### Note

The default values defined in the JSON schema is purely for user
documentation purpose only and does not replace the need to have the
rightful default in the `values.yaml` file. If using the default
property, please ensure that the default in `values.yaml` matches
that in the schema and the two artifacts (`values.schema.json`
and `values.yaml`) remain in sync whenever changes are made to
the Helm Chart.

```
"affinity": {
            "default": {
              "affinity": {
                "nodeAffinity": {
                  "preferredDuringSchedulingIgnoredDuringExecution": [
                    {
                      "preference": {
                        "matchExpressions": [
                          {
                            "key": "eks.amazonaws.com/compute-type",
                            "operator": "NotIn",
                            "values": [
                              "fargate"
                            ]
                          }
                        ]
                      },
                      "weight": 1
                    }
                  ]
                },
                "podAntiAffinity": {
                  "preferredDuringSchedulingIgnoredDuringExecution": [
                    {
                      "podAffinityTerm": {
                        "labelSelector": {
                          "matchExpressions": [
                            {
                              "key": "app",
                              "operator": "In",
                              "values": [
                                "ebs-csi-controller"
                              ]
                            }
                          ]
                        },
                        "topologyKey": "kubernetes.io/hostname"
                      },
                      "weight": 100
                    }
                  ]
                }
              }
            },
            "description": "Affinity of the controller pod",
            "type": [
              "object",
              "null"
            ]
          }
```

### Common parameters that aren't allowed for

configuration

Cluster metadata parameters such `clusterName`, `region`,
`vpcId`, `accountId`, and others may be required by
various add-ons (for example, ELB Controller). Any parameter similar to these that
is known by the Amazon EKS service will be automatically injected by Amazon EKS add-ons, and
not put on the responsibility of the user to specify as a configuration option.
These parameters include:

- AWS region
- Amazon EKS cluster name
- VPC ID of the cluster
- Container registry, specifically for build-prod accounts, which is used by
  networking add-ons
- DNS cluster IP, specifically for coredns add-on
- Amazon EKS cluster API endpoint
- IPv4 enabled on cluster
- IPv6 enabled on cluster
- Prefix delegation for IPv6 enabled on cluster

Add-on providers need to ensure you have templating defined for such applicable
parameters. Each of the above parameters will have a pre-defined
`parameterType` attribute defined by Amazon EKS. The release metadata will
specify the mapping between the `parameterType` and the name/path of the
parameter in the template. This way, the values can be dynamically passed-in by
Amazon EKS without requiring customers to specify these through configurations and also
gives flexibility to add-on providers to define their own template name/path.
Parameters such as the above that Amazon EKS needs to inject dynamically should be
excluded from the schema file.

**Example mapping from release metadata**

```
"defaultConfiguration": [
       {
            "key": "image.containerRegistry",
            "parameterType": "CONTAINER_REGISTRY"
       }
]
```

The following are parameters not recommended to be configurable in a customer
facing Helm schema file. Either the parameters should have non-modifiable defaults,
or not be included at all in the add-on template.

| Parameter                      | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Should have a default?                                                                                                                                                                                                      |
| ------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| image                          | Container image that will be deployed on the Kubernetes<br>cluster.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | No, managed through add-on definition                                                                                                                                                                                       |
| imagePullSecrets               | Configuring a pod to use a secret to pull from a private<br>registry.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | N/A                                                                                                                                                                                                                         |
| livenessProbe                  | The Kubelet process uses liveness probes to know when to restart<br>a container. For example, liveness probes could catch a deadlock,<br>where an application is running, but unable to make progress.<br>Restarting a container in such a state can help to make the<br>application more available despite bugs.                                                                                                                                                                                                                                           | Yes                                                                                                                                                                                                                         |
| readinessProbe                 | It is important that you have a readiness probe for your<br>containers. This way the Kubelet process running on your data plane<br>will know when the container is ready to serve traffic. A Pod is<br>considered ready when all of its containers are ready. One use of<br>this signal is to control which Pods are used as backends for<br>Services. When a Pod is not ready, it is removed from Service load<br>balancers.                                                                                                                               | Yes                                                                                                                                                                                                                         |
| startupProbe                   | The kubelet uses startup probes to know when a container<br>application has started. If such a probe is configured, it disables<br>liveness and readiness checks until it succeeds, making sure those<br>probes don't interfere with the application startup. This can be<br>used to adopt liveness checks on slow starting containers, avoiding<br>them getting killed by the kubelet before they are up and<br>running.                                                                                                                                   | Optional                                                                                                                                                                                                                    |
| podDisruptionBudget            | Define a Pod Discruption Budget (PDB) to ensure a minimum number<br>of PODS keep running during voluntary disruptions. A PDB limits the<br>number of Pods of a replicated application that are down<br>simultaneously from voluntary disruptions. For example, a<br>quorum-based application would like to ensure that the number of<br>replicas running is never brought below the number needed for a<br>quorum. A web front end might want to ensure that the number of<br>replicas serving load never falls below a certain percentage of the<br>total. | Yes, if defaulting to more than two replicas                                                                                                                                                                                |
| serviceAccount (name)          | Name of the service account pods will run under.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | Yes                                                                                                                                                                                                                         |
| serviceAccount (annotations)   | Annotations applied to the service account. Typically used for<br>IAM Roles for Service Accounts feature                                                                                                                                                                                                                                                                                                                                                                                                                                                    | No, IAM service account role ARN is set in top level Amazon EKS<br>add-ons API. An exception to this rule is if your add-on has<br>multiple deployments/controllers (such as Flux) and requires<br>separate IRSA role ARNs. |
| priorityClassName              | Priority indicates the importance of a Pod relative to other<br>Pods. If a Pod cannot be scheduled, the scheduler tries to preempt<br>(evict) lower priority Pods to make scheduling of the pending Pod<br>possible.                                                                                                                                                                                                                                                                                                                                        | Yes. Most add-ons are critical to cluster functionality, and<br>should have a priority class set by default.                                                                                                                |
| podSecurityContext             | A security context defines privilege and access control settings<br>for a Pod or Container. Typically used to set fsGroup<br>• which was<br>required for IRSA in v1.19 and lower clusters.                                                                                                                                                                                                                                                                                                                                                                  | Unlikely, given Amazon EKS no longer supports Kubernetes v1.19                                                                                                                                                              |
| securityContext                | A security context defines privilege and access control settings<br>for a Pod or Container.                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Yes                                                                                                                                                                                                                         |
| updateStrategy                 | Specifies the strategy used to replace old Pods by new<br>ones.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Yes                                                                                                                                                                                                                         |
| nameOverride                   | Override name of pods.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | No                                                                                                                                                                                                                          |
| podSecurityPolicy              | Enforce restrictions on parameters.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | No<br>• PSPs are deprecated                                                                                                                                                                                                 |
| extraVolumeMounts/extraVolumes | Used for IRSA in non Amazon EKS clusters.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | No                                                                                                                                                                                                                          |
