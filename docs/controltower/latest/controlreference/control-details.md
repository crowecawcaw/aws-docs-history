

# View control details
<a name="control-details"></a>

You can view control details in the AWS Control Tower console or retrieve them programmatically using [Control Catalog APIs](https://docs.aws.amazon.com/controlcatalog/latest/APIReference/Welcome.html).

## Access control metadata in the console
<a name="access-control-metadata-console"></a>

To view details about an individual control in the AWS Control Tower console, select the name of the control from the table on the **Controls** page. On the console page for the control, you may see metadata items such as **Categories**: Common controls, Frameworks, Services, and Groups. Select each item to get more information about the control. You can find additional information in the tabs: **About**, **OUs enabled**, and **Accounts**.

For each control, the global **API controlIdentifier** is available in the console, along with the framework and objective.

In each **Control details** page of the console, you can find the following details for each control:
+ **Name** – The name of the control.
+ **Common control (formerly, Control objective)** – The pre-defined objective that an implemented control helps you enforce. See [Control catalog: control objectives](control-catalog-objectives.md) and [About common controls](https://docs.aws.amazon.com/controltower/latest/controlreference/common-controls-list.html).
+ **Service** – The AWS service to which this control applies.
+ **Control owner** – The AWS service that owns and maintains this control.
+ **Behavior** – A control's behavior is set to preventive, detective, or proactive.
+ **Implementation** – The underlying implementation method for this control, such as SCP, AWS Config managed rule, or CloudFormation hook.
+ **GovernedResources** – The AWS resources that are monitored or affected by this control. This field can show an AWS service name, or an CloudFormation ARN. It can be blank if there's no CloudFormation ARN to represent the resource, or if the control governs resources across several AWS services (for example, the Region Deny control).
+ **Framework** – The industry-standard compliance framework that this control helps to enforce, for example, **NIST 800-53 Rev 5**.
+ **Control ID (Alias)** – A unique identifier assigned to each control. This identifier is part of a classification system for the controls.
+ **API controlIdentifier** – This identifier is needed when calling the AWS Control Tower APIs.
+ **Group** – A label for a group of controls with similar purpose, such as helping you create Digital Sovereignty.
+ **Guidance** – The guidance is either mandatory, strongly recommended, or elective.
+ **Severity** – The relative risk associated with any violation of this control.
+ **Release date** –The date the control became available.
+ **Deployable Regions** – Regions in which the control is available to be deployed.

**Note**  
 The control **State** and status information is available in the console only. It is not available from the [public API](https://docs.aws.amazon.com/controltower/latest/APIReference/API_Operations.html). To view the status of a control, navigate to the **Control details** page in the AWS Control Tower console.

**Open the tabs**
+ In the **About** tab, you can view the relationship of the control with other controls. We provide recommendations about how certain controls can work together with other controls to provide best security for your AWS environment.
+ The **OUs enabled** tab shows a list of OUs on which the control is actively enabled.

The status of the Region deny control is shown as a separate entry.

Other information may appear on the **Control details** page, including these items:
+ **Description** – A brief description of the control and its function.
+  **Remediation message** – Suggestions for what to change if your CloudFormation hook control returns a FAIL status.
+ **Remediation samples ** – Examples showing configurations that can return a PASS or FAIL result for your CloudFormation hook control.
+ **Usage considerations** – Additional information about how to apply this control or about the resources it can affect.
+ The **Gherkin** artifact – The Gherkin is a readable specification for the CloudFormation hook controls, showing requirements for tests that cause PASS, FAIL, or SKIP results to be returned.

**To view a control artifact**

Each control is implemented by one or more artifacts. These artifacts can include a baseline CloudFormation template, a service control policy (SCP) to prevent account-level configuration changes or activity that may create configuration drift, and AWS Config Rules to detect account-level policy violations.

To view a control's artifact, select the **Artifact** tab to view the **Service control policy (SCP)**, **AWS Config rule**, or **CloudFormation policy template** on the **Control details** page.

**Note**  
The four mandatory controls with `"Sid": "GRCLOUDTRAILENABLED"` are identical by design. The sample code is correct.

## Access control metadata programmatically
<a name="access-control-metadata-programmatically"></a>

Control metadata is available through Control Catalog APIs. For information about control identifiers, see [Resource identifiers for APIs and controls](control-identifiers.md).

To list all controls, use the [ListControls API](https://docs.aws.amazon.com/controlcatalog/latest/APIReference/API_ListControls.html). For example:

```
aws controlcatalog list-controls --max-result 2 --region us-east-1
```

To retrieve detailed metadata for a specific control, use the [GetControl API](https://docs.aws.amazon.com/controlcatalog/latest/APIReference/API_GetControl.html). For example:

```
aws controlcatalog get-control --control-arn arn:aws:controlcatalog:::control/4b0nsxnd47747up54ytdqesxi --region us-east-1
```

For more information, see the [Control Catalog API Reference](https://docs.aws.amazon.com/controlcatalog/latest/APIReference/Welcome.html).