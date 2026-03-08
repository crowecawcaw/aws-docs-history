# Insurance verification integration

Real-time insurance eligibility (RTE) verification is an optional feature of the Appointment management agent. When enabled, the agent verifies a patient’s insurance eligibility and retrieves copay information prior to confirming an appointment. This feature is recommended for organizations that want to provide copay transparency before scheduling or rescheduling appointments.

###### Topics

- [Overview](#iv-overview "#iv-overview")
- [How it works](#iv-how-it-works "#iv-how-it-works")
- [Lambda input and output schema](#iv-lambda-schema "#iv-lambda-schema")
- [Lambda resource policy](#iv-resource-policy "#iv-resource-policy")
- [Setup steps](#iv-setup-steps "#iv-setup-steps")

## Overview

Customers are responsible for creating and maintaining their Lambda function. AWS provides sample Lambda code that customers must update with their vendor-specific API integration details and authentication logic. Customers must deploy the Lambda to their AWS account, configure it with vendor credentials (using AWS Secrets Manager recommended), and add a resource policy allowing health-agent.amazonaws.com service principal to invoke the function.

### When to use insurance verification

Use insurance verification integration when you want to:

- Provide copay transparency to patients before confirming appointments
- Integrate with your preferred RTE vendor (such as Experian Health or Waystar)

You don’t need RTE Lambda if:

- Post-booking insurance verification through Epic’s private APIs is sufficient for your workflow
- You prefer to handle insurance verification through existing staff processes

## How it works

### Setup phase

The customer deploys a Lambda function that connects to their preferred RTE vendor (for example, Experian Health or Waystar). The Lambda function is registered with Amazon Connect Health and granted invocation permissions.

### Runtime phase

When a patient schedules or reschedules an appointment, the Appointment management agent invokes the customer’s Lambda function with patient and appointment details. The Lambda function queries the RTE vendor and returns eligibility status and copay information to the agent, which presents the results to the patient before confirming the appointment.

## Lambda input and output schema

AWS provides sample Lambda code for patient insurance verification. You update the sample code with your vendor-specific integration details and deploy to your production account.

For the sample Lambda code, see [sample-healthcare-realtime-eligibility](https://github.com/aws-samples/sample-healthcare-realtime-eligibility "https://github.com/aws-samples/sample-healthcare-realtime-eligibility") on GitHub.

### Input schema

The Appointment management agent provides the following information to your Lambda function:

| Field                            | Description                                                |
| -------------------------------- | ---------------------------------------------------------- |
| CoverageDetails.identifier       | Payer code identifying the insurance company               |
| CoverageDetails.groupNumber      | Insurance group number                                     |
| CoverageDetails.insuranceName    | Free-text insurance name                                   |
| CoverageDetails.memberNumber     | Subscriber’s member ID                                     |
| subscriber.identifier            | System identifier for the subscriber (optional)            |
| subscriber.name                  | Subscriber name (optional)                                 |
| subscriber.dateOfBirth           | Subscriber date of birth (optional)                        |
| subscriber.relationshipToPatient | Relationship to the patient, for example "Self" (optional) |
| patientIdentifier                | Patient identifier                                         |
| requestPeriodStart               | Service date start                                         |
| requestPeriodEnd                 | Service date end                                           |
| providerNPI                      | Provider’s 10-digit NPI                                    |
| providerLastName                 | Provider last name (optional)                              |
| departmentNPI                    | Department NPI (optional)                                  |

### Output schema

Your Lambda function must return the following information to the Appointment management agent:

| Field             | Type              | Description                                    |
| ----------------- | ----------------- | ---------------------------------------------- |
| eligibilityStatus | String            | One of: `eligible`, `ineligible`, or `unknown` |
| copayAmount       | Number (optional) | Estimated copay in USD                         |
| coverageDetails   | String (optional) | Free-text summary of coverage                  |
| errorMessage      | String (optional) | Error description if verification failed       |

## Lambda resource policy

The customer must attach a resource-based policy to their Lambda function granting the Amazon Connect Health service principal invocation permissions. The policy must include:

- **Effect**: Allow
- **Principal Service**: `health-agent.amazonaws.com`
- **Action**: `lambda:InvokeFunction`
- **Resource**: Your Lambda function ARN
- **Condition**: `ArnLike` with `AWS:SourceArn` matching `arn:aws:healthcareai:<region>:<aws-account-id>:*`

See [Granting Lambda function access to AWS services](../../../lambda/latest/dg/permissions-function-services.md "../../../lambda/latest/dg/permissions-function-services.md") for reference.

For the complete policy template, see the sample Lambda code at https://github.com/aws-samples/sample-healthcare-realtime-eligibility.

## Setup steps

1. Download the sample Lambda code from https://github.com/aws-samples/sample-healthcare-realtime-eligibility.
2. Update the sample code with your RTE vendor’s API integration details and authentication logic.
3. Deploy the Lambda function to your AWS account.
4. Configure the Lambda function with vendor credentials using AWS Secrets Manager (recommended).
5. Attach the resource policy to grant Amazon Connect Health permission to invoke the function. For more information, see [Granting Lambda function access to AWS services](../../../lambda/latest/dg/permissions-function-services.md "../../../lambda/latest/dg/permissions-function-services.md") in the _AWS Lambda Developer Guide_.
6. In the Amazon Connect Health console, configure the Lambda function ARN in the domain settings under **Integration function**.
7. Test the integration in a non-production environment before enabling in production.
