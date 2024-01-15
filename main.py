from typing import List


def level_1_needed(target_level: int) -> int:
    """
        level_1_needed beräkna hur många lvl 1 som behövs för att nå 'target_level'
        
        Args:
            target_level (int): Vilken nivå man vill nå. 
        Returns:
            int: Hur många lvl 1 items som behövs. 
    """
    return 2 ** (target_level - 1)


# level_1_needed(2)

def existing_level_1_used(items: List[int]) -> int:
    """
        existing_level_1_used beräknar hur många lvl 1 som behövs redan finns totalt i listan av 'items'
        Itererar över [items] i en for-loop och anropar 'level_1_needed()' för att beräkna hur många level 1 som använts för varje item. 
        Summerar ihop detta i 'total_used' vilket retuneras i funktionen 

        Args:
            items (List[int]): från input vilken level varje existerande item har 
        Returns:
            int: totala antalet level 1 som redan finns i alla items. 
    """
    total_used = 0

    for item in items:
        total_used += level_1_needed(item)

    return total_used


# existing_level_1_used([2,5,8])

