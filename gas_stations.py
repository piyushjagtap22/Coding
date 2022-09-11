gas = [1,2,3,4,5]
cost = [2,4,5,1,2]

def gas_station(gas,cost):
    tank = 0
    total = 0
    start = 0
    for i in range(len(gas)):
        tank = tank + gas[i] - cost[i]
        if tank < 0:
            start = i+1
            total = total + tank
            tank = 0
        # print(total,tank)
    if total + tank < 0:
        return -1
    else:
        return start


print(gas_station(gas, cost))