# Application Note for LPWA Cellular Networks

Applications should not be considered immediately portable
between LPWA technology types and the higher bandwidth
technology types. Applications leveraging LTE-M or Narrowband
IoT should have advanced error processing to accommodate for
slow throughput and high retransmission rates. The application
should also use advanced methods for reduction of the size of
packets sent. This includes reducing the size of TLS
handshakes using pre-shared keys as well as using CBOR or some
other application layer mechanism to reduce the data payload
size. Developers should make the application aware of when the
device enters into coverage enhancement modes. Coverage
enhancement modes can greatly reduce the data throughput rate
and greatly increase various errors within the TLS stack, IP
stack, and the application due to timeouts or retransmissions. In order to maintain an LPWA device and improve its
longevity, developers should take note of the elements called
out in this section in order to reduce the overall time the
radio is on and sending or receiving data.
