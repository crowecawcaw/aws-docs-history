NEW - You can now accelerate your migration and modernization with AWS Transform. Read [Getting Started](../../../transform/latest/userguide/getting-started.md "../../../transform/latest/userguide/getting-started.md") in the _AWS Transform User Guide_.

# Preparing for test and cutover instance launch

Prior to launching your instances, you must ensure that your environment is set up properly
to ensure successful launches. Check the following prior to continuing:

- Prepare your subnets for launch - Plan which subnets you will use to launch your test and
  cutover instances. You use these subnets in your EC2 launch template when you configure
  your Launch settings.
- Create security groups within the subnets - Create the Security groups you want to use
  within your prepared subnets. You set these Security groups in your EC2 Launch template
  when you configure launch settings.

###### Note

Customers that want to run a proof of concept can skip this step. AWS Application Migration Service
automatically uses the default subnet and Security groups. Make sure that you have not deleted
your default subnet.
