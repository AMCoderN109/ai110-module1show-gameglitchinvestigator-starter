from logic_utils import check_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"

def test_too_high_hint_says_go_lower():
    # Bug: a guess above the secret used to say "Go HIGHER!"
    _, message = check_guess(60, 50)
    assert "LOWER" in message

def test_too_low_hint_says_go_higher():
    # Bug: a guess below the secret used to say "Go LOWER!"
    _, message = check_guess(40, 50)
    assert "HIGHER" in message

def test_out_of_bounds_high_guess_says_go_lower():
    # Guess far above the 1-100 range should still point back down
    outcome, message = check_guess(200, 50)
    assert outcome == "Too High"
    assert "LOWER" in message

def test_out_of_bounds_low_guess_says_go_higher():
    # Guess below the range should still point back up
    outcome, message = check_guess(-5, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message

def test_compares_numbers_not_text():
    # Bug: secret was turned into a string, so "200" < "50" alphabetically.
    # 200 must count as higher than 50, and 9 as lower than 10.
    assert check_guess(200, 50)[0] == "Too High"
    assert check_guess(9, 10)[0] == "Too Low"
