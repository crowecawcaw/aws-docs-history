# FSIOPS2: Have you completed an operational risk assessment?

Financial services workloads should be continually reviewed and prioritized with regard to their risk impact to the overall business (for example, based on their reputational, financial, or regulatory impact).

## FSIOPS02-BP01 Understand the Shared Responsibility Model and how it applies to

services and workloads you run in the cloud

In connection with your use of the cloud, you must understand how the [AWS Shared
Responsibility Model](https://aws.amazon.com/compliance/shared-responsibility-model/ "https://aws.amazon.com/compliance/shared-responsibility-model/") affects your control environment. For example, certain
controls may be the responsibility of AWS, but certain controls remain the
responsibility of the financial services institution. Review the AWS Shared
Responsibility Model and map AWS responsibilities and customer responsibilities
according to each AWS service you use and your control environment. For those controls
that are the responsibility of AWS, you can use [AWS Artifact](https://aws.amazon.com/artifact/ "https://aws.amazon.com/artifact/") to access audit reports and review the
implementation and operating effectiveness of AWS security controls.

### Prescriptive guidance

Review and understand the [AWS Shared Responsibility
Model](https://aws.amazon.com/compliance/shared-responsibility-model/ "https://aws.amazon.com/compliance/shared-responsibility-model/"), and the different demarcation points that apply to AWS
infrastructure services (such as EC2), container services (such as RDS), and
abstracted services (such as S3). If your organization has central functions (like a
Cloud Center of Excellence or governance team), publish a shared responsibility model
for your organization, which clearly defines the roles of AWS, the central team, and
distributed teams.

## FSIOPS02-BP02 Develop an enterprise cloud risk plan

Map the interactions between business consumers of cloud services and the internal
stakeholders that shape this consumption, including risk and control considerations.
Integrate across the three lines of defense functions, and provide necessary resources
and training to satisfy their mandates for operating and protecting your business in the
cloud while you strive to achieve your strategic goals.

This integration can be achieved by carrying out a risk-based assessment of your
operating model, and is especially effective when complemented with a review of
decision-making processes and authority to determine if they are cloud-appropriate. As
requirements are translated into controls, pay attention to the strength of the controls
to mitigate the identified risks. Another key risk factor includes the ability to
control design and performance to facilitate independent assessment by internal risk
management and audit functions. Focus on control design helps you incorporate key
control requirements into the design from the start.

### Prescriptive guidance

Evaluate existing risk models in use, and related policies, for relevance in a
cloud environment. Many risk models are focused on on-premises architectures and do
not account for advantages of cloud-based workloads. Reach out to your AWS account
team to leverage AWS expertise in risk and compliance.
