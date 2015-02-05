from __future__ import division

def get_at_content(dna):
	length = len(dna)
	a_count = dna.count('A')
	t_count = dna.count ('T')
	at_content = (a_count + t_count) / length
	return at_content

my_at_content = get_at_content("ATTTGGGCCCCCTTTCCC")
print(str(my_at_content))
print(get_at_content("ATTTGGGCCCCCTTTGGG"))
print(get_at_content("aatttttcccccgggggga"))
