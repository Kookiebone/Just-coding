print("Please, input there 3 arguments - a, b and c:")
a = float(input())
b = float(input())
c = float(input())
a1 = str(a)
b1 = str(b)
c1 = str(c)
if (a and b and c) != 0:
  print("Your equations seems:")
  print(a1+"*x² + "+b1+"*x + "+c1+" = 0")
  D = (b**2 - 4*a*c)
  x1 = (-b + D**0.5) / (a*2)
  x2 = (-b - D**0.5) / (a*2)
  print("Roots of this equation:")
  print(x1, x2)
if a == 0:
  print("Your quadratic equation:")
  print(b1+"*x + "+c1+" = 0")
  x = -c /b1
  print("Root of this equation:")
  print(x)
if b == 0:
  print("Your equation seems as following:")
  print(a1+"*x² + "+c1+" = 0")
  x1 = (-c)**0.5
  x2 = -(-c)**0.5
  print("Roots of this equation:")
  print(x1, x2)
if c == 0:
  print("Your equestion:")
  print(a1+"*x² + "+b1+"*x = 0")
  x1 = 0
  x2 = -b / a
  print("Roots of this equation:")
  print(x1, x2)
