#Here we define a DFA class
class DFA:
    def __init__(self, states, alphabet, transitions, starting_state, accepting_states):
        self.states = states
        self.alphabet = alphabet
        self.transitions = transitions
        self.starting_state = starting_state
        self.accepting_states = accepting_states

#This is a function to get the needed inputs for a DFA and 
# return the 5-tuple 
def get_DFA():

    states = []
    alphabet = []
    transitions = {}
    starting_state = ""
    accepting_states = []

    print("Enter the states of your DFA(seperate states with a space):")
    states = input().split(' ')

    print("Enter the alphabet of your DFA(seperate with a space):")
    alphabet = input().split(' ')

    #getting all the "next" states from the user
    print("Enter the transtition function of your DFA...")
    for state in states:
        for alpha in alphabet:
            print(f"delta({state},{alpha}) = ",end='')
            next_state = input()

            if next_state == "phi":
                transitions[(state, alpha)] = None
                continue

            transitions[(state, alpha)] = next_state

    print("Enter the starting state of your DFA:")
    starting_state = input()

    print("Enter the accepting states of your DFA(seperate with a space):")
    accepting_states = input().split(' ')

    return states, alphabet, transitions, starting_state, accepting_states

#In this function we check if a string 'input_string' is accepted by the given DFA 'dfa'
def evaluate(dfa, input_string):

    this_state = dfa.starting_state

    for char in input_string:
        this_state = dfa.transitions[(this_state, char)]

        if this_state == None:
            print("Rejected")
            return
    else:
        if this_state in dfa.accepting_states:
            print("Accepted")
        else:
            print("Rejected")

#Here we define the NFA class
class NFA:
    def __init__(self, states, alphabet, transitions, starting_state, accepting_states):
        self.states = states
        self.alphabet = alphabet
        self.transitions = transitions
        self.starting_state = starting_state
        self.accepting_states = accepting_states

#In this function we get the inputs needed to make an nfa, from the user
def get_NFA():

    states = []
    alphabet = []
    transitions = {}
    starting_state = ""
    accepting_states = []

    print("Enter the states of your NFA(seperate states with a space):")
    states = input().split(' ')

    print("Enter the alphabet of your NFA(seperate with a space):")
    alphabet = input().split(' ')

    print("Enter the transtition function of your NFA(seperate states with a space)")
    for state in states:
        for alpha in alphabet:
            print(f"delta({state},{alpha}) = ",end='')
            next_state = input()

            #If there is no transition for the given state and alpha
            # the user can simply press "Enter" 
            if next_state == "phi" or next_state == "":
                transitions[(state, alpha)] = None
                continue

            next_state = set(next_state.split(' '))

            transitions[(state, alpha)] = next_state

    print("Enter the starting state of your NFA:")
    starting_state = input()

    print("Enter the accepting states of your NFA(seperate with a space):")
    accepting_states = input().split(' ')

    return states, alphabet, transitions, starting_state, accepting_states

#This function returns the list of states of a dfa correspondent to the given nfa(without e_transitions)
def DFA_states(nfa):
    states = []

    handle_queue = []

    states.append(set(nfa.starting_state))
    handle_queue.append(nfa.starting_state)
    while len(handle_queue) != 0:
        state = handle_queue[0]
        for alpha in nfa.alphabet:
            new_state = set_construct(nfa, state, alpha)

            if new_state == set():
                if set(["phi"]) not in states:
                    states.append(set(["phi"]))
                continue

            if new_state not in states:
                states.append(new_state)
                handle_queue.append(new_state)
        handle_queue.pop(0)
    
    return states

#This function returns the set of next_states for a set of starting states and a character of the alphabet
# in a given nfa
def set_construct(nfa, starter_states, alpha):
    ans = set()
    if type(starter_states) == type(ans):
        for state in starter_states:
            if nfa.transitions[(state, alpha)] != None:
                ans = ans.union(nfa.transitions[(state, alpha)])
    else:
        if nfa.transitions[(starter_states, alpha)] != None:
            ans = ans.union(nfa.transitions[(starter_states, alpha)])
    return ans

#This is a utility function that converts a list of sets to a list of tuples
def list_maker(list_of_sets):
    ans = []
    for a_set in list_of_sets:
        ans.append(tuple(sorted(tuple(a_set))))
    return ans

#This function returns a DFA correspondent to the given NFA
def NFA_to_DFA(nfa, states):
    DFA_states = states

    DFA_starting_state = tuple([nfa.starting_state])

    DFA_alphabet = nfa.alphabet

    DFA_accepting_states = []
    for each_accepting_state in nfa.accepting_states:
        for this_state in DFA_states:
            for a_single_state in this_state:
                if each_accepting_state == a_single_state:
                    if this_state not in DFA_accepting_states:
                        DFA_accepting_states.append(this_state)
                        continue
    
    DFA_transitions = {}
    for DFA_state in DFA_states:
        
        for alpha in DFA_alphabet:

            if DFA_state == tuple(['phi']):
                DFA_transitions[(DFA_state, alpha)] = tuple(['phi'])
                continue

            next_state = set_construct(nfa, set(DFA_state), alpha)

            if next_state == set():
                DFA_transitions[(DFA_state, alpha)] = tuple(['phi'])
                continue

            DFA_transitions[(DFA_state, alpha)] = tuple(sorted(tuple(next_state)))

    my_final_dfa = DFA(DFA_states, DFA_alphabet, DFA_transitions, DFA_starting_state, DFA_accepting_states)
    return my_final_dfa

def main():
    my_nfa = NFA(*get_NFA())
    print("\nThis is the NFA you Entered:")
    print("States:")
    print(my_nfa.states,"\n")
    print("Alphabet:")
    print(my_nfa.alphabet,"\n")
    for key, value in my_nfa.transitions:
        print(f"delta({key},{value}) = {my_nfa.transitions[(key,value)]}")
    print()
    print("Starting state:")
    print(my_nfa.starting_state, "\n")
    print("Accepting states:")
    print(my_nfa.accepting_states, "\n")
    print("\n**************************\n")

    my_dfa = NFA_to_DFA(my_nfa, list_maker(DFA_states(my_nfa)))

    print("\nThis is the result DFA:")
    print("States:")
    print(my_dfa.states,"\n")
    print("Alphabet:")
    print(my_dfa.alphabet,"\n")
    for key, value in my_dfa.transitions:
        print(f"delta({key},{value}) = {my_dfa.transitions[(key,value)]}")
    print()
    print("Starting state:")
    print(my_dfa.starting_state, "\n")
    print("Accepting states:")
    print(my_dfa.accepting_states, "\n")

    for _ in range(5):
        print("Type a string to evaluate:")
        my_str = input()
        evaluate(my_dfa, my_str)

main()