# A warning for all mapping

approaches

Regardless of partition mapping approach, it's important to also use an override table
to force specific keys to specific cells (except for [full mapping](full-mapping.md "full-mapping.md"),
which natively provides
this support). This can be useful for testing, quarantining, and special-case routing for
particularly heavy partition keys.

Another consideration is that the task of mapping a new customer to a cell and
registering it in the cell router is the control plane's task. After this provisioning of
the client and the cell router loads this configuration, the strategy defined in this
section starts to work
