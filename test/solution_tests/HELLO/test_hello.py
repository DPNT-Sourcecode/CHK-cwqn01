from lib.solutions.HLO import hello_solution


class TestSum():
    def test_hello(self):
        friend_name = 'sai'
        assert hello_solution.hello(friend_name) == f"Hello, {friend_name}!"
