..
   Generated automatically by cpp2rst

.. highlight:: c


.. _atomic_g_iw:

atomic_g_iw
===========

**Synopsis**:

.. code-block:: c

    template<bool Complex>                                                                                                                                                                                                               (1)
    block_gf<triqs::gfs::imfreq> atomic_g_iw (const gf_lehmann_t<Complex> & lehmann,
   const triqs::hilbert_space::gf_struct_t & gf_struct, const
   gf_mesh<triqs::gfs::imfreq> & mesh)

    template<bool Complex>                                                                                                                                                                                                               (2)
    block_gf<triqs::gfs::imfreq> atomic_g_iw (const atom_diag<Complex> & atom, double
   beta, const triqs::hilbert_space::gf_struct_t & gf_struct, int n_iw, const
   triqs::atom_diag::excluded_states_t & excluded_states = {})

(1)The atomic Matsubara Green's function, constructed from precomputed Lehmann representation


Template parameters
-------------------

 * **Complex**: Are we using Lehmann representation with complex matrix elements?



Parameters
----------

 * **lehmann**: Lehmann representation.

 * **gf_struct**: Block structure of the Green's function, block name -> list of inner indices.

 * **mesh**: Matsubara mesh used in construction.



Return value
------------

Atomic Green's function :math:`G_{at}(i\omega)`.


Documentation
-------------




(2)The atomic Matsubara Green's function, possibly with excluded states (none by default)


Template parameters
-------------------

 * **Complex**: Do we have a diagonalization problem with a complex-valued Hamiltonian?



Parameters
----------

 * **atom**: Solved diagonalization problem.

 * **beta**: Inverse temperature.

 * **gf_struct**: Block structure of the Green's function, block name -> list of inner indices.

 * **n_iw**: Number of Matsubara frequencies.

 * **excluded_states**: Excluded eigenstates as pairs (subspace index, inner index).



Return value
------------

Atomic Green's function :math:`G_{at}(i\omega)`.


Documentation
-------------