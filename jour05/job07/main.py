def correction(liste):
    notes_arrondies = []
    for note in liste:
        if note < 40:
            notes_arrondies.append(note)
        else:
            difference = note % 5
            if difference >= 3:
                note_arrondie = note + (5 - difference)
            else:
                note_arrondie = note
            notes_arrondies.append(note_arrondie)
    return notes_arrondies


test = [24, 53, 71, 89, 23, 68]
notes_arrondies = correction(test)
print(notes_arrondies)