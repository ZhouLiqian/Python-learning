# function1
def commentary(color):
    if color == 'red':
        return "It's a tomato."
    elif color == 'green':
        return "It's a green pepper."
    elif color == 'bee purple':
        return "I don't know what it is,but only bees can see it."
    else: 
        return "I've never heard of this color : " + color + "."

# function2
def is_none(thing):
    if thing is None:
        print("It's None")
    elif thing:
        print("It's True")
    else:
        print("It's False")

# positional parameters
def menu(wine,entree,dessert):
    return{'wine':wine, 'entree':entree, 'dessert':dessert}
# menu = menu('chardonnay','chicken','cake')

# keyword parameters
menu1 = menu(wine = 'bordeaux',entree = 'beef',dessert = 'bagel')

# default parameters
def mmenu(wine,entree,dessert = 'pudding'):
    return{'wine':wine,'entree':entree,'dessert':dessert}
# mmenu = mmenu('chardonnay','chicken')
mmenu1 = mmenu('dunkelfelder','duck','doughnut')

# add parameters to list
def buggy(arg,result = []):
    result.append(arg)
    print(result)

def works(arg):
    result = []
    result.append(arg)
    print(result)

# *:collect data to tuple
def print_args(*args):
    print('Positional argument tuple:',args)

def print_more(required1,required2,*args):
    print('Need this one:',required1)
    print('Need this one too:',required2)
    print('All the rest:',args)

# **:collect keyword parameters to dictionary
def print_kwargs(**kwargs):
    print('Keyword arguments:',kwargs)

# Notes
def echo(anything):
    'echo returns its input argument'
    return anything

def print_if_true(thing,check):
    '''
    Prints the first argument if a second argument is true.
    The operation is:
        1.Check whether the *second* argument is true.
        2.If it is, print the *first* argument.
    '''
    if check:
        print(thing)

# function
def answer():
    print(42)
def run_something(func):
    func()

def add_args(arg1,arg2):
    print(arg1+arg2)
def run_something_with_args(func,arg1,arg2):
    func(arg1,arg2)

def sum_args(*args):
    return sum(args)
def run_with_positional_args(func,*args):
    return func(*args)

# inner function
def outer(a,b):
    def inner(c,d):
        return c + d
    return inner(a,b)

def knights(saying):
    def inner(quote):
        return "We are the knights who say:'%s'" %quote
    return inner(saying)

def edit_story(words,func):
    for word in words:
        print(func(word))
stairs = ['thud','meow','thud','hiss']
def enliven(word):
    return word.capitalize() + '!'
edit_story(stairs,lambda word: word.capitalize() + '!')
