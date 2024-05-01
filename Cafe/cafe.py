import sys
from textx import metamodel_from_file

inputProgram = sys.argv[1]
state = {}


def varMap(state, target):
    variable = target[0]
    if variable in state:
        return state[variable]
    elif target not in state:
        state[target[0]] = target[1]


def interpret(program):
    for cafe_class in program.classes:
        for member in cafe_class.members:
            if hasattr(member, "name") and hasattr(member, "body"):
                for statement in member.body:
                    if isinstance(statement, cafe_grammar['PrintStatement']):
                        print(statement.expression)
                    elif isinstance(statement, cafe_grammar['AssignmentStatement']):
                        variable = statement.variable
                        value = statement.expression
                        target = (variable, value)
                        varMap(state, target)
                    elif isinstance(statement, cafe_grammar['PrintVariable']):
                        target = (statement.expression,)
                        print(varMap(state, target))


cafe_grammar = metamodel_from_file('cafe.tx')

program = cafe_grammar.model_from_file(inputProgram)

interpret(program)