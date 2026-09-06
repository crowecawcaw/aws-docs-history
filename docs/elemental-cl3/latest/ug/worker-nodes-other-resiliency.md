

# Resiliency features in Elemental Statmux
<a name="worker-nodes-other-resiliency"></a>

Elemental Statmux includes two features that provide resiliency for Elemental Statmux – output listening and output redundancy.

**Topics**
+ [Output listening in Elemental Statmux](#es-resiliency-opl)
+ [Output redundancy in Elemental Statmux](#es-resiliency-opr)
+ [Output listening combined with output redundancy](#es-resiliency-opl-opr)

## Output listening in Elemental Statmux
<a name="es-resiliency-opl"></a>

If your MPTS is on a node that is in a 1:1 (or 1:1 Plus) redundancy group, you can set up the MPTS for output listening. 

Output listening works only with multicast delivery to the system that is downstream of Elemental Statmux. It protects against the following problems:
+ Muxing problems within the MPTS.
+ Failure on an Elemental Statmux node.

**Setup**

You set up for output listening by checking the **Output Listening** field when you create the MPTS. See [Output tab](step-create-mpts-tab-output.md). 

Conductor Live replicates the MPTS on the two nodes in the redundancy group. The two MPTSes adopt roles. One MPTS is the primary MPTS, the other is the secondary MPTS. When you start the MPTS, Conductor Live automatically starts it on both nodes. Both MPTSes mux the output, but only the primary MPTS delivers the output to the destination. The secondary MPTS continually listens on the multicast destination, to monitor the health of the other MPTS.

The following diagram illustrates the setup. 

![Two Statmux nodes with MPTS1 and MPTS2, where MPTS1 Output-1 connects to a destination.](http://docs.aws.amazon.com/elemental-cl3/latest/ug/images/Sm_resil_OPL_1-1.png)


**What happens in a failure**

A failure might occur on the primary MPTS, either because there is a problem in the muxer, or because the node fails.

In either case, the secondary MPTS detects that the first MPTS is not delivering, and it automatically starts to deliver to the same destination. The secondary MPTS is already muxing, so there is minimal disruption in delivery.

## Output redundancy in Elemental Statmux
<a name="es-resiliency-opr"></a>

You can set up the MPTS with two destinations. Elemental Statmux delivers the MPTS to two different addresses. 

Output redundancy works on any type of redundancy setup. The node can be in any type of redundancy group, or it can be outside a redundancy group.

Output redundancy protects against the following:
+ Failure of the output interface on Elemental Statmux.
+ Failure in the network path to the downstream system.

This resiliency feature works with either unicast or multicast delivery to the system that is downstream of Elemental Statmux. 



**Output redundancy with N-to-M redundancy**

With this redundancy setup, you set up for output redundancy by specifying two destinations when you create the MPTS output. The two addresses can be identical or different. Usually the interfaces are different (as shown in the diagram), to protect again switch failure in the node. The downstream system must be able to handle the type of delivery. 

The MPTS continually delivers two outputs. If a failure occurs, the downstream system must be set up to detect problems and react appropriately.

The following diagram illustrates the setup. One MPTS has two destinations to the downstream system.

![Statmux node MPTS1 with two outputs connecting to downstream destinations.](http://docs.aws.amazon.com/elemental-cl3/latest/ug/images/sm_resil_opr_none.png)


**Output redundancy with 1-to-1 redundancy or 1-to-1 Plus redundancy**

With this redundancy setup, you set up for output redundancy by specifying two destinations when you create the MPTS output. The two addresses can be identical or different. Usually the interfaces are different (as shown in the diagram), to protect again switch failure in the node. The downstream system must be able to handle the type of delivery. 

The MPTS continually delivers two outputs from each node in the redundancy group. If a failure occurs, the downstream system must be set up to detect problems and react appropriately.

The following diagram illustrates the setup where there is 1-to-1 redundancy or 1-to-1 Plus redundancy.

![Two Statmux nodes MPTS1 and MPTS2 with outputs connecting to multiplexers in redundant setup.](http://docs.aws.amazon.com/elemental-cl3/latest/ug/images/sm_resil_opr_1-1.png)


## Output listening combined with output redundancy
<a name="es-resiliency-opl-opr"></a>

If your MPTS is on a node that is in a 1:1 (or 1:1 Plus) redundancy group, you can combine output listening and output redundancy for an MPTS. 

With this setup, you have two outputs from each node. The secondary MPTS continually listens on the two multicast destinations, to monitor the health of the other MPTS. Compare the diagram below to the diagram for output redundancy with 1-to-1 redundancy. There is a slight difference in the role of the secondary MPTS at each downstream destination.

This setup combines all the failure protection of output listening and output redundancy. 

![Two Statmux nodes with MPTS outputs connecting to destinations with listening configurations.](http://docs.aws.amazon.com/elemental-cl3/latest/ug/images/Sm_resil_opr_OPL_1-1.png)
