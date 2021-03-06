seq = "ISYIDAIIVRKIQVRWNRTDIYNKWHTTQCTKAYYWPIVHHDLCFNPVFAGQWSQVHLKMDPLIIQDNSWECTKMQSENSGCYATCSTPPHSEAPGIVKMWDIKACLALAILPLLQYIDKKLIVFCFWCDDWVWYCVSITQTWADKQKPASQVQPFRLDEPHNGSCEPYATKRYKAYHLTMYHQSWWDGTERDAFLTNDSFNRDHCVVRQQLVEDQTNWDDNKDHFMRWQMIPVGVHGLQATYIMHQAWISTQFVTDTQGWKVLMGKYNDYVQFEKYCKDDCITASQLATYNVTYEKTYWRCFNCNHIGKKMWWPQWIPEDLTNEARGDRELHDGEWMQLNMSYFEEGFHQSTLCHHWDVCNLECVQPNTYYYACIFLYRMKVCFFWLFGGIFAAIKPYKDNVEDKDSCKAHGKSSFYSSFCCEMGPYWTHTERVVRPTEIVTFHWQKKIWYLRIFRCNCNFFGDGGGLEGSEEFNTDFHPHQHKNCRRHLDHVGHWRDRFNAGCYLIGEYPCSWENYSHWHNLYGHQPDQTMAPGHCGCCGQVCSICLQAEFMSIKQIDGERWKDINTTVGFYENWEHYCWYHEEAGWVAQRIAAYNGSAHKQHIWCGHACPLQERYTMFDYLYAIEWKCRDKVVLCYFECFCSECQPNAYGGWAIHDWIIWMPFQPDICCAWDRQMRETIINSKNGTVNPLCPICHHVCYWKHDFAMDEEKPGVQGVSDSKYRKPNNQQKAWGQCFSFYKNLQSWVLIMQADMTSFHNLQPAIWAQSFSFKVQPEMFGHWDDGKLTFFDSRPATSMILWWYFLTKMWPHRHFHAPRQPPTHGEWVDCWARSQWCWEEMHWPLTAKSTEINQEDWMMLGKRNTELKITQLIMIVIGKKPKDGEDSHDPFKPMHGPMWKVRPDHSDSTCNLLQQSGYQKCYRVAKCVHFRYNLGECCKFSFHDQQPIAWVRSCPFYIANCAISHNHTGEAQQK"

amino_acid_mass = {"A" : 71.03711,
                   "C" : 103.00919,
                   "D" : 115.02694,
                   "E" : 129.04259,
                   "F" : 147.06841,
                   "G" : 57.02146,
                   "H" : 137.05891,
                   "I" : 113.08406,
                   "K" : 128.09496,
                   "L" : 113.08406,
                   "M" : 131.04049,
                   "N" : 114.04293,
                   "P" : 97.05276,
                   "Q" : 128.05858,
                   "R" : 156.10111,
                   "S" : 87.03203,
                   "T" : 101.04768,
                   "V" : 99.06841,
                   "W" : 186.07931,
                   "Y" : 163.06333}

def Protein_MW_Calc(Sequence) :
    #given a protein sequence, calculate molecular weight
    total_mass = 0
    for residue in Sequence :
        mass = amino_acid_mass.get(residue)
        total_mass += mass
    print(round(total_mass, 3))

Protein_MW_Calc(seq)
