def proteins(strand): 
    acids = {
        'Methionine': ['AUG'],
        'Phenylalanine': ['UUU', 'UUC'],
        'Leucine': ['UUA', 'UUG'],
        'Serine': ['UCU', 'UCC', 'UCA', 'UCG'],
        'Tyrosine': ['UAU', 'UAC'],
        'Cysteine': ['UGU', 'UGC'],
        'Tryptophan': ['UGG'],
        'STOP': ['UAA', 'UAG', 'UGA']
        }

    data =[(strand[i:i+3]) for i in range(0, len(strand),3)]
    result = list()
    for d in data:
        for key,value in acids.items():
            if d in value:
                if key == 'STOP':
                    return result
                else:
                    result.append(key)
    return result
    
