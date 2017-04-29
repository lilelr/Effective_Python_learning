def reminder(number, divisor):
    return number % divisor


assert reminder(20, 7) == 6

print(reminder(20, divisor=7))
reminder(number=20, divisor=7)
reminder(divisor=7, number=20)


def flow_rate(weight_diff, time_diff, period=1, units_per_kg=1):
    return ((weight_diff / units_per_kg) / time_diff * period)


weight_diff = 0.5
time_diff = 3
# The best practice is to always specify optional arguments
# using the keyword names and never pass them as positional arguments.
pounds_per_hour = flow_rate(weight_diff, time_diff, period=3600, units_per_kg=22)

pounds_per_hour2 = flow_rate(weight_diff, time_diff, 3600, 22)
print(pounds_per_hour2)
