# Optimization - brute force

portnames = ["PAN", "AMS", "CAS", "NYC", "HEL"]

# https://sea-distances.org/
# nautical miles converted to km

D = [
        [0,8943,8019,3652,10545],
        [8943,0,2619,6317,2078],
        [8019,2619,0,5836,4939],
        [3652,6317,5836,0,7825],
        [10545,2078,4939,7825,0]
    ]

# https://timeforchange.org/co2-emissions-shipping-goods
# assume 20g per km per metric ton (of pineapples)

co2 = 0.020

# DATA BLOCK ENDS

smallest = None
bestroute = [0, 0, 0, 0, 0]

def permutations(route, ports):
    global smallest, bestroute

    if len(ports) == 0:
        emission = 0
        for n in range(len(route) - 1): emission = emission + D[route[n]][route[n+1]]
        if smallest is None or smallest > emission:
            smallest = emission
            bestroute = route
        return

    for i in range(len(ports)):
        permutations(route + [ports[i]], ports[:i] + ports[i+1:])

def main():
    # this will start the recursion
    permutations([0], list(range(1, len(portnames))))

    # print the best route and its emissions
    print(' '.join([portnames[i] for i in bestroute]) + " %.1f kg" % smallest)

main()