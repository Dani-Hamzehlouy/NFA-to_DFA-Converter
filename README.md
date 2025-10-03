# NFA to DFA Converter

## Overview

This Python project implements a program to convert a Nondeterministic Finite Automaton (NFA) to a Deterministic Finite Automaton (DFA) based on principles from computability theory. The program allows users to define an NFA by inputting its states, alphabet, transition function, starting state, and accepting states, and then converts it to an equivalent DFA using the subset construction method. The resulting DFA can evaluate input strings to determine if they are accepted.

## Features

- **NFA Definition**: Users can input the components of an NFA, including states, alphabet, transitions, starting state, and accepting states.
- **NFA to DFA Conversion**: Converts the provided NFA to a DFA using the subset construction algorithm.
- **String Evaluation**: Evaluates input strings against the generated DFA to determine acceptance.
- **User-Friendly Interface**: Prompts users for input in a clear, step-by-step manner.
- **Support for Null Transitions**: Handles cases where transitions are undefined (represented as "phi" or empty input).

## Requirements

- Python 3.x
- No external libraries are required.

## Installation

1. Clone or download the project repository.
2. Ensure Python 3.x is installed on your system.
3. Save the provided Python code in a file (e.g., `nfa_to_dfa.py`).

## Usage

1. Run the Python script using the command:

   ```bash
   python nfa_to_dfa.py
   ```
2. Follow the prompts to input the NFA components:
   - **States**: Enter the states of the NFA, separated by spaces (e.g., `q0 q1 q2`).
   - **Alphabet**: Enter the alphabet symbols, separated by spaces (e.g., `0 1`).
   - **Transition Function**: For each state and alphabet symbol, specify the next state(s) or "phi" for no transition. For NFAs, multiple states can be entered, separated by spaces.
   - **Starting State**: Enter the starting state (e.g., `q0`).
   - **Accepting States**: Enter the accepting states, separated by spaces (e.g., `q1 q2`).
3. The program will display the entered NFA and the resulting DFA.
4. You can then input up to five strings to evaluate against the DFA, and the program will indicate whether each string is accepted or rejected.

## Example

### Input

```
Enter the states of your NFA(seperate states with a space):
q0 q1 q2
Enter the alphabet of your NFA(seperate with a space):
0 1
Enter the transtition function of your NFA(seperate states with a space)
delta(q0,0) = q0 q1
delta(q0,1) = q1
delta(q1,0) = q2
delta(q1,1) = q1 q2
delta(q2,0) = 
delta(q2,1) = 
Enter the starting state of your NFA:
q0
Enter the accepting states of your NFA(seperate with a space):
q2
Type a string to evaluate:
01
```

### Output

```
This is the NFA you Entered:
States:
['q0', 'q1', 'q2']

Alphabet:
['0', '1']

delta(('q0', '0')) = {'q0', 'q1'}
delta(('q0', '1')) = {'q1'}
delta(('q1', '0')) = {'q2'}
delta(('q1', '1')) = {'q1', 'q2'}
delta(('q2', '0')) = None
delta(('q2', '1')) = None

Starting state:
q0

Accepting states:
['q2']

**************************

This is the result DFA:
States:
[('q0',), ('q0', 'q1'), ('q1',), ('q1', 'q2'), ('q2',), ('phi',)]

Alphabet:
['0', '1']

delta((('q0',), '0')) = ('q0', 'q1')
delta((('q0',), '1')) = ('q1',)
delta((('q0', 'q1'), '0')) = ('q1', 'q2')
delta((('q0', 'q1'), '1')) = ('q1', 'q2')
delta((('q1',), '0')) = ('q2',)
delta((('q1',), '1')) = ('q1', 'q2')
delta((('q1', 'q2'), '0')) = ('q2',)
delta((('q1', 'q2'), '1')) = ('q1', 'q2')
delta((('q2',), '0')) = ('phi',)
delta((('q2',), '1')) = ('phi',)
delta((('phi',), '0')) = ('phi',)
delta((('phi',), '1')) = ('phi',)

Starting state:
('q0',)

Accepting states:
[('q1', 'q2'), ('q2',)]

Accepted
```

## Code Structure

- **Classes**:
  - `DFA`: Represents a Deterministic Finite Automaton with states, alphabet, transitions, starting state, and accepting states.
  - `NFA`: Represents a Nondeterministic Finite Automaton with similar components, but transitions can lead to multiple states.
- **Functions**:
  - `get_DFA()`: Collects user input to define a DFA.
  - `evaluate(dfa, input_string)`: Evaluates whether a string is accepted by the DFA.
  - `get_NFA()`: Collects user input to define an NFA.
  - `DFA_states(nfa)`: Generates the DFA states using subset construction.
  - `set_construct(nfa, starter_states, alpha)`: Computes the set of next states for a given state set and alphabet symbol.
  - `list_maker(list_of_sets)`: Converts a list of sets to a list of tuples for DFA state representation.
  - `NFA_to_DFA(nfa, states)`: Converts an NFA to a DFA.
  - `main()`: Orchestrates the program flow, including input collection, NFA to DFA conversion, and string evaluation.

## Limitations

- The program does not support epsilon-transitions in the NFA.
- Input validation is minimal; users must provide correct input formats.
- The DFA state names are represented as tuples, which may be less intuitive for complex NFAs.

## Contributing

Contributions are welcome! Please submit pull requests or issues to the project repository for bug fixes, enhancements, or additional features like epsilon-transition support or input validation.
