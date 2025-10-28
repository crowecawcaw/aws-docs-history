# Changing the instance type or size outside of the Auto Scaling group

AWS recommends that you keep your infrastructure immutable. If you need to change
instance sizes, you can either:

- Scale horizontally and add additional instances. Then, place additional tasks on
  those instances, or you
- Scale vertically by launching a new, larger/smaller instance and then drain the
  old instance.
  Both of these approaches will help minimize application availability impact.

If you used another method to change the instance, you might receive the following error:

```
Container instance type changes are not supported.
```

When you get this error, perform the following steps:

1. Launch new instances with the desired instance type.
2. Drain your old instance types. For more information, see [Draining Amazon ECS container instances](container-instance-draining.md "container-instance-draining.md").
