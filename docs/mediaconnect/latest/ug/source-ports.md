# Source ports on MediaConnect flows

Each source on a flow must use a different port (for exceptions to this, see the
note). Some protocols require additional ports for error correction. For sources that
use these protocols, AWS Elemental MediaConnect automatically reserves the additional ports that
are needed. All MediaConnect protocols use UDP ports. The following table lists which
additional ports, if any, the service reserves.

###### Important

There is an exception to the port requirements for sources that use the Zixi
protocol. For standard Zixi sources, all sources use port 2088. For VPC Zixi
sources, the sources will use an inbound port range of 2090-2099. The 2090-2099 port
range is reserved exclusively for Zixi VPC sources and cannot be used by another
source protocol. The VPC Zixi source port is assigned by MediaConnect when the source is
created.

| Protocol        | Ports needed             | Ports required                                                                                                                                                                                                                                                                                                |
| --------------- | ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| CDI             | Port                     | The port that you specify. This is the only port needed for the source.                                                                                                                                                                                                                                       |
| RIST            | Port and port+1          | The port that you specify, plus one additional port. MediaConnect automatically reserves a port that is +1 from the port that you specified. For example, if you specify port 3000 for this output, the service also reserves port 3001.                                                                      |
| RTP             | Port                     | The port that you specify. This is the only port needed for the output.                                                                                                                                                                                                                                       |
| RTP-FEC         | Port, port+2, and port+4 | The port that you specify, plus two additional ports. MediaConnect automatically reserves ports that are +2 and +4 from the port that you specified. For example, if you specify port 2000 for this output, the service also reserves ports 2002 and 2004 for error correction.                               |
| SRT listener    | Port                     | The port that you specify. This is the only port needed for the source.                                                                                                                                                                                                                                       |
| SRT caller      | Port                     | The port that you specify. This is the only port needed for the source.                                                                                                                                                                                                                                       |
| ST 2110 JPEG XS | Port                     | The port that you specify. This is the only port needed for the source.                                                                                                                                                                                                                                       |
| Zixi push       | Port                     | **For standard sources**: MediaConnect automatically uses port 2088.**For VPC sources**: MediaConnect automatically assigns a port in the range of 2090-2099 when the source is created. The 2090-2099 port range is reserved exclusively for Zixi VPC sources and cannot be used by another source protocol. |
