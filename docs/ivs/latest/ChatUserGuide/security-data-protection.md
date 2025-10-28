# IVS Chat Data Protection

For data sent to Amazon Interactive Video Service (IVS) Chat, the following data
protections are in place:

- Amazon IVS Chat traffic uses WSS to keep data secure in transit.
- Amazon IVS Chat tokens are encrypted using KMS customer-managed keys.
  Amazon IVS Chat does not require that you supply any customer (end user) data.
  There are no fields in chat rooms, inputs, or input security groups where there is an
  expectation that you will provide customer (end user) data.

Do not put sensitive identifying information such as your customer (end user) account
numbers into free-form fields such as a Name field. This includes when you work with the
Amazon IVS console or API, AWS CLI, or AWS SDKs. Any piece of data that you enter
into Amazon IVS Chat might be included in diagnostic logs.

Streams are not end-to-end encrypted; a stream may be transmitted unencrypted
internally in the IVS network, for processing.
