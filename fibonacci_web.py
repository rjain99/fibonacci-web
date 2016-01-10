import web
import functools
from functools import wraps
from web import form
call_count=0
urls = (
  '/', 'fibonacci_web')

app = web.application(urls, globals())
render = web.template.render('templates/')

number_form = form.Form( 
    form.Textbox('number',
                 form.notnull,
                 form.regexp('^-?\d+$', 'Not a number.'),
                 form.Validator('Not greater than 0.', lambda x: int(x)>0),
                 description='How many fibonacci numbers do you want in the series ?:'
                 ))

def cached(func):
    func.cache = {}
    @wraps(func)
    def wrapper(*args):
        try:
            return func.cache[args]
        except KeyError:
            func.cache[args] = result = func(*args)
            return result   
    return wrapper

@cached
def fib(n):
    global call_count 
    call_count = call_count + 1
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

class fibonacci_web:
    global call_count 
    def GET(self):
        my_form = number_form()
        return render.fibonacci_web(my_form)

    def POST(self): 
        my_form = number_form() 
        if not my_form.validates(): 
            return render.fibonacci_web(my_form)
        else:
            number = my_form['number'].value
            string = ''
            for i in range(int(number)):
                string = string + `(fib(i))` + " " 
                # For debugging purposes, to make sure that recursive calls are being optimized
                #string = string + `(fib(i))` + " " +  "(" + str(call_count) + ")"
            return string


if __name__ == "__main__":
    app.run()
