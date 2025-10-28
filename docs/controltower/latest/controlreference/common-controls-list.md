# About common controls

This page provides an overview and a partial list of the common controls available for the
Control Catalog. You can get a complete list of common controls by calling the [`ListCommonControls`](../../../controlcatalog/latest/APIReference/API_ListCommonControls.md "../../../controlcatalog/latest/APIReference/API_ListCommonControls.md") API.

###### Common controls in the ontology

- In the [_Control
  Catalog ontology_](../../../controlcatalog/latest/userguide/ontology-overview.md "../../../controlcatalog/latest/userguide/ontology-overview.md"), a _common control_
  conceptually expresses a single constraint or outcome that controls can help you to
  accomplish.
- In the hierarchy of the ontology, each common control has a single [_control objective_](control-catalog-objectives.md "control-catalog-objectives.md").
  A common control is more granular than a control objective, but the common control is not
  limited to any particular implementation. In fact, a common control can be implemented in
  several different ways, by individual controls, that you can view and enable.
  Hierarchically, a common control is the parent of certain individual controls that you see
  in the Control Catalog.

Because common controls are free of implementation, they do not have a defined
**Behavior** or **Guidance**. A common control may be
implemented by various preventive, detective, or proactive controls, or a combination of
these. Common controls cannot actually be enabled, only the implementations can be
enabled.

**Common controls and industry frameworks**

Each common control can be mapped to several industry frameworks, because that common
control can help you meet specific framework requirements. In the Control Catalog ontology,
an industry framework is represented by the term _Standard control_,
because the standard control represents a specific requirement of an industry standard.

###### Note

In the AWS Control Tower console, the field called **Frameworks** on the
**Control detail** page shows the frameworks that are related to
the control.

**View common controls**

You can view each common control on a page in the console, and see a list of specific
controls that implement the common control's functionality.

In the AWS Control Tower console, you can view the **Common control** field on the
**Control details** page of a control. Each implemented control has a
parent common control.

You can find the common control that is related to any specific control programmatically,
by calling the `GetControl` or `ListControls` API.

###### Examples of common controls

- Log aggregation
- Secure development environment
- Network topology design and review
- Asset retirement and disposition
- Data backup procedures
- Evidence preservation procedures and chain of custody
- Security metrics
- Guest and limited access wireless netwok management
- Asset labeling
- Security cameras
- Vendor incident management
- Data error checking and correction
- Secure encryption protocols
- Log protection and integrity
- Collaboration and communication
- External vulnerability scanning
- Patch testing and approval
- Access request and approval workflows
- Rollback and recovery procedures
- Security testing
