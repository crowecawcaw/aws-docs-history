

# What happens at the end of your reservation
<a name="braket-end-of-reservation"></a>

After your reservation ends, you no longer have dedicated access to the device. Any remaining workloads that are queued with this reservation are automatically canceled.

**Note**  
Any job that was in `RUNNING` status when the reservation ends is canceled. We recommend using [checkpoints to save and restart](https://docs.aws.amazon.com/braket/latest/developerguide/braket-jobs-checkpoints.html) jobs at your convenience.

An ongoing reservation, such as after reservation start and before reservation end, can't be extended because each reservation represents standalone dedicated device access. For example, two back-to-back reservations are considered separate and any pending tasks from the first reservation are automatically canceled. They do not resume in the second reservation.

**Note**  
Reservations represent dedicated device access for your AWS account. Even if the device remains idle, no other customers can use it. Therefore, you are charged for the length of the reserved time, regardless of the utilized time.