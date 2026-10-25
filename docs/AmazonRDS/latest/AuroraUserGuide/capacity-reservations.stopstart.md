

# Stopping and starting a DB cluster in a reservation
<a name="capacity-reservations.stopstart"></a>

You stop and start Aurora DB instances at the DB cluster level. The `stop-db-cluster` and `start-db-cluster` commands don't take the `--db-capacity-reservation-identifier` or `--detach-from-db-capacity-reservation` parameter, so you can't attach a DB instance to a reservation, or detach it, when you stop or start a DB cluster.

When you stop a DB cluster, each DB instance that uses reserved capacity stays associated with its reservation, but the capacity it was using is released back to the reservation.

Because the association persists, starting the DB cluster returns each DB instance to the same reservation. Amazon RDS places it back into the reservation using whatever capacity is available at that point.

**Important**  
Because stopping the DB cluster releases the capacity, another DB instance can take it while the DB cluster is stopped.

The DB instances of a DB cluster can use different reservations. If any of those reservations has no available capacity in its DB instance's Availability Zone, the start fails with an error, and the DB cluster stays stopped. No DB instance in the DB cluster starts, even if the other reservations have capacity. Amazon RDS doesn't fall back to On-Demand capacity, so that each DB instance keeps its reservation. If a DB instance's reservation was canceled or has expired, that DB instance starts with On-Demand capacity and is no longer associated with the reservation.

If Aurora automatically starts a DB cluster after it has been stopped for 7 days, and the reservation has no available capacity, the automatic start is postponed until capacity is available.