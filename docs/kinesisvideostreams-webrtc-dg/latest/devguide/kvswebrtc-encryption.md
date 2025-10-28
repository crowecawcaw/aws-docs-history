# WebRTC encryption

End to end encryption is a mandatory feature of Amazon Kinesis Video Streams with WebRTC, and Kinesis Video Streams enforces
it on all the components, including signaling and media or data streaming. Regardless of whether
the communication is peer-to-peer or relayed via Kinesis Video Streams TURN end points, all WebRTC
communications are securely encrypted through standardized encryption protocols.

The signaling messages are exchanged using secure Websockets (WSS), data
streams are encrypted using Datagram Transport Layer Security (DTLS), and media streams are
encrypted using Secure Real-time Transport Protocol (SRTP).
