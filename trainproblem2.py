t_length=int(input("train length in m: "))
t_speed=int(input("train speed in kmph: "))
m_speed=int(input("man speed in kmph: "))
rs=(t_speed+m_speed)*5/18
t=t_length/rs
print("time",t)