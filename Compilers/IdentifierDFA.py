from automata.fa.dfa import DFA
from sympy import true

from visual_automata.fa.dfa import VisualDFA



def id_dfa():
    new_dfa = VisualDFA(
    states={'q0', 'q1','DEAD'},
    input_symbols={'letter', 'digit','underscore'},
    transitions={
        'q0': {'letter': 'q1', 'digit': 'DEAD','underscore':'q1'},
        'q1':{'letter': 'q1', 'digit': 'q1','underscore':'q1'},
        'DEAD':{'letter': 'DEAD', 'digit': 'DEAD','underscore':'DEAD'},
        
    },
    initial_state='q0',
    final_states={'q1'}
)
    new_dfa.show_diagram(view=true,font_size=5)

   