

# What to do based on your score
<a name="capacity-manager-score-actions"></a>

What you do next depends on how your fleet is configured and whether a launch has already failed.
+ **If your fleet can draw from multiple types (mixed fleet)** — Read the aggregate. High means proceed — your orchestrator (Auto Scaling group, Karpenter, Amazon EC2 Fleet) distributes across instance type and Availability Zone combinations at launch time. Medium or Low means capacity is tight across everything you listed. Add more instance type and Availability Zone combinations or try again later.
+ **If you need one type (homogeneous fleet)** — Read the per-combination scores and pick the highest-scoring instance type and Availability Zone combination. If several tie, choose on cost, performance, or familiarity.
+ **If a launch already failed with an InsufficientCapacityError** — Call get-capacity-manager-supportability-scores for the same instance type, Availability Zone, and capacity amount. A High score means the combination has capacity but needs to resize hosts to produce instances at your requested size — launch what you can and continue to retry the remainder every few minutes. Medium or Low means the combination has limited available capacity for your request. Launch in another combination that scored High, or add more instance types.