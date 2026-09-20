

# Setting up a UDP/TS output group
<a name="opl-setup-udp"></a>

This section shows how to set up a UDP/TS output group to implement Elemental Live output locking. 

1. Go to the **UDP/TS Output Group **section of the event. Set the fields as follows.
   + **Custom Group Name**: Enter the same name across all events in the pool. 
   + Set other fields to suit your workflow.

1. Go to each output. In the **Transport Stream Settings** section, set the fields as specified in the following table. 


<table>
<thead>
  <tr><th>Field name</th><th>Instruction</th></tr>
</thead>
<tbody>
  <tr><td><b>Segmentation Markers</b></td><td>Output lock requires that a UDP/TS output have segmentation markers.<br />Always choose <b>EBP Cablelabs</b>. Other options aren't valid for output locking. This option adds Encoder Boundary Point information to the adaptation field in conformance with OpenCable specification OC-SP-EBP-I01-130118.</td></tr>
  <tr><td><b>Segmentation Time</b></td><td>Required.<br />This field ensures that all of the outputs in the pool synchronize continually, not just when the events first start.</td></tr>
  <tr><td><b>Fragment Time</b></td><td>Required.</td></tr>
</tbody>
</table>


1. Set other fields in the outputs to suit your workflow.