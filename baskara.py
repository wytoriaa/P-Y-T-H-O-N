a, b, c = input().split()
a = float(a)
b = float(b)
c = float(c)

delta = (b**2)-4*c*a

if delta >= 0 or a != 0:

    r1 = (-b - delta*0.5)/2*a
    r2 = (-b + delta*0.5)/2*a

    print('R1 = {:.5f}\n'.format(r1), 'R2 = {:.5f}'.format(r2))

else:
    print('Impossivel calcular')
    