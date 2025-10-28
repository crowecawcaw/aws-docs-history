# Use the default offset storage topic

By default, Amazon MSK Connect generates a new offset storage topic on your Kafka
cluster for each connector that you create. MSK constructs the default topic name
using parts of the connector ARN. For example,
`__amazon_msk_connect_offsets_my-mskc-connector_12345678-09e7-4abc-8be8-c657f7e4ff32-2`.
