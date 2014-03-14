#!/usr/bin/env python
# coding=utf-8

# File   : compar3.py
# Author : Dominik R. Laetsch, dominik.laetsch at gmail dot com 

# # # # # 
# MODULES										
# # # # # 

from __future__ import division
import sys 

def read_fasta_to_dict (filename):
	with open(filename) as fh:
		fasta_dict = {}
		contig = ''
		seq = ''
		for line in fh:
		    line = line.rstrip("\n")
		    if line.startswith(">"):
		        fasta_dict[contig] = seq
		        seq = ''
		        contig = line[1:]
		    else:
		        seq += line
		fasta_dict[contig] = seq
	return fasta_dict

def read_blast_to_dict (filename):
	with open(filename) as fh:
		blast_dict = {}
		for line in fh:
			if line.startswith("contig"):
				temp_list = line.rstrip("\n").rsplit("\t")
				contig = temp_list[0]
				hit = temp_list[1:]
				if (contig in blast_dict):
					pass
				else:
					blast_dict[contig] = hit
	return blast_dict

if __name__ == "__main__":
	fasta_A = read_fasta_to_dict(sys.argv[1])
	fasta_B = read_fasta_to_dict(sys.argv[2])
	fasta_C = read_fasta_to_dict(sys.argv[3])
	blast_A_to_B = read_blast_to_dict(sys.argv[4])
	blast_B_to_A = read_blast_to_dict(sys.argv[5])
	blast_A_to_C = read_blast_to_dict(sys.argv[6])
	blast_C_to_A = read_blast_to_dict(sys.argv[7])
	blast_B_to_C = read_blast_to_dict(sys.argv[8])
	blast_C_to_B = read_blast_to_dict(sys.argv[9])

	count_A = len(fasta_A)
	count_B = len(fasta_B)
	count_C = len(fasta_C)

	A_hits_B = len(blast_A_to_B)
	B_hits_A = len(blast_B_to_A)
	A_hits_C = len(blast_A_to_C)
	C_hits_A = len(blast_C_to_A)
	B_hits_C = len(blast_B_to_C)
	C_hits_B = len(blast_C_to_B)

	A_in_B = 0
	A_not_in_B = 0
	A_in_C = 0
	A_not_in_C = 0
	B_in_A = 0
	B_not_in_A = 0
	B_in_C = 0
	B_not_in_C = 0
	C_in_A = 0
	C_not_in_A = 0
	C_in_B = 0
	C_not_in_B = 0

	for read in fasta_A:
		if read in A_hits_B:
			A_in_B += 1
		else:
			A_not_in_B += 1
		if read in A_hits_C:
			A_in_C += 1
		else:
			A_not_in_C += 1
	for read in fasta_B:
		if read in B_hits_A:
			B_in_A
		else:
			B_not_in_A += 1
		if read in B_hits_C:
			B_in_C
		else:
			B_not_in_C += 1
	for read in fasta_C:
		if read in C_hits_A:
			C_in_A
		else:
			C_not_in_A += 1
		if read in C_hits_B:
			C_in_B
		else:
			C_not_in_B += 1

	print "A : " + str(count_A)
	print "B : " + str(count_B)
	print "C : " + str(count_C)
	print "A_in_B" + str(A_in_B)
	print "A_not_in_B" + str(A_not_in_B)
	print "A_in_C" + str(A_in_C)
	print "A_not_in_C" + str(A_not_in_C)
	print "B_in_A" + str(B_in_A)
	print "B_not_in_A" + str(B_not_in_A)
	print "B_in_C" + str(B_in_C)
	print "B_not_in_C" + str(B_not_in_C)
	print "C_in_A" + str(C_in_A)
	print "C_not_in_A" + str(C_not_in_A)
	print "C_in_B" + str(C_in_B)
	print "C_not_in_B" + str(C_not_in_B)