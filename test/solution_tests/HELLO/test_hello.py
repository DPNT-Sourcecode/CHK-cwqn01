from lib.solutions.HLO import hello_solution


class TestHello:
    def test_hello(self):
        friend_name = 'sai'
        assert hello_solution.hello(friend_name) == f"Hello, {friend_name}!"

