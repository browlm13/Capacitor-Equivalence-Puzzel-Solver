#python 3

"""
		Capacitor Equivalence Puzzel Solver

	You have an infinite supply of 5 microfarad capacitors.
	Create a circut out of wire and and these capacitors with an equivilent
	capacitance of 3 microfarads.
"""
import itertools

#
# Capacitor Equivalence Equations
#
def series(*capacitors):
	c_eq = 0
	for c in capacitors:
		c_eq += c**(-1)
	return c_eq**(-1) 

def parallel(*capacitors):
	return sum(capacitors)

# comparing floats with certain tolernce
def approximately_equal(a, b, rel_tol=1e-09, abs_tol=0.0):
    return abs(a-b) <= max(rel_tol * max(abs(a), abs(b)), abs_tol)

# generate permutations of size n, of ('P' and 'S')
def circut_strings(n):
	combinations = "PS" 	#P = Parallel, S = Series
	cs = []
	for p in itertools.product(combinations, repeat=n-1):
		cs.append(''.join(p))
	return cs

def calculate_equivalence(circut_strings, magic_value):
	eq = magic_value
	for c in circut_strings:
		if c == 'P': 
			eq = parallel(eq, magic_value)
		elif c == 'S': 
			eq = series(eq, magic_value)
	return eq

#return circut strings that match equivelence target within tolerence
def find_equivalent_solutions(magic_value, target_equivalence, max_depth, tolerance):
	solutions = []
	for i in range(2,max_depth+2):
		cs = circut_strings(i)
		for c in cs:
			eq = calculate_equivalence(c, magic_value)
			if abs(eq - target_equivalence) < tolerance:
				solutions.append(c)
	return solutions

#
#	Run Program
#
if __name__ == "__main__":

	# Magic Value (Capacitance of Infinite supply)
	magic = 5

	# Target Equicalence Value
	target = 3

	# Maximum Search Depth 
	max_depth = 4

	# Equivalence Tolerance 
	tolerance = .05

	# Solve And Display
	print(find_equivalent_solutions(magic,target,max_depth,tolerance))

