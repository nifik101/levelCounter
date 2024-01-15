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
    """
        run_app Skapar Streamlit GUI och hanterar input/output av beräkning. 
    """
    st.title("Level 1 counter")

    target_level = st.number_input("Target level :dart:", min_value=1, max_value=50, value=4,
                                   help="Set target level, max value: 50")

    items_level_str = st.text_input("Existing items level, SEPERATE WITH ' , ' (comma) ")

    if st.button("Calculate"):
        try:
            items_list = [int(number) for number in items_level_str.split(",")] if items_level_str else []
        except ValueError:
            st.error("Ogiltig input: Ange endast siffror separerade med kommatecken, inga släpande kommatecken", icon="🙅")
            return

        calculated_target_level = level_1_needed(target_level)
        calculated_items_total = existing_level_1_used(items_list)
        total_level_1 = calculated_target_level - calculated_items_total

        if total_level_1 < 0: 
            st.warning("Bror, du har redan items för att nå din Target Level", icon="🙄")

        st.markdown(f"""
        ## 🌟 Nödvändiga Nivå 1: {total_level_1}

        ### 🎯 Målnivå: {target_level}

        ### 🧳 Värde existerande items: {calculated_items_total}

        För att nå din målnivå av **{target_level}**, behöver du samla ihop **{total_level_1}** nivå 1-poäng. 
        """, unsafe_allow_html=True)
        
        # st.markdown(f"""
        # <style>
        # .custom-style {{
        #     padding: 10px;
        #     background-color: #f0f2f6;
        #     border-radius: 10px;
        #     border: 2px solid #4e73df;
        #     color: #4e73df;
        #     font-family: Arial, sans-serif;
        #     text-align: center;
        # }}
        # </style>

        # <div class="custom-style">
        #     <h2>🎯 Målnivå: {target_level}</h2>
        #     <h3>🌟 Nödvändiga Nivå 1: {total_level_1}</h3>
        #     <p>För att nå din målnivå av <strong>{target_level}</strong>, behöver du samla ihop <strong>{total_level_1}</strong> nivå 1-poäng.</p>
        # </div>
        # """, unsafe_allow_html=True)


if __name__ == "__main__":
    run_app()