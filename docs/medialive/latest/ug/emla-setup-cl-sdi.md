# Create SDI sources

If some of the nodes in a cluster include SDI cards and ports, you must create SDI
sources and SDI mappings:

- SDI sources: MediaLive Anywhere supports single-link and quad-link SDI interfaces, assuming that
  you have nodes that have the corresponding cards. For quad-link sources, MediaLive Anywhere supports
  quadrant or interleave mode.
- SDI mappings: Create an SDI mapping for each port on the SDI cards. The mappings let
  you configure MediaLive Anywhere to connect an SDI source to the physical SDI card and port that is
  the connection point for that source.

## Plan for SDI inputs

1. Identify your SDI sources and give each one a name that is unique in the AWS
   account. We recommend you assign a name that describes the source, for example
   `curling-cameraA`.
2. Identify the type of each source (single-link or quad-link) and the mode for any
   quad-link source (interleave or quadrant).
3. Plan how your SDI sources will be connected to the node. Specifically, identify
   any source that is quad-link and assign four contiguous ports for that source.
4. Identify the card number and port (or ports) for each SDI source. For information
   about how physical cards and ports are identified on your node hardware, see the
   documentation for your node hardware.

You will end up with a mapping for each SDI source. Each mapping consists of the
source name, a card number, and a port number.

## Create an SDI source

You must set up each SDI source that you plan to use in MediaLive Anywhere. You will reference
this source when you create an SDI input in MediaLive.

1. In the navigation bar, choose MediaLive Anywhere, then choose **SDI
   sources**. On the **SDI sources** page, choose
   **Create SDI source**.
2. Complete the fields to provide a name, the interface, and the mode (for quad-link
   only).
3. Choose **Create**.

## Create SDI mappings

Create SDI mappings on each node that has SDI cables connected. You perform this task
by editing the existing node.

1. In the MediaLive navigation bar, choose **Nodes**.
2. Select the node and choose **Edit**. On the
   **Edit** page. In the **SDI source mappings**
   field, choose **Add mapping**.
3. Complete the three fields to map a source to the SDI card and port (channel
   number).
