from pulp import *

places_name = ['TE', 'ML', 'AT', 'MO', 'JT', 'CA', 'CP', 'CN', 'BS', 'SC', 'PC', 'TM', 'AC']
price = [15.5, 12, 9.5, 11, 0, 10, 10, 5, 8, 8.5, 0, 15, 0]
duration = [4.5, 3, 1, 2, 1.5, 2, 2.5, 2, 2, 1.5, 0.75, 2, 1.5]
places = [LpVariable(i, 0, 1, LpInteger) for i in places_name]
places_dict = {i: j for i, j in zip(places_name, places)}
city_close = [('ML', 'SC'), ('AT', 'AC'), ('MO', 'JT'), ('MO', 'PC'),
              ('JT', 'PC'), ('CP', 'CN'), ('CP', 'SC'), ('CN', 'SC')]


def basic_constraint(problem):
    problem += lpSum(places), 'First Question'
    problem += lpSum([places[i] * price[i] for i in range(len(places))]) <= 65, "Money constraint"
    problem += lpSum([places[i] * duration[i] for i in range(len(places))]) <= 12, "Time constraint"


# Preference 1
def preference1(problem):
    for cc in city_close:
        problem += places_dict[cc[0]] == places_dict[cc[1]], cc[0] + "==" + cc[1]


# Preference 2
def preference2(problem):
    problem += places_dict['TE'] == 1, "Absolutely want to visit TE"
    problem += places_dict['CA'] == 1, "Absolutely want to visit CA"


# Preference 3
def preference3(problem):
    problem += places_dict['CN'] != places_dict['SC'], "If CN, then not SC"


# Preference 4
def preference4(problem):
    problem += places_dict['TM'] == 1, "Absolutely want to visit TM"


# Preference 5
def preference5(problem):
    problem += places_dict['ML'] == places_dict['CP']


if __name__ == "__main__":

    questions = {"2b": [1, 2],
                 "2c": [1, 3],
                 "2d": [1, 4],
                 "2e": [2, 5],
                 "2f": [3, 4],
                 "2g": [4, 5],
                 "2h": [1, 2, 3],
                 "2i": [2, 3, 5],
                 "2j": [2, 3, 4, 5],
                 "2k": [1, 2, 4, 5],
                 "2l": [1, 2, 3, 4, 5]}
    solutions = []
    preferences = {
        1: preference1,
        2: preference2,
        3: preference3,
        4: preference4,
        5: preference5,
    }

    # Question 1
    question1 = LpProblem("How to visit Paris? Question 1.", LpMaximize)
    basic_constraint(question1)
    question1.solve()
    solution1 = [v.name for v in question1.variables() if v.varValue == 1]
    solutions.append(solution1)

    # Question 2a
    for i in range(5):
        question2 = LpProblem("How to visit Paris? Question 2a{}.".format(i + 1), LpMaximize)
        basic_constraint(question2)
        preferences[i + 1](question2)
        question2.solve()
        solution2 = [v.name for v in question2.variables() if v.varValue == 1]
        solutions.append(solution2)

    # Question 2b-2l
    for (i, ps) in questions.items():
        print(i, ps)
        question = LpProblem("How to visit Paris? Question {}.".format(i), LpMaximize)
        basic_constraint(question)
        for p in ps:
            preferences[p](question)
        question.solve()
        solution = [v.name for v in question.variables() if v.varValue == 1]
        solutions.append(solution)

    # Solution 1
    print("==============================================================")
    print("Question 1:")
    print("It is assumed that Mr. Doe gives equal importance to each tourist site, "
          "and he wants to visit the maximum number of sites. Which list(s) of places could you recommend to him ? "
          "This solution will be called ListVisit 1.")
    print(solutions[0])
    print("Total sites that can be visited = ", len(solutions[0]))
    print()

    # Solution 2a
    print("==============================================================")
    print("Question 2a:")
    print("For each of the five preferences above, suggest to Mr. Doe, one or more lists of tourist sites to visit. "
          "Are the obtained lists different from the solution ListVisit 1 ? ")

    for i, solution in enumerate(solutions[1:6]):
        print("For preference {}:".format(i + 1))
        print(solution)
        print("Total sites that can be visited = ", len(solution))
        if solution == solutions[0]:
            print("ListVisit1 is same as Question 2a{}'s solution.".format(i + 1))
        else:
            print("ListVisit1 is different from Question 2a{}'s solution.".format(i + 1))
        print()

    # Solution 2b-2l
    for i, solution in zip(questions.items(), solutions[6:]):
        print("==============================================================")
        print("Question {}:".format(i[0]))
        print("For preference {}.".format(i[1]))
        print(solution)
        print("Total sites that can be visited = ", len(solution))
        if solution == solutions[0]:
            print("ListVisit1 is same as Question {}'s solution.".format(i[0]))
        else:
            print("ListVisit1 is different from Question {}'s solution.".format(i[0]))
        print()

    print("==============================================================")
    print("Question 2m: Mentioned above.")
