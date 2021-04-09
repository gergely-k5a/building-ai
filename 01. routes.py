# Optimization

portnames = ["PAN", "AMS", "CAS", "NYC", "HEL"]

def permutations(route, ports):
  if len(ports) == 0:
    print(' '.join([portnames[i] for i in route]))
    return

  for i in range(len(ports)):
    permutations(route + [ports[i]], ports[:i] + ports[i+1:])


# this will start the recursion with 0 as the first stop
permutations([0], list(range(1, len(portnames))))