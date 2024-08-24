import pytest
import builtins
import project

# Helper function to simulate input
def mock_input(inputs):
    input_gen = (i for i in inputs)
    builtins.input = lambda _: next(input_gen)

def test_user():
    mock_input(['Alice', 'Bob', 'Charlie', 'David'])
    result = project.user()
    assert result == ['Alice', 'Bob', 'Charlie', 'David']

def test_teamSelect_random():
    mock_input(['r'])  # Simulate choosing random teams
    names = ['Alice', 'Bob', 'Charlie', 'David']
    teams = project.teamSelect(names)
    assert len(set(teams)) == 4  # Ensure all teams are unique

def test_teamSelect_manual():
    mock_input(['t', 'Chelsea', 'Liverpool', 'Arsenal', 'Juventus'])  # Simulate manual team selection
    names = ['Alice', 'Bob', 'Charlie', 'David']
    teams = project.teamSelect(names)
    assert teams == ('Chelsea', 'Liverpool', 'Arsenal', 'Juventus')

def test_group():
    mock_input([
        '1', '1',  # Match 1: Draw
        '2', '1',  # Match 2: Team 3 wins
        '0', '0',  # Match 3: Draw
        '1', '2',  # Match 4: Team 4 wins
        '3', '1',  # Match 5: Team 1 wins
        '1', '2'   # Match 6: Team 3 wins
    ])
    names = ['Alice', 'Bob', 'Charlie', 'David']
    project.group(names)

    # Here we manually check the output; ideally, you'd return scores or winner and assert those

def test_knockout():
    mock_input([
        '2', '1',  # Semi-Final 1: Team 1 wins
        '3', '0',  # Semi-Final 2: Team 3 wins
        '1', '2'   # Final: Team 4 wins
    ])
    names = ['Alice', 'Bob', 'Charlie', 'David']
    project.knockout(names)

    # Similar to the group test, you would manually validate the print output
