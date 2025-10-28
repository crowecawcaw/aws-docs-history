# Design principles

There are several principles that can help strengthen the security
of EUC workload in addition to the overall Well-Architected
Framework security design principles:

- **Implement lifecycle management for AWS
  End User Computing instances and applications delivered by End
  User Computing services:** End to end lifecycle
  management should be adopted for the software used to deliver
  applications to your end users. Lifecycle management includes
  considering the operating system, middleware, runtime
  environments and patches associated with this software to make
  sure that components are patched and updated to the most
  recent release. It also includes the ongoing management of
  user identities used to access End User Computing services to
  make sure that accounts are regularly validated and where
  used, that certificates are validated and renewed.
- **Design EUC solutions that respect data
  classification and restrict access to data:** EUC
  solutions should respect the classification of data and
  restrict the ability for users to access data with
  classifications that they are not entitled to access.
- **Design for continuous monitoring of
  end user sessions:** Implement continuous monitoring
  of user sessions to determine the user experience that users
  are receiving while using AWS End User Computing services.
  Make sure that key operating system performance metrics
  covering processor, memory, disk and network are monitored.
  Review the performance of user sessions on a regular basis to
  determine if any anomalous metric data is being generated due
  to systems being compromised.
- **Limit access to AWS EUC services to
  approved and adherent devices:** Access from unknown
  or unsupported device systems should be restricted to the
  absolute minimum to allow users to connect to and use the
  service with the required level of functionality for their
  role. Adherent device access should be used, when possible,
  where devices are assessed for compliance against a set of
  criteria before being allowed to access the requested service.
