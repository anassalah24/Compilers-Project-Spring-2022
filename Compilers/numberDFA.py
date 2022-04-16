from automata.fa.dfa import DFA
from sympy import true

from visual_automata.fa.dfa import VisualDFA



def number_dfa():
    new_dfa = VisualDFA(
    states={'q0', 'q1','DEAD'},
    input_symbols={'digit', '+-'},
    transitions={
        'q0': {'digit':'q1','+-':'q1'},
        'q1':{'digit':'q1','+-':'DEAD'},
        'DEAD':{'digit':'DEAD','+-':'DEAD'},
        
    },
    initial_state='q0',
    final_states={'q1'}
)
    new_dfa.show_diagram(view=true,font_size=5)

