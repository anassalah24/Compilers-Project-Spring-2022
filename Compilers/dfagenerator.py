
from automata.fa.nfa import NFA
from sympy import true

from visual_automata.fa.nfa import VisualNFA


def dfagenerator(myinput):
    
    myDfa = VisualNFA(
        states={'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9','q10'},
        input_symbols={'I', 'N', 'A', 'S', 'F', 'T', 'E', 'L','G'},
        transitions={
            'q1': {'F': {'q2'}},
            'q2': {'N': {'q3'}},
            'q3': {'T': {'q4'}},
            'q4': {'I': {'q5'}, 'E': {'q10'}},
            'q5': {'A': {'q6'}},
            'q6': {'I': {'q7'}, 'N': {'q7'}},
            'q7': {'S': {'q8'}},
            'q8': {'I': {'q5'},'E': {'q10'}, 'L': {'q9'}},
            'q9': {'I': {'q5'},'E': {'q10'}},
            'q10': {},
            

            
        },
        initial_state='q1',
        final_states={'q10'}
    )

    myDfa.show_diagram(myinput,view=true)
    
 