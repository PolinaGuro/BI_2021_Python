class Rna:
    def __init__(self, sequence):
        title = [x for x in sequence.strip().split('>') if x]
        names = []
        seqs = []
        for i in title:
            lines = title.splitlines()
            names.append(lines[0].strip())
            seqs.append(''.join(lines[1:]))
            self.suquence = dict(zip(names, seqs))

    def reverse_complement(self, sequence):
        compl_dict = {'A': 'U', 'C': 'G', 'G': 'C', 'U': 'A'}
        return "".join(compl_dict[n] for n in reversed(sequence))

    def gc_content(self, sequence):
        G_count = sequence.count('G')
        C_count = sequence.count('C')
        Total_count = len(self.sequence)
        GC_Sum = int(G_count) + int(C_count)
        Percent_GC = GC_Sum / Total_count
        GC_total = (Percent_GC) * 100
        print(GC_total)
