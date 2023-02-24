class Solution:
    def hello(self, name="Ivan", surname="Ivanov", years=14):
        print("Hello", name, surname, years, "years old")
a=Solution()
a.hello("Oleg", "Andrianov", 16)
a.hello("Oleg", "Andrianov")
a.hello("Oleg")
a.hello()
