from wrap_generator import *

# The many_body_operators module
module = module_(full_name = "pytriqs.operators.util.extractors",
                 doc = "Functions to extract coefficients from many-body operators")

module.use_module("operators")
module.add_include("<triqs/operators/util/extractors.hpp>")
module.add_include("<triqs/python_tools/converters/map.hpp>")
module.add_include("<triqs/python_tools/converters/tuple.hpp>")
module.add_include("<triqs/python_tools/converters/arrays.hpp>")
module.add_using("namespace triqs::utility")
module.add_using("namespace triqs::operators::util")

module.add_preamble("""
using indices_v_t = typename op_t<double>::indices_t;
using indices_t_t = std::tuple<typename indices_v_t::value_type,typename indices_v_t::value_type>;
auto v2t = [](indices_v_t const& v) { return std::make_tuple(v[0],v[1]); };
using triqs::tuple::map;
""")

module.add_function("dict2_t<double> extract_h_dict(many_body_operator<double> H, bool ignore_irrelevant = false)",
                    calling_pattern = """
                    std::map<std::tuple<indices_t_t,indices_t_t>,double> result;
                    for(auto const& kv : extract_h_dict(*H,ignore_irrelevant)) result[map(v2t,kv.first)] = kv.second;
                    """,
                    doc = r"""
    Extract coefficients of the quadratic part :math:`\sum_{ij}h_{ij} c^\dagger_i c_j` from a Hamiltonian H as a 2-index dictionary.

    Parameters
    ----------
    H : Operator
        The Hamiltonian.
    ignore_irrelevant : bool
        If True, ignore all irrelevant terms in H.
        Otherwise raise an exception when such terms are met.

    Returns
    -------
    h_dict : dict
        The 2-index dictionary of the quadratic part coefficients, {(i,j) \: float}.

""")

module.add_function("dict2_t<double> extract_U_dict2(many_body_operator<double> H, bool ignore_irrelevant = false)",
                    calling_pattern = """
                    std::map<std::tuple<indices_t_t,indices_t_t>,double> result;
                    for(auto const& kv : extract_U_dict2(*H,ignore_irrelevant)) result[map(v2t,kv.first)] = kv.second;
                    """,
                    doc = r"""
    Extract U-matrix of the density-density interaction part :math:`\frac{1}{2}\sum_{ij} U_{ij} n_i n_j`
    from a Hamiltonian H as a 2-index dictionary.

    Parameters
    ----------
    H : Operator
        The Hamiltonian.
    ignore_irrelevant : bool
        If True, ignore all irrelevant terms in H.
        Otherwise raise an exception when such terms are met.

    Returns
    -------
    U_dict : dict
        The 2-index interaction dictionary, {(i,j) \: float}.

""")

module.add_function("dict4_t<double> extract_U_dict4(many_body_operator<double> H, bool ignore_irrelevant = false)",
                    calling_pattern = """
                    std::map<std::tuple<indices_t_t,indices_t_t,indices_t_t,indices_t_t>,double> result;
                    for(auto const& kv : extract_U_dict4(*H,ignore_irrelevant)) result[map(v2t,kv.first)] = kv.second;
                    """,
                    doc = r"""
    Extract U-matrix of the interaction part :math:`\frac{1}{2}\sum_{ijkl} U_{ijkl} c^\dagger_i c^\dagger_j c_l c_k`
    from a Hamiltonian H as a 4-index dictionary.

    Parameters
    ----------
    H : Operator
        The Hamiltonian.
    ignore_irrelevant : bool
        If True, ignore all irrelevant terms in H.
        Otherwise raise an exception when such terms are met.

    Returns
    -------
    U_dict : dict
        The 4-index interaction dictionary, {(i,j,k,l) \: float}.

""")

dict_to_matrix_docstring = r"""
Convert a 2/4-index dictionary to a 2/4-dimensional NumPy array given the structure of the Green's function.
The elements missing from the dictionary are assumed to be zero.

Parameters
----------
d : dict
    The 2/4-index dictionary.
gf_struct : dict
    The structure of the Green's function, {block_index \: [inner indices]}.

Returns
-------
arr : array
    The resulting NumPy array.

"""

module.add_function("triqs::arrays::array<double,2> dict_to_matrix(dict2_t<double> d, gf_struct_t gf_struct)",
                    doc = dict_to_matrix_docstring)
module.add_function("triqs::arrays::array<double,4> dict_to_matrix(dict4_t<double> d, gf_struct_t gf_struct)",
                    doc = dict_to_matrix_docstring)

module.generate_code()

