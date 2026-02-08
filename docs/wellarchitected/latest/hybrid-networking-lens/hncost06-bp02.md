# HNCOST06-BP02 Separate traffic classes for dedicated connections

Create multiple dedicated connections for distinct traffic classes
such as production versus backups. Assign guaranteed bandwidth to
critical dedicated connections and use best-effort routing for
dedicated connections.

**Desired outcome:** Cost-effective
traffic segregation with guaranteed SLAs for priority workloads.

**Level of risk exposed if this best
practice is not established:** Low

**Benefits of establishing this best
practice:**

- Simplifies cost allocation by traffic type
- Enables independent scaling of traffic classes
- Complies with network isolation requirements

## Implementation guidance

- Configure separate BGP communities for dedicated connection.
  For example, you can achieve this using AWS Direct Connection
  VIFs on dedicated connections.

### Resources

- [Direct
  Connect virtual interfaces](../../../directconnect/latest/UserGuide/create-vif.md "../../../directconnect/latest/UserGuide/create-vif.md")
