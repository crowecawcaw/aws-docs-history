# Roles of frames and ports

This section describes the predefined frames and ports available for each device. We
will also briefly discuss the mechanisms involved when pulses are played on certain
frames.

## Rigetti frames

Rigetti devices support predefined frames that have their frequency and
phase calibrated to be on resonance with the associated qubit. The naming convention is
`q{i}[_q{j}]_{role}_frame` where `{i}` refers to the first
qubit number, `{j}` refers to the second qubit number in case the frame
serves to activate a two-qubit interaction, and `{role}` refers to the role
of the frame. The roles are as follows:

- `rf` is the frame to drive the 0-1 transition of the qubit. Pulses are
  transmitted as microwave transient signals of frequency and phase previously
  provided through the `set` and `shift` functions. The
  time-dependent amplitude of the signal is given by the waveform played on the
  frame. The frame plugs a single-qubit, off-diagonal interaction. For more
  information, see [Krantz et
  al.](https://pubs.aip.org/aip/apr/article/6/2/021318/570326/A-quantum-engineer-s-guide-to-superconducting "https://pubs.aip.org/aip/apr/article/6/2/021318/570326/A-quantum-engineer-s-guide-to-superconducting") and [Rahamim et
  al.](https://pubs.aip.org/aip/apl/article-abstract/110/22/222602/34004/Double-sided-coaxial-circuit-QED-with-out-of-plane "https://pubs.aip.org/aip/apl/article-abstract/110/22/222602/34004/Double-sided-coaxial-circuit-QED-with-out-of-plane").
- `rf_f12` is similar to `rf` and its parameters target the
  1-2 transition.
- `ro_rx` is used to achieve dispersive readout of the qubit through a
  coupled coplanar waveguide. The frequency, phase, and full set of parameters for
  the readout waveform are precalibrated. It is used through the
  `capture_v0`, which does not require any argument besides the frame
  identifier.
- `ro_tx` is for transmitting signals from the resonator. It is currently
  unused.
- `cz` is a frame calibrated to enable the two-qubit `cz`
  gate. As with all the frames associated with an `ff` port, it turns on
  an entangling interaction through the flux line by modulating the tunable qubit of
  the pair on resonance with its neighbor. For more information about the entangling
  mechanism, see [Reagor et
  al.](https://www.science.org/doi/10.1126/sciadv.aao3603 "https://www.science.org/doi/10.1126/sciadv.aao3603"), [Caldwell et al.](https://journals.aps.org/prapplied/abstract/10.1103/PhysRevApplied.10.034050 "https://journals.aps.org/prapplied/abstract/10.1103/PhysRevApplied.10.034050"), and [Didier et al.](https://journals.aps.org/pra/abstract/10.1103/PhysRevA.97.022330 "https://journals.aps.org/pra/abstract/10.1103/PhysRevA.97.022330").
- `cphase` is a frame calibrated to enable the two-qubit
  `cphaseshift` gate and is linked to an `ff` port. For
  more information about the entangling mechanism, see the description for the
  `cz` frame.
- `xy` is a frame calibrated to enable the two-qubit XY(θ) gates and is
  linked to an `ff` port. For more information about the entangling
  mechanism and how to achieve XY gates, see the description for the `cz`
  frame and [Abrams et
  al.](https://www.nature.com/articles/s41928-020-00498-1#Abs1 "https://www.nature.com/articles/s41928-020-00498-1#Abs1").

As frames based on the `ff` port shift the frequency of the tunable qubit,
all the other driving frames related to the qubit will be dephased by an amount that is
related to the amplitude and the duration of the frequency shift. Consequently, you must
compensate for this effect by adding a corresponding phase shift to the frames of the
neighboring qubits.

**Ports**

The Rigetti devices provide a list of ports that you can inspect
through the device capabilities. Port names follow the convention
`q{i}_{type}` where `{i}` refers to the qubit number and
`{type}` refers to the type of the port. Note that not all of the qubits
have a complete set of ports. The types of ports are as follows:

- `rf` represents the main interface to drive the single-qubit
  transition. It is associated with the `rf` and `rf_f12`
  frames. It is capacitively coupled to the qubit, allowing microwave driving in the
  gigahertz range.
- `ro_tx` serves to transmit signals to the readout resonator
  capacitively coupled to the qubit. Readout signal delivery is multiplexed
  eight-fold by octagon.
- `ro_rx` serves to receive signals from the readout resonator coupled to
  the qubit.
- `ff` represents the fast-flux line inductively coupled to the qubit. We
  can use this to tune the frequency of the transmon. Only qubits designed to be
  highly tunable have an `ff` port. This port serves to activate
  qubit-qubit interaction as there is a static capacitive coupling between each pair
  of neighboring transmons.

For more information about the architecture, see [Valery et al.](https://journals.aps.org/prxquantum/abstract/10.1103/PRXQuantum.3.020337 "https://journals.aps.org/prxquantum/abstract/10.1103/PRXQuantum.3.020337").
