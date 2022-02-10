d = int(input())
c = int(input())

ticks = 12000
minutos_por_dia =180
min_ticks = 20


total_tick_dias = d * (minutos_por_dia/ min_ticks * ticks)
tick_per_house = (total_tick_dias/c)
print(int(tick_per_house))
