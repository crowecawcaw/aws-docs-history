# Definitions

This section provides key terminology used throughout this lens, focusing specifically on
modern industrial data concepts and manufacturing-specific definitions. These definitions
complement the standard AWS Well-Architected Framework terminology.

- **Operational technology (OT)**: Systems and equipment used
  to monitor and control industrial processes on the shop floor, such as sensors, PLCs, and
  SCADA systems
- **Information technology (IT)**: Technologies used to
  manage business operations and data, including enterprise systems like ERP, MES, and cloud
  computing systems.
- **Programmable logic controller (PLC)**: An industrial
  computer used to control machinery and processes on the factory floor, running real-time
  logic based on sensor inputs.
- **Supervisory control and data acquisition (SCADA)**: A
  system that provides centralized monitoring and control of industrial equipment and
  processes, often across multiple sites.
- **Manufacturing execution system (MES)**: Software that
  manages and monitors production operations in real time, bridging the gap between the
  factory floor (OT) and business systems (IT).
- **Enterprise resource planning (ERP)**: A business
  management system that integrates core processes like finance, inventory, and procurement,
  often linking with MES for end-to-end visibility.
- **Message Queuing Telemetry Transport (MQTT)**: A
  lightweight messaging protocol used in manufacturing to transmit data from machines and
  sensors to monitoring systems in real time.
- **Advanced Message Queuing Protocol (AMQP)**: A protocol
  used to provide reliable communication between systems in manufacturing, often for
  integrating OT and IT layers.
- **Open Platform Communications Unified Architecture (OPC
  UA)**: A standard protocol for secure, system-independent communication between
  industrial equipment and software systems, enabling seamless data exchange across the
  manufacturing environment.
- **Reliability**: The ability of a workload to perform its
  intended function correctly and consistently when it's expected to. This includes the
  ability to operate and test the workload through its total lifecycle.
- **Resilience**: The ability of a workload to recover from
  infrastructure or service disruptions, dynamically acquire computing resources to meet
  demand, and mitigate disruptions, such as misconfigurations or transient network issues.
- **Mean time to detection (MTTD)**: The average time
  required to detect a failure or anomaly in manufacturing systems after it occurs.
- **Mean time to resolution (MTTR)**: The average time taken
  to fully resolve an incident from the moment it is detected, including the time to restore
  normal manufacturing operations.
- **Recovery Time Objective (RTO)**: The maximum acceptable
  time to restore a manufacturing process or system after a disruption.
- **Recovery Point Objective (RPO)**: The maximum acceptable
  period of data loss measured in time. For manufacturing systems, this defines how much
  operational data loss can be tolerated in a recovery scenario.
- **Data mesh producer**: Any entity which offers a data
  product through the data mesh.
- **Data mesh consumer**: Any entity who subscribes to a data
  product in the data mesh.
- **Data product**: Today, a data product is scoped to be
  only an AWS Lake Formation table or database. In the future, this definition may expand.
- **Digital thread**: A framework that connects data flows
  and provides an integrated view of an asset throughout the manufacturing lifecycle, from
  design through production and in-service operation.
- **Manufacturing data lake**: A centralized repository that
  allows storing structured and unstructured manufacturing data at scale
- **Industrial data catalog**: A metadata management solution
  that helps manufacturing organizations find, organize and access their industrial data
  assets
