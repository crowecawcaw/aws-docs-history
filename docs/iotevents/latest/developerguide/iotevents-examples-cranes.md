End of support notice: On May 20, 2026, AWS will end support for
AWS IoT Events. After May 20, 2026, you will no longer be able to access the AWS IoT Events console or AWS IoT Events
resources. For more information, see [AWS IoT Events end of
support](iotevents-end-of-support.md "iotevents-end-of-support.md").

# Example: A crane detecting conditions using AWS IoT Events

An operator of many cranes wants to detect when the machines need maintenance or
replacement and trigger appropriate notifications. Each crane has a motor. A motor emits
messages (inputs) with information about pressure and temperature. The operator wants two
levels of event detectors:

- A crane-level event detector
- A motor-level event detector
  Using messages from the motors (that contain metadata with both the `craneId`
  and the `motorid`), the operator can execute both levels of event detectors using
  appropriate routing. When event conditions are met, notifications should be sent to
  appropriate Amazon SNS topics. The operator can configure the detector models so that duplicate
  notifications are not raised.

This example demonstrates the following functional capabilities:

- Create, Read, Update, Delete (CRUD) of inputs.
- Create, Read, Update, Delete (CRUD) of event detector models and different versions of
  event detectors.
- Routing one input to multiple event detectors.
- Ingestion of inputs into a detector model.
- Evaluation of trigger conditions and lifecycle events.
- Ability to refer to state variables in conditions and set their values depending on
  conditions.
- Runtime orchestration with definition, state, trigger evaluator, and actions
  executor.
- Execution of actions in `ActionsExecutor` with an SNS target.
