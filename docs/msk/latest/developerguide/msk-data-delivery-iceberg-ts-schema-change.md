# Delivery stops after a schema change

- **Symptom:** Delivery stops after the topic's schema changes in GSR.
- **Causes:** Schema evolution is not supported. A schema change can make new records incompatible with the existing Iceberg table.
- **Resolution:** Revert to the schema the Channel was created with, or delete the Channel and create a new one (with a new table) for the new schema. Check Amazon CloudWatch Logs for schema resolution errors.
