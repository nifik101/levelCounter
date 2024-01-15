import streamlit as st
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


def existing_level_1_used(items: List[int]) -> int:
    """
        existing_level_1_used beräknar hur många lvl 1 som redan finns totalt i listan av 'items'
        Itererar över [items] i en for-loop och anropar 'level_1_needed()' för att beräkna hur många level 1 som använts för varje item. 

        Args:
            items (List[int]): från input vilken level varje existerande item har.
        Returns:
            int: Summerat värde av totala antalet level 1 som redan finns i alla items.
    """
    total_used = 0

    for item in items:
        total_used += level_1_needed(item)

    return total_used


def run_app() -> None:
    st.title("Level 1 counter")

    target_level = st.number_input("Target level :dart:", min_value=1, max_value=20, value=4,
                                   help="Set target level, max value: 50")

    items_level_str = st.text_input("Existing items level, SEPERATE WITH ' , ' (comma) ")

    if st.button("Calculate"):
        items_list = [int(number) for number in items_level_str.split(",")] if items_level_str else []

        calculated_target_level = level_1_needed(target_level)
        calculated_items_total = existing_level_1_used(items_list)

        st.write(calculated_target_level - calculated_items_total)


if __name__ == "__main__":
    # run_app()
    print(type(existing_level_1_used([2,4,5])))
