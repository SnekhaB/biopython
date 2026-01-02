# Practice Questions – Lesson 7 (Biopython) 


# Section A: Conceptual Questions (Short Answer)
"""
1) What is Biopython?
answer : Biopython is a python library that provides tools for computational biology and bioinformatics to read, analyse, process and manipulate biological data.

2) Why do we need Biopython when we already know Python?
answer : We need biopython because it provides specialized tools and functions specifically designed for biological data analysis

3) Write any two tasks that can be done easily using Biopython.
answer : transcription and translation

4) Which module is used to work with biological sequences in Biopython?
answer : Seq (sequence) module is used to work with biological sequences in Biopython
"""


# Section B: Installation & Basics
"""
5) Write the command used to install Biopython.
answer : pip install biopython

6) Write the Python statement used to import Seq from Biopython.
answer : from Bio.Seq import Seq
"""


# Section C: First Biopython Code 
"""
7) Write a Python program to:

- Import Seq from Biopython
- Create a DNA sequence "ATGCAA"
- Print the DNA sequence
"""
# answer :
from Bio.Seq import Seq

dna = Seq("ATGCAA")
print(dna)


# Section D: Working with Biological Intelligence
"""
8) Given the DNA sequence below using Biopython:

from Bio.Seq import Seq
dna = Seq("ATGCGT")

Write code to print:

- Complement of the DNA sequence
- Transcribed RNA sequence
- Translated protein sequence
"""
from Bio.Seq import Seq
dna = Seq("ATGCGT")

com_strand =dna.complement()
rna = dna.transcribe()
protein = dna.translate()

print(f"complementary strand of dna is {com_strand}")
print(f'RNA sequence of DNA {rna}')
print(f"Protein seq from the rna sequence {protein}")
# Section E: Output-Based Question
"""
9) Predict the output (do not run the code):

from Bio.Seq import Seq
dna = Seq("ATGC")
print(dna.complement())
"""

# answer : TACG


# Section F: Thinking Question (2–3 lines)
"""
10) Why is Biopython called a library that gives biological intelligence to Python?
"""

"""answer : Biopython is called a library that gives biological intelligence to Python because it provides bioinformatics tool and algorithms that enable
python to understand and analyse biological data."""