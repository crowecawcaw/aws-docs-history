# Number of primary Elemental Statmux

nodes

Determine the number of _primary nodes_ you need:

- Identify the density of all the SPTS channels that you
  want to mux into MPTSes. Then consult with your AWS Elemental sales
  person for help to identify your node requirements.
- Keep in mind that you can run more than one MPTS on a
  node.

###### Note

You might have acquired a high-compute-power Elemental Statmux node with
the intention of implementing Simulcrypt encryption, when it
becomes available in Elemental Statmux.

Simulcrypt has high compute-power requirements. You might want
to plan fewer MPTSes on the node. In this way, you will be able
to implement Simulcrypt later without moving any MPTSes to
another node.

After you have determined the number of primary nodes, you should
identify your redundant node requirements. See [Worker node redundancy](redundancy-worker.md "redundancy-worker.md").
