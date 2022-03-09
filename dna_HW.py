class Dna:
    def __init__(self, sequence):
        chunks = [x for x in sequence.strip().split('>') if x]
        names = []
        seqs = []
        for chunk in chunks:
            lines = chunk.splitlines()
            names.append(lines[0].strip())
            seqs.append(''.join(lines[1:]))
            self.sequence = dict(zip(names, seqs))

    def reverse_complemen(self, sequence):
        compl_dict = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
        return "".join(compl_dict[n] for n in reversed(sequence))

    def gc_content(self, sequence):
        G_count = sequence.count('G')
        C_count = sequence.count('C')
        Total_count = len(sequence)
        GC_Sum = int(G_count) + int(C_count)
        Percent_GC = GC_Sum / Total_count
        GC_total = (Percent_GC) * 100
        print(GC_total)

    def transcribe(self, sequence):
        rna = ''
        for i in sequence:
            if i == "T":
                rna += "U"
            else:
                rna += i
        print(rna)
