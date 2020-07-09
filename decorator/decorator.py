from functools import wraps

def camel_case(func):
  @wraps(func)
  def wrapper(*args, **kwargs):
    returned_string = func(*args, **kwargs)
    camel_case_string = ''
    i = 0
    while i <= len(returned_string) - 1:
      if not i % 2:
        camel_case_string += returned_string[i].upper()
      else:
        camel_case_string += returned_string[i].lower()
      i += 1
    return camel_case_string
  return wrapper

@camel_case
def print_string(string):
  return string

print(print_string("Welcome to my nightmare!"))
