full_dot = '●'
empty_dot = '○'
def create_character(name,strength,intelligence,charisma):
    if not isinstance(name,str):
        return "The character name should be a string"
    if not name:
        return "The character should have a name"
    if len(name)>10:
        return "The character name is too long"
    if " " in name:
        return "The character name should not contain spaces"
    if not all(isinstance(stat, int) for stat in [strength, charisma, intelligence]):
        return "All stats should be integers"
    if any(stat<1 for stat in [strength, charisma, intelligence]):
        return "All stats should be no less than 1"
    if any(stat>4 for stat in [strength, charisma, intelligence]):
        return "All stats should be no more than 4"
    if strength+intelligence+charisma !=7:
        return "The character should start with 7 points"
    max_length=10
    
    return (
        f"{name}\n"
        f"STR {'●' * strength + '○' * (max_length - strength)}\n"
        f"INT {'●' * intelligence + '○' * (max_length - intelligence)}\n"
        f"CHA {'●' * charisma + '○' * (max_length - charisma)}"
    )
print(create_character('ren',4,2,1))
