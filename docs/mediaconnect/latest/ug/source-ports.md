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

| Protocol        | Ports needed             | Ports required                                                                                                                                                                                                                                                                                                               |
| --------------- | ------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| CDI             | Port                     | The port that you specify. This is the only port needed for the<br>source.                                                                                                                                                                                                                                                   |
| RIST            | Port and port+1          | The port that you specify, plus one additional port. MediaConnect<br>automatically reserves a port that is +1 from the port that you<br>specified.<br>For example, if you specify port 3000 for this output, the service<br>also reserves port 3001.                                                                         |
| RTP             | Port                     | The port that you specify. This is the only port needed for the<br>output.                                                                                                                                                                                                                                                   |
| RTP-FEC         | Port, port+2, and port+4 | The port that you specify, plus two additional ports. MediaConnect<br>automatically reserves ports that are +2 and +4 from the port that<br>you specified.<br>For example, if you specify port 2000 for this output, the service<br>also reserves ports 2002 and 2004 for error correction.                                  |
| SRT listener    | Port                     | The port that you specify. This is the only port needed for the<br>source.                                                                                                                                                                                                                                                   |
| SRT caller      | Port                     | The port that you specify. This is the only port needed for the<br>source.                                                                                                                                                                                                                                                   |
| ST 2110 JPEG XS | Port                     | The port that you specify. This is the only port needed for the<br>source.                                                                                                                                                                                                                                                   |
| Zixi push       | Port                     | **For standard sources**: MediaConnect<br>automatically uses port 2088.**For VPC<br>sources**: MediaConnect automatically assigns a port in the<br>range of 2090-2099 when the source is created. The 2090-2099 port<br>range is reserved exclusively for Zixi VPC sources and cannot be<br>used by another source protocol. |
| NDI**®**        | Port                     | The ports that you specify for each media stream. If you don't<br>specify a custom port, MediaConnect uses the default NDI discovery protocol<br>(TCP-5959) to announce NDI sources on your network.                                                                                                                         |
