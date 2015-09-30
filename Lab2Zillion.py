###########################################
# Author: Dennis Melamed                  #
# Date: Fri, Sept 25th                    #
# Assignment: CSci 1913, Lab2, "Zillion"  #
###########################################

class Zillion:
    def __init__(self, digits):
        self.numbers = []
        possibles = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        # tests for validity of string entered
        hasDigit = False
        for each in digits:
            if not (each == ',' or each == ' ' or each in possibles):
                raise RuntimeError('invalid char')
            if (each in possibles):
                hasDigit = True
        if not hasDigit:
            raise RuntimeError('invalid string')
        # transfers string to list
        for each in digits:
            if each in possibles:
                self.numbers = self.numbers + [int(each)]

    def increment(self):
        start = -1
        ninefound = False
        while start >= -len(self.numbers):
            if self.numbers[start] == 9:
                self.numbers[start] = 0
            else:
                self.numbers[start] = self.numbers[start] + 1
                return
            start = start - 1
        #
        for each in self.numbers:
            if each == 9:
                ninefound = True
        if not ninefound:
            self.numbers.insert(0, 1)

    def isZero(self):
        if 0 == reduce((lambda x, y: x + y), self.numbers):
            return True
        return False

    def toString(self):
        string = ''
        for each in self.numbers:
            string = string + str(each)
        return string

# tests (most tests show functionality of toString())

# tests if Zillion can handle numbers larger than int can hold
x = Zillion('99,999,999,999, 999')
print x.toString()  # 99999999999999


# tests if increment works, for cases where a digit rolls over to zero, does not roll over to zero, and roles over in a "full of nines" case
print "\n"
z = Zillion('12349')
z.increment()
print z.toString()  # 12350

a = Zillion('1234')
a.increment()
print a.toString()  # 1235

b = Zillion('999,999')
b.increment()
print b.toString()  # 1000000

# tests both cases for isZero()
print "\n"
x = Zillion("134")
print x.isZero()  # False

x = Zillion('000')
print x.isZero()  # True


# tests if RuntimeError is raised when an invalid string is entered
x = Zillion('a')
x = Zillion(', ,  ')
