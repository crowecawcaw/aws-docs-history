

# Multi-AZ cells
<a name="multi-az-cells"></a>

 A way to reduce the scope of impact of a service is to introduce Multi-AZ cells. In this approach, cells are Multi-AZ or Regional, and can take advantage of all the resiliency and availability of Regional and Multi-AZ services already offered by AWS, thus abstracting the great complexity that this management requires. Each replica of your workload (cell) will continue to running even if an AZ is unavailable for the subset of clients or traffic you have defined. 

![Diagram showing the use of Multi-AZ cells.](http://docs.aws.amazon.com/wellarchitected/latest/reducing-scope-of-impact-with-cell-based-architecture/images/multi-az-cells.png)


 Advantages of this approach: 
+  Wider use of serverless services that already are Regional.
+  It is easier to a cell be self-resilience using serverless or managed services with a Multi-AZ strategy, without share state with external components. 

 Disadvantages of this approach: 
+  Less control over an AZ failure, particularly gray failures, where some components or services are unstable. In this case, evacuate one isolation zone, where that zone can be an AZ or a Region may not solve the problem. 